# TOEIC Dictionary v2.82.0 — Documentation

- Current product source: `v2.82.0` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.81.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md` (single current roadmap/status source).
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.82.0.md`.
- Restored legacy Google AI scope: `reports/RESTORE_LEGACY_GOOGLE_AI_v2.82.0.md`.
- A2 writing portfolio report: `reports/A2_WRITING_PORTFOLIO_v2.81.0.md`.
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.82.0.md`.
- Generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.82.0.md`.
- Previous release test/feature records: `reports/` entries tagged v2.81.0.
- Older detailed records are consolidated in `archive/PROJECT_HISTORY.md`.
- TOEIC remains the primary track; IELTS remains deferred until TOEIC development/acceptance gates are met and the owner approves a phase change.
- Foundation pathway has 10 Pre-A1/A1 lessons and 13 A2 lessons. A2 has 13 Reading passages / 39 questions, 13 four-turn device-TTS Listening dialogues / 39 questions and 13 contextual writing tasks with guided revisions. v2.81.0 added a local-only writing portfolio. v2.82.0 restores pre-v2.80 feature-level Google AI actions (word lookup, practice, Grammar, Reading and Listening) as explicit external handoffs, while the newer floating-assistant Google AI flow from v2.80 stays removed. Local Quick Help remains offline-only.
- Foundation production history remains device-local under `toeic:foundation-progress:v1`. Previous response versions are stored for newly captured attempts; old records are not backfilled. Self-review is not automated grading or learner mastery.
- Foundation outcome evidence covers recognition, contextual learner-written production/self-report and 1/3-day delayed recall; it does not certify learner mastery.
- Foundation Listening uses browser SpeechSynthesis; it is synthesized learning material, not ETS or recorded native-speaker audio.
- Listening Part 1: JPG-only photo contract; all nine optimized images are embedded, 4:3 landscape, <=400,000 bytes and retain source attribution. `ai-generated` source strings, where present, identify asset provenance only and do not activate an AI feature.
- Vocabulary: 1,137 stable headwords; quantity coverage is 37.9% of the 3,000 minimum and 22.7% of the 5,000 planning ceiling; quality review remains separate.
- Profile repair and progress storage remain additive; IndexedDB remains v1 with no reset/migration in this release.
