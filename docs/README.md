# TOEIC Dictionary v2.83.0 — Documentation

- Current product source: `v2.83.0` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.82.1` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md` (single current roadmap/status source).
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.83.0.md`.
- Robot Buddy specification: `reports/LEARNING_COMPANION_ROBOT_v2.83.0.md`.
- Progress baseline/snapshot: `reports/PROJECT_PROGRESS_BASELINE_v2.83.0.md` and `reports/PROJECT_PROGRESS_SNAPSHOT_v2.83.0.md`.
- Older detailed records are consolidated in `archive/PROJECT_HISTORY.md`; release-level history remains in `CHANGELOG.md`.
- TOEIC remains the primary track; IELTS remains deferred until TOEIC development/acceptance gates are met and the owner approves a phase change.
- Foundation pathway: 10 Pre-A1/A1 lessons and 13 A2 lessons; 23 Reading resources / 59 questions; 23 Listening resources / 59 questions; 13 contextual A2 writing tasks with guided revision and a local portfolio.
- Google AI: only the original v2.79 feature-level user-triggered actions are retained for vocabulary lookup, practice answer/review, Grammar, Reading and Listening; there is no shared contextual AI assistant or copy/transfer workflow.
- Robot Buddy v2.83: local progress-aware companion, first-run Placement choice, milestone congratulations and direct review suggestions. It uses deterministic local summaries only; no generative AI model, network API or external transfer is involved. It replaces the usage guide and does not contain vocabulary search/letter-completion.
- Mock Exam icons: clipboard/check, bolt, stopwatch and trophy; the old clock glyph is retired.
- Foundation production history remains device-local under `toeic:foundation-progress:v1`. Revision/self-review is not automated grading or learner mastery.
- Listening Part 1: JPG-only photo contract; all nine optimized images are embedded, 4:3 landscape, <=400,000 bytes and retain source attribution. `ai-generated` source strings, where present, identify asset provenance only.
- Vocabulary: 1,137 stable headwords; quantity coverage is 37.9% of the 3,000 minimum and 22.7% of the 5,000 planning ceiling; quality review remains separate.
- The only new localStorage key in v2.83 is `toeic:robot-companion-onboarding:v1`. Existing learner progress keys and IndexedDB v1 remain unchanged.

- SW002 validation: `assets/js/learning-assistant.js` and the no-op `assets/js/quick-help.js` are both included in Service Worker `REQUIRED` and `APP_SHELL`; `python tools/validate-data.py` passes with zero errors/warnings.
