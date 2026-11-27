"""Regression contract for Word Family graph reconciliation Batch 027 (v2.95.74)."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
audit_spec = importlib.util.spec_from_file_location(
    "word_family_audit", ROOT / "tools/audit-word-family-graph.py"
)
audit_mod = importlib.util.module_from_spec(audit_spec)
assert audit_spec.loader is not None
audit_spec.loader.exec_module(audit_mod)


class WordFamilyBatch027Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = audit_mod.load_source(ROOT)

    def test_canonical_headword_and_graph_counts(self):
        self.assertEqual(self.report["headwords"], 1221)
        self.assertEqual(self.report["headwords_with_family"], 331)
        self.assertEqual(self.report["link_count"], 428)
        self.assertEqual(len(self.report["missing_targets"]), 50)

    def test_structural_integrity_zero_defects(self):
        self.assertEqual(len(self.report["duplicate_headwords"]), 0)
        self.assertEqual(len(self.report["duplicate_links"]), 0)
        self.assertEqual(len(self.report["malformed"]), 0)
        self.assertEqual(len(self.report["pos_mismatches"]), 0)
        self.assertEqual(len(self.report["nonreciprocal_links"]), 0)

    def test_sense_anchor_mismatch_count(self):
        self.assertEqual(len(self.report["meaning_mismatches"]), 70)

    def test_ci_registers_this_batch_test(self):
        workflow = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
        self.assertIn("-p 'test_word_family_batch_027.py'", workflow)


if __name__ == "__main__":
    unittest.main()
