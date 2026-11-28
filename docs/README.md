# TOEIC Dictionary v2.95.86 — Project Documentation

This documentation describes the current TOEIC-first GitHub Pages candidate. Source changes and release evidence are tracked separately from hosted CI, Pages deployment, installed-PWA behavior and physical-device acceptance.

- Current release: `2.95.86`.
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.86.md`.
- Current project progress: `reports/PROJECT_PROGRESS_v2.95.86.md` — provisional weighted measurable curriculum-build index **77.16%**, not learner mastery or TOEIC score readiness.
- Current change manifest: `reports/CHANGE_MANIFEST_v2.95.86.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.86.md`.
- Current Full-Mock readiness: `reports/TOEIC_MOCK_READINESS_v2.95.86.md` — Listening approved 102 / reserve 196; Reading approved 200 / Part 7 reserve 87; Separate Part 5 review-only 80.
- Current Listening pool readiness: `reports/TOEIC_LISTENING_READINESS_v2.95.86.md` — approved/reserve counts by part and the conditional two-form ceiling after independent review.
- Current Part 1 independent-review queue: `reports/PART1_PHOTO_BATCH_018_REVIEW_HANDOFF_v2.95.86.md`.
- Current major release quality audit: `reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.86.md`.
- v2.95.86 Batch 018 adds three Part 1 photo-description practice resources (construction plans, laboratory microscope and supermarket shelf) using existing repository JPG assets. Part 1 now has 12 resources/questions: 8 currently eligible and 4 pending independent review. The new three resources and questions are fail-closed and excluded from Mock.
- Listening resource inventory advances 145 → 148; Listening questions 308 → 311; Listening reserve 193 → 196. The approved Mock Listening pool remains **102**. No existing question, choice or answer IDs were changed.
- The new photo resources are registered in the canonical objective-resource map but are not added to the learning-outcome criterion map. Part 1 visual/detail mappings remain 8 each; `listening-part-1-paraphrase-recognition` remains deliberately uninstrumented.
- v2.95.85 source acceptance record: `reports/RELEASE_ACCEPTANCE_v2.95.85.md` — the project owner confirmed **865/865** tests, build/compilation and syntax-lint PASS for exact source HEAD `7b8d80f1eef1523b5c2f31f0361a51c90011da7e`. This earlier result is not transferred to v2.95.86.
- Learning outcome evidence: `reports/TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.85.md` — 26/27 TOEIC criteria instrumented across 1,163 stable question-to-criterion links and 651 unique stable question IDs; one criterion remains deliberately uninstrumented.
- Historical GitHub Validate / Pages evidence applies only to the exact historical commit SHAs recorded in the v2.95.85 acceptance documentation. It must not be generalized to v2.95.86.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Master project status: `MASTER_STATUS.md`.
- Assessment completion and draft/commit semantics: `ASSESSMENT_FLOW.md`.
- Changelog: `CHANGELOG.md`.

## Content and learner-data boundaries

- Existing canonical vocabulary IDs/headwords/senses and question/choice IDs/answer keys are preserved.
- All new Batch 018 Part 1 resources remain `reserve-pending-independent-review`, which is the resource-level Mock gate. Do not set question-level `mockEligible: false` on reserve questions; that flag is reserved for practice-only questions. No new item is treated as independently reviewed or approved for Mock.
- Listening reserve (196), Reading Part 7 reserve (87) and Separate Part 5 review-only (80) remain excluded from Mock.
- Learner IndexedDB v1 schema and local records are unchanged; no migration is introduced.
- UI/UX layout, navigation, Robot Buddy access boundary and GitHub Pages-only/offline architecture remain unchanged. No backend or Cloudflare service is introduced.
- Criterion evidence remains in the learner-local `objectiveProgress` ledger; Batch 018 adds no new criterion mapping.

## Acceptance boundary

Source release, candidate CI, Pages deployment, installed-PWA cache/offline propagation and physical-device QA are separate acceptance gates. The 865-test result belongs to v2.95.85 only. v2.95.86 remains pending exact-SHA CI and Pages evidence; no merge to `main` or production deployment is authorized.
