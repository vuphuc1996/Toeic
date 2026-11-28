"""Regression tests for Workstream F Full-Mock readiness consolidation."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("audit_mock_readiness", ROOT / "tools/audit-mock-readiness.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class MockReadinessAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = MOD.build_report(ROOT)
        cls.md = MOD.render_markdown(cls.report)

    def test_approved_only_pools_and_two_disjoint_reading_forms(self):
        self.assertEqual(self.report["listeningApprovedTotal"], 102)
        self.assertEqual(self.report["approvedPools"]["Listening Part 4"], 30)
        self.assertEqual(self.report["listeningReserveTotal"], 196)
        self.assertEqual(self.report["readingApprovedTotal"], 200)
        self.assertEqual(self.report["readingReserveTotal"], 87)
        self.assertEqual(self.report["separatePart5PracticeOnly"], 80)
        self.assertTrue(self.report["readingTwoDisjointFullFormsVerified"])

    def test_listening_bottleneck_and_overlap_disclosure(self):
        self.assertEqual(self.report["listeningSecondFullFormMinOverlap"], 98)
        self.assertEqual(self.report["listeningSecondFullFormMaxNew"], 2)
        self.assertEqual(self.report["listeningPostReviewByPart"]["Part 1"], 12)
        self.assertEqual(self.report["listeningPostReviewDisjointFullForms"], 2)
        self.assertTrue(self.report["modes"]["full"]["singleFormSupported"])
        self.assertEqual(self.report["modes"]["full"]["disjointListeningForms"], 1)
        self.assertEqual(self.report["modes"]["full"]["disjointReadingForms"], 2)
        self.assertEqual(self.report["modes"]["half"]["disjointFullCombinedForms"], 2)
        self.assertIn("Zero ETS scaled score claims", self.md)

    def test_cli_generates_report_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            md_out = Path(tmp) / "mock_readiness.md"
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tools/audit-mock-readiness.py"), "--markdown-output", str(md_out)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertIn("Listening Part 1", md_out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
