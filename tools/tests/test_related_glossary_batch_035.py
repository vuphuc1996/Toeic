"""Regression contract for Cambridge-sourced related-glossary coverage batch 035."""
from __future__ import annotations
import hashlib
import json
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


class RelatedGlossaryBatch035Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json("patches-related-terms/v2.95.42/batch-035-glossary-ledger.json")
        cls.patch = read_json("patches-related-terms/v2.95.42/related-terms-035.json")
        cls.data = read_json("data/related-terms.json")
        cls.current = {row["term"].casefold(): row for row in cls.data["terms"]}

    def test_batch_inventory_and_patch_match(self):
        expected = {"administer", "alert", "alike", "appeal", "article", "assist", "backer", "bargaining"}
        self.assertEqual(self.ledger["batch"], "035")
        self.assertEqual(self.ledger["release"], "2.95.42")
        self.assertEqual(self.ledger["count"], 8)
        self.assertEqual({r["term"] for r in self.ledger["records"]}, expected)
        self.assertEqual({op["term"] for op in self.patch["operations"]}, expected)
        self.assertEqual(self.patch["batchId"], "related-glossary-035-v2.95.42")
        self.assertTrue(all(op["expect"] == {"absent": True} for op in self.patch["operations"]))

    def test_patch_base_hash_reconstructs_pre_batch_file(self):
        added = {record["term"].casefold() for record in self.ledger["records"]}
        # Later additive batches are removed dynamically when reconstructing the
        # historical pre-035 baseline. This keeps the test valid in v2.95.42 too.
        for ledger_path in (ROOT / "patches-related-terms").glob("**/batch-*-glossary-ledger.json"):
            later = json.loads(ledger_path.read_text(encoding="utf-8"))
            if int(later.get("batch", 0)) > 35:
                added.update(record["term"].casefold() for record in later.get("records", []))
        baseline = dict(self.data)
        baseline["terms"] = [row for row in self.data["terms"] if row["term"].casefold() not in added]
        payload = (json.dumps(baseline, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch["baseFileSha256"])

    def test_entries_match_ledger_and_have_exact_cambridge_provenance(self):
        for record in self.ledger["records"]:
            row = self.current[record["term"].casefold()]
            later_values = {}
            for correction_path in (ROOT / "patches-related-terms").glob("**/glossary-corrections-*.json"):
                correction = json.loads(correction_path.read_text(encoding="utf-8"))
                for operation in correction.get("operations", []):
                    if operation["term"].casefold() == record["term"].casefold():
                        later_values.update(operation.get("set", {}))
            for field in ("meaning_vi_preserved", "pos", "definition_en", "source", "sourceUrls"):
                actual_field = "meaning_vi" if field == "meaning_vi_preserved" else field
                expected = later_values.get(actual_field, record[field])
                actual = row.get(actual_field)
                self.assertEqual(actual, expected, record["term"])
            self.assertGreaterEqual(len(row["definition_en"].split()), 5)
            self.assertTrue(row["source"].startswith("Cambridge "), record["term"])
            self.assertEqual(row["sourceUrls"], [f"https://dictionary.cambridge.org/dictionary/english/{record['term']}"])

    def test_batch_terms_are_real_relation_targets_and_not_canonical_headwords(self):
        canonical = set()
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            data = read_json(str(path.relative_to(ROOT)))
            canonical.update(row["word"].casefold() for row in data["words"])
        self.assertTrue(all(record["term"].casefold() not in canonical for record in self.ledger["records"]))
        targets = set()
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            data = read_json(str(path.relative_to(ROOT)))
            for word in data["words"]:
                for sense in word.get("senses", []):
                    for rel in ("synonyms", "antonyms"):
                        targets.update(str(term).strip().casefold() for term in sense.get(rel, []))
        self.assertTrue(all(record["term"].casefold() in targets for record in self.ledger["records"]))

    def test_batch_sources_are_https_cambridge_and_definitions_not_placeholders(self):
        for record in self.ledger["records"]:
            self.assertTrue(record["definition_en"].strip())
            self.assertNotIn("reference gloss", record["definition_en"].casefold())
            self.assertNotIn("placeholder", record["definition_en"].casefold())
            self.assertTrue(record["sourceUrls"])
            for url in record["sourceUrls"]:
                self.assertTrue(url.startswith("https://dictionary.cambridge.org/dictionary/english/"))

if __name__ == "__main__":
    unittest.main()
