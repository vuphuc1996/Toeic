# Command Log Index — v2.95.17

Local commands run from the repository root. Results below are from the current v2.95.17 workspace.

| Command / check | Result |
|---|---|
| `python tools/patch-related-terms.py --patch patches-related-terms/v2.95.17/related-terms-001.json --dry-run` | PASS; 9 absent-only operations, source URLs accepted, no data write |
| `python tools/patch-related-terms.py --patch patches-related-terms/v2.95.17/related-terms-001.json --apply` | PASS; 9 glosses applied; operation audit recorded locally under ignored `logs/` |
| Python focused tests: batches 021/022/023, patcher, package tool, CI coverage, project progress | 46/46 PASS |
| `python -m py_compile` on changed Python files | PASS |
| `node tools/tests/vocabulary-release-integrity.mjs` | PASS |
| `python tools/validate-data.py` | PASS; 1,141 records, 0 errors, 0 warnings |
| `python tools/validate-learning-content.py` | PASS; 0 errors, 0 warnings |
| `python tools/audit-repository-integrity.py` | PASS; 388 references, 0 errors, 0 optional warnings |
| `python tools/report-project-progress.py` | PASS; snapshot saved as `PROJECT_PROGRESS_SNAPSHOT_v2.95.17.md` |
| `python tools/sync-version.py --check` | PASS; all registered version markers synchronized |
| `python tools/package_source.py 2.95.17 release_v2.95.17/TOEIC_Dictionary_v2.95.17_FullSource.zip` | PASS; 369 files, exactly one root folder, zero excluded entries |

## Notes

- The first run of historical Batch 022 tests exposed an exact-total assertion pinned to 387 glossary entries. It was changed to a non-regressive minimum-size assertion; the batch's uniqueness and provenance checks remain. Batch 023 similarly uses a minimum-size guard for later expansions.
- The first CI coverage run found `test_package_source.py` was not yet registered in workflow execution. The workflow now runs that suite and includes the helper/test in Python syntax compilation; CI coverage then passed.
- These are local checks only. No remote workflow or browser/device check was executed.
