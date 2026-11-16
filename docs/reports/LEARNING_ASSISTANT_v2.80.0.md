# Shared Learning Assistant — v2.80.0

## Purpose

Give learners one optional, reusable help surface for the existing product. The assistant is part of the application shell, not a parallel learning module or second progress system.

## Learner-facing behavior

1. A floating launcher opens/closes the assistant; the small-screen control becomes icon-only and the panel stays above the mobile bottom navigation. The assistant is hidden during an active timed TOEIC Mock attempt.
2. Welcome panel offers the existing in-app guide destinations and the existing placement diagnostic.
3. Prefix lookup reads existing `state.words` records (canonical dictionary and any current personal records already loaded into the normal dictionary state). Search starts at two letters and shows at most six candidates. The remainder of each headword is masked; each missing letter has an individual field. The exact suffix is validated before existing dictionary details are shown. If the typed text is already a complete headword, the existing detail opens directly.
4. The canonical example `ho` returns hospitality, host, hotline, hour and housekeeping. `house`, `horse`, `home` and `hold` are not canonical headwords in this release, so the assistant does not invent their meanings or list them as dictionary records.
5. The contextual follow-up opens a preview with the complete active page/detail prompt and a copy action. For a prompt fitting the configured 12,000-character Google URL guard, the existing Google AI Mode link receives the prompt after a deliberate click. Above the guard, the entire prompt is copied and Google AI Mode is opened for manual paste; text is not silently truncated.

## Reuse and compatibility

- Existing navigation via `navigate`, existing placement diagnostic, existing vocabulary detail (`showDetail` / `buildWordAIPrompt`) and existing AI preview/modal are reused.
- Shared logic resides in `assets/js/learning-assistant.js`; the file is included in Service Worker `REQUIRED` and `APP_SHELL` for offline shell support.
- No new localStorage key, IndexedDB store/version, server endpoint, credential, third-party embedded model, auto-transfer or progress analytics.
- The assistant clears a completed-word context when navigating to another page to prevent a stale term from replacing the current page context.
- Exact-word search opens existing detail directly. Invalid suffix characters (including punctuation), incorrect letters and incorrect order are rejected.

## Mock-exam UI

- Mock navigation/shortcut uses a clipboard-check icon.
- Quick test uses bolt, one-half test uses stopwatch, and 200-question test uses trophy.
- The old `◷` glyph is absent from the shipped index UI.

## Product framing

The current code is the GitHub Pages product source; no separate demo mode or placeholder build is retained in the shipped UI. Educational questions mentioning a product demonstration remain legitimate TOEIC content and are not removed.

## Boundaries

Google AI Mode is an external site reached through a user-initiated search URL; its observed `udm=50` selector is not a documented stable API. The app does not embed Google AI, control its answer, or send data merely by opening the assistant. Users can inspect/copy the prompt before deciding to transfer it.
