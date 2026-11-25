# Command log — v2.95.54 independent audit Stage 1

All commands below ran from `Toeic_Dictionary_v2.95.53/` unless stated otherwise.

| # | Command | Result | Exit | Time / evidence |
|---:|---|---|---:|---|
| 1 | `python tools/patch-data.py --patch patches/v2.95.54/independent-audit-stage-1-data.json --dry-run` | Guarded 9 operations / 9 files | 0 | Output saved in development execution transcript |
| 2 | `python tools/patch-data.py --patch patches/v2.95.54/independent-audit-stage-1-data.json --apply` | Applied 9 operations; audit log written | 0 | Exact old-value and ID-set preconditions passed |
| 3 | `python -m unittest discover -s tools/tests -p 'test_editorial_review_queue.py' -v` | 8/8 PASS | 0 | 0.953 s unittest time |
| 4 | `python -m unittest discover -s tools/tests -p 'test_validator.py' -k verb_forms -v` | 4/4 PASS | 0 | 6.251 s unittest time |
| 5 | `python -m unittest discover -s tools/tests -p 'test_validator.py' -k word_cefr -v` | 2/2 PASS | 0 | 2.911 s unittest time |
| 6 | `python -m unittest discover -s tools/tests -p 'test_patch_data.py' -v` | 20/20 PASS | 0 | 15.799 s unittest time |
| 7 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_036.py' -v` | 6/6 PASS | 0 | 0.097 s unittest time |
| 8 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_037.py' -v` | 7/7 PASS | 0 | 0.096 s unittest time |
| 9 | `python -m unittest discover -s tools/tests -p 'test_related_glossary_merge_038.py' -v` | 8/8 PASS | 0 | 0.095 s unittest time |
| 10 | `python -m unittest discover -s tools/tests -p 'test_ci_coverage.py' -v` | 3/3 PASS | 0 | 0.003 s unittest time |
| 11 | `python -m py_compile tools/validate-data.py tools/patch-data.py tools/sync-version.py tools/tests/test_validator.py tools/tests/glossary_test_helpers.py tools/tests/test_related_glossary_batch_036.py tools/tests/test_related_glossary_batch_037.py tools/tests/test_related_glossary_merge_038.py` | PASS | 0 | Syntax validation |
| 12 | `python tools/validate-data.py` | 1,141 records; 0 ERROR / 0 WARNING; 0 ID additions/removals | 0 | ID-set SHA-256 preserved |
| 13 | `python tools/sync-version.py --check` | All markers synchronized to 2.95.54 | 0 | 13 markers + changelog |
| 14 | `python -m unittest discover -s tools/tests -v` (local reconstructed Git clone) | 711/711 PASS; 0 failures/errors/skips | 0 | 135.824 s unittest runtime; final verified log attached |
| 15 | `python -m unittest discover -s tools/tests -v` (extracted final FullSource; no `.git`) | 710 PASS / 1 accepted SKIP; 0 FAIL / 0 ERROR | 0 | 135.701 s; skip is the Git-metadata-dependent `.gitignore` test |
| 16 | `node --check sw.js` + `node --check` each `assets/js/*.js` via `.mjs` temp copy | PASS | 0 | Node v22.16.0 |
| 17 | `for f in tools/tests/*.mjs; do node "$f"; done` | 40/40 scripts PASS | 0 | Full output in `TOEIC_Dictionary_v2.95.54_Node_Regression.log` |
| 18 | `python tools/validate-data.py` on extracted FullSource | 1,141 records; 0 ERROR / 0 WARNING | 0 | `TOEIC_Dictionary_v2.95.54_CleanArchive_Data_Validator.log` |
| 19 | `python tools/sync-version.py --check` on extracted FullSource | all 13 markers + changelog PASS | 0 | `TOEIC_Dictionary_v2.95.54_CleanArchive_Version_Sync.log` |

## Initial full-discovery finding and resolution

The first discovery pass surfaced four failures: the exact allowlist order in the new patch, plus three historical glossary byte-hash assertions. The patch allowlist was sorted to the exact set of operation paths. The historical tests were updated to reconstruct the pre-v2.95.54 vocabulary snapshot by reversing only the new patch's `expect.old` values in memory, preserving their original hash assertions and learning-bank byte checks. All affected modules were rerun independently and the final full discovery then passed.

## Commit discipline

Each remediation task has a separate local commit. The initial commit is a reconstructed baseline from the supplied archive because the archive contained no upstream `.git` directory; hashes below are local development commits, not GitHub commits.

## Local Git commits (reconstructed from the archive)

- `15f45356fcc37fe003c7daa477c07313d76c1f91` — imported v2.95.53 source baseline (archive had no `.git`).
- `2225db82f110c9985c1190176e5d5c6b3f40de31` — guarded appliance verb-form + CEFR data correction patch.
- `89ead49d8fadab9f5f93475c3aa3178e11e41338` — VF003 / CE004 validator rules and focused tests.
- `810a78b0e2378bb49e8e690ff1024886c939789a` — CI full discovery step and legacy note relocation.
- `a0c7a0b813d224f48044f5a6113f653a938df85a` — manifest CEFR count synchronization.
- `934121a2d23d33815b3a00019083728d2157a335` — exact patch allowlist canonicalization.
- `f728a1d0d91a437af89e4cfc6831e171712ea2fd` — historical snapshot reconstruction tests.
- `5f11b87019638dfa2af99ca2deb1ba7b122cf236` — release documentation and reports.
- `27a672f6f8689c43f68f418f949a40aac0f40b6b` — package verification and release acceptance.
- `eac47347d47ef81fcf182b649468970628e70951` — Node 22 regression evidence.
- `bdfc129fd2da2d03b76a95711fbf82e3284db442` — commit ledger and raw-log references.
- `51e1f682fcf0f94ebe4aa66824479e716ffb1114` — clean FullSource archive test results and accepted Git skip.

Full raw logs are provided separately as `TOEIC_Dictionary_v2.95.54_Full_Unittest_Discover.log`, `TOEIC_Dictionary_v2.95.54_Node_Regression.log`, `TOEIC_Dictionary_v2.95.54_Data_Validator.log`, and `TOEIC_Dictionary_v2.95.54_Version_Sync.log`, `TOEIC_Dictionary_v2.95.54_CleanArchive_Unittest.log`, `TOEIC_Dictionary_v2.95.54_CleanArchive_Data_Validator.log`, and `TOEIC_Dictionary_v2.95.54_CleanArchive_Version_Sync.log`.
