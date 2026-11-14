"""Regression tests for sense-linked TOEIC examples and vocabulary detail UX."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class VocabularyDetailAndExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = load_json("data/manifest.json")
        cls.records = []
        for item in cls.manifest["letters"]:
            cls.records.extend(load_json(item["file"].replace("./", "", 1))["words"])
        cls.app_js = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.app_css = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")

    def test_base_vocabulary_id_set_is_preserved_with_batches_017_to_020(self):
        ids = [record["id"] for record in self.records]
        baseline = set(load_json("tools/baseline-ids.json")["ids"])
        batch = load_json("data/vocabulary/batch-006.json")
        self.assertTrue(baseline.issubset(set(ids)))
        self.assertEqual(len(batch["words"]), 43)
        batch_018 = load_json("data/vocabulary/batch-007.json")
        self.assertEqual(len(batch_018["words"]), 8)
        self.assertTrue({w["id"] for w in batch_018["words"]}.issubset(set(ids)))
        batch_020 = load_json("data/vocabulary/batch-008.json")
        self.assertEqual(len(batch_020["words"]), 13)
        self.assertTrue({w["id"] for w in batch_020["words"]}.issubset(set(ids)))
        self.assertEqual(len(ids), 992)
        self.assertEqual(len(ids), len(set(ids)))

    def test_each_example_points_to_an_existing_sense(self):
        for record in self.records:
            for index, example in enumerate(record.get("examples", [])):
                sense_index = example.get("sense_index", 0)
                self.assertIs(type(sense_index), int, (record["id"], index))
                self.assertIn(sense_index, range(len(record["senses"])), (record["id"], index))

    def test_every_sense_has_at_least_one_dedicated_example(self):
        for record in self.records:
            covered = {example.get("sense_index", 0) for example in record.get("examples", [])}
            self.assertEqual(covered, set(range(len(record["senses"]))), record["id"])

    def test_example_sentences_and_translations_are_complete_and_not_duplicated(self):
        sentences = []
        for record in self.records:
            self.assertTrue(record.get("examples"), record["id"])
            for example in record["examples"]:
                en = example.get("en", "").strip()
                vi = example.get("vi", "").strip()
                self.assertGreaterEqual(len(en.split()), 5, (record["id"], en))
                self.assertRegex(en, r"^[A-Z].*[.!?]$", (record["id"], en))
                self.assertTrue(vi)
                self.assertNotEqual(en.casefold(), vi.casefold())
                sentences.append(en.casefold())
        self.assertEqual(len(sentences), len(set(sentences)))

    def test_multisense_entries_have_examples_for_all_senses(self):
        multi = [record for record in self.records if len(record["senses"]) > 1]
        self.assertEqual(len(multi), 25)
        self.assertEqual(sum(len(record["examples"]) for record in multi), 51)
        self.assertTrue(all(len({e.get("sense_index", 0) for e in record["examples"]}) == len(record["senses"]) for record in multi))

    def test_detail_modal_groups_meanings_by_pos_without_duplicate_pos_strip(self):
        self.assertIn("pos-detail-grid", self.app_js)
        self.assertIn("pos-detail-card", self.app_js)
        self.assertIn("posDisplayLabel", self.app_js)
        self.assertNotIn('<div class="detail-pos">${posMarkup(w)}</div>', self.app_js)

    def test_data_workspace_word_name_opens_detail_modal(self):
        handler = re.search(r"\$\('#dataTableBody'\)\.addEventListener\('click',e=>\{([^;]+(?:;[^;]+)*)\}\);", self.app_js)
        self.assertIsNotNone(handler)
        self.assertIn("closest('[data-detail]')", handler.group(1))
        self.assertIn("showDetail(detail.dataset.detail)", handler.group(1))

    def test_personal_copy_retains_sense_linked_examples(self):
        self.assertIn("old?.examples?.slice(1)", self.app_js)
        self.assertIn("sense_index:0", self.app_js)

    def test_vocabulary_example_typography_is_readable(self):
        self.assertRegex(self.app_css, r"\.pos-detail-card \.example-card strong\{[^}]*font-size:13(?:\.25)?px")
        self.assertRegex(self.app_css, r"\.pos-detail-card \.example-card span\{[^}]*font-size:12px")
        self.assertRegex(self.app_css, r"\.pos-detail-grid\{[^}]*grid-template-columns")

    def test_browser_normalizer_preserves_and_sorts_sense_index(self):
        self.assertIn("Number.isInteger(e.sense_index)", self.app_js)
        self.assertIn("Number.isInteger(e.sense_index)", self.app_js)
        self.assertIn("sort((a,b)=>a.sense_index-b.sense_index)", self.app_js)


if __name__ == "__main__":
    unittest.main()
