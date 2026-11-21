#!/usr/bin/env python3
"""Read-only quality flag audit for related-term glossary entries; never edits data."""
from __future__ import annotations
import argparse, json, re, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
GLOSSARY = ROOT / 'data/related-terms.json'
PLACEHOLDER_PATTERNS = (
    re.compile(r'^reference gloss for\b', re.I),
    re.compile(r'^(?:tbd|todo|placeholder|definition pending|unknown|n/?a|not available|no definition)\.?$', re.I),
    re.compile(r'^(?:generic|temporary|sample) definition\b', re.I),
)


def flags(row):
    term = str(row.get('term') or '').strip()
    definition = str(row.get('definition_en') or '').strip()
    out = []
    if not definition:
        out.append('missing-definition')
    elif any(p.search(definition) for p in PLACEHOLDER_PATTERNS):
        out.append('placeholder-definition')
    if definition and term and definition.casefold().rstrip('.!') == term.casefold():
        out.append('definition-equals-term')
    if definition and len(definition.split()) < 4 and 'placeholder-definition' not in out:
        out.append('short-definition-review')
    if not str(row.get('meaning_vi') or '').strip():
        out.append('missing-meaning-vi')
    if not str(row.get('pos') or '').strip():
        out.append('missing-pos')
    if not str(row.get('source') or '').strip():
        out.append('missing-source-provenance')
    return out


def review_priority(issues):
    """Assign an actionable triage level without altering glossary data."""
    issues = set(issues)
    if issues & {'malformed-entry', 'missing-definition', 'placeholder-definition', 'definition-equals-term', 'duplicate-normalized-term'}:
        return 'high'
    if issues & {'missing-meaning-vi', 'missing-pos', 'missing-source-provenance'}:
        return 'medium'
    if issues:
        return 'low'
    return 'none'

def normalize_term(value):
    # Compatibility normalization, whitespace collapse, and case-folding for duplicate screening.
    return ' '.join(unicodedata.normalize('NFKC', str(value or '')).split()).casefold()

def audit(rows):
    container_issue = None
    if not isinstance(rows, list):
        container_issue = 'terms-not-list'
        rows = []
    flagged = []
    counts = {}
    duplicate_terms = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            row = {'term': '', 'definition_en': '', 'meaning_vi': '', 'pos': '', 'source': ''}
            issues = ['malformed-entry']
        else:
            issues = flags(row)
        term = str(row.get('term') or '').strip()
        normalized = normalize_term(term)
        if normalized:
            duplicate_terms.setdefault(normalized, []).append(index)
        for issue in issues:
            counts[issue] = counts.get(issue, 0) + 1
        if issues:
            flagged.append({'index': index, 'term': row.get('term', ''), 'issues': issues,
                           'definition_en': row.get('definition_en', ''),
                           'meaning_vi': row.get('meaning_vi', ''), 'priority': review_priority(issues)})
    duplicates = []
    for normalized, indices in sorted(duplicate_terms.items()):
        if len(indices) > 1:
            duplicates.append({'term': normalized, 'indices': indices, 'count': len(indices)})
            counts['duplicate-normalized-term'] = counts.get('duplicate-normalized-term', 0) + len(indices)
            for index in indices:
                existing = next((item for item in flagged if item['index'] == index), None)
                if existing:
                    existing['issues'].append('duplicate-normalized-term')
                    existing['priority'] = review_priority(existing['issues'])
                else:
                    row = rows[index]
                    flagged.append({'index': index, 'term': row.get('term', ''),
                                   'issues': ['duplicate-normalized-term'],
                                   'definition_en': row.get('definition_en', ''),
                                   'meaning_vi': row.get('meaning_vi', ''), 'priority': review_priority(['duplicate-normalized-term'])})
    return {'entries': len(rows), 'flagged_entries': len(flagged),
            'container_issue': container_issue,
            'issue_counts': dict(sorted(counts.items())), 'duplicates': duplicates,
            'priority_counts': {level: sum(1 for item in flagged if item.get('priority') == level) for level in ('high', 'medium', 'low')},
            'flagged': sorted(flagged, key=lambda x: ({'high': 0, 'medium': 1, 'low': 2}.get(x.get('priority'), 3), x['index']))}


def render(data):
    lines = ['# Related Glossary Quality Flags (read-only)', '',
             f"- Entries scanned: **{data['entries']}**",
             f"- Entries with one or more review flags: **{data['flagged_entries']}**",
             f"- Input container issue: **{data.get('container_issue') or 'none'}**", '',
             '## Review priority', '', '| Priority | Entries | Meaning |', '|---|---:|---|', f"| High | **{data.get('priority_counts', {}).get('high', 0)}** | Definition, placeholder, malformed, duplicate or term-echo risk |", f"| Medium | **{data.get('priority_counts', {}).get('medium', 0)}** | Missing POS, Vietnamese meaning or provenance |", f"| Low | **{data.get('priority_counts', {}).get('low', 0)}** | Remaining editorial review flags |", '', '## Issue counts', '', '| Flag | Entries |', '|---|---:|']
    for key, count in data['issue_counts'].items():
        lines.append(f'| {key} | {count} |')
    lines += ['', '## Duplicate normalized terms', '', f"- Duplicate groups: **{len(data.get('duplicates', []))}**", '', '| Normalized term | Entry indices | Count |', '|---|---|---:|']
    for duplicate in data.get('duplicates', []):
        lines.append(f"| {duplicate['term']} | {', '.join(str(i) for i in duplicate['indices'])} | {duplicate['count']} |")
    lines += ['', '## Review queue', '', '| Priority | Index | Term | Flags | English definition | Vietnamese gloss |', '|---|---:|---|---|---|---|']
    for row in data['flagged']:
        term = str(row['term']).replace('|', r'\|')
        definition = str(row['definition_en']).replace('|', r'\|')
        meaning = str(row['meaning_vi']).replace('|', r'\|')
        lines.append(f"| {row.get('priority', 'low')} | {row['index']} | {term} | {', '.join(row['issues'])} | {definition} | {meaning} |")
    lines += ['', '> Flags are screening aids, not automatic verdicts. The tool is read-only and does not change glossary entries.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Write markdown report')
    parser.add_argument('--json-output', type=Path, help='Write structured JSON audit')
    args = parser.parse_args()
    rows = json.loads(GLOSSARY.read_text(encoding='utf-8')).get('terms', [])
    data = audit(rows)
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
