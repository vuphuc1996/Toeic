#!/usr/bin/env python3
"""Build a deterministic, read-only priority queue for incomplete related-glossary entries.

Priority combines quality flags with the number of synonym/antonym references and the
number of distinct canonical headwords that point to each term. It never edits glossary data.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUALITY_TOOL = ROOT / 'tools/audit-related-glossary-quality.py'
MANIFEST = ROOT / 'data/manifest.json'
GLOSSARY = ROOT / 'data/related-terms.json'


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def load_quality_module():
    spec = importlib.util.spec_from_file_location('related_glossary_quality_audit', QUALITY_TOOL)
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot load related glossary quality audit')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def collect_references():
    manifest = load_json(MANIFEST)
    counts = Counter()
    anchors = defaultdict(set)
    for entry in manifest.get('letters', []):
        path = ROOT / str(entry['file']).removeprefix('./')
        data = load_json(path)
        for word in data.get('words', []):
            if not isinstance(word, dict):
                continue
            headword = str(word.get('word') or word.get('term') or '').strip()
            for sense in word.get('senses', []) if isinstance(word.get('senses'), list) else []:
                if not isinstance(sense, dict):
                    continue
                for field in ('synonyms', 'antonyms'):
                    values = sense.get(field) or []
                    if isinstance(values, str):
                        values = [values]
                    for value in values:
                        if isinstance(value, str) and value.strip():
                            key = value.strip().casefold()
                            counts[key] += 1
                            if headword:
                                anchors[key].add(headword)
    return counts, anchors


def build(glossary_rows=None, reference_counts=None, source_headwords=None):
    glossary_rows = load_json(GLOSSARY).get('terms', []) if glossary_rows is None else glossary_rows
    if reference_counts is None or source_headwords is None:
        reference_counts, source_headwords = collect_references()
    quality = load_quality_module()
    audit = quality.audit(glossary_rows)
    rows = []
    for flagged in audit['flagged']:
        term = str(flagged.get('term') or '').strip()
        key = term.casefold()
        refs = int(reference_counts.get(key, 0))
        anchors = sorted(source_headwords.get(key, set()), key=lambda x: (x.casefold(), x))
        issues = list(flagged.get('issues') or [])
        blocking = bool(set(issues) & {'missing-definition', 'placeholder-definition', 'malformed-entry', 'duplicate-normalized-term'})
        if blocking:
            tier = 'definition-blocker'
        elif 'missing-pos' in issues:
            tier = 'metadata-review'
        else:
            tier = 'editorial-review'
        rows.append({
            'term': term,
            'glossaryIndex': flagged['index'],
            'priority': flagged['priority'],
            'tier': tier,
            'issues': issues,
            'relationReferences': refs,
            'distinctSourceHeadwords': len(anchors),
            'sourceHeadwords': anchors,
            'definitionEn': flagged.get('definition_en', ''),
            'meaningVi': flagged.get('meaning_vi', ''),
        })
    rows.sort(key=lambda row: (
        -row['relationReferences'],
        -row['distinctSourceHeadwords'],
        {'high': 0, 'medium': 1, 'low': 2}.get(row['priority'], 3),
        row['term'].casefold(),
    ))
    tier_counts = {tier: sum(row['tier'] == tier for row in rows)
                   for tier in ('definition-blocker', 'metadata-review', 'editorial-review')}
    return {
        'schemaVersion': 1,
        'glossaryEntries': len(glossary_rows),
        'flaggedEntries': len(rows),
        'referencedFlaggedEntries': sum(row['relationReferences'] > 0 for row in rows),
        'relationReferencesAcrossFlaggedEntries': sum(row['relationReferences'] for row in rows),
        'tierCounts': tier_counts,
        'priorityPolicy': 'relation reference count desc; distinct source headwords desc; quality priority; term',
        'readOnly': True,
        'entries': rows,
    }


def render(data):
    lines = [
        '# Related Glossary Enrichment Queue (read-only)', '',
        f"- Glossary entries: **{data['glossaryEntries']}**",
        f"- Entries requiring review: **{data['flaggedEntries']}**",
        f"- Flagged entries used by relations: **{data['referencedFlaggedEntries']}**",
        f"- Relation references across flagged entries: **{data['relationReferencesAcrossFlaggedEntries']}**",
        '', '## Queue tiers', '', '| Tier | Entries | Scope |', '|---|---:|---|',
        f"| Definition blocker | {data['tierCounts']['definition-blocker']} | Missing or placeholder definitions, malformed/duplicate risks |",
        f"| Metadata review | {data['tierCounts']['metadata-review']} | POS or metadata gaps after definition blockers |",
        f"| Editorial review | {data['tierCounts']['editorial-review']} | Other quality flags requiring human review |",
        '', '## Prioritized queue', '',
        '| Rank | Term | References | Source headwords | Priority | Tier | Flags |',
        '|---:|---|---:|---:|---|---|---|',
    ]
    for rank, row in enumerate(data['entries'], 1):
        term = row['term'].replace('|', r'\|')
        flags = ', '.join(row['issues']).replace('|', r'\|')
        lines.append(f"| {rank} | {term} | {row['relationReferences']} | {row['distinctSourceHeadwords']} | {row['priority']} | {row['tier']} | {flags} |")
    lines += ['', '> Read-only research queue. Frequency indicates where a glossary gap is most exposed in the existing relation graph; it does not establish a definition or authorize automatic content insertion.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json-output', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = build()
    report = render(data)
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding='utf-8')
    print(report)

if __name__ == '__main__':
    main()
