"""Shared reconstruction helpers for historical Related Glossary regression tests."""
from __future__ import annotations
import copy
import json
from pathlib import Path



def restore_batch_047(glossary: dict, root: Path) -> dict:
    """Reverse Batch 047, restoring the Related Glossary to its v2.95.72 state."""
    restored = copy.deepcopy(glossary)
    patch_path = root / 'patches-related-terms/v2.95.74/related-terms-047.json'
    patch = json.loads(patch_path.read_text(encoding='utf-8'))
    by_key = {row['term'].casefold(): row for row in restored['terms']}
    for operation in patch['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = copy.deepcopy(old_value)
    return restored



def restore_batch_046(glossary: dict, root: Path) -> dict:
    """Reverse Batch 046 after reversing Batch 047, restoring the Related Glossary to its v2.95.71 state."""
    restored = restore_batch_047(glossary, root)
    patch_path = root / 'patches-related-terms/v2.95.72/related-terms-046.json'
    patch = json.loads(patch_path.read_text(encoding='utf-8'))
    by_key = {row['term'].casefold(): row for row in restored['terms']}
    for operation in patch['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = copy.deepcopy(old_value)
    return restored


def restore_batch_045(glossary: dict, root: Path) -> dict:
    """Reverse Batch 045 after reversing Batch 046, restoring the v2.95.70 state."""
    restored = restore_batch_046(glossary, root)
    patch_path = root / 'patches-related-terms/v2.95.71/related-terms-045.json'
    patch = json.loads(patch_path.read_text(encoding='utf-8'))
    by_key = {row['term'].casefold(): row for row in restored['terms']}
    for operation in patch['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = copy.deepcopy(old_value)
    return restored


def restore_batch_044(glossary: dict, root: Path) -> dict:
    """Return a copy of the glossary as it existed immediately before Batch 044.

    The current release includes Batch 045, so reverse it before reversing Batch 044.
    """
    restored = restore_batch_045(glossary, root)
    patch_path = root / 'patches-related-terms/v2.95.69/related-terms-044.json'
    patch = json.loads(patch_path.read_text(encoding='utf-8'))
    by_key = {row['term'].casefold(): row for row in restored['terms']}
    for operation in patch['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = copy.deepcopy(old_value)
    return restored


def restore_batch_039(glossary: dict, root: Path) -> dict:
    """Return a copy of the glossary as it existed immediately before batch 039."""
    restored = restore_batch_044(glossary, root)
    by_key = {row['term'].casefold(): row for row in restored['terms']}
    # Reverse Batch 044 first, then later batches in descending order before Batch 039. This keeps
    # historical reconstruction deterministic as the source advances.
    batch_043_path = root / 'patches-related-terms/v2.95.62/related-terms-043.json'
    batch_043 = json.loads(batch_043_path.read_text(encoding='utf-8'))
    for operation in batch_043['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = old_value
    batch_042_path = root / 'patches-related-terms/v2.95.61/related-terms-042.json'
    batch_042 = json.loads(batch_042_path.read_text(encoding='utf-8'))
    for operation in batch_042['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = old_value
    batch_041_path = root / 'patches-related-terms/v2.95.52/related-terms-041.json'
    batch_041 = json.loads(batch_041_path.read_text(encoding='utf-8'))
    for operation in batch_041['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = old_value
    batch_040_path = root / 'patches-related-terms/v2.95.51/related-terms-040.json'
    batch_040 = json.loads(batch_040_path.read_text(encoding='utf-8'))
    for operation in batch_040['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = old_value
    patch_path = root / 'patches-related-terms/v2.95.50/related-terms-039.json'
    patch = json.loads(patch_path.read_text(encoding='utf-8'))
    by_key = {row['term'].casefold(): row for row in restored['terms']}
    for operation in patch['operations']:
        row = by_key[operation['term'].casefold()]
        for field, old_value in operation['expect'].items():
            if field == 'term':
                continue
            if old_value is None:
                row.pop(field, None)
            else:
                row[field] = old_value
        for field in operation['set']:
            if field not in operation['expect']:
                row.pop(field, None)
    return restored


def reverse_batch_027_word_family(
    documents: dict[Path, dict],
    root: Path,
    restored_ids: set[str] | None = None,
) -> set[str]:
    """Restore the 12 word_family arrays edited by Batch 027 (v2.95.74) in memory."""
    ledger_path = root / "patches/v2.95.74/word-family-audit-ledger.json"
    if not ledger_path.exists():
        return set()
    seen = restored_ids if restored_ids is not None else set()
    batch_restored: set[str] = set()
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    for entry in ledger.get("reconciliationRecords", []):
        entry_id = entry["id"]
        if entry_id in seen:
            raise AssertionError(f"Duplicate Word Family reversal detected for canonical ID: {entry_id}")
        path = (root / entry["file"]).resolve()
        document = documents.get(path)
        if document is None:
            raise AssertionError(f"Word Family Batch 027 ledger references untracked file: {entry['file']}")
        record = next((row for row in document.get("words", []) if row.get("id") == entry_id), None)
        if record is None:
            raise AssertionError(f"Word Family Batch 027 ledger references missing canonical ID: {entry_id}")
        record["word_family"] = copy.deepcopy(entry.get("before", []))
        seen.add(entry_id)
        batch_restored.add(entry_id)
    return batch_restored


def composite_sha_reversing_vocabulary_patch(paths, root: Path, patch_rel: str) -> str:
    """Hash a historical vocabulary snapshot after reversing later guarded patch ops in memory.

    This preserves historical byte-integrity assertions while allowing a reviewed later
    release patch to change only explicitly guarded vocabulary fields.
    """
    import hashlib
    patch = json.loads((root / patch_rel).read_text(encoding="utf-8"))
    manifest = json.loads((root / "data/manifest.json").read_text(encoding="utf-8"))
    id_to_path = {}
    documents = {}
    later_addition_ids: set[str] = set()
    for batch_name in ("batch-026.json", "batch-028.json", "batch-029.json"):
        batch_path = root / "data/vocabulary" / batch_name
        if batch_path.exists():
            batch_data = json.loads(batch_path.read_text(encoding="utf-8"))
            later_addition_ids.update(w["id"] for w in batch_data.get("words", []))

    for entry in manifest.get("letters", []):
        path = (root / entry["file"].removeprefix("./")).resolve()
        document = json.loads(path.read_text(encoding="utf-8"))
        if later_addition_ids:
            document["words"] = [w for w in document.get("words", []) if w["id"] not in later_addition_ids]
        documents[path] = document
        for record in document.get("words", []):
            id_to_path[record["id"]] = path
    # Restore later canonical vocabulary changes in reverse chronological order:
    # Batch 027 (v2.95.74) whole-array word_family reconciliations, then Batch 025 (v2.95.67).
    restored_word_family_ids: set[str] = set()
    restored_027_ids = reverse_batch_027_word_family(documents, root, restored_ids=restored_word_family_ids)
    # Prove that v2.95.74 reconciliationRecords cover the exact 12 owner IDs from the
    # v2.95.73 reciprocity patch so those 12 whole arrays are never reversed twice.
    family_repair_path = root / "patches/v2.95.73/batch-001-word-family-reciprocity.json"
    if family_repair_path.exists():
        family_repair = json.loads(family_repair_path.read_text(encoding="utf-8"))
        patch_027_owner_ids = (
            {c["ownerId"] for c in family_repair.get("addedLinks", [])}
            | {c["ownerId"] for c in family_repair.get("removedSelfLinks", [])}
        )
        if restored_027_ids:
            if patch_027_owner_ids != restored_027_ids:
                raise AssertionError(
                    f"v2.95.74 ledger IDs ({len(restored_027_ids)}) do not match v2.95.73 patch owner IDs ({len(patch_027_owner_ids)})"
                )
        else:
            # Fallback only if the v2.95.74 whole-array ledger is absent.
            for change in family_repair.get("addedLinks", []):
                owner_id = change["ownerId"]
                if owner_id in restored_word_family_ids:
                    raise AssertionError(f"Duplicate Word Family reversal detected for canonical ID: {owner_id}")
                owner_path = id_to_path.get(owner_id)
                if owner_path is None:
                    raise AssertionError(f"Word Family repair references missing owner ID: {owner_id}")
                owner = next((row for row in documents[owner_path]["words"] if row.get("id") == owner_id), None)
                if owner is None:
                    raise AssertionError(f"Word Family repair owner not found in reconstructed data: {owner_id}")
                family = owner.get("word_family") or []
                matches = [i for i, row in enumerate(family)
                           if str(row.get("word", "")).casefold() == change["target"].casefold()]
                if len(matches) != 1:
                    raise AssertionError(
                        f"Expected one current Batch 027 link {change['owner']} -> {change['target']}; found {len(matches)}"
                    )
                family.pop(matches[0])
                owner["word_family"] = family
                restored_word_family_ids.add(owner_id)
            for change in family_repair.get("removedSelfLinks", []):
                owner_id = change["ownerId"]
                if owner_id in restored_word_family_ids:
                    raise AssertionError(f"Duplicate Word Family reversal detected for canonical ID: {owner_id}")
                owner_path = id_to_path.get(owner_id)
                if owner_path is None:
                    raise AssertionError(f"Word Family self-link repair references missing owner ID: {owner_id}")
                owner = next((row for row in documents[owner_path]["words"] if row.get("id") == owner_id), None)
                if owner is None:
                    raise AssertionError(f"Word Family self-link owner not found in reconstructed data: {owner_id}")
                family = owner.setdefault("word_family", [])
                index = change.get("index", len(family))
                if not isinstance(index, int) or index < 0 or index > len(family):
                    raise AssertionError(f"Invalid original Word Family index for {owner_id}: {index}")
                family.insert(index, {
                    "word": change["target"], "pos": change["pos"], "meaning_vi": change["meaning_vi"]
                })
                restored_word_family_ids.add(owner_id)
    later_family_ledger = root / "data/vocabulary/batch-025.json"
    if later_family_ledger.exists():
        family_batch = json.loads(later_family_ledger.read_text(encoding="utf-8"))
        for entry in family_batch.get("records", []):
            entry_id = entry["id"]
            if entry_id in restored_word_family_ids:
                raise AssertionError(f"Duplicate Word Family reversal detected for canonical ID: {entry_id}")
            path = (root / entry["file"]).resolve()
            document = documents.get(path)
            if document is None:
                raise AssertionError(f"Word Family batch references an untracked vocabulary file: {entry['file']}")
            record = next((row for row in document.get("words", []) if row.get("id") == entry_id), None)
            if record is None:
                raise AssertionError(f"Word Family batch references missing canonical ID: {entry_id}")
            record["word_family"] = copy.deepcopy(entry.get("before", []))
            restored_word_family_ids.add(entry_id)
    for operation in patch.get("operations", []):
        path = id_to_path[operation["id"]]
        record = next(row for row in documents[path]["words"] if row["id"] == operation["id"])
        pointer = operation["path"].strip("/").split("/")
        target = record
        for part in pointer[:-1]:
            target = target[int(part)] if isinstance(target, list) else target[part]
        old = operation["expect"]["old"]
        last = pointer[-1]
        if isinstance(target, list):
            target[int(last)] = old
        else:
            target[last] = old
    digest = hashlib.sha256()
    for path in sorted(paths):
        resolved = path.resolve()
        payload = (json.dumps(documents[resolved], ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(payload).digest())
        digest.update(b"\n")
    return digest.hexdigest()


def composite_sha_reversing_listening_translations(paths, root: Path) -> str:
    """Restore the v2.95.75 Listening resource before hashing approved learning-bank changes."""
    import hashlib

    added_ids = {
        "batch026-part3-vendor-call",
        "batch026-part3-training-room",
        "batch026-part3-invoice-correction",
        "batch026-part3-access-card",
        "batch026-part4-building-notice",
        "batch026-part4-travel-update",
        "batch026-part4-product-launch",
        "batch026-part4-policy-reminder",
    }
    practice_only_part4_ids = {
        "part4-office-announcement",
        "part4-conference-update",
        "part4-safety-announcement",
        "part4-product-launch",
        "part4-quarterly-town-hall",
        "part4-customer-voicemail",
        "part4-warehouse-safety-briefing",
        "part4-training-registration",
        "part4-travel-service-update",
        "part4-quarterly-inventory-report",
    }
    digest = hashlib.sha256()
    seen: set[str] = set()
    practice_only_seen: set[str] = set()
    for path in sorted(paths):
        data = path.read_bytes()
        if path.name == "listening-library.json":
            document = json.loads(data.decode("utf-8"))
            for unit in document["listening"]:
                if unit.get("id") in added_ids:
                    if not unit.get("transcriptTranslation", "").strip():
                        raise AssertionError(f"Missing v2.95.76 transcript translation: {unit.get('id')}")
                    seen.add(unit["id"])
                    del unit["transcriptTranslation"]
                if unit.get("id") in practice_only_part4_ids:
                    questions = unit.get("questions") or []
                    if len(questions) < 4 or any(q.get("mockEligible") is False for q in questions[:3]) or any(q.get("mockEligible") is not False for q in questions[3:]):
                        raise AssertionError(f"Unexpected Part 4 practice-only addition: {unit.get('id')}")
                    practice_only_seen.add(unit["id"])
                    unit["questions"] = questions[:3]
            if seen != added_ids:
                raise AssertionError(f"Listening remediation IDs differ: {sorted(seen ^ added_ids)}")
            if practice_only_seen != practice_only_part4_ids:
                raise AssertionError(f"Part 4 practice-only IDs differ: {sorted(practice_only_seen ^ practice_only_part4_ids)}")

            # v2.95.86 adds three Part 1 reserve-only photo resources after the
            # historical protected-bank snapshot. Validate their resource-level
            # review gate, then exclude only these exact allowlisted IDs before
            # computing the historical composite SHA.
            batch_018_part1_ids = {
                "part1-construction-plans",
                "part1-laboratory-bench",
                "part1-supermarket-shelf",
            }
            batch_018_seen: set[str] = set()
            restored_units = []
            for unit in document["listening"]:
                if unit.get("id") not in batch_018_part1_ids:
                    restored_units.append(unit)
                    continue
                questions = unit.get("questions") or []
                if (
                    unit.get("part") != "Part 1"
                    or unit.get("editorialBatch") != "018"
                    or unit.get("editorialStatus") != "reserve-pending-independent-review"
                    or unit.get("mockExamEligibility") != "excluded-until-independent-review"
                    or len(questions) != 1
                    or "mockEligible" in questions[0]
                ):
                    raise AssertionError(f"Unexpected Batch 018 Part 1 reserve record: {unit.get('id')}")
                batch_018_seen.add(unit["id"])
            if batch_018_seen != batch_018_part1_ids:
                raise AssertionError(f"Batch 018 Part 1 IDs differ: {sorted(batch_018_seen ^ batch_018_part1_ids)}")
            document["listening"] = restored_units
            data = json.dumps(document, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(data).digest())
        digest.update(b"\n")
    return digest.hexdigest()
