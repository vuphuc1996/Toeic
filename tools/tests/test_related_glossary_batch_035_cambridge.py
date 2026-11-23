"""Regression and provenance checks for Cambridge-sourced Related Glossary Batch 035."""
from __future__ import annotations
import copy
import hashlib
import json
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data/related-terms.json"
PATCH_PATH = ROOT / "patches-related-terms/v2.95.43/related-terms-035.json"
LEDGER_PATH = ROOT / "patches-related-terms/v2.95.43/batch-035-glossary-ledger.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class RelatedGlossaryBatch035Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_json(DATA_PATH)
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.rows = {row["term"].casefold(): row for row in cls.data["terms"]}
        cls.operations = {row["term"].casefold(): row for row in cls.patch["operations"]}
        cls.ledger_rows = {row["term"].casefold(): row for row in cls.ledger["records"]}

    def test_release_batch_identity_and_expected_inventory(self):
        self.assertEqual(self.ledger["batch"], "035")
        self.assertEqual(self.ledger["release"], "2.95.43")
        self.assertEqual(self.ledger["count"], 26)
        self.assertEqual(self.patch["batchId"], "related-glossary-035-v2.95.43")
        self.assertEqual(len(self.patch["operations"]), 26)
        self.assertEqual(len(self.rows), 553)
        self.assertEqual(len(set(self.rows)), 553)
        self.assertEqual(set(self.operations), set(self.ledger_rows))

    def test_every_added_term_has_sourced_fields_and_matching_ledger(self):
        for key, operation in self.operations.items():
            row = self.rows[key]
            ledger = self.ledger_rows[key]
            self.assertEqual(operation["expect"], {"absent": True})
            self.assertEqual(row, operation["new"])
            self.assertEqual(row["meaning_vi"], ledger["meaning_vi_added"])
            self.assertEqual(row["pos"], ledger["pos"])
            self.assertEqual(row["definition_en"], ledger["definition_en"])
            self.assertTrue(row["definition_en"].strip())
            self.assertIn("Cambridge Dictionary", row["source"])
            self.assertEqual(row["sourceUrls"], ledger["sourceUrls"])
            self.assertTrue(ledger["sourceHeadword"])
            self.assertEqual(ledger["relationType"], "synonym")
            for url in row["sourceUrls"]:
                parsed = urlsplit(url)
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.hostname, "dictionary.cambridge.org")
                self.assertTrue(parsed.path.startswith("/dictionary/english/"))

    def test_each_term_remains_linked_from_its_original_canonical_source(self):
        vocabulary = {}
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            source = read_json(path)
            for word in source.get("words", []):
                vocabulary[word["word"].casefold()] = word
        for key, record in self.ledger_rows.items():
            source = vocabulary[record["sourceHeadword"].casefold()]
            matches = [
                related.casefold()
                for sense in source.get("senses", [])
                for related in sense.get("synonyms", [])
            ]
            self.assertIn(key, matches, f"{record['term']} no longer has its canonical synonym source")

    def test_patch_reconstructs_exact_pre_batch_file_hash(self):
        reconstructed = copy.deepcopy(self.data)
        remove = set(self.operations)
        reconstructed["terms"] = [
            row for row in reconstructed["terms"]
            if row["term"].casefold() not in remove
        ]
        reconstructed["terms"].sort(key=lambda row: row["term"].casefold())
        raw = (json.dumps(reconstructed, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(raw).hexdigest(), self.patch["baseFileSha256"])

    def test_batch_increased_coverage_without_rewriting_relationships(self):
        self.assertEqual(self.ledger["baselineMetrics"]["entries"], 527)
        self.assertEqual(self.ledger["expectedAfterApply"]["entries"], 553)
        self.assertEqual(self.ledger["baselineMetrics"]["coveredUniqueTerms"], 516)
        self.assertEqual(self.ledger["expectedAfterApply"]["coveredUniqueTerms"], 542)
        self.assertEqual(self.ledger["expectedAfterApply"]["unglossedUniqueTerms"], 262)
        self.assertEqual(self.ledger["expectedAfterApply"]["coveragePercent"], 67.4)
        self.assertEqual(self.ledger["expectedAfterApply"]["referencedUniqueTerms"], 804)


if __name__ == "__main__":
    unittest.main()
