# Test Report — TOEIC Dictionary v2.95.66 candidate

## Current status

PENDING HOSTED VALIDATION

This candidate has source changes on fix/v2.95.66-pwa-release-coherence-ci-batch022. The PR workflow has not yet completed. This report intentionally does not claim a local or hosted PASS for commands that have not been executed against the candidate tree.

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
| Batch 022 | PENDING |
| PWA readiness | PENDING |
| CI coverage | PENDING |
| Release asset coherence | PENDING |
| Service Worker update lifecycle | PENDING |
| All Node regressions | PENDING |
| Full Python discovery | PENDING |
| Data validator | PENDING |
| Learning-content validator | PENDING |
| Version sync | PENDING |
| Git commit-readiness | PENDING |

## External acceptance

- GitHub PR Actions: PENDING.
- GitHub Pages deployment: PENDING.
- Existing installed PWA update from a v2.95.65 worker/cache: PENDING.
- Offline reload after successful update: PENDING.
- iOS/iPadOS/Android/desktop acceptance: PENDING.

A test suite that is skipped because an earlier step failed must remain marked PENDING, not PASS.
