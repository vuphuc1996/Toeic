# Test Report — TOEIC Dictionary v2.95.60

Date: 2026-11-24

## Source of truth

- Exact predecessor: `TOEIC_Dictionary_v2.95.59_FullSource.zip`
- SHA-256: `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`
- The archive contained 703 files; its extracted tree contained 703 files before development. No older source or alternate branch was used.

## Implementation scope

- Read-only missing US IPA review queue: 79 records (5 single-variant candidates, 49 multiple-variant review cases, 25 no exact CMUdict key).
- CMUdict package version recorded as 1.1.3. ARPABET variants retained; no automatic IPA conversion or canonical data mutation.
- Related Glossary audit: 567 entries; 198 flagged (194 high, 2 medium, 2 low); 131 missing definitions; 63 placeholders; 190 missing POS; 65 missing provenance; 0 duplicate normalized groups.
- Related glossary reference coverage audit: 804 distinct relation targets; 248 distinct terms / 249 reference occurrences remain uncovered; no candidate auto-imported.
- Item complexity inventory regenerated: 582 questions; 106 with one or more structural review signals; 280 reserve-pending (193 Listening, 87 Reading) remain excluded from Mock.

## Commands and results

| Command / check | Result |
|---|---|
| `python tools/sync-version.py --check` | PASS — all 14 version markers synchronized |
| `python tools/validate-data.py` | PASS — 1,141 records; 0 ERROR / 0 WARNING; 0 IDs added/removed; 79 missing US IPA |
| `python tools/validate-learning-content.py` | PASS — Listening 295, Reading 287, Grammar 58 lessons / 169 exercises; 0 errors / 0 warnings |
| `python tools/audit-item-complexity.py` | PASS — 582 indexed; 0 invalid answer-index errors |
| Focused Python tests (IPA, renderer, glossary audits/queues, complexity) | PASS — 37/37 |
| CI coverage regression | PASS — 3/3 after adding the new renderer test to the workflow |
| All `tools/tests/*.mjs` scripts | PASS — 42/42 |
| `node --check sw.js` and all `assets/js/*.js` syntax checks | PASS |
| Python compile for changed audit/render/test modules | PASS |
| Full Python sharded discovery | INCOMPLETE — 17/94 modules terminal PASS; 126/126 cases in those modules passed; 77 modules NOT RUN when the outer execution window ended. No full-suite PASS is claimed. |

The first sharded attempt exposed a CI coverage gap for the newly added renderer test. The workflow was corrected to explicitly invoke it; the CI coverage test then passed 3/3. The later full-suite attempt reached 17 modules and stopped at the outer execution limit. This is an incomplete run, not a test failure in the completed modules and not a full-suite pass.

## Preservation checks

- All A–Z canonical vocabulary JSON files: byte-identical to v2.95.59.
- `data/related-terms.json`: byte-identical.
- Listening and Reading question libraries: byte-identical.
- IndexedDB contract, learner data, question IDs, choices, answer keys, Mock eligibility and UI layout: unchanged.
- Reserve questions remain excluded.

## External acceptance

Hosted GitHub Actions, GitHub Pages deployment, installed-PWA cache propagation/offline behavior and physical device/browser acceptance are UNVERIFIED.
