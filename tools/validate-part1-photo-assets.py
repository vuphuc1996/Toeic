#!/usr/bin/env python3
"""Validate locally hosted Listening Part 1 photos and consolidated asset provenance.

Supports third-party licensed stock photos and project-generated AI images without
misclassifying one source type as the other. Strict by default for CI/release.
"""
from __future__ import annotations
import argparse
import csv
import json
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATTRIBUTION = ROOT / "assets/listening/ATTRIBUTION.csv"
LIBRARY = ROOT / "data/listening/listening-library.json"
MIN_WIDTH = 1280
MIN_HEIGHT = 960
SOF_MARKERS = {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}


def jpeg_dimensions(path: Path) -> tuple[int, int]:
    """Return (width, height) from a JPEG SOF segment; reject malformed/non-JPEG files."""
    data = path.read_bytes()
    if len(data) < 4 or data[:3] != b"\xff\xd8\xff":
        raise ValueError("missing JPEG SOI signature")
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        while i < len(data) and data[i] == 0xFF:
            i += 1
        if i >= len(data):
            break
        marker = data[i]
        i += 1
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7 or marker == 0x01:
            continue
        if i + 2 > len(data):
            break
        length = struct.unpack_from(">H", data, i)[0]
        if length < 2 or i + length > len(data):
            raise ValueError("invalid JPEG segment length")
        if marker in SOF_MARKERS:
            if length < 7:
                raise ValueError("invalid JPEG SOF segment")
            height, width = struct.unpack_from(">HH", data, i + 3)
            if width <= 0 or height <= 0:
                raise ValueError("invalid JPEG dimensions")
            return width, height
        i += length
    raise ValueError("JPEG has no supported Start Of Frame segment")


def validate(allow_missing: bool = False) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        library = json.loads(LIBRARY.read_text(encoding="utf-8"))
        part1 = [row for row in library["listening"] if row.get("part") == "Part 1"]
    except Exception as exc:  # noqa: BLE001
        return [f"Cannot read listening library: {exc}"], [], 0
    try:
        with ATTRIBUTION.open(encoding="utf-8-sig", newline="") as handle:
            attribution_rows = list(csv.DictReader(handle))
    except Exception as exc:  # noqa: BLE001
        return [f"Cannot read attribution CSV: {exc}"], [], 0

    if len(part1) < 8:
        errors.append(f"Expected at least 8 Part 1 items, found {len(part1)}")
    p1_ids = {row.get("id") for row in part1}
    attr_ids = {row.get("question_id") for row in attribution_rows}
    if p1_ids != attr_ids:
        errors.append(f"Attribution IDs differ from Part 1 IDs (missing={sorted(p1_ids-attr_ids)}, extra={sorted(attr_ids-p1_ids)})")
    if len(attribution_rows) != len(part1):
        errors.append(f"Expected {len(part1)} attribution rows, found {len(attribution_rows)}")
    attr_by_id = {row.get("question_id"): row for row in attribution_rows}

    valid_files = 0
    photo_count = len(part1)
    for item in part1:
        ident = item.get("id", "?")
        photo = item.get("photo", "")
        if not photo.startswith("./assets/listening/") or not photo.lower().endswith(".jpg"):
            errors.append(f"{ident}: photo path must be a local ./assets/listening/*.jpg path")
            continue
        filename = Path(photo[2:]).name
        row = attr_by_id.get(ident)
        if not row:
            errors.append(f"{ident}: missing attribution row")
            continue
        if row.get("filename") != filename:
            errors.append(f"{ident}: data path and attribution filename do not match")
        source_type = (row.get("source_type") or "licensed-stock").strip().lower()
        item_source_type = str(item.get("photoSourceType") or "").strip().lower()
        if item_source_type and item_source_type != source_type:
            errors.append(f"{ident}: Listening photoSourceType {item_source_type!r} does not match ATTRIBUTION.csv source_type {source_type!r}")
        provider = row.get("provider", "").strip()
        usage_basis = row.get("usage_basis", "").strip()
        if not row.get("photographer", "").strip():
            errors.append(f"{ident}: photographer/creator field is missing")
        if source_type == "licensed-stock":
            if "pexels.com/photo/" not in row.get("source_page", ""):
                errors.append(f"{ident}: licensed-stock source page is not a Pexels photo page")
            if "pexels.com/license" not in row.get("license", ""):
                errors.append(f"{ident}: licensed-stock license URL is missing or not Pexels")
            if provider and provider.casefold() != "pexels":
                errors.append(f"{ident}: current licensed-stock provider must be Pexels")
        elif source_type == "ai-generated":
            if not provider:
                errors.append(f"{ident}: AI-generated provider is missing")
            if "AI-generated" not in row.get("license", ""):
                errors.append(f"{ident}: AI-generated asset must be explicitly labelled in license/usage field")
            if "not an external stock" not in row.get("source_page", ""):
                errors.append(f"{ident}: AI-generated source must not be represented as a stock-photo URL")
            if not usage_basis:
                errors.append(f"{ident}: AI-generated usage basis is missing")
            if "pexels.com" in row.get("license", "").lower():
                errors.append(f"{ident}: AI-generated asset cannot be labelled as Pexels-licensed")
        else:
            errors.append(f"{ident}: unsupported source_type {source_type!r}")
        file_path = ROOT / photo[2:]
        if not file_path.is_file():
            message = f"{ident}: missing photo bytes ({photo})"
            if allow_missing:
                warnings.append(message)
            else:
                errors.append(message)
            continue
        try:
            width, height = jpeg_dimensions(file_path)
            if width < MIN_WIDTH or height < MIN_HEIGHT:
                errors.append(f"{ident}: photo is too small ({width}x{height}); minimum is {MIN_WIDTH}x{MIN_HEIGHT}")
            else:
                valid_files += 1
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{ident}: invalid JPEG ({exc})")
    return errors, warnings, valid_files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-missing", action="store_true", help="warn rather than fail when photo binaries are absent")
    args = parser.parse_args()
    errors, warnings, valid_files = validate(args.allow_missing)
    library = json.loads(LIBRARY.read_text(encoding="utf-8"))
    photo_count = sum(row.get("part") == "Part 1" for row in library["listening"])
    print(f"Part 1 photo files valid: {valid_files}/{photo_count}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: Part 1 records and mixed-source attribution rows checked; {len(warnings)} missing photo warning(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
