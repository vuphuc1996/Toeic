"""Compatibility regression for the historical Cambridge Batch 035 CI module.

This test intentionally reconstructs Batch 035 from the current glossary and
its later patch ledgers. It must not compare against a stale 553-row snapshot
or raw Batch 035 values after Batch 038's reviewed correction to ``article``.
"""
from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from glossary_test_helpers import restore_batch_039

ROOT = Path(__file__).resolve().parents[2]
LEDGER_PATH = "patches-related-terms/v2.95.42/batch-035-glossary-ledger.json"
PATCH_PATH = "patches-related-terms/v2.95.42/related-terms-035.json"
EXPECTED_TERMS = {
    "administer", "alert", "alike", "appeal",
    "article", "assist", "backer", "bargaining",
}


def read_json(relative_path: str):
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


class RelatedGlossaryBatch035CambridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json(LEDGER_PATH)
        cls.patch = read_json(PATCH_PATH)
        cls.data = read_json("data/related-terms.json")
        cls.rows = {row["term"].casefold(): row for row in cls.data["terms"]}
        cls.records = {record["term"].casefold(): record for record in cls.ledger["records"]}
        cls.operations = {operation["term"].casefold(): operation for operation in cls.patch["operations"]}

    def historical_batch_035_state(self):
        """Reconstruct the glossary immediately after Batch 035, before 036–038."""
        restored = restore_batch_039(self.data, ROOT)
        later_terms = set()
        for ledger_path in (ROOT / "patches-related-terms").glob("**/batch-*-glossary-ledger.json"):
            ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
            batch_number = int(ledger.get("batch", 0))
            if 35 < batch_number < 39:
                later_terms.update(record["term"].casefold() for record in ledger.get("records", []))
        restored["terms"] = [row for row in restored["terms"] if row["term"].casefold() not in later_terms]
        return restored

    def test_release_batch_identity_and_expected_inventory(self):
        self.assertEqual(self.ledger["batch"], "035")
        self.assertEqual(self.ledger["release"], "2.95.42")
        self.assertEqual(self.ledger["count"], 8)
        self.assertEqual(set(self.records), EXPECTED_TERMS)
        self.assertEqual(set(self.operations), EXPECTED_TERMS)
        self.assertEqual(self.patch["batchId"], "related-glossary-035-v2.95.42")
        self.assertTrue(all(op["expect"] == {"absent": True} for op in self.patch["operations"]))

        # The historical post-035 inventory is 535. Later additive batches
        # expanded today's glossary; do not freeze the entire current file at 553.
        post_035 = self.historical_batch_035_state()
        self.assertEqual(len(post_035["terms"]), 535)
        normalized = [row["term"].casefold() for row in self.data["terms"]]
        self.assertEqual(len(normalized), len(set(normalized)), "current glossary must not contain duplicate normalized terms")
        self.assertGreaterEqual(len(normalized), len(post_035["terms"]))
        self.assertTrue(set(self.records).issubset(self.rows))

    def test_every_added_term_has_sourced_fields_and_matching_ledger(self):
        correction_sets = {}
        for correction_path in sorted((ROOT / "patches-related-terms").glob("**/glossary-corrections-*.json")):
            correction = json.loads(correction_path.read_text(encoding="utf-8"))
            for operation in correction.get("operations", []):
                correction_sets.setdefault(operation["term"].casefold(), {}).update(operation.get("set", {}))

        for key, record in self.records.items():
            operation = self.operations[key]
            historical_row = {
                "term": record["term"],
                "meaning_vi": record["meaning_vi_preserved"],
                "pos": record["pos"],
                "definition_en": record["definition_en"],
                "source": record["source"],
                "sourceUrls": record["sourceUrls"],
            }
            self.assertEqual(operation["new"], historical_row, key)
            expected_current = {**historical_row, **correction_sets.get(key, {})}
            actual = self.rows[key]
            self.assertEqual(actual, expected_current, key)
            self.assertGreaterEqual(len(actual["definition_en"].split()), 5, key)
            self.assertTrue(actual["source"].startswith("Cambridge "), key)
            self.assertEqual(actual["sourceUrls"], [f"https://dictionary.cambridge.org/dictionary/english/{key}"])

    def test_each_term_remains_linked_from_its_original_canonical_source(self):
        canonical = set()
        relation_targets = set()
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            document = read_json(str(path.relative_to(ROOT)))
            for word in document["words"]:
                canonical.add(word["word"].casefold())
                for sense in word.get("senses", []):
                    for relation in ("synonyms", "antonyms"):
                        relation_targets.update(str(term).strip().casefold() for term in sense.get(relation, []))
        for term in EXPECTED_TERMS:
            self.assertNotIn(term, canonical, term)
            self.assertIn(term, relation_targets, term)
            self.assertIn(term, self.rows, term)

    def test_patch_reconstructs_exact_pre_batch_file_hash(self):
        restored = restore_batch_039(self.data, ROOT)
        remove_terms = set(EXPECTED_TERMS)
        for ledger_path in (ROOT / "patches-related-terms").glob("**/batch-*-glossary-ledger.json"):
            later = json.loads(ledger_path.read_text(encoding="utf-8"))
            batch_number = int(later.get("batch", 0))
            if 35 < batch_number < 39:
                remove_terms.update(record["term"].casefold() for record in later.get("records", []))
        baseline = dict(restored)
        baseline["terms"] = [row for row in restored["terms"] if row["term"].casefold() not in remove_terms]
        payload = (json.dumps(baseline, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch["baseFileSha256"])

    def test_batch_increased_coverage_without_rewriting_relationships(self):
        post_035 = self.historical_batch_035_state()
        before_count = len(post_035["terms"]) - len(EXPECTED_TERMS)
        after_count = len(post_035["terms"])
        self.assertEqual((before_count, after_count), (527, 535))
        self.assertEqual(after_count - before_count, self.ledger["count"])
        self.assertTrue(all(operation["expect"] == {"absent": True} for operation in self.patch["operations"]))
        self.assertEqual(set(self.records), set(self.operations))


if __name__ == "__main__":
    unittest.main()
