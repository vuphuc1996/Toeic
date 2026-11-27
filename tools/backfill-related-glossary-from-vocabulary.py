#!/usr/bin/env python3
"""Audit and optionally backfill placeholder related-term glosses from canonical vocabulary.

Only exact case-insensitive headword matches with existing bilingual senses are eligible.
The tool never adds terms, changes relationships, or overwrites non-placeholder definitions.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB = ROOT / 'data/vocabulary'
GLOSSARY = ROOT / 'data/related-terms.json'
REPORT = ROOT / 'docs/reports/RELATED_GLOSSARY_BACKFILL_AUDIT_v2.95.25.md'
PLACEHOLDER = 'reference gloss for practice distractors.'
SOURCE = 'canonical-vocabulary-senses'


def load_vocabulary():
    by_term = {}
    for path in sorted(VOCAB.glob('[A-Z].json')):
        data = json.loads(path.read_text(encoding='utf-8'))
        for word in data.get('words', []):
            term = str(word.get('word') or '').strip()
            if term:
                by_term.setdefault(term.casefold(), word)
    return by_term


def eligible(row, vocabulary):
    if PLACEHOLDER not in str(row.get('definition_en') or '').casefold():
        return None
    word = vocabulary.get(str(row.get('term') or '').strip().casefold())
    if not word:
        return None
    senses = [s for s in word.get('senses', []) if s.get('meaning_vi') and s.get('definition_en')]
    if not senses:
        return None
    return word, senses


def replacement(row, word, senses):
    # Preserve the current Vietnamese gloss because it may be broader than one sense.
    # English definitions and POS come from the exact canonical headword's senses.
    defs = list(dict.fromkeys(str(s['definition_en']).strip() for s in senses))
    pos = list(dict.fromkeys(str(s.get('pos') or '').strip() for s in senses if s.get('pos')))
    row = dict(row)
    row['definition_en'] = ' / '.join(defs)
    if pos:
        row['pos'] = '/'.join(pos)
    row['source'] = SOURCE
    row['sourceHeadword'] = word.get('word')
    row['sourceRelease'] = '2.95.24'
    return row


def audit(rows, vocabulary, write_report=True):
    placeholders = [r for r in rows if PLACEHOLDER in str(r.get('definition_en') or '').casefold()]
    candidates = [r for r in placeholders if eligible(r, vocabulary)]
    report = [
        '# Related Glossary Backfill Audit — v2.95.25', '',
        f'- Placeholder English definitions: **{len(placeholders)}**',
        f'- Exact canonical-headword matches with bilingual senses: **{len(candidates)}**',
        f'- Placeholder entries remaining after safe backfill: **{len(placeholders)-len(candidates)}**',
        '- Policy: no external claims or invented definitions; candidates must match an existing canonical headword and use its bilingual sense data.',
        '- Backfill preserves the existing Vietnamese meaning, replaces only the placeholder English definition, sets POS from canonical senses, and records provenance.',
        '- No glossary term or relationship is created or deleted by this operation.', '',
        '## Eligible entries', '', '| Term | POS | Vietnamese gloss | English source definition |', '|---|---|---|---|'
    ]
    for row in candidates:
        word, senses = eligible(row, vocabulary)
        defs = ' / '.join(dict.fromkeys(s['definition_en'] for s in senses))
        pos = '/'.join(dict.fromkeys(s.get('pos','') for s in senses if s.get('pos')))
        defs_escaped = defs.replace('|', '\\|')
        report.append(f"| {row['term']} | {pos} | {row.get('meaning_vi','')} | {defs_escaped} |")
    report.extend(['', '## Not eligible', '', 'Entries without exact canonical headword matches or complete bilingual senses remain for editorial review. No automatic rewrite was applied to those entries.', ''])
    if write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text('\n'.join(report), encoding='utf-8')
    return len(placeholders), len(candidates)


def apply(rows, vocabulary):
    updated = 0
    for row in rows:
        candidate = eligible(row, vocabulary)
        if candidate:
            word, senses = candidate
            updated_row = replacement(row, word, senses)
            row.clear(); row.update(updated_row)
            updated += 1
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Replace eligible placeholder definitions; default is audit-only')
    args = parser.parse_args()
    data = json.loads(GLOSSARY.read_text(encoding='utf-8'))
    rows = data.get('terms', [])
    vocab = load_vocabulary()
    placeholders, candidates = audit(rows, vocab)
    if args.apply:
        count = apply(rows, vocab)
        GLOSSARY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'Backfilled {count} entries; {placeholders-count} placeholders remain. Audit report: {REPORT.relative_to(ROOT)}')
    else:
        print(f'Audit only: {placeholders} placeholders; {candidates} exact-match candidates; report: {REPORT.relative_to(ROOT)}')

if __name__ == '__main__':
    main()
