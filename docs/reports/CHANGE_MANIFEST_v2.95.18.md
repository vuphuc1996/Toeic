# Change Manifest — TOEIC Dictionary v2.95.18

## Release intent

A content-first maintenance release for the ten-day completion sprint. UI layout, navigation, CSS, component structure and runtime learning behavior are frozen. This release adds source-checked US IPA to existing records and strengthens regression/CI coverage for that batch.

## Base and target

- Base source: v2.95.17 FullSource.
- Candidate: v2.95.18.
- Canonical vocabulary: 1,141 headwords before and after.
- Stable ID-set SHA-256 before and after: `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.
- Added IPA values: 13; remaining blank US IPA values: 80.
- Allowed changed data path: `/phonetic/us` only.

## Source/data changes

- `data/vocabulary/A.json` through `data/vocabulary/E.json`: 13 blank US IPA values populated on existing stable IDs.
- `data/vocabulary/batch-024.json`: source/provenance ledger for 13 records.
- `patches/v2.95.18/batch-001-ipa.json`: version-locked patch with blank-value preconditions, path allowlist and stable-ID hash.
- `data/manifest.json`: release version advanced to 2.95.18; canonical 1,141-word inventory unchanged.

## Regression and CI changes

- `tools/tests/test_ipa_backfill_batch_024.py`: verifies the exact records, source evidence, blank-value preconditions, stable ID set and CI registration.
- `tools/tests/test_project_progress.py`: expected US IPA coverage updated to 1,061/1,141.
- `tools/tests/vocabulary-release-integrity.mjs`: requires v2.95.18 and validates Batch 024 provenance/manifest presence.
- `.github/workflows/validate-data.yml`: registers the new Python regression module and source file in CI checks.

## Version/documentation changes

- Updated registered release markers in `assets/js/app.js`, `sw.js`, `index.html`, README and version records.
- Updated `docs/CHANGELOG.md`, `docs/MASTER_STATUS.md`, current/previous version pointers and v2.95.18 evidence reports.
- Generated progress, vocabulary coverage, editorial evidence, distractor and Listening readiness reports for the candidate.

## Explicitly unchanged

- No UI layout, CSS, responsive breakpoints, navigation, or visual behavior.
- No headword, stable ID, meaning, sense, topic, word-family, verb-form, collocation, synonym or antonym relationship.
- No grammar, Listening or Reading question, answer key, explanation, translation or Mock eligibility.
- No learner record, localStorage key, IndexedDB schema, Service Worker runtime feature or network/API contract.

## Verification boundaries

- Source checks and local tests are recorded in `TEST_REPORT_TOEIC_Dictionary_v2.95.18.md`.
- Independent phonetic review remains pending.
- The complete Python test inventory did not finish within this execution environment; the dedicated `test_validator.py` module also exceeded the local time limit. CLI validators and focused regression groups did pass.
- Remote GitHub Actions, GitHub Pages, browser/device acceptance, owner manual checklist and deployment are not claimed.
- This manifest describes a local release candidate. No GitHub push or deployment has been performed.
