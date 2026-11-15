# TOEIC Dictionary v2.66.1 — Documentation

- Current candidate: `v2.66.1` — `versions/CURRENT_VERSION.md`.
- Previous release: `v2.66.0` — `versions/PREVIOUS_VERSION.md`.
- Master status: `MASTER_STATUS.md`.
- Release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.66.1.md`.
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.66.1.md`.
- Generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.66.1.md`.
- Assessment flow: `ASSESSMENT_FLOW.md`; selection drafts stay ungraded until full completion and explicit confirmation.
- Mock Exam: time-weighted schedule, visible current location, automatic focus transitions, spoken lead-ins, and no repeated audio within the same Listening group.
- Listening Part 1: fixed 2-second TTS preparation, topic title, 1-second title gap, common lead-in, 1-second lead-in gap, separate A/B/C/D labels, 1.5-second label gap and 1.3-second inter-description gap. Practice and Mock Exam use the same player.
- GitHub CI: `test_distractor_quality.py` verifies draft selection and post-confirmation commit rather than pre-deferred immediate scoring.
- Dashboard: separate full-width rows by exam and skill, with independent Part grids; future Writing/Speaking/IELTS tracks can be added without changing the layout model.
- Design governance: `design/design-profile.json`, `DESIGN_SYSTEM.md`, `DESIGN_BRIEF_TEMPLATE.md`.
- Existing IndexedDB schema, question IDs, answer keys, learner progress and personal vocabulary are preserved.
- Deployment status: local candidate only; strict Part 1 asset validator remains blocked by eight missing original JPG files inherited from earlier source archives.
