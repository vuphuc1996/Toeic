# Python Test Report — TOEIC Dictionary v2.95.69

- Overall: **PASS WITH SKIPS (accepted skip policy)**
- Inventory: **104/104 modules completed**; 0 pending, 0 fail, 0 timeout, 0 errors, 0 incomplete.
- Cases: **785 collected; 784 passed; 0 failed; 1 skipped; 0 errored; 0 deselected**.
- Module outcomes: 103 PASS; 1 PASS WITH SKIPS; 0 FAIL.
- Final test-snapshot SHA-256: `68e068f459c17fe5b6ccc3a78f8a9681d1d2b1386dcc1306ace2e92e13e16880`
- Environment: Python 3.13.5 / CPython; Node v22.16.0; Linux x86_64.

## Inventory delta

- Compared with v2.95.45 baseline inventory (88 modules): 104 currently discovered; 16 added, 28 modified, 0 removed; no suspected renames.
- Discovery remains dynamic. No module was deselected or excluded from the 104-module final result.

## Accepted skip

- `tools/tests/test_patch_data.py::test_repository_gitignore_excludes_audit_logs` — skipped because the FullSource ZIP has no `.git` metadata; this assertion requires a Git clone. Policy marks this as accepted; all other 19 tests in that module passed.

## Execution method

- 96 modules were completed by the resumable full-inventory sharded runner.
- Seven final modules were run as complete `unittest discover` module invocations after the release-aware Word Family report-heading test was made dynamic.
- The 44-case `test_validator.py` module was run in one full `unittest discover` invocation (61.889s, PASS). It was also exercised in four chunks during diagnosis; the final count is from the single full-module run.
- The consolidated result joins disjoint module sets. It does not mark an interrupted shard attempt as PASS; only completed final module records are included.

## Module results

| Module | Status | Cases | PASS | FAIL | SKIP | Seconds |
|---|---:|---:|---:|---:|---:|---:|
| `tools/tests/test_alphabet_sound_lab.py` | PASS | 7 | 7 | 0 | 0 | 0.66 |
| `tools/tests/test_answer_leakage_audit.py` | PASS | 7 | 7 | 0 | 0 | 0.71 |
| `tools/tests/test_answer_position_balance.py` | PASS | 4 | 4 | 0 | 0 | 0.75 |
| `tools/tests/test_audit_design_tokens.py` | PASS | 8 | 8 | 0 | 0 | 0.80 |
| `tools/tests/test_baseline_ids.py` | PASS | 13 | 13 | 0 | 0 | 20.10 |
| `tools/tests/test_bind_events_dom_contract.py` | PASS | 4 | 4 | 0 | 0 | 0.67 |
| `tools/tests/test_choice_history.py` | PASS | 5 | 5 | 0 | 0 | 0.67 |
| `tools/tests/test_choice_identity.py` | PASS | 9 | 9 | 0 | 0 | 0.83 |
| `tools/tests/test_ci_coverage.py` | PASS | 8 | 8 | 0 | 0 | 0.69 |
| `tools/tests/test_cmudict_ipa_backfill.py` | PASS | 6 | 6 | 0 | 0 | 0.66 |
| `tools/tests/test_content_batch_024.py` | PASS | 8 | 8 | 0 | 0 | 0.76 |
| `tools/tests/test_content_batch_025.py` | PASS | 7 | 7 | 0 | 0 | 0.78 |
| `tools/tests/test_content_batch_026.py` | PASS | 6 | 6 | 0 | 0 | 0.79 |
| `tools/tests/test_content_batch_027.py` | PASS | 6 | 6 | 0 | 0 | 0.77 |
| `tools/tests/test_dashboard_layout.py` | PASS | 6 | 6 | 0 | 0 | 0.66 |
| `tools/tests/test_design_profile.py` | PASS | 6 | 6 | 0 | 0 | 1.44 |
| `tools/tests/test_design_system.py` | PASS | 19 | 19 | 0 | 0 | 0.64 |
| `tools/tests/test_distractor_quality.py` | PASS | 6 | 6 | 0 | 0 | 0.74 |
| `tools/tests/test_editorial_review.py` | PASS | 6 | 6 | 0 | 0 | 0.69 |
| `tools/tests/test_editorial_review_queue.py` | PASS | 8 | 8 | 0 | 0 | 1.56 |
| `tools/tests/test_foundation_a2_assessment_quality.py` | PASS | 8 | 8 | 0 | 0 | 1.61 |
| `tools/tests/test_foundation_a2_production.py` | PASS | 8 | 8 | 0 | 0 | 0.81 |
| `tools/tests/test_foundation_listening.py` | PASS | 14 | 14 | 0 | 0 | 0.71 |
| `tools/tests/test_foundation_listening_extended.py` | PASS | 4 | 4 | 0 | 0 | 0.69 |
| `tools/tests/test_foundation_outcome_evidence.py` | PASS | 2 | 2 | 0 | 0 | 0.85 |
| `tools/tests/test_foundation_pathway.py` | PASS | 10 | 10 | 0 | 0 | 0.66 |
| `tools/tests/test_foundation_production_revision.py` | PASS | 6 | 6 | 0 | 0 | 0.77 |
| `tools/tests/test_foundation_reading.py` | PASS | 9 | 9 | 0 | 0 | 0.65 |
| `tools/tests/test_foundation_reading_extended.py` | PASS | 7 | 7 | 0 | 0 | 0.66 |
| `tools/tests/test_git_commit_readiness.py` | PASS | 10 | 10 | 0 | 0 | 1.25 |
| `tools/tests/test_grammar_examples_quality.py` | PASS | 4 | 4 | 0 | 0 | 0.68 |
| `tools/tests/test_grammar_expansion.py` | PASS | 7 | 7 | 0 | 0 | 0.65 |
| `tools/tests/test_ipa_backfill_batch_024.py` | PASS | 6 | 6 | 0 | 0 | 0.75 |
| `tools/tests/test_item_complexity_review.py` | PASS | 5 | 5 | 0 | 0 | 1.41 |
| `tools/tests/test_learning_content.py` | PASS | 34 | 34 | 0 | 0 | 0.70 |
| `tools/tests/test_learning_detail_scope.py` | PASS | 4 | 4 | 0 | 0 | 0.80 |
| `tools/tests/test_learning_outcome_progress.py` | PASS | 3 | 3 | 0 | 0 | 0.77 |
| `tools/tests/test_learning_outcomes.py` | PASS | 3 | 3 | 0 | 0 | 1.39 |
| `tools/tests/test_learning_start_level.py` | PASS | 4 | 4 | 0 | 0 | 0.72 |
| `tools/tests/test_learning_surface_consistency.py` | PASS | 5 | 5 | 0 | 0 | 0.66 |
| `tools/tests/test_legacy_collocation_cleanup.py` | PASS | 3 | 3 | 0 | 0 | 0.73 |
| `tools/tests/test_listening_expansion.py` | PASS | 8 | 8 | 0 | 0 | 0.69 |
| `tools/tests/test_major_release_quality_audit_025.py` | PASS | 8 | 8 | 0 | 0 | 0.76 |
| `tools/tests/test_missing_ipa_markdown_report.py` | PASS | 2 | 2 | 0 | 0 | 0.59 |
| `tools/tests/test_missing_ipa_review_queue.py` | PASS | 8 | 8 | 0 | 0 | 0.64 |
| `tools/tests/test_missing_ipa_safe_backfill.py` | PASS | 8 | 8 | 0 | 0 | 0.65 |
| `tools/tests/test_objective_resource_map.py` | PASS | 2 | 2 | 0 | 0 | 0.72 |
| `tools/tests/test_package_source.py` | PASS | 3 | 3 | 0 | 0 | 0.73 |
| `tools/tests/test_part1_photo_assets.py` | PASS | 6 | 6 | 0 | 0 | 0.68 |
| `tools/tests/test_patch_data.py` | PASS WITH SKIPS | 20 | 19 | 0 | 1 | 15.71 |
| `tools/tests/test_patch_related_terms.py` | PASS | 11 | 11 | 0 | 0 | 9.02 |
| `tools/tests/test_placement_diagnostic.py` | PASS | 6 | 6 | 0 | 0 | 0.65 |
| `tools/tests/test_practice_mode_fallback.py` | PASS | 6 | 6 | 0 | 0 | 0.66 |
| `tools/tests/test_project_progress.py` | PASS | 4 | 4 | 0 | 0 | 3.67 |
| `tools/tests/test_pwa_readiness.py` | PASS | 3 | 3 | 0 | 0 | 0.66 |
| `tools/tests/test_python_test_shard_runner.py` | PASS | 19 | 19 | 0 | 0 | 1.71 |
| `tools/tests/test_question_evidence.py` | PASS | 7 | 7 | 0 | 0 | 1.43 |
| `tools/tests/test_reading_expansion.py` | PASS | 9 | 9 | 0 | 0 | 0.63 |
| `tools/tests/test_related_glossary_backfill_025.py` | PASS | 6 | 6 | 0 | 0 | 0.88 |
| `tools/tests/test_related_glossary_backlog.py` | PASS | 3 | 3 | 0 | 0 | 2.46 |
| `tools/tests/test_related_glossary_batch_021.py` | PASS | 7 | 7 | 0 | 0 | 0.81 |
| `tools/tests/test_related_glossary_batch_022.py` | PASS | 9 | 9 | 0 | 0 | 0.72 |
| `tools/tests/test_related_glossary_batch_023.py` | PASS | 9 | 9 | 0 | 0 | 0.72 |
| `tools/tests/test_related_glossary_batch_026.py` | PASS | 5 | 5 | 0 | 0 | 0.74 |
| `tools/tests/test_related_glossary_batch_027.py` | PASS | 5 | 5 | 0 | 0 | 0.72 |
| `tools/tests/test_related_glossary_batch_028.py` | PASS | 4 | 4 | 0 | 0 | 0.71 |
| `tools/tests/test_related_glossary_batch_030.py` | PASS | 4 | 4 | 0 | 0 | 0.65 |
| `tools/tests/test_related_glossary_batch_032.py` | PASS | 4 | 4 | 0 | 0 | 0.68 |
| `tools/tests/test_related_glossary_batch_033.py` | PASS | 3 | 3 | 0 | 0 | 0.67 |
| `tools/tests/test_related_glossary_batch_034.py` | PASS | 6 | 6 | 0 | 0 | 0.64 |
| `tools/tests/test_related_glossary_batch_035.py` | PASS | 5 | 5 | 0 | 0 | 0.68 |
| `tools/tests/test_related_glossary_batch_035_cambridge.py` | PASS | 5 | 5 | 0 | 0 | 0.74 |
| `tools/tests/test_related_glossary_batch_036.py` | PASS | 6 | 6 | 0 | 0 | 0.76 |
| `tools/tests/test_related_glossary_batch_037.py` | PASS | 7 | 7 | 0 | 0 | 0.71 |
| `tools/tests/test_related_glossary_batch_039.py` | PASS | 4 | 4 | 0 | 0 | 0.67 |
| `tools/tests/test_related_glossary_batch_041.py` | PASS | 4 | 4 | 0 | 0 | 0.70 |
| `tools/tests/test_related_glossary_batch_042.py` | PASS | 5 | 5 | 0 | 0 | 0.68 |
| `tools/tests/test_related_glossary_batch_043.py` | PASS | 6 | 6 | 0 | 0 | 0.67 |
| `tools/tests/test_related_glossary_batch_044.py` | PASS | 5 | 5 | 0 | 0 | 0.67 |
| `tools/tests/test_related_glossary_candidate_audit.py` | PASS | 4 | 4 | 0 | 0 | 0.69 |
| `tools/tests/test_related_glossary_canonical_enrichment_029.py` | PASS | 8 | 8 | 0 | 0 | 0.69 |
| `tools/tests/test_related_glossary_exact_match_enrichment_035.py` | PASS | 5 | 5 | 0 | 0 | 0.73 |
| `tools/tests/test_related_glossary_merge_038.py` | PASS | 8 | 8 | 0 | 0 | 0.84 |
| `tools/tests/test_related_glossary_quality_audit.py` | PASS | 15 | 15 | 0 | 0 | 0.88 |
| `tools/tests/test_related_term_explanation_context.py` | PASS | 4 | 4 | 0 | 0 | 0.67 |
| `tools/tests/test_release_acceptance_runner.py` | PASS | 10 | 10 | 0 | 0 | 0.61 |
| `tools/tests/test_release_rotation.py` | PASS | 9 | 9 | 0 | 0 | 7.97 |
| `tools/tests/test_release_shell_coherence.py` | PASS | 7 | 7 | 0 | 0 | 0.74 |
| `tools/tests/test_remaining_content_review.py` | PASS | 9 | 9 | 0 | 0 | 0.72 |
| `tools/tests/test_repository_integrity.py` | PASS | 2 | 2 | 0 | 0 | 1.45 |
| `tools/tests/test_responsive_layout.py` | PASS | 8 | 8 | 0 | 0 | 0.64 |
| `tools/tests/test_sentence_completion.py` | PASS | 12 | 12 | 0 | 0 | 0.71 |
| `tools/tests/test_single_overlay_contract.py` | PASS | 3 | 3 | 0 | 0 | 0.75 |
| `tools/tests/test_sync_version.py` | PASS | 13 | 13 | 0 | 0 | 12.74 |
| `tools/tests/test_test_fingerprints.py` | PASS | 10 | 10 | 0 | 0 | 0.76 |
| `tools/tests/test_tts_readiness.py` | PASS | 15 | 15 | 0 | 0 | 0.70 |
| `tools/tests/test_validator.py` | PASS | 44 | 44 | 0 | 0 | 61.89 |
| `tools/tests/test_visual_composition.py` | PASS | 9 | 9 | 0 | 0 | 0.87 |
| `tools/tests/test_vocabulary_batch_012.py` | PASS | 4 | 4 | 0 | 0 | 0.71 |
| `tools/tests/test_vocabulary_detail_examples.py` | PASS | 19 | 19 | 0 | 0 | 0.94 |
| `tools/tests/test_vocabulary_family_batch_025.py` | PASS | 5 | 5 | 0 | 0 | 0.75 |
| `tools/tests/test_vocabulary_family_links.py` | PASS | 6 | 6 | 0 | 0 | 0.80 |
| `tools/tests/test_vocabulary_relationship_graph_audit.py` | PASS | 8 | 8 | 0 | 0 | 0.70 |
| `tools/tests/test_word_family_graph_audit.py` | PASS | 1 | 1 | 0 | 0 | 1.26 |

## Test case with accepted skip

`test_patch_data.py` reported 20 cases: 19 passed and 1 accepted skip. The module-level skip reason is recorded above and in the JSON evidence.

## Limitations

- These are local source tests. They do not establish that a remote GitHub Actions workflow or GitHub Pages deployment succeeded.
- Device/browser behavior, active Service Worker migration, installed PWA cache propagation and iPad/iPhone/Android acceptance are unverified.
