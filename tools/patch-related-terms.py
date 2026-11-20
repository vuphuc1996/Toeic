#!/usr/bin/env python3
"""Safely add sourced Vietnamese glosses to the related-terms dictionary."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import stat
import tempfile
from urllib.parse import urlsplit
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as stream:
        return json.load(stream)


def write_atomic(path: Path, payload: bytes) -> None:
    fd, name = tempfile.mkstemp(prefix=f'.{path.name}.', suffix='.tmp', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
            if path.exists():
                os.fchmod(stream.fileno(), stat.S_IMODE(path.stat().st_mode))
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def audit(root: Path, patch: dict, mode: str, result: str, error: str | None = None) -> None:
    directory = root / 'logs' / 'patch-related-terms'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / 'operations.jsonl'
    at = datetime.now(timezone.utc).isoformat(timespec='seconds')
    rows = []
    for i, op in enumerate(patch.get('operations', []), 1):
        rows.append({
            'recordedAt': at, 'mode': mode, 'batchId': patch.get('batchId'),
            'operation': i, 'term': op.get('term'), 'old': None,
            'new': op.get('new'), 'result': result,
            **({'error': error} if error else {}),
        })
    if not rows:
        rows.append({'recordedAt': at, 'mode': mode, 'batchId': patch.get('batchId'), 'result': result,
                     **({'error': error} if error else {})})
    with path.open('a', encoding='utf-8') as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
        stream.flush()
        os.fsync(stream.fileno())


def validate_patch(patch: dict) -> list[dict]:
    if patch.get('schemaVersion') != 1:
        raise ValueError('schemaVersion phải bằng 1')
    if not isinstance(patch.get('batchId'), str) or not patch['batchId'].strip():
        raise ValueError('Thiếu batchId')
    operations = patch.get('operations')
    if not isinstance(operations, list) or not operations:
        raise ValueError('Patch phải có operations không rỗng')
    seen = set()
    for index, op in enumerate(operations, 1):
        if not isinstance(op, dict):
            raise ValueError(f'Operation #{index} không phải object')
        term = op.get('term')
        if not isinstance(term, str) or not term.strip():
            raise ValueError(f'Operation #{index}: term không hợp lệ')
        key = term.casefold()
        if key in seen:
            raise ValueError(f'Term trùng trong patch: {term}')
        seen.add(key)
        if op.get('expect') != {'absent': True}:
            raise ValueError(f'{term}: chỉ cho phép thêm mục mới với expect.absent=true')
        new = op.get('new')
        if not isinstance(new, dict) or new.get('term', '').casefold() != key:
            raise ValueError(f'{term}: new.term không khớp')
        for field in ('meaning_vi', 'pos', 'definition_en', 'source'):
            if not isinstance(new.get(field), str) or not new[field].strip():
                raise ValueError(f'{term}: thiếu hoặc rỗng trường {field}')
        urls = new.get('sourceUrls')
        if not isinstance(urls, list) or not urls:
            raise ValueError(f'{term}: phải có sourceUrls HTTPS từ Cambridge Dictionary')
        for url in urls:
            if not isinstance(url, str):
                raise ValueError(f'{term}: sourceUrls phải chứa URL dạng chuỗi')
            parsed = urlsplit(url)
            if (parsed.scheme != 'https' or parsed.hostname != 'dictionary.cambridge.org'
                    or parsed.username or parsed.password or not parsed.path.startswith('/dictionary/')):
                raise ValueError(f'{term}: URL phải thuộc đúng host Cambridge Dictionary')
    return operations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--patch', type=Path, required=True)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--dry-run', action='store_true')
    actions.add_argument('--apply', action='store_true')
    actions.add_argument('--rollback', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    patch_path = args.patch if args.patch.is_absolute() else root / args.patch
    mode = 'dry-run' if args.dry_run else ('apply' if args.apply else 'rollback')
    patch = None
    try:
        patch = read_json(patch_path)
        operations = validate_patch(patch)
        target = root / 'data' / 'related-terms.json'
        original = target.read_bytes()
        if args.dry_run or args.apply:
            expected_hash = patch.get('baseFileSha256')
            if expected_hash != sha256(original):
                raise ValueError('related-terms.json SHA-256 không khớp baseFileSha256')
        document = json.loads(original.decode('utf-8'))
        if not isinstance(document, dict) or document.get('schemaVersion') != 1:
            raise ValueError('related-terms.json phải là object schemaVersion=1')
        terms = document.get('terms')
        if not isinstance(terms, list):
            raise ValueError('related-terms.json thiếu mảng terms')
        by_key = {}
        for index, row in enumerate(terms, 1):
            if not isinstance(row, dict) or not isinstance(row.get('term'), str) or not row['term'].strip():
                raise ValueError(f'related-terms.json có mục không hợp lệ tại vị trí {index}')
            key = row['term'].casefold()
            if key in by_key:
                raise ValueError(f'related-terms.json có term trùng: {row["term"]}')
            by_key[key] = row
        if args.rollback:
            for op in operations:
                current = by_key.get(op['term'].casefold())
                if current != op['new']:
                    raise ValueError(f"Rollback dừng: mục {op['term']!r} không còn đúng bằng bản đã thêm")
            remove_keys = {op['term'].casefold() for op in operations}
            next_terms = [row for row in terms if row.get('term', '').casefold() not in remove_keys]
        else:
            for op in operations:
                if op['term'].casefold() in by_key:
                    raise ValueError(f"Term đã tồn tại, không ghi đè: {op['term']}")
            next_terms = terms + [op['new'] for op in operations]
        next_terms.sort(key=lambda row: row.get('term', '').casefold())
        document['terms'] = next_terms
        payload = (json.dumps(document, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        print(f"{mode.upper()} {patch['batchId']}: {len(operations)} terms / data/related-terms.json")
        for op in operations:
            print(f"  - {op['term']}: {op['new']['meaning_vi']}")
        if args.dry_run:
            audit(root, patch, mode, 'DRY_RUN_OK')
            print('DRY-RUN PASS — không ghi dữ liệu; đã ghi operation audit log')
        elif args.apply:
            write_atomic(target, payload)
            try:
                audit(root, patch, mode, 'APPLIED')
            except Exception:
                write_atomic(target, original)
                raise
            print(f"APPLY PASS — đã thêm {len(operations)} related-term glosses và ghi audit log")
        else:
            write_atomic(target, payload)
            try:
                audit(root, patch, mode, 'ROLLED_BACK')
            except Exception:
                write_atomic(target, original)
                raise
            print(f"ROLLBACK PASS — đã gỡ {len(operations)} related-term glosses")
        return 0
    except Exception as exc:
        try:
            audit(root, patch or {}, mode, 'REJECTED', str(exc))
        except Exception:
            pass
        print(f'{mode.upper()} FAIL: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
