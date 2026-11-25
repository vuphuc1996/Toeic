# Test report — TOEIC Dictionary v2.95.55

Date: 2026-11-24

## Environment

- Python 3.13.5
- Node.js v22.16.0
- Source base: exact v2.95.54 FullSource SHA-256 `05912f844fb0cd6a9997cd99964ef4ef887325fdb7d7520445994ded625f28ce`

## Results

| Check | Result |
|---|---:|
| JavaScript syntax (`assets/js/*.js`, `sw.js`) | PASS |
| JavaScript runtime regression scripts | 42/42 PASS |
| Python unittest discovery | 711 executed: 710 PASS, 1 accepted SKIP, 0 FAIL, 0 ERROR |
| Data validator | 1,141 records; 0 ID additions/removals; 0 ERROR / 0 WARNING |
| Version sync | All registered markers + changelog PASS at 2.95.55 |
| Learner backup focused runtime tests | PASS |
| Learner backup integration test | PASS |
| Service Worker lifecycle regression | PASS |

The single Python skip is the existing repository `.gitignore` assertion, which requires Git metadata and is intentionally skipped for a source-only archive. The full suite completed in 143.055 seconds from the source workspace and was independently rerun from the exact extracted final FullSource archive: 135.452 seconds, same 711/710 PASS/1 SKIP result. An earlier invocation was terminated by the command time limit before completion; it is not counted.

## Data and compatibility invariants

- Vocabulary ID set remains 1,141; no additions or removals.
- IndexedDB remains `toeic-vocabulary-phase1`, version 1, object store `workspace`.
- Existing vocabulary-only JSON/CSV export/import remains available and separate.
- No vocabulary/question content, question IDs, choices, answer keys, Mock eligibility, learner history, or Robot Buddy access rules were modified.
- New backup module is included in both required and app-shell Service Worker precache lists.

## Not verified

Remote GitHub Actions, GitHub Pages deployment, browser storage-persistence grant, actual iOS/iPadOS/Android file picker and download behavior, offline update propagation on physical devices, and crash-level storage rollback.
