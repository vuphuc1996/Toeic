#!/usr/bin/env python3
"""Safely backfill missing US IPA from exact, single-variant CMUdict entries.

Default mode is preview-only. --apply writes only entries that have exactly one
CMUdict pronunciation AND pass the project's ARPABET-to-IPA converter. It never
replaces existing phonetic.us, and it updates the source-linked cumulative ledger.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
LEDGER=ROOT/'docs/reports/CMUDICT_IPA_BACKFILL_v2.71.0.json'
QUEUE=ROOT/'docs/reports/MISSING_US_IPA_CMUdict_REVIEW_QUEUE.json'

def classify_missing(records, dictionary, converter):
    result=[]
    normalized_dictionary={str(key).casefold(): value for key,value in dictionary.items()}
    for rid,record in records.items():
        phonetic=record.get('phonetic') or {}
        if (phonetic.get('us') or '').strip(): continue
        word=(record.get('word') or '').strip()
        variants=[]
        for raw in normalized_dictionary.get(word.casefold(),[]):
            v=list(raw)
            if v not in variants: variants.append(v)
        status='no_exact_entry' if not variants else ('multiple_variants' if len(variants)>1 else 'single_variant')
        ipa=None; error=None
        if status=='single_variant':
            try: ipa=converter(variants[0])
            except (ValueError,KeyError) as exc: error=str(exc)
            if error: status='single_variant_conversion_failed'
        result.append({'id':rid,'word':word,'status':status,'arpabet':variants[0] if len(variants)==1 else None,'phoneticUs':ipa,'conversionError':error,'source':'CMUdict (exact headword)','action':'apply_safe' if ipa else 'review_only'})
    return sorted(result,key=lambda x:x['word'].casefold())

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--apply',action='store_true',help='apply only exact single-variant records that convert successfully'); args=ap.parse_args()
    try: import cmudict
    except ImportError: print('Optional dependency cmudict not installed.',file=sys.stderr); return 2
    from tools.cmudict_ipa import load_records,arpabet_to_ipa
    records,manifest=load_records(); candidates=classify_missing(records,cmudict.dict(),arpabet_to_ipa)
    safe=[x for x in candidates if x['phoneticUs']]
    counts={}
    for x in candidates: counts[x['status']]=counts.get(x['status'],0)+1
    print(f"Missing IPA examined: {len(candidates)}; safe candidates: {len(safe)}; statuses: {counts}")
    for x in safe: print(f"SAFE {x['id']} {x['word']} {x['phoneticUs']}")
    if not args.apply: print('PREVIEW ONLY — no canonical data or ledger changed.'); return 0
    ledger=json.loads(LEDGER.read_text(encoding='utf-8'))
    known={x['id'] for x in ledger['records']}
    added=[]
    for x in safe:
        if x['id'] in known: continue
        record=records.get(x['id'])
        if not record or record.get('word','').casefold()!=x['word'].casefold(): raise SystemExit(f"canonical mismatch: {x['id']}")
        current=(record.get('phonetic') or {}).get('us','')
        if current: raise SystemExit(f"refusing to overwrite existing IPA: {x['id']}")
        record.setdefault('phonetic',{})['us']=x['phoneticUs']
        added.append({'id':x['id'],'word':x['word'],'arpabet':x['arpabet'],'phoneticUs':x['phoneticUs']})
    if added:
        # Persist vocabulary by manifest letter mapping; records may be in letter or batch files.
        data_by_path={}
        for letter in manifest['letters']:
            path=ROOT/letter['file'].replace('./','',1); data=json.loads(path.read_text(encoding='utf-8')); data_by_path[path]=data
        by_id={r['id']:r for rows in data_by_path.values() for r in rows['words']}
        for row in added:
            by_id[row['id']]['phonetic']['us']=row['phoneticUs']
        for path,data in data_by_path.items(): path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        ledger['recordCount']=len(ledger['records'])+len(added); ledger['records'].extend(added)
        ledger['release']=manifest['version']; ledger.setdefault('notes',[]).append(f"{len(added)} exact single-variant missing-IPA records safely backfilled in v{manifest['version']} after converter validation; ambiguous and conversion-failing records remain blank.")
        LEDGER.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"APPLIED {len(added)} IPA entries; existing records preserved; ledger now {ledger['recordCount']}.")
    return 0
if __name__=='__main__': raise SystemExit(main())
