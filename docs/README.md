# TOEIC Dictionary v2.95.75 — Project Documentation

This documentation describes the current locally verified source candidate. It does not imply that the candidate has been pushed or deployed.

- Current release: `2.95.75`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.75.md`.
- 7-Part content & answer-evidence audit: `reports/TOEIC_SEVEN_PART_CONTENT_AUDIT_v2.95.75.md` (`831` total questions: `302` `APPROVED_FOR_MOCK`, `360` `HUMAN_REVIEW_REQUIRED`, `169` `PRACTICE_SUPPORT`, `0` structural errors).
- Learning outcome evidence & reconciliation: `reports/TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.75.md` (`11` objectives / `33` criteria; `6/33` criterion-level Foundation instrumented, `11/11` objective groups wired).
- Full-Mock readiness consolidation: `reports/TOEIC_MOCK_READINESS_v2.95.75.md` (Reading `200Q` supports 2 disjoint Full forms; Listening `102Q` supports 1 Full form / `98%` 2nd-form overlap; Part 1 = `8 + 1 = 9 < 12` hard bottleneck).
- Independent editorial review queue: `reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.75.md` (`360` reserve items protected).
- Data comparison: `reports/DATA_DIFF_v2.95.75.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.75.md`.
- Package verification: `reports/PACKAGE_VERIFICATION_v2.95.75.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.75.md`.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Word Family graph audit: `reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.75.md/.json` (read-only review flags; no automatic graph mutation).
- Project progress dashboard: `reports/PROJECT_PROGRESS_v2.95.75.md` (provisional weighted measurable build index `56.80%`; denominators/weights documented).
- Master project status: `MASTER_STATUS.md`.
- Assessment completion and draft/commit semantics: `ASSESSMENT_FLOW.md`.
- Changelog: `CHANGELOG.md`.

## Hosting and data boundaries

The project remains a static GitHub Pages PWA on port 3000 (`server.js`). No Cloudflare Worker, API server, Firebase, or LLM backend was added. LocalStorage/IndexedDB v1 schema and learner records remain intact. Hosted GitHub Actions, remote `candidate` push, live Pages deployment, installed-PWA update/offline propagation, and physical-device acceptance remain unverified.
