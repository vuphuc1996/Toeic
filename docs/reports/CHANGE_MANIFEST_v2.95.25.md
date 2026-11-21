# Change Manifest — v2.95.25 Major Quality Cycle

- Baseline: v2.95.24 FullSource.
- Changed canonical data: `data/related-terms.json` — 43 placeholder English definitions replaced with exact canonical vocabulary headword sense data; existing Vietnamese meanings preserved.
- Added tool: `tools/backfill-related-glossary-from-vocabulary.py` — audit-only default; `--apply` replaces eligible placeholder entries only; no term additions; idempotent.
- Added tool: `tools/audit-major-release.py` — cross-domain inventory/coverage audit; emits JSON and Markdown reports.
- Added tests: `tools/tests/test_related-glossary-backfill-025.py` (6 tests) and `tools/tests/test-major-release-quality-audit-025.py` (5 tests).
- Updated CI workflow to compile and run both new test modules; CI coverage regression verifies each Python test module is invoked.
- Added audit/release reports; synchronized all release markers to 2.95.25.
- No UI/CSS/layout, stable vocabulary IDs, headwords, relation arrays, question banks, learner records, local storage keys or eligibility gates changed.
- Verification: 53 focused Python tests PASS; version sync 12/12 PASS; JavaScript 38/38 PASS; data/content/repository and supporting audits PASS. Full Python sweep incomplete; remote CI, deployment and device QA not claimed.

## Robot Buddy opt-in clarification

- `assets/js/app.js`: Learning Insights defaults OFF; insight calculations/idle progress prompts require explicit `learningInsightsEnabled === true`; welcome copy describes optional analysis.
- `assets/js/robot-learning-insights.js`: clarifies opt-in/read-only/local boundary.
- `tools/tests/robot-buddy.mjs`: updated expectation for explicit opt-in.
- `tools/tests/robot-buddy-data-boundary.mjs`: new boundary regression.
- `.github/workflows/validate-data.yml`: runs the boundary regression.
- Master Status and test report updated. No UI redesign, learner records, schema, headwords, question bank or progress records changed.
