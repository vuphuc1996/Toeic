# Current Version

- Current source: **v2.95.10** — fixed 10-card Flashcard sessions, protected vocabulary ID baseline, guarded content patches and user-approved PWA updates.
- Based on: v2.95.9 Robot Buddy progressive response streaming and locally composed context-aware replies.
- Release package: `TOEIC_Dictionary_v2.95.10_FullSource.zip`.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.10.md`.
- Audit assessment: `reports/CLAUDE_AUDIT_ASSESSMENT_v2.95.10.md`.
- User acceptance checklist: `reports/USER_ACCEPTANCE_TEST_v2.95.10.md`.
- TOEIC Listening & Reading remains the active exam-development scope. Foundation B1 is blueprint-only; Speaking/Writing and IELTS remain deferred.
- Flashcard sessions have one fixed maximum of 10 cards. The retired 5-card option has been removed from the UI and runtime.
- New Service Worker versions wait for explicit user approval after the first installation. Real-browser and two-tab acceptance remains pending.
- No learner record, vocabulary identity, question, answer key, IndexedDB schema or localStorage learner key was reset or migrated. No GitHub push or deployment was performed in this workspace.
