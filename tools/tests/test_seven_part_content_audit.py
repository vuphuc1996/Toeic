"""Regression tests for the deterministic 7-Part TOEIC content & evidence audit."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "audit_seven_part_content", ROOT / "tools/audit-seven-part-content.py"
)
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class SevenPartContentAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MOD.audit_all(ROOT)
        cls.md = MOD.render_markdown(cls.report)

    def test_authoritative_inventory_counts_across_all_banks(self):
        t = self.report["totals"]
        self.assertEqual(t["listeningUnits"], 145)
        self.assertEqual(t["listeningQuestions"], 295)
        self.assertEqual(t["listeningApprovedForMock"], 102)
        self.assertEqual(t["listeningHumanReviewRequired"], 193)
        self.assertEqual(t["readingUnits"], 73)
        self.assertEqual(t["readingQuestions"], 287)
        self.assertEqual(t["readingApprovedForMock"], 200)
        self.assertEqual(t["readingHumanReviewRequired"], 87)
        self.assertEqual(t["separatePart5Questions"], 80)
        self.assertEqual(t["grammarLessons"], 58)
        self.assertEqual(t["grammarExercises"], 169)
        self.assertEqual(t["totalQuestionsAllBanks"], 831)
        self.assertEqual(t["totalHumanReviewRequired"], 360)

    def test_zero_structural_errors_and_apostrophe_normalization(self):
        self.assertEqual(self.report["structuralErrors"], [])
        self.assertEqual(self.report["duplicateStems"], [])
        self.assertEqual(MOD.norm_choice("its"), "its")
        self.assertEqual(MOD.norm_choice("it\u2019s"), "it's")
        self.assertNotEqual(MOD.norm_choice("its"), MOD.norm_choice("it\u2019s"))

    def test_epistemic_separation_and_part_breakdown(self):
        parts = self.report["parts"]
        self.assertEqual(parts["Listening Part 1"]["approved_for_mock_questions"], 8)
        self.assertEqual(parts["Listening Part 1"]["human_review_required_questions"], 1)
        self.assertEqual(parts["Listening Part 2"]["approved_for_mock_questions"], 25)
        self.assertEqual(parts["Listening Part 2"]["human_review_required_questions"], 36)
        self.assertEqual(parts["Listening Part 3"]["approved_for_mock_questions"], 39)
        self.assertEqual(parts["Listening Part 3"]["human_review_required_questions"], 84)
        self.assertEqual(parts["Listening Part 4"]["approved_for_mock_questions"], 30)
        self.assertEqual(parts["Listening Part 4"]["human_review_required_questions"], 72)
        self.assertEqual(parts["Reading Part 5"]["approved_for_mock_questions"], 60)
        self.assertEqual(parts["Reading Part 6"]["approved_for_mock_questions"], 32)
        self.assertEqual(parts["Reading Part 7"]["approved_for_mock_questions"], 108)
        self.assertEqual(parts["Reading Part 7"]["human_review_required_questions"], 87)
        self.assertEqual(parts["Separate Part 5 Practice"]["human_review_required_questions"], 80)
        self.assertEqual(parts["Grammar Support (Part 5/6)"]["practice_support_questions"], 169)
        self.assertIn("AI_TRIAGE / STRUCTURAL", self.md)
        self.assertIn("APPROVED_FOR_MOCK", self.md)
        self.assertIn("HUMAN_REVIEW_REQUIRED", self.md)
        self.assertIn("PRACTICE_SUPPORT", self.md)

    def test_cli_is_read_only_on_canonical_sources(self):
        canonical_files = [
            ROOT / "data/manifest.json",
            ROOT / "data/vocabulary/A.json",
            ROOT / "data/listening/listening-library.json",
            ROOT / "data/readings/reading-library.json",
            ROOT / "data/practice/part5-sentence-completion.json",
            ROOT / "data/grammar/lessons.json",
        ]
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in canonical_files}
        with tempfile.TemporaryDirectory() as tmp:
            md_out = Path(tmp) / "seven_part.md"
            json_out = Path(tmp) / "seven_part.json"
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools/audit-seven-part-content.py"),
                    "--markdown-output",
                    str(md_out),
                    "--json-output",
                    str(json_out),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertTrue(md_out.is_file())
            self.assertTrue(json_out.is_file())
        after = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in canonical_files}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
