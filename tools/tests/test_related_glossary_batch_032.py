"""Regression coverage for Cambridge-sourced glossary remediation Batch 032."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

class RelatedGlossaryBatch032Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json("patches-related-terms/v2.95.36/batch-032-glossary-ledger.json")
        cls.data = read_json("data/related-terms.json")
        cls.current = {row["term"].casefold(): row for row in cls.data["terms"]}


    def test_batch_has_six_named_recoveries(self):
        self.assertEqual(self.ledger["batch"], "032")
        self.assertEqual(self.ledger["release"], "2.95.36")
        self.assertEqual(self.ledger["count"], 6)
        self.assertEqual({r["term"] for r in self.ledger["records"]},
                       {"account", "acknowledgment", "acquire", "adaptable", "advance", "advantage"})


    def test_each_entry_has_definition_pos_source_and_urls(self):
        for record in self.ledger["records"]:
            row = self.current[record["term"].casefold()]
            for field in ("pos", "definition_en", "source", "sourceUrls"):
                self.assertEqual(row.get(field), record[field], record["term"])
            self.assertTrue(row["definition_en"].strip())
            self.assertTrue(row["pos"].strip())
            self.assertTrue(row["source"].strip())
            self.assertTrue(row["sourceUrls"])
            self.assertTrue(all(url.startswith("https://") for url in row["sourceUrls"]))


    def test_vietnamese_meanings_are_preserved(self):
        for record in self.ledger["records"]:
            self.assertEqual(self.current[record["term"].casefold()]["meaning_vi"], record["meaning_vi_preserved"])


    def test_no_placeholder_definitions_in_batch(self):
        for record in self.ledger["records"]:
            self.assertNotIn("reference gloss", record["definition_en"].casefold())
            self.assertNotIn("todo", record["definition_en"].casefold())

if __name__ == "__main__":
    unittest.main()
