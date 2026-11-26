# Command Log Index — v2.95.71

| Command / tool | Outcome | Evidence |
|---|---|---|
| `sha256sum TOEIC_Dictionary_v2.95.70_FullSource.zip` + `unzip -t` | PASS before editing | Baseline SHA and CRC in `versions/CURRENT_VERSION.md` |
| `python tools/patch-related-terms.py` / Batch 045 guarded application | 23 existing records enriched; no new terms/edges | `RELATED_GLOSSARY_BATCH_045_v2.95.71.md` and ledger |
| `python tools/project-progress-index.py` | PASS; index 54.47% | `PROJECT_PROGRESS_v2.95.71.md/.json` |
| `python tools/run-python-tests-sharded.py --timeout-per-module 120 --version 2.95.71` | PASS WITH SKIPS; 107/107 modules, 798 PASS, 1 approved SKIP | `PYTHON_TEST_SHARDS_v2.95.71.md/.json` |
| Execute all `tools/tests/*.mjs` | PASS; 45/45 | `NODE_TEST_REPORT_v2.95.71.md` |
| `python -m compileall -q tools` | PASS | Test report |
| `node --check assets/js/app.js && node --check sw.js` | PASS | Test report |
| `python tools/validate-data.py --json ...` | PASS; 1,141 records; +0/−0 IDs | `DATA_DIFF_v2.95.71.md` and validation JSON |
| `python tools/validate-learning-content.py` | PASS; 0 errors / 0 warnings | Test report |
| `python tools/audit-repository-integrity.py` | PASS; 409 inspected, 0 errors/warnings | Test report |
| `python tools/validate-part1-photo-assets.py` | PASS; 9/9 | Test report |
| `python tools/sync-version.py --check` | PASS; release markers/import/cache keys coherent | Test report |
| `python tools/sync-design-profile.py --check` | PASS | Test report |
| `python tools/audit-design-tokens.py` | PASS; 0 new violations; 2,773 legacy warning identities | Test report |
| `python tools/audit-related-glossary-quality.py` | PASS read-only; 119/567 flagged, 0 duplicate normalized groups | `RELATED_GLOSSARY_QUALITY_v2.95.71.md/.json` |
| `python tools/audit-word-family-graph.py` | PASS read-only; flags retained, no mutation | `WORD_FAMILY_GRAPH_AUDIT_v2.95.71.md/.json` |
| `python tools/build-related-glossary-enrichment-queue.py` | PASS read-only research queue | `RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.71.md/.json` |
| `python -m unittest discover ... test_ci_coverage.py` | 9/9 PASS | Python inventory |
| `python -m unittest discover ... test_word_family_graph_audit.py` | 1/1 PASS | Python inventory |
| `python tools/package_source.py 2.95.71 ... --repo <clean committed staging>` | PASS; FullSource 894 files, one release root | `PACKAGE_VERIFICATION_v2.95.71.md` |
| Apply Patch From v2.95.70 to a fresh clean predecessor extraction | PASS; 894/894 byte-identical, 0 extra/missing/different | `PACKAGE_VERIFICATION_v2.95.71.md` |
| `unzip -t` + external SHA-256 sidecar verification for both release ZIPs | PASS | Final package verification |

No hosted Actions run, live Pages deployment, installed-PWA/device verification or Git push was performed.
