# Test Report — TOEIC Dictionary v2.95.44

## Result summary

- Focused Python validation: **134 tests passed across 22 suites**.
- JavaScript tests: **39/39 `.mjs` test files passed**.
- JavaScript syntax: **18/18 `assets/js/*.js` modules passed** after syntax-checking as ES modules; `sw.js` passed `node --check`.
- Python compileall: PASS.
- Canonical data validator: PASS — 1,141 records, 0 new errors, 0 legacy warnings, 0 ID additions/losses.
- Learning-content validator: PASS — 0 errors / 0 warnings.
- Version sync: PASS — all 13 current markers match 2.95.44.
- Part 1 photo assets: PASS — 9/9.
- Repository integrity: PASS — 414 local references/data files inspected, 0 errors, 0 optional warnings.
- Listening readiness, question evidence, distractor, TOEIC content coverage, learning outcomes, Foundation A2 and independent-review-queue audits regenerated successfully.

## Focused Python suites (134 tests)

| Suite | Tests | Result |
|---|---:|---|
| `test_related_glossary_batch_037.py` | 7 | PASS |
| `test_related_glossary_batch_036.py` | 6 | PASS |
| `test_related_glossary_batch_035.py` | 5 | PASS |
| `test_related_glossary_batch_034.py` | 6 | PASS |
| `test_related_glossary_batch_027.py` | 5 | PASS |
| `test_patch_related_terms.py` | 11 | PASS |
| `test_related_glossary_candidate_audit.py` | 4 | PASS |
| `test_related_glossary_backlog.py` | 3 | PASS |
| `test_related_glossary_quality_audit.py` | 11 | PASS |
| `test_vocabulary_relationship_graph_audit.py` | 8 | PASS |
| `test_major_release_quality_audit_025.py` | 8 | PASS |
| `test_project_progress.py` | 4 | PASS |
| `test_related_term_explanation_context.py` | 3 | PASS |
| `test_ci_coverage.py` | 3 | PASS |
| `test_vocabulary_detail_examples.py` | 19 | PASS |
| `test_repository_integrity.py` | 1 | PASS |
| `test_package_source.py` | 3 | PASS |
| `test_responsive_layout.py` | 7 | PASS |
| `test_learning_surface_consistency.py` | 5 | PASS |
| `test_pwa_readiness.py` | 3 | PASS |
| `test_part1_photo_assets.py` | 6 | PASS |
| `test_release_rotation.py` | 6 | PASS |
| `test_editorial_review.py` | 6 | PASS |
| **Total** | **134** | **PASS** |

## Data and audit outcomes

- `python tools/validate-data.py`: 1,141 canonical vocabulary records; 0 ID additions and 0 ID losses; 0 validator errors and 0 legacy warnings. Related-term reference coverage reports 253/804 unresolved (the coverage audit resolves 551/804).
- `python tools/validate-learning-content.py`: Listening 145 units / 295 questions; Reading 73 units / 287 questions; Grammar 58 lessons / 169 exercises; separate Part 5 practice 80 questions; 0 errors / 0 warnings.
- Listening readiness: 102 eligible / 193 reserve-pending / 295 total. These are inventory/readiness counts, not editorial approval.
- Question evidence audit: 582 questions indexed.
- Distractor audit: 264 questions in scope; 156 reserve structural checks; 12 revisions; all checked options/answer keys structurally valid.
- Learning-outcome audit: 11/11 objectives; 33 criteria; 6/33 evidence paths. This is instrumentation coverage, not learner mastery.
- Foundation A2: Reading 13/13 resources and 39/39 questions; Listening 13/13 core resources and 39/39 questions; supplementary listening 13/13 resources and 39/39 questions; audit PASS.
- Independent review queue: 193 Listening + 87 Reading Part 7 + 80 separate Part 5 = 360 questions pending review decisions.

## Corrected issues encountered during validation

- The historical `test_vocabulary_detail_examples.py` initially failed because one canonical record includes later provenance fields introduced by a previous release after the old snapshot. The test was narrowed to check every original field while allowing only the known later provenance-field allowlist. It was rerun: **19/19 PASS**. No vocabulary data was changed to satisfy the stale test.
- Historical Batch 027 and current glossary/progress audit tests contained stale release literals. They now validate the current generated backlog/inventory instead of asserting old totals (535/767 or the pre-Batch-037 glossary count). Their final focused suites pass.
- Full `python -m unittest discover -s tools/tests -p 'test_*.py' -v` was attempted but the execution environment timed out before the aggregate suite completed (partial log stopped during `test_patch_data.py`). This is **INCOMPLETE**, not a pass or a test assertion failure. Focused suites listed above completed separately.

## Not verified in this environment

- Remote GitHub Actions execution.
- GitHub Pages deployment, CDN/cache propagation or production site response.
- Live browser acceptance and physical-device testing on Android/iOS/tablet/desktop.
- Independent human editorial review of the new Cambridge-sourced glossary entries.
- Learner-specific IndexedDB migration/import acceptance (no schema/data migration was made or requested).

## Package and Patch replay

- Full Source: **664 files**; ZIP CRC, one-root and exclusion checks PASS.
- Patch overlay from v2.95.43: **43 files** (**23 added + 20 modified + 0 deleted**).
- Replay: extracted v2.95.43 base + Patch; **664/664 files byte-identical** to the v2.95.44 Full Source; 0 missing, 0 extra and 0 mismatched files.
- ZIP CRC, sidecar SHA-256, single-root and exclusion contracts: PASS.
