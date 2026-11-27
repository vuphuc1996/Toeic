"""Shared reconstruction helpers for historical Related Glossary regression tests."""
from __future__ import annotations
import copy
import json
from pathlib import Path



def restore_batch_046(glossary: dict, root: Path) -> dict:
    """Reverse Batch 046, restoring the Related Glossary to its v2.95.71 state."""
    restored = copy.deepcopy(glossary)
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
    batch_026_path = root / "data/vocabulary/batch-026.json"
    batch_026_ids = set()
    if batch_026_path.exists():
        batch_026_data = json.loads(batch_026_path.read_text(encoding="utf-8"))
        batch_026_ids = {w["id"] for w in batch_026_data.get("words", [])}

    for entry in manifest.get("letters", []):
        path = (root / entry["file"].removeprefix("./")).resolve()
        document = json.loads(path.read_text(encoding="utf-8"))
        if batch_026_ids:
            document["words"] = [w for w in document.get("words", []) if w["id"] not in batch_026_ids]
        documents[path] = document
        for record in document.get("words", []):
            id_to_path[record["id"]] = path
    # Restore later canonical vocabulary changes before asserting historical
    # glossary ledgers. v2.95.67 added six reciprocal Word Family links only;
    # each row's before snapshot is an explicitly empty array.
    later_family_ledger = root / "data/vocabulary/batch-025.json"
    if later_family_ledger.exists():
        family_batch = json.loads(later_family_ledger.read_text(encoding="utf-8"))
        for entry in family_batch.get("records", []):
            path = (root / entry["file"]).resolve()
            document = documents.get(path)
            if document is None:
                raise AssertionError(f"Word Family batch references an untracked vocabulary file: {entry['file']}")
            record = next((row for row in document.get("words", []) if row.get("id") == entry["id"]), None)
            if record is None:
                raise AssertionError(f"Word Family batch references missing canonical ID: {entry['id']}")
            record["word_family"] = copy.deepcopy(entry.get("before", []))
    # Reverse later reciprocal Word Family-only repairs before reconstructing
    # historical glossary snapshots. These changes are intentionally present in the
    # current canonical data, but must not contaminate an older batch's frozen hash.
    family_repair_path = root / "patches/v2.95.73/batch-001-word-family-reciprocity.json"
    if family_repair_path.exists():
        family_repair = json.loads(family_repair_path.read_text(encoding="utf-8"))
        for change in family_repair.get("addedLinks", []):
            owner_id = change["ownerId"]
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
        for change in family_repair.get("removedSelfLinks", []):
            owner_id = change["ownerId"]
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
