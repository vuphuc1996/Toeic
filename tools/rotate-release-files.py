#!/usr/bin/env python3
"""Retire obsolete version-specific notes after consolidating their content.

Default is dry-run. Use --apply to append eligible old batch/report markdown to
`docs/archive/PROJECT_HISTORY.md`, remove those source copies, and keep only the
current and immediately previous root UPDATE_NOTES files. It never touches app
code, vocabulary, question data, assets, user images, or IndexedDB.
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'docs/archive/PROJECT_HISTORY.md'

def version_tuple(s): return tuple(map(int,s.split('.')))

def compact_summary(path: Path, text: str) -> str:
    """Create a short archive index entry instead of copying entire retired docs."""
    lines=[line.strip() for line in text.splitlines()]
    title=next((line.lstrip('#').strip() for line in lines if line.startswith('#') and line.lstrip('#').strip()),path.stem.replace('_',' '))
    version_match=re.search(r'v?(\d+\.\d+\.\d+)',path.name)
    version=version_match.group(1) if version_match else 'legacy'
    highlights=[]
    for line in lines:
        if not line or line.startswith('#') or line.startswith('|') or line.startswith('```') or line.startswith('---'):
            continue
        if line.startswith(('**','- ','* ')):
            candidate=re.sub(r'^[-*]\s*','',line).strip()
            candidate=re.sub(r'\*\*','',candidate)
            if len(candidate)>220: candidate=candidate[:217].rstrip()+'…'
            if candidate and candidate not in highlights:
                highlights.append(candidate)
        if len(highlights)>=3: break
    summary='; '.join(highlights) if highlights else 'Tài liệu lịch sử đã được rút gọn; nội dung release chính được truy vết trong docs/CHANGELOG.md.'
    return f"- **v{version} · {title}** (`{path.as_posix()}`): {summary}"


def append_archive_entries(existing: str, additions: list[str]) -> str:
    """Keep a single history-index heading while preserving every entry."""
    heading = "## Newly retired documents"
    if heading in existing:
        prefix, *chunks = existing.split(heading)
        historic_entries = "\n\n".join(chunk.strip() for chunk in chunks if chunk.strip())
        new_entries = "\n".join(additions)
        body = "\n\n".join(part for part in (historic_entries, new_entries) if part)
        return prefix.rstrip() + "\n\n" + heading + ("\n\n" + body.rstrip() if body else "") + "\n"
    if not additions:
        return existing
    return existing.rstrip() + "\n\n" + heading + "\n\n" + "\n".join(additions) + "\n"


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--apply',action='store_true',help='perform the planned retirement; default is dry-run')
    args=ap.parse_args()
    current=json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8'))['version']
    major,minor,patch=version_tuple(current)
    prev=f'{major}.{minor}.{max(0,patch-1)}'
    # If current patch is .0, keep the immediately prior minor's latest patch as fallback.
    if patch==0: prev=f'{major}.{max(0,minor-1)}.0'
    keep={current,prev}
    root_release_files=[]
    for pattern, rx in [
        ('V*_UPDATE_NOTES.txt', r'V(\d+\.\d+\.\d+)_UPDATE_NOTES\.txt'),
        ('V*_OVERLAY_MANIFEST.txt', r'V(\d+\.\d+\.\d+)_OVERLAY_MANIFEST\.txt'),
    ]:
        for p in ROOT.glob(pattern):
            m=re.fullmatch(rx,p.name)
            if m and m.group(1) not in keep: root_release_files.append(p)
    docs=[]
    for folder in [ROOT/'docs/batches',ROOT/'docs/reports',ROOT/'docs/sources']:
        if not folder.exists(): continue
        for p in folder.glob('*.md'):
            versions=set(re.findall(r'v(\d+\.\d+\.\d+)',p.name))
            if not versions or not (versions & keep): docs.append(p)
    print(f'Current={current}; keep={sorted(keep)}')
    for p in docs: print('ARCHIVE + RETIRE',p.relative_to(ROOT))
    for p in root_release_files: print('RETIRE',p.relative_to(ROOT))
    if not args.apply:
        print(f'DRY RUN: {len(docs)} markdown files and {len(root_release_files)} root release files would be retired.')
        return 0
    ARCHIVE.parent.mkdir(parents=True,exist_ok=True)
    existing=ARCHIVE.read_text(encoding='utf-8') if ARCHIVE.exists() else '# Consolidated Project History\n'
    additions=[]
    for p in docs + root_release_files:
        rel=p.relative_to(ROOT).as_posix()
        marker=f'`{rel}`'
        if marker not in existing:
            additions.append(compact_summary(p.relative_to(ROOT),p.read_text(encoding='utf-8')))
    updated_archive = append_archive_entries(existing, additions)
    if updated_archive != existing:
        ARCHIVE.write_text(updated_archive, encoding='utf-8')
    for p in docs+root_release_files: p.unlink(missing_ok=True)
    print(f'APPLIED: archived {len(docs)} markdown files; retired {len(root_release_files)} old root release files.')
    return 0
if __name__=='__main__': raise SystemExit(main())
