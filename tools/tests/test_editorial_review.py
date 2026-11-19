"""Second-pass editorial regression checks for TOEIC Part 7 content."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
READING = json.loads((ROOT / "data/readings/reading-library.json").read_text(encoding="utf-8"))["readings"]


def item(item_id):
    return next(x for x in READING if x.get("id") == item_id)


class Part7EditorialReviewTests(unittest.TestCase):
    def test_part7_inventory_is_monotonic_and_structurally_complete(self):
        rows = [x for x in READING if x.get("part") == "Part 7"]
        # The floor protects already-reviewed coverage without pinning the suite
        # to a historical count that breaks whenever a valid content batch grows.
        self.assertGreaterEqual(len(rows), 44)
        self.assertGreaterEqual(sum(len(x.get("questions", [])) for x in rows), 171)
        ids = [row.get("id") for row in rows]
        self.assertTrue(all(ids), "Every Part 7 resource needs a stable ID")
        self.assertEqual(len(ids), len(set(ids)), "Part 7 resource IDs must be unique")
        for row in rows:
            self.assertTrue(row.get("passage") or any(doc.get("content", "").strip() for doc in row.get("documents", [])), row.get("id"))
            self.assertTrue(row.get("questions"), row.get("id"))
            for index, question in enumerate(row["questions"], 1):
                self.assertIsInstance(question.get("question"), str, f"{row['id']} Q{index}")
                self.assertTrue(question["question"].strip(), f"{row['id']} Q{index}")

    def test_hotel_room_dates_match_two_night_stays_and_departure(self):
        row = item("part7-triple-conference-arrangements")
        docs = " ".join(d.get("content", "") for d in row.get("documents", []))
        self.assertIn("Two speakers will stay for two nights", docs)
        self.assertIn("until her departure after the morning session on April 19", docs)
        self.assertIn("for the nights of April 17 and April 18", docs)
        q2 = row["questions"][1]
        self.assertEqual(q2["choices"][q2["answerIndex"]], "April 19")
        self.assertIn("hai phòng được đặt cho các đêm 17 và 18", row.get("translation", ""))

    def test_reimbursement_course_is_after_policy_effective_date(self):
        row = item("part7-double-training-reimbursement")
        docs = " ".join(d.get("content", "") for d in row.get("documents", []))
        self.assertIn("Beginning July 1", docs)
        self.assertIn("completed a project-management course on July 18", docs)
        self.assertIn("approved the course in May", docs)
        self.assertEqual(row["questions"][2]["choices"][row["questions"][2]["answerIndex"]], "His course was approved before he registered")

    def test_all_part7_question_keys_and_choice_ids_remain_well_formed(self):
        for row in (x for x in READING if x.get("part") == "Part 7"):
            for qn, q in enumerate(row.get("questions", []), 1):
                self.assertEqual(len(q.get("choices", [])), 4, f"{row['id']} Q{qn}")
                self.assertTrue(0 <= q.get("answerIndex", -1) < 4, f"{row['id']} Q{qn}")
                self.assertEqual(len(q.get("choiceIds", [])), 4, f"{row['id']} Q{qn}")
                self.assertEqual(len(set(q["choiceIds"])), 4, f"{row['id']} Q{qn}")

    def test_part7_choices_are_nonempty_and_textually_distinct(self):
        """Catch editorially broken option sets that pass index/ID checks alone."""
        for row in (x for x in READING if x.get("part") == "Part 7"):
            for qn, question in enumerate(row.get("questions", []), 1):
                choices = question.get("choices", [])
                self.assertEqual(len(choices), 4, f"{row['id']} Q{qn}: exactly four choices")
                normalized = [" ".join(str(choice).casefold().split()) for choice in choices]
                self.assertTrue(all(normalized), f"{row['id']} Q{qn}: choices cannot be blank")
                self.assertEqual(len(normalized), len(set(normalized)),
                                 f"{row['id']} Q{qn}: duplicate choice text")

    def test_part7_answer_index_is_an_integer_not_a_boolean_or_string(self):
        """Python bool is an int subclass; reject it explicitly for answer keys."""
        for row in (x for x in READING if x.get("part") == "Part 7"):
            for qn, question in enumerate(row.get("questions", []), 1):
                answer_index = question.get("answerIndex")
                self.assertIs(type(answer_index), int, f"{row['id']} Q{qn}: answerIndex must be integer")
                self.assertIn(answer_index, range(4), f"{row['id']} Q{qn}: answerIndex out of range")


if __name__ == "__main__":
    unittest.main()
