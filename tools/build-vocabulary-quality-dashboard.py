#!/usr/bin/env python3
"""Read-only consolidated vocabulary, glossary and relationship quality dashboard."""
from __future__ import annotations
import argparse, importlib.util, json, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def norm(value):
    return ' '.join(unicodedata.normalize('NFKC', str(value or '')).split()).casefold()

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None: raise RuntimeError('cannot load ' + str(path))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

def build(root=ROOT):
    root = Path(root).resolve()
    manifest = json.loads((root / 'data/manifest.json').read_text(encoding='utf-8'))
    glossary_doc = json.loads((root / 'data/related-terms.json').read_text(encoding='utf-8'))
    rows = glossary_doc.get('terms', []) if isinstance(glossary_doc, dict) else []
    quality_mod = load_module('dashboard_glossary_quality', root / 'tools/audit-related-glossary-quality.py')
    relation_mod = load_module('dashboard_relation_graph', root / 'tools/audit-vocabulary-relationship-graph.py')
    family_mod = load_module('dashboard_word_family', root / 'tools/audit-word-family-graph.py')
    quality = quality_mod.audit(rows)
    vocab_files = sorted((root / 'data/vocabulary').glob('[A-Z].json'))
    relation = relation_mod.audit(vocab_files)
    family = family_mod.load_source(root)
    references = Counter(); anchors = defaultdict(set)
    for ref in relation.get('dangling_references', []):
        key = norm(ref.get('target'))
        if key: references[key] += 1; anchors[key].add(str(ref.get('source') or ''))
    glossary_keys = {norm(row.get('term')) for row in rows if isinstance(row, dict) and norm(row.get('term'))}
    missing = []
    for key, count in references.items():
        if key not in glossary_keys:
            missing.append({'term': key, 'references': count, 'sourceHeadwords': sorted(x for x in anchors[key] if x)})
    missing.sort(key=lambda x: (-x['references'], x['term']))
    flagged_by_index = {item['index']: item for item in quality.get('flagged', [])}
    queue = []
    for index, row in enumerate(rows):
        flag = flagged_by_index.get(index)
        if not flag: continue
        key = norm(row.get('term')) if isinstance(row, dict) else ''
        queue.append({'index': index, 'term': row.get('term', '') if isinstance(row, dict) else '',
                      'priority': flag.get('priority', 'low'), 'issues': list(flag.get('issues', [])),
                      'relationReferences': references.get(key, 0),
                      'definitionEn': row.get('definition_en', '') if isinstance(row, dict) else ''})
    queue.sort(key=lambda x: (-x['relationReferences'], {'high': 0, 'medium': 1, 'low': 2}.get(x['priority'], 3), norm(x['term']), x['index']))
    return {
      'schemaVersion': 1, 'release': manifest.get('version', 'unknown'), 'readOnly': True,
      'glossary': {'entries': len(rows), 'flaggedEntries': quality.get('flagged_entries', 0),
                   'issueCounts': quality.get('issue_counts', {}), 'priorityCounts': quality.get('priority_counts', {}),
                   'duplicateGroups': len(quality.get('duplicates', [])), 'containerIssue': quality.get('container_issue')},
      'relationshipGraph': {'headwords': relation.get('headwords', 0), 'uniqueHeadwords': relation.get('unique_headwords', 0),
                   'relations': relation.get('relation_count', 0), 'synonyms': relation.get('synonym_count', 0),
                   'antonyms': relation.get('antonym_count', 0), 'dangling': len(relation.get('dangling_references', [])),
                   'glossaryCovered': len(relation.get('glossary_covered_references', [])),
                   'unresolved': len(relation.get('unresolved_references', [])), 'selfReferences': len(relation.get('self_references', [])),
                   'nonreciprocalReview': len(relation.get('nonreciprocal_references', [])), 'malformed': len(relation.get('malformed', [])),
                   'duplicateHeadwordGroups': len(relation.get('duplicate_headwords', []))},
      'wordFamilyGraph': {'headwords': family.get('headwords', 0), 'headwordsWithFamily': family.get('headwords_with_family', 0),
                   'links': family.get('link_count', 0), 'missingTargets': len(family.get('missing_targets', [])),
                   'posMismatches': len(family.get('pos_mismatches', [])), 'meaningMismatches': len(family.get('meaning_mismatches', [])),
                   'nonreciprocalReview': len(family.get('nonreciprocal_links', [])), 'selfReferences': len(family.get('self_references', [])),
                   'duplicateLinks': len(family.get('duplicate_links', [])), 'malformed': len(family.get('malformed', []))},
      'missingGlossaryCandidates': missing, 'priorityQueue': queue,
      'guardrails': {'vocabularyChanged': False, 'glossaryChanged': False, 'questionBankChanged': False,
                     'answerKeysChanged': False, 'learnerStorageChanged': False, 'automaticDefinitionImport': False,
                     'reservePromotion': False, 'uiChanged': False, 'productionBranchChanged': False}
    }

def summarize(data):
    """Return compact machine-readable counts for CI and release evidence."""
    return {
        'schemaVersion': data['schemaVersion'],
        'release': data['release'],
        'readOnly': data['readOnly'],
        'glossary': data['glossary'],
        'relationshipGraph': data['relationshipGraph'],
        'wordFamilyGraph': data['wordFamilyGraph'],
        'missingGlossaryCandidateCount': len(data['missingGlossaryCandidates']),
        'priorityQueueCount': len(data['priorityQueue']),
        'guardrails': data['guardrails'],
    }

def render(data):
    g, r, w = data['glossary'], data['relationshipGraph'], data['wordFamilyGraph']
    lines = ['# Vocabulary & Glossary Quality Dashboard — v' + str(data['release']), '',
             '> Deterministic, read-only audit. Counts are screening signals, not editorial approval or learner mastery.', '',
             '## Glossary quality', '', '| Metric | Count |', '|---|---:|',
             '| Entries | ' + str(g['entries']) + ' |', '| Flagged entries | ' + str(g['flaggedEntries']) + ' |',
             '| Duplicate groups | ' + str(g['duplicateGroups']) + ' |', '| Issue counts | ' + json.dumps(g['issueCounts'], ensure_ascii=False, sort_keys=True) + ' |',
             '| Priority counts | ' + json.dumps(g['priorityCounts'], ensure_ascii=False, sort_keys=True) + ' |',
             '', '## Synonym / antonym graph', '', '| Metric | Count |', '|---|---:|']
    lines.extend('| ' + str(k) + ' | ' + str(v) + ' |' for k, v in r.items())
    lines += ['', '## Word Family graph', '', '| Metric | Count |', '|---|---:|']
    lines.extend('| ' + str(k) + ' | ' + str(v) + ' |' for k, v in w.items())
    lines += ['', '## Missing glossary candidates', '', '| Term | Relation references | Source headwords |', '|---|---:|---:|']
    lines.extend('| ' + x['term'].replace('|', '\\|') + ' | ' + str(x['references']) + ' | ' + str(len(x['sourceHeadwords'])) + ' |' for x in data['missingGlossaryCandidates'][:200])
    lines += ['', '## Priority review queue', '', '| Rank | Term | Priority | Relation references | Issues |', '|---:|---|---|---:|---|']
    lines.extend('| ' + str(i) + ' | ' + str(x['term']).replace('|', '\\|') + ' | ' + x['priority'] + ' | ' + str(x['relationReferences']) + ' | ' + ', '.join(x['issues']) + ' |' for i, x in enumerate(data['priorityQueue'][:300], 1))
    lines += ['', '## Safety invariants', '', '- No vocabulary, glossary, questions, choices, answer keys or learner IndexedDB records are written.',
              '- A missing glossary candidate is not a definition; no automatic definition copying or import is performed.',
              '- Non-reciprocal relations remain review signals, not automatic errors.',
              '- Listening and Reading reserve pools are not promoted by this dashboard.',
              '- No UI, Service Worker, deployment or production branch changes are made.', '']
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path); parser.add_argument('--json-output', type=Path)
    parser.add_argument('--summary-json', action='store_true', help='print compact machine-readable CI summary')
    args = parser.parse_args(); data = build(); report = render(data)
    if args.output: args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(report, encoding='utf-8')
    if args.json_output: args.json_output.parent.mkdir(parents=True, exist_ok=True); args.json_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if args.summary_json:
        print(json.dumps(summarize(data), ensure_ascii=False, sort_keys=True))
    else:
        print(report)
if __name__ == '__main__': main()