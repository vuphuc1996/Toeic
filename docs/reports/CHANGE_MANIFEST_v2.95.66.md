# Change Manifest — TOEIC Dictionary v2.95.66

## Baseline

- Exact predecessor: `TOEIC_Dictionary_v2.95.65_FullSource.zip`.
- SHA-256: `a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb`.
- Release version: `2.95.66`.

## Runtime / PWA changes

- Version-key the HTML entry's manifest, stylesheets and application module with `__release=2.95.66`.
- Version-key every local ES-module edge imported by `assets/js/app.js`, and the local mock module dependency.
- Release-key data fetches with `__release` plus `__shell`. Older Service Workers strip `__release` but preserve `__shell`, avoiding aliasing to stale cache keys; the new worker strips both keys only within its own release cache so its canonical precached data remains reusable offline.
- Add an HTML release meta marker and check HTML/JavaScript release agreement before binding app events.
- Guard the `#modalLayer` click listener with optional chaining.
- Keep root navigation on the active worker's cached index while an updated worker is waiting for user approval, preventing mixed release shells.

## CI / validator changes

- Correct Batch 022 and Batch 023 CI contract tests to assert their actual `unittest discover` commands.
- Teach the Service Worker asset validator to check the filesystem path independently of query/fragment cache keys, while preserving the full URL identity in Service Worker validation.
- Add regression tests for release-shell version agreement, required DOM listener targets, query-key cache normalization and missing-file rejection.

## Documentation / audit snapshots

- Synchronize release markers and Master/README/version ledgers.
- Add v2.95.66 test report, Python shard ledger, command log, runtime-fix report and package verification after packaging.
- Include six Markdown and one JSON read-only quality/review snapshots generated from current audit tools. These are review inventories, not editorial approvals and not learning-content edits.

## Data boundary

Only `data/manifest.json` changes under `data/`, and only its `version` value. No vocabulary/Related Glossary content, canonical IDs/headwords/relations, question IDs/choices/answer keys, Mock eligibility, learner IndexedDB data/schema or Robot Buddy privacy boundary changes.
