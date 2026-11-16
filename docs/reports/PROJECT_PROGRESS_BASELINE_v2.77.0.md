# Project Progress Baseline — TOEIC Dictionary v2.77.0

- Snapshot date: 2026-11-16.
- Base source: v2.76.0.
- Scope: focused A2 assessment-quality/source-evidence pass on top of v2.76.0. Five identified q2/q3 repetitions are corrected across 13 A2 Reading and 13 A2 Listening resources; prior A2 q1/q2 pairs, lesson inventory, vocabulary, TOEIC banks, images and Foundation outcome instrumentation are retained.
- Reporting rule: percentages are displayed only where a defensible target/denominator exists. Inventory and instrumentation do not equal independent approval or learner mastery.

## Target-based status

| Measure | Current | Target | Progress | Interpretation |
|---|---:|---:|---:|---|
| Vocabulary headwords | 1,137 | 3,000 minimum | 37.9% | Inventory only |
| Vocabulary planning ceiling | 1,137 | 5,000 | 22.7% | Planning reference, not official ETS list |
| Guided pathway stages represented | 3 | 6 | 50.0% | Pre-A1/A1/A2 represented; not complete stage coverage |
| Canonical objective-resource links | 294 | 294 | 100% | Link integrity only |
| Objectives with linked resources | 11 | 11 | 100% | Resource availability only |
| Outcome criteria defined | 33 | 33 | 100% | Framework definition, not mastery |
| Outcome criteria with evidence path | 6 | 33 | 18.2% | Instrumentation only |
| Foundation outcome evidence wired | 6 | 6 | 100% | Recognition, learner self-report production/explanation and delayed recall collection paths |
| TOEIC objective practice evidence wired | 9 | 9 | 100% | Practice evidence path only |
| TOEIC delayed recall scheduling wired | 9 | 9 | 100% | 1/3-day schedule; not a retention guarantee |

## Foundation inventory

- 23 lessons: 10 Pre-A1/A1 and 13 A2.
- The 13 A2 lessons include introductory Present Perfect, basic Passive Voice and defining Relative Clauses. Reading contains 13 passages of 69–80 words; Listening contains 13 four-turn dialogues of 51–74 words.
- Recognition/application: 69 recognition questions and 23 contextual-application tasks across the 23 Foundation lessons; A2 contributes 39 recognition questions and 13 application tasks.
- Reading: 23 passages / 59 questions (20 Pre-A1/A1 + 39 A2).
- Listening: 23 scripts / 59 questions (20 Pre-A1/A1 + 39 A2); A2 uses four-turn male/female device-TTS dialogues, not ETS/native recordings.
- A–Z: 26/26 letter records; TTS action tracking does not evaluate pronunciation.
- Production tasks save learner-authored text plus three self-report checks. This is not auto-grading.
- Recognition remains based on stable unique question IDs and latest result per question. Delayed recall is separately recorded and cannot inflate recognition denominators.
- A2 now has three questions per Reading/Listening resource with a 67% local practice threshold; Pre-A1/A1 remains 2 / 80%. These are not CEFR/mastery gates. More varied material, broader application and independent review remain open.

## Vocabulary quality fields

- US IPA: 1,044/1,137 (91.8%); the structural validator reports 93 empty IPA records. Do not fill uncertain pronunciation by guessing.
- Word-family records: 276/1,137 (24.3%); 374 directed links.
- Verb forms: 325/1,137 (28.6%).
- Collocations: 967/1,137 (85.0%).
- Synonyms: 404/1,137 (35.5%).
- Antonyms: 213/1,137 (18.7%).

## Verification and limitations

- Local selected Python tests: 147 PASS across 20 fully executed modules; other modules, including the generic full `test_validator.py` suite, are not counted.
- JavaScript regression: 22/22 suites PASS; all `assets/js/*.js` syntax and `sw.js` syntax PASS.
- Python syntax: 64/64 Python files under `tools/` compile successfully.
- Data validator: 1,137 records, 0 errors / 0 warnings.
- Learning-content validator: 0 errors / 0 warnings.
- Strict Part 1 photo validation: 9/9 PASS.
- Objective-resource audit: 294/294 links; learning-outcome audit: 11/11 objectives, 33 criteria and 6 evidence paths (Foundation 6/6).
- Design-profile sync and release-version sync PASS.
- Remote GitHub Actions, GitHub Pages deployment, independent A2 language review and physical iOS/Android/desktop QA remain unverified.

For generated row-by-row ratios, see `PROJECT_PROGRESS_SNAPSHOT_v2.77.0.md`.

## A2 assessment-quality checkpoint

- Focused audit scope: 13 A2 Reading resources / 39 questions and 13 A2 Listening resources / 39 questions (78 question records total).
- Five question tasks were revised to avoid identified q2/q3 repeated-information cases; five revised questions carry exact `evidenceText` pointers that are confirmed as substrings of the source passage/dialogue.
- Existing A2 q1/q2 question objects remain unchanged by the canonical v2.75.0 SHA-256 baseline; question IDs and full-bank answer positions remain stable.
- The focused audit verifies four unique options, valid keys, prompt/rationale presence, non-identical q2/q3 correct answers, source-evidence integrity and full-bank answer distribution. It does not certify every distractor semantically.
- This is internal single-author review. Independent second-person language review and psychometric validation remain pending.
