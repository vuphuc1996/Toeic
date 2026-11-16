# Test & Release Report — TOEIC Dictionary v2.84.0

**Release:** v2.84.0 — Head-only Robot Buddy & Offline Dialogue Library  
**Date:** 2026-11-16  
**Base:** v2.83.0 Full Source  
**Release state:** Local full-source release candidate; remote GitHub Actions, Pages deployment and physical-device QA remain pending.

## Release summary

- Replaced the progress-aware Robot from v2.83.0 with a head-only animated SVG companion.
- Bundled 500 unique authored messages in seven categories (greeting 60, encouragement 100, caring 60, learning 80, help 100, reaction 60, rest 40), plus 55 feature-help messages for 11 destinations, six FAQs and 12 quick prompts.
- Added bounded keyword intent detection, local static replies, feature navigation and an explicit fallback for unsupported natural-language questions. This is not a generative AI chatbot.
- Added proactive idle prompts, a compact chat panel, animated emotions, mute/snooze controls and interruption safeguards.
- Robot does not read learning progress, personal vocabulary, IndexedDB, Placement/Mock results or learner stores. It does not call Google AI, an API, a server or a hosted model. Chat history is not persisted.
- Preserved existing Placement only as an explicit user-triggered destination from first-run onboarding. The Robot does not read assessment results.
- Preserved the v2.79 feature-level Google AI actions independently of Robot Buddy.
- Migrates only the v2.83 onboarding preference key so existing users are not asked the first-use question again; no learning data is migrated.

## Automated regression results

| Gate | Result |
|---|---|
| JavaScript regression suites | **28/28 PASS** |
| Selected Python regression tests | **62/62 PASS across 9 modules** |
| Python syntax compilation | PASS — all Python files under `tools/` |
| JavaScript syntax | PASS — all 15 `assets/js/*.js` files and `sw.js` |
| HTML ID audit | PASS — 291 IDs, 0 duplicates |
| CSS parse | PASS — `app.css` and `design-system.css`, 0 parse errors |
| Robot dialogue inventory | PASS — 500/500 unique core messages; 11 feature groups; 6 FAQs; 12 quick prompts |
| Design profile | PASS — 54 tokens / 395 legacy typography selector groups |
| Version synchronization | PASS — manifest, app, service worker, index and docs at v2.84.0 |
| Service Worker/PWA resource gate | PASS — required and app-shell resources exist, including Robot runtime and JSON library |

Python regression selection: design profile (6), design system (19), PWA readiness (3), version sync (12), Placement diagnostic (6), responsive layout (5), learning-surface consistency (5), CI coverage (2), project-progress reporting (4). The full Python discovery command was not treated as a release pass; the selected modules completed independently.

## Data and content validators

- `python tools/validate-data.py`: PASS — 1,137 records; 0 ERROR; 0 legacy WARNING. ID set adds 209 vs prior baseline, removes 0; ID-set SHA-256 prefix `f8a47a88f6a3257b`.
- `python tools/validate-learning-content.py`: PASS — 0 errors / 0 warnings. Listening 107 units / 201 questions; Reading 51 / 200; Grammar 33 / 86; standalone Part 5 practice 80 questions (pending independent review).
- `python tools/validate-part1-photo-assets.py`: PASS — 9/9 photo assets; 0 missing-photo warnings.
- `python tools/audit-objective-resources.py`: PASS — 11 objectives; 294/294 linked resources.
- `python tools/audit-learning-outcomes.py`: PASS — 11/11 objectives, 33 criteria, 6/33 evidence paths; Foundation instrumentation 6/6. Instrumentation is not learner mastery.
- `python tools/audit-question-evidence.py`: PASS — 401 indexed questions in audit scope.
- `python tools/audit-distractors.py`: PASS — structural audit of 177 questions plus 72 reserve structural checks; answer keys and unique choices valid in review scope.

## Robot Buddy acceptance contract

- One head-only SVG mascot; no body, arms or legs.
- Emotional states: happy, thinking, celebration, caring, sleepy, greeting, surprised, motivation, concerned, playful, listening and speaking.
- Idle: first prompt after 90 seconds, then 5- and 10-minute spacing; at most three prompts per rolling hour; auto-dismiss 14 seconds; dismiss snoozes; mute preference is available.
- Idle prompts are suppressed for hidden/unfocused tabs, open Robot panel, text entry, active learning focus/modal, speech playback, install/mobile menus and timed Mock Exam.
- The first-use Placement question is optional; a choice is required before opening the existing diagnostic. The user can skip.
- Chat transcript is held in session memory only. Text is rendered safely via text nodes; input length is limited to 240 characters.
- The only current persistent Robot preference key is `toeic:robot-buddy-settings:v1`. One-time migration reads only `toeic:robot-companion-onboarding:v1` from v2.83 to preserve onboarding choice.

## Not verified

- Actual GitHub Actions result after push.
- GitHub Pages production deployment and production Service Worker update behavior.
- Visual/browser testing, animation feel, keyboard/screen-reader checks and real-device testing on laptop, iPhone, Android and tablet. No browser automation package was available in this environment.
- Remote/offline testing after a clean browser install.

Do not mark remote CI, production deployment or physical-device QA as complete until tested on the target environment.
