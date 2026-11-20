# Test Report — TOEIC Dictionary v2.95.15 candidate

## Scope

Local candidate based on v2.95.14 (`e269173`). This release adds four related-term glosses and test/metadata coverage. It does not change canonical headwords, IDs, topics, relationship arrays or learner data.

## Data and content validation

- Canonical vocabulary: **1,141 records**; stable ID additions 0 / missing 0; SHA-256 set `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.
- Glossary: **387 entries**; exact term join 376/804 glossed, 428/804 still unglossed; 465/1,037 relationship occurrences still unglossed.
- `python tools/validate-data.py`: PASS; 0 errors, 0 new warnings (0 legacy baseline warnings); informational `syn/ant chưa có nghĩa=321/804` uses a different legacy counting rule.
- `python tools/validate-learning-content.py`: PASS; Listening 121/239, Reading 65/263, Grammar 50/137, separate Part 5 practice 80; 0 errors / 0 warnings.
- `python tools/audit-repository-integrity.py`: PASS; 384 local references/data files, 0 errors / 0 optional warnings.
- `python tools/sync-version.py --check`: PASS; manifest/app/Service Worker/HTML/README/CURRENT_VERSION/Master/Changelog markers synchronized to 2.95.15.

## Focused Python regression

| Test module | Cases | Result |
|---|---:|---|
| `test_related_glossary_batch_022.py` | 9 | PASS |
| `test_related_glossary_batch_021.py` | 7 | PASS |
| `test_patch_related_terms.py` | 11 | PASS |
| `test_ci_coverage.py` | 3 | PASS |
| `test_release_rotation.py` | 6 | PASS |
| **Total** | **36** | **PASS** |

The complete Python test inventory was not run to completion and is not claimed as PASS.

## JavaScript and syntax regression

- All **38/38 `.mjs` suites** exited 0, including the updated vocabulary release-integrity test.
- `node --check sw.js` and `node --check` for every `assets/js/*.js` module passed.
- `python -m compileall -q tools` passed.

One initial release-integrity run exposed a stale assertion still expecting manifest version 2.95.14. The assertion was corrected to 2.95.15 and the full 38-suite rerun passed. The failure was in test expectation maintenance, not a data/runtime regression.

## Patch safety

- Batch 022 dry-run: PASS; no target data mutation.
- Batch 022 apply: PASS; four absent-only entries added.
- Rollback was executed in a disposable workspace. The resulting file SHA-256 exactly matched the patch's `baseFileSha256`: `57c97c32c8d681ebbbb0129e9b21dc0ba3d4c7f8e12731a9d0f54d6a42b83fbc`.
- Patcher safety regression: 11/11 PASS, including rejection of existing terms, file-hash mismatch, invalid source hosts, duplicate rows and audit-write restoration.

## Not run / not verified

- Full Python discovery and every Python module as a single aggregate: NOT RUN to completion.
- Remote GitHub Actions, GitHub Pages deployment/cache, actual browser UI, PWA install/offline/reconnect/two-tab update, iOS/Android TTS and physical-device behavior: NOT VERIFIED.
- All 22 owner-run rows in `reports/MANUAL_ACCEPTANCE_CHECKLIST.md`: **Chưa kiểm**.
- New glosses are provisional and still need independent lexical review.
- No GitHub push or deployment was performed.

## Evidence

- `reports/COMMAND_LOG_INDEX_v2.95.15.md`
- `reports/CHANGE_MANIFEST_v2.95.15.md`
- `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.15.md`
- `reports/MANUAL_ACCEPTANCE_CHECKLIST.md`
- `TOEIC_v2.95.15_Test_Logs.zip`
