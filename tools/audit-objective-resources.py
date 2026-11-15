#!/usr/bin/env python3
"""Validate objective-to-resource links against canonical content IDs."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def audit():
    mapping=load('data/learning-path/objective-resource-map.json')
    if mapping.get('schemaVersion') != 1: raise ValueError('Unsupported objective map schemaVersion')
    objectives=mapping.get('objectives',[])
    ids=[x.get('id') for x in objectives]
    if not objectives or len(ids)!=len(set(ids)) or any(not x for x in ids): raise ValueError('Objective IDs must be present and unique')
    total=0; mapped=0; rows=[]; canonical_inventory=set(); mapped_inventory=set()
    for obj in objectives:
        rel=obj['resourceFile']; collection=obj['resourceCollection']
        source=load(rel)
        records=source.get(collection)
        if not isinstance(records,list): raise ValueError(f'{obj["id"]}: missing collection {collection}')
        canonical={x.get('id') for x in records}
        refs=obj.get('resourceIds',[])
        if len(refs)!=len(set(refs)): raise ValueError(f'{obj["id"]}: duplicate resource IDs')
        missing=sorted(set(refs)-canonical)
        if missing: raise ValueError(f'{obj["id"]}: unknown resource IDs {missing[:5]}')
        if obj.get('availability')=='available' and not refs: raise ValueError(f'{obj["id"]}: marked available but has no resources')
        canonical_inventory.update((rel,collection,rid) for rid in canonical)
        mapped_inventory.update((rel,collection,rid) for rid in refs)
        rows.append((obj['id'],len(refs),len(records)))
    total=len(canonical_inventory); mapped=len(mapped_inventory)
    return objectives,rows,total,mapped
if __name__=='__main__':
    objectives,rows,total,mapped=audit()
    print(f'PASS: {len(objectives)} objectives; {mapped}/{total} resource records linked')
    for oid,n,d in rows: print(f'{oid}: {n}/{d}')
