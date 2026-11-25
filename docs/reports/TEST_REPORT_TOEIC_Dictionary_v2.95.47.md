# Test Report — TOEIC Dictionary v2.95.47

## Scope and terminal state

- Dynamically discovered Python test modules: **89**.
- Completed modules: **88/89** (82 PASS in the resumable runner, 1 PASS WITH SKIPS, plus 5 separately executed modules PASS).
- Pending module: `tools/tests/test_validator.py` — did not reach a terminal summary within the available execution window. It is not counted as pass or fail.
- Terminal case totals: **653 passed, 1 accepted skip, 0 failed, 0 errors** across completed modules.
- Full Python suite: **INCOMPLETE** until `test_validator.py` is completed. Do not interpret the absence of failures in completed modules as a full-suite PASS.

## New regression scope

- Node runtime test `tools/tests/learning-outcome-progress.mjs`: PASS.
- Python wrapper `tools/tests/test_learning_outcome_progress.py`: 3/3 PASS.
- Five remaining Python modules separately completed: visual composition 9/9, vocabulary batch 012 4/4, vocabulary detail examples 19/19, vocabulary family links 6/6, relationship graph audit 8/8.
- JavaScript syntax check for `assets/js/learning-outcome-progress.js`: PASS.
- Version synchronization (`tools/sync-version.py --check`): PASS, all 14 registered markers including CHANGELOG.

## Incomplete / unverified

- `tools/tests/test_validator.py` is pending; a direct run did not complete within the tool execution window. No result is claimed.
- GitHub Actions hosted execution, GitHub Pages deployment, cache propagation and physical iOS/Android/tablet/desktop browser acceptance remain unverified.

## Data protection

The development delta does not intentionally change vocabulary records, related-term relations, question IDs, choices, answer keys, IndexedDB schema or learner history. These are verified byte-identical against the exact v2.95.46 Integrity Continuation base archive in the package verification report.
