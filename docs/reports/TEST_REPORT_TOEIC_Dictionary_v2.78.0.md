# Test Report — TOEIC Dictionary v2.78.0

**Release:** A2 Contextual Production Tasks & Separate Learner Evidence  
**Date:** 2026-11-16  
**Base:** v2.77.0 Full Source  
**Execution scope:** local source tree; remote GitHub Actions, GitHub Pages and physical devices were not tested.

## Summary

| Check | Result |
|---|---:|
| Selected Python tests | **154/154 PASS** across 21 fully executed modules |
| JavaScript regression scripts | **23/23 PASS** |
| Python syntax compilation | **65/65 files PASS** |
| JavaScript module syntax | **12/12 PASS**, plus `sw.js` |
| Vocabulary validator | **1,137 records; 0 errors / 0 warnings** |
| Learning-content validator | **0 errors / 0 warnings** |
| Part 1 photo validator | **9/9 PASS** |
| Objective-resource map | **294/294; 11/11 objectives** |
| Learning outcome audit | **11/11 objectives; 33 criteria; 6 evidence paths** |
| A2 Reading/Listening audit | **13/13 resources each; 39/39 questions each; source evidence 5/5** |
| Design profile | **54 tokens; 363 typography selector groups PASS** |
| Version synchronization | **All registered markers v2.78.0 PASS** |
| CMUdict IPA ledger | **333 source-linked records PASS** |

## Python test modules

| Module | Tests |
|---|---:|
| `test_foundation_outcome_evidence.py` | 2 |
| `test_learning_outcomes.py` | 3 |
| `test_project_progress.py` | 4 |
| `test_foundation_pathway.py` | 10 |
| `test_ci_coverage.py` | 2 |
| `test_design_profile.py` | 6 |
| `test_foundation_reading.py` | 9 |
| `test_foundation_listening.py` | 13 |
| `test_learning_content.py` | 34 |
| `test_learning_outcome_progress.py` | 3 |
| `test_learning_start_level.py` | 4 |
| `test_learning_surface_consistency.py` | 5 |
| `test_objective_resource_map.py` | 2 |
| `test_pwa_readiness.py` | 3 |
| `test_responsive_layout.py` | 5 |
| `test_sync_version.py` | 12 |
| `test_part1_photo_assets.py` | 6 |
| `test_sentence_completion.py` | 12 |
| `test_vocabulary_batch_012.py` | 4 |
| `test_foundation_a2_assessment_quality.py` | 8 |
| `test_foundation_a2_production.py` | 7 |
| **Total** | **154** |

The Python total is a selected, explicit set of fully completed modules. It is not a claim that every Python test file in the repository was executed; `test_validator.py` is not included in this report's PASS total.

## JavaScript regression scripts

All 23 scripts passed: `alphabet-sound-progress.mjs`, `assessment-deferred-workflow.mjs`, `explanation-rubric-self-report.mjs`, `flashcard-image-policy.mjs`, `foundation-a2-production.mjs`, `foundation-application-evidence.mjs`, `foundation-evidence.mjs`, `foundation-listening-evidence.mjs`, `foundation-outcome-evidence.mjs`, `foundation-reading-evidence.mjs`, `learning-focus-workspace.mjs`, `learning-outcome-progress.mjs`, `listening-tts-regression.mjs`, `mock-exam-engine.mjs`, `mock-guided-flow.mjs`, `mock-ui-integrity.mjs`, `objective-recall-timing.mjs`, `part5-timing-integration.mjs`, `practice-progress.mjs`, `recall-queue.mjs`, `runtime-render-smoke.mjs`, `sentence-completion.mjs`, and `vocabulary-release-integrity.mjs`.

## Key v2.78.0 coverage

- 13/13 A2 writing tasks are present and each task has a stable `::produce1` ID separate from its old `::apply1` application ID.
- The response validator rejects fewer than eight words for A2 and keeps the previous three-word fallback for older Foundation levels.
- The new task content matches its immutable SHA-256 baseline; three self-review criteria, sentence frame and model-answer example are present for every lesson.
- The hidden model answer is collapsed by default; it is an example, not the only accepted answer.
- Old A2 `::apply1` evidence stays in the existing progress record and is not reused as proof that the new `::produce1` task has been completed.
- Storage remains additive: the existing `toeic:foundation-progress:v1` key is retained; no IndexedDB v1 schema/store migration, reset or backend is introduced.

## Validator notes

- `validate-data.py`: 1,137 records, 0 errors, 0 warnings. The validator logs 93 missing IPA records; these remain intentionally blank rather than guessed.
- `validate-learning-content.py`: Listening 107 units / 201 questions, Reading 51 / 200, Grammar 33 lessons / 86 exercises, separate Part 5 practice 80 questions; no errors or warnings.
- `validate-part1-photo-assets.py`: all 9 JPG assets pass.
- `audit-objective-resources.py`: all 294 resource links across 11 objectives are mapped.
- `audit-learning-outcomes.py`: 33 outcome criteria are defined; 6/33 have evidence-collection paths. Evidence wiring does not imply learner mastery.
- `audit-foundation-a2-assessment.py`: A2 Reading and Listening 13/13 resources each, 39 questions each, five source evidence pointers verified, balanced answer counts 15/15/15/14.
- `audit-listening-readiness.py`: 102 eligible and 99 pending independent review; pending content remains excluded from Mock.
- `audit-question-evidence.py`: 401 indexed questions; the report is an evidence-inventory audit, not editorial approval.
- `audit-distractors.py`: structural audit passed for its 177-question review scope; 12 revisions are flagged/recorded. This is not psychometric or independent editorial certification.
- `sync-design-profile.py --check`: PASS; `sync-version.py --check`: all current markers v2.78.0.
- `cmudict_ipa.py --check`: 333 source-linked pronunciation records PASS.

## Not verified

No remote GitHub Actions run, GitHub Pages deployment, live cache refresh, iOS/Android/desktop device test, or real device SpeechSynthesis voice-quality check was performed. The 13 new writing tasks have not received independent second-person linguistic review or empirical learner testing. Their rubric values are learner self-report, not machine-graded writing scores or CEFR/ETS mastery.
