# Command Log Index — v2.95.46

All listed commands were executed locally on 2026-11-24. Full workflow step-level status is in `GITHUB_ACTIONS_SHELL_REPLAY_v2.95.46.md`; per-module Python evidence is in the Test Report.

1. `python tools/run-release-acceptance.py --timeout 1800 --report-dir logs/release-acceptance --version 2.95.46`
2. `python tools/run-python-tests-sharded.py --timeout-per-module 180 --resume`
3. `python tools/audit-design-tokens.py`
4. `python tools/sync-design-profile.py --check`
5. `python tools/audit-repository-integrity.py`
6. `python tools/validate-data.py`
7. `python tools/validate-learning-content.py`
8. `python tools/validate-part1-photo-assets.py`
9. `python tools/sync-version.py --check`
10. `GitHub Actions workflow `.github/workflows/validate-data.yml`: replayed every run: block in order (110/110 PASS).`

## Development continuation — 2026-11-24

11. `node tools/tests/learning-outcome-progress.mjs` — PASS (deterministic recall boundary assertions included).
12. `python -m unittest tools.tests.test_learning_outcome_progress tools.tests.test_learning_outcomes tools.tests.test_objective_resource_map -v` — 8/8 PASS.
13. `python tools/audit-learning-outcomes.py` — PASS (11 objectives, 33 criteria, 6 instrumented).
14. `python tools/audit-objective-resources.py` — PASS (379/379 linked resources).
15. `node --check assets/js/learning-outcome-progress.js` — PASS.
16. `node --check tools/tests/learning-outcome-progress.mjs` — PASS.
17. `python -m unittest discover -s tools/tests -p 'test_*.py' -v` — INCOMPLETE: outer execution timeout at 300 seconds after 334 test cases had reported; no complete-suite result is claimed.
