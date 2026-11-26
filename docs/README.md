# TOEIC Dictionary v2.95.70 — Project Documentation

This documentation describes the current locally verified source candidate. It does not imply that the candidate has been pushed or deployed.

- Current release: `2.95.70`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.70.md`.
- Python inventory: `reports/PYTHON_TEST_SHARDS_v2.95.70.md` and `.json` (105/105 modules; 788 pass, 1 accepted skip, no failures).
- Node regression: `reports/NODE_TEST_REPORT_v2.95.70.md` (45/45 PASS).
- Data comparison: `reports/DATA_DIFF_v2.95.70.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.70.md`.
- Package/replay evidence: `reports/PACKAGE_VERIFICATION_v2.95.70.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.70.md`.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Master project status: `MASTER_STATUS.md`.
- Assessment completion and draft/commit semantics: `ASSESSMENT_FLOW.md`.
- Changelog: `../CHANGELOG.md` and `CHANGELOG.md`.

## Hosting and data boundaries

The project remains a static GitHub Pages PWA. No Cloudflare Worker, API server or backend was added. LocalStorage/IndexedDB learner data is not migrated by this release. Hosted GitHub Actions, live Pages deployment, installed-PWA update/offline propagation and physical-device acceptance remain unverified.
