# Command Log Index — v2.95.34


## Data and version

- `python tools/sync-version.py --set 2.95.34 --apply` — applied release markers.
- `python tools/sync-version.py --check` — PASS.
- `python tools/audit-related-glossary-quality.py --output docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.34.md --json-output docs/reports/RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.34.json` — generated read-only audit.
- `python tools/validate-data.py` — PASS, 1,141 words, 0 errors / 0 warnings.
- `python tools/validate-learning-content.py` — PASS, 0 errors / 0 warnings.
- `python tools/audit-repository-integrity.py` — PASS, 406 files, 0 errors / 0 warnings.

## Tests

- `python -m unittest discover -s tools/tests -p 'test_*.py' -v` — 592 PASS, 1 SKIP (source archive has no Git metadata).
- Focused tests: batch 030 (3/3), canonical glossary backfill compatibility (6/6), candidate audit (4/4), major-release audit (8/8), glossary quality audit (11/11), CI coverage (3/3).
- `node --check sw.js` and syntax checks for `assets/js/*.js` — PASS.
- 39 JavaScript regression `.mjs` scripts from workflow — PASS.

## Release package

FullSource 527 files; patch 24 entries (15 changed + 9 added), 0 deletions. Patch replay against v2.95.33 reproduced FullSource 527/527 files byte-for-byte. CRC, single-root and exclusion checks PASS. SHA-256 values are in the external release manifest `TOEIC_Dictionary_v2.95.34_SHA256SUMS.txt` (excluded from FullSource to avoid self-referential checksums).
