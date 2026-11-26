# Test Report — TOEIC Dictionary v2.95.69

## Summary

- **Python inventory: PASS WITH SKIPS (accepted skip policy).** 104/104 modules completed; 785 cases collected; 784 PASS, 0 FAIL, 1 accepted SKIP, 0 errors. Module results: 103 PASS, 1 PASS WITH SKIPS, 0 FAIL, timeout, incomplete or error.
- **Node regression: 44/44 PASS**, 0 failed.
- **Data validator: PASS** — 1,141 canonical records; baseline ID set present; +0/-0 IDs; 0 new errors and 0 warnings.
- **Learning-content validator: PASS** — 0 errors, 0 warnings. Inventory includes Listening 145 units/295 questions (102 eligible, 193 reserve), Reading 73/287, Grammar 58/169 and Part 5 80 practice-only questions pending independent review.
- **Part 1 photo assets: PASS** — 9/9 valid, zero missing-photo warnings.
- **Repository integrity: PASS** — 408 local references/data files inspected; 0 errors, 0 optional warnings.
- **Version synchronisation: PASS** — 18 standard markers, 17/17 local `app.js` import cache keys and 42/42 Service Worker release-keyed cache URLs match manifest `2.95.69`.
- **JavaScript syntax: PASS** — `node --check assets/js/app.js` and `node --check sw.js`.
- **Design-token audit:** 0 new violations; 2,773 legacy findings remain (warnings only).
- **Word Family graph audit:** read-only; results and review-only flags in `WORD_FAMILY_GRAPH_AUDIT_v2.95.69.md`.

## Python inventory evidence

The complete dynamically discovered inventory contains 104 modules, up from 88 in the v2.95.45 baseline (16 added, 28 modified, 0 removed; no suspected renames). No modules were excluded or deselected. The aggregate combines disjoint completed evidence: 96 modules from the resumable full-inventory runner, seven final module invocations after correcting the release-dynamic Word Family test, and the 44-case `test_validator.py` module run in one full `unittest discover` invocation (61.889 seconds, PASS). The aggregate report records all 104 distinct module rows and its test-snapshot fingerprint.

The one accepted skip is `tools/tests/test_patch_data.py::test_repository_gitignore_excludes_audit_logs`: the FullSource ZIP has no `.git` metadata and this assertion requires a Git clone; the other 19 tests in that module passed. No test case was removed or silently deselected.

See `PYTHON_TEST_SHARDS_v2.95.69.md/.json` for each module, case count, timing, and skip rationale.

## Significant defects closed during this batch

1. **Release cache coherence:** changing the manifest release to `.69` previously left 17 local module import URLs in `assets/js/app.js` and 42 Service Worker `REQUIRED`/`APP_SHELL` URLs keyed to `.68`. `tools/sync-version.py` now updates/checks every cache-busting key in both files. Regression tests cover discovery, apply and verification. Current counts are 17/17 and 42/42 on `.69`.
2. **Historical test reconstruction:** Batch 044 is reversed before reconstructing earlier glossary snapshots. Historical assertions remain active; count expectations were updated only where Batch 044 changes the actual audited counts.
3. **Learning Focus result contract:** Python and Node regression checks now enforce reuse of `learningFocusDialog` without a duplicate `modalLayer` during focused sessions; non-focused modal fallback remains. The stale Robot Buddy test expectation that described stacking has been corrected.

## Content and data review boundaries

Related Glossary Batch 044 updates 15 existing rows; the quality audit improves flagged entries from 157 to 142. Definitions are paraphrases of indexed Cambridge Dictionary entry excerpts and remain subject to independent editorial review. The Word Family audit is read-only: 90 missing canonical targets, 1 target POS mismatch, 72 Vietnamese sense-anchor mismatches and 10 non-reciprocal links are review flags, not auto-corrected data. There are no duplicate links/headwords or malformed records.

Canonical IDs/headwords/relations, question IDs, choice IDs, answer keys, protected learning-bank content, learner IndexedDB schema/records, UI design and Robot Buddy behavior remain unchanged. Data differences are fully detailed in `DATA_DIFF_v2.95.69.md`.

## Not verified

No hosted GitHub Actions run or live GitHub Pages deployment was initiated in this local task. Installed-PWA service-worker migration, offline/cache propagation, desktop browser behavior and iPad/iPhone/Android physical-device acceptance remain **UNVERIFIED**. The source is a locally validated release candidate, not a production deployment acceptance.

## Package reproducibility

- FullSource v2.95.69: 847 files, ZIP CRC valid.
- Patch from the exact v2.95.68 FullSource: 59 changed paths (31 added, 28 modified, 0 deleted).
- Clean replay: 847 files; 0 extra, 0 missing and 0 byte differences against FullSource.
- See `PACKAGE_VERIFICATION_v2.95.69.md`; archive SHA-256 values are delivered in external `.sha256` sidecars.
