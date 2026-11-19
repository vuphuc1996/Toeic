# Test Report — TOEIC Dictionary v2.95.0

- Release: **2.95.0**
- Baseline: v2.94.0
- Scope: Robot Buddy page actions and progress dashboard, review-mode recovery, Flashcard result-modal layering, Reading/Listening narration sequence, CI/editorial-review assertions and repository integrity.
- Verification class: local automated checks only. This is not remote GitHub Actions, deployed Pages or physical-device acceptance.

## Changes verified

1. Robot Buddy delegated click handling accepts both `data-robot-command` and `data-robot-page`. Page actions close Buddy and navigate to the selected module. Progress insight replies render one progress dashboard and do not repeat a prose summary beside it; navigation actions are placed within the dashboard.
2. `editorial_review` tests were updated to validate current Part 7 resource/question inventory using structural and monotonic assertions rather than stale release-specific counts. The test module passes 4/4. `question_evidence` continues to index the current 502 question inventory and passes 6/6.
3. Review mode resolves Part 5 question headwords against immutable release vocabulary when a user has hidden a personal dictionary entry. Empty or unavailable modes can fall back through common valid practice modes. The active heading reflects the actual mode chosen. Six dedicated fallback/flashcard tests pass.
4. Flashcard completion result modal uses the `assessment-result` stacking layer above the focused learning workspace. Confirmation remains required before the existing answer/progress workflow continues.
5. Listening and Reading narration uses the part title, lead-in, passage/dialogue, question and separately spoken A/B/C/D option labels/content with the defined pauses. This behavior is covered by TTS regression tests.
6. CI coverage checks verify Python test discovery and JavaScript suite registration. Repository-integrity preflight validates local paths, PWA shell references, HTML/CSS/JS dependencies, workflow references and JSON parsing.

## Local verification results

| Check | Result |
|---|---:|
| JavaScript regression suites | **33/33 PASS** |
| Focused Python tests | **87/87 PASS** across 15 modules |
| Python syntax compilation | **All `tools/**/*.py` PASS** |
| `test_editorial_review.py` | **4/4 PASS** |
| `test_question_evidence.py` | **6/6 PASS** |
| `test_practice_mode_fallback.py` | **6/6 PASS** |
| `test_tts_readiness.py` | **15/15 PASS** |
| CI coverage test | **2/2 PASS** |
| Repository-integrity unit test | **1/1 PASS** |
| Repository-integrity preflight | **362 local references/data files; 0 errors; 0 optional warnings** |
| Vocabulary validator | **1,141 records; 0 errors; 0 new warnings (legacy warnings not promoted)** |
| Learning-content validator | **0 errors; 0 warnings** |
| Objective-resource mapping | **339/339 links** |
| Question-evidence audit | **502 questions indexed** |
| Distractor structural audit | **PASS** |
| Foundation A2 assessment audit | **PASS** |
| Part 1 photo assets | **9/9 PASS** |
| Version synchronization | **PASS — 2.95.0** |
| Design profile synchronization | **PASS — 54 tokens / 406 font-floor selector groups** |
| JavaScript syntax checks | **PASS** |

The 87 selected Python tests comprise the following focused modules: practice-mode fallback (6), editorial review (4), question evidence (6), CI coverage (2), repository integrity (1), TTS readiness (15), responsive layout (7), sentence completion (12), learning detail scope (4), Grammar examples quality (4), project progress (4), objective-resource map (2), Foundation A2 assessment quality (8), Part 1 photo assets (6), and design profile (6).

## Full-discovery limitation

A full `python -m unittest discover -s tools/tests -p 'test_*.py' -v` attempt exceeded the local execution limit and did not complete. It is **not** reported as a full Python-suite pass. CI has explicit discovery commands for each registered test module; the remote workflow result must still be checked after push.

## Not yet verified

- GitHub-hosted Actions result after pushing this exact source.
- GitHub Pages deployment and cache propagation.
- Actual audible output on the user's Windows, iOS, Android and tablet devices.
- Real touch interaction and visual acceptance on laptop 15.6-inch at 100%, phones and tablets.
- Production user acceptance and independent editorial review of reserve content.

## Data-preservation boundary

No IndexedDB schema migration, learner-progress reset, local progress export or remote upload was introduced. Existing vocabulary, practice, Flashcard, Reading, Listening, Foundation and Mock evidence stores remain intact. TOEIC Listening/Reading remains the active scope; Foundation B1 remains blueprint-only; Speaking/Writing and IELTS are deferred.
