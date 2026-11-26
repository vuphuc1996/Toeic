# TOEIC Dictionary v2.95.71 — Project Documentation

This documentation describes the current locally verified source candidate. It does not imply that the candidate has been pushed or deployed.

- Current release: `2.95.71`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.71.md`.
- Python inventory: `reports/PYTHON_TEST_SHARDS_v2.95.71.md` and `.json` (107/107 modules; 798 pass, 1 accepted skip, no failures).
- Node regression: `reports/NODE_TEST_REPORT_v2.95.71.md` (45/45 PASS).
- Data comparison: `reports/DATA_DIFF_v2.95.71.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.71.md`.
- Package/replay evidence: `reports/PACKAGE_VERIFICATION_v2.95.71.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.71.md`.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Word Family graph audit: `reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.71.md/.json` (read-only review flags; no automatic graph mutation).
- Related Glossary quality and next-candidate queue: `reports/RELATED_GLOSSARY_QUALITY_v2.95.71.md` and `reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.71.md`.
- Project progress dashboard: `reports/PROJECT_PROGRESS_v2.95.71.md` (54.47% provisional weighted measurable build index; denominators/weights documented).
- Batch 045 glossary ledger: `../patches-related-terms/v2.95.71/batch-045-glossary-ledger.json`.
- Master project status: `MASTER_STATUS.md`.
- Assessment completion and draft/commit semantics: `ASSESSMENT_FLOW.md`.
- Changelog: `../CHANGELOG.md` and `CHANGELOG.md`.

## Hosting and data boundaries

The project remains a static GitHub Pages PWA. No Cloudflare Worker, API server or backend was added. LocalStorage/IndexedDB learner data is not migrated by this release. Hosted GitHub Actions, live Pages deployment, installed-PWA update/offline propagation and physical-device acceptance remain unverified.
