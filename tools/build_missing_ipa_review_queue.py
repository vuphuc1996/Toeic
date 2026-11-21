#!/usr/bin/env python3
"""Build a source-linked, non-mutating CMUdict IPA review queue for missing US IPA."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
OUT=ROOT/'docs/reports/MISSING_US_IPA_CMUdict_REVIEW_QUEUE.json'

def collect(records, dictionary):
    queue=[]
    for rid, record in records.items():
        phonetic=record.get('phonetic') or {}
        if (phonetic.get('us') or '').strip(): continue
        word=(record.get('word') or '').strip()
        key=word.casefold()
        if key not in dictionary:
            status='no_exact_dictionary_entry'; variants=[]
        else:
            unique=[]
            for pronunciation in dictionary[key]:
                value=list(pronunciation)
                if value not in unique: unique.append(value)
            variants=unique
            status='single_pronunciation_candidate' if len(variants)==1 else ('multiple_pronunciations_review' if variants else 'empty_dictionary_entry')
        queue.append({'id':rid,'word':word,'status':status,'arpabet_variants':variants,'source':'CMUdict (cmudict package)','decision':'review_only_no_auto_apply'})
    queue.sort(key=lambda item:item['word'].casefold())
    return queue

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=OUT)
    args=parser.parse_args()
    try:
        import cmudict
    except ImportError:
        print('Missing optional dependency: cmudict. Install it to generate the review queue.',file=sys.stderr); return 2
    from tools.cmudict_ipa import load_records
    records,_=load_records(); queue=collect(records,cmudict.dict())
    counts={}
    for row in queue: counts[row['status']]=counts.get(row['status'],0)+1
    payload={'schemaVersion':1,'source':'CMUdict via cmudict package; ARPABET retained for human review','canonicalMissingUsIpaCount':len(queue),'statusCounts':counts,'policy':'No IPA values are applied. Exact headwords only; all unique pronunciation variants are retained. Review before use.','records':queue}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"Queue written: {args.output} ({len(queue)} missing IPA records; {counts})")
    return 0
if __name__=='__main__': raise SystemExit(main())
