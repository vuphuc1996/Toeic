#!/usr/bin/env python3
"""Apply reviewed vocabulary patches by stable ID with strict optimistic locking."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any


def id_sha256(ids: list[str]) -> str:
    return hashlib.sha256("\n".join(sorted(ids)).encode("utf-8")).hexdigest()


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def pointer_parts(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError(f"JSON Pointer không hợp lệ: {pointer!r}")
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]


def get_pointer(obj: Any, pointer: str) -> Any:
    cur = obj
    for part in pointer_parts(pointer):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


def set_pointer(obj: Any, pointer: str, value: Any) -> None:
    parts = pointer_parts(pointer)
    cur = obj
    for part in parts[:-1]:
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    last = parts[-1]
    if isinstance(cur, list):
        cur[int(last)] = value
    else:
        cur[last] = value


def load_all_records(root: Path) -> tuple[dict[str, tuple[Path, dict]], list[str]]:
    manifest = read_json(root / "data/manifest.json")
    found: dict[str, tuple[Path, dict]] = {}
    ids: list[str] = []
    for entry in manifest.get("letters", []):
        rel = entry.get("file", "")
        path = (root / rel.removeprefix("./")).resolve()
        if root.resolve() not in path.parents:
            raise ValueError(f"Đường dẫn dữ liệu vượt khỏi root: {rel}")
        doc = read_json(path)
        for rec in doc.get("words", []):
            rid = rec.get("id")
            if not isinstance(rid, str) or not rid:
                raise ValueError(f"ID không hợp lệ trong {rel}")
            if rid in found:
                raise ValueError(f"ID trùng trong dữ liệu: {rid}")
            found[rid] = (path, rec)
            ids.append(rid)
    return found, ids


def validate_patch_context(root: Path, patch: dict, mode: str) -> tuple[dict[str, tuple[Path, dict]], list[str]]:
    manifest = read_json(root / "data/manifest.json")
    expected_version = patch.get("baseDataVersion") if mode != "rollback" else patch.get("targetDataVersion")
    if manifest.get("version") != expected_version:
        raise ValueError(f"Version không khớp: đang {manifest.get('version')}, yêu cầu {expected_version}")
    found, ids = load_all_records(root)
    actual_hash = id_sha256(ids)
    if patch.get("idSetSha256") != actual_hash:
        raise ValueError(f"ID set SHA-256 không khớp: {actual_hash}")
    return found, ids


def verify_operations(patch: dict, found: dict[str, tuple[Path, dict]], mode: str) -> dict[Path, dict]:
    staged: dict[Path, dict] = {}
    seen: set[tuple[str, str]] = set()
    ops = patch.get("operations")
    if not isinstance(ops, list) or not ops:
        raise ValueError("Patch không có operations hợp lệ.")
    for i, op in enumerate(ops, 1):
        if not isinstance(op, dict):
            raise ValueError(f"Operation #{i} không phải object")
        rid, pointer = op.get("id"), op.get("path")
        if rid not in found:
            raise ValueError(f"Operation #{i}: không tìm thấy ID {rid!r}")
        key = (rid, pointer)
        if key in seen:
            raise ValueError(f"Operation trùng: {rid} {pointer}")
        seen.add(key)
        path, rec = found[rid]
        actual_pos = rec.get("senses", [{}])[int(pointer_parts(pointer)[1])].get("pos") if pointer.startswith("/senses/") else None
        expected_pos = op.get("expect", {}).get("pos")
        if expected_pos is not None and actual_pos != expected_pos:
            raise ValueError(f"{rid} {pointer}: POS mismatch ({actual_pos!r} != {expected_pos!r})")
        actual = get_pointer(rec, pointer)
        expected = op.get("new") if mode == "rollback" else op.get("expect", {}).get("old")
        if actual != expected:
            label = "new" if mode == "rollback" else "old"
            raise ValueError(f"{rid} {pointer}: expect.{label} mismatch; dữ liệu hiện tại không còn như dự kiến")
        staged.setdefault(path, read_json(path))
        target_rec = next(x for x in staged[path]["words"] if x.get("id") == rid)
        set_pointer(target_rec, pointer, op.get("expect", {}).get("old") if mode == "rollback" else op.get("new"))
    return staged


def write_atomically(staged: dict[Path, dict]) -> None:
    temps: dict[Path, Path] = {}
    originals: dict[Path, bytes] = {}
    replaced: list[Path] = []
    try:
        for path, doc in staged.items():
            originals[path] = path.read_bytes()
            payload = (json.dumps(doc, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
            tmp = Path(tmp_name)
            with os.fdopen(fd, "wb") as f:
                f.write(payload)
                f.flush()
                os.fsync(f.fileno())
            temps[path] = tmp
        for path, tmp in temps.items():
            os.replace(tmp, path)
            replaced.append(path)
    except Exception:
        for path in reversed(replaced):
            fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.restore.", dir=str(path.parent))
            with os.fdopen(fd, "wb") as f:
                f.write(originals[path])
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_name, path)
        raise
    finally:
        for tmp in temps.values():
            if tmp.exists():
                tmp.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--patch", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--apply", action="store_true")
    group.add_argument("--rollback", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    patch_path = args.patch if args.patch.is_absolute() else (root / args.patch)
    try:
        patch = read_json(patch_path)
        if patch.get("schemaVersion") != 1:
            raise ValueError("schemaVersion patch phải bằng 1")
        mode = "rollback" if args.rollback else "apply"
        found, ids = validate_patch_context(root, patch, mode)
        staged = verify_operations(patch, found, mode)
        action = "ROLLBACK" if args.rollback else "APPLY"
        print(f"{action} {patch.get('batchId')}: {len(patch['operations'])} operations / {len(staged)} files")
        for path in sorted(staged):
            print(f"  - {path.relative_to(root)}")
        for op in patch["operations"]:
            before = op.get("new") if args.rollback else op.get("expect", {}).get("old")
            after = op.get("expect", {}).get("old") if args.rollback else op.get("new")
            before_text = repr(before)
            after_text = repr(after)
            if len(before_text) > 100:
                before_text = before_text[:97] + "..."
            if len(after_text) > 100:
                after_text = after_text[:97] + "..."
            print(f"  * {op['id']} {op['path']}: {before_text} -> {after_text}")
        if args.dry_run:
            print("DRY-RUN PASS — không ghi file")
            return 0
        write_atomically(staged)
        print(f"{action} PASS — đã ghi {len(staged)} file")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
