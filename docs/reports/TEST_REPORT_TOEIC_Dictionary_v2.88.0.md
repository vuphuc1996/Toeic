# Test Report — TOEIC Dictionary v2.88.0

## Scope

- Add 13 extended learner-authored A2 writing tasks (`::produce2`), one for each of the 13 A2 lessons, alongside the original 13 `::produce1` tasks.
- Preserve the original task IDs, v2.78.0 task-content baseline, v2.87.0 scenario correction fingerprint, historical learner evidence and local storage contracts.
- Render the extended tasks in a collapsed section and give each task independent response, self-rating and guided-revision history; preserve the first response as the visible baseline while showing the latest revision separately.
- Update the Foundation A2 portfolio summary, evidence aggregation and local Markdown export to enumerate all 26 production tasks.
- Add a SHA-256 registry for the new task content and update the legacy revision regression to expect 26 available A2 writing tasks.

## Results

| Check | Result | Scope |
|---|---|---|
| All `tools/tests/*.mjs` suites | PASS 31/31 | All JavaScript regression suites in the repository |
| Selected Python suites | PASS 89/89 | 10 focused modules: A2 production, guided revision, A2 assessment quality, Foundation pathway/outcome, learning content, PWA readiness, CI coverage, version sync and project progress |
| `test_foundation_a2_production.py` | PASS 8/8 | All 13 original + 13 extended tasks, stable IDs, requirements/rubrics, model answer feature checks, 20-word floor, registry fingerprints and legacy evidence isolation |
| `test_foundation_production_revision.py` | PASS 6/6 | Separate revision histories, review gates, preservation and 26-task portfolio availability |
| `test_foundation_a2_assessment_quality.py` | PASS 8/8 | A2 question integrity, answer-position balance and existing Reading/Listening assessment checks |
| `test_foundation_pathway.py` | PASS 10/10 | 13 A2 lesson IDs, teaching/assessment scope and local storage compatibility |
| `test_foundation_outcome_evidence.py` | PASS 2/2 | Separate recognition, production and retention evidence |
| `test_learning_content.py` | PASS 34/34 | Listening, Reading and Grammar data integrity |
| `test_pwa_readiness.py` | PASS 3/3 | Required shell assets and Service Worker readiness |
| `test_ci_coverage.py` | PASS 2/2 | Every JS/Python regression file is registered in GitHub Actions |
| `node --check` | PASS | `assets/js/app.js`, `assets/js/foundation-evidence.js`, `sw.js` |
| CSS parse (`tinycss2`) | PASS | 1,805 top-level nodes; 0 parse errors |
| `tools/validate-data.py` | PASS | 1,137 vocabulary records; 0 errors / 0 warnings (legacy baseline noted) |
| `tools/validate-learning-content.py` | PASS | 0 errors / 0 warnings |
| `tools/validate-part1-photo-assets.py --allow-missing` | PASS | 9/9 Part 1 photo records/assets and attribution checked; 0 missing warnings |
| Version synchronization | PASS | All registered app, SW, HTML and documentation markers agree at v2.88.0 |

The **89 Python tests are selected targeted modules**, not the full Python test discovery suite. The 31 JavaScript suites were all run.

## Manual/browser verification not claimed

- Browser visual rendering, including the desktop 15.6-inch 100% zoom layout and physical mobile/tablet layouts, was not verified in this execution.
- GitHub Actions remote execution, GitHub Pages deployment and real-device offline/reconnect behavior were not verified.
- A2 extended writing prompts have structural/content-contract checks but remain `pending-independent-editorial-review`. A second human linguistic reviewer and learner validation are still required.

## Preservation and limits

- No IndexedDB schema/store/version migration; IndexedDB remains v1.
- No localStorage key change, migration, progress reset or overwrite. Foundation evidence stays under `toeic:foundation-progress:v1`.
- Original 13 `::produce1` task IDs and the earlier `::apply1` legacy evidence remain intact and separate. Each new task uses a distinct `::produce2` ID.
- New-task responses and self-ratings are device-local. The Markdown export remains user-initiated, read-only and local; no data is sent to a server/API/Google AI.
- Self-ratings are not automated grammar grading, CEFR certification or TOEIC/ETS scores.
- Reading/Listening variety and independent A2 review remain open. The 99 Listening reserve questions remain excluded from Mock until independently approved.
