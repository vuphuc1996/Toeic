# Test Report — TOEIC Dictionary v2.90.0

## Release scope

1. Add 13 supplementary A2 Foundation Listening clips / 39 questions, one clip per A2 lesson, across 13 audio-task formats.
2. Render each supplementary clip in a collapsed “Nghe hiểu mở rộng” panel with on-device configured SpeechSynthesis, optional transcript and independently scoped progress.
3. Preserve all 23 core Foundation Listening clips / 59 questions and the v2.75.0 A2 q1/q2 canonical baseline.
4. Update project inventory reporting and CI coverage; preserve all learner progress, the existing Listening localStorage key, IndexedDB v1 and TOEIC Mock eligibility.

## Local verification results

| Check | Result | Notes |
|---|---|---|
| JavaScript regression suites | PASS 32/32 | Every `tools/tests/*.mjs` suite was executed |
| Selected Python tests | PASS 104/104 | 17 focused modules; not full-suite discovery |
| Python syntax compilation | PASS | All `tools/**/*.py` files compiled |
| Foundation Listening core + extended | PASS | 13 core A2 clips / 39 questions protected; 13 supplementary clips / 39 questions validated |
| Supplementary Listening registry | PASS | 13 full-object SHA-256 fingerprints match canonical JSON |
| A2 assessment quality audit | PASS | Core Reading 13/13 / 39 questions; core Listening 13/13 / 39 questions; supplementary Listening 13/13 / 39 questions; 5 exact source-evidence pointers |
| Listening answer-position distribution | PASS | Full Foundation bank A/B/C/D = 25/25/24/24 |
| TTS regression | PASS | Device voice selection, inter-speaker pause, stop/cancel and legacy script fallback |
| CI coverage | PASS | New Python regression module is included in workflow; all Python test modules and JS suites are registered |
| `node --check` | PASS | `sw.js` and every `assets/js/*.js` module |
| CSS parse (`tinycss2`) | PASS | `app.css`: 1,824 top-level nodes; `design-system.css`: 270; 0 parse errors |
| Canonical design profile | PASS | 54 tokens / 400 generated legacy font-floor selector groups synchronized |
| `tools/validate-data.py` | PASS | 1,137 vocabulary records; 0 new ERROR / 0 new WARNING (legacy baseline noted) |
| `tools/validate-learning-content.py` | PASS | Listening 107/201, Reading 51/200, Grammar 33/86; 0 errors / 0 warnings |
| Part 1 photo assets | PASS | 9/9 photo records/assets and attribution checked; 0 missing warnings |
| Version synchronization | PASS | App, Service Worker, HTML, README, Master and CHANGELOG agree at v2.90.0 |
| Full archive integrity | PASS | Final ZIP checked and SHA-256 written to companion checksum file |

The 104 Python tests are selected targeted modules across 17 focused areas, not the full Python test discovery suite. The 32 JavaScript suites are the complete `tools/tests/*.mjs` set in this release.

## Preservation and review boundary

- Original 23 core Foundation Listening clips / 59 questions and original A2 q1/q2 content baseline remain unchanged.
- Supplementary IDs use `::listening2`; evidence is stored under `{lessonId}::listening2` inside the existing `toeic:foundation-listening-progress:v1` key. Core evidence remains under the original lesson ID.
- No new localStorage key, IndexedDB schema/store/version migration, progress reset, external API, server upload or automated language grading is introduced.
- Supplementary scripts are browser SpeechSynthesis, not authentic ETS recordings. All 13 clips / 39 questions remain `pending-independent-review`; they are not official A2 evidence, CEFR certification or Mock-eligible content.
- The 99 TOEIC Listening reserve questions and their independent-review gate remain untouched.

## Not verified

- Remote GitHub Actions run, GitHub Pages deployment and production cache behavior.
- Visual rendering in a live browser at 15.6-inch desktop 100% zoom, mobile, iOS/Android and landscape orientations.
- Independent second-person linguistic review and learner validation.
- Full Python test discovery.
