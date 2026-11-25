# Test Report — TOEIC Dictionary v2.95.66 candidate

## Current status

HOSTED ACTIONS PASS — PACKAGE / DEVICE ACCEPTANCE PENDING

This candidate has source changes on fix/v2.95.66-pwa-release-coherence-ci-batch022. The PR workflow completed successfully on commit `9fdfc39` in GitHub Actions run `45589650195`: 130/130 steps succeeded, 0 failed and 0 skipped. All 762 discovered Python tests passed in 13.230s. This report keeps source packaging and real-device PWA acceptance separate from hosted CI.

## Defect evidence and correction

- The user supplied browser output showed v2.95.65 HTML, modalLayer: true, legacyModalBackdrop: false, and app.js loaded from the GitHub Pages path.
- Repository history confirms that the exact stale $('#modalBackdrop').addEventListener(...) call at line 2135 / around column 170 is in app.js v2.95.64. The v2.95.65 source uses #modalLayer.
- The v2.95.65 Service Worker used cache-first lookup for same-origin non-data assets. As the HTML script URL did not carry a release query, an older worker could return its cached v2.95.64 app.js while navigation delivered the newer HTML shell. The app then attempted to bind a listener to a DOM element that no longer existed.
- v2.95.66 adds release-query URLs for app.js/CSS, precaches those exact URLs, keeps the Service Worker script URL stable with updateViaCache: none, and adds an HTML/app release guard before event binding.

## Added / changed regression coverage

- Batch 022 now validates the actual unittest discover -p 'test_related_glossary_batch_022.py' selector.
- PWA readiness resolves local files from URL paths, ignoring release query strings.
- release-asset-coherence.mjs checks manifest/HTML/app/SW release agreement, versioned shell URLs, old-cache-key isolation and startup mismatch handling.
- The new Node test is registered in the Actions JavaScript regression group.

## Execution results

| Test group | Result |
|---|---|
| GitHub Actions workflow steps | 130/130 PASS; 0 FAIL; 0 SKIP |
| Full Python unittest discovery | 762/762 PASS (13.230s) |
| Node regression scripts | 44/44 PASS |
| JavaScript syntax (`sw.js` and `assets/js/*.js`) | PASS |
| Release asset coherence | PASS |
| Service Worker update lifecycle | PASS |
| Design System | 19/19 PASS |
| PWA readiness | PASS |
| Version synchronization | 13/13 markers PASS |
| Vocabulary data validator | 1,141 records; 0 errors; 0 new warnings; 0 IDs added/removed |
| Learning-content validator | 0 errors; 0 warnings |
| Part 1 photo assets | 9/9 PASS |
| Repository integrity and commit-readiness preflight | PASS |
| CSS design-token ratchet and canonical design profile | PASS |
|---|---|
| Batch 022 | PASS |
| PWA readiness | PASS |
| CI coverage | PASS |
| Release asset coherence | PASS |
| Service Worker update lifecycle | PASS |
| All Node regressions | 44/44 PASS |
| Full Python discovery | 762/762 PASS |
| Data validator | PASS — 1,141 records, 0 errors, 0 new warnings |
| Learning-content validator | PASS — 0 errors / 0 warnings |
| Version sync | PASS — 13/13 markers |
| Git commit-readiness | PASS — GitHub preflight |

## External acceptance

- GitHub PR Actions: PASS — 130/130 steps, 0 failures, 0 skipped.
- GitHub Pages deployment: PENDING.
- Existing installed PWA update from a v2.95.65 worker/cache: PENDING.
- Offline reload after successful update: PENDING.
- iOS/iPadOS/Android/desktop acceptance: PENDING.

A test suite that is skipped because an earlier step failed must remain marked PENDING, not PASS.
