# Test Report — TOEIC Dictionary v2.95.39

## Scope

Related Glossary research Batch 033 adds eight missing synonym/antonym reference terms: ability, acceptable, action, accusation, advertise, advise, allow and announce. Each new row includes Vietnamese meaning, POS, a concise English definition paraphrased from the linked Cambridge Dictionary entry, source label and direct source URL. Existing relation arrays and canonical vocabulary are unchanged.

## Verified results

- Batch 033 patch dry-run: PASS; apply: PASS; 8 additions.
- Batch regression suites 021, 022, 023, 026, 027, 028, 030, 032 and 033: **49 tests PASS**.
- Relation-specific explanation, practice fallback, CI coverage and glossary candidate audit suites: PASS.
- JavaScript regression suites: **39/39 PASS**.
- `tools/validate-data.py`: **1,141 canonical records; 0 errors; 0 warnings**; canonical ID set unchanged.
- `tools/validate-learning-content.py`: **0 errors; 0 warnings**; Listening 145 units / 295 questions; Reading 73 / 287; Grammar 58 / 169; Part 5 curated practice 80.
- Repository integrity: **409 references/data files inspected; 0 errors; 0 optional warnings**.
- Version synchronization: PASS.
- Major release audit: PASS. Related Glossary now **527 entries**; 804 unique referenced terms; 516 covered (64.2%); 288 unique terms / 289 reference occurrences remain uncovered; 73 placeholder English definitions remain.

## Packaging verification

- FullSource: **569 files**; Update Patch: **28 files** (10 added + 18 modified, 0 deleted).
- Patch replayed against v2.95.38 and matched the complete v2.95.39 source tree byte-for-byte: **569/569 files**.
- ZIP CRC, single-root structure, exclusion rules and SHA-256 checks: PASS.
- SHA-256 values are recorded in the release checksum file.

## Not verified / limitations

- Full Python unittest discovery was attempted but exceeded the execution time limit; it is not reported as passed. Focused suites listed above completed successfully.
- Remote GitHub Actions, GitHub Pages deployment, browser/device acceptance and independent editorial review have not been run in this environment.
- Dictionary-source lookup verifies lexical reference provenance, not suitability of every sense for every TOEIC relation context. Batch 033 remains pending independent editorial review.

## Scope protection

No canonical vocabulary IDs, synonym/antonym arrays, learning questions/answers, learner progress, IndexedDB schema, Robot Buddy permissions or UI layout were changed.
