"""Regression coverage for Cambridge-sourced glossary completion Batch 033."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

class RelatedGlossaryBatch033Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json("patches-related-terms/v2.95.39/batch-033-glossary-ledger.json")
        cls.patch = read_json("patches-related-terms/v2.95.39/related-terms-033.json")
        cls.data = read_json("data/related-terms.json")
        cls.current = {row["term"].casefold(): row for row in cls.data["terms"]}

    def test_batch_has_eight_named_additions(self):
        expected = {"ability", "acceptable", "action", "accusation", "advertise", "advise", "allow", "announce"}
        self.assertEqual(self.ledger["batch"], "033")
        self.assertEqual(self.ledger["release"], "2.95.39")
        self.assertEqual(self.ledger["count"], 8)
        self.assertEqual({r["term"] for r in self.ledger["records"]}, expected)
        self.assertEqual({r["term"] for r in self.patch["operations"]}, expected)

    def test_each_addition_has_cambridge_source_pos_and_definition(self):
        for record in self.ledger["records"]:
            row = self.current[record["term"].casefold()]
            for field in ("meaning_vi_preserved", "pos", "definition_en", "source", "sourceUrls"):
                expected = record[field]
                actual = row["meaning_vi"] if field == "meaning_vi_preserved" else row.get(field)
                self.assertEqual(actual, expected, record["term"])
            self.assertIn(row["pos"], {"n", "v", "adj", "adv"})
            self.assertTrue(row["definition_en"].strip())
            self.assertTrue(row["sourceUrls"][0].startswith("https://dictionary.cambridge.org/dictionary/"))

    def test_existing_glossary_terms_are_not_overwritten(self):
        existing = read_json("patches-related-terms/v2.95.36/batch-032-glossary-ledger.json")
        for record in existing["records"]:
            row = self.current[record["term"].casefold()]
            self.assertEqual(row["meaning_vi"], record["meaning_vi_preserved"])

if __name__ == "__main__":
    unittest.main()
