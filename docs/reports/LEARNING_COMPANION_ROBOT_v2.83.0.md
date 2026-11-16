# TOEIC Dictionary v2.83.0 — Robot Buddy specification

**Base:** v2.82.1 Full Source  
**Purpose:** replace the old Quick Help usage guide with a responsive, local-progress-aware Robot Buddy while preserving every feature-level Google AI action that existed in v2.79.0.

## 1. Product boundary

Robot Buddy is a deterministic, device-local companion. It reads the app's existing progress stores and chooses from authored messages/actions. It is not a generative model, not a free-form chatbot and does not call Google, another model API or a backend. It does not upload learning history. This distinction is intentional: legacy Google AI remains available separately through the original feature-level controls in Vocabulary, practice answer/review, Grammar, Reading and Listening.

The v2.80 shared floating assistant, page-context prompt, follow-up/copy/transfer handoff, vocabulary prefix search and masked-letter exercise are withdrawn prototypes and are not reintroduced here.

## 2. First-run experience

- The Robot launcher uses the existing SVG sprite symbol `icon-robot`.
- After the current progress stores have loaded, the app checks `toeic:robot-companion-onboarding:v1`.
- If there is no onboarding decision and no meaningful learning footprint in the existing local progress stores, the Robot panel opens once and asks whether the learner wants the existing Placement Diagnostic before starting.
- **Đánh giá đầu vào** saves `accepted`, closes the panel and opens the current Placement Diagnostic. On completion, the Robot publishes the locally derived recommended starting level.
- **Để sau, bỏ qua** saves `skipped`; the first-run prompt is not shown again on subsequent visits. The Placement action is not re-offered inside the skipped onboarding state.
- If existing learning evidence is found, the learner is marked as returning and is not asked the first-run question.
- The decision is device/browser-local, not account-wide. Clearing local browser storage can cause the first-run prompt to appear again.

## 3. Local progress signals

`assets/js/learning-assistant.js` is a pure summary module. `assets/js/app.js` passes it already-loaded state from the existing stores:

- Vocabulary review progress: unique headwords reviewed, total review attempts, accuracy derived from recorded correct/review counts, and words already due or with more wrong than correct answers.
- Flashcard progress: unique cards seen and repetitions; it does not infer mastery from `reps` alone.
- Grammar: number of attempted exercises, total available exercises and latest-answer accuracy; a lesson is suggested for review only after at least three unique answered exercises.
- Reading Parts 5–7 and Listening Parts 1–4: unique answered questions, latest answer per question and accuracy. Retry history is not counted as extra unique questions. A Part is presented as a review priority only when at least three unique questions have been answered.
- Foundation Reading and Listening: separate evidence ledgers and latest correctness are summarized separately.
- Foundation delayed recall: number of questions currently due, using `listDueFoundationRecallItems`.
- A2 writing: started tasks and revised tasks from the existing Foundation production portfolio. Different task-specific rubrics are not combined into one artificial score.
- Placement: the existing locally stored recommended starting level, with a clear statement that this is not CEFR certification.
- Mock Exam: completed attempts and the latest stored practice result, explicitly not an ETS-equated score.

All summary calculations are derived from existing learner data. The Robot does not write to these stores; only the one-time onboarding choice is stored in the new `toeic:robot-companion-onboarding:v1` key.

## 4. Milestones and actions

The Robot can publish a message after a completed learning action:

- third consecutive correct vocabulary answer;
- completed Flashcard quiz;
- confirmed Grammar, Reading or Listening practice batch;
- confirmed Foundation assessment or delayed recall;
- completed Placement Diagnostic;
- submitted or revised A2 contextual writing;
- completed Mock Exam.

When the panel is closed, the launcher shows a small update dot; opening it displays the latest message and a refreshed summary. The Robot offers direct actions to existing destinations: review due words, open a Reading/Listening Part with sufficient evidence, open a Grammar lesson with sufficient evidence, review Foundation recall, open the A2 writing portfolio, view the latest Mock result, open Placement (unless intentionally skipped), and continue Practice/Foundation.

It does not display an unverified weak-area label from fewer than three unique answers. Recommendations are guidance, not a learner grade or mastery certificate.

## 5. UI, animation and accessibility

- Floating Robot launcher replaces the old headset helper icon.
- Panel entrance, launcher float, avatar bob, online pulse, message and action-card entrance animations provide a light companion feel.
- On widths up to 820 px the launcher becomes a compact icon and the panel moves above the mobile bottom navigation.
- At widths up to 390 px onboarding actions stack into one column; panel height remains bounded and the body scrolls internally.
- Short landscape viewports use a tighter panel height and safe bottom position.
- The Robot is hidden during an active timed Mock Exam.
- Escape closes the panel; the launcher exposes `aria-expanded` and controls the panel; the greeting is announced with `aria-live`.
- `prefers-reduced-motion: reduce` disables all Robot motion/transitions.
- All Robot action icons use symbol IDs already present in the existing SVG sprite and existing design-system type roles.

## 6. Service Worker / SW002

- `assets/js/learning-assistant.js` is the active local Robot module.
- `assets/js/quick-help.js` is a no-op compatibility tombstone. It intentionally executes nothing; its purpose is to overwrite a stale file at the same path when the user overlays this release onto an older GitHub checkout.
- Both paths are included in `sw.js` `REQUIRED` and `APP_SHELL`. The cache version is synced to `data/manifest.json` (`2.83.0`).
- `python tools/validate-data.py` now reports zero SW002 errors for these two assets.

## 7. Preserved and removed scope

**Preserved:** all v2.79.0 feature-level Google AI actions and their original prompt builders, preview and explicit external handoff; Mock Exam icon family; A2 writing tasks, guided revision and portfolio; all vocabulary/question IDs and existing progress stores.

**Removed:** the usage guide; prefix-based helper search; suggestion list; masked headword; letter-entry challenge; exact-match helper shortcut; v2.80 contextual assistant prompt/follow-up/copy/transfer integration and any Google action inside Quick Help.

**Storage:** one new localStorage key only: `toeic:robot-companion-onboarding:v1`. No IndexedDB v1 schema/store migration, no changes to `toeic:foundation-progress:v1`, no vocabulary or question additions and no learner-data reset.
