# Change Manifest — TOEIC Dictionary v2.95.77

Baseline: `candidate` commit `035dd6e2001b3b049407f71acd21f9c33f33e776` (v2.95.76).

- Added source & regression test reports: **5** (`v2.95.77` reports)
- Modified source, manifest, test & doc files: **9**
- Deleted: **0**
- Final packagable source inventory: **1,557** files

## Added paths (`docs/reports/`)
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.77.md`
- `docs/reports/CHANGE_MANIFEST_v2.95.77.md`
- `docs/reports/COMMAND_LOG_INDEX_v2.95.77.md`
- `docs/reports/PACKAGE_VERIFICATION_v2.95.77.md`
- `docs/reports/MIGRATION_COMPATIBILITY_v2.95.77.md`

## Modified paths
- `data/manifest.json` (updated version to `2.95.77` and extended all 8 legacy migration profiles with Batch 028 IDs)
- `tools/tests/vocabulary-release-integrity.mjs` (updated assertions for 1,221-word inventory, Batch 028 additions, and all 8 legacy migration profiles)
- `assets/js/app.js`, `sw.js`, `index.html`, `assets/js/mock-engine.js` (synchronized version markers & cache keys to `2.95.77`)
- `docs/README.md`, `docs/MASTER_STATUS.md`, `docs/CHANGELOG.md`, `docs/versions/CURRENT_VERSION.md` (synchronized release documentation)

## Change boundaries
- All 1,221 canonical vocabulary headwords, senses, and Batch 028 terms remain protected.
- All 831 question/support items, Mock eligibility rules, and IndexedDB v1 schema remain untouched.
- `main` branch remains untouched.
