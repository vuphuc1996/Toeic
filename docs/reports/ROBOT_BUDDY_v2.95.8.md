# Robot Buddy — v2.95.8 behavior and preservation

## Preserved features

- Head-only mascot with the existing emotion states and lightweight animation behavior.
- Static offline dialogue library, supported intent/FAQ responses, feature shortcuts and quick prompts.
- First-use Placement Diagnostic consent with an explicit skip option.
- Idle encouragement/caring reminders, mute control and interruption safeguards.
- Context-aware guidance using the active page and current vocabulary word, Flashcard, practice question, Grammar lesson, Reading item, Listening item or Foundation lesson.
- Optional Learning Insights using a local, read-only in-memory snapshot supplied by the application.
- One visual progress dashboard with Cần học / Cần luyện / Cần ôn totals, module coverage/evidence notes and relevant navigation actions.
- Existing Google AI feature-level actions remain separate and user-initiated.

## Correct behavior

- Robot Buddy itself does not open IndexedDB or localStorage. The app passes only the already-loaded snapshot to the pure `robot-learning-insights.js` aggregator when Learning Insights is enabled.
- The aggregator does not write learner records, migrate data, upload learner information or call external APIs.
- Turning Learning Insights off stops progress analysis; normal dialogue, help, shortcuts, Placement onboarding and generic reminders remain available.
- Progress analysis renders one dashboard. Do not append a second prose report repeating the same totals or module counts.
- Idle nudges can reference the current learning item with a short study suggestion; when no current item is available they use the static dialogue library.
- Page-only action buttons are delegated, close the Buddy panel and navigate to a valid existing page.
- Robot Buddy is a scripted companion, not an unrestricted generative chatbot. Unsupported questions must receive an honest limitation response.

## v2.95.7 comparison decision

The v2.95.7 privacy correction removed the insight module, dashboard, toggle and progress-derived nudges. This release does not retain that removal because it conflicts with the approved opt-in local learning-support requirement. Its documentation consolidation, interaction/idle safeguards and maintenance improvements are retained where compatible.
