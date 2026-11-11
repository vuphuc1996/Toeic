"""Second-pass editorial regression checks for TOEIC Part 7 content."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
READING = json.loads((ROOT / "data/readings/reading-library.json").read_text(encoding="utf-8"))["readings"]


def item(item_id):
    return next(x for x in READING if x.get("id") == item_id)


class Part7EditorialReviewTests(unittest.TestCase):
    def test_part7_second_pass_scope_remains_63_questions(self):
        rows = [x for x in READING if x.get("part") == "Part 7"]
        self.assertEqual(sum(len(x.get("questions", [])) for x in rows), 63)
        self.assertEqual(len(rows), 24)

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


if __name__ == "__main__":
    unittest.main()
