# Current Version — TOEIC Dictionary v2.95.68

- Current source: **v2.95.68** — assessment-result reuse of the active Learning Focus dialog, 2.4-second confetti animation, historical Batch 036 checksum reconstruction correction, and regression coverage.
- Exact predecessor FullSource: `TOEIC_Dictionary_v2.95.67_FullSource(1).zip`; SHA-256 `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`. This uploaded, complete archive is the sole v2.95.68 baseline (807 files; ZIP CRC verified).
- Release package: `TOEIC_Dictionary_v2.95.68_FullSource.zip`.
- Patch: `TOEIC_Dictionary_v2.95.68_Patch_From_v2.95.67.zip`; generated only from the exact predecessor and replay-verified before acceptance.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.68.md`.
- Data comparison: `reports/DATA_DIFF_v2.95.68.md`.
- Word Family graph audit: `reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.68.md` and JSON.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.68.md`.
- Package verification: `reports/PACKAGE_VERIFICATION_v2.95.68.md`.
- Command log: `reports/COMMAND_LOG_INDEX_v2.95.68.md`.
- Batch 036 historical check now reconstructs the pre-Batch-036 vocabulary snapshot correctly: actual reconstructed SHA-256 equals the existing ledger SHA-256 `8c35a6fce159d056832f1e7c6ab395a5dd1d1b34d94e371cb464d6ae1bef11a2`. The ledger is unchanged.
- Source-level data remains unchanged except `data/manifest.json` release marker. The canonical vocabulary identity remains 1,141/1,141 baseline IDs; the four protected learning-bank files retain their ledger composite SHA-256.
- Source release status: candidate with focused local verification; complete Python discovery was attempted but did not finish. Hosted Actions, GitHub Pages deployment, installed-PWA propagation and physical-device acceptance remain unverified.
