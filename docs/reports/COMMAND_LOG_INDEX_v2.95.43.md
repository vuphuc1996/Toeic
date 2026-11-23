# Command Log Index — v2.95.43


## Batch/data application

- `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.43/related-terms-036.json --dry-run` — PASS, 11 guarded additions; no writes to canonical vocabulary.
- `python tools/patch-related-terms.py --root . --patch patches-related-terms/v2.95.43/related-terms-036.json --apply` — PASS, 11 rows added; updater audit log written under excluded `logs/`.

## Regression commands

- `python -m unittest discover -s tools/tests -p 'test_related_glossary*.py' -v` — PASS 104/104 (rerun after reconciling stale Batch 027 and 034 historical expectations).
- `python -m unittest discover -s tools/tests -p 'test_patch_related_terms.py' -v` — PASS 11/11.
- `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` — PASS 3/3.
- `python -m unittest discover -s tools/tests -p 'test_major_release_quality_audit_025.py' -v` — PASS 8/8.
- `python -m unittest discover -s tools/tests -p 'test_related_term_explanation_context.py' -v` — PASS 3/3.
- `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` — PASS 12/12.
- `python -m unittest discover -s tools/tests -p 'test_package_source.py' -v` — PASS 3/3.
- `python -m compileall -q tools` — PASS.
- Each `tools/tests/*.mjs` executed with Node — PASS 39/39 suites.

## Data and audit commands

- `python tools/validate-data.py` — PASS, 1,141 records; 0 IDs added/lost; 0 errors/0 warnings.
- `python tools/validate-learning-content.py` — PASS, 0 errors/0 warnings.
- `python tools/audit-repository-integrity.py` — PASS, 413 references/data files; 0 errors/optional warnings.
- `python tools/sync-version.py --check` — PASS, all registered release markers synchronized to 2.95.43.
- `python tools/audit-related-glossary-candidates.py --output docs/reports/RELATED_GLOSSARY_CANDIDATE_AUDIT_v2.95.43.md` — PASS; 546/535/269.
- `python tools/build-related-glossary-backlog.py` — PASS; 269 unique missing / 270 occurrences.
- `python tools/audit-related-glossary-quality.py --output ... --json-output ...` — PASS; report generated.
- `python tools/audit-vocabulary-relationship-graph.py --output ... --json-output ...` — PASS; report generated.
- `python tools/audit-major-release.py` — PASS; current Major Release Audit and Outcome Evidence Matrix generated.
- `python tools/audit-toeic-coverage.py` — PASS; current content coverage generated.
- `python tools/report-project-progress.py` — PASS; current snapshot generated.

## Incomplete

- `python -m unittest discover -s tools/tests -p 'test_*.py' -v` — started but terminated by runtime time limit before aggregate summary. Partial output is not a full-suite result.
- Remote Actions, Pages deployment and browser/device acceptance were not executed.


## Packaging/replay

- `python tools/package_source.py 2.95.43 ...FullSource.zip` — PASS, 641 files.
- ZIP CRC/root/exclusion validation — PASS; single root `Toeic_Dictionary_v2.95.43/`.
- Generated overlay Patch: 39 files (18 modified + 21 added; 0 deletions).
- Replay against v2.95.42 Full Source — PASS, 641/641 exact; 0 missing, extra or mismatched files.
- SHA-256 sidecars created and verified for both archives.
