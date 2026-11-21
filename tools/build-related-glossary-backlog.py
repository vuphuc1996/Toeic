#!/usr/bin/env python3
"""Build a deterministic, source-headword traceable queue of unglossed related terms."""
import json
from collections import Counter, defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VOCAB = ROOT / 'data/vocabulary'
MANIFEST = ROOT / 'data/manifest.json'
GLOSS = ROOT / 'data/related-terms.json'
OUT_JSON = ROOT / 'docs/reports/related-glossary-backlog.json'
OUT_MD = ROOT / 'docs/reports/RELATED_GLOSSARY_BACKLOG.md'



def build_rows(references, synonym_refs, antonym_refs, headwords):
    """Merge spelling/case variants into one case-insensitive editorial queue row."""
    grouped = {}
    for raw_term, count in references.items():
        key = raw_term.strip().casefold()
        if not key:
            continue
        row = grouped.setdefault(key, {
            'term': raw_term.strip(), 'references': 0, 'synonymReferences': 0,
            'antonymReferences': 0, 'sourceHeadwords': set(),
        })
        # Use a deterministic display spelling when case variants are encountered.
        row['term'] = min((row['term'], raw_term.strip()), key=lambda value: (value.casefold(), value))
        row['references'] += count
        row['synonymReferences'] += synonym_refs.get(raw_term, 0)
        row['antonymReferences'] += antonym_refs.get(raw_term, 0)
        row['sourceHeadwords'].update(headwords.get(raw_term, set()))
    rows = []
    for row in grouped.values():
        anchors = sorted(row.pop('sourceHeadwords'), key=str.casefold)
        row['sourceHeadwordCount'] = len(anchors)
        row['sourceHeadwords'] = anchors
        rows.append(row)
    rows.sort(key=lambda x: (-x['references'], -x['sourceHeadwordCount'], -x['synonymReferences'], x['term'].casefold()))
    return rows


def build():
    gloss = json.loads(GLOSS.read_text(encoding='utf-8'))['terms']
    known = {x['term'].strip().casefold() for x in gloss if x.get('term')}
    references = Counter()
    synonym_refs = Counter()
    antonym_refs = Counter()
    headwords = defaultdict(set)
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    for item in manifest.get('letters', []):
        path = ROOT / item['file'].replace('./', '', 1)
        data = json.loads(path.read_text(encoding='utf-8'))
        for word in data.get('words', []):
            if not isinstance(word, dict):
                continue
            headword = str(word.get('word') or word.get('term') or '').strip()
            for sense in word.get('senses', []):
                for field, counter in (('synonyms', synonym_refs), ('antonyms', antonym_refs)):
                    vals = sense.get(field) or []
                    if isinstance(vals, str):
                        vals = [vals]
                    for term in vals:
                        if isinstance(term, str) and term.strip():
                            normalized = term.strip().casefold()
                            if normalized not in known:
                                references[term.strip()] += 1
                                counter[term.strip()] += 1
                                if headword:
                                    headwords[term.strip()].add(headword)
    rows = build_rows(references, synonym_refs, antonym_refs, headwords)
    payload = {'schemaVersion': 2, 'glossaryCount': len(gloss), 'uniqueUnglossedTerms': len(rows),
              'uncoveredReferenceCount': sum(references.values()), 'terms': rows}
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True); OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = ['# Related-term Glossary Backlog', '', f'- Glossary entries: **{len(gloss)}**',
          f'- Unglossed unique terms: **{len(rows)}**', f'- Unglossed references: **{sum(references.values())}**',
          '- Queue priority: number of references, distinct source headwords, synonym references, then term.',
          '- Each row includes source headwords for editorial context; this is a review queue, not an automatic glossary import.',
          '', '## Prioritized terms', '', '| Term | References | Headwords | Synonym | Antonym | Source headwords |',
          '|---|---:|---:|---:|---:|---|']
    for row in rows:
        anchors = ', '.join(row['sourceHeadwords']).replace('|', '\\|')
        term = row['term'].replace('|', '\\|')
        md.append(f"| {term} | {row['references']} | {row['sourceHeadwordCount']} | {row['synonymReferences']} | {row['antonymReferences']} | {anchors} |")
    OUT_MD.write_text('\n'.join(md) + '\n', encoding='utf-8')
    return payload


if __name__ == '__main__':
    result = build()
    print(f"Glossary {result['glossaryCount']}; unique missing {result['uniqueUnglossedTerms']}; refs missing {result['uncoveredReferenceCount']}")
