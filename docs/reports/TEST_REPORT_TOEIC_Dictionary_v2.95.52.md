# Test Report — TOEIC Dictionary v2.95.52

## Dynamic Python suite

- Approved root: `tools/tests`; baseline inventory: v2.95.45 (88 modules).
- Discovered / completed: **91 / 91 modules**.
- Collected test cases: **705**.
- Passed / failed / skipped / errored: **704 / 0 / 1 / 0**.
- Timed out / not run / deselected: **0 / 0 / 0**.
- Module outcomes: **90 PASS + 1 PASS WITH SKIPS**.
- Overall: **PASS WITH SKIPS**; all discovered modules reached terminal execution.
- Accepted skip: `test_patch_data.PatchDataTests.test_repository_gitignore_excludes_audit_logs`; reason: `source archive has no Git metadata; gitignore assertion requires a clone`. This exact reason is allowlisted; skipped test is not counted as passed.
- Environment: Python 3.13.5 / Node v22.16.0 / Linux x86_64. Hosted workflow targets Python 3.12 / Node 24.
- Machine-readable evidence: `PYTHON_TEST_SHARDS_v2.95.52.json` and `PYTHON_TEST_SHARDS_v2.95.52.md` in this report directory.

## Focused Related Glossary verification

- All Related Glossary Python modules: **131/131 PASS** after updating historical snapshot reconstruction to reverse Batch 041 → Batch 040 → Batch 039 in descending order.
- Batch 041 regression: **4/4 PASS**; exact 11-term inventory, relation anchors, POS, source provenance, guarded preimage reconstruction, Vietnamese meaning preservation and glossary identity count.
- Batch 040 regression remains PASS after historical test reconstruction was extended for the newer Batch 041.
- `test_related_glossary_quality_audit.py`: **15/15 PASS**.
- `tools/tests/related-glossary-quality.mjs`: Node regression must pass as part of workflow replay.
- Quality audit: 567 entries; 373 definitions present; 131 missing definitions; 63 placeholders; 190 missing POS; 65 missing provenance; 198 flagged entries.
- Relation-target coverage remains 556/804 (69.2%); 248 unique relation terms / 249 occurrences remain uncovered. No missing relation term was auto-added.

## Data and project audits

- `tools/validate-data.py`: **PASS**, 1,141 vocabulary records; zero ID additions/removals; 0 ERROR / 0 WARNING. ID-set SHA-256 prefix `adccbdb4c9887220`.
- `tools/sync-version.py --check`: **PASS**, all registered version markers and changelog heading aligned to 2.95.52.
- Learning outcome audit: 11 objectives / 33 criteria; 6/33 have evidence-collection paths; Foundation 6/6. Wiring does not certify mastery.
- Objective resource map: 379/379 links.
- Related Glossary candidate audit: 556/804 covered; 248 missing unique terms; zero missing terms have canonical headwords.

## CI and production boundary

- Local shell replay of every `run:` step in `.github/workflows/validate-data.yml`: **113/113 PASS**, 0 fail / timeout / error / pending. This is a local replay, not a hosted GitHub Actions execution. Evidence: `GITHUB_ACTIONS_SHELL_REPLAY_v2.95.52.md` and `.json`.
- GitHub-hosted Actions, GitHub Pages deployment, installed-PWA cache propagation, offline behavior and physical iOS/Android/tablet/desktop acceptance remain **UNVERIFIED**.
- Independent editorial review of all eleven Batch 041 Cambridge paraphrases remains pending.

## Overall

**Local Python suite: PASS WITH SKIPS. Production acceptance is not granted.**
