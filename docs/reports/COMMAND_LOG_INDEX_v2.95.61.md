# Command Log Index — TOEIC Dictionary v2.95.61

All paths are relative to the exact v2.95.60-derived working root. Exit code 0 is recorded only for commands that completed successfully. The full-suite process was interrupted by the outer 300-second tool limit; no shell exit code was captured.

## Source patch and reports

| Command | Result |
|---|---|
| `python tools/update-related-terms.py --patch patches-related-terms/v2.95.61/related-terms-042.json --dry-run` | PASS · exit 0 · 20 exact-guarded updates previewed |
| `python tools/update-related-terms.py --patch patches-related-terms/v2.95.61/related-terms-042.json --apply` | PASS · exit 0 · atomic update of 20 existing rows |
| `python tools/audit-related-glossary-quality.py --output docs/reports/RELATED_GLOSSARY_QUALITY_v2.95.61.md --json-output docs/reports/RELATED_GLOSSARY_QUALITY_v2.95.61.json` | PASS · exit 0 |
| `python tools/build-related-glossary-enrichment-queue.py --output docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.61.md --json-output docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.61.json` | PASS · exit 0 |
| `python tools/audit-related-glossary-candidates.py --output docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.61.md` | PASS · exit 0 |
| `python tools/sync-version.py --set 2.95.61 --apply` | PASS · exit 0 · 13 markers synchronized |
| `python tools/sync-version.py --check` | PASS · exit 0 · 13/13 markers |
| `python -m py_compile` for the updated Python helper and regression modules | PASS · exit 0 |

## Focused Python tests

Each row ran with `python -m unittest discover -s tools/tests -p '<module>' -v`; every command exited 0.

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
| **Total** | **121** | **121 PASS** |

## Validators and Node

| Command | Result |
|---|---|
| `python tools/validate-data.py` | PASS · exit 0 · 1,141 records, 0 errors / 0 warnings |
| `python tools/validate-learning-content.py` | PASS · exit 0 · 0 errors / 0 warnings |
| `node tools/tests/related-glossary-quality.mjs` | PASS · exit 0 |
| `for f in tools/tests/*.mjs; do node "$f"; done` | PASS · 42/42 scripts, all exit 0 |
| `node --check` for `sw.js` and every `assets/js/*.js` | PASS · 21/21 files |

## Full Python discovery

| Command | Result |
|---|---|
| `python tools/run-python-tests-sharded.py --version 2.95.61 --report-dir docs/reports/python-test-shards-v2.95.61` | INCOMPLETE · outer tool reached 300 seconds; report records 19/95 modules PASS, 140/140 cases in completed modules, 76 NOT RUN; no shell exit code captured |

## Package and Patch verification

| Command / operation | Result |
|---|---|
| `git diff --cached --check` | PASS · exit 0 |
| `git apply --check patch.diff` on a fresh extraction of the exact v2.95.60 FullSource | PASS · exit 0 |
| `git apply patch.diff` on that fresh extraction | PASS · exit 0 |
| `python tools/package_source.py 2.95.61 /mnt/data/TOEIC_Dictionary_v2.95.61_FullSource.zip --repo <committed-v2.95.61-repo>` | PASS · exit 0 · 737 files / one root |
| Patch ZIP creation and FullSource/Patch CRC + SHA sidecar verification | PASS |
| SHA-256 file-tree comparison of replay against target source | PASS · 737/737 identical; 0 missing / extra / mismatched |
| Protected source comparison (A–Z vocabulary + Grammar/Listening/Reading/Part 5 banks) | PASS · 54/54 byte-identical |

## Superseded exploratory invocations

- An early combined dotted-module unittest invocation produced import errors for tests that rely on the `tools/tests` discovery path; the same modules were rerun using the repository's supported discovery command and passed.
- The first draft of the candidate-audit test expected the prior release's metric; the expected metric was updated to the measured v2.95.61 count. Historical patch reconstruction was extended to reverse Batch 042 before older batches. Final focused tests all pass.
