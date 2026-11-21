# Command Log Index — v2.95.28


## Validation and audit
- `python -m py_compile tools/audit-vocabulary-relationship-graph.py tools/tests/test_vocabulary_relationship_graph_audit.py` — PASS.
- `python -m unittest discover -s tools/tests -p 'test_vocabulary_relationship_graph_audit.py' -v` — 8/8 PASS.
- Related glossary quality audit tests — 9/9 PASS.
- Related glossary candidate audit tests — 4/4 PASS.
- Related glossary batch 028 tests — 4/4 PASS.
- Related glossary backfill 025 tests — 6/6 PASS.
- Major release quality audit 025 tests — 8/8 PASS.
- All `.mjs` regression suites — 39/39 PASS.
- `python tools/validate-data.py` — 1,141 records, 0 errors, 0 warnings.
- `python tools/validate-learning-content.py` — 0 errors, 0 warnings.
- `python tools/audit-repository-integrity.py` — 401 items inspected, 0 errors, 0 optional warnings.
- `python tools/sync-version.py --check` — PASS.

## Packaging
- FullSource and Patch ZIP CRC checks — PASS.
- Patch replay from v2.95.27 baseline, byte comparison across 474 files — PASS.
- SHA-256 — recorded and independently rechecked.

## Limits
Full Python discovery, remote CI, Pages deployment and real-device/browser QA were not performed.
