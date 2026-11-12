# Test Report — TOEIC Dictionary v2.22.0

Date: 2026-11-11
Baseline: v2.21.0
Scope: Listening Part 1 photo integration and offline-safe rendering.

## Changes
- Eight Part 1 resources now prefer Pexels JPGs named in `assets/listening/ATTRIBUTION.csv`; SVG fallback paths remain available.
- Runtime caption and visual type now identify the asset as a photograph. Image frame uses 4:3 crop and asynchronous decoding.
- Service Worker version is 2.22.0. JPGs are OPTIONAL cached resources, while SVG fallbacks remain REQUIRED.
- Updated correct spoken statements B/C/D for reception plant, restaurant table setting and photocopier to match the corresponding photos. All answer indexes (0–3), resource IDs, question IDs and choiceIds are unchanged.

## Local checks
- Python compile checks: PASS. Node syntax checks for `assets/js/app.js` and `sw.js`: PASS. `tools/sync-version.py --check`: PASS (all release markers 2.22.0).
- Focused regression tests: 32/32 PASS (28 Learning Content + 4 Question Evidence).
- Editorial evidence audit: 211 questions indexed; Part 1 photo/key category 8; remaining answer-key mapping counts retained. Distractor structural audit: 132 reviewed, 12 historic revisions, PASS.
- Learning validator: 0 errors / 8 warnings; all warnings are exactly the eight JPG byte files absent from this local source snapshot. All eight SVG fallback assets exist.
- JSON parse and dataset integrity: PASS; 8 Part 1 entries still have four statements and one question each.
- Existing SVG fallback files: 8/8 present in local snapshot.
- Photo metadata/path declaration: 8/8 mapped to exact `.jpg` filenames from supplied manifest.
- JavaScript syntax, CSS checks, service-worker cache list checks and focused Part 1 tests are recorded below.
- Actual JPG image bytes were not present in the available local source snapshot. User reports placing the files in the GitHub repository; this could not be independently fetched/read in this session. Therefore pixel-level match, real image dimensions, byte-size and actual offline loading are NOT claimed. The full `validate-data.py` APP_SHELL path check must be rerun after applying this patch beside the eight JPGs; it was not marked PASS here.

## Preservation
- Listening 102 questions; Reading 109; Grammar 25 lessons / 54 exercises.
- 928 vocabulary records and stable IDs untouched.
- Part 1 answers remain A/B/C/D = 0/1/2/3. All `choiceIds`, choices and question IDs retained.
- No IndexedDB schema, personal profile, import/export, reset or migration was touched.

## QA boundary
- Local code references photos at `assets/listening/part1-*.jpg`. Before pushing the patch, confirm these 8 files are present under that exact path in the GitHub repository.
- Since the JPG binaries were not in the local snapshot, `validate-data.py` APP_SHELL resource existence check and true offline photo verification must be rerun against the full repository after merging the patch with the existing assets.
- Remote GitHub Actions, Pages deployment, laptop browser visual QA and physical device QA remain unverified.
