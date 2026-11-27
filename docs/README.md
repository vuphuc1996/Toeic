# TOEIC Dictionary v2.95.73 — Project Documentation

This page describes the current GitHub `candidate` source. It is not a statement that production `main` has been updated.

- Current release: `2.95.73` (candidate-only).
- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.73.md`.
- Current command-log index: `reports/COMMAND_LOG_INDEX_v2.95.73.md`.
- Word Family Batch 027: `reports/WORD_FAMILY_BATCH_027_v2.95.73.md`.
- Word Family audit implementation: `../tools/audit-word-family-graph.py`.
- Current version ledger: `versions/CURRENT_VERSION.md`.
- Master project status: `MASTER_STATUS.md`.
- Changelog: `../docs/CHANGELOG.md`.

## Current source and data boundaries

The canonical vocabulary inventory remains at 1,181 headwords. Batch 027 adds 10 reciprocal Word Family links and removes 2 self-referential links; it does not add or remove headwords or canonical IDs. The source contains 50 missing Word Family targets and 70 Vietnamese sense-anchor review flags; these remain explicit editorial work, not silently accepted items.

The production branch `main` remains separate. GitHub Pages preview/deployment and GitHub Actions must be checked for each candidate commit. Installed-PWA cache propagation and physical-device acceptance remain separate verification gates. Learner LocalStorage/IndexedDB records are not migrated by this release.
