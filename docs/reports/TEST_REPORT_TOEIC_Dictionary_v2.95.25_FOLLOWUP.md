# v2.95.25 Follow-up Test Report

## Passed
- 66 focused Python tests across 8 modules: package source (3), CI coverage (3), major audit (5), glossary backfill (6), backlog (3), data patch safety (20), version sync (12), baseline IDs (13), and repository integrity (1.
- 39/39 JavaScript regression suites.
- Vocabulary validator: 1,141 canonical records; 0 errors, 0 warnings.
- Learning-content validator: 0 errors, 0 warnings.
- Version sync check: PASS.
- ZIP CRC and single-root checks: PASS for FullSource and Update Patch.
- FullSource includes nested documentation history and excludes `.tmp` artifacts.

## Not completed
- Full Python unittest discovery did not complete within the execution time limit.
- Remote GitHub Actions, deployment, and browser/device manual acceptance were not run.

## Latest scope changes in v2.95.25
- Robot Buddy OFF toggle removes visible progress dashboards while preserving other chat messages.
- Packaging now preserves nested `docs/archive/` history while excluding only root archive folders and temporary `.tmp` files.
