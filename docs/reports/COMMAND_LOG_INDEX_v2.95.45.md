# Test & Command Log — v2.95.45

Date: 2026-11-23 (Asia/Ho_Chi_Minh)
Source baseline: released v2.95.44 FullSource; merged source candidate: v2.95.45.

## Completed commands

```bash
python -m compileall -q tools
python tools/sync-version.py --check
python tools/validate-data.py
python tools/validate-learning-content.py
python tools/audit-repository-integrity.py
node --check <18 assets/**/*.js|mjs files>
node --check sw.js
node tools/tests/<each of 39 *.mjs files>
python -m unittest discover -s tools/tests -p 'test_related_glossary_merge_038.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_037.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_036.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_035.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_034.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_027.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_candidate_audit.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_quality_audit.py' -v
python -m unittest discover -s tools/tests -p 'test_related_glossary_backlog.py' -v
python -m unittest discover -s tools/tests -p 'test_vocabulary_relationship_graph_audit.py' -v
python -m unittest discover -s tools/tests -p 'test_project_progress.py' -v
python -m unittest discover -s tools/tests -p 'test_major_release_quality_audit_025.py' -v
python -m unittest discover -s tools/tests -p 'test_patch_related_terms.py' -v
python -m unittest discover -s tools/tests -p 'test_patch_data.py' -v
python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v
python -m unittest discover -s tools/tests -p 'test_python_test_shard_runner.py' -v
python -m unittest discover -s tools/tests -p 'test_release_acceptance_runner.py' -v
python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v
python -m unittest discover -s tools/tests -p 'test_vocabulary_detail_examples.py' -v
```

The module-focused runs above yielded 283 passing test methods and one environment-dependent skip across 35 distinct modules. A separate broad shard pass observed 17/88 modules PASS before the outer execution limit interrupted further work. See `PYTHON_TEST_SHARDS_v2.95.45.md` and `RELEASE_ACCEPTANCE_v2.95.45.md`.

## Commands attempted but incomplete

```bash
python tools/run-release-acceptance.py --timeout 1800
python tools/run-python-tests-sharded.py --version 2.95.45 --timeout-per-module 120 --split-large-modules --only <first 22 modules>
```

The orchestration calls were terminated by the outer execution time limit while larger aggregate/editorial-review work remained. The tool did not report a completed full-suite status; these commands are not PASS.

## Regenerated reports

- Project Progress Snapshot v2.95.45
- Related Glossary Candidate Audit / Backlog / Quality Flags
- Vocabulary Relationship Graph Audit
- Major Release Quality Audit
- TOEIC Content Coverage
- Listening Readiness / Question Evidence / Distractor Audit
- Learning Outcome Evidence Matrix
- Foundation A2 Assessment Quality
