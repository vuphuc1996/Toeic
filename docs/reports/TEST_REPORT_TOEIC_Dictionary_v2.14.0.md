# TOEIC Dictionary v2.14.0 — Test Report

**Date:** 10 November 2026  
**Release scope:** cross-device Design System + editorial evidence audit (TOEIC-only).

## 1. Unit test results

**116 / 116 unit tests passed.**

| Suite | Tests | Result / execution note |
|---|---:|---|
| Baseline vocabulary ID integrity | 13 | 13/13 PASS |
| Guarded patch engine | 11 | 11/11 PASS |
| Version synchronization | 12 | 12/12 PASS |
| Vocabulary validator regression | 33 | 33/33 PASS; completed in four grouped invocations after the all-module run hit the sandbox timeout |
| Learning content | 24 | 24/24 PASS |
| Diagnostics layout | 6 | 6/6 PASS |
| Shared Design System | 13 | 13/13 PASS |
| Answer-to-source evidence audit | 4 | 4/4 PASS |
| **Total** | **116** | **116/116 PASS** |

The validator suite is counted only after each of its 33 named test cases passed across four completed groups. The earlier timed-out all-module invocation is not counted as a complete run.

## 2. Data/content validators

- Vocabulary: **928 records**, 0 new ERROR, 12 unchanged legacy warnings (DF005=3, EX006=1, FD001=8 across 7 records). Added IDs=0, missing IDs=0; ID-set SHA-256 prefix `dd1705e64c8df4ad`.
- Listening: 56 units / 102 questions; P1 8, P2 25, P3 39, P4 30.
- Reading: 35 resources / 109 questions; P5 30, P6 16, P7 63 (38 single, 25 multiple).
- Grammar: 25 lessons / 54 exercises.
- Learning validator: **0 errors, 0 warnings**.
- Editorial evidence audit: all 211 answer keys mapped; 6 low-overlap inference/paraphrase cases checked against source; 8 P1 visual/key, 25 P2 response-fit, 30 P5 grammar and 16 P6 context items reviewed. 126 direct/lexical evidence mappings remain for a dedicated distractor-uniqueness pass.

## 3. Static/build validation

- `python -m py_compile tools/*.py tools/tests/*.py`: PASS.
- JavaScript syntax (`sw.js` and `assets/js/*.js`): PASS.
- GitHub Actions YAML parse: PASS.
- CSS parser: 0 errors.
- HTML IDs: 206 total / 206 unique / 0 duplicates.
- APP_SHELL: 73/73 paths exist; design-system stylesheet included in required shell.
- Version sync (`data/manifest.json`, Service Worker, index, Master, README, Changelog): PASS at v2.14.0.
- Project Markdown placement: all Markdown files under `docs/`.
- All 26 vocabulary A–Z files were compared byte-for-byte with the v2.13.0 ZIP and remain identical, including after clean v2.14.0 ZIP extraction.

## 4. Browser and device QA boundary

Local headless Chromium 144 could not complete the preview because sandbox navigation/rendering was blocked (`ERR_BLOCKED_BY_ADMINISTRATOR` / renderer termination). No browser screenshot or interaction QA is claimed. No physical iPhone, Android, iPad, Windows/macOS browser, remote GitHub Actions run or production GitHub Pages deployment is claimed. See `RESPONSIVE_LAYOUT_QA_v2.14.0.md`.

## 5. Scope and preservation

- Vocabulary remains 928/928 records and stable IDs; 26 A–Z files unchanged.
- Listening/Reading question counts and IDs/order remain unchanged; only Part 2 transcript translations and one response wording were clarified, with the correct answer index preserved.
- Grammar remains 25/54.
- No IndexedDB or personal vocabulary schema migration; no progress data migration.
- Part 1 still uses SVG illustrations; browser SpeechSynthesis remains synthesized audio, not recorded ETS audio.
- No official ETS score conversion and no completed Full Mock engine. IELTS remains deferred.

## 6. ZIP packaging

- Final ZIP: `TOEIC_Dictionary_v2.14.0_Cross_Device_Design_System.zip` — **156 files**, CRC PASS.
- Clean extraction: **156/156** files exact match with the final build tree; no missing, extra or modified entries.
- The clean extracted package reran both validators and version sync: vocabulary 0 ERROR / 12 legacy warnings; learning content 0 ERROR / 0 WARNING; version sync PASS.
- All 26 A–Z vocabulary JSON files in the clean extraction are byte-identical to v2.13.0.
