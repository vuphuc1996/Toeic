# Test Report — TOEIC Dictionary v2.62.0

## Scope

Normalize typography and layout across the existing application, fix the Foundation pathway intro layout, make the Objective Learning Tracker / practice-mode / TOEIC mock-test copy readable and consistent, then continue development with Foundation Listening for Pre-A1/A1.

## 1. Typography and interface work

- Added an application-wide typography floor in `assets/css/design-system.css`. Ordinary reading copy in paragraphs, lists, tables and review text is normalized to at least 13.5px; secondary labels/captions use a 12px minimum; controls use a 14px minimum. The mobile bottom navigation is 12px. The larger score/time hierarchy remains distinct.
- Normalized card titles/body/meta in the Objective Learning Tracker, Spaced Recall, Foundation lessons, Practice Mode, Grammar/Reading/Listening cards and the TOEIC mock-test setup/results/review surfaces.
- Removed inherited microtype from the audited mock-test cards, header/timer labels, question controls and result annotations.
- Explicitly fixed `.foundation-intro.panel` to one column; the inner level selector and actions now occupy their own responsive row. The intro body changes to one column on narrow viewports.
- Practice-mode choices use an auto-fit content-width grid. Mock-test cards use three columns on wide screens, two columns on tablet widths and one column on narrow mobile widths. Breakpoints use CSS pixels, not physical device inches.
- Updated `tools/tests/test_design_system.py` and `test_learning_surface_consistency.py` to prevent regressions to microtype, the old two-column intro and squeezed learning cards.

## 2. Foundation Listening development

- Added `data/learning-path/foundation-listening.json` with 10 original short scripts, each mapped one-to-one to an existing Pre-A1/A1 lesson, and 20 comprehension questions (two per lesson).
- Answer-key positions are balanced: A/B/C/D = 5/5/5/5. A dedicated semantic assertion checks the delivery/storage-room item so a rationale and answer choice cannot silently diverge.
- Playback uses the browser/device Speech Synthesis API and current app voice settings. The script/transcript is hidden by default and revealed only when requested. The UI makes clear that this is TTS practice, not authentic ETS audio or an official TOEIC recording.
- Added `assets/js/foundation-listening-evidence.js`. Latest correctness and retry history are stored separately under `toeic:foundation-listening-progress:v1`; unique-question coverage is not inflated by retries.
- Listening evidence is not mixed into the Foundation recognition, contextual application or reading denominators. Existing user progress and IDs are kept intact.
- Added the data/helper to Service Worker REQUIRED and APP_SHELL, with Python, JavaScript and CI regression coverage.

## 3. Local verification

- Focused Python regression tests: **163/163 PASS** across 23 selected test modules: design system (19), learning-surface consistency (5), learning-detail scope (4), remaining-content review (8), version synchronization (12), project progress (3), PWA readiness (3), Foundation Listening (7), Foundation pathway (6), Foundation Reading (5), responsive layout (5), CI coverage (2), learning outcomes (3), objective-resource mapping (2), answer-position balance (4), dashboard layout (6), learning start-level (4), and placement diagnostic (6), Part 1 asset metadata/local-mode (4), learning content (34), Listening expansion (5), Grammar expansion (7), and Reading expansion (9).
- JavaScript regression scripts: **18/18 PASS**.
- JavaScript syntax checks: **PASS** for `sw.js` and all `assets/js/*.js` modules.
- `python tools/sync-version.py --check`: **PASS** across manifest, app release constant, Service Worker, HTML markers, docs README, Master and Changelog.
- `python tools/validate-data.py`: **992 vocabulary records, 0 errors, 0 warnings**; all A–Z counts and manifest totals are consistent.
- `python tools/validate-learning-content.py`: **0 errors, 8 warnings**. All 8 warnings are known missing original Part 1 JPG bytes; SVG fallbacks remain.
- Objective-resource audit: **10/10 objectives, 281/281 resource links PASS**.
- Learning-outcome audit: **30/30 criteria framework PASS**; this is framework coverage, not learner mastery.
- CSS parser: PASS (0 parse errors). CSS regression: 19/19 design-system tests, including the new global typography floor and responsive layout assertions.

## 4. Known blocker and verification boundary

- Strict `python tools/validate-part1-photo-assets.py` result: **1/9 assets available; 8 missing JPG files; FAIL**. These files were already missing in the v2.60.0 input archive; v2.62.0 does not remove or replace them. Keep the CI validator strict and restore the exact licensed source images before deployment. SVG fallbacks remain but do not satisfy the strict asset gate.
- One attempt to run the broader `test_validator.py` module did not complete within the 300-second execution window; the test was interrupted during its long baseline-ID case. It is not counted in the 163 focused tests. No full Python-suite pass is claimed.
- Browser visual QA is not claimed: Chromium in this environment is blocked from opening localhost. Source-level CSS/HTML and responsive regression tests pass, but real visual rendering on iOS/Android/tablet/laptop has not been verified here.
- GitHub Actions, GitHub Pages deployment, installed-PWA updates and physical-device TTS playback have not been run/verified.

## 5. Test steps after the source is deployed

1. Open Dashboard → Theo dõi mục tiêu học tập. Confirm card titles, detail lines and evidence labels are readable without zooming, and cards wrap without clipping.
2. Open Lộ trình học → “Học đúng phần bạn cần”. Confirm the heading is on its own row, the level selector and actions are aligned below it, and lesson cards reflow as the content width narrows.
3. Open Ôn tập → Chọn dạng ôn tập. Confirm title, description and action text have the same scale as the app's other learning cards.
4. Open Thi thử TOEIC. Confirm the test mode cards are balanced (3 / 2 / 1 columns by viewport), copy is readable, and the live timer/header do not overlap at 320px, 390px, tablet and laptop widths.
5. Open a Pre-A1/A1 lesson → “Nghe hiểu đoạn ngắn”. Play the script, answer both questions, reveal/hide transcript, then reload. New listening attempts must remain saved under the separate listening progress key, while older lesson/reading/application progress remains unchanged.
6. Do not clear Safari/site data or delete the installed PWA to force an update; preserve existing personal vocabulary and learner progress.
