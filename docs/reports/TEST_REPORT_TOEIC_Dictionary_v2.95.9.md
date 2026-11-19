# Test Report — TOEIC Dictionary v2.95.9

**Scope:** v2.95.8 baseline plus Robot Buddy progressive replies and locally composed context-aware response phrasing.

## Release changes verified

- Robot Buddy displays a preparation indicator, then progressively reveals the reply with a blinking caret. Text is inserted with `textContent`; streamed text is not injected as HTML.
- The renderer uses grapheme segmentation when `Intl.Segmenter` is available, falls back safely, and respects `prefers-reduced-motion`.
- A new user turn finishes any in-flight response before adding the next turn. Reply actions are appended only after the response completes.
- Supported feature, FAQ, contextual-help, encouragement and clarification responses are composed from local phrase groups, existing library content, rule-based intent and the active in-memory app/item context.
- Unknown prompts request clarification instead of fabricating an answer.
- No generative model, external API, backend, WebSocket or external learner-data transmission was added. Robot Buddy does not read IndexedDB/localStorage directly.
- Learning Insights remains opt-in and read-only through the app-provided in-memory snapshot. Existing dashboard, navigation, content, TTS and learner storage contracts remain in place.

## Automated verification

| Check | Result | Notes |
|---|---|---|
| JavaScript regression suites | **35/35 PASS** | Includes the new `robot-buddy-streaming.mjs` suite and existing Buddy/dashboard/layout suites |
| JavaScript syntax | **PASS** | Every `assets/js/*.js` file and `sw.js` passed `node --check` |
| Python syntax compilation | **PASS** | `python -m compileall -q tools` |
| Python test modules | **53/54 completed individually** | `test_validator.py` full module exceeded the 300-second execution window; 23 of 38 cases had reported `ok` before timeout. Two relevant cases (`test_new_defect_not_hidden_by_equal_count`, `test_manifest_total_words_wrong`) passed when run individually. Do not interpret this as 54/54 complete. |
| CI coverage | **3/3 PASS** | Confirms all JS suites and Python modules are included in workflow and editorial review has an explicit CI step |
| Repository integrity test | **1/1 PASS** | Dedicated Python test |
| Responsive-layout tests | **7/7 PASS** | Includes Robot Buddy input/dashboard layout checks |
| Version synchronization | **PASS** | App, Service Worker, HTML and current docs declare 2.95.9 |
| Repository integrity audit | **PASS** | 364 local references/data files inspected; 0 errors, 0 optional warnings |
| Vocabulary validation | **PASS** | 1,141 records; 0 errors, 0 new warnings; 213 additive IDs relative to the legacy baseline, 0 removed |
| Learning-content validation | **PASS** | Listening 121 units/239 questions; Reading 65/263; Grammar 50/137; separate Part 5 practice 80; 0 errors, 0 warnings |

### Test limitation

The full `test_validator.py` suite did not finish within its execution window. Although the first 23 of 38 cases returned `ok` and two relevant cases later passed in isolation, the remaining full-suite coverage is **not claimed as passing**. The remote GitHub Actions workflow must run after the source is uploaded to verify the full CI gate in its intended environment.

## Not verified in this workspace

- Remote GitHub Actions and GitHub Pages deployment/cache update.
- Browser-level visual acceptance of the streaming effect and its timing.
- Actual offline PWA installation/reconnect behavior after deployment.
- Screen-reader behavior and physical-device performance on Windows, iOS/iPadOS and Android.
- Audible TTS voice quality and real acoustic pause timing on each device.

## Data and release safety

- No IndexedDB schema change, localStorage key reset, learner-record migration or progress reset was made.
- Vocabulary/question content, answer keys, stable IDs and Mock eligibility were not changed by this Robot Buddy release.
- Generated `__pycache__`, `.pyc` and `.pyo` artifacts are excluded from the release ZIP.
- Local checks do not prove a successful GitHub push or deployment. Neither was performed by this test run.

## Conclusion

The v2.95.9 source passes the complete JavaScript regression suite, version/data/repository audits and the listed focused Python checks. One Python validator module remains partially unverified due to an execution timeout, and all deployment/browser/device acceptance gates remain open. Use `USER_ACCEPTANCE_TEST_v2.95.9.md` for post-upload acceptance.
