# Mock Listening form diversity — v2.95.56

## Scope

This change addresses one measurement-integrity issue: the TOEIC Score Readiness panel previously treated three completed Full Mock attempts as sufficient to show both Listening and Reading trends, without checking whether the Listening question sets differed.

## Source-backed pool finding

- Full Listening blueprint: 100 questions per Full Mock.
- Current eligible Listening pool is 102 questions; 193 additional Listening questions remain `reserve-pending-independent-review` and are excluded from Mock.
- Replaying the existing `createMockExam` selection engine with the current data and persistent usage ledger produced two distinct Full forms with 100 Listening questions each, 98 shared question IDs, and only 2 questions exchanged (98% overlap).
- This is a concrete test of the current source pool and selection engine, not a claim that every random sequence will have an identical arrangement.

## Implementation

- `buildMockScoreReadiness` derives Listening form signatures from existing `questionIds` beginning with `listening:` in completed Full Mock history.
- Listening trend is enabled only after at least two distinct Listening question-ID sets are identified among the latest three eligible attempts. Repeated attempts on the same exact form are collapsed to the latest result for that form before calculating the Listening average/change.
- Legacy history without question IDs fails closed; it does not count as an independent Listening form and its Listening accuracy is excluded from the form-diversity trend calculation.
- The panel keeps Reading readiness independent. Three completed Full Mock attempts can still unlock Reading trend while Listening trend remains hidden.
- If the latest two distinct Listening forms share at least 90% of their smaller question set, a caution is displayed. The observed current-pool case reports 98% overlap.
- No new learner-history field or schema is introduced. The history already stores the full exam `questionIds` when an attempt starts.

## Safety boundaries

- No listening question, answer key, choice, content asset or source record was edited.
- No reserve-pending question was approved or promoted.
- No Mock blueprint, question count, usage ledger, IndexedDB schema, vocabulary data, or Robot Buddy behavior was changed.
- This gate describes form diversity, not psychometric equivalence or ETS calibration.

## Verification

- `node tools/tests/mock-score-readiness.mjs`: PASS — repeated same form, distinct forms, 98% overlap warning, legacy fail-closed, Reading independence and Full Mock filtering.
- `node tools/tests/mock-exam-engine.mjs`: PASS — existing 15/60/120-minute blueprint, reserve exclusion, usage rotation and scoring.
- `node tools/tests/mock-ui-integrity.mjs`: PASS — 299 unique HTML IDs and existing UI integrity.
- All 42 `tools/tests/*.mjs` runtime scripts: PASS.
- `python tools/validate-data.py`: PASS — 1,141 records, 0 errors, 0 warnings; no ID additions/removals.
- `python tools/sync-version.py --check`: PASS — all registered version markers synchronized to 2.95.56.
- Full Python `unittest discover` was attempted but exceeded the 300-second execution limit before completion. It is INCOMPLETE and is not counted as PASS.
- Hosted GitHub Actions, Pages deployment and physical-device behavior are not verified here.
