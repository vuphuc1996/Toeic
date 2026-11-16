#!/usr/bin/env python3
"""Validate that each mapped learning objective has measurable outcome criteria."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def main():
    mapped=load('data/learning-path/objective-resource-map.json')['objectives']
    registry=load('data/learning-path/objective-outcomes.json')
    rows=registry.get('objectives',[])
    by_id={x.get('objectiveId'):x for x in rows}
    errors=[]
    if len(by_id)!=len(rows): errors.append('duplicate outcome objective IDs')
    if set(by_id)!={x['id'] for x in mapped}: errors.append('outcome objective IDs must match resource-map objective IDs exactly')
    outcome_ids=set(); count=0; instrumented=0; foundation_instrumented=0; foundation_total=0
    for item in rows:
        outcomes=item.get('outcomes',[])
        if len(outcomes)<2: errors.append(f"{item.get('objectiveId')}: at least 2 outcomes required")
        for outcome in outcomes:
            count+=1; oid=outcome.get('id')
            if not oid or oid in outcome_ids: errors.append(f'duplicate/missing outcome ID: {oid}')
            outcome_ids.add(oid)
            if not outcome.get('title'): errors.append(f'{oid}: missing title')
            if outcome.get('evidenceMetric') not in registry.get('policy',{}).get('scoreTypes',[]): errors.append(f'{oid}: unsupported evidence metric')
            threshold=outcome.get('masteryThreshold')
            if not isinstance(threshold,(int,float)) or not 0<threshold<=1: errors.append(f'{oid}: invalid mastery threshold')
            if outcome.get('minimumUniqueItems',0)<1: errors.append(f'{oid}: minimumUniqueItems must be positive')
            status=outcome.get('status')
            allowed={'criteria_defined_not_yet_instrumented','instrumented_practice_evidence','instrumented_learner_self_report','instrumented_delayed_recall'}
            if status not in allowed: errors.append(f'{oid}: unsupported evidence instrumentation status: {status}')
            if str(status).startswith('instrumented_'):
                instrumented += 1
                if str(item.get('objectiveId','')).startswith('foundation-'): foundation_instrumented += 1
            if str(item.get('objectiveId','')).startswith('foundation-'): foundation_total += 1
    if errors:
        print('\n'.join('FAIL: '+e for e in errors)); return 1
    print(f'PASS: {len(rows)}/{len(mapped)} objectives; {count} measurable outcome criteria; {instrumented}/{count} outcomes have an evidence-collection path.')
    print(f'Foundation instrumentation: {foundation_instrumented}/{foundation_total} outcomes wired; learner records and mastery are not inferred from wiring.')
    print('NOTE: production ratings are learner self-reports; practice thresholds and delayed recall do not certify CEFR/ETS mastery.')
    return 0
if __name__=='__main__': raise SystemExit(main())
