# Test Report — TOEIC Dictionary v2.67.0

Date: 2026-11-15  
Scope: local source, canonical data, JPG-only Listening Part 1 contract and vocabulary Batch 009

## Passing checks

| Check | Result |
|---|---:|
| Learning content Python tests | 34/34 PASS |
| PWA readiness Python tests | 3/3 PASS |
| Part 1 photo-contract Python tests | 5/5 PASS |
| Vocabulary family-link Python tests | 5/5 PASS |
| Vocabulary details/examples Python tests | 11/11 PASS |
| Legacy collocation Python tests | 3/3 PASS |
| Project progress Python tests | 4/4 PASS |
| CI coverage Python tests | 2/2 PASS |
| Version-sync Python tests | 12/12 PASS |
| Design profile Python tests | 6/6 PASS |
| Design system Python tests | 19/19 PASS |
| Responsive layout Python tests | 5/5 PASS |
| Visual composition Python tests | 8/8 PASS |
| **Selected Python test total** | **117/117 PASS** |
| JavaScript regression suites | 21/21 PASS |
| Vocabulary release-integrity Node test | PASS |
| Learning Focus Workspace Node test including Batch 009 | PASS |
| Python tool/test compilation | PASS |
| `python tools/validate-data.py` | 1,026 records; 0 errors; 0 warnings |
| `python tools/validate-learning-content.py` | 0 errors; 8 missing-original-JPG warnings |
| `python tools/sync-version.py --check` | PASS |
| `python tools/sync-design-profile.py --check` | PASS (54 tokens; 361 legacy font-floor selector groups) |
| Node syntax: `assets/js/app.js`, `sw.js` | PASS |
| Coverage audit | 1,026 vocabulary; Listening 107 units/201 questions; Reading 51 resources/200 questions |
| Distractor structural audit | PASS for 177 questions in scope; 72 reserve structural checks; 12 revisions flagged for review |

## JPG-only contract verification

- All nine Part 1 records reference `.jpg` under `photo` and contain no `image` fallback property.
- No `assets/listening/part1-*.svg` files remain.
- No Part 1 SVG path is present in the Service Worker or the active Listening/Mock fallback renderer.
- The redundant reserve-status UI text is absent from `assets/js/app.js`; its underlying editorial status metadata remains present and Mock eligibility remains fail-closed.
- `python tools/validate-part1-photo-assets.py --allow-missing` reports 1/9 local JPG binaries present and 8 warnings.

## Release blocker / unverified work

- Eight original repository-owned JPG binaries are missing from this workspace archive. The strict photo validator must fail until those exact JPG files are restored from the GitHub repository. Do not substitute generated photos, reintroduce SVGs or disable the validator.
- Remote GitHub Actions, Pages deployment, real browser rendering, offline cache behavior and device audio have not been verified.
- Batch 009 has completed an internal author pass only. Independent lexical review is pending; CEFR values remain editorial estimates.
- The 79 Python tests are selected module tests, not proof that full Python discovery has passed. Broad/slow suites should remain separately reported if they are not run.

## Data preservation

- Canonical headwords: 992 → 1,026; +34 new stable IDs.
- Existing vocabulary IDs remain; no existing term, sense order or saved learner progress is removed.
- Legacy migration repair profiles cover exact 979- and 992-word historical snapshots without un-hiding unrelated user-hidden entries.
- No IndexedDB schema/version/store migration or learner progress reset.
- Listening question IDs, choice IDs, answer keys and attribution rows are unchanged.
