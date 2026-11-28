# TOEIC Dictionary v2.95.80 — Project Documentation

This documentation describes the current TOEIC-first GitHub Pages candidate. Source changes and release evidence are tracked separately from hosted CI, Pages deployment, installed-PWA behavior and physical-device acceptance.

- Current release: `2.95.80`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.80.md`.
- Predecessor v2.95.79 acceptance: candidate source commit `76ca52457929493a2a587f7673367bc29eeace49` passed Validate [run 46105814708](https://github.com/vuphuc1996/Toeic/actions/runs/46105814708) and Pages [run 46105814298](https://github.com/vuphuc1996/Toeic/actions/runs/46105814298). v2.95.80 hosted acceptance is pending its own exact-commit runs.
- Learning outcome evidence matrix: `reports/TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.80.md` — 22/27 TOEIC criteria mapped to 1,103 stable question-to-criterion links across 638 unique stable question IDs; five criteria remain deliberately uninstrumented.
- Criterion map audit: `../tools/audit-objective-criterion-map.py` — checks exact question IDs, question indices, Listening reserve exclusion, Part 7 multi-document source quotes and review gates.
- Criterion mapping remediation: `reports/CRITERION_MAPPING_REMEDIATION_v2.95.80.md` — 21 additional links; explains why below-minimum criteria remain below 10.
- Candidate change manifest: `reports/CHANGE_MANIFEST_v2.95.80.md`.
- Candidate command log: `reports/COMMAND_LOG_INDEX_v2.95.80.md`.
- Project progress dashboard: `reports/PROJECT_PROGRESS_v2.95.80.md` — provisional weighted build index remains 73.73%; mapping depth does not increase the instrumented-criterion count.
- Migration compatibility audit: `reports/MIGRATION_COMPATIBILITY_v2.95.77.md` — reconciliation of all 8 historical migration repair profiles for the 1,221-word inventory.
- Vocabulary Batch 028: `reports/VOCABULARY_BATCH_028_v2.95.76.md` — 40 original TOEIC workplace headwords across Contracts / Legal Administration and Facilities / Property Maintenance.
- Listening translation remediation: `reports/LISTENING_TRANSLATION_REMEDIATION_v2.95.76.md` — 8 existing Part 3/4 units receive Vietnamese transcript translations.
- TOEIC content coverage: `reports/TOEIC_CONTENT_COVERAGE_v2.95.76.md` — vocabulary inventory 1,221; Listening transcript translations 295/295.
- Project progress history v2.95.76: `reports/PROJECT_PROGRESS_v2.95.76.md` — prior weighted build index 57.07%.
- Major release quality audit: `reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.76.md`.
- Change manifest: `reports/CHANGE_MANIFEST_v2.95.80.md`.
- Package verification: `reports/PACKAGE_VERIFICATION_v2.95.77.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.80.md`.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Prior 7-Part assessment and Mock-readiness baseline: `reports/TOEIC_SEVEN_PART_CONTENT_AUDIT_v2.95.75.md`, `reports/TOEIC_MOCK_READINESS_v2.95.75.md`.
- Master project status: `MASTER_STATUS.md`.
- Assessment completion and draft/commit semantics: `ASSESSMENT_FLOW.md`.
- Changelog: `CHANGELOG.md`.


## Content and learner-data boundaries

- The 40 new headwords are original editorial additions. IPA is left blank pending source verification; CEFR labels are editorial estimates; no Word Family links are inferred.
- The 8 Listening changes add only unit-level `transcriptTranslation`. Existing transcript segments, resource/question/choice IDs, answer keys and editorial status remain unchanged.
- Listening reserve (193), Reading Part 7 reserve (87) and Separate Part 5 reserve (80) remain excluded from Mock.
- Existing canonical vocabulary IDs/headwords/senses, learner IndexedDB v1 schema and learner records are preserved; 40 new canonical IDs are appended.
- UI/UX layout, navigation, Robot Buddy access boundary and GitHub Pages-only/offline architecture remain unchanged. No backend or Cloudflare service was introduced.
- v2.95.78 adds criterion evidence to the existing `objectiveProgress` ledger without an IndexedDB schema migration. Grammar and Reading Part 5 explanation rubrics are optional learner self-reports.

## Acceptance boundary

Source release, candidate CI, Pages deployment, installed-PWA cache/offline propagation and physical-device QA are separate acceptance gates. Do not infer one from another.
