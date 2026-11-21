# Command Log Index — v2.95.35


## Data / enrichment
- Exact-match enrichment was applied only to complete canonical bilingual senses.
- Canonical single-sense entries receive `sourceSenseIndex: 0` when absent.
- Missing source headword/release and POS fields are filled without overwriting existing values.
- Multi-sense rows are not assigned a source sense index; their missing definitions remain editorial-review items.

## Tests and validation
- `python -m unittest discover -s tools/tests -p 'test_related_glossary*.py' -v` — 79/79 PASS.
- `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` — 3/3 PASS.
- `node tools/tests/*.mjs` (each file invoked individually) — 39/39 PASS.
- `python tools/validate-data.py` — PASS, 1,141 records, 0 errors/warnings.
- `python tools/validate-learning-content.py` — PASS, 0 errors/warnings.
- `python tools/audit-repository-integrity.py` — PASS, 406 inspected, 0 errors/warnings.
- `python tools/sync-version.py --check` — PASS.
- Full Python discovery attempted but timed out after 180 seconds; full suite status remains incomplete.

## Packaging
- FullSource: 535 source/data/docs files.
- Patch: 26 files (18 changed, 8 added, 0 deleted).
- Patch replay from v2.95.34: 535/535 packageable files byte-identical.
- ZIP CRC, single-root and SHA-256 verification passed.
