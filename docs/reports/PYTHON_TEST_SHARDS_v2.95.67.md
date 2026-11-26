# Python Test Inventory and Focused Execution — v2.95.67

## Execution status

- Overall Python suite: **INCOMPLETE — focused selection only; full inventory not executed to completion**.
- Dynamically discovered modules: **102**.
- Fully executed focused modules: **17 PASS**.
- Focused test cases: **161 collected / 161 passed / 0 failed / 0 skipped / 0 errors**.
- Additional targeted release-key methods in `test_validator.py`: **2/2 PASS**, executed independently and not included in the 161-case total.
- Full `test_validator.py` module: 44 test methods; did not emit a final unittest summary inside the execution window. It remains INCOMPLETE.
- Other unselected test modules are NOT RUN for this release. No status is inferred from the test inventory of an earlier release.

## Focused modules

| Module | Collected | Passed | Failed | Skipped | Errors | Status |
|---|---:|---:|---:|---:|---:|---|
| `test_vocabulary_family_batch_025.py` | 5 | 5 | 0 | 0 | 0 | PASS |
| `test_vocabulary_family_links.py` | 6 | 6 | 0 | 0 | 0 | PASS |
| `test_vocabulary_relationship_graph_audit.py` | 8 | 8 | 0 | 0 | 0 | PASS |
| `test_ci_coverage.py` | 8 | 8 | 0 | 0 | 0 | PASS |
| `test_sync_version.py` | 12 | 12 | 0 | 0 | 0 | PASS |
| `test_project_progress.py` | 4 | 4 | 0 | 0 | 0 | PASS |
| `test_repository_integrity.py` | 2 | 2 | 0 | 0 | 0 | PASS |
| `test_package_source.py` | 3 | 3 | 0 | 0 | 0 | PASS |
| `test_test_fingerprints.py` | 10 | 10 | 0 | 0 | 0 | PASS |
| `test_git_commit_readiness.py` | 10 | 10 | 0 | 0 | 0 | PASS |
| `test_release_acceptance_runner.py` | 10 | 10 | 0 | 0 | 0 | PASS |
| `test_learning_content.py` | 34 | 34 | 0 | 0 | 0 | PASS |
| `test_question_evidence.py` | 7 | 7 | 0 | 0 | 0 | PASS |
| `test_answer_position_balance.py` | 4 | 4 | 0 | 0 | 0 | PASS |
| `test_baseline_ids.py` | 13 | 13 | 0 | 0 | 0 | PASS |
| `test_related_glossary_backfill_025.py` | 6 | 6 | 0 | 0 | 0 | PASS |
| `test_vocabulary_detail_examples.py` | 19 | 19 | 0 | 0 | 0 | PASS |
| **Focused total** | **161** | **161** | **0** | **0** | **0** | **PASS** |

## Targeted validator methods

Command:

```sh
python -m unittest discover -s tools/tests -p 'test_validator.py' -k release_keyed -v
```

- `test_release_keyed_appshell_url_resolves_to_real_file` — PASS.
- `test_release_keyed_appshell_url_still_rejects_missing_file` — PASS.
- Total: 2/2 PASS.

The full validator class was also attempted, but it did not complete in the available execution window. Targeted method success must not be represented as full-module success.

## Inventory interpretation

The dynamic inventory currently contains 102 Python modules. This file documents only the selected focused execution listed above; it is not a full 102-module shard ledger. The full-suite acceptance gate remains open until every discovered module has a recorded accepted terminal state, including explicit skip/failure/timeout accounting.
