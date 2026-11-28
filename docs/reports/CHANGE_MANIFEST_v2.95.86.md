# Change Manifest — TOEIC Dictionary v2.95.86

**Branch:** `candidate`  
**Baseline:** v2.95.85 source HEAD `7b8d80f1eef1523b5c2f31f0361a51c90011da7e`  
**Release purpose:** expand Part 1 reserve coverage and reconcile release documentation without changing the production branch.

## Content and data

- Added three Part 1 photo-description resources: `part1-construction-plans`, `part1-laboratory-bench`, and `part1-supermarket-shelf`.
- Reused three JPG assets already present in the candidate repository; added explicit Google Imagen provenance rows to `assets/listening/ATTRIBUTION.csv`.
- Each resource contains four English SpeechSynthesis statements, one provisional answer, a Vietnamese explanation, exact `evidenceText`, and stable choice IDs.
- Added the three resource IDs to the Part 1 objective-resource inventory.
- Listening resources: **145 → 148**. Listening questions: **308 → 311**. Part 1: **9 → 12**.
- Reserve questions: **193 → 196**. Part 1 reserve: **1 → 4**. Approved Mock Listening remains **102**; the new questions have `mockEligible: false` and resources remain `reserve-pending-independent-review`.

## Validation coverage

- Added `tools/content-batch-018-v2.95.86.json` and `tools/tests/test_content_batch_018.py`.
- Updated Listening expansion, Full-Mock readiness, reserve-exclusion and historical batch fingerprint regressions to the new inventory.
- The Part 1 asset validator continues to enforce local JPG presence, minimum resolution, 4:3 aspect ratio, maximum file size and source-type-matched attribution.
- Added/updated tests without weakening the historical content integrity checks.

## Learning outcomes and protected boundaries

- No new outcome criterion mapping was added. Part 1 visual/audio and delayed-retention mapping remain 8 each; `listening-part-1-paraphrase-recognition` remains uninstrumented.
- No existing question IDs, choice IDs, answer keys or canonical vocabulary IDs were changed.
- No IndexedDB schema migration, learner-data rewrite, UI redesign, Robot Buddy change, backend or Cloudflare dependency was introduced.
- All new Part 1 items remain pending independent review. No content is promoted to Mock in this batch.

## Documentation

- Corrected stale v2.95.85 documentation references and added an explicit release acceptance evidence record.
- Added v2.95.86 Full-Mock readiness, quality audit, project progress, test status and review handoff reports.
- Synced all application release/cache markers to v2.95.86.

## Acceptance boundary

The v2.95.85 owner-confirmed **865/865** test result applies only to that earlier exact source SHA. It is not carried forward as a v2.95.86 test result. The v2.95.86 full test suite and hosted GitHub Actions/Pages results must be checked against the final v2.95.86 candidate HEAD. No merge to `main` or production deployment is authorized.
