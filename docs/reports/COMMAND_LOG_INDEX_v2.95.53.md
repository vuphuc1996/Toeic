# Command Log Index — TOEIC Dictionary v2.95.53

| Area | Command / evidence | Result |
|---|---|---|
| Version | `python tools/sync-version.py --check` | PASS |
| Design profile | `python tools/sync-design-profile.py --check` | PASS; 54 tokens / 406 legacy font-floor groups |
| Vocabulary data | `python tools/validate-data.py` | PASS; 1,141 records; 0 ID changes; 0 errors/warnings |
| Learning content | `python tools/validate-learning-content.py` | PASS; 0 errors/warnings |
| Part 1 media | `python tools/validate-part1-photo-assets.py` | PASS; 9/9 files |
| Repository | `python tools/audit-repository-integrity.py` | PASS; 429 inspected; 0 errors/warnings |
| Design tokens | `python tools/audit-design-tokens.py` | PASS; 0 new violations |
| Learning outcomes | `python tools/audit-learning-outcomes.py` | PASS; 11 objectives / 33 criteria / 6 instrumented |
| Objective resources | `python tools/audit-objective-resources.py` | PASS; 379/379 |
| Related Glossary | `python tools/audit-related-glossary-quality.py` | 567 rows; 198 flagged |
| Relation graph | `python tools/audit-vocabulary-relationship-graph.py` | 1,037 references; 0 malformed/self refs; 248 non-reciprocal review flags |
| Candidate coverage | `python tools/audit-related-glossary-candidates.py` | 556/804 covered; 248 unique missing |
| Fingerprint policy | `python -m unittest discover -s tools/tests -p test_test_fingerprints.py -v` | 10/10 PASS; generated evidence excluded, governance docs remain fingerprinted |
| Test runner regressions | `python -m unittest discover -s tools/tests -p test_python_test_shard_runner.py -v` | 19/19 PASS |
| Release runner regressions | `python -m unittest discover -s tools/tests -p test_release_acceptance_runner.py -v` | 10/10 PASS |
| Responsive tests | `python -m unittest discover -s tools/tests -p test_responsive_layout.py -v` | 8/8 PASS |
| Design system tests | `python -m unittest discover -s tools/tests -p test_design_system.py -v` | 19/19 PASS |
| Viewport rendering | Chromium simulation at 834×1194, 1194×834, 768×1024, 390×844, 1440×900 | PASS |
| All-page overflow | 11 page sections × 4 profiles | 44/44; 0 overflow |
| Python suite | `PYTHON_TEST_SHARDS_v2.95.53.md` | 91/91 terminal; 705 PASS / 1 accepted skip |
| Node suite | 40 scripts under `tools/tests/*.mjs` | 40/40 PASS |

Detailed test inventory and outcomes are in `PYTHON_TEST_SHARDS_v2.95.53.md` / `.json`. Exact source and package hashes are in `PACKAGE_VERIFICATION_v2.95.53.md`.
