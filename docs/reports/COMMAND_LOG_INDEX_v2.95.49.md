# Command Log Index — v2.95.49

Date: 2026-11-24

| Command / check | Outcome |
|---|---|
| `node tools/tests/related-glossary-quality.mjs` | PASS; placeholder families, genuine definitions, empty/malformed inputs, app integration and all 73 canonical placeholders checked |
| `python -m unittest discover -s tools/tests -p test_related_term_explanation_context.py -v` | PASS 4/4 |
| `python tools/sync-version.py --check` | PASS; all registered version markers and changelog |
| `python tools/validate-data.py` | PASS; 1,141 records; 0 ERROR / 0 WARNING; no vocabulary ID added/missing |
| `python tools/audit-learning-outcomes.py` | PASS; 11 objectives / 33 criteria; 6 evidence-collection paths |
| `python tools/audit-objective-resources.py` | PASS; 379/379 resource records linked |
| `python tools/audit-related-glossary-quality.py` | PASS; read-only report: 567 entries, 227 flagged (223 high / 2 medium / 2 low), 150 missing definitions, 73 placeholders |
| `python tools/audit-related-glossary-candidates.py` | PASS; 556/804 referenced terms covered; 248 unique missing terms; no canonical headword for those candidates |
| Full Python sharded suite | PASS WITH SKIPS; 89/89 modules terminal; 692 PASS / 1 accepted SKIP / 0 FAIL / 0 ERROR / 0 TIMEOUT |
| GitHub Actions shell replay | PASS 110/110 run steps; 0 fail / timeout / error / pending |

No hosted GitHub Actions run, GitHub Pages deployment or physical browser/device test is implied by local commands.


## Additional verified commands

- `python tools/run-python-tests-sharded.py --root . --timeout-per-module 180 --report-dir /tmp/toeic_v29549_full_suite --version 2.95.49`: 89/89 modules terminal; 692 passed, 1 accepted skip, 0 failed, 0 errored, 0 timed out, 0 not run.
- Local `.github/workflows/validate-data.yml` shell replay: 110/110 run steps PASS. Report: `GITHUB_ACTIONS_SHELL_REPLAY_v2.95.49.md`.
- New module cache path checked through the real data validator and workflow replay; `assets/js/related-glossary-quality.js` is present in both REQUIRED and APP_SHELL.
