# Test Report — TOEIC Dictionary v2.25.0

**Release candidate:** Full TOEIC Mock Practice Beta / Batch 015  
**Base:** V2.24.0 Full Source  
**Date:** 11 November 2026

## Delivered scope

A dedicated Mock page provides a 15-minute / 25-question Quick Test, 60-minute / 100-question Half Test and 120-minute / 200-question Full Test. Each mode has separately timed Listening and Reading sections. The exam saves answers/flags locally, supports resume after refresh, auto-advances at the Listening deadline, auto-submits at the total deadline and displays per-skill and per-Part results.

## Content counts used

| Part | Current eligible bank | Full-test selection |
|---|---:|---:|
| Listening Part 1 | 8 | 6 |
| Listening Part 2 | 25 | 25 |
| Listening Part 3 | 39 | 39 |
| Listening Part 4 | 30 | 30 |
| **Listening** | **102** | **100** |
| Reading Part 5 | 30 | 30 |
| Reading Part 6 | 16 | 16 |
| Reading Part 7 single passage | 38 | 29 |
| Reading Part 7 multiple passage | 25 | 25 |
| **Reading** | **109** | **100** |

The 11 additional Batch 013 Listening reserve questions are not in the mock pool because they remain marked `reserve-pending-independent-review`.

## Format and behavior

| Mode | Listening timer | Reading timer | Total | Q count |
|---|---:|---:|---:|---:|
| Quick | 05:22 | 09:38 | 15:00 | 25 |
| Half | 22:30 | 37:30 | 60:00 | 100 |
| Full | 45:00 | 75:00 | 120:00 | 200 |

The engine samples questions randomly and uses stable IDs to assert no duplicates inside a generated test. P3/P4 whole 3-question blocks, P6 whole 4-question blocks and Part 7 document blocks remain intact. A dedicated lifetime usage ledger (`toeic:mock-usage:v1`) records every generated test independently from the 60-row display history, so rotation does not forget older attempts. Existing attempt history is used to bootstrap/reconcile the ledger on upgrade. Questions that have never been selected are prioritized before previously used items. Since current pool counts exactly match Full Test targets for P2/P3/P4/P5/P6 and all P7 multiple-passage questions, later Full Tests can reuse content. `reusedQuestionCount` is displayed; the content bank must grow before promising multiple fully non-overlapping full tests.

UI includes question map and jump controls, answer selection, flags, section countdown, Listening-to-Reading transition, manual submit, timeout submit, answer explanations, transcript/passage review after completion, visually separated Listening/Reading score rings, raw correct counts, accuracy, distance to the 75% internal target and per-Part improvement guidance. Part 1 prefers JPG and handles load error by switching to its SVG fallback.

## Automated test results

- `node tools/tests/mock-exam-engine.mjs`: **PASS** — exact 25/100/200 questions, timers, Part distributions, unique IDs, grouped audio/passage blocks, excluded reserve content, history and lifetime-ledger rotation, deadlines and scoring.
- `node tools/tests/mock-ui-integrity.mjs`: **PASS** — unique HTML IDs, all three mode controls, split-skill report markup, lifetime-use storage key, no IndexedDB writes from Mock and required PWA resource.
- `node tools/tests/runtime-render-smoke.mjs`: **PASS** — existing Reading/Listening/Grammar render and migration regression.
- `node tools/tests/listening-tts-regression.mjs`: **PASS** — V2.24 TTS cancellation/voice behavior unchanged.
- `node --check` for app module, mock engine and Service Worker: **PASS**.
- HTML static ID check: **PASS** — 235 IDs, no duplicate IDs; all Mock-required IDs exist.
- Existing data, coverage, evidence, distractor and version validators are run separately and summarized after the final build below.

## Score integrity

The redesigned report shows separate Listening and Reading visual score rings, raw correct count out of the questions in that mode, percentage, unanswered count, and the additional correct answers needed to reach 75% for a comparable test. This is not a score out of 495. `75%` is an internal practice target for improvement guidance, not an ETS cutoff or CEFR estimate. No 10–990 score conversion is generated. ETS scores are scaled/equated; the current content pack has no reliable form-specific equating data.

## Storage boundary

Mock test data uses the isolated LocalStorage keys `toeic:mock-history:v1`, `toeic:mock-active:v1`, `toeic:mock-last-result:v1` and the dedicated lifetime rotation ledger `toeic:mock-usage:v1`. No new IndexedDB calls are made. DB `toeic-vocabulary-phase1` version 1, store `workspace`, 928 vocabulary IDs and all existing study progress are untouched. Personal profile import/export/inspection/reset/migration remains deferred and was not performed.

## Known limitations / QA not claimed

- Local source snapshot has no actual Part 1 JPG bytes (0/8). SVG fallbacks exist and the UI fallback path is implemented; strict photo gate remains pending on user's GitHub assets.
- Browser-render/interaction and 15.6-inch 100% zoom, iPhone Safari, Android Chrome and tablet QA are not certified in this release cycle.
- Remote GitHub Actions and Pages deploy are not verified.
- TOEIC teacher/independent editorial signoff is pending.
- Multiple Full Test forms with zero overlap require more reviewed content.
