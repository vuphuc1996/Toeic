#!/usr/bin/env python3
"""Build a version-aware cross-domain release quality audit from canonical local data."""
from __future__ import annotations
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
VERSION=read('data/manifest.json').get('version','unknown')
REPORT=ROOT/f'docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v{VERSION}.md'
JSON_REPORT=ROOT/f'docs/reports/major-release-quality-audit-v{VERSION}.json'
OUTCOME_REPORT=ROOT/f'docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v{VERSION}.md'
def audit():
    words=[]
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': words.extend(read(f'data/vocabulary/{letter}.json').get('words',[]))
    related=read('data/related-terms.json').get('terms',[])
    relation_counts={}
    for word in words:
        for sense in word.get('senses',[]):
            for field in ('synonyms','antonyms'):
                vals=sense.get(field) or []
                if isinstance(vals,str): vals=[x.strip() for x in vals.split(',') if x.strip()]
                for term in vals:
                    key=str(term).strip().casefold()
                    if key: relation_counts[key]=relation_counts.get(key,0)+1
    related_keys={str(r.get('term','')).strip().casefold() for r in related if r.get('term')}
    glossary_placeholder=sum('reference gloss for practice distractors.' in str(r.get('definition_en','')).casefold() for r in related)
    backfilled=sum(r.get('source')=='canonical-vocabulary-senses' for r in related)
    outcomes=read('data/learning-path/objective-outcomes.json').get('objectives',[])
    criteria=[outcome for obj in outcomes for outcome in obj.get('outcomes',[])]
    instrumented=sum(str(o.get('status','')).startswith('instrumented_') for o in criteria)
    status_counts={}
    criteria_detail=[]
    for obj in outcomes:
        for outcome in obj.get('outcomes',[]):
            status=str(outcome.get('status','unknown'))
            status_counts[status]=status_counts.get(status,0)+1
            criteria_detail.append({'objectiveId':obj.get('objectiveId'),'outcomeId':outcome.get('id'),'title':outcome.get('title'),'status':status,'evidenceMetric':outcome.get('evidenceMetric'),'masteryThreshold':outcome.get('masteryThreshold'),'minimumUniqueItems':outcome.get('minimumUniqueItems')})
    listening=read('data/listening/listening-library.json').get('listening',[])
    readings=read('data/readings/reading-library.json').get('readings',[])
    grammar=read('data/grammar/lessons.json').get('lessons',[])
    part5=read('data/practice/part5-sentence-completion.json').get('questions',[])
    vocab={
      'headwords':len(words),
      'ipa_us':sum(bool(w.get('phonetic',{}).get('us')) for w in words),
      'word_family':sum(bool(w.get('word_family')) for w in words),
      'verb_forms':sum(bool(w.get('verb_forms')) for w in words),
      'collocations':sum(bool(w.get('collocations')) for w in words),
      'synonyms':sum(any(s.get('synonyms') for s in w.get('senses',[])) for w in words),
      'antonyms':sum(any(s.get('antonyms') for s in w.get('senses',[])) for w in words),
    }
    vocab_fields={k:{'count':v,'percent':round(100*v/vocab['headwords'],1)} for k,v in vocab.items() if k!='headwords'}
    referenced_unique=len(relation_counts)
    glossary_join=len(set(relation_counts)&related_keys)
    missing_unique=referenced_unique-glossary_join
    missing_occurrences=sum(count for key,count in relation_counts.items() if key not in related_keys)
    summary={
      'version':VERSION,'vocabulary':vocab,'vocabularyFieldCoverage':vocab_fields,
      'relatedGlossary':{'entries':len(related),'referencedUniqueTerms':referenced_unique,'coveredUniqueTerms':glossary_join,'coveragePercent':round(glossary_join/referenced_unique*100,1) if referenced_unique else 0,'unglossedUniqueTerms':missing_unique,'unglossedReferenceOccurrences':missing_occurrences,'placeholderEnglishDefinitions':glossary_placeholder,'backfilledFromCanonicalVocabulary':backfilled},
      'contentInventory':{'grammarLessons':len(grammar),'listeningResources':len(listening),'readingResources':len(readings),'part5PracticeQuestions':len(part5)},
      'learningOutcomes':{'objectives':len(outcomes),'criteria':len(criteria),'instrumentedCriteria':instrumented,'instrumentedPercent':round(instrumented/len(criteria)*100,1) if criteria else 0,'statusCounts':status_counts,'criteriaDetail':criteria_detail},
    }
    rows=[f'# Major Release Quality Audit — v{VERSION}','', '> Inventory and coverage metrics only; not editorial approval, learner mastery, independent review, CEFR or ETS certification.','', '## Vocabulary data coverage','', '| Field | Records | Coverage |','|---|---:|---:|']
    for k,v in vocab_fields.items(): rows.append(f"| {k.replace('_',' ').title()} | {v['count']}/{vocab['headwords']} | {v['percent']}% |")
    g=summary['relatedGlossary']; rows.extend(['','## Related-term glossary','',f"- Entries: **{g['entries']}**",f"- Referenced unique terms: **{g['referencedUniqueTerms']}**",f"- Exact covered terms: **{g['coveredUniqueTerms']} ({g['coveragePercent']}%)**",f"- Missing unique terms: **{g['unglossedUniqueTerms']}**",f"- Missing reference occurrences: **{g['unglossedReferenceOccurrences']}**",f"- Placeholder English definitions remaining: **{g['placeholderEnglishDefinitions']}**",f"- Canonical headword sense backfills in this release: **{g['backfilledFromCanonicalVocabulary']}**",'','## Content inventory','', '| Domain | Count |', '|---|---:|',f"| Grammar lessons | {summary['contentInventory']['grammarLessons']} |",f"| Listening resources | {summary['contentInventory']['listeningResources']} |",f"| Reading resources | {summary['contentInventory']['readingResources']} |",f"| Separate Part 5 questions | {summary['contentInventory']['part5PracticeQuestions']} |",'','## Learning outcomes','',f"- Objectives: **{summary['learningOutcomes']['objectives']}**",f"- Criteria: **{summary['learningOutcomes']['criteria']}**",f"- Instrumented criteria: **{instrumented}/{len(criteria)} ({summary['learningOutcomes']['instrumentedPercent']}%)**",'- Status distribution: '+', '.join(f'{k}: {v}' for k,v in sorted(status_counts.items())),'- Evidence wiring is not completion, mastery or certification.','', '| Objective | Outcome criterion | Status | Metric | Threshold | Minimum items |','|---|---|---|---|---:|---:|',*[f"| {r['objectiveId']} | {r['outcomeId']} | {r['status']} | {r['evidenceMetric']} | {r['masteryThreshold']} | {r['minimumUniqueItems']} |" for r in criteria_detail], '', '## Major-release priorities','', '1. Backfill only glossary placeholder definitions where an exact canonical headword and bilingual sense exists.', '2. Independently review remaining placeholder glosses and high-frequency unglossed relation terms; do not auto-import uncertain entries.', '3. Improve IPA and morphology only with source-backed evidence; coverage percentage is not accuracy.', '4. Complete independent review for reserve Listening, Reading Part 7 and separate Part 5 items before Mock eligibility changes.', '5. Instrument learning outcomes only when an outcome-specific evidence mapping is defensible and regression-tested.', '6. Run browser/device, offline/reconnect and remote CI acceptance before deployment.',''])
    REPORT.write_text('\n'.join(rows),encoding='utf-8')
    outcome_rows=[f'# Learning Outcome Evidence Matrix — v{VERSION}','', '> This is a wiring/coverage audit only. Instrumentation does not establish learner completion, mastery, independent assessment or CEFR/ETS certification.','',f"- Objectives: {len(outcomes)}",f"- Criteria: {len(criteria)}",f"- Instrumented: {instrumented}/{len(criteria)} ({summary['learningOutcomes']['instrumentedPercent']}%)",f"- Not yet instrumented: {len(criteria)-instrumented}",'', '| Objective | Criterion | Evidence status | Metric | Threshold | Min. unique items |','|---|---|---|---|---:|---:|']
    for row in criteria_detail:
        outcome_rows.append(f"| {row['objectiveId']} | {row['outcomeId']} — {row['title']} | {row['status']} | {row['evidenceMetric']} | {row['masteryThreshold']} | {row['minimumUniqueItems']} |")
    outcome_rows.extend(['','## Review notes','','- Criteria marked not yet instrumented are definitions only; do not report learner mastery for these criteria.','- Metrics and thresholds must be interpreted with the configured minimum item count.','- This matrix is generated from the canonical `objective-outcomes.json` file.',''])
    OUTCOME_REPORT.write_text('\n'.join(outcome_rows),encoding='utf-8')
    JSON_REPORT.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return summary
if __name__=='__main__':
    s=audit(); print(json.dumps(s,ensure_ascii=False,indent=2))
