"""Regression contract for Related Glossary remediation Batch 046 (v2.95.72)."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import re
import unittest
from pathlib import Path
from glossary_test_helpers import restore_batch_046

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / "patches-related-terms/v2.95.72/related-terms-046.json"
LEDGER_PATH = ROOT / "patches-related-terms/v2.95.72/batch-046-glossary-ledger.json"
ALLOWED_FIELDS = {"pos", "definition_en", "source", "sourceUrls", "sourceRelease"}

qa_spec = importlib.util.spec_from_file_location("glossary_qa", ROOT / "tools/audit-related-glossary-quality.py")
qa_mod = importlib.util.module_from_spec(qa_spec)
assert qa_spec.loader is not None
qa_spec.loader.exec_module(qa_mod)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class RelatedGlossaryBatch046Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.glossary = read_json(ROOT / "data/related-terms.json")
        cls.rows = {row["term"].casefold(): row for row in cls.glossary["terms"]}

    def test_batch_inventory_and_guarded_fields(self):
        self.assertEqual(self.patch["batchId"], "related-glossary-046-v2.95.72")
        self.assertEqual(self.ledger["batch"], "046")
        self.assertEqual(self.ledger["release"], "2.95.72")
        self.assertEqual(self.ledger["predecessorRelease"], "2.95.71")
        self.assertEqual(self.ledger["count"], 65)
        self.assertEqual(len(self.patch["operations"]), 65)
        self.assertEqual({x["term"].casefold() for x in self.patch["operations"]}, {x["term"].casefold() for x in self.ledger["records"]})
        for op in self.patch["operations"]:
            self.assertTrue(set(op["set"]).issubset(ALLOWED_FIELDS))
            self.assertIn("source", op["set"])
            self.assertIn("sourceUrls", op["set"])
            self.assertEqual(op["set"]["sourceRelease"], "2.95.72")

    def test_remediated_entries_have_valid_pos_definition_and_provenance(self):
        for record in self.ledger["records"]:
            term = record["term"].casefold()
            row = self.rows[term]
            self.assertIn(row.get("pos"), {"n", "v", "adj", "adv", "pron", "v/n", "v/adj", "n/adj", "n/v"}, term)
            definition = row.get("definition_en", "")
            self.assertGreaterEqual(len(definition.split()), 5, term)
            self.assertNotRegex(definition, re.compile(r"placeholder|reference gloss|todo|tbd|definition pending", re.I))
            self.assertEqual(row["meaning_vi"], record["meaning_vi_preserved"], term)
            self.assertEqual(row.get("sourceRelease"), "2.95.72")
            urls = row.get("sourceUrls", [])
            self.assertEqual(len(urls), 1)
            self.assertRegex(urls[0], r"^https://(en\.wiktionary\.org/wiki/|dictionary\.cambridge\.org/dictionary/english/)")
            self.assertIn("independent editorial review pending", row["source"].lower())

    def test_historical_reconstruction_reproduces_v29571_base_sha256(self):
        restored = restore_batch_046(self.glossary, ROOT)
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        reconstructed = hashlib.sha256(payload).hexdigest()
        self.assertEqual(reconstructed, self.patch["baseFileSha256"])
        self.assertEqual(reconstructed, self.ledger["baseRelatedTermsSha256"])

    def test_quality_audit_reflects_batch_046_and_keeps_unsupported_entries_flagged(self):
        audit = qa_mod.audit(self.glossary["terms"])
        self.assertEqual(audit["entries"], 567)
        self.assertEqual(audit["flagged_entries"], 54)
        self.assertEqual(audit["issue_counts"]["placeholder-definition"], 1)
        self.assertEqual(audit["issue_counts"]["missing-source-provenance"], 1)
        self.assertEqual(audit["issue_counts"]["missing-definition"], 51)
        self.assertEqual(audit["issue_counts"]["missing-pos"], 52)
        self.assertEqual(audit["issue_counts"]["short-definition-review"], 2)
        self.assertEqual(len(audit["duplicates"]), 0)
        flagged_terms = {x["term"]: x["issues"] for x in audit["flagged"]}
        self.assertIn("once-a-year", flagged_terms)
        self.assertIn("placeholder-definition", flagged_terms["once-a-year"])

    def test_ci_registers_this_batch_test(self):
        workflow = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
        self.assertIn("-p 'test_related_glossary_batch_046.py'", workflow)


if __name__ == "__main__":
    unittest.main()
