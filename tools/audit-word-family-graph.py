#!/usr/bin/env python3
"""Read-only audit of canonical derivational word-family links and their sense anchors."""
from __future__ import annotations
import argparse, json, re, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def norm(value: object) -> str:
    return ' '.join(unicodedata.normalize('NFKC', str(value or '')).split()).casefold()

def split_pos(value: object) -> set[str]:
    return {part.strip().casefold() for part in re.split(r'[/,]', str(value or '')) if part.strip()}

def audit_data(inputs):
    records: dict[str, dict] = {}
    duplicate_headwords = []
    malformed = []
    for filename, data in inputs:
        words = data.get('words') if isinstance(data, dict) else None
        if not isinstance(words, list):
            malformed.append({'file': filename, 'issue': 'words-not-list'})
            continue
        for index, word in enumerate(words):
            if not isinstance(word, dict) or not norm(word.get('word')) or not isinstance(word.get('senses'), list):
                malformed.append({'file': filename, 'index': index, 'issue': 'malformed-word-record'})
                continue
            key = norm(word.get('word'))
            if key in records:
                duplicate_headwords.append({'word': word.get('word'), 'first_file': records[key]['__file__'], 'duplicate_file': filename})
            else:
                copy = dict(word); copy['__file__'] = filename; records[key] = copy

    links = []
    duplicate_links = []
    for source_key, source in records.items():
        family = source.get('word_family', [])
        if family is None:
            family = []
        if not isinstance(family, list):
            malformed.append({'file': source['__file__'], 'word': source.get('word'), 'issue': 'word-family-not-list'})
            continue
        seen = set()
        for index, item in enumerate(family):
            if not isinstance(item, dict) or not all(norm(item.get(k)) for k in ('word', 'pos', 'meaning_vi')):
                malformed.append({'file': source['__file__'], 'word': source.get('word'), 'index': index, 'issue': 'malformed-family-link'})
                continue
            target_key = norm(item['word'])
            if target_key in seen:
                duplicate_links.append({'source': source['word'], 'target': item['word']})
            seen.add(target_key)
            links.append({'source': source['word'], 'source_key': source_key, 'target': str(item['word']).strip(),
                          'target_key': target_key, 'pos': str(item['pos']).strip(),
                          'meaning_vi': str(item['meaning_vi']).strip(), 'file': source['__file__'], 'index': index})

    missing_targets, pos_mismatches, meaning_mismatches, nonreciprocal = [], [], [], []
    for link in links:
        target = records.get(link['target_key'])
        if target is None:
            missing_targets.append({k: link[k] for k in ('source', 'target', 'pos', 'file')})
            continue
        requested = split_pos(link['pos'])
        target_pos = set().union(*(split_pos(s.get('pos')) for s in target.get('senses', []) if isinstance(s, dict)))
        if not requested or not requested.issubset(target_pos):
            pos_mismatches.append({**{k: link[k] for k in ('source', 'target', 'pos', 'file')}, 'target_pos': sorted(target_pos)})
        candidates = [s for s in target.get('senses', []) if isinstance(s, dict) and split_pos(s.get('pos')) & requested]
        target_meanings = {norm(s.get('meaning_vi')) for s in candidates if norm(s.get('meaning_vi'))}
        if norm(link['meaning_vi']) not in target_meanings:
            meaning_mismatches.append({**{k: link[k] for k in ('source', 'target', 'meaning_vi', 'file')},
                                       'target_meanings': [s.get('meaning_vi') for s in candidates if norm(s.get('meaning_vi'))]})
        reverse = any(isinstance(row, dict) and norm(row.get('word')) == link['source_key']
                      for row in (target.get('word_family') or []) if isinstance(target.get('word_family'), list))
        if not reverse:
            nonreciprocal.append({k: link[k] for k in ('source', 'target', 'pos', 'file')})

    return {
        'headwords': len(records), 'duplicate_headwords': duplicate_headwords,
        'link_count': len(links), 'headwords_with_family': len({x['source_key'] for x in links}),
        'missing_targets': missing_targets, 'pos_mismatches': pos_mismatches,
        'meaning_mismatches': meaning_mismatches, 'nonreciprocal_links': nonreciprocal,
        'duplicate_links': duplicate_links, 'malformed': malformed,
    }

def load_source(root: Path):
    manifest = json.loads((root / 'data/manifest.json').read_text(encoding='utf-8'))
    inputs = []
    for item in manifest.get('letters', []):
        path = root / item['file'].replace('./', '', 1)
        inputs.append((path.name, json.loads(path.read_text(encoding='utf-8'))))
    return audit_data(inputs)

def render(report):
    lines = [
        '# Word Family Graph Audit — v2.95.67', '',
        f"- Canonical headwords: **{report['headwords']}**",
        f"- Headwords with at least one family link: **{report['headwords_with_family']}**",
        f"- Directed family links: **{report['link_count']}**",
        f"- Missing canonical targets: **{len(report['missing_targets'])}**",
        f"- Target POS mismatches: **{len(report['pos_mismatches'])}**",
        f"- Vietnamese sense-anchor mismatches: **{len(report['meaning_mismatches'])}**",
        f"- Non-reciprocal links: **{len(report['nonreciprocal_links'])}**",
        f"- Duplicate links: **{len(report['duplicate_links'])}**",
        f"- Duplicate headwords: **{len(report['duplicate_headwords'])}**",
        f"- Malformed records/links: **{len(report['malformed'])}**", '',
        '> This is a read-only structural and sense-anchor audit. Non-reciprocal links and meaning mismatches are editorial review flags, not automatic proof that a relationship is wrong. No canonical records are rewritten by this tool.', ''
    ]
    for key, title, columns in [
        ('missing_targets','Missing canonical targets',('source','target','pos','file')),
        ('pos_mismatches','Target POS mismatches',('source','target','pos','target_pos','file')),
        ('meaning_mismatches','Vietnamese sense-anchor mismatches',('source','target','meaning_vi','target_meanings')),
        ('nonreciprocal_links','Non-reciprocal links — review only',('source','target','pos','file')),
    ]:
        lines += [f'## {title}', '', '| ' + ' | '.join(columns) + ' |', '|' + '|'.join(['---']*len(columns)) + '|']
        for row in report[key][:200]:
            vals=[]
            for col in columns:
                value=row.get(col,'')
                if isinstance(value,list): value='; '.join(str(x) for x in value)
                vals.append(str(value).replace('|','\\|').replace('\n',' '))
            lines.append('| ' + ' | '.join(vals) + ' |')
        if len(report[key]) > 200:
            lines.append(f"| … | {len(report[key])-200} additional rows omitted from this Markdown view |")
        lines.append('')
    return '\n'.join(lines)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--json-output',type=Path)
    args=parser.parse_args()
    report=load_source(args.root.resolve())
    text=render(report)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text,encoding='utf-8')
    if args.json_output:
        args.json_output.parent.mkdir(parents=True,exist_ok=True); args.json_output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(text)
if __name__ == '__main__': main()
