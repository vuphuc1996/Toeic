# Change Manifest — v2.95.63

## Source baseline

- Sole baseline: `TOEIC_Dictionary_v2.95.62_FullSource.zip`
- Baseline SHA-256: `b9d56cd27d0d13c4c8781732ac72c17b526b2aa451fa1393c39fd30820260f96`
- Uploaded v2.95.60 and all older/intermediate sources were not used.

## Implementation files

| File | Change |
|---|---|
| `.github/workflows/validate-data.yml` | Batch 035 unittest glob broadened; modal dismissal regression script registered |
| `assets/js/app.js` | Safe modal reset/close dispatcher, pending-result confirmation serialization, explicit dismiss paths for review and auto-next wait, visible close controls and focus management |
| `tools/tests/test_ci_coverage.py` | unittest glob semantics; Cambridge split-module selection regression |
| `tools/tests/modal-dismissal-workflow.mjs` | New state-machine regression for completion stats and X/Escape safe dismiss/commit routes |
| `data/manifest.json` | Release version only: 2.95.62 → 2.95.63 |
| `index.html`, `sw.js` | Version marker/cache version synchronization only |

## Documentation files

- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/versions/CURRENT_VERSION.md`
- `docs/versions/PREVIOUS_VERSION.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.63.md`
- `docs/reports/COMMAND_LOG_INDEX_v2.95.63.md`
- `docs/reports/CHANGE_MANIFEST_v2.95.63.md`
- `docs/reports/PACKAGE_VERIFICATION_v2.95.63.md`

## Explicit no-change boundaries

- No canonical vocabulary JSON or IDs, headwords, senses, relations, translations or pronunciation content changed.
- No Related Glossary row, term, meaning, relation or provenance content changed.
- No question IDs, choice IDs/order, answer keys, explanations, reserved/Mock eligibility or learning content changed.
- No learner IndexedDB database/store/schema or saved learner record was read for mutation, migrated, cleared or overwritten.
- No CSS/layout redesign, navigation redesign, Cloudflare, API or backend addition.

A baseline-to-release hash comparison confirms `data/manifest.json` is the only changed file under `data/`; all other data files are byte-identical.
