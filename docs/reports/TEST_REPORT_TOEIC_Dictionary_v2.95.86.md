# Test Report — TOEIC Dictionary v2.95.86

**Branch:** `candidate`  
**Baseline:** v2.95.85 `7b8d80f1eef1523b5c2f31f0361a51c90011da7e`  
**Current candidate scope:** Batch 018 Part 1 reserve expansion, reserve-count regression updates, release shell synchronization and documentation repair.

## Evidence status

<badge>AWAITING EXACT-SHA VALIDATION</badge>

The user confirmed that v2.95.85 passed **865/865 unit tests**, compilation/build checks and syntax lint. Those results apply only to v2.95.85 and are not attributed to v2.95.86.

The v2.95.86 source changes are committed to `candidate`. The repository workflow `.github/workflows/validate-data.yml` is configured to run on candidate pushes. The complete test suite must finish on the final v2.95.86 SHA before this report can record PASS.

## Added/updated validation

- Python: `tools/tests/test_content_batch_018.py` checks exact batch inventory, image provenance, local JPG files, answer evidence, stable IDs, independent-review status, absence of outcome-map promotion, and unchanged Mock-approved count.
- Python: `tools/tests/test_listening_expansion.py` updated pending total to 196 and projected Part 1 inventory to 12.
- Python: `tools/tests/test_content_batch_027.py` removes the Batch 018 additions when reconstructing its historical Listening-library fingerprint.
- Python: `tools/tests/test_mock_readiness_audit.py` updated Part 1 post-review ceiling to 12 and the partwise post-review Listening count ceiling to two forms.
- JavaScript: `tools/tests/mock-exam-engine.mjs` confirms 196 reserve questions remain excluded while approved Listening Mock count remains 102.
- CI validator: `tools/validate-part1-photo-assets.py` checks local JPG dimensions, 4:3 ratio, file-size limits and attribution/source-type consistency.
- Full workflow also runs Python discovery, Python compilation, JavaScript syntax checks, Mock engine regressions, listening TTS checks, content audits and `tools/sync-version.py --check`.

## Not yet verified

- v2.95.86 complete Python/JavaScript test results and exact test count.
- GitHub Actions Validate and GitHub Pages jobs on the final candidate SHA.
- FullSource ZIP generation.
- Installed-PWA/offline cache propagation and physical-device QA.

Do not merge `candidate` into `main` or mark production accepted on the basis of the v2.95.85 baseline result.
