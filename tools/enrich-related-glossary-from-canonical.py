#!/usr/bin/env python3
"""Add missing related-term glosses only from exact canonical bilingual headwords.

Strict enrichment: exact normalized headword match, complete bilingual senses,
no existing glossary row, deterministic output, and provenance on every addition.
Default is audit-only; --apply writes additions.
"""
from __future__ import annotations
import argparse, json, re, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VOCAB=ROOT/'data/vocabulary'
GLOSS=ROOT/'data/related-terms.json'
REPORT=ROOT/'docs/reports/RELATED_GLOSSARY_CANONICAL_ENRICHMENT_v2.95.29.md'
SOURCE='canonical-vocabulary-senses'
SOURCE_RELEASE='2.95.28'

def norm(value):
    return ' '.join(unicodedata.normalize('NFKC',str(value or '')).split()).casefold()

def load_vocab():
    vocab={}
    for path in sorted(VOCAB.glob('[A-Z].json')):
        data=json.loads(path.read_text(encoding='utf-8'))
        for word in data.get('words',[]):
            term=str(word.get('word') or '').strip()
            if term: vocab.setdefault(norm(term),word)
    return vocab

def candidate_rows(gloss_rows,vocab):
    present={norm(row.get('term')) for row in gloss_rows if isinstance(row,dict)}
    # Build term set from vocabulary relationships, but only terms with exact canonical entries.
    references=set()
    for word in vocab.values():
        for sense in word.get('senses',[]):
            for field in ('synonyms','antonyms'):
                vals=sense.get(field) or []
                if isinstance(vals,str): vals=[vals]
                for term in vals:
                    if isinstance(term,str) and norm(term): references.add(norm(term))
    rows=[]
    for key in sorted(references):
        if key in present: continue
        word=vocab.get(key)
        if not word: continue
        senses=word.get('senses') or []
        # Conservative: every canonical sense must contain both languages, no partial copy.
        if not senses or any(not str(s.get('meaning_vi') or '').strip() or not str(s.get('definition_en') or '').strip() for s in senses): continue
        terms=sorted({str(t).strip() for s in senses for field in ('synonyms','antonyms') for t in (s.get(field) or []) if isinstance(t,str) and norm(t)==key},key=lambda x:(norm(x),x))
        term=str(word.get('word') or terms[0] or '').strip()
        if not term: continue
        rows.append({'term':term,'meaning_vi':' / '.join(dict.fromkeys(str(s['meaning_vi']).strip() for s in senses)),
          'definition_en':' / '.join(dict.fromkeys(str(s['definition_en']).strip() for s in senses)),
          'pos':'/'.join(dict.fromkeys(str(s.get('pos') or '').strip() for s in senses if s.get('pos'))),
          'source':SOURCE,'sourceHeadword':word.get('word'),'sourceRelease':SOURCE_RELEASE})
    rows.sort(key=lambda r:norm(r['term']))
    return rows

def render(rows, existing_count):
    lines=['# Related Glossary Canonical Enrichment — v2.95.29','',f'- Existing glossary entries: **{existing_count}**',f'- Exact canonical bilingual additions eligible: **{len(rows)}**',
      '- Eligibility: referenced by synonym/antonym, exact NFKC/casefold headword, every canonical sense has Vietnamese and English, not already present.',
      '- Applied fields are copied from canonical senses; multi-sense entries are joined with ` / `, not newly authored.',
      '- Provenance recorded per addition: `canonical-vocabulary-senses`, source headword, source release `2.95.28`.','',
      '| Term | POS | Vietnamese | Canonical English senses |','|---|---|---|---|']
    for r in rows:
        safe=lambda x:str(x).replace('|',r'\|')
        lines.append(f"| {safe(r['term'])} | {safe(r['pos'])} | {safe(r['meaning_vi'])} | {safe(r['definition_en'])} |")
    lines+=['','> This is a deterministic data transfer, not AI-generated definitions. Existing entries and relation arrays are not overwritten.','']
    return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--apply',action='store_true'); args=ap.parse_args()
    data=json.loads(GLOSS.read_text(encoding='utf-8')); rows=data.get('terms',[]); vocab=load_vocab(); candidates=candidate_rows(rows,vocab)
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text(render(candidates,len(rows)),encoding='utf-8')
    if args.apply:
        data['terms'].extend(candidates); GLOSS.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"Existing {len(rows)}; eligible {len(candidates)}; {'added' if args.apply else 'audit-only'} {len(candidates)}; report {REPORT.relative_to(ROOT)}")
if __name__=='__main__': main()
