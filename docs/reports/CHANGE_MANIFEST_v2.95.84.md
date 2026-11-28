# Change Manifest — TOEIC Dictionary v2.95.84

**Branch:** `candidate`
**Predecessor:** stabilized `v2.95.83` (`137160f08cd1ef2b2b505a8af1c9e7ba829b4297` + CI reconciliation commit)
**Target:** Mock Exam UI pool-count reconciliation with question-level eligibility, plus verified Part 3/Part 4 purpose criterion depth on existing non-reserve items.

## Changes

1. Mock Exam UI & Engine Alignment
   - Export `isQuestionMockEligible` and `countMockPool(list, parts)` from `assets/js/mock-engine.js`.
   - Update `mockPoolCount` and `eligibleByPart` in `assets/js/app.js` to filter question-level `mockEligible !== false`, ensuring the 10 practice-only Part 4 questions (`mockEligible: false`) stay excluded from displayed Mock landing totals (`102` Listening / `30` Part 4 / `200` Reading / `295` projected Listening total).
   - Add automated Node assertions in `tools/tests/mock-exam-engine.mjs` and `tools/tests/mock-ui-integrity.mjs`.
2. Listening Part 3 & Part 4 Purpose Criterion Mapping
   - Add 4 verbatim audio-backed mappings to `listening-part-3-conversation-purpose` (`7 → 11`, clearing the 10-item minimum) on existing non-reserve Part 3 questions (`part3-invoice-error:1`, `part3-interview-schedule:2`, `part3-procurement-quotation:1`, `part3-elevator-maintenance:1`).
   - Add 5 verbatim audio-backed mappings to `listening-part-4-talk-purpose` (`2 → 7`, explicitly kept below the 10-item minimum) on existing non-reserve Part 4 questions (`part4-office-announcement:1`, `part4-conference-update:2`, `part4-warehouse-safety-briefing:1`, `part4-training-registration:1`, `part4-travel-service-update:1`).
   - Add `validate_listening_purpose_evidence` in `tools/audit-objective-criterion-map.py` and positive/negative regressions in `tools/tests/test_objective_criterion_map.py`.
3. Release Shell & Documentation
   - Synchronize manifest, package, HTML, app, Service Worker, mock-engine, and documentation markers to `v2.95.84`.
   - Reconcile release ledger, progress dashboard, command index, test report, and outcome evidence matrix for `v2.95.84`.

## Reconciliation

- Mapping inventory: **1,148 links / 648 unique stable question IDs**.
- TOEIC criteria with evidence paths: **25/27**; Foundation **6/6**; total **31/33**.
- `listening-part-3-conversation-purpose`: **11** (meets 10-item minimum); `listening-part-4-talk-purpose`: **7** (below 10-item minimum).
- Remaining uninstrumented criteria: Part 1 paraphrase recognition and Part 7 paraphrase/inference.
- Provisional weighted measurable curriculum-build index: **76.00%**; not learner mastery or total product completion.

## Protected boundaries

- No canonical vocabulary IDs/records, question text, choices, answer keys, choice IDs, learner IndexedDB schema/records, UI layout/navigation, Robot Buddy behavior, or GitHub Pages architecture are altered.
- Listening reserve 193, Reading Part 7 reserve 87, Separate Part 5 review-only 80, and Part 4 practice-only 10 remain excluded from Mock.
- Part 1 visual review and Part 7 independent second-review gates remain active.
- `main` stays unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.
