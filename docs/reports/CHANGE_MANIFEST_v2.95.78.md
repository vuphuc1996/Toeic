# Change Manifest — TOEIC Dictionary v2.95.78

**Predecessor:** latest candidate HEAD `c1f9702579633aeb6cd372b29e17b143cb2868a1` (v2.95.77).
**Target:** v2.95.78 — Criterion-level TOEIC Learning Outcome Evidence.
**Target branch:** `candidate`; `main` is not modified.

## Source and runtime

- Add `data/learning-path/objective-criterion-map.json`: 1,082 stable question-to-criterion links across 638 unique question IDs. 22/27 TOEIC criteria are mapped; five remain explicitly uninstrumented.
- Extend `assets/js/learning-outcome-progress.js` with criterion-index construction, non-mutating criterion summaries and criterion-level due-recall enumeration. Existing read/write helpers and the learner IndexedDB v1 data structure remain in place.
- Extend `assets/js/app.js` to load the map, record criterion evidence alongside existing group-level evidence, render an expandable criteria dashboard, save optional Grammar and Reading Part 5 explanation self-reports, and reopen the exact source question from recall.
- Add dashboard markup and CSS for a collapsible criterion matrix. The existing page layout and primary navigation are not redesigned.
- Add the new map to Service Worker REQUIRED and APP_SHELL lists, and synchronize release/cache keys to v2.95.78.

## Quality and tests

- Add `tools/audit-objective-criterion-map.py` to verify every link against canonical banks, question identity, index, objective ownership, review state and Listening reserve boundaries.
- Add Node runtime regressions for criterion accuracy, timed accuracy, optional explanation rubric, second-review blocking, due recall, audit and read-only summaries.
- Extend Python tests for evidence-map reconciliation, target-based reports, weighted index and Service Worker cache coverage.
- Update the report generator to distinguish 28/33 total evidence paths from 22/27 TOEIC sub-skill mappings.

## Protected data

- No vocabulary record, canonical vocabulary ID/headword/sense/relationship, Grammar/Reading/Listening bank content, question ID, choice ID or answer key is intentionally changed.
- All 831 assessment/support items and all Mock/reserve eligibility flags remain unchanged.
- Listening reserve remains unmapped; Part 7 second-review and Separate Part 5 independent-review gates remain active.
- Existing learner progress records are not migrated, reset or deleted. The new criterion evidence is appended within the existing `objectiveProgress` object.

## Verification

Hosted acceptance verified on exact candidate HEAD `0187b446123fca1a8708b496e971e18b19a46c57`: GitHub Validate PASS (run 46100106836; 846 Python tests PASS) and GitHub Pages build/deploy PASS (run 46100106757). FullSource ZIP generation, installed-PWA/offline verification and physical-device QA remain unverified.
