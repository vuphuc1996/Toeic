import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from helpers import Repo, rec


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.repo = Repo(Path(self._tmp.name))

    def clean_with_baseline(self):
        code, out = self.repo.init_baseline()
        self.assertEqual(code, 0, out)

    # ---- valid / baseline basics
    def test_valid_repo_passes(self):
        self.clean_with_baseline()
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("RESULT: PASS", out)

    def test_missing_baseline_makes_ids_check_fail(self):
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ003", out)

    def test_init_refuses_to_overwrite_existing_baseline(self):
        self.clean_with_baseline()
        before = sha(self.repo.baseline_path())
        code, out = self.repo.init_baseline()
        self.assertEqual(code, 1, out)
        self.assertEqual(before, sha(self.repo.baseline_path()))

    def test_init_refuses_when_structural_errors_exist(self):
        self.repo.manifest_over["totalWords"] = 99
        self.repo.save()
        code, out = self.repo.init_baseline()
        self.assertEqual(code, 1)
        self.assertFalse(self.repo.baseline_path().exists())

    def test_normal_run_never_modifies_baseline(self):
        self.clean_with_baseline()
        self.repo.words["A"][0]["senses"][0]["definition_en"] = "Alpha — see Vietnamese meaning."
        self.repo.save()
        before = sha(self.repo.baseline_path())
        self.repo.run()
        self.assertEqual(before, sha(self.repo.baseline_path()))

    # ---- structural errors are never excused
    def test_duplicate_id_is_structural_error(self):
        self.clean_with_baseline()
        self.repo.words["B"][0]["id"] = "alpha-n"
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ002", out)

    def test_duplicate_headword_is_structural_error(self):
        self.clean_with_baseline()
        self.repo.words["A"].append(rec("Alpha", id="alpha2-n"))
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ002", out)

    def test_wrong_type_examples_is_structural_error(self):
        self.clean_with_baseline()
        self.repo.words["A"][0]["examples"] = "not a list"
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ004", out)

    def test_missing_required_field(self):
        self.clean_with_baseline()
        del self.repo.words["A"][0]["collocations"]
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ004", out)

    def test_manifest_total_words_wrong(self):
        self.clean_with_baseline()
        self.repo.manifest_over["totalWords"] = 3
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ005", out)

    def test_manifest_letters_must_stay_an_array(self):
        self.clean_with_baseline()
        self.repo.manifest_over["letters"] = 26
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ005", out)

    def test_cefr_out_of_range(self):
        self.clean_with_baseline()
        self.repo.words["A"][0]["cefr_level"] = "C2"
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("CE001", out)

    def test_unknown_topic(self):
        self.clean_with_baseline()
        self.repo.words["A"][0]["topics"] = ["NOPE"]
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("TP001", out)

    def test_duplicate_example_sentence(self):
        self.clean_with_baseline()
        self.repo.words["B"][0]["examples"][0]["en"] = self.repo.words["A"][0]["examples"][0]["en"]
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("EX003", out)

    def test_invalid_ipa_character(self):
        self.clean_with_baseline()
        self.repo.words["A"][0]["phonetic"]["us"] = "/ˈæl.fə😀/"
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("IP002", out)

    # ---- ID integrity
    def test_missing_id_against_baseline_is_error(self):
        self.clean_with_baseline()
        self.repo.words["B"] = []
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("DQ003", out)
        self.assertIn("bravo-n", out)

    def test_allow_remove_permits_intentional_removal(self):
        self.clean_with_baseline()
        self.repo.words["B"] = []
        self.repo.save()
        code, out = self.repo.run("--allow-remove", "bravo-n")
        self.assertEqual(code, 0, out)

    def test_added_ids_are_reported_not_failed(self):
        self.clean_with_baseline()
        self.repo.words["A"].append(rec("apple", id="apple-n", examples=[
            {"en": "She ate an apple after lunch yesterday.", "vi": "Cô ấy ăn một quả táo sau bữa trưa hôm qua."}]))
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("thêm 1", out)

    # ---- Service worker
    def test_appshell_missing_file(self):
        self.clean_with_baseline()
        self.repo.sw_extra_paths = ["./assets/topics/ghost.webp"]
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("SW001", out)

    def test_unlisted_asset_is_new_error(self):
        self.clean_with_baseline()
        self.repo.extra_assets = ["assets/topics/office.webp"]
        self.repo.sw_omit = {"assets/topics/office.webp"}
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("[ERROR] SW002", out)

    def test_unlisted_asset_in_baseline_is_warning(self):
        self.repo.extra_assets = ["assets/topics/office.webp"]
        self.repo.sw_omit = {"assets/topics/office.webp"}
        self.repo.save()
        self.clean_with_baseline()
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("[WARNING] SW002", out)

    def test_cache_name_must_match_manifest_version(self):
        self.clean_with_baseline()
        self.repo.cache_name = "toeic-vocab-github-only-v0.9.0"
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("SW003", out)

    def test_cache_name_prefix_is_enforced(self):
        self.clean_with_baseline()
        self.repo.cache_name = "toeic-dictionary-1.0.0"
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("SW003", out)

    # ---- ratchet behaviour
    def test_legacy_defect_in_baseline_is_warning(self):
        self.repo.words["A"][0]["senses"][0]["definition_en"] = "alpha: một thứ để thử."
        self.repo.save()
        self.clean_with_baseline()
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("[WARNING] DF002", out)

    def test_new_defect_outside_baseline_is_error(self):
        self.clean_with_baseline()
        self.repo.words["B"][0]["senses"][0]["definition_en"] = "Bravo — see Vietnamese meaning and examples."
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("[ERROR] DF002", out)

    def test_new_defect_not_hidden_by_equal_count(self):
        # baseline holds one legacy defect (alpha). Fix alpha, break bravo: the total stays 1,
        # but bravo is not in the baseline, so it must still fail.
        self.repo.words["A"][0]["senses"][0]["definition_en"] = "alpha: một thứ để thử."
        self.repo.save()
        self.clean_with_baseline()
        self.repo.words["A"][0]["senses"][0]["definition_en"] = "A thing that is used when checking item number A."
        self.repo.words["B"][0]["senses"][0]["definition_en"] = "bravo: một thứ để thử."
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("[ERROR] DF002", out)
        self.assertIn("bravo-n", out)

    def test_template_examples_detected_by_repetition(self):
        self.repo.words["A"] = [
            rec(w, id=f"{w}-n", examples=[{"en": f"The team discussed {w} during the meeting.",
                                           "vi": f"Nhóm đã thảo luận về “{w}” trong cuộc họp."}])
            for w in ("alpha", "apple", "apex")
        ]
        self.repo.save()
        self.clean_with_baseline()
        self.repo.words["B"] = [rec("bravo", examples=[{"en": "The team discussed bravo during the meeting.",
                                                       "vi": "Nhóm đã thảo luận về “bravo” trong cuộc họp."}])]
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("EX004", out)

    def test_rule_drift_is_error(self):
        self.clean_with_baseline()
        path = self.repo.baseline_path()
        doc = json.loads(path.read_text(encoding="utf-8"))
        doc["rules"]["EX004"]["params"]["minRepeat"] = 99
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
        code, out = self.repo.run()
        self.assertEqual(code, 1)
        self.assertIn("RULE-DRIFT", out)

    def test_tighten_removes_only_resolved_entries(self):
        self.repo.words["A"][0]["senses"][0]["definition_en"] = "alpha: một thứ để thử."
        self.repo.save()
        self.clean_with_baseline()
        self.repo.words["A"][0]["senses"][0]["definition_en"] = "A thing that is used when checking item number A."
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("resolved DF002", out)
        code, out = self.repo.run("--tighten-baseline")
        self.assertEqual(code, 0, out)
        doc = json.loads(self.repo.baseline_path().read_text(encoding="utf-8"))
        self.assertEqual(doc["rules"]["DF002"]["violations"], [])
        code, out = self.repo.run()
        self.assertNotIn("resolved DF002", out)

    def test_tighten_refuses_when_new_debt_exists_and_never_adds(self):
        self.clean_with_baseline()
        before = sha(self.repo.baseline_path())
        self.repo.words["B"][0]["senses"][0]["definition_en"] = "bravo: một thứ để thử."
        self.repo.save()
        code, out = self.repo.run("--tighten-baseline")
        self.assertEqual(code, 1, out)
        self.assertEqual(before, sha(self.repo.baseline_path()))


if __name__ == "__main__":
    unittest.main()
