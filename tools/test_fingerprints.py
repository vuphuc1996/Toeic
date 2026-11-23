#!/usr/bin/env python3
"""Deterministic source and test-input fingerprints for release test checkpoints.

Fingerprints contain source metadata and content hashes only. Environment secrets
are never read or serialized.
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import platform
import shutil
import stat
import subprocess
import sys
import unicodedata
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 2
DEPENDENCY_INPUT_FILES = (
    "requirements.txt", "requirements-test.txt", "requirements-dev.txt",
    "pyproject.toml", "poetry.lock", "Pipfile.lock", "package.json",
    "package-lock.json", "npm-shrinkwrap.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb", "bun.lock",
)
DEFAULT_SCOPE_POLICY = {
    "schemaVersion": 1,
    "exclude_directories": [".git", "__pycache__", ".pytest_cache", "node_modules"],
    "exclude_directory_prefixes": ["release_"],
    "exclude_paths": ["logs", "docs/archive"],
    "exclude_suffixes": [".zip", ".bundle", ".log", ".pyc", ".tmp"],
    "include_file_metadata": ["relative_path", "kind", "size", "mode", "content_sha256"],
    "timestamps_in_fingerprint": False,
    "owner_metadata_in_fingerprint": False,
    "symlink_policy": "record_target_without_following_and_reject_targets_outside_source_root",
}


def _canonical_json(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_relative_path(value: str) -> str:
    """Normalize a source-relative path without resolving symlinks."""
    normalized = unicodedata.normalize("NFC", value.replace("\\", "/"))
    while normalized.startswith("./"):
        normalized = normalized[2:]
    if normalized.startswith("/") or any(part in {"", ".", ".."} for part in normalized.split("/")):
        raise ValueError(f"unsafe or non-normalized source path: {value!r}")
    return normalized


def load_scope_policy(root: Path) -> dict[str, Any]:
    policy_path = root / "tools" / "source-fingerprint-policy.json"
    policy = json.loads(policy_path.read_text(encoding="utf-8")) if policy_path.is_file() else DEFAULT_SCOPE_POLICY
    required = {"exclude_directories", "exclude_directory_prefixes", "exclude_paths", "exclude_suffixes"}
    missing = required - set(policy)
    if missing:
        raise ValueError(f"source fingerprint policy missing keys: {sorted(missing)}")
    return policy


def is_excluded_relative_path(relative: str, policy: dict[str, Any]) -> bool:
    path = Path(relative)
    parts = path.parts
    if not parts:
        return True
    excluded_paths = {normalize_relative_path(item).rstrip("/") for item in policy.get("exclude_paths", [])}
    if relative in excluded_paths or any(relative.startswith(item + "/") for item in excluded_paths):
        return True
    excluded_dirs = set(policy.get("exclude_directories", []))
    prefixes = tuple(policy.get("exclude_directory_prefixes", []))
    if any(part in excluded_dirs or part.startswith(prefixes) for part in parts) if prefixes else any(part in excluded_dirs for part in parts):
        return True
    if path.suffix.lower() in {suffix.lower() for suffix in policy.get("exclude_suffixes", [])}:
        return True
    return any(fnmatch.fnmatchcase(relative, pattern) for pattern in policy.get("exclude_patterns", []))


def _scan_entries(root: Path) -> list[dict[str, Any]]:
    """Walk without following symlinks; fingerprint each regular file/link once."""
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"source root is not a directory: {root}")

    entries: list[dict[str, Any]] = []
    seen_casefold: dict[str, str] = {}
    policy = load_scope_policy(root)

    def visit(directory: Path) -> None:
        try:
            children = sorted(os.scandir(directory), key=lambda item: unicodedata.normalize("NFC", item.name).casefold())
        except OSError as exc:
            raise OSError(f"cannot scan source directory {directory}: {exc}") from exc
        for item in children:
            path = Path(item.path)
            relative = normalize_relative_path(path.relative_to(root).as_posix())
            if is_excluded_relative_path(relative, policy):
                continue
            folded = relative.casefold()
            previous = seen_casefold.get(folded)
            if previous is not None:
                raise ValueError(f"normalized/case-folded path collision: {previous!r} vs {relative!r}")
            seen_casefold[folded] = relative
            info = item.stat(follow_symlinks=False)
            mode = stat.S_IMODE(info.st_mode)
            if stat.S_ISLNK(info.st_mode):
                target = os.readlink(path)
                if os.path.isabs(target):
                    raise ValueError(f"absolute symbolic link target is not allowed in source fingerprint: {relative} -> {target}")
                resolved_target = (path.parent / target).resolve(strict=False)
                if not resolved_target.is_relative_to(root):
                    raise ValueError(f"symbolic link escapes approved source root: {relative} -> {target}")
                entries.append({
                    "path": relative,
                    "kind": "symlink",
                    "size": len(os.fsencode(target)),
                    "mode": mode,
                    "target": unicodedata.normalize("NFC", target.replace("\\", "/")),
                    "target_sha256": _sha256(os.fsencode(target)),
                })
            elif stat.S_ISDIR(info.st_mode):
                visit(path)
            elif stat.S_ISREG(info.st_mode):
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for block in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(block)
                entries.append({
                    "path": relative,
                    "kind": "file",
                    "size": info.st_size,
                    "mode": mode,
                    "sha256": digest.hexdigest(),
                })
            else:
                raise ValueError(f"unsupported source filesystem object: {relative}")

    visit(root)
    entries.sort(key=lambda row: row["path"].encode("utf-8"))
    return entries


def source_release_fingerprint(root: Path) -> dict[str, Any]:
    entries = _scan_entries(root)
    policy = load_scope_policy(root)
    manifest = {"schema": SCHEMA_VERSION, "scope": "source-release-v2", "scope_policy": policy, "entries": entries}
    return {
        "fingerprint": _sha256(_canonical_json(manifest)),
        "file_count": sum(row["kind"] == "file" for row in entries),
        "symlink_count": sum(row["kind"] == "symlink" for row in entries),
        "manifest": manifest,
    }


def _safe_node_version() -> str | None:
    node = shutil.which("node")
    if not node:
        return None
    try:
        result = subprocess.run([node, "--version"], capture_output=True, text=True, timeout=5, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return "unavailable"
    if result.returncode != 0:
        return "unavailable"
    return (result.stdout or result.stderr).strip()[:80]


def environment_fingerprint() -> dict[str, Any]:
    """Record non-secret runtime metadata; never serialize environment values."""
    safe = {
        "schema": SCHEMA_VERSION,
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_executable_name": Path(sys.executable).name,
        "python_cache_tag": getattr(sys.implementation, "cache_tag", None),
        "node_version": _safe_node_version(),
        "os_name": os.name,
        "platform_system": platform.system(),
        "platform_release": platform.release(),
        "platform_machine": platform.machine(),
        "platform_architecture": platform.architecture()[0],
    }
    # Environment variables are deliberately not read: they may contain secrets.
    return {"fingerprint": _sha256(_canonical_json(safe)), "metadata": safe}


def test_input_fingerprint(root: Path, modules: list[str], command_config: dict[str, Any]) -> dict[str, Any]:
    source = source_release_fingerprint(root)
    environment = environment_fingerprint()
    root = root.resolve()
    inventory = []
    for module in sorted(modules):
        module_path = Path(module)
        if not module_path.as_posix().startswith("tools/tests/"):
            module_path = Path("tools/tests") / module_path
        path = root / module_path
        relative = normalize_relative_path(path.relative_to(root).as_posix())
        inventory.append({"path": relative, "sha256": _sha256(path.read_bytes())})
    dependency_inputs = []
    for relative in DEPENDENCY_INPUT_FILES:
        path = root / relative
        if path.is_file():
            dependency_inputs.append({"path": relative, "sha256": _sha256(path.read_bytes()), "size": path.stat().st_size})
    payload = {
        "schema": SCHEMA_VERSION,
        "source_release_fingerprint": source["fingerprint"],
        "dependency_inputs": dependency_inputs,
        "environment_fingerprint": environment["fingerprint"],
        "test_inventory": inventory,
        "command_config": command_config,
    }
    return {
        "fingerprint": _sha256(_canonical_json(payload)),
        "source_release_fingerprint": source["fingerprint"],
        "source_file_count": source["file_count"],
        "dependency_inputs": dependency_inputs,
        "source_symlink_count": source["symlink_count"],
        "environment_fingerprint": environment["fingerprint"],
        "environment": environment["metadata"],
        "inventory_fingerprint": _sha256(_canonical_json(inventory)),
        "command_config": command_config,
        "schema": SCHEMA_VERSION,
    }
