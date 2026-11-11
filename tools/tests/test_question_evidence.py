"""Regression tests for the traceable TOEIC answer-to-source audit."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools" / "audit-question-evidence.py"
VERSION = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))["version"]
REPORT = ROOT / "docs" / "reports" / f"TOEIC_EDITORIAL_EVIDENCE_AUDIT_v{VERSION}.md"


class QuestionEvidenceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stdout + "\n" + result.stderr)
        cls.report = REPORT.read_text(encoding="utf-8")

    def test_all_222_answer_keys_are_mapped(self):
        self.assertIn("Questions indexed: **222** (113 Listening + 109 Reading).", self.report)

    def test_all_manual_review_categories_have_expected_counts(self):
        for expected in (
            "Manual paraphrase/inference checked against source | 3",
            "Part 1 Pexels source description and keyed action reviewed | 8",
            "Part 2 speech-act / response-fit checked | 30",
            "Part 5 sentence grammar checked | 30",
            "Part 6 context/cohesion checked | 16",
        ):
            self.assertIn(expected, self.report)

    def test_remaining_distractor_audit_scope_is_explicit(self):
        self.assertIn("distractor plausibility and uniqueness for the 126 direct/lexical items plus six inference/paraphrase items were reviewed in v2.15.0", self.report.lower())
        self.assertIn(f"TOEIC_DISTRACTOR_AUDIT_v{VERSION}.md", self.report)

    def test_no_unresolved_low_overlap_inference_label_remains(self):
        self.assertNotIn("Manual paraphrase/inference review |", self.report)
        self.assertEqual(self.report.count("manual-paraphrase-verified"), 0)
        self.assertIn("6 low-overlap paraphrase/inference items were checked", self.report)


if __name__ == "__main__":
    unittest.main()
