"""Regression checks for the guided Pre-A1/A1 foundation pathway."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FoundationPathwayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/learning-path/pre-a1-a1.json").read_text(encoding="utf-8"))
        cls.app = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.sw = (ROOT / "sw.js").read_text(encoding="utf-8")

    def test_lesson_ids_are_stable_and_unique(self):
        ids = [row["id"] for row in self.data["lessons"]]
        self.assertEqual(len(ids), 10)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(re.fullmatch(r"(?:pa1|a1)-[a-z0-9-]+", value) for value in ids))

    def test_each_lesson_has_teaching_and_assessment(self):
        for lesson in self.data["lessons"]:
            with self.subTest(lesson=lesson["id"]):
                self.assertTrue(lesson["objective"])
                self.assertTrue(lesson["explanation"])
                self.assertGreaterEqual(len(lesson["examples"]), 2)
                self.assertEqual(len(lesson["choices"]), 4)
                self.assertIn(lesson["answerIndex"], range(4))
                self.assertTrue(lesson["rationale"])

    def test_each_lesson_has_three_stable_evidence_questions(self):
        all_ids = []
        for lesson in self.data["lessons"]:
            bank = lesson.get("questionBank", [])
            self.assertEqual(len(bank), 3, lesson["id"])
            ids = [item["id"] for item in bank]
            self.assertEqual(len(ids), len(set(ids)))
            self.assertTrue(all(item["choices"] and len(item["choices"]) == 4 for item in bank))
            self.assertTrue(all(item["answerIndex"] in range(4) and item["rationale"] for item in bank))
            all_ids.extend(ids)
        self.assertEqual(len(all_ids), 30)
        self.assertEqual(len(all_ids), len(set(all_ids)))
        self.assertEqual(self.data["evidencePolicy"]["minimumUniqueQuestions"], 3)

    def test_each_lesson_has_separate_contextual_application_task(self):
        task_ids = []
        for lesson in self.data["lessons"]:
            task = lesson.get("applicationTask")
            self.assertIsNotNone(task, lesson["id"])
            self.assertEqual(task["id"], f"{lesson['id']}::apply1")
            self.assertEqual(len(task["choices"]), 4)
            self.assertIn(task["answerIndex"], range(4))
            self.assertTrue(task["prompt"] and task["rationale"] and task["focus"])
            task_ids.append(task["id"])
        self.assertEqual(len(task_ids), len(set(task_ids)))
        self.assertIn("recordFoundationApplicationAttempt", self.app)
        self.assertIn("data-foundation-application-answer", self.app)

    def test_learning_path_is_loaded_and_rendered(self):
        self.assertIn("./data/learning-path/pre-a1-a1.json", self.app)
        self.assertIn("function renderFoundationPath()", self.app)
        self.assertIn("function answerFoundationQuestion(", self.app)
        self.assertIn('id="page-foundation"', self.html)
        self.assertIn('data-page="foundation"', self.html)

    def test_progress_is_isolated_from_existing_indexeddb(self):
        self.assertIn("toeic:foundation-progress:v1", self.app)
        self.assertIn("DB_NAME = 'toeic-vocabulary-phase1'", self.app)
        self.assertIn("./data/learning-path/pre-a1-a1.json", self.sw)


if __name__ == "__main__":
    unittest.main()
