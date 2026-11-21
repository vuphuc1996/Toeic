# Test Report — TOEIC Dictionary v2.95.18

## Scope

Source-checked US IPA backfill for 13 existing headwords; stable-ID protection; batch provenance; version alignment; progress report; CI registration; no UI/layout changes.

## Focused Python regression

| Module | Result |
|---|---:|
| `test_ipa_backfill_batch_024.py` | 6/6 PASS |
| `test_project_progress.py` | 4/4 PASS |
| `test_ci_coverage.py` | 3/3 PASS |
| `test_package_source.py` | 3/3 PASS |
| `test_baseline_ids.py` | 13/13 PASS |
| `test_patch_data.py` | 20/20 PASS |
| `test_related_glossary_batch_021.py` | 7/7 PASS |
| `test_related_glossary_batch_022.py` | 9/9 PASS |
| `test_related_glossary_batch_023.py` | 9/9 PASS |
| `test_vocabulary_detail_examples.py` | 19/19 PASS |
| `test_vocabulary_family_links.py` | 6/6 PASS |
| `test_sync_version.py` | 12/12 PASS |
| **Focused Python regression total** | **111/111 PASS** |

All Python source/test files under `tools/` also passed `py_compile`.

## JavaScript and syntax

- All **38/38** `.mjs` regression suites passed.
- All `assets/js/*.js` files passed Node syntax checks using temporary `.mjs` copies.
- `node tools/tests/vocabulary-release-integrity.mjs`: PASS as part of the 38-suite run.

## Project validators and audits

| Command / audit | Result |
|---|---|
| `python tools/sync-version.py --check` | PASS — all registered markers match 2.95.18 |
| `python tools/validate-data.py` | PASS — 1,141 records; 0 ID additions; 0 missing IDs; 0 errors; 0 warnings |
| `python tools/validate-learning-content.py` | PASS — 0 errors; 0 warnings |
| `python tools/audit-repository-integrity.py` | PASS — 390 references/data files; 0 errors; 0 optional warnings |
| `python tools/validate-part1-photo-assets.py` | PASS — 9/9 referenced photos valid |
| `python tools/audit-toeic-coverage.py` | PASS — report generated |
| `python tools/audit-question-evidence.py` | PASS — evidence report generated; review labels retained |
| `python tools/audit-distractors.py` | PASS — structural uniqueness and answer-key checks passed for 240-question audit scope |
| `python tools/audit-listening-readiness.py` | PASS — 102 eligible / 137 pending / 239 total; no reserve promotion |
| `python tools/audit-learning-outcomes.py` | PASS — 11/11 objectives, 33 outcome criteria; only 6/33 instrumented |
| `python tools/audit-objective-resources.py` | PASS — 339/339 objective-resource links |
| `python tools/sync-design-profile.py --check` | PASS — 54 design tokens and 406 legacy font-floor selector groups synchronized |
| `python tools/audit-design-tokens.py` | PASS — 0 new violations; 2,778 inherited baseline findings remain warnings |
| `python tools/report-project-progress.py` | PASS — snapshot generated |

## Incomplete test runs / limits

- `python -m unittest discover -s tools/tests -p 'test_*.py' -v` did not finish within the local execution time limit. It is **not** reported as a full-suite pass.
- `test_validator.py` passed the cases emitted before the local timeout, but the module did not complete; therefore it is **not** reported as PASS. The actual `validate-data.py` CLI did pass.
- An earlier run of `test_patch_data.py` lacked a `.git` directory and failed its `git check-ignore` prerequisite. After initializing the local repository, a separate full run passed 20/20.

## Release ZIP validation

- `tools/package_source.py 2.95.18 ...` — PASS.
- Archive contains **382 source/data/documentation files** under exactly one root: `Toeic_Dictionary_v2.95.18/`.
- Archive size: **3,806,760 bytes** (~3.81 MB).
- Excluded-path check: 0 `.git`, log, cache, nested ZIP/bundle or release/archive directory entries.
- The package is generated from a clean committed Git tree; generated local audit logs and Python caches are excluded.

## Not verified

- Remote GitHub Actions and GitHub Pages deployment/cache.
- Real browser/PWA install, offline update, cross-tab update and desktop/mobile layout acceptance.
- Physical iOS/Android SpeechSynthesis output.
- Owner-run manual acceptance checklist (22 items; still unchecked).
- Independent phonetic/lexical editorial approval.
- No GitHub push or deployment was performed from this workspace.
