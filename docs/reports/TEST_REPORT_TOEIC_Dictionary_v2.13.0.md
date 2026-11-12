# Test Report — TOEIC Dictionary v2.13.0

- **Date:** 2026-11-10
- **Baseline:** v2.12.0
- **Release status:** Local release candidate; not committed, pushed or deployed.

## Content totals

| Content | v2.12.0 | v2.13.0 |
|---|---:|---:|
| Vocabulary records | 928 | 928 |
| Listening questions | 102 | 102 |
| Reading questions | 109 | 109 |
| Grammar exercises | 54 | 54 |

Listening: 56 units — P1=8, P2=25, P3=39, P4=30. Reading: 35 resources — P5=30, P6=16, P7=63 (38 single-passage +25 multiple-passage). Grammar: 25 lessons /54 exercises.

## Automated validation

- Vocabulary data validator: **PASS** — 928 records, 0 ERROR, 12 legacy warnings (DF005=3, EX006=1, FD001=8 across 7 records); ID set unchanged, 0 added / 0 missing, no new debt.
- Learning-content validator: **PASS** — 0 ERROR /0 WARNING; checks Part blueprint, resource IDs, choices/answer indexes, Part 3/4 set shapes, multi-speaker conversations, Part 6 blanks, Part 7 multi-documents and explanations.
- Version synchronization: **PASS** — manifest, Service Worker, UI markers, README and Master all v2.13.0.
- Unit tests: **97/97 PASS** across six suites:
  - baseline IDs 13/13 (module run);
  - patch engine 11/11 (module run);
  - version sync 12/12 (each method isolated);
  - data validator 33/33 (each method isolated);
  - learning content 22/22 (module run);
  - dashboard layout 6/6 (module run).
  The full `test_sync_version.py` and `test_validator.py` module runs time out in this Python 3.13 sandbox. Every test method in both suites was run independently and passed. No claim is made that a single monolithic discovery run passed. GitHub Actions is configured for Python 3.12 and runs the suites as individual modules.

## Static and preservation checks

- Python: production tools and test files compile with `py_compile`.
- JavaScript: `node --check` passes for `sw.js` and all `assets/js/*.js` (ES modules checked through `.mjs` copies).
- Workflow YAML parses successfully.
- HTML: 206 IDs, 206 unique, no duplicates.
- PWA: 73 `APP_SHELL` resources, 0 missing paths.
- Documentation: 37 Markdown files; all are under `docs/`; no project Markdown was added to the repository root.
- Vocabulary: all 26 A–Z JSON files are byte-identical to v2.12.0; validator confirms same 928 IDs.
- Static assets: all 36 assets other than the intentionally revised `assets/css/app.css` and `assets/js/app.js` are byte-identical to v2.12.0. The CSS contains the open diagnostics layout and illustration-frame styling; app.js renames the Part 1 rendering variable/class to illustration terminology only.
- No IndexedDB/local-storage schema migration, user-progress key change or Grammar data change.

## Dashboard visual QA boundary

- `test_dashboard_layout.py`: 6/6 PASS for wrapper unboxing, heading hierarchy, separate groups, mobile/tablet breakpoints, card focus and accessible live region.
- A rendered screenshot and interactive browser check could not be completed because the headless browser was blocked by the sandbox (`ERR_BLOCKED_BY_ADMINISTRATOR`). Therefore real Chrome/Safari/iOS/Android visual QA remains pending.

## Packaging and extracted-package recheck

- Final ZIP: `TOEIC_Dictionary_v2.13.0_TOEIC_Editorial_Layout_Refinement.zip` — **146 files**.
- `ZipFile.testzip()` returned no CRC error.
- Extracted into a fresh directory and compared every archived entry byte-for-byte: **146/146 match**, with no extra or missing extracted files.
- On the clean extracted package, data validator, learning-content validator, version sync, Python compile, JavaScript syntax, workflow YAML, 206 unique HTML IDs, 73 APP_SHELL paths (0 missing) and 38 Markdown files under `docs/` were rechecked and passed.
- Package SHA-256 is recorded in the delivery message; no ZIP hash is embedded inside the archive itself.
