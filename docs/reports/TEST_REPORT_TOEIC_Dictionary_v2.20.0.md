# Test Report — TOEIC Dictionary v2.20.0

- **Date:** 2026-11-11
- **Baseline:** v2.19.0
- **Release:** v2.20.0 (local release candidate)
- **Platform:** static GitHub Pages + PWA; no backend.

## Release scope

Vocabulary example readability, per-sense example mapping, one-card-per-POS word details, Data Workspace detail-click handling, and validator regression gates. V2.19.0 sidebar viewport-height changes are retained.

## Unit tests

**164/164 test methods PASS**, accounted for by independently executed module/group runs rather than one uninterrupted test-discovery command:

- Non-validator suites: **129/129 PASS** across 15 modules, including 10 new vocabulary detail/example tests.
- Validator suite: **35/35 PASS** in three groups after the combined sandbox run exceeded its execution limit. This includes two new negative tests for invalid `sense_index` and a sense without a mapped example.
- New/expanded checks cover base ID preservation, example normalization/sorting, Data Workspace detail action, one card per POS, sense-index mapping, example completeness and duplicates, personal-copy preservation, typography, and invalid mapping rejection.

The grouped accounting is intentional: do not treat the timed-out monolithic command as a PASS; every method was separately accounted for in successful runs.

## Data validators and audits

- `tools/validate-data.py`: **928 records**, **0 errors**, **8 known legacy warnings**. The remaining warnings are FD001 collocation/headword traceability warnings affecting 7 records. The baseline decreased from 12 to 8 after resolving three duplicated cross-POS definitions and one example/headword mismatch. No new EX010/EX011 warning/error.
- Stable vocabulary ID set: **928/928 preserved**, no added/missing IDs. ID-set SHA-256 prefix: `dd1705e64c8df4ad`.
- Canonical examples: **954** across 928 headwords. Each example has a valid `sense_index`; all 51 senses within the 25 multi-sense headwords have at least one dedicated example. Short-example INFO count: **0**.
- `tools/validate-learning-content.py`: **0 errors, 0 warnings**; Listening 102, Reading 109, Grammar 54 exercises.
- Content coverage, editorial evidence and distractor audits regenerated for v2.20.0. The existing 211-question item pool remains intact; no question or answer keys were changed in this batch.
- `tools/sync-version.py --check`: PASS; manifest, HTML, Service Worker, README, Master and changelog synchronized to 2.20.0.

## Static/runtime checks

- `node --check assets/js/app.js`: PASS.
- `node --check sw.js`: PASS.
- `node tools/tests/runtime-render-smoke.mjs`: PASS (Reading P5/P7 multi-document, Grammar, and synthetic choice-identity/progress-mapping fixtures).
- Existing static shell tests include unique HTML IDs and app-shell path checks; 74/74 `APP_SHELL` paths exist.
- Workflow Python syntax configuration updated to compile the new test module; named `vocabulary_detail_examples` workflow step added.

## ZIP and integrity

Release ZIP: **204 files**; `ZipFile.testzip()` CRC check PASS; clean extraction and byte-for-byte comparison **204/204 PASS**. Archive root contains the app files directly (no additional enclosing project folder). SHA-256 sidecar is outside the ZIP: `TOEIC_Dictionary_v2.20.0_Vocabulary_Examples_POS_DataDetail.zip.sha256`.

## Explicitly not verified

- **Real browser/device:** Playwright navigation to the local app returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` in the sandbox. No screenshot, click-interaction run, 100% zoom observation or physical 15.6-inch laptop QA is claimed. Desktop/mobile CSS and regression tests are not equivalent to visual confirmation.
- **Remote CI / GitHub Pages:** no direct remote GitHub Actions rerun, commit/push or deployed Pages verification was performed in this environment. The user previously confirmed v2.17.0 on GitHub; v2.20.0 is a new local package for the next upload.
- **Personal IndexedDB:** database remains version 1, store `workspace`; no schema or object-store change. Per user instruction, no personal-profile import/export, reset, inspection or migration test was performed. Runtime smoke uses synthetic fixtures only.
- **Independent editorial approval:** automated corpus screening and this internal review do not equal review by a qualified TOEIC teacher or psychometric validation.

## Result

Local code, test methods, validators, runtime smoke and version synchronization are PASS as specified above. Release remains **local candidate / awaiting GitHub push, remote CI, real-browser visual QA and independent editorial signoff**.
