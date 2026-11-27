# Change Manifest — TOEIC Dictionary v2.95.75

Baseline: preserved local `v2.95.74` source snapshot (ahead of GitHub `candidate` `cfae6ce` at `v2.95.73`; `main` untouched).

- Added source & regression test files: **5**
- Added `v2.95.75` audit & release report files: **23** (total added: **28**)
- Modified source, data, config, test & doc files: **29** (+2 refreshed non-versioned backlog snapshots: `docs/reports/RELATED_GLOSSARY_BACKLOG.md`, `docs/reports/related-glossary-backlog.json`)
- Deleted: **0**
- Final packagable source inventory (matching `tools/package_source.py` + `.gitignore` exclusion rules): **1,550** files

## Added paths

### Audit tooling & Python tests
- `tools/audit-seven-part-content.py`
- `tools/audit-learning-outcome-evidence.py`
- `tools/audit-mock-readiness.py`
- `tools/tests/test_seven_part_content_audit.py`
- `tools/tests/test_mock_readiness_audit.py`

### `v2.95.75` release & audit reports (`docs/reports/`)
- `docs/reports/TOEIC_SEVEN_PART_CONTENT_AUDIT_v2.95.75.md`
- `docs/reports/TOEIC_LEARNING_OUTCOME_EVIDENCE_v2.95.75.md`
- `docs/reports/TOEIC_MOCK_READINESS_v2.95.75.md`
- `docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.75.md`
- `docs/reports/TOEIC_CONTENT_COVERAGE_v2.95.75.md`
- `docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.75.md`
- `docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.95.75.md`
- `docs/reports/TOEIC_ANSWER_LEAKAGE_DIAGNOSTIC_v2.95.75.md`
- `docs/reports/TOEIC_ITEM_COMPLEXITY_REVIEW_v2.95.75.md`
- `docs/reports/TOEIC_LISTENING_READINESS_v2.95.75.md`
- `docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.75.md`
- `docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.75.md`
- `docs/reports/WORD_FAMILY_GRAPH_AUDIT_v2.95.75.json`
- `docs/reports/PROJECT_PROGRESS_v2.95.75.md`
- `docs/reports/PROJECT_PROGRESS_v2.95.75.json`
- `docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v2.95.75.md`
- `docs/reports/major-release-quality-audit-v2.95.75.json`
- `docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.75.md`
- `docs/reports/DATA_DIFF_v2.95.75.md`
- `docs/reports/CHANGE_MANIFEST_v2.95.75.md`
- `docs/reports/PACKAGE_VERIFICATION_v2.95.75.md`
- `docs/reports/COMMAND_LOG_INDEX_v2.95.75.md`
- `docs/reports/TEST_REPORT_TOEIC_Dictionary_v2.95.75.md`

## Modified paths

### Data & curriculum metadata
- `data/manifest.json`
- `data/learning-path/objective-outcomes.json`

### Application runtime & hardening (`assets/js/`)
- `assets/js/app.js`
- `assets/js/mock-engine.js`
- `assets/js/robot-learning-insights.js`
- `assets/js/mock-score-readiness.js`
- `assets/js/learning-outcome-progress.js`

### Release shell, package & CI
- `package.json`
- `index.html`
- `sw.js`
- `.github/workflows/validate-data.yml`

### Tooling & tests (`tools/`)
- `tools/audit-toeic-coverage.py`
- `tools/editorial_inventory.py`
- `tools/audit-learning-outcomes.py`
- `tools/audit-distractors.py`
- `tools/build-editorial-review-queue.py`
- `tools/sync-version.py`
- `tools/tests/test_learning_outcomes.py`
- `tools/tests/test_sync_version.py`
- `tools/tests/test_release_shell_coherence.py`
- `tools/tests/test_project_progress_index.py`
- `tools/tests/robot-learning-insights.mjs`
- `tools/tests/mock-score-readiness.mjs`
- `tools/tests/learning-outcome-progress.mjs`
- `tools/tests/learner-data-backup.mjs`

### Documentation (`docs/`)
- `docs/CHANGELOG.md`
- `docs/MASTER_STATUS.md`
- `docs/README.md`
- `docs/versions/CURRENT_VERSION.md`

## Change boundaries

- Canonical vocabulary IDs/headwords/senses/relations (`1,181` headwords), Related Glossary meanings (`567` rows), TOEIC question/passage/choice IDs, and answer keys remain untouched.
- Mock reserve exclusions (`193` Listening, `87` Part 7, `80` Separate Part 5) remain strictly enforced.
- IndexedDB v1 stores/schema, UI/UX layout, and static PWA offline-first architecture remain unchanged.
