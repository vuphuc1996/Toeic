# Major Release Quality Audit — v2.95.85

> Inventory and coverage metrics only; not editorial approval, learner mastery, independent review, CEFR or ETS certification.

## Vocabulary data coverage

| Field | Records | Coverage |
|---|---:|---:|
| Ipa Us | 1102/1281 | 86.0% |
| Word Family | 331/1281 | 25.8% |
| Verb Forms | 328/1281 | 25.6% |
| Collocations | 1111/1281 | 86.7% |
| Synonyms | 405/1281 | 31.6% |
| Antonyms | 210/1281 | 16.4% |

## Related-term glossary

- Entries (raw rows): **567**
- Unique normalized glossary terms: **567**
- Duplicate normalized rows: **0**
- Referenced unique terms: **804**
- Exact covered terms: **556 (69.2%)**
- Missing unique terms: **248**
- Missing reference occurrences: **249**
- Placeholder English definitions remaining: **0**
- Glossary entries carrying canonical-vocabulary sense provenance (cumulative inventory; not this release delta): **205**

## Content inventory

| Domain | Count |
|---|---:|
| Grammar lessons | 58 |
| Listening resources | 145 |
| Reading resources | 73 |
| Separate Part 5 questions | 80 |

## Learning outcomes

- Objectives: **11**
- Criteria: **33**
- Instrumented criteria: **32/33 (97.0%)**
- Status distribution: criteria_defined_not_yet_instrumented: 1, instrumented_delayed_recall: 3, instrumented_learner_self_report: 5, instrumented_practice_evidence: 24
- Evidence wiring is not completion, mastery or certification.

| Objective | Outcome criterion | Status | Metric | Threshold | Minimum items |
|---|---|---|---|---:|---:|
| foundation-pre-a1-a1 | foundation-pre-a1-a1-recognition | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| foundation-pre-a1-a1 | foundation-pre-a1-a1-production | instrumented_learner_self_report | rubric_score | 0.8 | 10 |
| foundation-pre-a1-a1 | foundation-pre-a1-a1-retention | instrumented_delayed_recall | delayed_correct_rate | 0.8 | 10 |
| foundation-a2 | foundation-a2-recognition | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| foundation-a2 | foundation-a2-application | instrumented_learner_self_report | rubric_score | 0.8 | 10 |
| foundation-a2 | foundation-a2-retention | instrumented_delayed_recall | delayed_correct_rate | 0.8 | 10 |
| grammar-core | grammar-core-form-recognition | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| grammar-core | grammar-core-contextual-choice | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| grammar-core | grammar-core-error-explanation | instrumented_learner_self_report | explanation_rubric | 0.8 | 10 |
| listening-part-1 | listening-part-1-visual-audio-match | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-1 | listening-part-1-paraphrase-recognition | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-1 | listening-part-1-detail-retention | instrumented_delayed_recall | delayed_correct_rate | 0.8 | 10 |
| listening-part-2 | listening-part-2-response-intent | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-2 | listening-part-2-natural-response | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-2 | listening-part-2-distractor-resistance | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-3 | listening-part-3-conversation-purpose | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-3 | listening-part-3-detail-inference | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-3 | listening-part-3-speaker-linking | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-4 | listening-part-4-talk-purpose | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-4 | listening-part-4-detail-tracking | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| listening-part-4 | listening-part-4-inference-action | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-5 | reading-part-5-sentence-completion | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-5 | reading-part-5-word-form-selection | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-5 | reading-part-5-distractor-explanation | instrumented_learner_self_report | explanation_rubric | 0.8 | 10 |
| reading-part-6 | reading-part-6-text-cohesion | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-6 | reading-part-6-context-completion | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-6 | reading-part-6-discourse-purpose | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-7 | reading-part-7-information-location | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-7 | reading-part-7-paraphrase-inference | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| reading-part-7 | reading-part-7-cross-document-link | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| part5-sentence-completion | part5-sentence-completion-accuracy | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| part5-sentence-completion | part5-sentence-completion-time-management | instrumented_practice_evidence | timed_accuracy | 0.8 | 10 |
| part5-sentence-completion | part5-sentence-completion-error-review | instrumented_learner_self_report | explanation_rubric | 0.8 | 10 |

## Major-release priorities

1. Backfill only glossary placeholder definitions where an exact canonical headword and bilingual sense exists.
2. Independently review remaining placeholder glosses and high-frequency unglossed relation terms; do not auto-import uncertain entries.
3. Improve IPA and morphology only with source-backed evidence; coverage percentage is not accuracy.
4. Complete independent review for reserve Listening, Reading Part 7 and separate Part 5 items before Mock eligibility changes.
5. Instrument learning outcomes only when an outcome-specific evidence mapping is defensible and regression-tested.
6. Run browser/device, offline/reconnect and remote CI acceptance before deployment.
