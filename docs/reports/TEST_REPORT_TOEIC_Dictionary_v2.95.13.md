# Test Report — TOEIC Dictionary v2.95.13 candidate

## Scope and baseline

- Candidate: **v2.95.13**, local source only.
- Comparison baseline: **v2.95.12**, Git commit `85be68a`.
- This is a focused source/data release report. It does not claim GitHub deployment, remote CI, browser/device acceptance or independent lexical approval.

## Change summary

- Ten existing headwords were split into more precise POS/usage senses: `bill`, `charge`, `document`, `experience`, `function`, `host`, `minute`, `offer`, `supply`, `value`.
- Added 24 sense-linked bilingual examples.
- Added four sourced Vietnamese related-term glosses: `demand`, `guest`, `inexperience`, `refund`.
- Corrected `valuable → value (n)` and `valuation → value (v)` family links.
- Multi-sense headwords: 39 → 49; examples linked to multi-sense records: 81 → 105; related glossary: 369 → 373.
- Canonical headwords remain 1,141. Stable IDs, `word` and `topics` are unchanged.
- Existing Flashcard sense renderer, Robot Buddy streaming, fixed 10-card maximum and PWA update-consent behavior are retained; no runtime behavior changed in this candidate.

## Automated test results

### Python focused unit tests

**17 modules / 175 test cases passed**, individually invoked; combined reported test runtime 54 seconds. Every listed command returned exit code 0.

| Module | Test cases | Runtime | Exit code |
|---|---:|---:|---:|
| `test_vocabulary_detail_examples.py` | 19 | 1s | 0 |
| `test_vocabulary_family_links.py` | 6 | 1s | 0 |
| `test_patch_data.py` | 20 | 17s | 0 |
| `test_patch_related_terms.py` | 11 | 10s | 0 |
| `test_ci_coverage.py` | 3 | 1s | 0 |
| `test_audit_design_tokens.py` | 8 | 1s | 0 |
| `test_learning_content.py` | 34 | 0s | 0 |
| `test_repository_integrity.py` | 1 | 2s | 0 |
| `test_design_system.py` | 19 | 1s | 0 |
| `test_responsive_layout.py` | 7 | 1s | 0 |
| `test_design_profile.py` | 6 | 2s | 0 |
| `test_sync_version.py` | 12 | 12s | 0 |
| `test_part1_photo_assets.py` | 6 | 0s | 0 |
| `test_sentence_completion.py` | 12 | 1s | 0 |
| `test_question_evidence.py` | 6 | 2s | 0 |
| `test_objective_resource_map.py` | 2 | 1s | 0 |
| `test_learning_outcomes.py` | 3 | 1s | 0 |

### JavaScript regression suites

**38/38 `.mjs` suites exited 0.** These are suite-file pass counts, not a claim about the number of assertions contained inside the files. Individual output logs are included in the test-evidence package.

### Data, repository and build checks

| Check | Result | Exit code |
|---|---|---:|
| `python tools/validate-data.py --verbose` | 1,141 records; ID additions 0 / missing 0; 0 errors / 0 legacy warnings; multi-sense 49 | 0 |
| `python tools/validate-learning-content.py` | Listening 121 units / 239 questions; Reading 65 / 263; Grammar 50 / 137; Part 5 practice 80; 0 errors / 0 warnings | 0 |
| `python tools/audit-repository-integrity.py` | 380 references/data files; 0 errors / 0 optional warnings | 0 |
| `python tools/audit-design-tokens.py` | 2,778 inherited legacy warnings; 0 new violations | 0 |
| `python tools/validate-part1-photo-assets.py` | 9/9 photo entries valid | 0 |
| `python tools/sync-version.py --check` | All release markers synchronized to v2.95.13 | 0 |
| `python -m compileall -q tools` | PASS | 0 |
| `node --check sw.js` and each `assets/js/*.js` via temporary `.mjs` check files | PASS | 0 |
| `git diff --check` | PASS | 0 |

Validator informational values (missing IPA, unglossed synonym/antonym occurrences, CEFR differences) are tracked editorial metrics, not release errors; see generated editorial coverage reports. They were not relabeled as approved content.

## Patch replay from clean baseline

Started from `git archive 85be68a` into an empty temporary directory, then ran dry-run and apply for:

1. `patches/v2.95.13/batch-001.json` — 20 operations across 10 letter files.
2. `patches/v2.95.13/batch-002-family-gloss.json` — 1 operation.
3. `patches/v2.95.13/batch-003-family-gloss.json` — 1 operation.
4. `patches-related-terms/v2.95.13/related-terms-001.json` — 4 glossary additions.

All dry-runs and applies passed. `validate-data.py` and `validate-learning-content.py` on the replay passed. The 10 changed A–Z files and `data/related-terms.json` matched the candidate byte-for-byte. The stable ID set also matched across replay and candidate (1,141 IDs).

A first targeted run of `test_vocabulary_family_links.py` detected that `valuable → value` still had the old combined Vietnamese gloss. The family-link patch was corrected; the final rerun passed 6/6, including the `valuable` and `valuation` sense/POS assertions. The initial failing run is preserved in the attached test log pack rather than omitted.

The first replay command used the unsupported option `--file` and exited 2 at argument parsing; no patch was applied. After consulting each patch tool's `--help`, the command was corrected to `--patch`; the full clean replay passed. Both the argument error and corrected run logs are included for transparency.

## Not run / not verified

- Full Python `unittest discover` aggregate and `test_validator.py` were not completed in this execution environment; they are **NOT RUN to completion**, not PASS.
- GitHub Actions on the remote repository, GitHub Pages deployment, installed PWA behavior, real-browser visuals, offline/reconnect, two-tab update behavior, iPhone/Android TTS and physical-device audio were not tested here.
- All 20 rows in `docs/reports/MANUAL_ACCEPTANCE_CHECKLIST.md` remain **Chưa kiểm**.
- New meanings/examples/glosses/family links are source-referenced but remain pending independent human lexical review.
- No GitHub push or deployment was performed.

## Evidence paths

- `TOEIC_v2.95.13_Test_Logs.zip` — per-module Python logs, JavaScript suite logs, validators, patch replay and summaries.
- `docs/reports/COMMAND_LOG_INDEX_v2.95.13.md` — concise commands, exit codes, durations and evidence locations.
- `docs/reports/CHANGE_MANIFEST_v2.95.13.md` — baseline-to-candidate scope.
- `docs/reports/MANUAL_ACCEPTANCE_CHECKLIST.md` — owner-run checks, all pending.
