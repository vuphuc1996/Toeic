# Command Log Index — v2.95.60

- Baseline archive SHA-256: `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`.
- Python runtime: Python 3.13.5. Node runtime: v22.16.0.

## Completed commands

- `python tools/sync-version.py --apply` — PASS.
- `python tools/sync-version.py --check` — PASS.
- `python tools/validate-data.py` — PASS.
- `python tools/validate-learning-content.py` — PASS.
- `python tools/audit-item-complexity.py` — PASS.
- `python tools/audit-related-glossary-quality.py --output ... --json-output ...` — PASS.
- `python tools/audit-related-glossary-candidates.py --output ...` — PASS.
- `python tools/build-related-glossary-enrichment-queue.py --output ... --json-output ...` — PASS.
- `python tools/build_missing_ipa_review_queue.py --output ...` — PASS (79 records; cmudict 1.1.3).
- `python tools/render_missing_ipa_review_queue.py --input ... --output ...` — PASS.
- Focused unittest command covering six modules — PASS 37/37.
- `python -m unittest tools.tests.test_ci_coverage -v` — PASS 3/3 after workflow correction.
- Every `tools/tests/*.mjs` script — PASS 42/42.
- `node --check sw.js`; syntax check of every `assets/js/*.js` — PASS.
- Python compile of changed tools/tests — PASS.

## Incomplete command

- `python tools/run-python-tests-sharded.py --root . --timeout-per-module 60 --report-dir ... --version 2.95.60` — execution window ended after 17/94 modules. 126 cases collected and passed in those modules; 77 modules were not run. Report: `PYTHON_TEST_SHARDS_v2.95.60.md/.json`. Do not treat as full suite completion.

## External commands not run

- Hosted GitHub Actions workflow and GitHub Pages deployment were not triggered or inspected.
- No physical iOS/iPadOS/Android device testing was performed.
