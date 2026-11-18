# TOEIC Dictionary v2.93.0 — Documentation

- Current product source: `v2.93.0` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.92.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md` (single current roadmap/status source).
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.93.0.md`.
- Robot Buddy specification: `reports/ROBOT_BUDDY_v2.86.0.md`.
- Progress baseline/snapshot: `reports/PROJECT_PROGRESS_BASELINE_v2.83.0.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.83.0.md`.
- Current progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.93.0.md`.
- Overall roadmap assessment: `reports/PROJECT_ROADMAP_STATUS_v2.93.0.md`.
- A2 extended Listening review handoff: `reports/FOUNDATION_A2_LISTENING_REVIEW_CHECKLIST_v2.91.0.md`.
- A2 extended Listening technical report: `reports/FOUNDATION_A2_EXTENDED_LISTENING_v2.91.0.md`.
- Older detailed records are consolidated in `archive/PROJECT_HISTORY.md`; release-level history remains in `CHANGELOG.md`.
- TOEIC remains the primary track; TOEIC Speaking/Writing remain deferred until L/R is complete and accepted; IELTS remains deferred until the later S/W phase is complete and the owner approves a phase change.
- Foundation pathway: 10 Pre-A1/A1 lessons and 13 A2 lessons; 23 core Foundation Reading resources / 59 questions plus 13 supplementary A2 Reading resources / 39 questions and 13 supplementary A2 Listening resources / 39 questions (pending independent editorial review); 23 core Listening resources / 59 questions; 26 contextual A2 writing tasks (13 foundational + 13 extended), each with separate local evidence/revision history, a writing portfolio and device-local Markdown export. The 13 extended writing tasks, 13 supplementary Reading passages (39 questions) and 13 supplementary Listening clips (39 questions) remain pending independent editorial review.
- Google AI: only the original v2.79 feature-level user-triggered actions are retained for vocabulary lookup, practice answer/review, Grammar, Reading and Listening; there is no shared contextual AI assistant or copy/transfer workflow.
- Robot Buddy v2.86.0: head-only animated companion with 500 offline dialogue variants, 59 feature-help messages for 12 destinations (11 menu areas plus Placement), six FAQs and 16 quick prompts that remain available throughout the current chat session. The message area scrolls independently from the prompt menu. It can analyze already-loaded local learner progress in read-only mode; no learning data is sent outside the device. The user can disable progress analysis while retaining dialogue and help. Evidence-based insight replies can show up to four direct links to the corresponding existing learning modules.
- Mock Exam icons: clipboard/check, bolt, stopwatch and trophy; the old clock glyph is retired.
- Foundation production history remains device-local under `toeic:foundation-progress:v1`. Revision/self-review is not automated grading or learner mastery.
- Listening Part 1: JPG-only photo contract; all nine optimized images are embedded, 4:3 landscape, <=400,000 bytes and retain source attribution. `ai-generated` source strings, where present, identify asset provenance only.
- Vocabulary: 1,141 stable headwords; quantity coverage is 38.0% of the 3,000 minimum and 22.8% of the 5,000 planning target; quality review remains separate.
- Robot Buddy uses `toeic:robot-buddy-settings:v1` for onboarding choice and idle-reminder mute preference. A one-time migration reads only the old v2.83 onboarding-choice key `toeic:robot-companion-onboarding:v1`. Learning progress is passed to the insights aggregator as an in-memory read-only snapshot; Robot itself does not open IndexedDB or localStorage. Chat history remains in memory for the current session. Existing learner progress keys and IndexedDB v1 remain unchanged.

- SW002 validation: `assets/js/robot-buddy.js`, `assets/js/robot-learning-insights.js`, `data/robot/robot-library.json`, and the legacy no-op tombstones are included in Service Worker `REQUIRED` and `APP_SHELL`.

- v2.92.0 and v2.93.0 expanded TOEIC Grammar, Listening and Reading. v2.93.0 adds 9 Grammar lessons / 27 exercises, 8 Listening units / 20 questions, 8 Reading Part 7 resources / 36 questions and 4 vocabulary headwords. New Listening/Reading content remains reserve-pending-independent-review and Mock-excluded.
- Foundation B1 is documented as a 12-unit curriculum blueprint only; no B1 learner pathway is implemented or selectable yet.

- v2.92.0 content batch: Grammar 41 lessons / 110 exercises; TOEIC Listening 113 units / 219 questions; TOEIC Reading 57 resources / 227 questions. The 18 v2.92.0 Listening and 27 v2.92.0 Reading questions plus 20 v2.93.0 Listening and 36 v2.93.0 Reading questions remain pending independent review and are excluded from Mock.
- B1 curriculum blueprint: `reports/FOUNDATION_B1_CURRICULUM_BLUEPRINT_v2.92.0.md` (design-only, not a selectable pathway).
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.93.0.md`.
- v2.92.0 independent-review handoff: `reports/TOEIC_BATCH_024_REVIEW_CHECKLIST_v2.92.0.md`.

- v2.93.0 adds the local Full Mock score-readiness evidence tracker. It requires three completed 200-question Full Mocks before showing L/R trends; it never converts accuracy into ETS scaled scores.
- v2.93.0 review handoff: `reports/TOEIC_BATCH_025_REVIEW_CHECKLIST_v2.93.0.md`; score-readiness design: `reports/TOEIC_SCORE_READINESS_v2.93.0.md`.
- TOEIC L/R remain the active scope. B1 remains design-only; Speaking/Writing and IELTS remain deferred.

- Current v2.93.0 inventory: 1,141 vocabulary headwords; 50 Grammar lessons / 137 exercises; 121 Listening units / 239 questions; 65 Reading resources / 263 questions.
- v2.93.0 score readiness uses three completed 200-question Full Mocks to show L/R trends only; it never estimates an ETS scaled score.

- v2.93.0 is the consolidated acceptance-test target. Hold v2.94.0 until the user completes the combined test and feedback is recorded in Master.
- Consolidated user acceptance test: `reports/USER_ACCEPTANCE_TEST_v2.93.0.md`.
