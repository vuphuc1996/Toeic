# Test Report — TOEIC Dictionary v2.61.0

## Scope

Correct the two reported validation failures, normalize the Spaced Recall and Foundation learning-path interfaces to the shared design system, and continue release-level integrity checks.

## Verified findings and fixes

### 1. `test_learning_detail_scope`

- Reproduced the false positive: the old helper sliced `openGrammarLesson()` through the hard-coded `answerGrammarExercise()` declaration, unintentionally including `renderRecallQueue()` and other inserted helpers.
- Confirmed the body of `openGrammarLesson()` did not contain an out-of-scope `item.` reference.
- Replaced the hard-coded endpoint with the next top-level function declaration; added a regression guard showing the Recall Queue callback's `item` remains valid in its own function.
- The updated test still searches the entire isolated grammar renderer for an actual `item.` reference.

### 2. `test_remaining_content_review`

- Reproduced the fingerprint failure and inspected all eight reviewed Listening Part 1 units. For each unit, the old `unitContentSha256` exactly matched the current metadata payload after removing only `photoSourceType: "licensed-stock"`.
- All eight `questionSha256` values matched the existing questions byte-for-byte under the canonical JSON digest. No transcript, translation, title, answer, choices or question order was changed.
- Refreshed the eight unit fingerprints and recorded old/new digests, the field/value, scope, date and per-unit verification flags in `fingerprintRefreshLog`.
- Added `tools/refresh-photo-source-fingerprints.py`. It is fail-closed: it refuses to write unless the exact eight IDs are present, old hashes match with only the new metadata field removed, the expected value is present and all question hashes still match.

## Interface changes

- Spaced Recall now uses the common `.panel`, `.panel-header`, `.learning-card`, `.library-count` and `.secondary-button` patterns. Human-readable card copy no longer prints the internal stable question ID; the action still carries that ID to open the precise question. Opening the queue remains read-only.
- Foundation overview now uses the standard page heading, panel/header, learning-card grid, category/level markers and common controls. Type sizes use fluid `clamp()` values with readable minimums. The progress meter exposes `role="progressbar"` and updates `aria-valuenow`.
- Both areas use content-based `auto-fit` grids and CSS-pixel breakpoints, not device-inch assumptions. The app's existing shared design-system stylesheet remains authoritative for font, touch-target and focus states.

## Local verification

- Focused Python regression tests: **41/41 PASS** across `test_learning_detail_scope`, `test_remaining_content_review`, `test_learning_surface_consistency`, `test_responsive_layout`, `test_design_system` and `test_learning_start_level`.
- Both original failing suites now pass: **12/12 tests** across the two files. The Foundation, dashboard, project-progress and PWA groups add **22/22 PASS**; learning-outcome, question-evidence, choice-history and choice-identity groups add **25/25 PASS**; baseline-ID integrity adds **13/13 PASS**; safe data-patching tests add **11/11 PASS**; answer-position balance adds **4/4 PASS**.
- Selected Python regressions run individually: **130/130 PASS** across the first selected groups; the Part 1 asset metadata/local-mode module adds 4/4, for **134/134 selected Python tests PASS** overall. This is not a full Python-suite result. Full discovery was attempted but exceeded the 300-second execution window; no full-suite pass is claimed.
- `test_sync_version.py`: **12/12 PASS**; `test_ci_coverage.py`: **2/2 PASS**; `test_part1_photo_assets.py`: **4/4 PASS** (metadata and explicit local-mode behavior).
- JavaScript syntax checks: **PASS** for `sw.js` and all `assets/js/*.js`; JavaScript regression scripts: **17/17 PASS**.
- Data validation: **992 records, 0 errors, 0 warnings**.
- Learning-content validation: **0 errors, 8 warnings** because eight original Part 1 JPG files are absent from this source snapshot; SVG fallbacks are present.
- Objective resource map: **281/281 PASS**; outcome criteria: **30/30 PASS**.
- Version synchronization: **PASS** for the manifest, app, Service Worker, HTML markers, README, Master and Changelog.

## Known release blocker — inherited Part 1 image binaries

- Strict `python tools/validate-part1-photo-assets.py` currently **FAILS**: 8 licensed-stock JPG files are missing from this source archive; only `part1-office-cleaning.jpg` is present. This condition is also present in the v2.60.0 input ZIP, so it was not introduced by v2.61.0.
- The corresponding eight SVG fallbacks are present, and the metadata/attribution tests pass. However, `.github/workflows/validate-data.yml` invokes the strict validator without `--allow-missing`, so this gate is expected to fail in GitHub Actions until the exact source JPGs are restored.
- The official Pexels pages and direct download URLs are catalogued in `docs/reports/PART1_PHOTO_ASSET_RECOVERY_v2.61.0.md`. The container could not resolve `images.pexels.com`, so the binaries could not be fetched into this package. No generated substitute was made.
- **Deployment hold:** do not treat this candidate as GitHub Actions / Pages ready until the strict validator reports 9/9 valid image files.

## Additional test execution boundary

- `test_learning_start_level.py`: **4/4 PASS** after updating its old wording assertion to the current “chưa được phát hành” empty-state copy; higher-level selection still filters out lower stages without changing the canonical dictionary.
- The initial direct package-style invocation of `test_answer_position_balance` could not import its helper module; rerunning through the repository's supported discovery path passed **4/4**.
- Chromium in this environment is policy-blocked from opening localhost. No real browser screenshot or pixel-level visual QA is claimed; the interface evidence is source-level HTML/CSS and automated responsive/layout assertions.

## Preservation and release boundary

- No canonical vocabulary records, stable learning question IDs, answer keys, question order, personal data, localStorage keys, IndexedDB stores/schema or learner-progress records were reset or migrated.
- Release candidate is **v2.61.0 local source only**. GitHub Actions, GitHub Pages deployment, offline PWA behavior, and physical iOS/Android layout have not been verified from this workspace.

## Test instructions after deployment

1. Open the Dashboard and inspect the Spaced Recall section. Confirm the count and cards follow the same panel/card style as the rest of the app; each “Mở ôn tập” action opens the exact due question. With no due questions, confirm a readable empty state appears.
2. Open **Lộ trình học**. Confirm the heading, progress panel, selector, lesson cards and action buttons match the system style. Resize the browser across narrow mobile width, tablet, and laptop/desktop widths; cards should wrap without horizontal overflow and text should remain readable.
3. Run the existing recall and Foundation checks after testing one due question and one Foundation lesson. Progress must remain saved after reload.
4. Do not clear Safari/site data or delete the installed PWA to force an update; preserve local progress.
