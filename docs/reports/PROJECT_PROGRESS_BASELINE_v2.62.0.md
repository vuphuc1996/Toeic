# Project Progress Baseline — v2.62.0

## Target coverage

| Metric | Result | Progress | Interpretation |
|---|---:|---:|---|
| Canonical GitHub vocabulary | 992/992 | 100% | Current manifest integrity, not editorial approval |
| Vocabulary minimum target | 992/3,000 | 33.1% | Canonical headword quantity only |
| Vocabulary planning ceiling | 992/5,000 | 19.8% | Planning ceiling coverage, not a quality score |
| Objective groups with linked resources | 10/10 | 100% | Availability, not mastery |
| Canonical resource links | 281/281 | 100% | Link coverage |
| Learning-outcome criteria framework | 30/30 | 100% | Criteria defined; learner attainment remains separate |
| TOEIC objective groups with practice evidence | 9/10 | 90% | Instrumentation coverage |
| TOEIC groups with recall scheduling | 9/9 | 100% | Wired groups only |
| TOEIC groups with response-time capture | 9/9 | 100% | Wired groups only |
| TOEIC groups with explanation self-report | 1/9 | 11.1% | Part 5 self-report, not independently graded |
| Foundation recognition bank | 30/30 | 100% | Three stable checks in each of 10 existing lessons |
| Foundation contextual application | 10/10 | 100% | One contextual multiple-choice task per lesson |
| Foundation reading | 10/10 passages; 20/20 questions | 100% | Bank coverage only |
| Foundation Listening | 10/10 scripts; 20/20 questions | 100% | Device TTS practice, not ETS audio |
| Foundation learner recognition/application/reading/listening attainment | Not measured | — | Requires actual learner attempts; no mastery percentage claimed |

## Typography and responsive scope

- Added a common typography floor to the existing stylesheet rather than introducing separate feature styles. Reading copy is normalized to at least 13.5px; supporting labels/captions to at least 12px; controls to at least 14px.
- Explicitly normalized the Objective Learning Tracker, Spaced Recall, Foundation cards, Practice Mode selector, mock-test setup/results/review, shared cards/panels/forms and mobile bottom navigation.
- Fixed the Foundation intro one-column layout and standardized responsive card grids. Layout adapts to available viewport width, with 3-column / 2-column / 1-column mock-test cards across wide / tablet / phone widths.
- Source-level CSS tests pass. Browser pixel-level/physical device QA is not available in this workspace, so visual rendering across actual device/browser combinations remains to be confirmed after deployment.

## Foundation Listening scope

- 10 original short scripts are mapped exactly one-to-one to the current 10 Pre-A1/A1 lesson IDs.
- 20 stable comprehension questions, two per script; answer-position distribution A/B/C/D = 5/5/5/5.
- Playback is generated with browser/device Speech Synthesis using current app voice settings. Transcript is hidden by default and available on request.
- Progress is stored separately in `toeic:foundation-listening-progress:v1`; retry history is retained and repeated attempts do not inflate unique-question coverage.
- No authentic ETS recording, speaking assessment, official CEFR score or learner mastery claim is made.

## Verification status

- Selected Python regression tests: **163/163 PASS** across 23 selected modules.
- JavaScript regression scripts: **18/18 PASS**.
- Part 1 photo metadata/local-mode unit checks: 4/4 PASS; these do not override the separate strict validator result.
- JavaScript syntax: PASS for Service Worker and all application JS modules.
- `tools/sync-version.py --check`: PASS.
- `tools/validate-data.py`: 992 records, 0 errors, 0 warnings.
- `tools/validate-learning-content.py`: 0 errors, 8 known missing-JPG warnings.
- CSS parser: 0 parse errors.
- Objective resource audit: 281/281; outcome criteria: 30/30.
- Full Python discovery is not claimed as passed. One wider validator module exceeded the 300-second execution window before completion.

## Release blocker

`python tools/validate-part1-photo-assets.py` currently returns **FAIL: 1/9 original photo assets present; 8 JPG files missing**. This issue was inherited from the v2.60.0 source archive. The SVG alternatives remain, but GitHub Actions invokes the strict validator; the exact original licensed JPG binaries must be restored before deployment. Do not weaken the strict check or create replacement files that pretend to be the licensed photographs.

## Deployment boundary

This is a local source candidate only. Remote GitHub Actions, GitHub Pages, installed-PWA update behavior, real-device responsive screenshots and physical-device TTS playback have not been verified. No existing user vocabulary, stable learning IDs, IndexedDB schema or previously stored learning-progress key was reset or migrated.
