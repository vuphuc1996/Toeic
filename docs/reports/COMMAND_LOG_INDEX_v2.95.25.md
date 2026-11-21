# Command Log Index — v2.95.25


| Command / check | Result |
|---|---|
| `python tools/backfill-related-glossary-from-vocabulary.py --apply` | Backfilled 43 exact-match entries; 73 placeholders remain |
| Related-term Batch 028 (exact canonical senses) | Added 7 glossary entries; exact coverage 419/804 (52.1%); 385 unique terms / 386 references remain unglossed |
| `python tools/audit-major-release.py` | PASS; JSON and Markdown report generated |
| Focused Python modules (glossary/backfill, backlog, Batch 021–027, CI coverage, repository integrity) | 34 focused tests PASS (follow-up validation group) |
| `python -m unittest discover -s tools/tests -p 'test_sync_version.py' -v` | 12/12 PASS |
| 39 `tools/tests/*.mjs` suites | 39/39 PASS |
| `node --check assets/js/*.js` and `node --check sw.js` | PASS |
| Changed scripts/tests `py_compile` | PASS |
| `python tools/validate-data.py` | PASS; 1,141 records; 0 errors/warnings; stable ID set unchanged |
| `python tools/validate-learning-content.py` | PASS; 0 errors/warnings |
| `python tools/audit-repository-integrity.py` | PASS; 397 refs/data files; 0 errors/warnings |
| `python tools/audit-objective-resources.py` | PASS; 339/339 links |
| `python tools/audit-learning-outcomes.py` | PASS; 11 objectives, 33 criteria, 6 instrumented |
| `python tools/audit-question-evidence.py` | PASS; 502 questions indexed |
| `python tools/audit-distractors.py` | PASS; structural audit, 240 questions |
| `python tools/audit-listening-readiness.py` | PASS; 102 eligible / 137 pending |
| `python tools/sync-version.py --check` | PASS; all markers synchronized |


The full Python test sweep was attempted but did not complete. No remote CI, deploy or device acceptance is inferred.
