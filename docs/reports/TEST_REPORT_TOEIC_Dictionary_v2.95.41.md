# Test Report — TOEIC Dictionary v2.95.41

## 1. Release scope

- Base: exact user-supplied v2.95.40 Full Source.
- Release: v2.95.41 — Listening reserve inventory and answer-position identity regression correction.
- Scope: tests, release/version markers and generated audit/progress reports. No app feature or learning-content change.

## 2. Root cause and fix

- Reproduced the CI failure in `test_answer_position_balance.py`: expected 161 reserve Listening questions; canonical data contains 193. After this assertion, the stale total expectation of 263 would also have been wrong; current total is 295.
- v2.95.37 Batch 027 added 16 original-editorial Listening resources / 32 questions (Part 2=8, Part 3=12, Part 4=12). Every new question remains `reserve-pending-independent-review` and excluded from Mock.
- Updated the regression contract to 102 eligible + 193 pending = 295 total. Per-Part eligible and pending counts are asserted; Batch 027's resource/question count and fail-closed status are checked.
- Retained choice identity validation: unique choice IDs, valid key indexes, historical 27-key movement and the link between the answer text and the same stable `choiceId` after reorder.
- The existing GitHub Actions step for `test_answer_position_balance.py` is unchanged. The CI coverage tests confirm all Python modules remain registered.

## 3. Current Listening inventory

| Part | Eligible | Reserve pending | Total |
|---|---:|---:|---:|
| Part 1 | 8 | 1 | 9 |
| Part 2 | 25 | 36 | 61 |
| Part 3 | 39 | 84 | 123 |
| Part 4 | 30 | 72 | 102 |
| **Total** | **102** | **193** | **295** |

- Listening: 145 units / 295 questions.
- Batch 027: 16 units / 32 pending questions; P2=8, P3=12, P4=12.
- Reading: 73 resources / 287 questions.
- Grammar: 58 lessons / 169 exercises.
- Separate Part 5 sentence completion: 80 questions, practice-only and independently review-pending.

## 4. Focused Python tests

**46/46 PASS across 7 modules**, executed as separate unittest discoveries:

| Module | Result |
|---|---:|
| `test_answer_position_balance.py` | 4/4 PASS |
| `test_listening_expansion.py` | 8/8 PASS |
| `test_question_evidence.py` | 7/7 PASS |
| `test_distractor_quality.py` | 6/6 PASS |
| `test_content_batch_027.py` | 6/6 PASS |
| `test_ci_coverage.py` | 3/3 PASS |
| `test_sync_version.py` | 12/12 PASS |
| **Total** | **46/46 PASS** |

Additional syntax verification: `python -m compileall -q tools` and `python -m py_compile tools/tests/test_answer_position_balance.py` PASS.

## 5. JavaScript regression and syntax

- JavaScript `.mjs` regression suites: **39/39 PASS**.
- `node --check sw.js`: PASS.
- All 18 `assets/js/*.js` modules: PASS.

## 6. Data, content and cross-domain validation

| Check | Result |
|---|---|
| `tools/validate-data.py` | PASS — 1,141 vocabulary records; 0 errors / 0 warnings; 0 IDs added or removed |
| `tools/validate-learning-content.py` | PASS — 0 errors / 0 warnings; Listening 145/295, Reading 73/287, Grammar 58/169; Part 5 practice 80 |
| Repository integrity | PASS — 411 local references/data files; 0 errors / 0 optional warnings |
| Version synchronization | PASS — all markers v2.95.41 |
| Design profile | PASS — 54 tokens / 406 legacy font-floor groups synchronized |
| Part 1 photos | PASS — 9/9 assets |
| Objective resources | PASS — 379/379 across 11 objectives |
| Learning outcomes | PASS — 11 objectives / 33 measurable criteria; 6/33 have evidence paths; no full-instrumentation claim |
| Foundation A2 assessment | PASS — core Reading 13/13, Listening 13/13; supplementary Listening 13/13; source evidence 5/5 |
| Listening readiness | PASS — 102 eligible / 193 reserve-pending / 295 total |
| Question evidence | PASS — 582 questions indexed; reserve scope 193 |
| Distractor structural audit | PASS — 264 questions in scope, unique choices and valid keys; 156 Part 3/4 reserve question structures checked |
| Content coverage | PASS — generated from canonical v2.95.41 data |
| Project progress | PASS — generated from canonical v2.95.41 data |

## 7. Release synchronization and regenerated reports

- Manifest, app release marker, Service Worker cache version, index title/sidebar/phase/footer, README, Master Status and Current Version are synchronized at v2.95.41.
- Generated reports: Listening Readiness, Editorial Evidence, Distractor Audit, Content Coverage, Foundation A2 assessment and Project Progress.
- Current changelog entry and immediate previous version record were updated.

## 8. Data preservation

No Listening/Reading/Grammar question, choice text, answer key/index, question or resource ID, choice ID, editorial status, Mock eligibility, learner progress, IndexedDB schema, localStorage key, UI layout or Robot Buddy behavior was changed. Reserve questions remain Mock-excluded until independent editorial approval is recorded.

## 9. Not verified / limits

- Full aggregate Python test discovery is not claimed; only the 7 named modules (46/46 tests) and direct validation commands above were run for this release.
- Remote GitHub Actions, GitHub Pages deployment/cache and browser/physical-device acceptance were not run in this environment.
- Independent second-person editorial approval for reserve content remains pending.

## 10. Package

- Full Source: **597 files** under one root folder, `Toeic_Dictionary_v2.95.41/`.
- ZIP CRC test: PASS; single-root and exclusion policy: PASS (no `.git`, caches, `__pycache__`, `.pyc`, `.pyo` or nested release ZIPs).
- Exact source comparison after archive creation: **597/597 files byte-identical**.
- SHA-256 sidecar generated beside the ZIP and verified against the final archive.
