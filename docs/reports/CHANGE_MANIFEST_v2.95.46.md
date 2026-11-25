# Change Manifest — v2.95.46

- Development base: user-supplied v2.95.46 candidate ZIP, SHA-256 `4748288320b17ba4e94b1f5f064288034418ee23d1cc67a739d9614f9f410966`.
- Patch lineage: candidate-based patch replayed against that exact candidate ZIP; not an official v2.95.45-to-v2.95.46 patch because the v2.95.45 source ZIP was not supplied in this task.
- Comparison reference: previous assistant-generated v2.95.46 ZIP, SHA-256 `d285cb64441d74b2625553d98213a9dc5f2fb81de230efc4e1c551a302d9cd7b` (used only for the initial comparison, not as development base).
- This development batch preserves the user candidate as its baseline.

## Functional changes

- Fixed test checkpoint resume identity: `--resume` no longer participates in the execution fingerprint because it changes checkpoint loading behavior, not test semantics.
- Expanded generated audit snapshot exclusions in source fingerprint policy; generated reports remain in FullSource and are covered by ZIP SHA-256.
- Fixed toast close-button CSS to use existing design-system tokens for font size, radius and surface color; no layout redesign.
- Added regression tests for resume identity, generated-report fingerprint scope and Toast token compliance.
- Refreshed current Master/README/version ledger and release evidence reports.

## Protected source invariants

- No `data/vocabulary/**`, `data/related-terms.json`, learning content, question/choice/answer-key data, IndexedDB schema, learner history or service-worker runtime logic was intentionally modified.
- No Cloudflare/backend/GAS/iframe integration added.
- UI remains frozen except the narrow Toast close-control styling fix.

## Changed implementation files

- `tools/run-python-tests-sharded.py`
- `tools/tests/test_python_test_shard_runner.py`
- `tools/source-fingerprint-policy.json`
- `tools/tests/test_test_fingerprints.py`
- `assets/css/app.css`
- `tools/tests/test_visual_composition.py`
- `V2.95.46_UPDATE_NOTES.txt`, `docs/README.md`, `docs/MASTER_STATUS.md`, `docs/CHANGELOG.md`, `docs/versions/CURRENT_VERSION.md`
