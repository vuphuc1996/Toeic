# Project Progress Dashboard — TOEIC Dictionary v2.95.84

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

## v2.95.84 — Mock pool alignment and criterion depth

- Mock Exam UI (`assets/js/app.js`) now uses shared question-level eligibility helpers from `assets/js/mock-engine.js`, keeping the 10 practice-only Part 4 questions (`mockEligible: false`) excluded from both exam generation and displayed Mock pool totals (**102** Listening / **30** Part 4 / **200** Reading / **295** projected Listening total).
- Listening Part 3 conversation purpose adds **4** audio-backed mappings (`7 → 11`, clearing the 10-item minimum); Listening Part 4 talk purpose adds **5** audio-backed mappings (`2 → 7`, honestly remaining below the 10-item minimum).
- Mapping inventory becomes **1,148 links / 648 unique stable question IDs**; instrumentation stays **25/27 TOEIC** and **31/33 overall** (Foundation **6/6**).
- Part 1 visual/detail (`8` each) and Part 7 cross-document (`2`) remain below 10; Part 1 paraphrase recognition and Part 7 paraphrase/inference remain uninstrumented pending human review.
- Listening reserve (193), Reading Part 7 reserve (87), Separate Part 5 review-only (80), and Part 4 practice-only (10) remain excluded from Mock.

## Protected boundaries

- All 1,221 vocabulary records and all 841 existing assessment/support items remain unchanged in content and answer keys.
- Learner IndexedDB v1 schema and local data are unchanged; no data migration is introduced.
- UI layout, navigation, Robot Buddy access boundary and GitHub Pages-only architecture remain protected.

> This is a provisional measurable curriculum-build index, not total system completion, official TOEIC readiness, learner mastery, CEFR/ETS certification or production acceptance.
