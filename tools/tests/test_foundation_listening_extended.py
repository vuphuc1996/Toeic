"""Integrity and runtime-isolation checks for supplementary A2 Listening clips."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def canonical_hash(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class FoundationExtendedListeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/learning-path/foundation-listening.json").read_text(encoding="utf-8"))
        cls.registry = json.loads((ROOT / "tools/foundation-a2-listening-extended-v2.91.0.json").read_text(encoding="utf-8"))
        cls.curriculum = json.loads((ROOT / "data/learning-path/pre-a1-a1.json").read_text(encoding="utf-8"))
        cls.app = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        cls.sw = (ROOT / "sw.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")

    def test_thirteen_new_clips_map_one_to_each_a2_lesson(self):
        a2_ids = {row["id"] for row in self.curriculum["lessons"] if row.get("level") == "A2"}
        rows = [row for row in self.data["clips"] if row.get("supplementary")]
        self.assertEqual(len(a2_ids), 13)
        self.assertEqual(len(rows), 13)
        self.assertEqual({row["lessonId"] for row in rows}, a2_ids)
        self.assertEqual({row["id"] for row in rows}, {f"{lesson_id}::listening2" for lesson_id in a2_ids})

    def test_clip_scripts_segments_and_questions_are_complete(self):
        rows = [row for row in self.data["clips"] if row.get("supplementary")]
        self.assertGreaterEqual(len({row["format"] for row in rows}), 10)
        all_question_ids = []
        for row in rows:
            with self.subTest(clip=row["id"]):
                self.assertTrue(75 <= len(row["script"].split()) <= 100)
                self.assertEqual("\n".join(f'{seg["speaker"]}: {seg["text"]}' for seg in row["segments"]), row["script"])
                self.assertEqual(len(row["segments"]), 6)
                self.assertEqual(sorted(seg["voice"] for seg in row["segments"]), ["female", "female", "female", "male", "male", "male"])
                self.assertEqual([q["skill"] for q in row["questions"]], ["listen-for-detail", "understand-purpose-context", "infer-next-action"])
                self.assertEqual([seg["speaker"] for seg in row["segments"]], [row["segments"][0]["speaker"], row["segments"][1]["speaker"], row["segments"][0]["speaker"], row["segments"][1]["speaker"], row["segments"][0]["speaker"], row["segments"][1]["speaker"]])
                self.assertEqual(len(row["questions"]), 3)
                self.assertEqual(row["reviewState"], "pending-independent-review")
                self.assertEqual(row["evidenceScope"], "listening2")
                for q in row["questions"]:
                    all_question_ids.append(q["id"])
                    self.assertEqual(len(q["choices"]), 4)
                    self.assertEqual(len(set(q["choices"])), 4)
                    self.assertIn(q["answerIndex"], range(4))
                    self.assertTrue(q["prompt"].strip() and q["rationale"].strip())
                    self.assertTrue(q.get("evidenceText") and q["evidenceText"] in row["script"])
        self.assertEqual(len(all_question_ids), 39)
        self.assertEqual(len(set(all_question_ids)), 39)

    def test_registry_hashes_match_and_are_pending_review(self):
        self.assertEqual(self.registry["version"], "2.91.0")
        self.assertEqual(self.registry["reviewStatus"], "pending-independent-review")
        rows = {row["id"]: row for row in self.registry["items"]}
        clips = [row for row in self.data["clips"] if row.get("supplementary")]
        self.assertEqual(len(rows), 13)
        for clip in clips:
            record = rows[clip["id"]]
            self.assertEqual(record["contentSha256"], canonical_hash(clip))
            self.assertEqual(record["questionIds"], [q["id"] for q in clip["questions"]])
            self.assertEqual(record["reviewState"], "pending-independent-review")

    def test_runtime_renders_supplementary_panel_and_scopes_progress(self):
        self.assertIn("renderFoundationListeningPanel(extendedListeningClip,id,'listening2')", self.app)
        self.assertIn("data-foundation-listening-scope", self.app)
        self.assertIn("scopeId?`${lessonId}::${scopeId}`:lessonId", self.app)
        self.assertIn("item.evidenceScope==='listening2'", self.app)
        self.assertIn("foundation-listening-extension", self.css)
        self.assertIn("./data/learning-path/foundation-listening.json", self.sw)


if __name__ == "__main__":
    unittest.main()
