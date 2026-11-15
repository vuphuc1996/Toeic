# Test Report — TOEIC Dictionary v2.69.0

- Date: 2026-11-15
- Release: **v2.69.0**
- Scope: CMUdict US IPA backfill, word-family coverage, progress reporting, version sync, retained content integrity and core design/PWA/Listening/Reading regressions.

## 1. Focused Python test result

**178 tests passed across 20 Python test modules**. The selected modules were:

| Module | Tests |
|---|---:|
| test_alphabet_sound_lab.py | 7 |
| test_answer_position_balance.py | 4 |
| test_baseline_ids.py | 13 |
| test_choice_history.py | 5 |
| test_choice_identity.py | 9 |
| test_ci_coverage.py | 2 |
| test_remaining_content_review.py | 9 |
| test_cmudict_ipa_backfill.py | 5 |
| test_vocabulary_family_links.py | 5 |
| test_project_progress.py | 4 |
| test_sync_version.py | 12 |
| test_part1_photo_assets.py | 5 |
| test_pwa_readiness.py | 3 |
| test_learning_content.py | 34 |
| test_vocabulary_detail_examples.py | 12 |
| test_tts_readiness.py | 13 |
| test_dashboard_layout.py | 6 |
| test_design_system.py | 19 |
| test_design_profile.py | 6 |
| test_responsive_layout.py | 5 |
| **Total** | **178** |

`test_ci_coverage.py` confirms all Python test modules and all JavaScript regression suites are referenced by the CI workflow. This does not mean every module was executed in this local run.

## 2. JavaScript regression

- **21/21 JavaScript regression suites PASS**.
- `node --check assets/js/app.js`: PASS.
- `node --check sw.js`: PASS.
- Python compile checks for the new IPA tooling and focused tests: PASS.

## 3. Data and release checks

| Check | Result |
|---|---|
| `python tools/cmudict_ipa.py --check` | PASS — 261 source-linked entries |
| `test_cmudict_ipa_backfill.py` | 5/5 PASS |
| `test_vocabulary_family_links.py` | 5/5 PASS |
| `test_remaining_content_review.py` | 9/9 PASS |
| `test_project_progress.py` | 4/4 PASS |
| `test_sync_version.py` | 12/12 PASS |
| `test_ci_coverage.py` | 2/2 PASS |
| `python tools/validate-data.py` | 1,063 records; 0 errors; 0 warnings |
| `python tools/sync-design-profile.py --check` | PASS — 54 tokens and 361 legacy font-floor selector groups |
| `python tools/sync-version.py --check` | PASS — all release markers synchronized to 2.69.0 |
| `python tools/audit-toeic-coverage.py` | PASS — report generated |

## 4. Learning content and media

`python tools/validate-learning-content.py` reports 0 errors and 8 warnings because eight repository-owned original Part 1 JPG binaries are absent from this source snapshot. `python tools/validate-part1-photo-assets.py --allow-missing` passes with 1/9 photo bytes present and 8 warnings.

The **strict** command `python tools/validate-part1-photo-assets.py` exits with code 1 and reports 8 missing JPG files. This is a deployment blocker inherited from the provided source workspace; it is not a data/IPA failure. Preserve the eight original repository JPG files when merging the source. Do not create fake replacement photos or disable the strict validator.

## 5. Python suite completeness

The local execution covered the 20 selected modules listed above. A broad loop over every Python module was stopped by the execution time limit; `test_validator.py` and several non-selected modules are not claimed as locally passed in this release. No failure is reported for those unexecuted modules; they remain to be verified by remote CI.

## 6. Deployment status

- Local source checks: PASS for the selected scope above.
- Strict Part 1 asset gate: FAIL (8 missing JPG binaries).
- Remote GitHub Actions: not run/verified from this workspace.
- GitHub Pages deployment: not verified.
- Physical iOS/Android/desktop pronunciation QA: not performed.

Release state: **local release candidate / deployment hold**.
