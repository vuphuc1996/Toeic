# Current version

- Version: **v2.82.0**
- Status: current GitHub Pages product source; local source, tests and packages verified in this development session. Remote Actions/Pages/device behavior are not claimed.
- Source of truth: `data/manifest.json`
- Master: `docs/MASTER_STATUS.md`
- Changelog: `docs/CHANGELOG.md`
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.82.0.md`
- Restored legacy Google AI scope: `reports/RESTORE_LEGACY_GOOGLE_AI_v2.82.0.md`
- A2 writing portfolio: `reports/A2_WRITING_PORTFOLIO_v2.81.0.md`
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.82.0.md`
- Progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.82.0.md`
- Previous release: v2.81.0.
- Foundation: 23 lessons (10 Pre-A1/A1 + 13 A2); 23 Reading resources / 59 questions; 23 Listening resources / 59 questions; 13 A2 contextual writing tasks with guided revisions and local portfolio.
- Vocabulary: 1,137 canonical headwords; Quick Help searches existing records only, using local masked completion.
- Legacy Google AI Mode actions from v2.79.0 are restored for word lookup, practice answer/review, Grammar, Reading and Listening. They are explicit external handoffs; no embedded model/API/backend is used.
- The newer v2.80 floating assistant's contextual Google AI follow-up/copy/transfer is not present. Quick Help remains local-only.
- No new localStorage key, IndexedDB v1 migration, server-side storage or learner progress reset is introduced.
- Mock exam quick/half/full modes keep the refreshed SVG icons; Quick Help is compact on small screens and hidden during active timed mock exams.
