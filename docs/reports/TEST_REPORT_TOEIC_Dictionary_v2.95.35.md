# Test Report — TOEIC Dictionary v2.95.35

## Scope
- Related Glossary canonical provenance recovery batch 031.
- 155 single-sense rows received canonical sense index `0` (228 total exact single-sense rows now indexed).
- 37 rows received source-headword/source-release metadata; 6 rows also received canonical POS.
- 165 unique glossary rows changed; no terms added/deleted and no existing definitions or Vietnamese meanings overwritten.
- New helper is idempotent and does not combine definitions from multiple canonical senses.

## Verified
- Related Glossary focused regression group: **79/79 PASS**.
- New exact-match enrichment tests: **5/5 PASS** (included in the 79 focused tests).
- CI coverage checks: **3/3 PASS**, including invocation coverage for every Python test module.
- JavaScript regression suites: **39/39 PASS**.
- Vocabulary validator: **PASS**, 1,141 records, 0 errors, 0 warnings.
- Learning-content validator: **PASS**, 0 errors, 0 warnings (Listening 129/263; Reading 73/287; Grammar 58/169; Part 5 80 practice-only).
- Repository integrity preflight: **PASS**, 406 references/data files, 0 errors, 0 optional warnings.
- Version synchronization: **PASS**.
- Glossary audit: 519 entries; 156 missing definitions; 73 placeholder definitions; 223 missing POS; 75 audit missing-source flags; 0 duplicate normalized terms. Flag counts overlap.

## Incomplete / not verified
- Full Python unittest discovery was attempted but exceeded the 180-second runtime limit. The first attempt exposed a CI-coverage assertion that was fixed; focused CI coverage and glossary suites pass afterward, but the entire Python suite has not been rerun to completion after those fixes.
- Remote GitHub Actions, GitHub Pages deployment, browser/device acceptance, and independent editorial review were not run.


## Packaging
- FullSource: 535 files, CRC verified, one archive root.
- Update Patch: 26 entries (18 changed + 8 added), 0 deletions.
- Patch replay on v2.95.34 baseline: 535/535 files byte-identical to FullSource.
- ZIP CRC and SHA-256 verified.
