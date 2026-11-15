#!/usr/bin/env python3
"""Fail-closed fingerprint refresh for the approved removal of Part 1 SVG fallback metadata.

This changes only the eight historical unitContentSha256 values after proving that
restoring the exact old image=./assets/listening/<unitId>.svg metadata reproduces
the currently certified digest. Question objects and questionSha256 values must
remain unchanged. The operation appends a separate audit entry; it never rewrites
or deletes prior fingerprint history.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "tools/remaining-content-review-v2.19.0.json"
LISTENING_PATH = ROOT / "data/listening/listening-library.json"
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
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    listening_doc = json.loads(LISTENING_PATH.read_text(encoding="utf-8"))
    units = {unit["id"]: unit for unit in listening_doc["listening"]}
    rows = [
        row for row in registry["items"]
        if row.get("collection") == "listening" and row.get("part") == "Part 1"
    ]
    row_units = {row["unitId"] for row in rows}
    if len(rows) != 8 or row_units != EXPECTED_UNITS:
        raise SystemExit(
            f"ABORT: expected exactly 8 reviewed Part 1 rows; found {len(rows)} rows / {len(row_units)} units"
        )

    prior_logs = registry.get("fingerprintRefreshLog", [])
    if len(prior_logs) != 1 or prior_logs[0].get("fieldAdded") != "photoSourceType":
        raise SystemExit("ABORT: expected exactly one preserved photoSourceType refresh entry")

    changes = []
    for row in rows:
        unit_id = row["unitId"]
        unit = units.get(unit_id)
        if not unit:
            raise SystemExit(f"ABORT: missing listening unit {unit_id}")
        if "image" in unit:
            raise SystemExit(f"ABORT: {unit_id} still has an image fallback field")
        expected_photo = f"./assets/listening/{unit_id}.jpg"
        if unit.get("photo") != expected_photo:
            raise SystemExit(f"ABORT: {unit_id} photo path differs from expected JPG path")
        if unit.get("photoSourceType") != "licensed-stock":
            raise SystemExit(f"ABORT: {unit_id} licensed photo metadata is missing")

        current_payload = {key: value for key, value in unit.items() if key != "questions"}
        old_payload = dict(current_payload)
        old_payload["image"] = f"./assets/listening/{unit_id}.svg"
        old_hash = row["unitContentSha256"]
        if digest(old_payload) != old_hash:
            raise SystemExit(
                f"ABORT: {unit_id} differs from the certified hash for a reason beyond removal of its SVG fallback field"
            )

        question = unit.get("questions", [])[row["questionNumber"] - 1]
        if digest(question) != row["questionSha256"]:
            raise SystemExit(f"ABORT: reviewed question hash changed for {row['key']}")

        new_hash = digest(current_payload)
        changes.append({
            "unitId": unit_id,
            "oldUnitContentSha256": old_hash,
            "newUnitContentSha256": new_hash,
            "oldHashMatchesAfterRestoringField": True,
            "questionSha256Unchanged": True,
        })

    change_by_id = {item["unitId"]: item for item in changes}
    for row in rows:
        row["unitContentSha256"] = change_by_id[row["unitId"]]["newUnitContentSha256"]

    prior_logs.append({
        "date": date.today().isoformat(),
        "reason": "Approved metadata-only removal of the obsolete Part 1 SVG fallback after the runtime and all nine Part 1 records were switched to JPG-only",
        "approvalContext": "The user explicitly requested removal of obsolete SVG files because the application now uses JPG, in the 2026-11-15 conversation",
        "scope": "unitContentSha256 only; no photo JPG paths, photoSourceType, questions, transcripts, translations, titles, choices, answer keys, ordering, or review decisions changed",
        "fieldRemoved": "image",
        "expectedRemovedValuePattern": "./assets/listening/<unitId>.svg",
        "changedUnitCount": len(changes),
        "units": changes,
    })
    registry["fingerprintRefreshLog"] = prior_logs
    REGISTRY_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"PASS: refreshed {len(changes)} Part 1 metadata fingerprints after verified SVG fallback-field removal")
    print("PASS: all eight previous hashes reproduced by restoring only the exact image SVG field")
    print("PASS: all eight reviewed question hashes unchanged")
    for item in changes:
        print(f"{item['unitId']}: {item['oldUnitContentSha256']} -> {item['newUnitContentSha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
