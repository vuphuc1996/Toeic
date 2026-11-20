# Test Report — TOEIC Dictionary v2.95.14 candidate

## Scope

- Candidate: **v2.95.14**, local source only.
- Baseline: v2.95.13 at commit `a04a4d97472cb856c2459aab19d2a18090204e40`.
- Change scope: ten related-term glossary additions, provenance and regression coverage, CI path-filter hardening, release metadata/docs.
- This report does not claim remote GitHub Actions, Pages deployment, browser/device acceptance or independent lexical approval.

## Change summary

- Related-term glossary increased from 373 to 383 entries.
- Added Vietnamese glosses and concise English definitions for ten existing link terms: `requirement`, `pay`, `ignore`, `withhold`, `retain`, `earnings`, `duty`, `distribute`, `discourage`, `decline`.
- Added provenance batch 021 and an absent-only patch guarded by the v2.95.13 base-file SHA-256.
- CI now executes the new focused regression and triggers when `patches-related-terms/**` changes on push or pull request.
- Canonical vocabulary remains 1,141 headwords; stable IDs, words, topics, synonym/antonym links and learner data are unchanged.

## Automated verification

### Focused Python unit tests

**5 modules / 43 test cases passed**, each command exited 0.

| Module | Cases | Result |
|---|---:|---|
| `test_related_glossary_batch_021.py` | 6 | PASS |
| `test_patch_related_terms.py` | 11 | PASS |
| `test_vocabulary_detail_examples.py` | 19 | PASS |
| `test_ci_coverage.py` | 3 | PASS |
| `test_project_progress.py` | 4 | PASS |
| **Total** | **43** | **PASS** |

The new glossary test verifies source metadata, correspondence between patch and ledger, existing synonym/antonym use, a minimum frequency of three references per term, no duplicate glossary keys and CI path-filter coverage.

### JavaScript regression

**38/38 `.mjs` test files passed** when run individually. The release-integrity test also passed after adding an explicit v2.95.14 manifest assertion and batch-021 coverage.

### Data, content and integrity checks

| Check | Result |
|---|---|
| `python tools/validate-data.py` | 1,141 records; ID additions 0 / missing 0; 0 errors / 0 warnings |
| `python tools/validate-learning-content.py` | Listening 121 units / 239 questions; Reading 65 / 263; Grammar 50 / 137; Part 5 practice 80; 0 errors / 0 warnings |
| `python tools/audit-repository-integrity.py` | 382 local references/data files; 0 errors / 0 optional warnings |
| `python tools/sync-version.py --check` | All release markers synchronized to v2.95.14 |
| `node tools/tests/vocabulary-release-integrity.mjs` | PASS; 1,141 unique records, 383 glossary entries and batch 021 verified |
| `node --check assets/js/app.js`; `node --check sw.js` | PASS |
| `python -m py_compile tools/tests/test_related_glossary_batch_021.py` | PASS |

### Patch safety and replay

The v2.95.14 patch was rollback-tested to restore the baseline glossary file hash, then dry-run and applied. Dry-run and apply both passed. The patch contains ten `expect.absent=true` operations, rejects overwrites, validates Cambridge hostname/path constraints and checks the exact base-file SHA-256. The patcher regression is 11/11 PASS.

## Editorial coverage metrics

- Current glossary count: 383.
- 804 distinct terms occur in canonical synonym/antonym fields; 372 have a matching glossary record and 432 remain unglossed.
- 477 of 1,037 synonym/antonym link occurrences remain unglossed. The ten additions resolve 33 previously unglossed occurrences.
- `validate-data.py` separately reports `syn/ant chưa có nghĩa=323/804`; this legacy informational metric uses a different counting rule and must not be conflated with the exact-term join above.
- Other editorial indicators remain: 93 missing US IPA entries, four duplicate-definition pairs and nine word/sense CEFR differences. They were not modified in this release.

## Not run / not verified

- The entire Python test inventory (57 modules) and one aggregate `unittest discover` run were not completed; only the five focused modules listed above were run for this candidate.
- The GitHub Actions workflow itself was not run remotely. Local checks of the workflow definition do not equal a remote CI result.
- GitHub Pages deployment, `/Toeic/` path, PWA installation, offline/reconnect, two-tab update, actual desktop/mobile rendering, iPhone/Android TTS and device audio remain unverified.
- All **21** owner-run checks in `reports/MANUAL_ACCEPTANCE_CHECKLIST.md` remain **Chưa kiểm**.
- New glossary entries remain provisional pending independent lexical review.
- No GitHub push or deployment was performed.

## Evidence files

- `reports/COMMAND_LOG_INDEX_v2.95.14.md`
- `reports/CHANGE_MANIFEST_v2.95.14.md`
- `reports/VOCABULARY_GLOSSARY_EXPANSION_v2.95.14.md`
- `reports/MANUAL_ACCEPTANCE_CHECKLIST.md`
- Test logs distributed with `TOEIC_v2.95.14_Test_Logs.zip`.
