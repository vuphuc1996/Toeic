# Test Report — TOEIC Dictionary v2.60.0

## Feature under test

Vocabulary release integrity and compatibility repair for the observed 979-versus-992 mismatch. Scope includes Service Worker cache keys, runtime manifest validation, Dashboard count semantics, legacy workspace migration and preservation of personal/learning data.

## Passed checks

- JavaScript regression scripts: 17/17 PASS, including new `vocabulary-release-integrity.mjs` plus existing Foundation, Recall Queue, Part 5 timing, explanation rubric, Reading/Listening/Grammar runtime, mock and TTS suites.
- Focused Python tests: 33/33 PASS across `test_sync_version.py` (12), `test_pwa_readiness.py` (3), `test_responsive_layout.py` (5), `test_project_progress.py` (2), `test_foundation_pathway.py` (6) and `test_foundation_reading.py` (5).
- JavaScript syntax: `sw.js` and every `assets/js/*.js` file PASS.
- Vocabulary source integrity: 26 A–Z files, 992 records, 992 unique IDs and headwords; per-letter counts and manifest total agree.
- Release delta: 13 IDs in `manifest.releaseAdditionIds` exactly match the 13 records in `batch-008.json`; the 979→992 legacy repair test restores only those IDs when the full old-snapshot fingerprint matches.
- Runtime guards: release version mismatch, per-letter count mismatch, total count mismatch, duplicate IDs/headwords are rejected before the dictionary is rendered.
- Cache/update guards: manifest and JSON fetches carry `__release`; current SW normalizes that key only inside its versioned cache; registration uses `updateViaCache: 'none'`; controlled clients reload once after controller replacement.
- `tools/validate-data.py`: 992 records, 0 errors, 0 new warnings.
- `tools/validate-learning-content.py`: 0 errors, 8 known warnings for missing original Part 1 JPG bytes in this source snapshot; SVG fallbacks remain.
- Objective resource map: 281/281; learning outcome criteria: 30/30.
- Version synchronization: PASS for manifest, Service Worker, title, sidebar, phase note, footer, README, Master and Changelog.

## Data and compatibility preservation

- Canonical A–Z vocabulary records and stable IDs are byte-for-byte unchanged from v2.59.0; only manifest release metadata/version changed.
- The new migration no longer interprets absence from an old workspace snapshot as an explicit deletion.
- Existing `deletedBaseIds` outside the exact 13-ID 979→992 repair fingerprint are retained.
- Existing personal additions, overrides, override base signatures, learning progress and IndexedDB v1 schema are preserved. No profile reset or store/schema migration.
- Main Dashboard count represents the canonical GitHub base dictionary. Detail text separately reports currently visible words and local hidden/add/edit counts.

## Known limitations

- Full Python test discovery was attempted but exceeded the 240-second execution window during the existing baseline-ID test group. The 33 focused Python tests listed above passed; full discovery is not claimed as green.
- Eight original Listening Part 1 JPG files are not present in this source snapshot; SVG fallback remains.
- A previous `part1-meeting-documents` editorial fingerprint discrepancy remains a known review item; this release does not change that content or its fingerprint.
- Remote GitHub Actions, GitHub Pages deployment, offline browser execution and physical iOS PWA update behavior were not run. The cache/update fix is locally verified, not yet confirmed on the user's device.
