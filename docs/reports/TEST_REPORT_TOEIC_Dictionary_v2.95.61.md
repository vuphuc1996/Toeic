# Test Report — TOEIC Dictionary v2.95.61

## Environment

- Python: 3.13.5
- Node.js: v22.16.0
- Platform: Linux container; local source/archive verification only.

## Focused Python regression

**121/121 PASS across 16 modules**; 0 failed, 0 errored, 0 skipped, 0 deselected.

| Module | Cases | Result |
|---|---:|---|
| `test_related_glossary_batch_042.py` | 5 | PASS |
| `test_related_glossary_batch_041.py` | 4 | PASS |
| `test_related_glossary_batch_039.py` | 4 | PASS |
| `test_related_glossary_merge_038.py` | 8 | PASS |
| `test_related_glossary_batch_037.py` | 7 | PASS |
| `test_related_glossary_batch_036.py` | 6 | PASS |
| `test_related_glossary_batch_035.py` | 5 | PASS |
| `test_related_glossary_batch_034.py` | 6 | PASS |
| `test_related_glossary_backlog.py` | 3 | PASS |
| `test_related_glossary_quality_audit.py` | 15 | PASS |
| `test_related_glossary_candidate_audit.py` | 4 | PASS |
| `test_patch_related_terms.py` | 11 | PASS |
| `test_related_term_explanation_context.py` | 4 | PASS |
| `test_test_fingerprints.py` | 10 | PASS |
| `test_python_test_shard_runner.py` | 19 | PASS |
| `test_release_acceptance_runner.py` | 10 | PASS |

Historical reconstruction tests explicitly reverse the newer Batch 042 before checking older patch hashes. They are not disabled or weakened.

## Full Python discovery — incomplete

Command: `python tools/run-python-tests-sharded.py --version 2.95.61 --report-dir docs/reports/python-test-shards-v2.95.61`

- Discovered: 95 modules / 95.
- Completed: 19 modules PASS; 76 modules NOT RUN.
- Completed cases: 140 collected / 140 passed; 0 failed / 0 skipped / 0 errored / 0 deselected.
- Module failures, module timeouts and collection/import errors among completed modules: 0.
- The outer tool execution reached its 300-second limit before remaining modules could run. No shell exit code was captured for the interrupted outer process. This is **INCOMPLETE**, not a full-suite PASS.
- The sharded report and JSON preserve the 19 completed modules and list all pending modules.
- Test inventory comparison against the v2.95.45 baseline: 88 baseline modules, 95 current; 7 added, 18 content-modified, 0 removed, 0 confirmed renames, 0 suspected renames.

## Node and syntax

- All `tools/tests/*.mjs`: **42/42 PASS**.
- `node tools/tests/related-glossary-quality.mjs`: PASS.
- `node --check` for 20 `assets/js/*.js` modules and `sw.js`: PASS (21 files total).

## Data and version validators

- `python tools/validate-data.py`: PASS — 1,141 canonical records; 0 ID additions/removals; 0 ERROR / 0 WARNING (legacy baseline warnings: 0). Current US IPA coverage 1,062/1,141 (93%); 79 missing remain review-only. Relation targets lacking glossary coverage remain 248/804.
- `python tools/validate-learning-content.py`: PASS — Listening 145 units / 295 questions; Reading 73 units / 287 questions; Grammar 58 lessons / 169 exercises; Part 5 practice-only 80 questions; 0 errors / 0 warnings.
- `python tools/sync-version.py --check`: PASS — all 13 registered release markers synchronized to v2.95.61.

## Initial harness issues and resolution

- An initial combined `python -m unittest tools.tests...` invocation was not the project's supported discovery invocation for tests importing `glossary_test_helpers`; four modules failed import under that invocation. They were rerun individually with the repository's supported `python -m unittest discover -s tools/tests -p '<module>' -v` command and passed.
- The first candidate-audit assertion still expected the v2.95.60 missing-definition count (131); it was updated to the measured v2.95.61 count (111). The historical Batch 040 test was also updated to reverse Batch 042 before reconstructing its original snapshot. All affected tests pass in the focused result above.
- No production code or test assertion was weakened to obtain a pass.

## Not verified

Hosted GitHub Actions, GitHub Pages deployment, installed-PWA cache propagation/offline behavior, browser storage restore on physical devices, and physical iOS/iPadOS/Android acceptance were not performed in this run.
