# Test Report — TOEIC Dictionary v2.70.0

- Date: 2026-11-15
- Release: **v2.70.0**
- Scope: Batch 011 vocabulary, cumulative CMUdict IPA ledger, family-link updates, migration repair profiles, IPA missing-counter correction, content integrity and existing design/PWA/learning regressions.

## 1. Data validation

- `python tools/validate-data.py`: PASS — 1,100 canonical records, 0 errors, 0 warnings (legacy baseline warnings are distinguished from new debt); IPA coverage reports 1,009 populated and **91 missing**.
- `python tools/cmudict_ipa.py --check`: PASS — 298 source-linked entries.
- `python tools/audit-toeic-coverage.py`: PASS — report generated for 1,100 words, IPA 1,009, word-family 267, Listening 107/201 and Reading 51/200.
- `python tools/validate-learning-content.py`: PASS — 0 errors, 8 warnings for the eight missing original Part 1 JPG binaries.
- `python tools/sync-version.py --check`: PASS — all release markers synchronized to 2.70.0.
- `python tools/sync-design-profile.py --check`: PASS — 54 tokens and 361 legacy font-floor selector groups synchronized.

## 2. Focused Python tests

- Selected Python coverage: **157 tests PASS** across 19 fully completed test modules plus 2 focused validator regression methods. The completed modules include baseline IDs, version synchronization, remaining-content review, CI coverage, Part 1 metadata, PWA readiness, dashboard/design/responsive layout, CMUdict IPA, vocabulary families, vocabulary examples, project progress, learning-content, objective map/outcomes and placement diagnostics.
- IPA missing-counter regression: **2/2 tests PASS**, covering an absent `phonetic` object (still correctly reported as a structural error) and a missing `phonetic.us` key.
- `test_validator.py` was not run as a complete module; only the two new regression methods were run. Full Python test discovery is not claimed as complete. A broad run exceeded the available execution window; unexecuted modules remain for remote CI.

## 3. JavaScript and release integrity

- `node --check assets/js/app.js`: PASS.
- `node --check sw.js`: PASS.
- All **21/21 JavaScript regression suites** listed in the GitHub Actions workflow: PASS, including runtime rendering, TTS, Mock Exam, Focus Workspace, practice progress, learning-outcome evidence, Foundation evidence, alphabet sound progress and vocabulary-release integrity.
- `node --check` for all `assets/js/*.js` modules and `sw.js`: PASS.
- `node tools/tests/vocabulary-release-integrity.mjs`: PASS — 1,100 records, unique IDs/headwords, Batch 011 and 979/992/1026/1063 legacy migration profiles.
- Remote GitHub Actions has not been run or verified from this workspace.

## 4. Media gate and deployment

- `python tools/validate-part1-photo-assets.py --allow-missing`: PASS with 8 missing JPG warnings; only 1/9 original Part 1 JPG files is present in this source archive.
- Strict `python tools/validate-part1-photo-assets.py`: expected FAIL until the eight repository-owned original JPG binaries are restored. Do not fabricate replacement media or disable the strict validator.
- Remote GitHub Actions, GitHub Pages deployment and physical iOS/Android/desktop visual/audio QA are not verified.

## 5. Release state

**Local release candidate / deployment hold.** Batch 011 and canonical vocabulary checks pass, but this is not a deployable release until the original Part 1 media gate and remaining CI checks pass. Independent lexical review and CEFR-by-sense review for Batch 011 remain pending.
