# TOEIC Dictionary v2.82.1 — Documentation

- Current product source: `v2.82.1` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.82.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md` (single current roadmap/status source).
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.82.1.md`.
- Scope correction (preserve v2.79 Google AI; remove v2.80 Quick Help word search): `reports/REMOVE_QUICK_HELP_WORD_SEARCH_v2.82.1.md`.
- A2 writing portfolio history: `archive/PROJECT_HISTORY.md` (v2.81.0 entry).
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.82.1.md`.
- Generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.82.1.md`.
- Previous release test/feature records: `reports/` entries tagged v2.82.0.
- Older detailed records are consolidated in `archive/PROJECT_HISTORY.md`.
- TOEIC remains the primary track; IELTS remains deferred until TOEIC development/acceptance gates are met and the owner approves a phase change.
- Foundation pathway has 10 Pre-A1/A1 lessons and 13 A2 lessons. A2 has 13 Reading passages / 39 questions, 13 four-turn device-TTS Listening dialogues / 39 questions and 13 contextual writing tasks with guided revisions. v2.81.0 added a local-only writing portfolio. v2.82.1 retains every pre-v2.80 Google AI action from v2.79 as explicit external handoffs, while removing the v2.80 floating assistant and prefix/masked-letter search in Quick Help. Local Quick Help remains an offline navigation/Placement guide only.
- Foundation production history remains device-local under `toeic:foundation-progress:v1`. Previous response versions are stored for newly captured attempts; old records are not backfilled. Self-review is not automated grading or learner mastery.
- Foundation outcome evidence covers recognition, contextual learner-written production/self-report and 1/3-day delayed recall; it does not certify learner mastery.
- Foundation Listening uses browser SpeechSynthesis; it is synthesized learning material, not ETS or recorded native-speaker audio.
- Listening Part 1: JPG-only photo contract; all nine optimized images are embedded, 4:3 landscape, <=400,000 bytes and retain source attribution. `ai-generated` source strings, where present, identify asset provenance only and do not activate an AI feature.
- Vocabulary: 1,137 stable headwords; quantity coverage is 37.9% of the 3,000 minimum and 22.7% of the 5,000 planning ceiling; quality review remains separate.
- Profile repair and progress storage remain additive; IndexedDB remains v1 with no reset/migration in this release.
