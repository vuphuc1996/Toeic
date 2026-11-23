# Major Release Quality Audit — v2.95.44

> Inventory and coverage metrics only; not editorial approval, learner mastery, independent review, CEFR or ETS certification.

## Vocabulary data coverage

| Field | Records | Coverage |
|---|---:|---:|
| Ipa Us | 1062/1141 | 93.1% |
| Word Family | 276/1141 | 24.2% |
| Verb Forms | 329/1141 | 28.8% |
| Collocations | 971/1141 | 85.1% |
| Synonyms | 405/1141 | 35.5% |
| Antonyms | 210/1141 | 18.4% |

## Related-term glossary

- Entries (raw rows): **567**
- Unique normalized glossary terms: **567**
- Duplicate normalized rows: **0**
- Referenced unique terms: **804**
- Exact covered terms: **556 (69.2%)**
- Missing unique terms: **248**
- Missing reference occurrences: **249**
- Placeholder English definitions remaining: **73**
- Canonical headword sense backfills in this release: **205**

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
- Instrumented criteria: **6/33 (18.2%)**
- Status distribution: criteria_defined_not_yet_instrumented: 27, instrumented_delayed_recall: 2, instrumented_learner_self_report: 2, instrumented_practice_evidence: 2
- Evidence wiring is not completion, mastery or certification.

| Objective | Outcome criterion | Status | Metric | Threshold | Minimum items |
|---|---|---|---|---:|---:|
| foundation-pre-a1-a1 | foundation-pre-a1-a1-recognition | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| foundation-pre-a1-a1 | foundation-pre-a1-a1-production | instrumented_learner_self_report | rubric_score | 0.8 | 10 |
| foundation-pre-a1-a1 | foundation-pre-a1-a1-retention | instrumented_delayed_recall | delayed_correct_rate | 0.8 | 10 |
| foundation-a2 | foundation-a2-recognition | instrumented_practice_evidence | correct_rate | 0.8 | 10 |
| foundation-a2 | foundation-a2-application | instrumented_learner_self_report | rubric_score | 0.8 | 10 |
| foundation-a2 | foundation-a2-retention | instrumented_delayed_recall | delayed_correct_rate | 0.8 | 10 |
| grammar-core | grammar-core-form-recognition | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| grammar-core | grammar-core-contextual-choice | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| grammar-core | grammar-core-error-explanation | criteria_defined_not_yet_instrumented | explanation_rubric | 0.8 | 10 |
| listening-part-1 | listening-part-1-visual-audio-match | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-1 | listening-part-1-paraphrase-recognition | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-1 | listening-part-1-detail-retention | criteria_defined_not_yet_instrumented | delayed_correct_rate | 0.8 | 10 |
| listening-part-2 | listening-part-2-response-intent | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-2 | listening-part-2-natural-response | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-2 | listening-part-2-distractor-resistance | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-3 | listening-part-3-conversation-purpose | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-3 | listening-part-3-detail-inference | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-3 | listening-part-3-speaker-linking | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-4 | listening-part-4-talk-purpose | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-4 | listening-part-4-detail-tracking | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| listening-part-4 | listening-part-4-inference-action | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-5 | reading-part-5-sentence-completion | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-5 | reading-part-5-word-form-selection | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-5 | reading-part-5-distractor-explanation | criteria_defined_not_yet_instrumented | explanation_rubric | 0.8 | 10 |
| reading-part-6 | reading-part-6-text-cohesion | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-6 | reading-part-6-context-completion | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-6 | reading-part-6-discourse-purpose | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-7 | reading-part-7-information-location | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-7 | reading-part-7-paraphrase-inference | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| reading-part-7 | reading-part-7-cross-document-link | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| part5-sentence-completion | part5-sentence-completion-accuracy | criteria_defined_not_yet_instrumented | correct_rate | 0.8 | 10 |
| part5-sentence-completion | part5-sentence-completion-time-management | criteria_defined_not_yet_instrumented | timed_accuracy | 0.8 | 10 |
| part5-sentence-completion | part5-sentence-completion-error-review | criteria_defined_not_yet_instrumented | explanation_rubric | 0.8 | 10 |

## Major-release priorities

1. Backfill only glossary placeholder definitions where an exact canonical headword and bilingual sense exists.
2. Independently review remaining placeholder glosses and high-frequency unglossed relation terms; do not auto-import uncertain entries.
3. Improve IPA and morphology only with source-backed evidence; coverage percentage is not accuracy.
4. Complete independent review for reserve Listening, Reading Part 7 and separate Part 5 items before Mock eligibility changes.
5. Instrument learning outcomes only when an outcome-specific evidence mapping is defensible and regression-tested.
6. Run browser/device, offline/reconnect and remote CI acceptance before deployment.
