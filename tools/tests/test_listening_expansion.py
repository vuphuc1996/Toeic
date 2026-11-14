import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class ListeningExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.units = json.loads((ROOT / "data/listening/listening-library.json").read_text(encoding="utf-8"))["listening"]
        cls.batch = [u for u in cls.units if u.get("editorialBatch") == "015"]

    def test_batch_015_inventory_and_part_blueprint(self):
        self.assertEqual(len(self.batch), 34)
        self.assertEqual(sum(len(u.get("questions", [])) for u in self.batch), 70)
        self.assertEqual(Counter(u["part"] for u in self.batch), Counter({"Part 2": 16, "Part 3": 11, "Part 4": 7}))
        self.assertTrue(all(len(u.get("questions", [])) == 1 for u in self.batch if u["part"] == "Part 2"))
        self.assertTrue(all(len(u.get("questions", [])) == 3 for u in self.batch if u["part"] in ("Part 3", "Part 4")))

    def test_every_batch_015_item_stays_pending_independent_review(self):
        for unit in self.batch:
            self.assertEqual(unit.get("contentSource"), "original-editorial", unit["id"])
            self.assertEqual(unit.get("editorialStatus"), "reserve-pending-independent-review", unit["id"])
            self.assertEqual(unit.get("reviewNote"), "internal-author-check; independent-second-review-pending", unit["id"])
            self.assertEqual(unit.get("contentBatch"), "batch-015-listening-expansion", unit["id"])

    def test_question_choice_ids_are_unique_and_keys_valid(self):
        item_ids = [u["id"] for u in self.units]
        self.assertEqual(len(item_ids), len(set(item_ids)))
        all_choice_ids = []
        for unit in self.batch:
            source = " ".join(s.get("text", "") for s in unit.get("segments", []))
            for index, question in enumerate(unit.get("questions", []), 1):
                expected = 3 if unit["part"] == "Part 2" else 4
                self.assertEqual(len(question.get("choices", [])), expected, unit["id"])
                self.assertEqual(len(question.get("choiceIds", [])), expected, unit["id"])
                self.assertEqual(len(set(question["choiceIds"])), expected, unit["id"])
                self.assertIn(question.get("answerIndex"), range(expected), unit["id"])
                self.assertTrue(question.get("question", "").strip())
                self.assertTrue(question.get("explanation", "").strip())
                all_choice_ids.extend(question["choiceIds"])
                evidence = question.get("evidenceText", "").casefold()
                self.assertTrue(evidence, f"{unit['id']} Q{index}: missing evidenceText")
                if unit["part"] == "Part 2":
                    # In Part 2 the audio contains the spoken question; response options are answer choices, not transcript audio.
                    self.assertIn(evidence, source.casefold(), unit["id"])
                else:
                    self.assertIn(evidence, source.casefold(), unit["id"])
        self.assertEqual(len(all_choice_ids), len(set(all_choice_ids)))

    def test_author_review_repairs_three_response_or_evidence_gaps(self):
        by_id = {u["id"]: u for u in self.units}
        p2 = by_id["part2-warehouse-label-printing"]
        p2q = p2["questions"][0]
        self.assertEqual(p2q["choices"][p2q["answerIndex"]], "Only the labels for the first shipment have been printed.")

        procurement = by_id["part3-procurement-quote-comparison"]
        procurement_q = procurement["questions"][1]
        self.assertIn("installation is included", procurement_q["evidenceText"])
        self.assertIn("installation included", procurement_q["choices"][procurement_q["answerIndex"]].lower())

        customs = by_id["part3-international-shipment-customs"]
        customs_q = customs["questions"][1]
        self.assertEqual(customs_q["choices"][customs_q["answerIndex"]], "Product codes, country of origin, and quantities for each code")
        self.assertIn(customs_q["evidenceText"], customs["segments"][-1]["text"])

        for unit in (p2, procurement, customs):
            self.assertEqual(unit.get("editorialStatus"), "reserve-pending-independent-review")

    def test_listening_inventory_separates_eligible_and_pending(self):
        pending = [u for u in self.units if u.get("editorialStatus") == "reserve-pending-independent-review"]
        eligible = [u for u in self.units if not u.get("editorialStatus") or u.get("editorialStatus") == "approved-for-mock"]
        self.assertEqual(sum(len(u["questions"]) for u in eligible), 102)
        self.assertEqual(sum(len(u["questions"]) for u in pending), 98)
        projected = Counter()
        for unit in eligible + pending:
            projected[unit["part"]] += len(unit["questions"])
        self.assertEqual(projected, Counter({"Part 1": 8, "Part 2": 51, "Part 3": 81, "Part 4": 60}))

if __name__ == "__main__":
    unittest.main()
