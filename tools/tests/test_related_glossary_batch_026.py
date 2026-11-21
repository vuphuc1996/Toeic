"""Regression tests for related-term glossary Batch 026."""
from __future__ import annotations
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

class RelatedGlossaryBatch026Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batch = read_json("patches-related-terms/v2.95.20/batch-026-glossary-ledger.json")
        cls.patch = read_json("patches-related-terms/v2.95.20/related-terms-026.json")
        cls.related = read_json("data/related-terms.json")
        cls.terms = {row["term"].casefold(): row for row in cls.related["terms"]}
        cls.words = []
        manifest = read_json("data/manifest.json")
        for letter in manifest["letters"]:
            cls.words.extend(read_json(letter["file"].removeprefix("./"))["words"])

    def test_batch_metadata_and_terms(self):
        self.assertEqual(self.batch["batch"], "026")
        self.assertEqual(self.batch["release"], "2.95.20")
        self.assertEqual(self.batch["count"], 4)
        self.assertEqual({row["term"] for row in self.batch["records"]}, {"method", "consume", "function", "launch"})


    def test_patch_is_absent_only_and_matches_ledger(self):
        ledger = {row["term"].casefold(): row for row in self.batch["records"]}
        self.assertEqual(len(self.patch["operations"]), 4)
        for operation in self.patch["operations"]:
            self.assertEqual(operation["expect"], {"absent": True})
            self.assertEqual(operation["new"], ledger[operation["term"].casefold()])

    def test_glosses_exist_with_cambridge_source(self):
        for row in self.batch["records"]:
            current = self.terms[row["term"].casefold()]
            for key, value in row.items():
                self.assertEqual(current.get(key), value, row["term"])
            self.assertTrue(row["meaning_vi"])
            self.assertTrue(row["definition_en"])
            self.assertTrue(row["sourceUrls"])
            self.assertTrue(all(url.startswith("https://dictionary.cambridge.org/dictionary/english/") for url in row["sourceUrls"]))

    def test_terms_are_referenced_in_synonym_or_antonym_fields(self):
        frequency = Counter()
        for word in self.words:
            for sense in word.get("senses", []):
                for field in ("synonyms", "antonyms"):
                    frequency.update(term.casefold() for term in (sense.get(field) or []))
        for row in self.batch["records"]:
            self.assertGreater(frequency[row["term"].casefold()], 0, row["term"])

    def test_glossary_casefold_uniqueness(self):
        keys = [row["term"].casefold() for row in self.related["terms"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertGreaterEqual(len(keys), 400)

if __name__ == "__main__":
    unittest.main()
