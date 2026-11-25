# Current Version — TOEIC Dictionary v2.95.66

- Current source: **v2.95.66** — PWA asset cache coherence and Batch 022 CI discovery repair (candidate).
- Exact predecessor: `TOEIC_Dictionary_v2.95.65_FullSource.zip` (SHA-256 `a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb`; 779 files).
- Release package: `TOEIC_Dictionary_v2.95.66_FullSource.zip`.
- Package generation, detached SHA-256 verification and ZIP CRC: PENDING final acceptance.
- Candidate Patch: `TOEIC_Dictionary_v2.95.66_Patch_From_v2.95.65.zip` (exact-base replay pending package generation).
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.66.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.66.md`.
- Package verification: `reports/PACKAGE_VERIFICATION_v2.95.66.md`.
- Command-log index: `reports/COMMAND_LOG_INDEX_v2.95.66.md`.
- HTML, CSS and app.js now carry the manifest release query; the Service Worker REQUIRED/APP_SHELL arrays precache the exact versioned URLs, while registration stays stable at `./sw.js`. A startup guard blocks mismatched HTML/app releases before binding DOM events.
- Batch 022 CI contract checks the active unittest discovery selector; PWA readiness strips query strings before checking local file paths.
- No learning-data, learner IndexedDB, stable identity, Mock eligibility or Robot Buddy privacy-boundary migration is included.
- Hosted GitHub Actions, Pages and installed-PWA/device acceptance remain pending. This candidate must not be marked accepted until the complete workflow and exact package replay pass.
