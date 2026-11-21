#!/usr/bin/env python3
"""Read-only cross-file audit of canonical synonym/antonym relationship graph."""
from __future__ import annotations
import argparse, json, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VOCAB=ROOT/'data/vocabulary'

def norm(value):
    return ' '.join(unicodedata.normalize('NFKC', str(value or '')).split()).casefold()

def audit(files):
    inputs=[]
    for path in sorted(files, key=lambda p:p.name):
        try: inputs.append((path.name,json.loads(path.read_text(encoding='utf-8'))))
        except Exception as e: inputs.append((path.name,{'__invalid_json__':str(e)}))
    glossary=[]
    glossary_path=ROOT/'data/related-terms.json'
    if glossary_path.exists():
        try: glossary=[row.get('term','') for row in json.loads(glossary_path.read_text(encoding='utf-8')).get('terms',[]) if isinstance(row,dict)]
        except Exception: glossary=[]
    return audit_data(inputs,glossary)

def audit_data(inputs,glossary_terms=None):
    records=[]; index={}; malformed=[]
    for filename,data in inputs:
        words=data.get('words') if isinstance(data,dict) else None
        if not isinstance(words,list):
            malformed.append({'file':filename,'issue':'words-not-list'}); continue
        for wi,w in enumerate(words):
            if not isinstance(w,dict) or not str(w.get('word') or '').strip() or not isinstance(w.get('senses'),list):
                malformed.append({'file':filename,'word_index':wi,'issue':'malformed-word-record'}); continue
            key=norm(w['word']); index.setdefault(key,[]).append({'word':w['word'],'file':filename,'index':wi})
            for si,s in enumerate(w['senses']):
                if not isinstance(s,dict):
                    malformed.append({'file':filename,'word':w['word'],'sense_index':si,'issue':'malformed-sense'}); continue
                for reltype in ('synonyms','antonyms'):
                    vals=s.get(reltype,[])
                    if vals is None: vals=[]
                    if not isinstance(vals,list):
                        malformed.append({'file':filename,'word':w['word'],'sense_index':si,'relation':reltype,'issue':'relation-not-list'}); continue
                    seen=set()
                    for ri,term in enumerate(vals):
                        target=norm(term)
                        if not target:
                            malformed.append({'file':filename,'word':w['word'],'sense_index':si,'relation':reltype,'relation_index':ri,'issue':'blank-reference'}); continue
                        if target in seen:
                            malformed.append({'file':filename,'word':w['word'],'sense_index':si,'relation':reltype,'reference':term,'issue':'duplicate-reference'}); continue
                        seen.add(target)
                        records.append({'source':w['word'],'source_norm':key,'sense_index':si,'relation':reltype,'target':str(term).strip(),'target_norm':target,'file':filename})
    duplicate_headwords=[{'normalized':k,'entries':v} for k,v in sorted(index.items()) if len(v)>1]
    glossary_index={norm(t) for t in (glossary_terms or []) if norm(t)}
    dangling=[]; glossary_covered=[]; unresolved=[]; selfrefs=[]; reciprocal_missing=[]
    for r in records:
        if r['target_norm'] not in index:
            item={k:r[k] for k in ('source','sense_index','relation','target','file')}
            dangling.append(item)
            (glossary_covered if r['target_norm'] in glossary_index else unresolved).append(item)
        if r['target_norm']==r['source_norm']: selfrefs.append({k:r[k] for k in ('source','sense_index','relation','target','file')})
        if r['target_norm'] in index and r['target_norm']!=r['source_norm']:
            counterpart=r['relation']; reciprocal=any(x['source_norm']==r['target_norm'] and x['target_norm']==r['source_norm'] and x['relation']==counterpart for x in records)
            if not reciprocal: reciprocal_missing.append({k:r[k] for k in ('source','sense_index','relation','target','file')})
    return {'headwords':sum(len(v) for v in index.values()),'unique_headwords':len(index),'duplicate_headwords':duplicate_headwords,'relation_count':len(records),'synonym_count':sum(r['relation']=='synonyms' for r in records),'antonym_count':sum(r['relation']=='antonyms' for r in records),'dangling_references':dangling,'glossary_covered_references':glossary_covered,'unresolved_references':unresolved,'missing_canonical_unique_terms':sorted({norm(r['target']) for r in dangling}),'unresolved_unique_terms':sorted({norm(r['target']) for r in unresolved}),'self_references':selfrefs,'nonreciprocal_references':reciprocal_missing,'malformed':malformed}

def render(d):
    lines=['# Vocabulary Relationship Graph Audit (read-only)','',f"- Headword records: **{d['headwords']}**",f"- Unique normalized headwords: **{d['unique_headwords']}**",f"- Duplicate normalized headword groups: **{len(d['duplicate_headwords'])}**",f"- Relation references: **{d['relation_count']}**",f"- Synonym references: **{d['synonym_count']}**",f"- Antonym references: **{d['antonym_count']}**",f"- Missing canonical headword references: **{len(d['dangling_references'])}**",f"- Covered by related glossary: **{len(d['glossary_covered_references'])}**",f"- Unresolved beyond glossary: **{len(d['unresolved_references'])}** ({len(d['unresolved_unique_terms'])} unique terms)",f"- Self-references: **{len(d['self_references'])}**",f"- Non-reciprocal references: **{len(d['nonreciprocal_references'])}**",f"- Malformed items: **{len(d['malformed'])}**",'', '## References absent from canonical vocabulary (some may be glossary-covered)','', '| Source | Sense | Relation | Target | File |','|---|---:|---|---|---|']
    for r in d['dangling_references']: lines.append(f"| {r['source']} | {r['sense_index']} | {r['relation']} | {r['target']} | {r['file']} |")
    lines += ['', '## Unresolved targets (not in canonical vocabulary or related glossary)', '', '| Source | Sense | Relation | Target | File |','|---|---:|---|---|---|']
    for r in d['unresolved_references']: lines.append(f"| {r['source']} | {r['sense_index']} | {r['relation']} | {r['target']} | {r['file']} |")
    lines += ['', '## Self-references','', '| Source | Sense | Relation | Target |','|---|---:|---|---|']
    for r in d['self_references']: lines.append(f"| {r['source']} | {r['sense_index']} | {r['relation']} | {r['target']} |")
    lines += ['', '## Non-reciprocal references (review only)','', '| Source | Sense | Relation | Target |','|---|---:|---|---|']
    for r in d['nonreciprocal_references']: lines.append(f"| {r['source']} | {r['sense_index']} | {r['relation']} | {r['target']} |")
    lines += ['', '## Malformed records','', '| File | Word | Issue |','|---|---|---|']
    for r in d['malformed']: lines.append(f"| {r.get('file','')} | {r.get('word','')} | {r['issue']} |")
    lines += ['', '> This audit is read-only. Targets missing from canonical vocabulary may be valid if present in the related glossary. Non-reciprocal relationships are review flags only because sense-specific relations may be intentionally asymmetric.', '']
    return '\n'.join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--output',type=Path); p.add_argument('--json-output',type=Path); a=p.parse_args()
    d=audit(list(VOCAB.glob('[A-Z].json'))); report=render(d)
    if a.output: a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(report,encoding='utf-8')
    if a.json_output: a.json_output.parent.mkdir(parents=True,exist_ok=True); a.json_output.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(report)
if __name__=='__main__': main()
