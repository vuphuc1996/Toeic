# Compatibility & Retirement Register

> Single register for current runtime, storage, offline and retirement contracts. Release history belongs in `CHANGELOG.md`.

## Current support window — 2026-11-19

| Role | Version | Policy |
|---|---|---|
| Current product source | v2.95.9 | v2.95.8 functional baseline retained; Robot Buddy progressive response stream and context-aware local composition added. |
| Immediately previous source | v2.95.8 | Five-defect consolidation, opt-in local read-only Learning Insights, one visual progress dashboard and repository cleanup. |
| Older releases | ≤ v2.95.6 | Historical; details are in `CHANGELOG.md` and the consolidated archive. |

## Runtime contracts

- **Deployment:** GitHub Pages static PWA. No application backend, GAS, iframe or Cloudflare dependency.
- **Canonical vocabulary:** `data/vocabulary/A.json`–`Z.json`; `data/manifest.json` declares the release version, letter files and total count. `data/vocabulary/batch-*.json` are editorial provenance, not runtime vocabulary sources.
- **TOEIC content:** canonical Listening, Reading, Grammar, Part 5 practice and Foundation JSON files are loaded by the app and protected by validation/tests. Stable resource, question and choice IDs must not be repurposed.
- **Mock eligibility:** reserve-pending-independent-review content and unknown statuses are excluded; inventory presence is not editorial approval. Keep practice-only Part 5 and supplementary Foundation content separate from Mock pools.
- **Flashcard batch size:** one fixed maximum of 10 vocabulary cards per session. The retired 5-card option must not return in UI or runtime; topic, mixed learning, continue/next batch and wrong-answer review all use the same 10-card cap. If fewer than 10 eligible items remain, show only the available items.
- **TTS:** browser/device SpeechSynthesis only. It is synthesized speech, not ETS/native audio. Voice availability, voice quality and acoustic timing are device-dependent.
- **Part 1 media:** JPG-only contract; each Part 1 item uses its `photo` asset and source attribution. Do not add SVG fallback or replace licensed/project-owned photos with unrelated generated assets.

## Robot Buddy and privacy boundary

- `assets/js/robot-buddy.js` and `data/robot/robot-library.json` implement the head-only offline companion. Replies are composed from bundled dialogue/FAQ content, lightweight rule-based intent handling, varied language fragments and current in-memory app context; `app.js` streams the text progressively with a blinking cursor.
- Robot Buddy may use its own onboarding/reminder preferences, the currently active app surface, the current word/question/lesson being viewed and idle-time context. Context-aware replies and nudges use only the current in-session item, not a stored learner profile. When the learner enables Learning Insights, the application may pass an in-memory snapshot of already-loaded local learning records to the pure `robot-learning-insights.js` aggregator. The aggregator is read-only: it does not open IndexedDB/localStorage, mutate records, migrate data or transmit learner data.
- Learning Insights is opt-in and can be disabled from the Robot Buddy header. When disabled, the Buddy still supports offline composed conversation, feature guidance, quick prompts, Placement consent/skip and generic idle reminders.
- Personal progress analysis may summarize only evidence already present in the local snapshot. It must not claim mastery, predict ETS scores or infer weakness when evidence is insufficient. The visual dashboard is the single progress summary; do not repeat its totals in prose.
- The progressive typing effect is a presentation behavior, not evidence of model generation. Robot Buddy does not use a generative model, call external APIs or send learner data outside the device. Unknown prompts receive a clarification request rather than an invented answer. Feature-level Google AI handoffs remain separate and user-initiated.
- `assets/js/learning-assistant.js` and `assets/js/quick-help.js` are intentionally inert compatibility tombstones. The current app does not import them. They remain in the source and offline shell only to overwrite/serve legacy paths during GitHub repository overlay updates; they are not active Robot logic or duplicate implementations.
- Legacy feature-level Google AI handoffs remain user-triggered at their existing feature entry points and are separate from Robot Buddy.

## Storage compatibility

- IndexedDB remains `toeic-vocabulary-phase1`, schema version 1, store `workspace`. Do not reset, rename or migrate it without a separately approved migration plan.
- Preserve existing vocabulary, practice, review, Flashcard, Mock and Foundation localStorage keys and learner records. New evidence fields must be additive and scoped by stable IDs.
- Robot settings use `toeic:robot-buddy-settings:v1`; the one-time onboarding migration may read the legacy `toeic:robot-companion-onboarding:v1` key. Chat history remains in memory for the current session.
- No profile import/export or cross-device sync is part of the current GitHub-only product contract.

## Offline / Service Worker

- `sw.js` `REQUIRED` resources must be present and also appear in `APP_SHELL`; optional illustrations/photos must not block installation.
- The cache namespace version must match `data/manifest.json`. A release bump creates a new cache namespace; activation removes only older caches with the TOEIC-specific prefix.
- Structural cache-list tests do not prove actual browser offline/reconnect behavior. Verify installed PWA update, offline navigation and recovery on real devices.

## Developer and CI contract

- `.github/workflows/validate-data.yml` must invoke every `tools/tests/test_*.py` module and every `tools/tests/*.mjs` suite.
- `test_ci_coverage.py` enforces registration; `audit-repository-integrity.py` checks local references, PWA shell lists, workflow references and JSON syntax.
- Canonical patch payloads under `patches/` and vocabulary batch JSON are retained as provenance/reproducible editorial history; they are not shipped runtime features and must not be deleted as presumed dead code.
- Never remove a file solely because it lacks a direct import: check Service Worker compatibility, tests, data provenance, migration history and documentation references first.

## Retired / incompatible

- Legacy GAS, iframe and backend proposals are historical only.
- The old Quick Help word-search UI and the legacy v2.83 progress-reader implementation are retired. Current Robot learning insights use the separate `robot-learning-insights.js` pure aggregator; the inert tombstones above exist only for overlay compatibility.
- No duplicate canonical data store, parallel Master roadmap or feature-specific design-system copy should be introduced.


## PWA update lifecycle

- The first install may activate immediately because there is no older worker/cache to replace.
- A later worker update installs its complete required shell, then waits. It does not call `skipWaiting()` automatically.
- The app displays “Có bản mới – Tải lại”; only that explicit action sends `SKIP_WAITING`. The old worker/cache remains active until confirmation and successful activation.
- Activation then removes only older `toeic-vocab-github-only-v*` caches. This behavior still requires real-browser acceptance with two open tabs; local simulation is not a substitute.
