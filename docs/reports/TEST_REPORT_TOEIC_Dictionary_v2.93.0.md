# Test Report — TOEIC Dictionary v2.93.0

**Release:** v2.93.0 — Batch 025 L/R expansion + Full Mock score-readiness evidence tracker  
**Base:** v2.92.0 Full Source  
**Date:** 2026-11-18

## 1. Release scope

- Grammar: +9 lessons / +27 exercises.
- Listening: +8 units / +20 questions (2 Part 2, 3 Part 3, 3 Part 4).
- Reading: +8 Part 7 resources / +36 questions (4 single × 4; 4 double × 5).
- Vocabulary: +4 headwords, canonical total 1,141.
- New local Full Mock score-readiness tracker: requires 3 completed 200-question Full Mocks; shows L/R practice accuracy averages and trend only. No ETS scaled-score conversion.
- No IndexedDB v1 migration, no new learning-progress key, no remote data transfer.

## 2. Automated verification

| Check | Result | Detail |
|---|---|---|
| JavaScript regression | PASS | 33/33 `.mjs` suites |
| Focused Python tests | PASS | 100/100 tests across 13 selected modules |
| Python compilation | PASS | `compileall` across `tools/` |
| Vocabulary validation | PASS | 1,141 records; 0 new ERROR / 0 new WARNING (legacy baseline retained) |
| CMUdict IPA validation | PASS | 333 source-linked records; new batch adds 4 single-pronunciation entries; no IPA guessed |
| Learning-content validation | PASS | Listening 121/239; Reading 65/263; Grammar 50/137; 0 errors / 0 warnings |
| Objective-resource mapping | PASS | 339/339 resource records linked; 11 objectives |
| Learning-outcome audit | PASS | 11/11 objectives; 33 criteria; 6/33 evidence paths |
| Batch 025 integrity/evidence | PASS | 9 Grammar / 27 exercises; 8 Listening / 20 questions; 8 Reading / 36 questions; 4 vocabulary records; hashes and evidence verified |
| Reading answer positions | PASS | Batch 025 A/B/C/D = 9/9/9/9 |
| Distractor structural audit | PASS | 240 questions in audit scope; unique choices and valid answer keys |
| Foundation A2 assessment audit | PASS | Reading 13/13, Listening 13/13, supplementary Listening 13/13; 5/5 evidence checks |
| Part 1 photo validation | PASS | 9/9 assets |
| Design profile | PASS | 54 tokens / 401 legacy font-floor selector groups |
| Version synchronization | PASS | manifest, app, SW, index, README, Master and Changelog all 2.93.0 |
| CSS parsing | PASS | app.css 1,837 top-level nodes / 0 parse errors; design-system.css 270 / 0 errors |
| PWA cache declaration | PASS | new `mock-score-readiness.js` included in REQUIRED and APP_SHELL |
| Mock exclusion boundary | PASS | 137 pending Listening questions and 63 new Part 7 reserve questions remain Mock-excluded |
| CI coverage | PASS | new Batch 025 Python test and Mock score-readiness Node test are registered in GitHub Actions workflow |

## 3. Content inventory after release

| Library | Total |
|---|---:|
| Vocabulary | 1,141 headwords |
| Grammar | 50 lessons / 137 exercises |
| Listening | 121 units / 239 questions |
| Reading | 65 resources / 263 questions |
| Separate Part 5 practice | 80 questions (practice-only / review pending) |

The 137 pending Listening questions consist of 99 earlier reserve questions, 18 added in v2.92.0 and 20 added in v2.93.0. The 63 new Part 7 reserve questions consist of 27 added in v2.92.0 and 36 added in v2.93.0. These items remain available for practice but excluded from Mock eligibility until independent approval.

## 4. Score-readiness behavior

- Reads existing device-local Mock history only.
- Counts completed Full Mock records with exactly 200 questions and both Listening/Reading accuracy values.
- Before three qualifying attempts, reports insufficient evidence.
- After three, reports L/R averages and direction of change across the latest three attempts.
- Quick/Half Mock attempts are not counted.
- No raw-accuracy-to-ETS conversion; no guarantee of 500+, 850+ or any official score.
- Unit regression covers empty, one/two attempts, three attempts, sorting and exclusion of non-Full attempts.

## 5. Not verified / acceptance still pending

- Full Python test discovery was not run; the 100 selected tests are the executed Python test scope.
- Remote GitHub Actions result is not verified.
- GitHub Pages deployment and production service-worker cache are not verified.
- Live browser UI, visual regression and physical-device checks (15.6-inch desktop at 100%, iOS, Android, tablet, offline/reconnect) are not verified.
- Independent second-person review of Batch 025 and previous reserve content is pending.
- Learner validation and official TOEIC score calibration are pending.

## 6. User acceptance test timing

This is the consolidated acceptance-test round requested by the user. The Full Source package is ready for one broad test pass. Hold v2.94.0 development until the user returns the results, then record defects and close the acceptance gates together.
