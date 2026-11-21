#!/usr/bin/env python3
"""Conservatively enrich exact-match Related Glossary rows from canonical vocabulary."""
from __future__ import annotations
import argparse, json, unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VOCAB=ROOT/'data/vocabulary'; GLOSS=ROOT/'data/related-terms.json'
def norm(value): return ' '.join(unicodedata.normalize('NFKC',str(value or '')).split()).casefold()
def load_vocab(directory=VOCAB):
 out={}
 for path in sorted(Path(directory).glob('[A-Z].json')):
  data=json.loads(path.read_text(encoding='utf-8'))
  for word in data.get('words',[]):
   key=norm(word.get('word'))
   if key: out.setdefault(key,word)
 return out
def eligible(row,vocab):
 word=vocab.get(norm(row.get('term')))
 if not word: return None
 senses=word.get('senses') or []
 if not senses or any(not str(s.get('meaning_vi') or '').strip() or not str(s.get('definition_en') or '').strip() for s in senses): return None
 missing_metadata=any(not str(row.get(k) or '').strip() for k in ('pos','sourceHeadword','sourceRelease'))
 missing_sense_index=len(senses)==1 and row.get('sourceSenseIndex') is None
 missing_single_definition=len(senses)==1 and not str(row.get('definition_en') or '').strip()
 if not (missing_metadata or missing_single_definition or missing_sense_index): return None
 return word,senses
def apply(rows,vocab,release):
 count=0
 for row in rows:
  found=eligible(row,vocab)
  if not found: continue
  word,senses=found
  if not str(row.get('definition_en') or '').strip() and len(senses)==1: row['definition_en']=str(senses[0]['definition_en']).strip()
  if not str(row.get('pos') or '').strip(): row['pos']='/'.join(dict.fromkeys(str(s.get('pos') or '').strip() for s in senses if s.get('pos')))
  if not str(row.get('sourceHeadword') or '').strip(): row['sourceHeadword']=word.get('word')
  if not str(row.get('sourceRelease') or '').strip(): row['sourceRelease']=release
  if len(senses)==1 and row.get('sourceSenseIndex') is None: row['sourceSenseIndex']=0
  if not str(row.get('source') or '').strip(): row['source']='canonical-vocabulary-senses'
  count+=1
 return count
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); a=ap.parse_args()
 data=json.loads(GLOSS.read_text(encoding='utf-8')); rows=data.get('terms',[]); vocab=load_vocab(); candidates=sum(eligible(r,vocab) is not None for r in rows)
 version=json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8')).get('version','unknown')
 if a.apply:
  n=apply(rows,vocab,version); GLOSS.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(f'Enriched {n} exact-match rows; canonical source release {version}.')
 else: print(f'Audit only: {len(rows)} glossary rows; safe exact-match enrichment candidates {candidates}; canonical release {version}.')
if __name__=='__main__': main()
