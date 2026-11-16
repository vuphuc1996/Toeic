# Test & Release Report — TOEIC Dictionary v2.77.0

- Date: 2026-11-16.
- Source base: exact v2.76.0 Full Source ZIP.
- Release state: local full-source release candidate; remote deployment not verified.

## Regression tests

- **Python: 147/147 PASS** across 20 fully executed modules. Selected modules:

1. `test_foundation_outcome_evidence.py` — 2 tests
2. `test_learning_outcomes.py` — 3 tests
3. `test_project_progress.py` — 4 tests
4. `test_foundation_pathway.py` — 10 tests
5. `test_ci_coverage.py` — 2 tests
6. `test_design_profile.py` — 6 tests
7. `test_foundation_reading.py` — 9 tests
8. `test_foundation_listening.py` — 13 tests
9. `test_learning_content.py` — 34 tests
10. `test_learning_outcome_progress.py` — 3 tests
11. `test_learning_start_level.py` — 4 tests
12. `test_learning_surface_consistency.py` — 5 tests
13. `test_objective_resource_map.py` — 2 tests
14. `test_pwa_readiness.py` — 3 tests
15. `test_responsive_layout.py` — 5 tests
16. `test_sync_version.py` — 12 tests
17. `test_part1_photo_assets.py` — 6 tests
18. `test_sentence_completion.py` — 12 tests
19. `test_vocabulary_batch_012.py` — 4 tests
20. `test_foundation_a2_assessment_quality.py` — 8 tests

- **JavaScript: 22/22 regression suites PASS**, including Foundation outcome/Reading/Listening evidence, runtime rendering/migration, mock flow, vocabulary integrity and Listening/TTS regression.
- Python compile: **64/64** files under `tools/` compile successfully.
- JavaScript syntax: **12/12** `assets/js/*.js` files plus `sw.js` pass `node --check`.
- The generic `test_validator.py` suite is not included in the selected Python total; it is not counted as PASS.

## Data and contract validators

- `validate-data.py`: 1,137 headwords, 0 errors, 0 warnings; 93 intentionally blank IPA records remain rather than being guessed.
- `validate-learning-content.py`: 0 errors / 0 warnings; TOEIC Listening 107 units / 201 questions, Reading 51 resources / 200 questions, Grammar 33 lessons / 86 exercises, separate Part 5 practice 80 questions.
- Strict Part 1 photo validator: 9/9 PASS.
- Objective-resource audit: 11 objectives; 294/294 linked records.
- Learning-outcome audit: 11/11 objectives, 33 criteria, 6/33 evidence paths; Foundation instrumentation 6/6. Wiring is not learner mastery.
- Design profile: 54 tokens and 363 legacy typography selector groups synchronized.
- Release sync: manifest, app, service worker, page markers, README, Master and changelog all v2.77.0.
- Dedicated A2 audit: 13/13 Reading, 13/13 Listening, 78 questions; five q2/q3 repetition fixes, five exact source-evidence pointers, valid four-choice answer structures and balanced full-bank A/B/C/D = 15/15/15/14.

## Foundation A2 preservation and scope

- Foundation inventory remains 23 lessons; Reading 23 resources / 59 questions; Listening 23 resources / 59 questions.
- All 13 A2 Reading passages and 13 A2 four-turn Listening dialogues retain three questions each.
- All pre-existing A2 q1/q2 question objects remain unchanged against `tools/foundation-a2-question-baseline-v2.75.0.json`. Pre-A1/A1 resources, existing lesson/question IDs, prior answer keys and progress stores remain untouched.
- Revised A2 questions: Reading `a2-quantities`, `a2-comparisons`, `a2-obligation-permission` q3; Listening `a2-comparisons` and `a2-sequencing-instructions` q3.
- Each revised question has exact `evidenceText` checked against the actual passage or spoken segment. Existing 67% A2 / 80% Pre-A1/A1 local practice thresholds are unchanged.
- Existing two-gender device SpeechSynthesis and configured speaker pacing remain unchanged; no new audio asset or dependency was added.

## Archive and scope limits

- ZIP and TAR.GZ are created from the full project root without a wrapper directory. They are separately extracted for validation; checksums are verified.
- No localStorage key, IndexedDB v1 database/store/schema, learner profile, historical progress, personal vocabulary, settings or TOEIC L&R question pool is reset/migrated.
- No GitHub Actions remote run, GitHub Pages deployment, browser offline session, physical Android/iOS/desktop QA or independent second-person language review is claimed. The focused review is internal and does not constitute psychometric validation, CEFR mastery or ETS equivalence.
