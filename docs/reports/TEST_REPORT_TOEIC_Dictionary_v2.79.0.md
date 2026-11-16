# Test Report — TOEIC Dictionary v2.79.0

- **Build:** v2.79.0 — A2 Guided Writing Revision.
- **Base:** v2.78.0.
- **Environment:** local working tree; these results do not establish remote GitHub Actions or deployed Pages state.

## Completed automated checks

| Check | Result | Scope |
|---|---:|---|
| Selected Python regression | **151/151 PASS** | 21 complete modules listed below |
| JavaScript regression | **24/24 PASS** | Every `tools/tests/*.mjs` suite |
| Python syntax compilation | **45/45 PASS** | Exact source list in `.github/workflows/validate-data.yml` |
| JavaScript syntax | **12/12 PASS** | All `assets/js/*.js` parsed as modules |
| Service Worker syntax | **PASS** | `sw.js` |
| Version sync | **PASS** | manifest, app, SW, HTML and docs markers |
| Canonical design profile | **PASS** | 54 tokens / 363 legacy typography groups |
| CMUdict IPA check | **PASS** | 333 source-linked records |
| Vocabulary validator | **PASS** | 1,137 records; 0 errors / 0 warnings |
| Learning-content validator | **PASS** | 0 errors / 0 warnings |
| Part 1 photo validator | **PASS** | 9/9 JPGs |
| Objective-resource audit | **PASS** | 11 objectives; 294/294 links |
| Learning-outcome audit | **PASS** | 11/11 objectives; 33 criteria; 6 evidence paths |
| Foundation A2 assessment audit | **PASS** | Reading 13/13, Listening 13/13; 39 questions each; source evidence 5/5 |
| Runtime render/migration smoke | **PASS** | Included in JS regression suite |

### Python modules included in the 151-test total

| Module | Tests |
|---|---:|
| `test_foundation_production_revision.py` | 6 |
| `test_foundation_a2_production.py` | 7 |
| `test_ci_coverage.py` | 2 |
| `test_sync_version.py` | 12 |
| `test_design_profile.py` | 6 |
| `test_learning_content.py` | 34 |
| `test_foundation_pathway.py` | 10 |
| `test_foundation_reading.py` | 9 |
| `test_foundation_listening.py` | 13 |
| `test_foundation_outcome_evidence.py` | 2 |
| `test_learning_outcomes.py` | 3 |
| `test_learning_outcome_progress.py` | 3 |
| `test_project_progress.py` | 4 |
| `test_objective_resource_map.py` | 2 |
| `test_pwa_readiness.py` | 3 |
| `test_responsive_layout.py` | 5 |
| `test_learning_surface_consistency.py` | 5 |
| `test_part1_photo_assets.py` | 6 |
| `test_sentence_completion.py` | 12 |
| `test_vocabulary_batch_012.py` | 4 |
| `test_release_rotation.py` | 3 |
| **Total** | **151 across 21 modules** |

## Execution boundary

A separate all-module `unittest discover -p 'test_*.py'` attempt exceeded the five-minute command limit while executing `test_project_progress.py`; it did not produce a complete all-module result and is not counted. The completed selected modules above were rerun individually and all finished successfully. In particular, this report does not state that every Python test module in the repository was executed.

## Product-specific checks

- All 13 A2 tasks have topic-specific revision checklist items and a revision hint.
- First and revised response versions are linked in local evidence history.
- Identical revisions, under-length responses, missing review confirmations and missing self-ratings are rejected.
- Existing `::produce1` and legacy `::apply1` evidence are not mixed.
- No IndexedDB migration, localStorage key change, learner reset, backend upload or automatic language grade.

## Not verified

- Remote GitHub Actions execution.
- GitHub Pages deployment and cache behavior in the public site.
- Real-device interaction and SpeechSynthesis behavior on iOS/Android/desktop.
- Independent second-person linguistic/content review.
