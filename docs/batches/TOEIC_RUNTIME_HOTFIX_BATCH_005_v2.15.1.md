# Batch 005 — Reading/Grammar Runtime Hotfix & CI Maintenance (v2.15.1)

## Scope

Fix the Reading detail `ReferenceError: item is not defined`, fix the same out-of-scope identifier in Grammar lesson rendering, protect Part 5 card metadata where passage text is intentionally absent, add regression tests and modernize the GitHub Actions runtime.

## Files changed

- `assets/js/app.js`
- `.github/workflows/validate-data.yml`
- `tools/tests/test_learning_detail_scope.py`
- `docs/MASTER_STATUS.md`
- `docs/CHANGELOG.md`
- `docs/README.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.15.1.md`

## Compatibility guarantees

No source vocabulary JSON, reading/listening/grammar content, stable IDs, answer keys, choice order, correct answer indices, IndexedDB object stores, schemas or existing personal progress values are modified.

## Verification

- Three new scope/card-rendering regression tests: 3/3 PASS.
- `node --check assets/js/app.js`: PASS.
- Workflow YAML parser: PASS.
- The v2.15.0 data validator snapshot passes locally (928 records, 0 errors, 12 legacy warnings).
- GitHub-hosted Actions rerun is required to verify action v7 and the pinned Ubuntu 24.04 runner remotely.
