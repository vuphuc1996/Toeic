# Batch 019 — Shared Learning Workspace & Flashcard Single Scroll (v2.29.0)

**Base:** v2.28.0  
**Status:** implemented locally; automated regression checks recorded in the v2.29.0 test report. Browser/device QA and remote deployment remain pending.

## 1. User-facing changes

### Flashcard two-zone layout

- The upper panel is always the vocabulary face: word, IPA/POS, topic and card position.
- First tap/Enter/Space or the explicit flip button reveals a lower details panel containing Vietnamese meaning, English definition, example + translation, collocations, synonyms/antonyms and verb forms where available.
- The user advances using the explicit “Từ tiếp theo” action or activating the top panel again. Pronunciation playback remains a separate action and does not trigger card advance.
- Approved word-specific artwork remains optional and is displayed within the upper panel. Topic art is never substituted for a word-specific image.

### Single vertical scroll owner

- `.learning-focus-content` owns the only vertical scrollbar for the focused learning session.
- Flashcard front and revealed detail panels are natural-height blocks; neither has fixed height, `max-height` clipping or `overflow-y:auto`.
- Grammar, Reading and Listening detail content is mounted inside the shared focus content node; the moved modal-content node is reset to visible overflow.
- Short content does not need to scroll; long Reading passages, transcripts or explanation sets scroll once in the outer workspace.

### Common learning design

- Flashcard and Review already used the focus shell; Grammar/Reading/Listening now enter through `openLearningDetail()` and share the same header, close control, backdrop, dialog width, responsive safe areas and content scroll.
- No new feature-specific backdrop/modal component is introduced.
- Vocabulary editor/detail and Smart Review answer explanation remain utility overlays by purpose, not alternate Learning Unit detail shells.

## 2. Responsive requirements

- Desktop: upper vocabulary panel, then lower meaning panel; action row follows details. The dialog stays centered and bounded by viewport height.
- Tablet: same hierarchy; optional art stacks above word text when width is constrained.
- Phone: one-column layout and safe-area-aware bottom sheet; the whole learning content scrolls as one document.
- `prefers-reduced-motion` disables the details reveal animation; focus and keyboard operation remain available.

## 3. Source files changed

- `assets/js/app.js`: `openLearningDetail()` shared entry point; Grammar/Reading/Listening use the same focus host; Flashcard markup split into front + revealed detail panels.
- `assets/css/app.css`: shared learning shell content reset, single-scroll layout, responsive two-zone Flashcard panels and reduced-motion rule. Removed 40 obsolete selectors/rules for the previous `.flashcard-content` inner scrolling face, `.flashcard-no-art` layout and old card-flip shell.
- `tools/tests/learning-focus-workspace.mjs`: guards shared shell behavior, single-scroll contract and unchanged IndexedDB v1.
- `tools/tests/flashcard-image-policy.mjs`: validates the new flashcard stack and approved word-image contract.
- `tools/tests/runtime-render-smoke.mjs`: confirms Reading/Grammar render through the shared detail helper and preserve the existing choice/progress migration behavior.
- `tools/rotate-release-files.py` and `tools/tests/test_release_rotation.py`: dry-run/apply logic preserves only previous/current release documents and compacts retired notes into Project History; the regression tests confirm that user assets are not touched.

## 4. Explicit non-changes / safety boundaries

- No vocabulary records, Listening/Reading question pool, answer keys or Grammar content changed.
- No `data/manifest.json` data count change; canonical vocabulary remains 979.
- IndexedDB stays `toeic-vocabulary-phase1` version 1 / store `workspace`; no personal profile import/export/reset/inspection/migration.
- No JPG/attribution or SVG fallback asset is removed or modified.
- No TTS voice defaults, pause timings, Mock engine or scoring logic changed.

## 5. Manual acceptance steps

1. Open Flashcard on a 15.6-inch laptop at 100% zoom. Select a topic and confirm the word/IPA remains in the top panel.
2. Flip the card. Confirm the meaning/example panel appears below the word panel, not inside a second fixed-height scrolling face.
3. Use the mouse wheel/trackpad over the word and lower content. Confirm one workspace scrollbar moves the whole content; there is no inner thumb/scroll capture.
4. Try a short word and a word with long example/collocations. Short content should not create needless scrolling; long content should scroll once in the outer workspace.
5. Use next word, voice playback, keyboard Enter/Space and close ×. Confirm voice does not advance the card and closing returns to topic selection.
6. Open one Grammar lesson, one Reading passage and one Listening unit. Confirm all share the same backdrop/header/close button and content width; each long unit scrolls in the same outer area.
7. Repeat at phone widths 320–430px and tablet portrait/landscape. Confirm safe-area padding, no horizontal overflow and no nested vertical scrollbar.

**Expected:** Flashcard and all Learning Unit detail flows use a single coherent shell; only the outer focus content scrolls. Record any visual or browser-specific exception with viewport dimensions, browser and screenshot.
