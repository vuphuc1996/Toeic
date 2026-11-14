# Test Report — TOEIC Dictionary v2.38.0

**Release:** TOEIC Part 5 Sentence Completion Practice  
**Base:** v2.37.0  
**State:** local release candidate; not a remote deployment/acceptance statement.

## Focused regression results

| Suite / check | Result | Scope |
|---|---:|---|
| `test_sentence_completion.py` | 8/8 PASS | Metadata, pending review status, IDs, canonical word links, one blank, four unique options, key/explanation, topics and targeted item revisions |
| `test_pwa_readiness.py` | 3/3 PASS | Service Worker cache version, required/app-shell assets, Part 1 fallback rules |
| `test_ci_coverage.py` | 2/2 PASS | Every Python regression module and JavaScript suite is declared in CI workflow |
| `sentence-completion.mjs` | PASS | Bank validation, four choices, shuffle/explanation alignment, question-ID cycling and separation from word-ID history |
| `learning-focus-workspace.mjs` | PASS | Mode tile, unique DOM IDs, shared Focus Workspace, separate saved Part 5 history, IndexedDB v1 and existing retry/history rules |
| `practice-progress.mjs` | PASS | Per-question retry, full-set retry, attempt history, latest-result analytics and legacy v1 compatibility |
| `runtime-render-smoke.mjs` | PASS | Existing Reading/Listening/Grammar render, retry/history and stable choice-ID paths |
| JS syntax checks | PASS | `sw.js`, `assets/js/sentence-completion.js`, `assets/js/app.js` (module syntax) |
| Python compile | PASS | validator and changed Python test modules |

Python regression total: **13/13 tests** across three focused suites. JavaScript regression total: **4 suites passed**.

## Data/content validators

- `python tools/validate-data.py`: 992 canonical vocabulary records; 0 errors, 0 warnings. The validator notes only the legacy baseline condition; no new ID debt was detected.
- `python tools/validate-learning-content.py`: 0 errors, 8 warnings. All 35 Sentence Completion questions pass schema/reference validation and remain practice-only/pending independent review. The eight warnings are existing missing Part 1 JPG binaries in this supplied source snapshot; SVG fallbacks remain available. The original user-owned JPGs must be preserved in the actual repository.
- `python tools/audit-toeic-coverage.py`: generated current coverage including the separate 35-question Sentence Completion bank. This bank is explicitly excluded from Reading Mock counts.
- `python tools/sync-version.py --set 2.38.0 --dry-run`: all registered markers structurally found; changes are limited to registered version markers. Apply/check is recorded after final documentation update.

## Scope boundaries

- No real browser session, mobile/desktop physical device, GitHub Actions execution or GitHub Pages deployment is verified in this workspace.
- No actual offline/reconnect test was performed. PWA readiness is a static source/resource check.
- No independent second-person editorial review was performed. The 35 questions remain reserve-pending-independent-review and are not eligible for Mock.
- No IndexedDB schema migration or learner-profile reset/import/export/inspection was performed.
