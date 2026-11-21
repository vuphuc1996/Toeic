# Test Report — TOEIC Dictionary v2.95.28

## Scope
- Baseline: v2.95.27 FullSource.
- Added read-only cross-file vocabulary relationship graph audit.
- No canonical vocabulary, synonym/antonym arrays, learning questions/answers, learner records, IndexedDB, runtime behavior, or UI changes.

## Relationship graph audit snapshot
- Canonical headword records: 1,141; normalized unique: 1,141; duplicate groups: 0.
- Relation references: 1,037 (814 synonym, 223 antonym).
- Targets absent from canonical headwords: 673 reference occurrences; 376 are present in related glossary; 297 occurrences / 296 unique terms are absent from both canonical vocabulary and related glossary and require editorial review.
- Self references: 0; malformed relation structures: 0.
- Non-reciprocal references: 248 review flags only; no automatic edits or assumptions because relations may be sense-specific.

## Tests executed
- New relationship graph audit unit tests: 8/8 PASS.
- Related glossary quality audit: 9/9 PASS.
- Related glossary candidate audit: 4/4 PASS.
- Related glossary batch 028: 4/4 PASS.
- Related glossary backfill 025: 6/6 PASS.
- Major release quality audit 025: 8/8 PASS.
- Focused Python tests total: 39/39 PASS.
- JavaScript `.mjs` suites: 39/39 PASS.
- Python compile checks for new tool/tests: PASS.
- Vocabulary data validation: 1,141 records; 0 errors, 0 warnings (legacy warning category only).
- Learning-content validation: 0 errors, 0 warnings.
- Repository integrity: 401 local references/data files inspected; 0 errors, 0 optional warnings.
- Version synchronization: PASS.

## Not verified
- Full Python unittest discovery.
- Remote GitHub Actions, GitHub Pages deployment, or browser/device acceptance.
- Relationship review flags are not correctness verdicts; manual semantic review remains required.

## Release package integrity
- FullSource: 475 source/data/docs files, ZIP CRC PASS, single root `TOEIC_Dictionary_v2.95.28/`.
- Patch: 15 changed/added files, 0 deletions; ZIP CRC PASS, single root.
- Patch replay on v2.95.27 baseline: all 475 target files compared byte-for-byte; PASS.
- SHA-256 recorded in `TOEIC_Dictionary_v2.95.28_SHA256SUMS.txt`.
