# Command Log Index — v2.95.72

| Command / tool | Outcome | Evidence |
|---|---|---|
| `python tools/sync-version.py --set 2.95.72 --apply` | PASS; all 18 release markers, app imports, and SW precache keys synchronized | Test report and `sync-version.py --check` |
| `python tools/audit-repository-integrity.py` | PASS; 411 references/data files inspected; 0 errors/warnings | Test report |
| `python tools/validate-data.py` | PASS; 1,181 canonical records; IDs +0/−0; 0 errors, 0 legacy warnings | Test report |
| `python tools/validate-learning-content.py` | PASS; 0 errors, 0 warnings | Test report |
| `python tools/validate-part1-photo-assets.py` | PASS; 9/9 valid | Test report |
| `python tools/sync-design-profile.py --check` | PASS | Test report |
| `python tools/audit-design-tokens.py` | PASS; 0 new violations; 2,773 legacy warning identities | Test report |
| `python tools/audit-word-family-graph.py` | PASS; 50 missing targets remaining (−40) | `WORD_FAMILY_GRAPH_AUDIT_v2.95.72.md/.json` |
| `python tools/audit-related-glossary-quality.py` | PASS; 567 entries, 54 flagged, 0 duplicate normalized groups | `RELATED_GLOSSARY_QUALITY_v2.95.72.md/.json` |
| `python tools/project-progress-index.py` | PASS; weighted index **55.88%** | `PROJECT_PROGRESS_v2.95.72.md/.json` |
| `python tools/audit-major-release.py` | PASS | `MAJOR_RELEASE_QUALITY_AUDIT_v2.95.72.md/.json`, `LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.72.md` |
| `python tools/run-python-tests-sharded.py --timeout-per-module 120 --version 2.95.72` | PASS; 106/109 modules pass (1 pass with skips, 0 fail/error) | Python inventory report |
| Node regression test suite (`tools/tests/*.mjs`) | PASS; 45/45 scripts PASS | `NODE_TEST_REPORT_v2.95.72.md` |
| `compile_applet` & `lint_applet` | PASS | Build succeeded, linting completed successfully |

No hosted Actions run, live Pages deployment, installed-PWA/device verification or Git push was performed.
