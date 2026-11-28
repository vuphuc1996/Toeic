# Project Progress Dashboard — TOEIC Dictionary v2.95.83

**Weighted measurable curriculum-build index: 76.00%**

Model: `toeic-dictionary-measurable-build-index-v1` · Status: `provisional-transparent-model-not-an-official-acceptance-score` · Total weight: 100

| Workstream | Numerator / denominator | Coverage | Weight | Contribution | Interpretation |
|---|---:|---:|---:|---:|---|
| Vocabulary headwords vs 3,000 minimum | 1,221/3,000 | **40.7%** | 20% | 8.14 pts | Inventory only; editorial quality separate. |
| Related glossary exact-join coverage | 556/804 | **69.2%** | 10% | 6.92 pts | Exact relation-target join; no sense-quality claim. |
| Related glossary records without automated flags | 565/567 | **99.6%** | 10% | 9.96 pts | Automated screening only. |
| Guided pathway stage presence | 3/6 | **50.0%** | 15% | 7.50 pts | Presence only; stage completion not claimed. |
| Canonical objective-resource mapping | 379/379 | **100.0%** | 10% | 10.00 pts | Stable resource ID mapping only. |
| Outcome criteria with evidence instrumentation | 31/33 | **93.9%** | 25% | 23.48 pts | Evidence-collection path, not learner attainment. |
| Foundation core content coverage | 100% | **100.0%** | 10% | 10.00 pts | Existing Foundation scope only. |

## v2.95.83 — New evidence and protected boundaries

- Part 4 adds **10** new next-step/action questions across ten existing non-reserve scripts. They are practice-only at question level and excluded from Mock selection.
- Part 6 adds **10** mappings to existing questions across four internally reviewed resources. No source question or answer key is modified.
- Instrumentation becomes **25/27 TOEIC** and **31/33 overall**, with **1,139 links / 648 stable question IDs**.
- The two criteria still uninstrumented are Part 1 paraphrase recognition and Part 7 paraphrase/inference. Part 1 photos and Part 7 resources remain in the human-review handoff queue.
- Listening reserve (193), Reading Part 7 reserve (87) and Separate Part 5 review-only (80) remain excluded from Mock.
## New criterion-level TOEIC evidence

- **25/27 TOEIC sub-skill criteria** now have an explicit stable-question mapping.
- **1,139** question-to-criterion links span the same **638** unique stable question IDs (+21 links; no new question IDs).
- The six Foundation outcome criteria retain their separate evidence paths; total instrumentation is **31/33**.
- Two TOEIC criteria remain deliberately uninstrumented: Listening Part 1 paraphrase recognition and Reading Part 7 paraphrase/inference.
- The index increases to **76.00%** because Part 2 distractor-resistance gains its first defensible item-level evidence path. The index is a selected measurable build model, not learner attainment. It does **not** mean learners have attained those outcomes.

## Protected boundaries

- 1,221 vocabulary records and all 831 assessment/support items remain unchanged.
- Existing answer keys, stable question/choice IDs, Mock eligibility and reserve-review gates are preserved.
- Learner IndexedDB v1 schema and local data are unchanged; no data migration is introduced.
- UI structure, layout, navigation, Robot Buddy access boundary and GitHub Pages-only architecture remain protected.

> This is a provisional measurable curriculum-build index, not total system completion, official TOEIC readiness, learner mastery, CEFR/ETS certification or production acceptance.

## v2.95.83 mapping-depth note

- Grammar form recognition and Listening Part 3 speaker/action now each have 10 mapped stable questions.
- Listening Part 1 criteria remain at 8; Listening Part 3 purpose at 7; Listening Part 4 purpose at 2; Part 7 cross-document at 2. They are not represented as meeting the 10-item minimum.
- No reserve content is mapped or promoted. The Part 7 cross-document mapping audit requires reviewed resources and source quotes from at least two documents.
