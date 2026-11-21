#!/usr/bin/env python3
"""Read-only related glossary candidate audit; never edits project data."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLACEHOLDER_PATTERNS=(re.compile(r'^reference gloss for\b',re.I), re.compile(r'^(?:tbd|placeholder|definition pending|n/?a|not available)\.?$',re.I))

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def classify_definition(text):
    text=(text or '').strip()
    if not text: return 'missing'
    if any(pattern.search(text) for pattern in PLACEHOLDER_PATTERNS): return 'placeholder'
    return 'present'

def canonical_preview(word):
    if not word: return None
    senses=word.get('senses',[])
    return {'sense_count':len(senses),'senses':[{'pos':s.get('pos'),'meaning_vi':s.get('meaning_vi'),'definition_en':s.get('definition_en')} for s in senses]}

def collect():
    manifest=load(ROOT/'data/manifest.json'); vocab={}; refs={}
    for entry in manifest['letters']:
        data=load(ROOT/entry['file'].removeprefix('./'))
        for word in data['words']:
            key=word['word'].casefold(); vocab[key]=word
            for sense in word.get('senses',[]):
                for field in ('synonyms','antonyms'):
                    for term in sense.get(field,[]):
                        k=term.casefold(); refs[k]=refs.get(k,0)+1
    glossary=load(ROOT/'data/related-terms.json')['terms']; existing={r['term'].casefold():r for r in glossary}
    missing=[]
    for term,count in refs.items():
        if term in existing: continue
        canonical=vocab.get(term); preview=canonical_preview(canonical)
        tier=('single-sense-review' if preview and preview['sense_count']==1 else 'multi-sense-review' if preview else 'no-canonical-headword')
        missing.append({'term':term,'references':count,'canonical':bool(canonical),'tier':tier,'preview':preview})
    missing.sort(key=lambda x:(-x['references'],x['term']))
    definition_categories={key:[] for key in ('missing','placeholder','present')}
    for row in glossary: definition_categories[classify_definition(row.get('definition_en'))].append(row['term'])
    return {'vocabulary_count':len(vocab),'glossary_count':len(glossary),'referenced_distinct':len(refs),
            'covered':sum(1 for t in refs if t in existing),'referenced_occurrences':sum(refs.values()),
            'missing_distinct':len(missing),'missing_occurrences':sum(x['references'] for x in missing),
            'canonical_candidates':sum(1 for x in missing if x['canonical']),'missing':missing,
            'definition_categories':{k:sorted(v) for k,v in definition_categories.items()},
            'definition_category_counts':{k:len(v) for k,v in definition_categories.items()}}

def render(data):
    counts=data['definition_category_counts']
    lines=['# Related Glossary Candidate Audit (read-only)','',f"- Vocabulary headwords: **{data['vocabulary_count']}**",f"- Glossary entries: **{data['glossary_count']}**",f"- Referenced terms: **{data['referenced_distinct']}**",f"- Covered: **{data['covered']}**",f"- Missing unique terms: **{data['missing_distinct']}** ({data['missing_occurrences']} occurrences)",f"- Missing terms with canonical headword: **{data['canonical_candidates']}**",f"- Definition audit: **{counts['present']} present / {counts['missing']} missing / {counts['placeholder']} placeholder**",'', '## Missing candidate review tiers','', '| Term | References | Review tier | Canonical senses |','|---|---:|---|---:|']
    for row in data['missing'][:100]: lines.append(f"| {row['term']} | {row['references']} | {row['tier']} | {row['preview']['sense_count'] if row['preview'] else 0} |")
    lines+=['','## Definition audit','',f"- Missing English definitions: **{counts['missing']}**",f"- Placeholder definitions: **{counts['placeholder']}**",f"- Non-placeholder definitions: **{counts['present']}**",'', '> Audit-only: candidate tiers and canonical previews are review aids, not permission to copy meanings. No vocabulary or glossary data is modified.','']
    return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path); args=ap.parse_args()
    result=collect(); text=render(result)
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text,encoding='utf-8')
    print(text)
if __name__=='__main__': main()
