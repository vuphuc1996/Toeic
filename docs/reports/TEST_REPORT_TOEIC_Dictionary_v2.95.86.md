# Test Report — TOEIC Dictionary v2.95.86

**Branch:** `candidate`  
**Validated application/source SHA:** `d5cefa69610bc381a802127d5f9f000d88e48df8`  
**Baseline:** v2.95.85 `7b8d80f1eef1523b5c2f31f0361a51c90011da7e`

## Exact-SHA acceptance evidence

<badge color="green">PASS</badge> **GitHub Actions Validate — run 46137090655**

- Exact SHA: `d5cefa69610bc381a802127d5f9f000d88e48df8`
- Overall workflow: **SUCCESS, 152/152 steps**
- Full Python test discovery: **871 tests PASS** in **14.759 seconds** (`python -m unittest discover -s tools/tests`)
- JavaScript syntax check: **PASS**
- `tools/sync-version.py --check`: **PASS**
- Data validators, Part 1 photo/attribution validator, Listening/Reading/Grammar validators, objective-resource mapping, learning-outcome criteria, Mock-readiness and content/evidence audits: **PASS**.

<badge color="green">PASS</badge> **GitHub Pages — run 46137089787**

- Exact SHA: `d5cefa69610bc381a802127d5f9f000d88e48df8`
- Build with Jekyll: **SUCCESS**
- Upload artifact: **SUCCESS**
- Deploy to GitHub Pages: **SUCCESS**
- Build-status reporting: **SUCCESS**

These results apply to the exact v2.95.86 source/code SHA above. A subsequent documentation-only candidate commit updates the release ledger; it does not change the application source validated at this SHA.

## Focused Batch 018 coverage

- `tools/tests/test_content_batch_018.py` checks the three new photo units, local JPG binaries, provenance, four statements, evidence/answer IDs, resource-level reserve status, no criterion-map promotion and unchanged Mock-approved count.
- Listening reserve regression: **196**, with Part 1 **4** pending review; approved Mock Listening remains **102**.
- Editorial queue tests distinguish resource-level reserve from question-level Part 4 practice-only status.
- Historical Batch 026/027/036/037/038 fingerprints remain protected using exact Batch 018 allowlist reconstruction; expected historical hashes were not loosened.
- Full seven-part inventory audit: **0 structural errors**, Listening **148 resources / 311 questions**, review queue **363**.

## Still not independently verified

- FullSource ZIP generation, CRC/SHA and replay verification.
- Installed-PWA cache propagation and a real offline relaunch after deployment.
- Physical-device QA on iPad, phones and desktop/laptop viewports.
- Independent second-person editorial approval for the four Part 1 reserve questions.

## Release boundary

This is **candidate source acceptance**, not production acceptance. No merge to `main` or production promotion is authorized by this report. The v2.95.85 owner-supplied 865-test result remains predecessor evidence only and is not substituted for the v2.95.86 GitHub Actions evidence above.
