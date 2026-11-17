# Test Report — TOEIC Dictionary v2.87.0

## Scope

- Add an on-device Markdown export for Foundation A2 writing portfolio responses and guided revisions.
- Preserve learner progress and storage schema; exclude legacy application evidence and non-A2 lessons.
- Correct the `a2-polite-requests` scenario direction and record the exact baseline fingerprint refresh.
- Extend regression and CI coverage for portfolio export and task-content consistency.

## Results

| Check | Result | Scope |
|---|---|---|
| All `tools/tests/*.mjs` suites | PASS 31/31 | Full registered JavaScript regression suite |
| `test_foundation_a2_production.py` | PASS 7/7 | A2 task content, baseline refresh, legacy separation |
| `test_foundation_production_revision.py` | PASS 6/6 | Guided revision integrity and baseline |
| `test_foundation_outcome_evidence.py` | PASS 2/2 | Separate recognition/production/retention evidence |
| `test_learning_content.py` | PASS 34/34 | Listening, Reading and Grammar data integrity |
| `test_ci_coverage.py` | PASS 2/2 | New JavaScript regression suite registered in CI |
| `test_pwa_readiness.py` | PASS 3/3 | App shell and Service Worker readiness |
| CSS parse (`tinycss2`) | PASS | 1,795 top-level nodes; 0 top-level parse errors |
| `tools/validate-data.py` | PASS | 1,137 vocabulary records; 0 errors / 0 warnings (legacy baseline noted) |
| `tools/validate-learning-content.py` | PASS | 0 errors / 0 warnings |
| Version synchronization | PASS | `tools/sync-version.py --check`; all registered app, SW, HTML and documentation markers agree at v2.87.0 |

Total selected Python tests across the eight executed modules (including version synchronization and project-progress checks): **70/70 PASS**. The full Python suite was not run.

## Manual/browser verification not claimed

The local browser visual/device run, GitHub Actions remote result and GitHub Pages deployment have not been verified in this execution. Test on a desktop browser and mobile PWA after publishing.

## Preservation

- No IndexedDB version/store/schema or migration change.
- No localStorage key or learner progress overwrite/reset.
- No external transfer; Markdown export is a user-triggered local download.
- No automatic grammar scoring or CEFR/ETS mastery claim.
- Listening reserve questions remain excluded from Mock until the required independent review is recorded.
