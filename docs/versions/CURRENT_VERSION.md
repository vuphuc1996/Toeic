# Current version

- Version: **v2.78.0**
- Status: local release candidate. Adds 13 contextual written-production tasks to A2; each has a workplace prompt, scaffold, task-specific self-review rubric, hidden model answer and eight-word minimum.
- Source: `data/manifest.json`
- Master: `docs/MASTER_STATUS.md`
- Changelog: `docs/CHANGELOG.md`
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.78.0.md`
- Progress baseline: `reports/PROJECT_PROGRESS_BASELINE_v2.78.0.md`
- Generated progress snapshot: `reports/PROJECT_PROGRESS_SNAPSHOT_v2.78.0.md`
- Production task report: `reports/FOUNDATION_A2_PRODUCTION_TASKS_v2.78.0.md`
- Production task integrity baseline: `tools/foundation-a2-production-baseline-v2.78.0.json`
- Previous release: v2.77.0.
- Foundation: 23 lessons (10 Pre-A1/A1 + 13 A2); 23 Reading resources / 59 questions; 23 Listening resources / 59 questions.
- A2 written production: 13/13 task definitions; responses are learner-authored and self-reported, not automatically graded. New evidence uses separate `::produce1` IDs; previous `::apply1` data remains in the local progress record.
- Vocabulary: 1,137 headwords; 1,044/1,137 US IPA populated (91.8%; 93 remain blank); word-family 276/1,137 (24.3%) and 374 directed links. Targets: 37.9% of 3,000 minimum and 22.7% of 5,000 planning ceiling.
- Objective-resource map: 11 objectives; 294/294 links. Outcome registry: 33 criteria defined; 6/33 have evidence paths.
- Part 1: nine 1448×1086 4:3 JPGs, each below 400,000 bytes.
- No IndexedDB v1 schema/store migration, Foundation localStorage key change, learner-progress reset or TOEIC Mock-pool change.
- Independent linguistic review, remote GitHub Actions, Pages deployment and physical-device QA remain unverified.
