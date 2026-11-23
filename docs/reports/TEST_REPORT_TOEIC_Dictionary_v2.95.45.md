# Test Report — TOEIC Dictionary v2.95.45

Date: 2026-11-23. Baseline: released v2.95.44 FullSource. Candidate: selectively merged v2.95.45.

## Results summary

| Scope | Result | Notes |
|---|---:|---|
| Focused Python regression | **283 PASS / 1 SKIP** | 284 cases across 35 distinct modules; one `.git`-metadata-dependent assertion skipped because the source was extracted from ZIP |
| JavaScript regression | **39/39 PASS** | Every `tools/tests/*.mjs` suite was executed individually with Node |
| JavaScript syntax | **19/19 PASS** | 18 JS/MJS files under `assets` plus `sw.js` |
| Python compile | **PASS** | `python -m compileall -q tools` |
| Repository integrity | **PASS** | 419 local references/data files; 0 errors, 0 optional warnings |
| Data validator | **PASS** | 1,141 canonical records; 0 errors, 0 warnings; 0 ID additions/losses |
| Learning-content validator | **PASS** | 0 errors / 0 warnings |
| Version synchronization | **PASS** | 13/13 version markers |
| Batch 038 merge contract | **8/8 PASS** | Five additions, three exact-guarded sense corrections and protected-data hashes |
| Python test-shard runner | **12/12 PASS** | Includes process-group timeout termination, versioned checkpoint, resume and large-module splitting |
| Release Acceptance runner | **10/10 PASS** | Includes manifest-derived version, JSON/Markdown version consistency, timeout status and child-process-group cleanup |

The 35 focused Python modules include Batch 027, 034, 035, 036, 037 and 038; glossary candidate/quality/backlog audits; relation graph; project progress; major release audit; patch updater/data; CI coverage; baseline IDs; choice history/identity; answer-position; sync-version; vocabulary detail/examples; and both runner suites. Module-level result lists and command details are in `COMMAND_LOG_INDEX_v2.95.45.md`.

## Full Python discovery / aggregate acceptance

**INCOMPLETE — do not interpret as PASS.** The full inventory contains 88 Python test modules. A broad sharded run completed 17/88 modules (125 tests) successfully before the outer execution limit interrupted the run while larger editorial-review work remained. A separate combined `run-release-acceptance.py` invocation was also terminated by the outer execution limit before it could write a final aggregate report. Focused tests were run separately and passed as listed above; the unexecuted/unfinished modules remain unverified.

The sharded runner report is `PYTHON_TEST_SHARDS_v2.95.45.md` (17/88 PASS, 71 pending). Timeout or interruption is not converted to PASS.

## Local validators

- `python -m compileall -q tools`: exit 0.
- `python tools/sync-version.py --check`: all 13 marker locations match `data/manifest.json` v2.95.45.
- `python tools/validate-data.py`: 1,141 records, 0 ERROR, 0 WARNING; baseline ID set unchanged. Informational counters: US IPA 1,062; word family 276; verb forms 329; collocations 971; synonyms 405; antonyms 210; exact relation glossary coverage 556/804.
- `python tools/validate-learning-content.py`: Listening 145 units / 295 questions; Reading 73 / 287; Grammar 58 / 169; practice-only Part 5 80; 0 errors / 0 warnings.
- `python tools/audit-repository-integrity.py`: 419 local references/data files; 0 errors / 0 optional warnings.
- `node --check`: 19 files; all pass.
- All 39 JavaScript regression modules pass.

## Preservation and UI verification

- Every protected canonical A–Z vocabulary file and all protected learning-content JSON files are byte-identical to released v2.95.44.
- Baseline identity test: 13/13 PASS; no canonical vocabulary ID was added or lost.
- Choice history/identity and answer-position tests pass; no question/choice ID or answer-key file was modified.
- The only runtime/UI files changed are `assets/js/app.js`, `index.html` and `sw.js`, each only to increment the release/cache marker from 2.95.44 to 2.95.45. No CSS, layout, visual component, IndexedDB implementation or learner-data migration changed.

## External / manual checks not performed

- Remote GitHub Actions: not verified.
- GitHub Pages deployment, CDN/cache propagation and installed-PWA update: not verified.
- Browser and physical Android/iOS/tablet/desktop acceptance: not verified.
- Independent lexical/pedagogical review of new/corrected glossary senses: pending.

See `RELEASE_ACCEPTANCE_v2.95.45.md`, `COMPARE_MERGE_REVIEW_v2.95.45.md` and `COMMAND_LOG_INDEX_v2.95.45.md` for limitations and supporting detail.
