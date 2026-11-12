# Batch 015 — Full TOEIC Mock Practice Beta (v2.25.0)

## Objective
Deliver the three user-requested timed Listening & Reading test modes using the existing reviewed question pool. Keep the build independent from IndexedDB personal data.

## Formats

| Mode | Listening | Reading | Total | Questions |
|---|---:|---:|---:|---:|
| Quick | 05:22 | 09:38 | 15 min | 12 + 13 = 25 |
| Half | 22:30 | 37:30 | 60 min | 50 + 50 = 100 |
| Full | 45:00 | 75:00 | 120 min | 100 + 100 = 200 |

## Content selection

- Eligible existing content: Listening 102 questions; Reading 109 questions.
- Listening reserve Batch 013: 11 questions are excluded because their `editorialStatus` is `reserve-pending-independent-review`.
- Full form: Listening Part 1–4 = 6/25/39/30; Reading Part 5–7 = 30/16/54, with Part 7 selection of 29 single-passage + 25 multiple-passage questions.
- Randomization is at the question or source-block level as appropriate. Part 3/4 three-question audio units, Part 6 four-question passage sets and each Part 7 source block remain indivisible. The generator rejects a form with duplicate stable question IDs or a pool that cannot satisfy the exact target.
- A separate lifetime-use ledger stored in `toeic:mock-usage:v1` contributes question-use counts independently of the most-recent-60 display history; least-used eligible questions are prioritized, including after older attempts age out of the visible history. The current bank only fits one full 200-question blueprint in several Parts, so repeated full tests cannot yet be guaranteed to be entirely disjoint. The UI reports reused question count rather than concealing it.

## User interface

- New desktop sidebar and mobile Học tập entry, dashboard shortcut and dedicated `page-mock`.
- Three mode cards and data-pool counts.
- Section timer and auto transition Listening → Reading; Reading cannot return to Listening.
- Question map, answer selection, flag/unflag, submitted/unanswered count and local resume.
- Part 1 displays the JPG photograph path and switches to the existing SVG fallback after a JPG load error. Part 3/4 use the existing Listening TTS, not licensed/ETS recordings.
- Reading displays source passage/documents. Transcript and source text are revealed in review after submission.
- Results show total raw correct count, separate visual Listening/Reading score rings with raw counts and accuracy, unanswered counts, the additional correct answers needed to reach the internal 75% target, per-Part accuracy, learning guidance, answer explanations and history. No ETS-equated 5–495/10–990 estimate is fabricated.

## Score integrity

No ETS 10–990 score or CEFR conversion is fabricated. ETS scaled scoring is based on equated score conversion; this content collection does not contain form-specific equating tables. The result is explicitly labeled as practice-only.

## Storage and non-regression

Dedicated keys: `toeic:mock-history:v1`, `toeic:mock-active:v1`, `toeic:mock-last-result:v1`. The mock feature does not call the existing IndexedDB wrapper, change DB version 1, create stores, or modify vocabulary/Reading/Listening/Grammar study progress. No personal profile inspection/import/export/reset/migration was performed.

## Automated checks

- `node tools/tests/mock-exam-engine.mjs`: PASS.
- `node tools/tests/runtime-render-smoke.mjs`: PASS.
- `node tools/tests/listening-tts-regression.mjs`: PASS.
- JS syntax/static HTML checks: PASS.

## Remaining release gates

- Actual 8 JPG binaries are missing from the local source snapshot. The Part 1 UI fallback exists, but strict photo validation still must pass 8/8 on the actual repository before release.
- Local Chromium / physical laptop/tablet/iPhone/Android QA has not been verified in this work cycle.
- Remote GitHub Actions and GitHub Pages deployment have not been run from the user's repository.
- Independent TOEIC content/editorial review is pending; Batch 013 reserve stays excluded.
- More reserve content is needed for multiple non-overlapping 200-question forms.
