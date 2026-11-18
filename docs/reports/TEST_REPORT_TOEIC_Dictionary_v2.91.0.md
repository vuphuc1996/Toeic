# Test Report — TOEIC Dictionary v2.91.0

## Release scope

1. Upgrade all 13 supplementary A2 Foundation Listening dialogues from four turns to six alternating speaker turns, 75–100 words each.
2. Align the 39 questions to a consistent skill progression: detail, purpose/context, inference/next action; add exact source-turn evidence snippets.
3. Preserve stable clip/question IDs, `{lessonId}::listening2` progress scope, the existing localStorage key, IndexedDB v1, core Foundation Listening and TOEIC Mock reserve boundaries.
4. Improve the project progress report, add an overall roadmap assessment and provide a blank second-person review checklist.

## Local verification results

| Check | Result | Notes |
|---|---|---|
| JavaScript regression suites | PASS 32/32 | Every `tools/tests/*.mjs` suite executed |
| Selected Python tests | PASS 114/114 | 17 focused modules; not full-suite discovery |
| Python syntax compilation | PASS | All `tools/**/*.py` files compiled |
| Foundation Listening regression | PASS | 23 core clips / 59 questions unchanged; 13 supplementary clips / 39 questions validated |
| Supplementary dialogue quality contract | PASS | Each has 6 turns, 75–100 words, 3 female + 3 male turns, 3 skill-distinct questions and exact evidence snippets |
| Supplementary Listening SHA-256 registry | PASS | 13 complete clip object fingerprints match canonical JSON; review status remains pending |
| A2 assessment quality audit | PASS | Core Reading 13/13 / 39 questions; core Listening 13/13 / 39 questions; supplementary Listening 13/13 / 39 questions; five core source-evidence pointers registered |
| Listening answer-position distribution | PASS | Full Foundation bank A/B/C/D = 25/25/24/24 |
| TTS regression | PASS | All 32 JS suites pass, including shared TTS regression coverage for voice selection, pauses, stop/cancel and legacy fallback |
| CI coverage | PASS | New/updated Python tests and JS regression suites remain registered in workflow |
| `node --check` | PASS | `sw.js` and every `assets/js/*.js` module |
| CSS parse (`tinycss2`) | PASS | `app.css`: 1,824 top-level nodes; `design-system.css`: 270; 0 parse errors |
| Canonical design profile | PASS | 54 tokens / 400 generated legacy font-floor selector groups synchronized |
| `tools/validate-data.py` | PASS | 1,137 vocabulary records; 0 new ERROR / 0 new WARNING (legacy baseline noted) |
| `tools/validate-learning-content.py` | PASS | Listening 107/201, Reading 51/200, Grammar 33/86; 0 errors / 0 warnings |
| Part 1 photo assets | PASS | 9/9 photo records/assets and attribution checked; 0 missing warnings |
| Version synchronization | PASS | App, Service Worker, HTML, README, Master and CHANGELOG agree at v2.91.0 |
| Progress and roadmap documentation | PASS | Snapshot generated from canonical inventory; roadmap report distinguishes quantity, quality, independent review and deployment acceptance |
| Full archive integrity | PASS | ZIP integrity checked; SHA-256 written to companion checksum file |

The 114 Python tests are selected targeted modules across 17 focused areas, not the full Python test discovery suite. The 32 JavaScript suites are the complete `tools/tests/*.mjs` set in this release.

## Preservation and review boundary

- Original 23 core Foundation Listening clips / 59 questions and original A2 q1/q2 canonical baseline remain unchanged.
- Supplementary clip IDs remain `{lessonId}::listening2`; question IDs are unchanged. Evidence continues under `{lessonId}::listening2` inside the existing `toeic:foundation-listening-progress:v1` key.
- No new localStorage key, IndexedDB schema/store/version migration, progress reset, external API, server upload or automated language grading is introduced.
- Supplementary scripts are browser SpeechSynthesis, not authentic ETS recordings. All 13 clips / 39 questions remain `pending-independent-review`; they are optional practice, not official A2 evidence, CEFR certification or Mock-eligible content.
- The 99 TOEIC Listening reserve questions and their independent-review gate remain untouched.
- `PROJECT_ROADMAP_STATUS_v2.91.0.md` gives current coverage and backlog. It intentionally does not invent a global project-completion percentage.
- `FOUNDATION_A2_LISTENING_REVIEW_CHECKLIST_v2.91.0.md` is a blank handoff for an independent reviewer; no second-person approval is claimed.

## Not verified

- Remote GitHub Actions run, GitHub Pages deployment and production cache behavior.
- Visual rendering in a live browser at 15.6-inch desktop 100% zoom, mobile, iOS/Android and landscape orientations.
- Actual device TTS voice quality and six-turn pause perception on the user's devices.
- Independent second-person linguistic review and learner validation.
- Full Python test discovery.
