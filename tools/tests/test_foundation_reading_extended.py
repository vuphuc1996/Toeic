"""Integrity and app-integration checks for the optional A2 extended Reading bank."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def canonical_hash(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class FoundationExtendedReadingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resource = json.loads((ROOT / "data/learning-path/foundation-reading-extended.json").read_text(encoding="utf-8"))
        cls.registry = json.loads((ROOT / "tools/foundation-a2-reading-extended-v2.89.0.json").read_text(encoding="utf-8"))
        cls.curriculum = json.loads((ROOT / "data/learning-path/pre-a1-a1.json").read_text(encoding="utf-8"))
        cls.app = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.sw = (ROOT / "sw.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")

    def test_thirteen_a2_lessons_have_one_extended_passage_each(self):
        a2_ids = {row["id"] for row in self.curriculum["lessons"] if row.get("level") == "A2"}
        passages = self.resource["passages"]
        self.assertEqual(len(a2_ids), 13)
        self.assertEqual(len(passages), 13)
        self.assertEqual({row["lessonId"] for row in passages}, a2_ids)
        self.assertEqual(len({row["id"] for row in passages}), 13)
        self.assertTrue(all(row["id"] == f'{row["lessonId"]}::reading2' for row in passages))

    def test_each_passage_has_three_distinct_questions_and_exact_source_evidence(self):
        question_ids = []
        answer_positions = [0, 0, 0, 0]
        for passage in self.resource["passages"]:
            with self.subTest(passage=passage["id"]):
                self.assertTrue(90 <= len(passage["text"].split()) <= 110)
                self.assertEqual(len(passage["questions"]), 3)
                self.assertEqual(passage.get("level"), "A2")
                self.assertEqual(passage.get("minimumUniqueQuestions"), 3)
                self.assertEqual(passage.get("practiceAccuracyThreshold"), 0.67)
                self.assertEqual(passage.get("editorialStatus"), "pending-independent-editorial-review")
                self.assertTrue(passage.get("format"))
                for question in passage["questions"]:
                    question_ids.append(question["id"])
                    self.assertTrue(question["id"].startswith(passage["id"] + "::q"))
                    self.assertEqual(len(question["choices"]), 4)
                    self.assertEqual(len(set(question["choices"])), 4)
                    self.assertIn(question["answerIndex"], range(4))
                    self.assertTrue(question["prompt"].strip())
                    self.assertTrue(question["rationale"].strip())
                    self.assertGreaterEqual(len(question["evidenceText"].strip()), 12)
                    self.assertIn(question["evidenceText"], passage["text"])
                    answer_positions[question["answerIndex"]] += 1
        self.assertEqual(len(question_ids), 39)
        self.assertEqual(len(question_ids), len(set(question_ids)))
        self.assertLessEqual(max(answer_positions) - min(answer_positions), 2)

    def test_registry_hashes_match_complete_passages(self):
        self.assertEqual(self.registry["version"], "2.89.0")
        self.assertIn("complete passage object", self.registry["hashPolicy"])
        rows = {row["id"]: row for row in self.registry["items"]}
        self.assertEqual(len(rows), 13)
        for passage in self.resource["passages"]:
            row = rows[passage["id"]]
            with self.subTest(passage=passage["id"]):
                self.assertEqual(row["lessonId"], passage["lessonId"])
                self.assertEqual(row["questionIds"], [q["id"] for q in passage["questions"]])
                self.assertEqual(row["wordCount"], len(passage["text"].split()))
                self.assertEqual(row["editorialStatus"], passage["editorialStatus"])
                self.assertEqual(row["contentSha256"], canonical_hash(passage))

    def test_loader_rendering_scope_and_resume_hooks_are_integrated(self):
        self.assertIn("foundationReadingExtendedPassages: []", self.app)
        self.assertIn("fetchReleaseJson('./data/learning-path/foundation-reading-extended.json')", self.app)
        self.assertIn("state.foundationReadingExtendedPassages=Array.isArray(foundationReadingExtendedData.passages)", self.app)
        self.assertIn("renderFoundationReadingPanel(extendedReadingPassage,id,'reading2')", self.app)
        self.assertIn("scopeId==='reading2'?state.foundationReadingExtendedPassages:state.foundationReadingPassages", self.app)
        self.assertIn("scopeId?`${lessonId}::${scopeId}`:lessonId", self.app)
        self.assertIn("data-foundation-reading-scope", self.app)
        self.assertIn("data-foundation-scope", self.app)
        self.assertIn("openExtensionIds", self.app)
        self.assertIn("data-foundation-extension", self.app)
        self.assertIn("chờ kiểm duyệt độc lập", self.app)
        self.assertIn("chờ duyệt ${extendedReading.uniqueQuestions}", self.app)

    def test_extended_reading_is_required_in_both_service_worker_lists(self):
        path = '"./data/learning-path/foundation-reading-extended.json"'
        self.assertEqual(self.sw.count(path), 2)

    def test_extension_layout_is_responsive_and_uses_readable_type(self):
        self.assertIn(".foundation-reading-extension", self.css)
        self.assertIn("@media(max-width:560px){.foundation-reading-extension>summary", self.css)
        self.assertIn("font-size:12.5px", self.css)

    def test_existing_base_reading_resource_is_not_replaced(self):
        base = json.loads((ROOT / "data/learning-path/foundation-reading.json").read_text(encoding="utf-8"))
        self.assertEqual(len(base["passages"]), 23)
        self.assertEqual(sum(1 for row in base["passages"] if row.get("level") == "A2"), 13)
        self.assertTrue(self.resource["evidencePolicy"]["scope"].startswith("extended-reading-practice-only"))
        self.assertEqual(self.resource["evidencePolicy"]["storageKey"], "toeic:foundation-reading-progress:v1")
        self.assertEqual(self.resource["evidencePolicy"]["progressScopeSuffix"], "reading2")


if __name__ == "__main__":
    unittest.main()
