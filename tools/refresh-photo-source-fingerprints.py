#!/usr/bin/env python3
"""Refresh the historical Part 1 unit fingerprints for one verified metadata-only field.

The tool is intentionally narrow and fail-closed. It writes nothing unless all 8
Part 1 records match their old unit hash after removing only photoSourceType, all
question hashes still match, and the expected licensed-stock marker is present.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "tools/remaining-content-review-v2.19.0.json"
LISTENING_PATH = ROOT / "data/listening/listening-library.json"
FIELD = "photoSourceType"
EXPECTED_VALUE = "licensed-stock"
EXPECTED_UNITS = {
    "part1-meeting-documents",
    "part1-warehouse-box",
    "part1-technician-inspection",
    "part1-airport-suitcase",
    "part1-presentation-room",
    "part1-reception-plant",
    "part1-restaurant-setting",
    "part1-photocopier",
}


def digest(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    listening_doc = json.loads(LISTENING_PATH.read_text(encoding="utf-8"))
    units = {unit["id"]: unit for unit in listening_doc["listening"]}
    rows = [row for row in registry["items"] if row.get("collection") == "listening" and row.get("part") == "Part 1"]
    row_units = {row["unitId"] for row in rows}

    if len(rows) != 8 or row_units != EXPECTED_UNITS:
        raise SystemExit(f"ABORT: expected exactly 8 reviewed Part 1 units; found {len(rows)} rows / {len(row_units)} units")
    if registry.get("fingerprintRefreshLog"):
        raise SystemExit("ABORT: a fingerprintRefreshLog already exists; inspect it before attempting another refresh")

    changes = []
    for row in rows:
        unit_id = row["unitId"]
        unit = units.get(unit_id)
        if not unit or unit.get(FIELD) != EXPECTED_VALUE:
            raise SystemExit(f"ABORT: {unit_id} is missing the expected {FIELD}={EXPECTED_VALUE!r}")
        unit_payload = {key: value for key, value in unit.items() if key != "questions"}
        unit_payload_without_field = {key: value for key, value in unit_payload.items() if key != FIELD}
        old_hash = row["unitContentSha256"]
        if digest(unit_payload_without_field) != old_hash:
            raise SystemExit(f"ABORT: {unit_id} differs from the old fingerprint for a reason beyond {FIELD}")

        question = unit.get("questions", [])[row["questionNumber"] - 1]
        if digest(question) != row["questionSha256"]:
            raise SystemExit(f"ABORT: question hash changed for {row['key']}")
        new_hash = digest(unit_payload)
        changes.append({
            "unitId": unit_id,
            "oldUnitContentSha256": old_hash,
            "newUnitContentSha256": new_hash,
            "oldHashMatchesAfterRemovingField": True,
            "questionSha256Unchanged": True,
        })

    # All preconditions have passed; now make the narrow update and keep a trace.
    by_unit = {change["unitId"]: change for change in changes}
    for row in rows:
        row["unitContentSha256"] = by_unit[row["unitId"]]["newUnitContentSha256"]
    registry["fingerprintRefreshLog"] = [{
        "date": date.today().isoformat(),
        "reason": "Metadata-only addition of photoSourceType to the eight reviewed Listening Part 1 units",
        "approvalContext": "The user instructed continuation after fixing the listed issues in the 2026-11-15 conversation",
        "scope": "unitContentSha256 only; no question hashes, transcripts, translations, titles, choices, answer keys, ordering, or review decisions changed",
        "fieldAdded": FIELD,
        "expectedFieldValue": EXPECTED_VALUE,
        "changedUnitCount": len(changes),
        "units": changes,
    }]
    REGISTRY_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: refreshed {len(changes)} metadata fingerprints; all old hashes matched after removing only {FIELD}; all question hashes unchanged")
    for change in changes:
        print(f"{change['unitId']}: {change['oldUnitContentSha256']} -> {change['newUnitContentSha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
