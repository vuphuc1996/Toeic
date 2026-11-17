# TOEIC Dictionary v2.88.0 — Documentation

- Current product source: `v2.88.0` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.87.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md` (single current roadmap/status source).
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.88.0.md`.
- Robot Buddy specification: `reports/ROBOT_BUDDY_v2.86.0.md`.
- Progress baseline/snapshot: `reports/PROJECT_PROGRESS_BASELINE_v2.83.0.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.83.0.md`.
- Older detailed records are consolidated in `archive/PROJECT_HISTORY.md`; release-level history remains in `CHANGELOG.md`.
- TOEIC remains the primary track; IELTS remains deferred until TOEIC development/acceptance gates are met and the owner approves a phase change.
- Foundation pathway: 10 Pre-A1/A1 lessons and 13 A2 lessons; 23 Reading resources / 59 questions; 23 Listening resources / 59 questions; 26 contextual A2 writing tasks (13 foundational + 13 extended), each with separate local evidence/revision history, a writing portfolio and device-local Markdown export. The 13 extended tasks remain pending independent editorial review.
- Google AI: only the original v2.79 feature-level user-triggered actions are retained for vocabulary lookup, practice answer/review, Grammar, Reading and Listening; there is no shared contextual AI assistant or copy/transfer workflow.
- Robot Buddy v2.86.0: head-only animated companion with 500 offline dialogue variants, 59 feature-help messages for 12 destinations (11 menu areas plus Placement), six FAQs and 16 quick prompts that remain available throughout the current chat session. The message area scrolls independently from the prompt menu. It can analyze already-loaded local learner progress in read-only mode; no learning data is sent outside the device. The user can disable progress analysis while retaining dialogue and help. Evidence-based insight replies can show up to four direct links to the corresponding existing learning modules.
- Mock Exam icons: clipboard/check, bolt, stopwatch and trophy; the old clock glyph is retired.
- Foundation production history remains device-local under `toeic:foundation-progress:v1`. Revision/self-review is not automated grading or learner mastery.
- Listening Part 1: JPG-only photo contract; all nine optimized images are embedded, 4:3 landscape, <=400,000 bytes and retain source attribution. `ai-generated` source strings, where present, identify asset provenance only.
- Vocabulary: 1,137 stable headwords; quantity coverage is 37.9% of the 3,000 minimum and 22.7% of the 5,000 planning ceiling; quality review remains separate.
- Robot Buddy uses `toeic:robot-buddy-settings:v1` for onboarding choice and idle-reminder mute preference. A one-time migration reads only the old v2.83 onboarding-choice key `toeic:robot-companion-onboarding:v1`. Learning progress is passed to the insights aggregator as an in-memory read-only snapshot; Robot itself does not open IndexedDB or localStorage. Chat history remains in memory for the current session. Existing learner progress keys and IndexedDB v1 remain unchanged.

- SW002 validation: `assets/js/robot-buddy.js`, `assets/js/robot-learning-insights.js`, `data/robot/robot-library.json`, and the legacy no-op tombstones are included in Service Worker `REQUIRED` and `APP_SHELL`.
