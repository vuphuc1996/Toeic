# Test Report — TOEIC Dictionary v2.95.62

## Source and scope

- Exact source baseline: `TOEIC_Dictionary_v2.95.61_FullSource.zip`, SHA-256 `63bb04e7f9bbb15fa76ff00ab833b392bf6d48e71ecafd8740b05c2ff1cb56b7`; checksum sidecar and ZIP CRC were verified before extraction.
- Implementation: Related Glossary Batch 043, 21 exact-guarded updates to existing relation-target rows; regression/history tests and GitHub Actions coverage were updated.
- Scope intentionally excludes UI redesign, vocabulary/learning-bank mutations, question/choice/answer-key changes, learner data migrations and backend/hosting changes.

## Focused Python tests — final execution

**160/160 tests PASS across 24 modules.** Each module was run with `python -m unittest discover -s tools/tests -p '<module>' -v`; all listed final runs exited 0.

| Module | Cases | Result |
|---|---:|---|
| `test_related_glossary_batch_043.py` | 6 | PASS |
| `test_related_glossary_batch_042.py` | 5 | PASS |
| `test_related_glossary_batch_041.py` | 4 | PASS |
| `test_related_glossary_batch_039.py` | 4 | PASS |
| `test_related_glossary_merge_038.py` | 8 | PASS |
| `test_related_glossary_quality_audit.py` | 15 | PASS |
| `test_related_glossary_candidate_audit.py` | 4 | PASS |
| `test_related_glossary_backfill_025.py` | 6 | PASS |
| `test_patch_related_terms.py` | 11 | PASS |
| `test_related_glossary_canonical_enrichment_029.py` | 8 | PASS |
| `test_related_glossary_batch_030.py` | 4 | PASS |
| `test_related_glossary_batch_032.py` | 4 | PASS |
| `test_related_glossary_batch_033.py` | 3 | PASS |
| `test_related_glossary_batch_034.py` | 6 | PASS |
| `test_related_glossary_batch_035.py` | 5 | PASS |
| `test_related_glossary_batch_036.py` | 6 | PASS |
| `test_related_glossary_batch_037.py` | 7 | PASS |
| `test_vocabulary_relationship_graph_audit.py` | 8 | PASS |
| `test_repository_integrity.py` | 1 | PASS |
| `test_test_fingerprints.py` | 10 | PASS |
| `test_python_test_shard_runner.py` | 19 | PASS |
| `test_release_acceptance_runner.py` | 10 | PASS |
| `test_package_source.py` | 3 | PASS |
| `test_ci_coverage.py` | 3 | PASS |
| **Total** | **160** | **160 PASS** |

The candidate-audit and legacy Batch 025 fixture tests initially surfaced hard-coded prior-release counts/reconstruction order. Those assertions were corrected to the measured v2.95.62 state, and the final reruns above passed. No validation rule or data-quality threshold was weakened.

## Node and JavaScript syntax

- Every `tools/tests/*.mjs` regression script: **42/42 PASS**. This includes the related-glossary placeholder suppression check after its expected live placeholder count was updated from 63 to 50.
- `node --check` on `sw.js` and all `assets/js/*.js`: **21/21 PASS**.

## Validators and audits

| Check | Observed result |
|---|---|
| `tools/validate-data.py` | PASS; 1,141 vocabulary records; 0 ID additions / 0 removals; 0 ERROR / 0 WARNING (legacy baseline) |
| `tools/validate-learning-content.py` | PASS; 0 errors / 0 warnings; Listening 145 units / 295 questions, Reading 73 / 287, Grammar 58 / 169 exercises |
| Related Glossary quality audit | PASS; 567 rows; 157 flagged (153 high, 2 medium, 2 low); 103 missing definitions, 50 placeholders, 153 missing POS, 52 missing provenance; 0 duplicate groups |
| Related Glossary enrichment queue | PASS; read-only queue; 150 flagged rows are currently referenced, 152 relation occurrences |
| `tools/audit-toeic-coverage.py` | PASS; vocabulary 1,141; IPA 1,062; word family 276; Listening 145/295; Reading 73/287; Grammar 58; sentence completion practice 80 |
| `tools/audit-question-evidence.py` | PASS; 582 indexed questions; 193 Listening reserve questions remain reserve-pending independent review |
| `tools/audit-distractors.py` | PASS; 264 questions in audit scope; 156 reserve structural checks; valid unique choices and answer keys in review scope |
| `tools/audit-repository-integrity.py` | PASS; 442 local references/data files inspected; 0 errors / 0 optional warnings |
| `tools/sync-version.py --check` | PASS; 13/13 release markers synchronized to 2.95.62 |
| `test_ci_coverage.py` | PASS; every Python test module and JavaScript regression suite is registered in GitHub Actions |

## Full-suite boundary

- The test inventory lists **96 Python test modules** (`tools/run-python-tests-sharded.py --list`); the historical inventory baseline contains 88 modules and reports 8 additions (including Batch 043 and several prior-release test files).
- A full 96-module execution was **NOT RUN** in this batch. Only the 24 focused modules listed above are claimed as executed; do not interpret 160/160 as a full-suite pass. A separate attempt to run `test_validator.py` hit the 180-second command limit after 23 tests had reported `ok`, while the 24th test was still running; no aggregate suite result was produced and this partial attempt is excluded from the 160-test total.
- The workflow file was updated so `test_related_glossary_batch_043.py` is compiled and executed by GitHub Actions. A hosted GitHub Actions run was not initiated or verified here.

## Not verified in this environment

- Hosted GitHub Actions status and GitHub Pages deployment.
- Installed-PWA service-worker update/cache propagation, offline behavior and browser storage retention on real browsers.
- Physical iPhone/iPad/Android/desktop acceptance.
- Independent editorial approval of the 21 Cambridge paraphrases; this remains pending.
