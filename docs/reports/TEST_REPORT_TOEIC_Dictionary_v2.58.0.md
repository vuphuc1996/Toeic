# Test Report — TOEIC Dictionary v2.58.0

## Scope

Added one stable contextual-application multiple-choice task to each of 10 existing Pre-A1/A1 lessons. Added a separate application-evidence ledger and UI feedback. Existing recognition evidence remains unchanged.

## Results

- JavaScript regression scripts: 15/15 PASS.
- Focused Python regression tests: 36/36 PASS (Foundation pathway, learning start-level, placement diagnostic, PWA readiness, responsive layout, version synchronization).
- `node --check assets/js/app.js`: PASS.
- `node --check assets/js/foundation-evidence.js`: PASS.
- `python tools/validate-data.py`: 992 records, 0 errors, 0 warnings relative to legacy baseline.
- `python tools/validate-learning-content.py`: 0 errors, 8 warnings; eight Part 1 JPG binaries are absent from this source snapshot; SVG fallbacks remain available.
- `python tools/audit-objective-resources.py`: PASS, 10 objectives and 281/281 resource records.
- `python tools/audit-learning-outcomes.py`: PASS, 10/10 objectives and 30 measurable criteria.
- `python tools/sync-version.py --check`: PASS, all registered markers at v2.58.0.
- Foundation application integrity: 10/10 stable IDs, four choices per task, valid answer key/rationale/focus.
- Evidence isolation: application attempts do not alter recognition unique-question denominator; retry history and latest-result scoring verified.

## Compatibility

- Retained all 10 lesson IDs and 30 recognition question IDs.
- Retained `toeic:foundation-progress:v1` and legacy fields.
- Added `applicationEvidence` alongside the existing per-lesson evidence; no IndexedDB schema change.
- No personal learner profile was imported, migrated or reset.

## Known limitations

- Application items are contextual MCQs, not open-ended production or spontaneous communication. Listening and speaking are not measured.
- Full test discovery was not run; the focused 36-test suite passed.
- GitHub Actions, GitHub Pages deployment, and physical-device QA were not performed.
- Eight missing JPG warnings remain; SVG fallbacks exist.
