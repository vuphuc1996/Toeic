# Sharded Python Test Run — v2.95.61

- Timestamp (UTC): 2026-11-25T02:54:42Z
- Overall: **INCOMPLETE / FAIL**
- Modules: 19 PASS; 0 PASS WITH SKIPS; 0 FAIL; 0 TIMEOUT; 0 INCOMPLETE; 0 ERROR; 76 NOT RUN
- Test cases: 140 collected; 140 passed; 0 failed; 0 skipped; 0 errored; 0 deselected

## Fingerprints

- Source release: `960f6508d8e54b854d3f3697a2a340850dff4762a0ac2f702ec506aa60660cbe`
- Test input: `f231b7df91151c94a49127c2dc64903a406fa4e705e125b5bbafffddf299fef1`
- Environment: `a96ea9867a14ba7c8b6768be97052f22a766eb6cda34241b201a29c747041425`

| Module | Discovery | Collection | Execution | Final | Cases | PASS | FAIL | SKIP | ERR | Exit | Seconds |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `tools/tests/test_alphabet_sound_lab.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 7 | 7 | 0 | 0 | 0 | 0 | 0.831 |
| `tools/tests/test_answer_leakage_audit.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 7 | 7 | 0 | 0 | 0 | 0 | 0.627 |
| `tools/tests/test_answer_position_balance.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 4 | 4 | 0 | 0 | 0 | 0 | 0.802 |
| `tools/tests/test_audit_design_tokens.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 8 | 8 | 0 | 0 | 0 | 0 | 0.702 |
| `tools/tests/test_baseline_ids.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 13 | 13 | 0 | 0 | 0 | 0 | 19.037 |
| `tools/tests/test_choice_history.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 5 | 5 | 0 | 0 | 0 | 0 | 0.713 |
| `tools/tests/test_choice_identity.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 9 | 9 | 0 | 0 | 0 | 0 | 0.779 |
| `tools/tests/test_ci_coverage.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 3 | 3 | 0 | 0 | 0 | 0 | 0.644 |
| `tools/tests/test_cmudict_ipa_backfill.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 0.658 |
| `tools/tests/test_content_batch_024.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 8 | 8 | 0 | 0 | 0 | 0 | 0.699 |
| `tools/tests/test_content_batch_025.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 7 | 7 | 0 | 0 | 0 | 0 | 0.688 |
| `tools/tests/test_content_batch_026.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 0.704 |
| `tools/tests/test_content_batch_027.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 0.704 |
| `tools/tests/test_dashboard_layout.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 0.641 |
| `tools/tests/test_design_profile.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 1.349 |
| `tools/tests/test_design_system.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 19 | 19 | 0 | 0 | 0 | 0 | 0.659 |
| `tools/tests/test_distractor_quality.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 0.765 |
| `tools/tests/test_editorial_review.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 6 | 6 | 0 | 0 | 0 | 0 | 0.766 |
| `tools/tests/test_editorial_review_queue.py` | DISCOVERED | COLLECTED | COMPLETED | PASS | 8 | 8 | 0 | 0 | 0 | 0 | 1.351 |

## Not yet run

- `tools/tests/test_foundation_a2_assessment_quality.py`
- `tools/tests/test_foundation_a2_production.py`
- `tools/tests/test_foundation_listening.py`
- `tools/tests/test_foundation_listening_extended.py`
- `tools/tests/test_foundation_outcome_evidence.py`
- `tools/tests/test_foundation_pathway.py`
- `tools/tests/test_foundation_production_revision.py`
- `tools/tests/test_foundation_reading.py`
- `tools/tests/test_foundation_reading_extended.py`
- `tools/tests/test_grammar_examples_quality.py`
- `tools/tests/test_grammar_expansion.py`
- `tools/tests/test_ipa_backfill_batch_024.py`
- `tools/tests/test_item_complexity_review.py`
- `tools/tests/test_learning_content.py`
- `tools/tests/test_learning_detail_scope.py`
- `tools/tests/test_learning_outcome_progress.py`
- `tools/tests/test_learning_outcomes.py`
- `tools/tests/test_learning_start_level.py`
- `tools/tests/test_learning_surface_consistency.py`
- `tools/tests/test_legacy_collocation_cleanup.py`
- `tools/tests/test_listening_expansion.py`
- `tools/tests/test_major_release_quality_audit_025.py`
- `tools/tests/test_missing_ipa_markdown_report.py`
- `tools/tests/test_missing_ipa_review_queue.py`
- `tools/tests/test_missing_ipa_safe_backfill.py`
- `tools/tests/test_objective_resource_map.py`
- `tools/tests/test_package_source.py`
- `tools/tests/test_part1_photo_assets.py`
- `tools/tests/test_patch_data.py`
- `tools/tests/test_patch_related_terms.py`
- `tools/tests/test_placement_diagnostic.py`
- `tools/tests/test_practice_mode_fallback.py`
- `tools/tests/test_project_progress.py`
- `tools/tests/test_pwa_readiness.py`
- `tools/tests/test_python_test_shard_runner.py`
- `tools/tests/test_question_evidence.py`
- `tools/tests/test_reading_expansion.py`
- `tools/tests/test_related_glossary_backfill_025.py`
- `tools/tests/test_related_glossary_backlog.py`
- `tools/tests/test_related_glossary_batch_021.py`
- `tools/tests/test_related_glossary_batch_022.py`
- `tools/tests/test_related_glossary_batch_023.py`
- `tools/tests/test_related_glossary_batch_026.py`
- `tools/tests/test_related_glossary_batch_027.py`
- `tools/tests/test_related_glossary_batch_028.py`
- `tools/tests/test_related_glossary_batch_030.py`
- `tools/tests/test_related_glossary_batch_032.py`
- `tools/tests/test_related_glossary_batch_033.py`
- `tools/tests/test_related_glossary_batch_034.py`
- `tools/tests/test_related_glossary_batch_035.py`
- `tools/tests/test_related_glossary_batch_036.py`
- `tools/tests/test_related_glossary_batch_037.py`
- `tools/tests/test_related_glossary_batch_039.py`
- `tools/tests/test_related_glossary_batch_041.py`
- `tools/tests/test_related_glossary_batch_042.py`
- `tools/tests/test_related_glossary_candidate_audit.py`
- `tools/tests/test_related_glossary_canonical_enrichment_029.py`
- `tools/tests/test_related_glossary_exact_match_enrichment_035.py`
- `tools/tests/test_related_glossary_merge_038.py`
- `tools/tests/test_related_glossary_quality_audit.py`
- `tools/tests/test_related_term_explanation_context.py`
- `tools/tests/test_release_acceptance_runner.py`
- `tools/tests/test_release_rotation.py`
- `tools/tests/test_remaining_content_review.py`
- `tools/tests/test_repository_integrity.py`
- `tools/tests/test_responsive_layout.py`
- `tools/tests/test_sentence_completion.py`
- `tools/tests/test_sync_version.py`
- `tools/tests/test_test_fingerprints.py`
- `tools/tests/test_tts_readiness.py`
- `tools/tests/test_validator.py`
- `tools/tests/test_visual_composition.py`
- `tools/tests/test_vocabulary_batch_012.py`
- `tools/tests/test_vocabulary_detail_examples.py`
- `tools/tests/test_vocabulary_family_links.py`
- `tools/tests/test_vocabulary_relationship_graph_audit.py`

Policy: every dynamically discovered module is accounted for. A module PASS requires exit code 0 and a valid unittest summary with at least one collected case. PASS WITH SKIPS is distinct from PASS. Overall success requires all discovered modules to reach an accepted terminal state; pending modules are never hidden.
