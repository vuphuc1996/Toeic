#!/usr/bin/env python3
"""Create a lightweight, one-root ZIP for GitHub commits from tracked Git files."""
from __future__ import annotations
import argparse, io, re, subprocess, tarfile, zipfile
from pathlib import Path

EXCLUDED_DIRS = {".git", "logs", "archive", "__pycache__", ".pytest_cache", "node_modules", "release", "releases"}
EXCLUDED_SUFFIXES = {".zip", ".bundle", ".log", ".pyc"}

def is_excluded(path: str) -> bool:
    parts = Path(path).parts
    if any(part in EXCLUDED_DIRS or part.startswith("release_") for part in parts):
        return True
    if Path(path).suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    return False

def package(repo: Path, version: str, output: Path) -> int:
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Version must be numeric X.Y.Z")
    diff = subprocess.run(["git", "diff", "--quiet", "HEAD", "--"], cwd=repo, check=False)
    if diff.returncode != 0:
        raise RuntimeError("Tracked working-tree changes must be committed before packaging")
    archive = subprocess.run(["git", "archive", "--format=tar", "HEAD"], cwd=repo, capture_output=True, check=True)
    prefix = f"Toeic_Dictionary_v{version}/"
    output.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(archive.stdout), mode="r:") as tar, zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        written = 0
        for member in tar.getmembers():
            if not member.isfile() or is_excluded(member.name):
                continue
            fileobj = tar.extractfile(member)
            if fileobj is None:
                continue
            zf.writestr(prefix + member.name, fileobj.read())
            written += 1
    with zipfile.ZipFile(output) as zf:
        names = zf.namelist()
        roots = {name.split("/", 1)[0] for name in names}
        if roots != {prefix.rstrip("/")}:
            raise RuntimeError(f"Unexpected ZIP root(s): {roots}")
        if any(is_excluded(name[len(prefix):]) for name in names):
            raise RuntimeError("ZIP contains excluded auxiliary paths")
        if not names:
            raise RuntimeError("ZIP is empty")
    return written

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("version")
    ap.add_argument("output", type=Path)
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args=ap.parse_args()
    count=package(args.repo.resolve(),args.version,args.output.resolve())
    print(f"OK: {args.output} | {count} source/data/docs files | root Toeic_Dictionary_v{args.version}/")
if __name__=="__main__": main()
