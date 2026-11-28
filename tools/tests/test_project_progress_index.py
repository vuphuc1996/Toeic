"""Tests for reproducible, transparent project progress index calculations."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

spec = importlib.util.spec_from_file_location("project_progress_index", ROOT / "tools/project-progress-index.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ProjectProgressIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = module.build()

    def test_weights_sum_to_one_hundred_and_model_discloses_provisional_status(self):
        plan = module.load("tools/project-progress-plan-v2.95.71.json")
        self.assertEqual(sum(plan["weights"].values()), 100)
        self.assertEqual(self.report["totalWeight"], 100)
        self.assertIn("provisional", self.report["status"])
        self.assertIn("not an official", self.report["warning"])

    def test_core_denominators_and_quality_counts_are_live(self):
        metrics = {x["name"]: x for x in self.report["metrics"]}
        self.assertEqual(metrics["Vocabulary headwords vs 3,000 minimum"]["numerator"], 1221)
        self.assertEqual(metrics["Vocabulary headwords vs 3,000 minimum"]["denominator"], 3000)
        self.assertEqual(metrics["Guided pathway stage presence"]["numerator"], 3)
        self.assertEqual(metrics["Guided pathway stage presence"]["denominator"], 6)
        self.assertEqual(metrics["Outcome criteria with evidence instrumentation"]["numerator"], 31)
        self.assertEqual(metrics["Outcome criteria with evidence instrumentation"]["denominator"], 33)
        self.assertEqual(self.report["outcomeEvidenceDetail"]["toeicInstrumented"], 25)
        self.assertEqual(self.report["outcomeEvidenceDetail"]["toeicTotal"], 27)
        self.assertEqual(self.report["outcomeEvidenceDetail"]["questionCriterionLinks"], 1139)
        self.assertEqual(self.report["outcomeEvidenceDetail"]["uniqueQuestionIds"], 648)
        self.assertEqual(self.report["glossaryAudit"]["entries"], 567)
        self.assertEqual(self.report["glossaryAudit"]["flagged"], 2)
        self.assertEqual(self.report["glossaryAudit"]["duplicateGroups"], 0)

    def test_weighted_index_is_reproducible_and_caveated(self):
        self.assertAlmostEqual(self.report["weightedIndexPercent"], 76.00, places=2)
        output = module.render(self.report)
        self.assertIn("76.00%", output)
        self.assertIn("not an official total-system completion", output)
        self.assertIn("Mock exam approval", output)


if __name__ == "__main__":
    unittest.main()
