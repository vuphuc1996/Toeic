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
    notes=[]
    for p in ROOT.glob('V*_UPDATE_NOTES.txt'):
        m=re.fullmatch(r'V(\d+\.\d+\.\d+)_UPDATE_NOTES\.txt',p.name)
        if m and m.group(1) not in keep: notes.append(p)
    docs=[]
    for folder in [ROOT/'docs/batches',ROOT/'docs/reports']:
        if not folder.exists(): continue
        for p in folder.glob('*.md'):
            versions=set(re.findall(r'v(\d+\.\d+\.\d+)',p.name))
            if not versions or not (versions & keep): docs.append(p)
    print(f'Current={current}; keep={sorted(keep)}')
    for p in docs: print('ARCHIVE + RETIRE',p.relative_to(ROOT))
    for p in notes: print('RETIRE',p.relative_to(ROOT))
    if not args.apply:
        print(f'DRY RUN: {len(docs)} markdown files and {len(notes)} root notes would be retired.')
        return 0
    ARCHIVE.parent.mkdir(parents=True,exist_ok=True)
    existing=ARCHIVE.read_text(encoding='utf-8') if ARCHIVE.exists() else '# Consolidated Project History\n'
    additions=[]
    for p in docs:
        rel=p.relative_to(ROOT).as_posix()
        marker=f'## Archived source: `{rel}`'
        if marker not in existing:
            additions.append(f'\n---\n\n{marker}\n\n{p.read_text(encoding="utf-8")}\n')
    if additions: ARCHIVE.write_text(existing+'\n'.join(additions),encoding='utf-8')
    for p in docs+notes: p.unlink(missing_ok=True)
    print(f'APPLIED: archived {len(docs)} markdown files; retired {len(notes)} old release notes.')
    return 0
if __name__=='__main__': raise SystemExit(main())
