#!/usr/bin/env python3
"""Apply exact-guarded field corrections to existing related-term glossary entries."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = Path('data/related-terms.json')
ALLOWED_FIELDS = {'meaning_vi', 'pos', 'definition_en', 'source', 'sourceUrls', 'sourceHeadword', 'sourceRelease', 'sourceSenseIndex'}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def update_document(document: dict, patch: dict) -> tuple[dict, list[str]]:
    """Return an updated copy after exact old-value guards; never mutate input."""
    if not isinstance(document, dict) or document.get('schemaVersion') != 1:
        raise ValueError('related-terms document must use schemaVersion=1')
    if not isinstance(patch, dict) or patch.get('schemaVersion') != 1:
        raise ValueError('patch schemaVersion must be 1')
    operations = patch.get('operations')
    if not isinstance(operations, list) or not operations:
        raise ValueError('patch operations must be a non-empty list')
    rows = document.get('terms')
    if not isinstance(rows, list):
        raise ValueError('related-terms document must contain a terms list')

    index_by_key = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or not isinstance(row.get('term'), str) or not row['term'].strip():
            raise ValueError(f'malformed existing glossary row at index {index}')
        key = row['term'].strip().casefold()
        if key in index_by_key:
            raise ValueError(f'duplicate existing glossary term: {row["term"]}')
        index_by_key[key] = index

    seen = set()
    changes = []
    output = copy.deepcopy(document)
    for number, operation in enumerate(operations, 1):
        if not isinstance(operation, dict):
            raise ValueError(f'operation #{number} must be an object')
        term = operation.get('term')
        if not isinstance(term, str) or not term.strip():
            raise ValueError(f'operation #{number} has invalid term')
        key = term.strip().casefold()
        if key in seen:
            raise ValueError(f'duplicate term in patch: {term}')
        seen.add(key)
        if key not in index_by_key:
            raise ValueError(f'cannot update missing glossary term: {term}')
        expect = operation.get('expect')
        updates = operation.get('set')
        if not isinstance(expect, dict) or not expect:
            raise ValueError(f'{term}: exact expect object is required')
        if not isinstance(updates, dict) or not updates:
            raise ValueError(f'{term}: set object is required')
        if set(expect) - (ALLOWED_FIELDS | {'term'}):
            raise ValueError(f'{term}: expect contains unsupported fields')
        if set(updates) - ALLOWED_FIELDS:
            raise ValueError(f'{term}: set contains unsupported or immutable fields')
        row_index = index_by_key[key]
        current = output['terms'][row_index]
        for field, expected_value in expect.items():
            actual_value = current.get('term') if field == 'term' else current.get(field)
            if actual_value != expected_value:
                raise ValueError(f'{term}: stale expectation for {field!r}')
        for field, value in updates.items():
            if value is None or (isinstance(value, str) and not value.strip()):
                raise ValueError(f'{term}: updated {field!r} must not be empty')
            current[field] = value
        changes.append(term)

    # Preserve order and all non-target rows; re-check identity uniqueness.
    normalized = [row['term'].strip().casefold() for row in output['terms']]
    if len(normalized) != len(set(normalized)):
        raise ValueError('updated glossary contains duplicate term identities')
    return output, changes


def write_atomic(path: Path, content: bytes) -> None:
    fd, temporary = tempfile.mkstemp(prefix=f'.{path.name}.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
            if path.exists():
                os.fchmod(stream.fileno(), stat.S_IMODE(path.stat().st_mode))
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--patch', type=Path, required=True)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--dry-run', action='store_true')
    actions.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    patch_path = args.patch if args.patch.is_absolute() else root / args.patch
    target = root / TARGET
    try:
        raw = target.read_bytes()
        patch = json.loads(patch_path.read_text(encoding='utf-8'))
        expected_hash = patch.get('baseFileSha256')
        if expected_hash != sha256(raw):
            raise ValueError('related-terms.json SHA-256 does not match patch baseFileSha256')
        document = json.loads(raw.decode('utf-8'))
        updated, changes = update_document(document, patch)
        payload = (json.dumps(updated, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        print(f"{'DRY-RUN' if args.dry_run else 'APPLY'} {patch['batchId']}: {len(changes)} guarded updates")
        for term in changes:
            print(f'  - {term}')
        if args.apply:
            write_atomic(target, payload)
            print('APPLY PASS — canonical glossary updated atomically')
        else:
            print('DRY-RUN PASS — no source files changed')
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f'UPDATE FAIL: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
