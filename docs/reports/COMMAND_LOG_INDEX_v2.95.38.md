# Command Log Index — v2.95.38

- `python -m unittest tools.tests.test_related_term_explanation_context tools.tests.test_choice_identity tools.tests.test_choice_history tools.tests.test_practice_mode_fallback -v` — PASS, 23 tests.
- `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_0*.py' -v` — PASS, 46 tests.
- `python -m unittest tools.tests.test_ci_coverage tools.tests.test_repository_integrity tools.tests.test_related_term_explanation_context -v` — PASS, 7 executions (3 duplicate feature tests).
- JavaScript regression loop over `tools/tests/*.mjs` — 39 files, no failure observed.
- `python tools/validate-data.py` — PASS, 0 errors/0 warnings.
- `python tools/validate-learning-content.py` — PASS, 0 errors/0 warnings.
- `python tools/audit-repository-integrity.py` — PASS, 408 checks, 0 errors/optional warnings.
- `python tools/sync-version.py --check` — PASS.
- Full Python discovery, remote CI, Pages deployment and device/browser acceptance were not run.

- FullSource packaging: 559 files; Patch 12 files (9 changed + 3 added), 0 deletions; clean replay matched 559/559; ZIP CRC/root and SHA verification PASS.
