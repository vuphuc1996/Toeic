# Test & Release Report — TOEIC Dictionary v2.95.34

## Scope

Batch 030: fill missing English definitions and POS in the Related Glossary for exact canonical vocabulary headwords with a single canonical sense. Source definition/POS are copied verbatim. No guesswork or external paraphrasing. Existing Vietnamese meanings, all 519 glossary rows, normalized identities, canonical vocabulary IDs, relation arrays, learner progress/IndexedDB and question content are preserved.


## Data delta

- Terms improved: **73**.
- English definitions missing: **229 → 156** (−73).
- POS populated for those same 73 terms.
- Placeholder definitions: **73**, unchanged.
- Related Glossary: **519** terms; duplicate normalized term groups: **0**.
- Current read-only quality snapshot: **233** flagged (229 High, 2 Medium, 2 Low). Flags overlap by row; priority counts do not.
- Vocabulary canonical IDs/headwords: **1,141**, unchanged.


## Automated verification

| Check | Result |
|---|---|
| Full Python unittest discovery | **592 PASS, 1 SKIP** (skip: gitignore assertion requires `.git` metadata, unavailable in source ZIP) |
| Batch 030 focused | 3/3 PASS |
| Backfill 025 compatibility suite | 6/6 PASS |
| Related-glossary candidate audit suite | 4/4 PASS |
| Major release quality audit suite | 8/8 PASS |
| Related-glossary quality audit suite | 11/11 PASS |
| CI coverage registration | 3/3 PASS |
| JavaScript regression suites | **39/39 PASS** |
| JavaScript syntax checks | PASS (`sw.js` and `assets/js/*.js`) |
| Vocabulary validation | PASS — 0 errors, 0 warnings (legacy warnings: 0) |
| Learning-content validation | PASS — 0 errors, 0 warnings |
| Repository integrity preflight | PASS — 406 files checked, 0 errors, 0 optional warnings |
| Version synchronization | PASS — all markers 2.95.34 |
| ZIP CRC / root / SHA | See package verification section below |


## Reproduction steps

1. Run `python -m unittest discover -s tools/tests -p 'test_*.py' -v` — expected: 592 tests pass; one Git metadata-dependent test is skipped in the extracted source archive.
2. Run `python tools/validate-data.py` — expected: 1,141 vocabulary records, zero errors/warnings.
3. Run `python tools/validate-learning-content.py` — expected: zero errors/warnings.
4. Run `python tools/audit-repository-integrity.py` — expected: 406 local references/data files, zero errors/warnings.
5. Run `python tools/sync-version.py --check` — expected: every version marker 2.95.34.
6. Run `node --check sw.js` and syntax checks for `assets/js/*.js`.
7. Execute the 39 `.mjs` regressions listed in `.github/workflows/validate-data.yml` — expected: all PASS.


## Not performed

- GitHub Actions remote run / Pages deployment.
- Browser/device smoke test, including real iOS/Android.
- Independent editorial verification of the remaining 156 missing definitions or 73 placeholder definitions.


## Package verification

- FullSource: `TOEIC_Dictionary_v2.95.34_FullSource.zip` — 527 files.
- Update Patch: `TOEIC_Dictionary_v2.95.34_Update_Patch.zip` — 24 entries (15 changed + 9 added), 0 deletions.
- Patch replay from v2.95.33 FullSource matched v2.95.34 FullSource **527/527 files byte-for-byte**.
- ZIP CRC, single-root structure, excluded-path policy and SHA-256 checks: **PASS**.
- SHA-256 hashes are stored in the external release manifest `TOEIC_Dictionary_v2.95.34_SHA256SUMS.txt` (not embedded in the source archive, avoiding a self-referential hash).
