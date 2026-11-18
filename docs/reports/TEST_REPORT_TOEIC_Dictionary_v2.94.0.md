# Test Report — TOEIC Dictionary v2.94.0

**Release:** v2.94.0 — Voice reliability, Robot Buddy progress dashboard, Grammar example deepening and repository integrity preflight  
**Base:** v2.93.0 Full Source  
**Date:** 2026-11-18

## 1. User feedback addressed

| Feedback | v2.94.0 action | Status |
|---|---|---|
| `question_evidence` Unit tests fail on GitHub | Removed stale fixed counts; derive expected question/reserve categories from current source and audit output | Local PASS 6/6; remote Actions not verified |
| Buddy input zooms page on mobile/tablet | Chat input font floor is 16px; coarse-pointer tap targets tuned; pinch zoom remains enabled | CSS/regression PASS; device UAT pending |
| Some Grammar lessons lack complete examples/analysis | Enriched 42 bilingual examples across the newest 17 lessons with sentence breakdowns | Quality tests PASS; earlier lessons remain backlog |
| Listening / Reading voice sometimes silent | Removed shadowed duplicate TTS functions; synchronous queue, system-default fallback and start/end watchdogs; actionable statuses | Local regression PASS; real speaker output pending device UAT |
| Progress analysis hard to discover / not visual | Welcome CTA triggers analysis; dashboard shows Cần học/Cần luyện/Cần ôn totals and colored, accessible per-module meters | Logic/layout regression PASS; device UAT pending |
| Remove test-only clutter | Corrected stale two-second voice note; automated tests/audits remain developer/CI-only and are not presented as learner content | Source scan; no learner-facing QA/debug page introduced |

## 2. Release content / inventory

- Vocabulary: 1,141 stable headwords.
- Grammar: 50 lessons / 137 exercises. The 17 newest lessons now contain 42 enriched examples with English, Vietnamese and structured breakdowns.
- Listening: 121 units / 239 questions (Parts 1–4).
- Reading: 65 resources / 263 questions (Parts 5–7).
- Separate Part 5 practice: 80 questions; practice-only and independent-review pending.
- Listening reserve: 137 questions pending independent review; 102 are Mock-eligible under the current editorial rules.
- New v2.92/v2.93 Listening and Part 7 questions remain pending independent review and excluded from Mock.

## 3. Automated JavaScript verification

| Check | Result | Detail |
|---|---|---|
| JavaScript regression suites | PASS | 33/33 `.mjs` files executed |
| Voice playback regression | PASS | empty/throwing voice catalogue, immediate queue, selected-voice fallback, stale callback/cancellation race, throwing utterance constructor, 10-second start watchdog, cancel/stop, Part 1 pacing, Listening, Reading and Foundation TTS |
| Robot Buddy | PASS | CTA/action flow, local-only progress insight and offline dialogues |
| Robot Buddy responsive layout | PASS | independent chat scroll, pinned quick prompts/composer/footer, mobile no-auto-zoom rule |
| Score Readiness / Mock | PASS | score-readiness behavior and 200-question Full Mock boundary unchanged |
| Runtime rendering/migration smoke | PASS | Reading/Listening/Grammar render and legacy progress behavior |
| JavaScript syntax | PASS | `sw.js` and every `assets/js/*.js` file |

## 4. Targeted Python verification

**118/118 selected tests PASS across 15 modules.**

| Module | Tests | Result |
|---|---:|---|
| `test_tts_readiness.py` | 14 | PASS |
| `test_question_evidence.py` | 6 | PASS |
| `test_grammar_examples_quality.py` | 4 | PASS |
| `test_responsive_layout.py` | 7 | PASS |
| `test_content_batch_024.py` | 8 | PASS |
| `test_content_batch_025.py` | 7 | PASS |
| `test_legacy_collocation_cleanup.py` | 3 | PASS |
| `test_project_progress.py` | 4 | PASS |
| `test_ci_coverage.py` | 2 | PASS |
| `test_repository_integrity.py` | 1 | PASS |
| `test_sync_version.py` | 12 | PASS |
| `test_design_profile.py` | 6 | PASS |
| `test_grammar_expansion.py` | 7 | PASS |
| `test_learning_content.py` | 34 | PASS |
| `test_pwa_readiness.py` | 3 | PASS |
| **Total** | **118** | **PASS** |

`test_ci_coverage.py` verifies that all 53 Python test modules and all 33 Node regression suites are referenced by the GitHub Actions workflow. This checks workflow registration; it does not mean all 53 Python modules were executed in this session.

## 5. Static/data/repository checks

| Check | Result | Detail |
|---|---|---|
| Repository integrity preflight | PASS | 361 local references/data items inspected; 0 errors / 0 optional warnings |
| Vocabulary validation | PASS | 1,141 records; 0 new ERROR / 0 new WARNING (legacy baseline preserved) |
| Learning-content validation | PASS | Listening 121/239; Reading 65/263; Grammar 50/137; 0 errors / 0 warnings |
| Question evidence audit | PASS | 502 indexed questions exactly once; Listening 239 / Reading 263 |
| Distractor structural audit | PASS | 240 questions in review scope; unique choices and valid answer keys |
| Objective-resource map | PASS | 339/339 links; 11 objectives |
| Learning outcome audit | PASS | 11/11 objectives; 33 criteria; 6/33 evidence paths |
| Foundation A2 audit | PASS | core Reading/Listening 13/13 and 39/39; supplementary Listening 13/13 and 39/39; source evidence 5/5 |
| CMUdict IPA | PASS | 333 source-linked records |
| Part 1 photos | PASS | 9/9 valid JPG assets |
| Version synchronization | PASS | manifest, app, SW, index, README, Master and Changelog all 2.94.0 |
| Design profile | PASS | 54 tokens / 406 legacy font-floor selector groups |
| CSS parsing | PASS | app.css 1,864 top-level nodes / 0 parse errors; design-system.css 270 / 0 errors |
| GitHub Actions YAML | PASS | parsed successfully; all new test scripts registered |
| Python syntax | PASS | `compileall` for `tools/` |
| ZIP | PASS | ZIP CRC/integrity and manifest v2.94.0 are checked after packaging |

## 6. Python full-discovery limitation

A full `python -m unittest discover -s tools/tests -p 'test_*.py' -v` attempt exceeded the local execution time limit (300 seconds) before completion. It is **not** recorded as a full-suite pass. The 118 targeted tests above were executed in the release session. The CI coverage check confirms all 53 Python test modules are wired into the GitHub Actions workflow, where the workflow runs their individual patterns. Remote CI must still be verified after publishing.

## 7. Not verified / acceptance still pending

- Remote GitHub Actions result and GitHub Pages deployment.
- Production service-worker activation/cache update.
- Actual audible TTS output from Windows/macOS/iOS/Android and tablet browsers. Browser/OS voice catalogues and speech synthesis behavior vary; the local tests validate calls, fallback and watchdog handling, not speaker output.
- Mobile/tablet visual acceptance of Buddy no-auto-zoom and manual pinch zoom.
- User visual acceptance of Robot Buddy progress dashboard and device-local data preservation.
- Independent second-person content review and learner validation for pending Listening/Reading/Grammar/vocabulary content.

## 8. Acceptance target

Run `USER_ACCEPTANCE_TEST_v2.94.0.md` after publishing the complete Full Source. The highest-priority user checks are Voice on Listening and Reading, Buddy mobile focus/zoom, Buddy progress dashboard and preservation of existing learning data. Do not start the next release before this one-pass acceptance result is recorded in Master.
