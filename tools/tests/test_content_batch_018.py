"""Integrity, provenance, identity and Mock exclusion for Listening photo batch 018."""
from __future__ import annotations

import csv
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_IDS = {
    "part1-construction-plans",
    "part1-laboratory-bench",
    "part1-supermarket-shelf",
}


def read_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class ContentBatch018Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = read_json("data/listening/listening-library.json")["listening"]
        cls.by_id = {row["id"]: row for row in cls.library}
        cls.batch = read_json("tools/content-batch-018-v2.95.86.json")
        cls.resource_map = read_json("data/learning-path/objective-resource-map.json")
        cls.criterion_map = read_json("data/learning-path/objective-criterion-map.json")
        with (ROOT / "assets/listening/ATTRIBUTION.csv").open(encoding="utf-8-sig", newline="") as handle:
            cls.attribution = {row["question_id"]: row for row in csv.DictReader(handle)}

    def test_batch_manifest_and_inventory_are_exact(self):
        self.assertEqual(self.batch["batch"], "018")
        self.assertEqual(self.batch["version"], "2.95.86")
        self.assertEqual(self.batch["counts"], {
            "listeningResources": 3,
            "listeningQuestions": 3,
            "part1Resources": 3,
            "approvedForMock": 0,
            "reservePendingIndependentReview": 3,
        })
        self.assertEqual({row["id"] for row in self.batch["listening"]}, EXPECTED_IDS)
        self.assertEqual(len(self.batch["listening"]), 3)
        self.assertTrue(EXPECTED_IDS.issubset(self.by_id))
        self.assertEqual(sum(row.get("editorialBatch") == "018" for row in self.library), 3)

    def test_all_photos_have_ai_provenance_and_valid_local_jpg_assets(self):
        for ident in EXPECTED_IDS:
            unit = self.by_id[ident]
            self.assertTrue(unit["photo"].startswith("./assets/listening/"))
            self.assertTrue(unit["photo"].endswith(".jpg"))
            asset = ROOT / unit["photo"].removeprefix("./")
            self.assertTrue(asset.is_file(), unit["photo"])
            self.assertLessEqual(asset.stat().st_size, 400_000)
            optional_match = re.search(r"const OPTIONAL = (\[.*?\]);", (ROOT / "sw.js").read_text(encoding="utf-8"), re.S)
            self.assertIsNotNone(optional_match, "Service Worker OPTIONAL cache list is missing")
            optional_assets = set(json.loads(optional_match.group(1)))
            self.assertIn(unit["photo"], optional_assets, "Part 1 photo should be in the best-effort offline cache")
            self.assertEqual(unit["photoSourceType"], "ai-generated")
            self.assertIn("Google Imagen", unit["sourceNote"])
            row = self.attribution[ident]
            self.assertEqual(row["source_type"], "ai-generated")
            self.assertEqual(row["provider"], "Google Imagen image generation")
            self.assertIn("not an external stock", row["source_page"])
            self.assertIn("AI-generated", row["license"])

    def test_questions_have_verbatim_audio_evidence_and_fail_closed_review_flags(self):
        all_existing_choice_ids = {
            choice_id
            for unit in self.library if unit["id"] not in EXPECTED_IDS
            for question in unit.get("questions", [])
            for choice_id in question.get("choiceIds", [])
        }
        new_choice_ids = []
        for ident in EXPECTED_IDS:
            unit = self.by_id[ident]
            self.assertEqual(unit["part"], "Part 1")
            self.assertEqual(unit["editorialStatus"], "reserve-pending-independent-review")
            self.assertEqual(unit["editorialBatch"], "018")
            self.assertEqual(unit["contentBatch"], "batch-018-part1-ai-generated-photo-expansion")
            self.assertEqual(unit["mockExamEligibility"], "excluded-until-independent-review")
            self.assertEqual(unit["reviewNote"], "internal-author-check; independent-second-review-pending")
            self.assertIn("independent second-person review remains pending", unit["visualEvidenceNote"])
            self.assertEqual(len(unit["segments"]), 4)
            self.assertEqual(len(unit["questions"]), 1)
            question = unit["questions"][0]
            self.assertIs(question.get("mockEligible"), False)
            self.assertEqual(len(question["choices"]), 4)
            self.assertEqual(question["choices"], ["Option A", "Option B", "Option C", "Option D"])
            self.assertEqual(len(question["choiceIds"]), 4)
            self.assertEqual(len(set(question["choiceIds"])), 4)
            self.assertIn(question["answerIndex"], range(4))
            self.assertEqual(question["evidenceText"], unit["segments"][question["answerIndex"]]["text"])
            self.assertTrue(question["explanation"].strip())
            new_choice_ids.extend(question["choiceIds"])
        self.assertEqual(len(new_choice_ids), 12)
        self.assertEqual(len(new_choice_ids), len(set(new_choice_ids)))
        self.assertFalse(set(new_choice_ids) & all_existing_choice_ids)

    def test_resource_registration_does_not_instrument_or_promote_outcomes(self):
        p1 = next(row for row in self.resource_map["objectives"] if row["id"] == "listening-part-1")
        self.assertTrue(EXPECTED_IDS.issubset(set(p1["resourceIds"])))
        self.assertEqual(sum(row["part"] == "Part 1" for row in self.library), 12)
        serialized_criterion_map = json.dumps(self.criterion_map, ensure_ascii=False)
        self.assertTrue(all(ident not in serialized_criterion_map for ident in EXPECTED_IDS))
        self.assertEqual(self.criterion_map["mappingCountsByCriterion"]["listening-part-1-visual-audio-match"], 8)
        self.assertEqual(self.criterion_map["mappingCountsByCriterion"]["listening-part-1-detail-retention"], 8)
        self.assertNotIn("listening-part-1-paraphrase-recognition", self.criterion_map["mappingCountsByCriterion"])

    def test_mock_pool_is_unchanged_and_pending_reserve_is_three_larger(self):
        approved = [
            unit for unit in self.library
            if unit.get("editorialStatus") in (None, "approved-for-mock", "internal-editorial-reviewed")
        ]
        pending = [unit for unit in self.library if unit.get("editorialStatus") == "reserve-pending-independent-review"]
        approved_count = sum(
            question.get("mockEligible") is not False
            for unit in approved for question in unit.get("questions", [])
        )
        pending_count = sum(len(unit.get("questions", [])) for unit in pending)
        pending_by_part = Counter(
            unit["part"] for unit in pending for _ in unit.get("questions", [])
        )
        self.assertEqual(approved_count, 102)
        self.assertEqual(pending_count, 196)
        self.assertEqual(pending_by_part["Part 1"], 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
