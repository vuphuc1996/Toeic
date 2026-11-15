"""Quality and integration checks for the Pre-A1/A1 synthesized listening practice."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FoundationListeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/learning-path/foundation-listening.json").read_text(encoding="utf-8"))
        cls.lessons = json.loads((ROOT / "data/learning-path/pre-a1-a1.json").read_text(encoding="utf-8"))["lessons"]
        cls.app = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.sw = (ROOT / "sw.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "assets/css/design-system.css").read_text(encoding="utf-8")

    def test_ten_clips_map_one_to_each_stable_lesson(self):
        self.assertEqual(len(self.data["clips"]), 10)
        self.assertEqual({x["lessonId"] for x in self.data["clips"]}, {x["id"] for x in self.lessons})
        self.assertEqual(len({x["id"] for x in self.data["clips"]}), 10)

    def test_scripts_and_question_banks_are_complete_and_unique(self):
        question_ids = []
        for clip in self.data["clips"]:
            with self.subTest(clip=clip["id"]):
                self.assertGreaterEqual(len(clip["script"].split()), 25)
                self.assertLessEqual(len(clip["script"].split()), 45)
                self.assertEqual(len(clip["questions"]), 2)
                for question in clip["questions"]:
                    self.assertEqual(len(question["choices"]), 4)
                    self.assertEqual(len(set(question["choices"])), 4)
                    self.assertIn(question["answerIndex"], range(4))
                    self.assertTrue(question["prompt"] and question["rationale"])
                    question_ids.append(question["id"])
        self.assertEqual(len(question_ids), 20)
        self.assertEqual(len(question_ids), len(set(question_ids)))

    def test_selected_answer_matches_the_listening_detail(self):
        clip = next(x for x in self.data["clips"] if x["lessonId"] == "a1-plurals")
        question = next(x for x in clip["questions"] if x["id"].endswith("::q2"))
        self.assertEqual(question["choices"][question["answerIndex"]], "To the storage room")

    def test_answer_key_positions_are_balanced(self):
        counts = [sum(q["answerIndex"] == i for clip in self.data["clips"] for q in clip["questions"]) for i in range(4)]
        self.assertEqual(counts, [5, 5, 5, 5])

    def test_scope_discloses_synthesized_audio_not_ets_recording(self):
        self.assertIn("browser-speech-synthesis", self.data["playback"]["engine"])
        self.assertIn("not authentic recorded audio", self.data["evidencePolicy"]["scope"])
        self.assertTrue(self.data["playback"]["scriptHiddenByDefault"])
        self.assertTrue(self.data["playback"]["usesCurrentAppVoiceSettings"])

    def test_runtime_keeps_listening_evidence_separate_and_integrated(self):
        self.assertIn("./data/learning-path/foundation-listening.json", self.app)
        self.assertIn("toeic:foundation-listening-progress:v1", self.app)
        self.assertIn("recordFoundationListeningAttempt", self.app)
        self.assertIn("data-foundation-listening-answer", self.app)
        self.assertIn("data-foundation-listening-play", self.app)
        self.assertIn("data-foundation-listening-transcript-toggle", self.app)
        self.assertIn("./foundation-listening-evidence.js", self.app)

    def test_service_worker_precaches_required_and_app_shell_resources(self):
        required = self.sw.split("const REQUIRED = ", 1)[1].split(";", 1)[0]
        shell = self.sw.split("const APP_SHELL = ", 1)[1].split(";", 1)[0]
        for path in ("./assets/js/foundation-listening-evidence.js", "./data/learning-path/foundation-listening.json"):
            self.assertEqual(required.count(path), 1)
            self.assertEqual(shell.count(path), 1)


if __name__ == "__main__":
    unittest.main()
