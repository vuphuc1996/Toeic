# Change Manifest — TOEIC Dictionary v2.95.62

## Source baseline

- Base archive: `TOEIC_Dictionary_v2.95.61_FullSource.zip`
- Base SHA-256: `63bb04e7f9bbb15fa76ff00ab833b392bf6d48e71ecafd8740b05c2ff1cb56b7`
- Base source root: `Toeic_Dictionary_v2.95.61/`
- Base repository commit in the isolated working repository is recorded in the package manifest and package verification report.

## Implementation

- `data/related-terms.json`: 21 existing relation-target entries updated with POS, paraphrased English definitions and Cambridge provenance using exact-old-value guards; no rows added or deleted.
- `patches-related-terms/v2.95.62/related-terms-043.json`: guarded patch bound to SHA-256 `5783c70ea0ae04b12f2ee8ca220d2bb6a218c7766486319cce5ecc395c0f24d8`.
- `patches-related-terms/v2.95.62/batch-043-glossary-ledger.json`: per-entry source URLs, sense anchors, preserved Vietnamese gloss, relation anchors and editorial review status.
- `tools/tests/test_related_glossary_batch_043.py`: six new regression tests for inventory, anchors, POS/definitions/provenance, guarded reconstruction and unchanged meaning/relations.
- Historical tests/helpers reverse Batch 043 before reconstructing Batch 025 and Batches 038–042; live quality/candidate/backfill expectations track the measured v2.95.62 glossary counts.
- `.github/workflows/validate-data.yml`: register the new test in Python compilation and dedicated unit-test execution.

## Release metadata and evidence

- Version markers synchronized to 2.95.62; visible UI changes are limited to version text/cache version, with no layout or navigation changes.
- Updated root/docs changelogs, Master Status and current-version reference.
- Added Batch 043, quality audit, enrichment queue, coverage, question-evidence, distractor, test, command and package reports.

## Protected surfaces

No changes to canonical vocabulary IDs/headwords/senses/relation arrays; Reading/Listening/Grammar/Part 5 content, question IDs, choices or answer keys; Mock eligibility/reserve state; learner records, IndexedDB schema or Robot Buddy data boundary; CSS/layout/navigation; external services/backends.
