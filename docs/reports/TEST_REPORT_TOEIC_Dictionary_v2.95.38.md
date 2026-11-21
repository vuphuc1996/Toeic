# Test Report — TOEIC Dictionary v2.95.38

## Scope
- Fixed related-term explanation context filtering by relation type: synonym questions show synonym source references only; antonym questions show antonym references only.
- Glossary alias explanations now display POS and English definition when available alongside Vietnamese meaning.
- Added `test_related_term_explanation_context.py` (3 tests), registered in workflow syntax compilation and explicit test execution.

## Verification
- Focused Python tests: **76 test executions (73 unique tests; 3 repeat executions)** across 14 distinct suites (new explanation context, choice identity/history, practice fallback, CI coverage/repository integrity, and related-glossary batches 021/022/023/026/027/028/030/032).
- New feature tests: **3/3 PASS**.
- JavaScript regression files: **39/39 PASS**.
- `tools/validate-data.py`: PASS, 1,141 headwords, 0 errors/0 warnings; no IDs added or removed.
- `tools/validate-learning-content.py`: PASS, 0 errors/0 warnings.
- `tools/audit-repository-integrity.py`: PASS, 408 local references/data files inspected, 0 errors/optional warnings.
- `tools/sync-version.py --check`: PASS.

## Package verification
- FullSource: **559 files**.
- Patch: **12 files (9 changed + 3 added), 0 deleted**.
- Replay onto v2.95.37: **559/559 byte-for-byte match**.
- ZIP CRC, single root, excluded-path check and SHA-256: PASS.

## Not verified
- Full Python unittest discovery not run in this release.
- Remote GitHub Actions, Pages deployment, real browser/device acceptance not run.

## Data safety
No vocabulary meanings, relation arrays, question/answer keys, learner progress, IndexedDB schema or UI layout were changed.
