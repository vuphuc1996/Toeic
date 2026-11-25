# Change Manifest — TOEIC Dictionary v2.95.66 candidate

## Source baseline

- Exact predecessor: TOEIC_Dictionary_v2.95.65_FullSource.zip
- Baseline SHA-256: a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb
- Baseline inventory: 779 files
- Candidate branch: fix/v2.95.66-pwa-release-coherence-ci-batch022
- Base commit: bfb28d63669508dc8fd766802c1203f6a2e86087

## Defects addressed

1. A v2.95.64 cached app.js could be returned alongside a v2.95.65 HTML shell. The stale source still attempted to register a click listener on #modalBackdrop, causing Cannot read properties of null (reading 'addEventListener') at the reported line and column.
2. Batch 022's CI contract asserted that the workflow contained a literal source path, although the workflow invokes the test with python -m unittest discover.
3. PWA readiness checked a file-system path including a cache-busting query string, which would incorrectly flag the new versioned shell URLs as missing.

## Changes

- Bump manifest, app, Service Worker and visible release markers to v2.95.66.
- Version the HTML references to app.css, design-system.css and app.js with ?v=2.95.66.
- Put the same versioned asset URLs in Service Worker REQUIRED and APP_SHELL.
- Register the Service Worker using a release-specific __release query and retain updateViaCache: 'none'.
- Check the HTML release meta against APP_RELEASE_VERSION before bindEvents(); show an explicit recovery message and skip initialization when the shell/module pair is mismatched.
- Change Batch 022's CI assertion to test the actual unittest discover selector, using glob semantics.
- Normalize query strings out of local file existence checks in the PWA readiness test.
- Add tools/tests/release-asset-coherence.mjs and register it in GitHub Actions.
- Update Master Status, Master Development Prompt, CURRENT/PREVIOUS version ledger, README, CHANGELOG and manual PWA acceptance checklist.

## Preservation

No vocabulary/Related Glossary content, canonical word IDs/headwords/relations, question/choice IDs, answer keys, Mock eligibility, learner IndexedDB records/schema, Robot Buddy privacy boundary or UI layout is intentionally changed.

## Acceptance status

- Source changes: committed to the candidate branch.
- GitHub Actions PR validation: PENDING.
- Full Python discovery: PENDING.
- Node regression suite: PENDING.
- ZIP/patch generation, checksum verification and exact replay: PENDING.
- GitHub Pages deploy and real installed-PWA/device cache acceptance: PENDING.
