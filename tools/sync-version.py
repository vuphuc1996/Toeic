#!/usr/bin/env python3
"""Keep every version string in the project equal to data/manifest.json -> version.

  python tools/sync-version.py --check     list every place that disagrees (exit 1 if any)
  python tools/sync-version.py --dry-run   show the exact edits --apply would make (writes nothing)
  python tools/sync-version.py --apply     write the edits, then re-run --check
  python tools/sync-version.py --set 2.9.8 --apply   first set manifest version, then sync

Safety rules
  * Only the registered markers below are touched; no blind search/replace of version-like text.
  * Every marker must match EXACTLY once. A missing or duplicated marker stops the run (exit 2)
    before any file is written.
  * CHANGELOG.md is check-only: the changelog must contain a heading for the current version, but
    its history is never rewritten.
Exit codes: 0 ok, 1 versions disagree (check) or post-apply check failed, 2 marker/structure problem.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

SEMVER = r"\d+\.\d+\.\d+"


@dataclass(frozen=True)
class Marker:
    name: str
    file: str
    patterns: tuple[str, ...]  # alternatives: exactly ONE must match, exactly once; group 1 = version
    apply: bool = True


MARKERS: tuple[Marker, ...] = (
    Marker("sw.js version", "sw.js", (
        rf"const VERSION = '({SEMVER})';",                              # v2.9.8+ layout
        rf"CACHE_NAME = 'toeic-vocab-github-only-v({SEMVER})';",         # v2.9.7 layout
    )),
    Marker("index.html <title>", "index.html", (rf"<title>TOEIC Dictionary v({SEMVER}) ",)),
    Marker("index.html sidebar", "index.html", (rf'<div class="sidebar-version">Phase 5 · v({SEMVER}) · GitHub-only</div>',)),
    Marker("index.html phase-note", "index.html", (rf"<strong>GitHub-only v({SEMVER}):</strong>",)),
    Marker("index.html footer", "index.html", (rf"<span>GitHub-only · v({SEMVER})</span>",)),
    Marker("README.md title", "README.md", (rf"\A# TOEIC Dictionary v({SEMVER})",)),
    Marker("MASTER_STATUS.md version line", "MASTER_STATUS.md",
           (rf"\*\*Phiên bản mã nguồn đang kiểm kê:\*\* v({SEMVER})",)),
)
CHANGELOG = "CHANGELOG.md"


class StructureError(Exception):
    pass


def read_raw(path: Path) -> str:
    """Read without newline translation so CRLF/LF files are written back unchanged."""
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def read_manifest_version(root: Path) -> str:
    path = root / "data" / "manifest.json"
    try:
        version = json.loads(path.read_text(encoding="utf-8"))["version"]
    except Exception as exc:  # noqa: BLE001
        raise StructureError(f"không đọc được version từ {path}: {exc}") from exc
    if not (isinstance(version, str) and re.fullmatch(SEMVER, version)):
        raise StructureError(f"manifest version phải dạng x.y.z, hiện là {version!r}")
    return version


def locate(root: Path, marker: Marker, texts: dict[str, str]) -> tuple[str, re.Match]:
    path = root / marker.file
    if not path.exists():
        raise StructureError(f"{marker.name}: không có file {marker.file}")
    if marker.file not in texts:
        texts[marker.file] = read_raw(path)
    text = texts[marker.file]
    found: list[tuple[str, re.Match]] = []
    for pattern in marker.patterns:
        matches = list(re.finditer(pattern, text, re.M))
        if len(matches) > 1:
            raise StructureError(f"{marker.name}: marker xuất hiện {len(matches)} lần (cần đúng 1): {pattern}")
        found.extend((pattern, m) for m in matches)
    if not found:
        raise StructureError(f"{marker.name}: không tìm thấy marker trong {marker.file}")
    if len(found) > 1:
        raise StructureError(f"{marker.name}: nhiều kiểu marker cùng khớp trong {marker.file}")
    return found[0]


def survey(root: Path, expected: str) -> tuple[list[dict], dict[str, str]]:
    texts: dict[str, str] = {}
    rows = []
    for marker in MARKERS:
        _, m = locate(root, marker, texts)
        rows.append({"marker": marker, "found": m.group(1), "span": m.span(1), "ok": m.group(1) == expected})
    return rows, texts


def check_changelog(root: Path, expected: str) -> tuple[bool, str]:
    path = root / CHANGELOG
    if not path.exists():
        return False, f"không có {CHANGELOG}"
    text = path.read_text(encoding="utf-8")
    versions = re.findall(rf"^##\s+v?({SEMVER})\b", text, re.M)
    if expected in versions:
        return True, f"{CHANGELOG}: có mục cho {expected}"
    return False, f"{CHANGELOG}: chưa có mục '## v{expected}' (các mục hiện có: {', '.join(versions) or 'không có'})"


def atomic_write(path: Path, text: str) -> None:
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def set_manifest_version(root: Path, new_version: str, write: bool) -> str:
    path = root / "data" / "manifest.json"
    text = read_raw(path)
    matches = list(re.finditer(rf'("version"\s*:\s*")({SEMVER})(")', text))
    if len(matches) != 1:
        raise StructureError(f'manifest.json: khóa "version" xuất hiện {len(matches)} lần (cần đúng 1)')
    m = matches[0]
    updated = text[:m.start(2)] + new_version + text[m.end(2):]
    if write:
        atomic_write(path, updated)
    return m.group(2)


def report(rows: list[dict], expected: str, changelog: tuple[bool, str]) -> int:
    bad = 0
    print(f"Phiên bản chuẩn (data/manifest.json): {expected}")
    for row in rows:
        mark = "OK  " if row["ok"] else "LỆCH"
        print(f"  [{mark}] {row['marker'].name}: {row['found']}" + ("" if row["ok"] else f"  (cần {expected})"))
        bad += not row["ok"]
    print(f"  [{'OK  ' if changelog[0] else 'LỆCH'}] {changelog[1]}")
    bad += not changelog[0]
    return bad


def run(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    ap.add_argument("--set", metavar="X.Y.Z", help="đặt version trong manifest trước (cần --apply hoặc --dry-run)")
    args = ap.parse_args(argv)
    root = args.root.resolve()
    apply = args.apply
    dry = args.dry_run

    try:
        if args.set:
            if not re.fullmatch(SEMVER, args.set):
                raise StructureError(f"--set cần dạng x.y.z, nhận {args.set!r}")
            if not (apply or dry):
                raise StructureError("--set chỉ dùng cùng --apply hoặc --dry-run")
            old = read_manifest_version(root)
            # validate all markers BEFORE touching the manifest
            survey(root, args.set)
            set_manifest_version(root, args.set, write=apply)
            print(f"manifest version: {old} -> {args.set}" + ("" if apply else "  (dry-run, chưa ghi)"))
            expected = args.set
        else:
            expected = read_manifest_version(root)
        rows, texts = survey(root, expected)
    except StructureError as exc:
        print(f"ERROR: {exc}")
        print("Dừng: chưa ghi file nào.")
        return 2

    changelog = check_changelog(root, expected)
    if not (apply or dry):
        bad = report(rows, expected, changelog)
        print("RESULT: " + ("PASS — mọi vị trí đồng bộ" if not bad else f"FAILED — {bad} vị trí lệch"))
        return 0 if not bad else 1

    # dry-run / apply: compute edits (marker spans are non-overlapping per file)
    edits: dict[str, list[tuple[int, int, str]]] = {}
    for row in rows:
        if row["ok"]:
            continue
        s, e = row["span"]
        edits.setdefault(row["marker"].file, []).append((s, e, row["found"]))
    if not edits:
        print("Không có gì cần sửa.")
    for file, items in edits.items():
        for s, e, old in items:
            print(f"  {file}: {old} -> {expected}")
    if dry:
        print("DRY-RUN: chưa ghi file nào.")
        return 0
    for file, items in edits.items():
        text = texts[file]
        for s, e, _old in sorted(items, reverse=True):
            text = text[:s] + expected + text[e:]
        atomic_write(root / file, text)
    # re-check
    rows2, _ = survey(root, expected)
    bad = sum(not r["ok"] for r in rows2)
    print(f"Đã ghi {len(edits)} file." if edits else "Không ghi file nào.")
    if not changelog[0]:
        print(f"LƯU Ý: {changelog[1]} (CHANGELOG không được script sửa; thêm mục thủ công)")
    if bad:
        print(f"FAILED — sau apply còn {bad} vị trí lệch")
        return 1
    return 0 if changelog[0] else 1


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
