# Batch 017 — Focus Learning Workspace & Vocabulary Expansion (v2.27.0)

**Date:** 2026-11-12  
**Status:** implemented locally; browser/device QA and independent vocabulary review pending.

## A. Learning interaction unification

1. Flashcard page shows the topic-selection dashboard. Selecting a topic opens a fixed focus layer with blurred/dimmed background, centered workspace, internal scroll and close ×.
2. First click/Enter/Space flips the card to the detailed face; second click advances. The detail face contains meaning, US IPA where available, definition, example and translation, collocations and lexical relations.
3. The post-learning vocabulary quiz stays in the same focus layer. Closing returns to topic selection.
4. Review page shows statistics, eight modes (smart, word→meaning, meaning→word, missing letters, POS, synonym, antonym, verb forms), weak vocabulary and a Start button. Questions are moved into focus mode only after Start; × returns to the dashboard.
5. Grammar, Listening and Reading details use consistent centered focus-modal styling, internal scrolling, mobile safe-area behavior and reduced-motion support.

## B. Vocabulary content

Added 43 headwords to `data/vocabulary/batch-006.json` and their canonical A–Z files. The records cover business/legal/finance/workplace operations, staffing and logistics.

`allegation`, `arbitration`, `attire`, `authenticate`, `automate`, `brokerage`, `convene`, `demolition`, `diagnosis`, `dividend`, `embark`, `escalate`, `exposure`, `hamper`, `impose`, `indispensable`, `inflation`, `integration`, `patent`, `penetrate`, `persist`, `prerequisite`, `premise`, `preserve`, `prospect`, `relocation`, `remit`, `retire`, `solicitation`, `sponsor`, `staffing`, `stockholder`, `subsequent`, `succession`, `tariff`, `transition`, `treasury`, `unanimous`, `voluntary`, `onboarding`, `offsite`, `counterpart`, `disruption`.

- Canonical total: 928 → 971 headwords.
- Existing vocabulary IDs retained; no duplicate canonical IDs.
- Each new entry has at least one sense, POS, Vietnamese meaning, English definition, example/translation, topic and US IPA. Collocations/verb forms are included where applicable.
- CEFR is an editorial estimate, not an official ETS or CEFR certification. The entire batch remains pending editorial verification.

## C. Regression and data-safety boundaries

- Added `tools/tests/learning-focus-workspace.mjs` and a GitHub Actions invocation.
- Test checks unique HTML IDs, flash flip and next flow, practice dashboard/modes/start/close, shared detail modal styling, responsive CSS, vocabulary batch inclusion and no IndexedDB schema change.
- Database remains `toeic-vocabulary-phase1` v1 / `workspace`; do not import/export/inspect/reset/migrate personal profiles as part of this batch.
- No TTS settings, Mock Engine, Listening/Reading question content or Part 1 photo files were changed.

## D. Manual test steps after applying overlay

1. Open Flashcard. Confirm topics are visible. Select a topic. Confirm the page behind dims and one contained study card appears.
2. Tap the card once; confirm meaning/example face appears with flip transition. Tap again; confirm next word appears. Use ×; confirm topic chooser returns.
3. Complete a learning batch; confirm the check/quiz stays inside the same focus frame. Close with × and reopen another topic.
4. Open Review. Confirm statistics, eight modes and weak-word list appear without a question. Select a mode and Start; confirm only the question workspace takes focus. Close with ×; confirm dashboard returns.
5. Open one Grammar lesson, Reading resource and Listening item. Confirm same backdrop, centered frame, internal scroll and close action.
6. Test 320–390px phone, large phone, tablet portrait/landscape, 15.6-inch laptop at 100% zoom and wide desktop. Confirm no horizontal overflow and no page content pushed by the focus frame.

**Expected:** 5 and 6 behave consistently. Record any browser/device-specific layout defect with viewport width/height, browser and screenshot.
