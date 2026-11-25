# Command log index — v2.95.55

Date: 2026-11-24. Runtime: Python 3.13.5, Node v22.16.0.

- `Node_Regression.log`: all JavaScript syntax checks and 42 `.mjs` runtime regression scripts PASS.
- `Full_Unittest_Discover.log`: complete Python discovery from the source workspace, 711 executed; 710 PASS, 1 accepted Git-metadata SKIP, 0 FAIL, 0 ERROR; 143.055 seconds.
- `CleanArchive_Unittest.log`: same complete discovery rerun from the extracted final FullSource ZIP; 711 executed; 710 PASS, 1 accepted Git-metadata SKIP, 0 FAIL, 0 ERROR; 135.452 seconds.
- `Data_Validator.log`: 1,141 vocabulary records, 0 ID additions/removals, 0 ERROR / 0 WARNING.
- `Version_Sync.log`: every registered version marker and `docs/CHANGELOG.md` synchronized to 2.95.55.
- Focused scripts also executed after final Service Worker precache edit: `learner-data-backup.mjs`, `learner-data-backup-integration.mjs`, `service-worker-update.mjs` — all PASS.

The first full Python run hit the tool's time limit before completing and is not treated as a result. The successful retry log is the authoritative full-suite evidence.
