# Robot Buddy v2.84.0 — Product and Technical Specification

## Product identity

Robot Buddy is a head-only animated companion. It is a scripted, static-content feature for the GitHub Pages PWA, not a general-purpose AI chatbot. A single SVG head is reused in the launcher, chat panel and idle prompt. Emotions include happy, thinking, celebration, caring, sleepy, greeting, surprised, motivation, concerned, playful, listening and speaking.

## Content inventory

`data/robot/robot-library.json` is the single local dialogue catalogue. It contains 500 unique lines in seven groups: greeting 60; encouragement 100; caring 60; learning 80; help 100; reaction 60; rest 40. It also contains feature-help text for 11 in-app destinations, six FAQ answers and 12 quick prompts. The JSON is a read-only app asset, precached by the Service Worker.

## Runtime behavior

- Opens from a head-only launcher; panel supports a chat-like transcript, quick prompt chips and a short text input (maximum 240 characters).
- First use asks whether the learner wants to open the existing Placement Diagnostic or skip it. The Robot only launches the assessment after explicit selection; it does not inspect the answers or result.
- Keyword-based local intent matching routes supported subjects to static feature help or app navigation. FAQ keywords are checked before broad feature routes.
- Unsupported free-text questions receive a transparent fallback stating that the local companion does not understand all unrestricted questions.
- Idle bubble: first notice after 90 seconds; later notices after five and ten minutes; maximum three per rolling hour. Each bubble auto-dismisses after 14 seconds. Dismiss snoozes for ten minutes. A separate setting mutes proactive idle prompts while keeping the launcher and chat available.
- Idle notices are suppressed if the tab is hidden/unfocused, Robot panel is open, an input is active, speech is playing, a modal or learning-focus surface is open, an install prompt/mobile menu is visible, or a timed Mock Exam is running.
- `prefers-reduced-motion` disables nonessential animations. Layout adjusts for desktop, mobile, tablet and short landscape screens.

## Strict data and privacy boundary

Robot Buddy reads only its bundled `data/robot/robot-library.json` and current UI visibility/focus state needed for interruption safeguards. It does not read learner progress, personal vocabulary, question answers, Flashcard/Grammar/Reading/Listening/Foundation records, Placement results, Mock history/scores, IndexedDB or learning localStorage keys. It does not subscribe to learning-result events. It does not call Google AI, a hosted model, external API, server, analytics or remote endpoint. Chat transcript stays in runtime memory and is discarded when the page reloads.

The only persistent Robot settings are stored under `toeic:robot-buddy-settings:v1`: onboarding choice (`start` or `skip`) and proactive-idle mute. A one-time v2.83 migration reads only `toeic:robot-companion-onboarding:v1` to preserve the prior onboarding choice. No chat text is stored. Existing user learning data and IndexedDB v1 are untouched.

## Test contract

`tools/tests/robot-buddy.mjs` verifies message counts/uniqueness, feature and FAQ routing, identity and fallback language, head-only UI, emotion styles, idle safeguards, first-run Placement handoff, Service Worker cache inclusion and absence of learner-progress data access. Separate compatibility tests confirm the retired progress-aware implementation and old Quick Help file are no-op tombstones.

## Limitations

This is not generative AI, does not learn from the user, does not perform learner assessment and does not answer arbitrary natural-language questions. Its responses are selected from authored local content based on limited keyword matching. Repeated or overlapping messages remain acceptable by design; the 500 core library strings are unique within this release.
