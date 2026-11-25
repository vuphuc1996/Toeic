#!/usr/bin/env python3
"""Fail-fast GitHub commit-readiness audit for a checked-out repository.

The audit is deliberately dependency-free. It checks Git state, index/tree paths,
GitHub/Windows-sensitive names, binary/large-file hazards, release artifacts,
repository ignore rules, Git attributes and whitespace in the commit or staging
area. It does not stage, commit, amend, reset or otherwise mutate Git state.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
GITHUB_HARD_FILE_LIMIT = 100 * 1024 * 1024
SAFE_FILE_LIMIT = 90 * 1024 * 1024
WARN_FILE_LIMIT = 50 * 1024 * 1024
WINDOWS_RESERVED = re.compile(r"^(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?$", re.IGNORECASE)
INVALID_WINDOWS_CHARS = set('<>:"|?*')
RELEASE_SUFFIXES = (".zip", ".sha256", ".tar", ".tar.gz")
IGNORE_PROBES = (
    "logs/git-readiness/probe.log",
    "tools/tests/__pycache__/probe.pyc",
    ".venv/git-readiness-probe.txt",
    "release/git-readiness-probe.zip",
    "release/git-readiness-probe.zip.sha256",
    ".DS_Store",
    "Thumbs.db",
)


class GitAuditError(RuntimeError):
    pass


def git(args: list[str], *, check: bool = True, text: bool = True) -> str | bytes:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=text, check=False
    )
    if check and result.returncode:
        stderr = result.stderr if text else (result.stderr or b"").decode("utf-8", "replace")
        raise GitAuditError(f"git {' '.join(args)} failed ({result.returncode}): {stderr.strip()}")
    return result.stdout


def ensure_git_repository() -> None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], cwd=ROOT,
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise GitAuditError("source has no Git metadata; run this check in a Git clone")
    top = Path(result.stdout.strip()).resolve()
    if top != ROOT.resolve():
        raise GitAuditError(f"Git root mismatch: expected {ROOT}, got {top}")
    git(["rev-parse", "--verify", "HEAD"])


def status_rows() -> list[tuple[str, str]]:
    raw = git(["status", "--porcelain=v1", "--untracked-files=all"])
    rows: list[tuple[str, str]] = []
    for line in str(raw).splitlines():
        if not line:
            continue
        rows.append((line[:2], line[3:] if len(line) > 3 else ""))
    return rows


def tracked_paths() -> list[str]:
    raw = git(["ls-files", "-z"], text=False)
    return [item.decode("utf-8", "surrogateescape") for item in bytes(raw).split(b"\0") if item]


def validate_paths(paths: list[str]) -> list[str]:
    errors: list[str] = []
    by_casefold: dict[str, str] = {}
    for raw in paths:
        path = PurePosixPath(raw)
        if path.is_absolute() or ".." in path.parts:
            errors.append(f"unsafe repository path: {raw!r}")
            continue
        folded = raw.casefold()
        previous = by_casefold.get(folded)
        if previous is not None and previous != raw:
            errors.append(f"case-insensitive path collision: {previous!r} vs {raw!r}")
        else:
            by_casefold[folded] = raw
        for part in path.parts:
            if part.endswith((".", " ")):
                errors.append(f"Windows-incompatible trailing dot/space: {raw!r}")
                break
            if any(char in INVALID_WINDOWS_CHARS or ord(char) < 32 for char in part):
                errors.append(f"Windows-incompatible character in path: {raw!r}")
                break
            if WINDOWS_RESERVED.match(part):
                errors.append(f"Windows reserved device name in path: {raw!r}")
                break
        lowered = raw.lower()
        if lowered.endswith(RELEASE_SUFFIXES):
            errors.append(f"release/package artifact must not be committed: {raw!r}")
    return errors


def validate_file_sizes(paths: list[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for raw in paths:
        path = ROOT / raw
        if not path.exists() or not path.is_file():
            continue  # A staged delete is no longer present in the index/worktree.
        size = path.stat().st_size
        if size >= GITHUB_HARD_FILE_LIMIT:
            errors.append(f"file reaches GitHub's 100 MiB hard limit: {raw} ({size} bytes)")
        elif size > SAFE_FILE_LIMIT:
            errors.append(f"file exceeds 90 MiB commit safety threshold: {raw} ({size} bytes)")
        elif size > WARN_FILE_LIMIT:
            warnings.append(f"large tracked file: {raw} ({size} bytes)")
    return errors, warnings


def validate_symlinks() -> list[str]:
    raw = git(["ls-files", "-s", "-z"], text=False)
    errors: list[str] = []
    for item in bytes(raw).split(b"\0"):
        if not item:
            continue
        metadata, _, path = item.partition(b"\t")
        fields = metadata.decode("ascii", "replace").split()
        if fields and fields[0] == "120000":
            errors.append(
                "symbolic link is not allowed in the GitHub Pages source tree: "
                + path.decode("utf-8", "surrogateescape")
            )
    return errors


def validate_ignore_rules() -> list[str]:
    errors: list[str] = []
    for probe in IGNORE_PROBES:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", "--", probe],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            errors.append(f".gitignore does not exclude generated/local path: {probe}")
    return errors


def validate_attributes() -> list[str]:
    text_paths = ["index.html", "sw.js", "tools/audit-git-commit-readiness.py"]
    binary_paths = ["assets/listening/part1-office-cleaning.jpg"]
    errors: list[str] = []
    for expected, paths in (("lf", text_paths), ("binary", binary_paths)):
        for path in paths:
            if not (ROOT / path).is_file():
                continue
            output = str(git(["check-attr", "text", "eol", "--", path]))
            if expected == "lf":
                if f"{path}: text: auto" not in output or f"{path}: eol: lf" not in output:
                    errors.append(f".gitattributes must normalize text to LF: {path}")
            elif f"{path}: text: unset" not in output:
                errors.append(f".gitattributes must mark media as binary: {path}")
    return errors


def validate_whitespace(staged: bool) -> list[str]:
    if staged:
        command = ["diff", "--cached", "--check"]
    else:
        parent = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD^"], cwd=ROOT,
            capture_output=True, text=True, check=False,
        )
        if parent.returncode:
            # A root/one-deep checkout has no safe predecessor diff. GitHub CI
            # requests depth=2 so normal release commits are always checked.
            return []
        command = ["diff", "--check", "HEAD^", "HEAD"]
    result = subprocess.run(
        ["git", *command], cwd=ROOT, capture_output=True, text=True, check=False
    )
    if result.returncode:
        detail = (result.stdout + result.stderr).strip()
        return [f"Git whitespace/conflict-marker check failed: {detail or result.returncode}"]
    return []


def validate_git_state(staged: bool) -> list[str]:
    errors: list[str] = []
    rows = status_rows()
    for code, path in rows:
        if code == "??":
            errors.append(f"untracked file is not part of the staged commit: {path}")
            continue
        if staged:
            if len(code) > 1 and code[1] != " ":
                errors.append(f"unstaged working-tree change remains: {path} ({code})")
        elif code.strip():
            errors.append(f"working tree is not clean: {path} ({code})")
    if staged:
        staged_count = sum(1 for code, _ in rows if code[0] not in (" ", "?"))
        if staged_count == 0:
            errors.append("--staged requires at least one staged change")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--require-clean", action="store_true", help="require a clean checkout (default; used in GitHub Actions)")
    modes.add_argument("--staged", action="store_true", help="allow staged changes but reject unstaged/untracked files")
    args = parser.parse_args()
    staged = bool(args.staged)

    errors: list[str] = []
    warnings: list[str] = []
    try:
        ensure_git_repository()
        paths = tracked_paths()
        errors.extend(validate_paths(paths))
        size_errors, size_warnings = validate_file_sizes(paths)
        errors.extend(size_errors)
        warnings.extend(size_warnings)
        errors.extend(validate_symlinks())
        errors.extend(validate_ignore_rules())
        errors.extend(validate_attributes())
        errors.extend(validate_whitespace(staged))
        errors.extend(validate_git_state(staged))
    except (GitAuditError, OSError, UnicodeError) as exc:
        errors.append(str(exc))

    print(f"Git commit readiness: {len(paths) if 'paths' in locals() else 0} indexed paths inspected")
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    if not errors:
        print("RESULT: PASS — Git index/worktree, path portability, ignore rules and commit whitespace are safe")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
