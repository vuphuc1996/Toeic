# Test Report — TOEIC Dictionary v2.66.1

## Release scope verified

1. Shared Speech Synthesis preparation is fixed at 2,000 ms after the voice catalogue readiness check and residual queue cleanup. No setting field can override this delay.
2. Listening Part 1 speech order is `Part 1: [Topic]` → 1,000 ms → `Now, listen to the four statements.` → 1,000 ms → `A.` → 1,500 ms → description → 1,300 ms → repeat for B, C and D.
3. Practice Listening and Mock Exam share the same `playListeningAudio()` pipeline for Part 1. Mock Exam does not prepend a duplicate generic transition to a Part 1 group.
4. The in-app transcript and Mock Exam audio hint reflect the same topic, lead-in, labels and timing.
5. GitHub's failing `test_learning_progress_persists_selected_choice_index` was stale: it expected immediate `recordPracticeAnswer()` on selection. It now validates the current deferred-assessment contract (`stagePracticeChoice()` on selection and `commitPracticeDraftSet()` only after full-set confirmation).

## Python tests

**85/85 selected test cases PASS across 10 modules.**

| Module | Result |
|---|---:|
| `test_tts_readiness.py` | 13/13 |
| `test_distractor_quality.py` | 6/6 |
| `test_sync_version.py` | 12/12 |
| `test_pwa_readiness.py` | 3/3 |
| `test_ci_coverage.py` | 2/2 |
| `test_learning_surface_consistency.py` | 5/5 |
| `test_learning_content.py` | 34/34 |
| `test_learning_outcomes.py` | 3/3 |
| `test_learning_outcome_progress.py` | 3/3 |
| `test_part1_photo_assets.py` | 4/4 |
| **Total** | **85/85** |

The full Python discovery suite was not run in this release check; the count above is the named focused test set only.

## JavaScript regression

**21/21 scripts PASS**, including:

- `runtime-render-smoke.mjs`
- `listening-tts-regression.mjs`
- `mock-exam-engine.mjs`
- `mock-guided-flow.mjs`
- `mock-ui-integrity.mjs`
- `assessment-deferred-workflow.mjs`
- `practice-progress.mjs`
- Foundation, recall, vocabulary-release and sentence-completion regressions.

All `assets/js/*.js` files and `sw.js` pass Node syntax checks. Both focused Python test files pass `py_compile`.

## Data, version and design validation

- `python tools/sync-version.py --check`: PASS (manifest, app.js, Service Worker, HTML and documentation agree on v2.66.1).
- `python tools/sync-design-profile.py --check`: PASS (54 canonical tokens; 362 legacy font-floor selector groups synchronized).
- `python tools/validate-data.py`: 992 vocabulary records; **0 errors, 0 warnings**.
- `python tools/validate-learning-content.py`: **0 errors, 8 warnings** for missing original Part 1 JPG byte assets; corresponding SVG fallbacks remain declared.
- `python tools/validate-part1-photo-assets.py`: **FAIL, 8 missing original JPGs (1/9 present)**. This strict media gate is intentionally unchanged and remains a deployment blocker.

## GitHub error diagnosis

The pasted `Ran 6 tests ... FAILED (failures=1)` was reproduced by `test_distractor_quality.py`. The failing assertion expected immediate `recordPracticeAnswer(...)` in the app source, which contradicts the v2.66.0 deferred-answer workflow. The test now checks that an option is staged as a draft and that commit occurs only in `confirmPracticeBatchResult()` after the complete answer set. The long `app.js` body in the traceback was Python's escaped representation of a string value, not literal escaped source. `buildOneWayGoogleAIUrl()` is intact and JavaScript syntax checks pass.

## Not verified

- Real audible onset, exact timing, English letter pronunciation and voice choice on Windows, iOS/iPadOS and Android devices.
- Remote GitHub Actions or GitHub Pages deployment.
- Browser-rendered visual QA on physical devices.

## Data preservation

No vocabulary/question content, answer keys, stable IDs, IndexedDB schema/stores, personal vocabulary, answer history, selected voices, rate, pitch or volume were reset or migrated. Deprecated timing settings from older releases are ignored; the new fixed timing constants apply to all devices.
