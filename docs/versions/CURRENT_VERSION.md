# Current Version — TOEIC Dictionary v2.95.65

- Current source: **v2.95.65** — Batch 035 Cambridge historical-test repair and single shared modal overlay.
- Exact predecessor: `TOEIC_Dictionary_v2.95.64_FullSource.zip` (SHA-256 `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`).
- Release package: `TOEIC_Dictionary_v2.95.65_FullSource.zip`.
- FullSource metadata: detached SHA-256 sidecar; final file inventory and archive checksum are recorded in `reports/PACKAGE_VERIFICATION_v2.95.65.md`.
- Patch: `TOEIC_Dictionary_v2.95.65_Patch_From_v2.95.64.zip` (generated only from the exact v2.95.64 predecessor; clean-extraction replay is recorded in package verification).
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.65.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.65.md`.
- Package verification: `reports/PACKAGE_VERIFICATION_v2.95.65.md`.
- Command-log index: `reports/COMMAND_LOG_INDEX_v2.95.65.md`.
- Batch 035 Cambridge tests reconstruct the historical Batch 035 snapshot after reversing later additions/corrections; both files selected by `test_related_glossary_batch_035*.py` pass locally.
- `learningFocusBackdrop` is the sole full-screen dimming surface. `modalLayer` is a nested panel layer; modal close preserves an active learning-focus session.
- No learning content, stable IDs, relations, answer keys, Mock eligibility, learner IndexedDB data/schema or Robot Buddy privacy boundary changed. UI layout remains frozen; no Cloudflare/backend was added.
- Hosted GitHub Actions, deployed Pages, installed-PWA cache/offline behavior and physical-device acceptance remain unverified until deployment/device testing.
