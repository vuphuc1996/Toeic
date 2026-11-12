# Test report — TOEIC Dictionary v2.12.0

- **Date:** 2026-11-10
- **Status:** Release candidate package verified locally. ZIP CRC, clean extraction, exact archive/tree comparison and repeated extracted-package validators passed.
- **Baseline:** v2.11.0.

## Content totals

| Content | v2.11.0 | v2.12.0 |
|---|---:|---:|
| Vocabulary records | 928 | 928 |
| Listening questions | 36 | 102 |
| Reading questions | 77 | 109 |
| Grammar exercises | 54 | 54 |

Listening per Part: P1=8, P2=25, P3=39, P4=30. Reading per Part: P5=30, P6=16, P7=63; Part 7 split: 38 single-passage / 25 multiple-passage.

## Validation gates

- Vocabulary data validator: **PASS** — 928 records, 0 ERROR, 12 known legacy warnings (DF005=3, EX006=1, FD001=8 across 7 records); no new validator debt.
- Learning-content validator: **PASS** — 0 ERROR / 0 WARNING; checks one-form pool thresholds, Part 2/3/4 item structure and speaker rules, P7 multi-document structure and all answer choice bounds.
- Version synchronization: **PASS** — manifest, Service Worker, UI markers and documentation agree at 2.12.0.
- Unit tests: **86/86 PASS** — baseline IDs 13/13 (module), patch engine 11/11 (module), version sync 12/12 (each test method isolated), data validator 33/33 (each test method isolated), learning content 17/17 (module). Full-module execution for the two slower suites timed out in the Python 3.13 sandbox, so their individual methods were run and passed; no claim is made that one monolithic discovery run passed.
- Static QA: **PASS** — Python compile for tools/tests, `node --check` for `sw.js` and all `assets/js/*.js`, GitHub Actions YAML parse, 206 unique HTML IDs, 73 APP_SHELL resources with none missing, 33 Markdown files all under `docs/`, and all 26 vocabulary A–Z files byte-identical to v2.11.0 (928 unique IDs). All 38 files under `assets/` are also byte-identical to v2.11.0.
- Packaging: **PASS** — ZIP contains 140 files; `ZipFile.testzip()` returned no CRC error. A clean extraction was compared with all 140 archive entries and the working tree byte-for-byte; no missing, extra or modified files. Python cache artifacts generated during extraction checks were removed before exact comparison.
- Extracted-package recheck: **PASS** — `validate-data.py`, `validate-learning-content.py`, `audit-toeic-coverage.py`, `sync-version.py --check`, Python compile, Node syntax, workflow YAML, 206 unique HTML IDs, 73 APP_SHELL paths (0 missing), and 33 Markdown files under `docs/` passed again from the extracted tree.

## Known limitations

- The automated content validator is structural. Semantic correctness, transcript/passage grounding and distractor quality still need a complete human editorial pass.
- Part 1 uses SVG illustrations, not photo-quality images. Audio is browser SpeechSynthesis, not recorded audio/ETS.
- The pool can supply one blueprint-compliant form but the timed Full Mock engine is not implemented. No official ETS score conversion is claimed.
- Remote GitHub Actions, GitHub Pages deployment, production cache, and physical PC/iPhone/Android QA are not confirmed by local package checks.
