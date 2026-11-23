# Validator Regression Tests — Case-batched Execution — v2.95.43

- Module: `tools/tests/test_validator.py`
- TestCase methods discovered by unittest: 38
- Execution: 10 commands using unittest discovery `-k` selection; nine groups of four and one group of two.
- Results: 38/38 PASS; all 10 commands exit code 0; 0 skipped in this module.
- Each method remained unchanged and ran with its normal `setUp`/`tearDown`; groups were isolated in fresh Python processes.
- A monolithic invocation repeatedly stalled after an initial subset; case batching was used to verify every remaining method without treating an interrupted full-module process as PASS.

| Group | Cases | Result | Exit | Runtime (s) |
|---:|---:|---|---:|---:|
| 1 | 4 | PASS | 0 | 6.686 |
| 2 | 4 | PASS | 0 | 5.897 |
| 3 | 4 | PASS | 0 | 6.184 |
| 4 | 4 | PASS | 0 | 5.409 |
| 5 | 4 | PASS | 0 | 5.328 |
| 6 | 4 | PASS | 0 | 5.686 |
| 7 | 4 | PASS | 0 | 6.533 |
| 8 | 4 | PASS | 0 | 6.803 |
| 9 | 4 | PASS | 0 | 5.761 |
| 10 | 2 | PASS | 0 | 2.717 |

## Exact commands

### Group 1

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_added_ids_are_reported_not_failed -k ValidatorTests.test_allow_remove_permits_intentional_removal -k ValidatorTests.test_appshell_missing_file -k ValidatorTests.test_cache_name_must_match_manifest_version -v
```

### Group 2

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_cache_name_prefix_is_enforced -k ValidatorTests.test_cefr_out_of_range -k ValidatorTests.test_duplicate_example_sentence -k ValidatorTests.test_duplicate_headword_is_structural_error -v
```

### Group 3

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_duplicate_id_is_structural_error -k ValidatorTests.test_every_sense_requires_its_own_example -k ValidatorTests.test_example_sense_index_must_be_in_range -k ValidatorTests.test_init_refuses_to_overwrite_existing_baseline -v
```

### Group 4

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_init_refuses_when_structural_errors_exist -k ValidatorTests.test_invalid_ipa_character -k ValidatorTests.test_ipa_missing_counter_includes_absent_phonetic_object -k ValidatorTests.test_ipa_missing_counter_includes_missing_us_key -v
```

### Group 5

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_legacy_defect_in_baseline_is_warning -k ValidatorTests.test_manifest_letters_must_stay_an_array -k ValidatorTests.test_manifest_total_words_wrong -k ValidatorTests.test_missing_baseline_makes_ids_check_fail -v
```

### Group 6

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_missing_id_against_baseline_is_error -k ValidatorTests.test_missing_optional_cache_asset_is_not_a_structural_error -k ValidatorTests.test_missing_required_field -k ValidatorTests.test_new_defect_not_hidden_by_equal_count -v
```

### Group 7

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_new_defect_outside_baseline_is_error -k ValidatorTests.test_normal_run_never_modifies_baseline -k ValidatorTests.test_rule_drift_is_error -k ValidatorTests.test_template_examples_detected_by_repetition -v
```

### Group 8

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_tighten_refuses_when_new_debt_exists_and_never_adds -k ValidatorTests.test_tighten_removes_only_resolved_entries -k ValidatorTests.test_unknown_topic -k ValidatorTests.test_unlisted_asset_in_baseline_is_warning -v
```

### Group 9

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_unlisted_asset_is_new_error -k ValidatorTests.test_valid_repo_passes -k ValidatorTests.test_verb_forms_v1_must_match_headword -k ValidatorTests.test_verb_sense_requires_collocations -v
```

### Group 10

```bash
python -m unittest discover -s tools/tests -p test_validator.py -k ValidatorTests.test_verb_sense_requires_verb_forms -k ValidatorTests.test_wrong_type_examples_is_structural_error -v
```

No test assertion, fixture, data validator, or baseline behavior was weakened for this execution.
