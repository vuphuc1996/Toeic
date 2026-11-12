# Test Report — TOEIC Dictionary v2.27.0

**Scope:** unified focused learning interactions, responsive detail modal presentation and Vocabulary Batch 017. This is a local release candidate; it is not evidence of a remote deployment.

## Implemented

- Flashcard keeps the topic chooser visible until a topic is chosen. A chosen session moves into a fixed focus workspace over a dimmed/blurred backdrop. First tap/keyboard activation reveals details; the next advances to the following word. The × button returns to the topic chooser.
- The vocabulary check following a Flashcard learning batch remains inside the same focus workspace.
- Review landing page presents statistics, eight exercise modes, weak-word list and Start action. The question panel is hidden until Start; Start moves it into focus mode; × restores the dashboard.
- Grammar, Listening and Reading details use a consistent centered focus modal. Content scrolls inside the modal; responsive breakpoints and mobile safe-area insets prevent the modal from expanding the page. Reduced-motion preference is respected.
- Vocabulary Batch 017 contributes 43 new headwords; canonical total is 971. Batch metadata marks CEFR as editorial estimate and the content as pending editorial verification.

## Local checks — completed in this release session

| Check | Result |
|---|---|
| `node --check sw.js` and every `assets/js/*.js` module | PASS |
| `tools/tests/learning-focus-workspace.mjs` | PASS — 243 unique HTML IDs, focus/close/flip flow, responsive CSS, unchanged IndexedDB v1, all 43 Batch 017 words are present in 971 canonical records |
| `tools/tests/flashcard-image-policy.mjs` | PASS — 971 words; no generic topic image on word cards |
| `tools/tests/mock-ui-integrity.mjs` | PASS — Mock UI and lifetime usage ledger remain intact |
| `tools/tests/mock-exam-engine.mjs` | PASS — all three modes, blueprint, no in-form duplicate questions |
| `tools/tests/listening-tts-regression.mjs` | PASS — previous playback behavior unchanged |
| `tools/tests/runtime-render-smoke.mjs` | PASS — Reading, Listening, Grammar render and choice-ID migration smoke |
| `test_vocabulary_detail_examples.py` | PASS — 10/10, including preservation of 928 baseline IDs plus 43 additions |
| `test_legacy_collocation_cleanup.py` | PASS — 3/3 |
| `test_sync_version.py` | PASS — 12/12 |
| `test_patch_data.py` | PASS — 11/11 |
| `python tools/validate-data.py` | PASS — 971 records, 0 errors, 0 legacy warnings; +43 IDs, 0 removed |
| `python tools/validate-learning-content.py` | PASS — 0 errors, 8 JPG-missing warnings (SVG fallback present) |
| `python tools/audit-question-evidence.py` | PASS — 222 indexed Listening/Reading questions |
| `python tools/audit-distractors.py` | PASS — 132 reviewed historic questions; 6 reserve sets separately structural |
| `python tools/validate-part1-photo-assets.py --allow-missing` | Diagnostic only — 0/8 JPEG binaries found; 8 warnings; **not** a release photo-gate PASS |
| `python tools/sync-version.py --check` | PASS — all registered version markers at 2.27.0 |


## Package verification

- Update Overlay: 35 entries (27 changed + 8 added; 0 deletions), SHA-256 `fe9365f14740fe41fe9e1b04edd93eac9c11d7788d6bade087760582d7a9ef11`; CRC and clean-extraction byte comparison PASS.
- Full Source: 256 files; SHA-256 sidecar provided; CRC and clean-extraction byte comparison PASS.
- Neither archive contains the eight JPG binaries; Overlay does not modify or remove any file under `assets/listening/`. Preserve the existing GitHub images when merging.

## Safety and limitations

- IndexedDB database remains `toeic-vocabulary-phase1`, version 1, object store `workspace`; no user profile migration or test import/export/reset/inspection was done.
- No TTS voice settings, Listening/Reading question pools or Mock Engine were modified.
- The eight JPG Part 1 image bytes are absent from this working snapshot. SVG fallbacks and `ATTRIBUTION.csv` remain present. Strict photo validation must be run on the complete repository with all eight images before release.
- No real-device/browser interaction, remote Actions result or GitHub Pages deployment is claimed. Check laptop 15.6-inch at 100% zoom, tablet portrait/landscape, iPhone Safari and Android Chrome after applying the patch.
- Vocabulary CEFR labels in new Batch 017 records are editorial estimates; independent lexical review remains pending.
