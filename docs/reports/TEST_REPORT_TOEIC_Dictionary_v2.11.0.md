# Test Report — TOEIC Dictionary v2.11.0

**Release:** v2.11.0 — TOEIC-first coverage expansion & content QA pipeline  
**Initial build:** 2026-11-09  
**Final extracted verification:** 2026-11-10  
**Base:** v2.10.2 ZIP  
**Scope:** TOEIC Listening & Reading (7 Parts) only. IELTS/Academic content remains deferred.

## Release summary

- 928 vocabulary headwords, 26 A–Z files and 928/928 stable IDs retained.
- 6 sourced US IPA values added through the guarded patch engine; IPA coverage is now 580/928.
- Listening: 22 units / 36 questions (P1=8, P2=2, P3=18, P4=8).
- Reading: 27 resources / 77 questions (P5=16, P6=12, P7=49); current passage/document count is approximately 2,080 words.
- Grammar: 25 lessons / 54 exercises.
- Per-Part local progress/accuracy summaries and Part filters are available.
- All project Markdown files are consolidated under `docs/`; `docs/MASTER_STATUS.md` remains the single source of truth.

## Automated unit tests

| Test suite | Cases | Result | Execution note |
|---|---:|---|---|
| `test_baseline_ids.py` | 13 | PASS 13/13 | Full module run |
| `test_patch_data.py` | 11 | PASS 11/11 | Full module run |
| `test_sync_version.py` | 12 | PASS 12/12 | Each test method executed independently; includes CRLF preservation. The combined module run exceeded the sandbox time limit. |
| `test_validator.py` | 33 | PASS 33/33 | Each test method executed independently because the combined process exceeded the sandbox time limit. Every case passed; no monolithic full-discovery PASS is claimed. |
| `test_learning_content.py` | 13 | PASS 13/13 | Full module run |
| **Total** | **82** | **PASS 82/82** | Baseline IDs, patch engine and learning content ran by module; sync-version and validator were run per test method. |

## Data and release validation

- `python tools/validate-data.py`: PASS — 928 records, 0 ERROR, 12 known legacy warnings; no new debt. Legacy warnings: DF005=3, EX006=1, FD001=8 violations across 7 records.
- `python tools/validate-learning-content.py`: PASS — Listening 22/36, Reading 27/77, Grammar 25/54; 0 ERROR / 0 WARNING.
- `python tools/audit-toeic-coverage.py`: PASS — report generated at `docs/reports/TOEIC_CONTENT_COVERAGE_v2.11.0.md`.
- `python tools/sync-version.py --check`: PASS — manifest, Service Worker, HTML and docs markers all 2.11.0.
- `python -m py_compile` for all five project tools: PASS.
- JavaScript syntax: PASS for `sw.js` and all `assets/js/*.js`.
- Workflow YAML parse: PASS.
- HTML parse: 206 unique IDs, no duplicates.
- Service Worker app shell: 73 resources (46 required + 27 optional), 0 missing files.
- Vocabulary ID set: 928/928 retained; no new headwords or ID changes in this release.
- Final ZIP integrity (`testzip`): PASS. All 136 archived files were compared byte-for-byte with the clean extracted release tree; no missing, modified or unarchived project files. Python `__pycache__` artifacts generated during verification were excluded from the release package.
- Final extracted-package recheck on 2026-11-10: both validators and version sync PASS against the extracted archive; HTML has 206 unique IDs; APP_SHELL has 73 resources with 0 missing; 29 Markdown files are under `docs/` and none remain outside it.

## Editorial QA and answer distribution

- Part 1 now uses explanations that name the actual correct answer letter. The validator checks this relationship against `answerIndex`.
- Part 6 training blank 3 was rewritten as a grammatical phrase-completion item (`as early as possible`); customer-service tense was corrected to `was being shipped`.
- Newly-authored P5/P6/P7 and Grammar answer keys were distributed across A–D. New P5: 4/4/4/4; new P6: 4/3/2/3; new P7: 5/4/4/4; new Grammar exercises are round-robin balanced.
- Legacy answer order was not reshuffled, avoiding a mismatch with any existing local progress stored by question ID / choice index. As a result, the aggregate legacy P2 and several P3/P4/Part7 distributions remain uneven and are recorded in the coverage report.

## Known limitations — not passed off as complete

- Part 1 visuals are original SVG illustrations, not realistic photographs. Replace or supplement with suitable original/licensed photo-quality assets in a later TOEIC batch.
- Audio is browser SpeechSynthesis using voices supplied by the operating system/browser; it is not studio-recorded native-speaker or ETS audio.
- The bank is not yet sufficient for a complete 100-question Listening + 100-question Reading form: current pool is 36 Listening and 77 Reading questions.
- There is no full 200-question, 120-minute exam engine or validated TOEIC score-equating model. Current Part accuracy is a local practice indicator, not an ETS score prediction.
- Physical iPhone Safari, Android Chrome and desktop visual/TTS QA have not been performed in this environment.
- Remote GitHub Actions and GitHub Pages production deployment have not been run or confirmed.

## Final status

**Release candidate package is locally validated.** Do not mark Phase 5 complete, claim production deployment, claim authentic ETS material, or enable IELTS scope until the remaining acceptance gates in `docs/MASTER_STATUS.md` are met and the user approves the transition.
