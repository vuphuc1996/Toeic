"""Regression checks for v2.33 Reading expansion and source evidence."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_reading():
    return json.loads((ROOT / "data/readings/reading-library.json").read_text(encoding="utf-8"))["readings"]


class ReadingExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = load_reading()
        cls.p5 = [x for x in cls.items if x.get("part") == "Part 5"]
        cls.p6 = [x for x in cls.items if x.get("part") == "Part 6"]
        cls.p7 = [x for x in cls.items if x.get("part") == "Part 7"]
        cls.p7_multi = [x for x in cls.p7 if x.get("documentType") in ("DOUBLE PASSAGE", "TRIPLE PASSAGE")]
        cls.p7_single = [x for x in cls.p7 if x not in cls.p7_multi]

    def test_reading_pool_has_200_questions_with_exact_part_totals(self):
        counts = {
            f"Part {part}": sum(len(x.get("questions", [])) for x in self.items if x.get("part") == f"Part {part}")
            for part in (5, 6, 7)
        }
        self.assertEqual(counts, {"Part 5": 60, "Part 6": 32, "Part 7": 108})
        self.assertEqual(sum(counts.values()), 200)
        self.assertEqual(len(self.items), 51)

    def test_part6_keeps_all_four_blanks_and_questions_together(self):
        import re
        self.assertEqual(len(self.p6), 8)
        for item in self.p6:
            markers = re.findall(r"\[(\d+)\]", item.get("passage", ""))
            self.assertEqual(markers, ["1", "2", "3", "4"], item["id"])
            self.assertEqual(len(item.get("questions", [])), 4, item["id"])

    def test_part7_single_passages_are_complete_two_to_four_question_blocks(self):
        self.assertEqual(len(self.p7_single), 20)
        self.assertEqual(sum(len(x.get("questions", [])) for x in self.p7_single), 58)
        for item in self.p7_single:
            self.assertIn(len(item.get("questions", [])), (2, 3, 4), item["id"])
            self.assertTrue(item.get("passage", "").strip() or item.get("documents"), item["id"])

    def test_part7_multiple_passages_are_complete_five_question_blocks(self):
        self.assertEqual(len(self.p7_multi), 10)
        self.assertEqual(sum(len(x.get("questions", [])) for x in self.p7_multi), 50)
        for item in self.p7_multi:
            expected_docs = 2 if item["documentType"] == "DOUBLE PASSAGE" else 3
            self.assertEqual(len(item.get("documents", [])), expected_docs, item["id"])
            self.assertEqual(len(item.get("questions", [])), 5, item["id"])
            self.assertTrue(all(d.get("label", "").strip() and d.get("content", "").strip() for d in item["documents"]), item["id"])

    def test_new_part7_questions_have_45_traceable_source_quotes(self):
        new_questions = [
            (item, q)
            for item in self.p7
            for q in item.get("questions", [])
            if q.get("evidence") and q.get("evidence", {}).get("sourceLabels")
        ]
        self.assertEqual(len(new_questions), 45)
        for item, q in new_questions:
            evidence = q["evidence"]
            labels = evidence.get("sourceLabels", [])
            quotes = evidence.get("quotes", [])
            self.assertTrue(labels, f"{item['id']}: missing sourceLabels")
            self.assertTrue(quotes, f"{item['id']}: missing quotes")
            source_map = {d.get("label"): d.get("content", "") for d in item.get("documents", [])}
            if item.get("documentType") and item.get("passage"):
                source_map.setdefault(item["documentType"], item["passage"])
            for label in labels:
                self.assertIn(label, source_map, f"{item['id']}: unknown evidence source {label}")
            for quote in quotes:
                self.assertTrue(any(quote in source_map[label] for label in labels), f"{item['id']}: quote not found in labelled source")

    def test_v232_questions_and_resource_metadata_are_preserved(self):
        import hashlib
        baseline = json.loads((ROOT / "tools/reading-baseline-v2.32.0.json").read_text(encoding="utf-8"))
        self.assertEqual(baseline["resourceCount"], 35)
        self.assertEqual(baseline["questionCount"], 109)
        current_by_id = {item["id"]: item for item in self.items}
        self.assertTrue(set(baseline["units"]).issubset(current_by_id))
        for item_id, snapshot in baseline["units"].items():
            current = current_by_id[item_id]
            self.assertGreaterEqual(len(current.get("questions", [])), snapshot["questionCount"], item_id)
            self.assertEqual(current.get("part"), snapshot["part"], item_id)
            self.assertEqual(current.get("documentType"), snapshot["documentType"], item_id)
            old_questions = current["questions"][:snapshot["questionCount"]]
            payload = json.dumps(old_questions, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
            self.assertEqual(hashlib.sha256(payload).hexdigest(), snapshot["sha256"], item_id)

    def test_reading_resource_and_choice_ids_are_unique(self):
        resource_ids = [x.get("id") for x in self.items]
        self.assertTrue(all(resource_ids))
        self.assertEqual(len(resource_ids), len(set(resource_ids)))
        choice_ids = [
            choice_id
            for item in self.items
            for q in item.get("questions", [])
            for choice_id in q.get("choiceIds", [])
        ]
        self.assertEqual(len(choice_ids), len(set(choice_ids)))
        for item in self.items:
            for q in item.get("questions", []):
                self.assertEqual(len(q.get("choices", [])), 4, item["id"])
                self.assertEqual(len(q.get("choiceIds", [])), 4, item["id"])
                self.assertIn(q.get("answerIndex"), range(4), item["id"])
                self.assertTrue(q.get("explanation", "").strip(), item["id"])

    def test_new_part7_batch_answer_positions_are_balanced(self):
        import collections
        distribution = collections.Counter(
            q["answerIndex"]
            for item in self.p7
            for q in item.get("questions", [])
            if q.get("evidence", {}).get("sourceLabels")
        )
        self.assertEqual(distribution, {0: 11, 1: 11, 2: 11, 3: 12})
        whole_distribution = collections.Counter(
            q["answerIndex"] for item in self.p7 for q in item.get("questions", [])
        )
        self.assertEqual(whole_distribution, {0: 27, 1: 27, 2: 27, 3: 27})

    def test_new_content_is_original_editorial_and_part7_batch_is_tagged(self):
        new_items = [x for x in self.items if x.get("editorialBatch") == "023"]
        self.assertEqual(len(new_items), 16)
        self.assertTrue(all(x.get("contentSource") == "original-editorial" for x in new_items))
        p7_evidence_questions = [
            q for item in self.p7 for q in item.get("questions", [])
            if q.get("evidence", {}).get("sourceLabels") and q.get("evidence", {}).get("quotes")
        ]
        self.assertEqual(len(p7_evidence_questions), 45)
        self.assertTrue(all(x.get("editorialStatus") == "internal-editorial-reviewed" for x in new_items))


if __name__ == "__main__":
    unittest.main()
