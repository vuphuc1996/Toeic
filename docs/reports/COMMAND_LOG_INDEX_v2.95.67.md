# Command Log Index — TOEIC Dictionary v2.95.67

All commands below were executed locally against the working tree reconstructed from the exact v2.95.66 FullSource baseline. The full Python suite and all remote deployment checks are not represented as complete.

| Area | Command / procedure | Result |
|---|---|---|
| Baseline | Verify v2.95.66 FullSource SHA-256 and ZIP CRC | PASS; exact sole predecessor |
| Batch 025 family links | `python -m unittest discover -s tools/tests -p 'test_vocabulary_family_batch_025.py' -v` | 5/5 PASS |
| Existing Word Family regressions | `python -m unittest discover -s tools/tests -p 'test_vocabulary_family_links.py' -v` | 6/6 PASS |
| Word Family graph regressions | `python -m unittest discover -s tools/tests -p 'test_vocabulary_relationship_graph_audit.py' -v` | 8/8 PASS |
| CI coverage | `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | 8/8 PASS |
| Version-sync unit tests | `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | 12/12 PASS |
| Project progress | `python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v` | 4/4 PASS after refreshing stale expected count assertions |
| Repository integrity tests | `python -m unittest discover -s tools/tests -p 'test_repository_integrity.py' -v` | 2/2 PASS |
| Package source tests | `python -m unittest discover -s tools/tests -p 'test_package_source.py' -v` | 3/3 PASS |
| Test fingerprints | `python -m unittest discover -s tools/tests -p 'test_test_fingerprints.py' -v` | 10/10 PASS |
| Git commit readiness | `python -m unittest discover -s tools/tests -p 'test_git_commit_readiness.py' -v` | 10/10 PASS |
| Release acceptance runner | `python -m unittest discover -s tools/tests -p 'test_release_acceptance_runner.py' -v` | 10/10 PASS |
| Learning content | `python -m unittest discover -s tools/tests -p 'test_learning_content.py' -v` | 34/34 PASS |
| Question evidence | `python -m unittest discover -s tools/tests -p 'test_question_evidence.py' -v` | 7/7 PASS |
| Answer-position balance | `python -m unittest discover -s tools/tests -p 'test_answer_position_balance.py' -v` | 4/4 PASS |
| Canonical baseline IDs | `python -m unittest discover -s tools/tests -p 'test_baseline_ids.py' -v` | 13/13 PASS |
| Related Glossary safe backfill | `python -m unittest discover -s tools/tests -p 'test_related_glossary_backfill_025.py' -v` | 6/6 PASS |
| Vocabulary detail/examples | `python -m unittest discover -s tools/tests -p 'test_vocabulary_detail_examples.py' -v` | 19/19 PASS |
| Python focused total | 17 commands above | 161/161 PASS |
| Validator release-key cases | `python -m unittest discover -s tools/tests -p 'test_validator.py' -k release_keyed -v` | 2/2 PASS; targeted methods only |
| Full Python inventory | Dynamic discovery via `tools/run-python-tests-sharded.py --list` | 102 modules discovered; full execution INCOMPLETE |
| Full validator module | `python -m unittest discover -s tools/tests -p 'test_validator.py' -v` | INCOMPLETE; no final module summary within execution window |
| Node regression scripts | `for f in tools/tests/*.mjs; do node "$f"; done` | 43/43 PASS |
| Data validator | `python tools/validate-data.py` | 1,141 records; 0 errors / 0 warnings; IDs +0/-0 |
| Learning-content validator | `python tools/validate-learning-content.py` | 0 errors / 0 warnings |
| Part 1 assets | `python tools/validate-part1-photo-assets.py` | 9/9 PASS |
| Word Family graph audit | `python tools/audit-word-family-graph.py --output docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.67.md --json-output docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.67.json` | PASS; read-only report generated |
| Repository integrity | `python tools/audit-repository-integrity.py` | 407 references; 0 errors / 0 optional warnings |
| Design tokens | `python tools/audit-design-tokens.py` | 0 new violations; 2,773 legacy warnings |
| Version synchronization | `python tools/sync-version.py --check` | 18/18 markers PASS |
| Python syntax | `python -m compileall -q tools` | PASS |
| JavaScript syntax | `node --check sw.js`; loop through `assets/js/*.js` | PASS |

The 17 focused Python modules account for 161 completed test cases. The two targeted validator methods are reported separately. These focused results do not substitute for a complete run of all 102 dynamically discovered Python modules.
