"""Regression contract for Cambridge-sourced Related Glossary Batch 045."""
from __future__ import annotations
import copy
import hashlib
import json
import re
import unittest
from pathlib import Path
from glossary_test_helpers import restore_batch_045

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / "patches-related-terms/v2.95.71/related-terms-045.json"
LEDGER_PATH = ROOT / "patches-related-terms/v2.95.71/batch-045-glossary-ledger.json"
EXPECTED_TERMS = {
    "drawback", "due date", "employ", "housing", "installation", "leaflet",
    "output", "permanent", "purchaser", "progress report", "funds", "objection",
    "distinction", "modify", "global", "inflexible", "incapable", "specialist",
    "tendency", "nonurgent", "dismiss", "equilibrium", "initiate",
}
ALLOWED_FIELDS = {"pos", "definition_en", "source", "sourceUrls", "sourceRelease"}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class RelatedGlossaryBatch045Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.glossary = read_json(ROOT / "data/related-terms.json")
        cls.rows = {row["term"].casefold(): row for row in cls.glossary["terms"]}
        # Reconstruct the v2.95.71 canonical headword set: Batch 028 was added
        # later and must not retroactively invalidate Batch 045 relation-target status.
        batch_028 = read_json(ROOT / "data/vocabulary/batch-028.json")
        later_headwords = {row["word"].casefold() for row in batch_028["words"]}
        cls.headwords = set()
        cls.targets = {}
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            for word in read_json(path)["words"]:
                if word["word"].casefold() not in later_headwords:
                    cls.headwords.add(word["word"].casefold())
                for sense in word.get("senses", []):
                    for field in ("synonyms", "antonyms"):
                        for target in sense.get(field, []) or []:
                            cls.targets.setdefault(str(target).strip().casefold(), set()).add(
                                (word["word"], "synonym" if field == "synonyms" else "antonym")
                            )

    def test_release_inventory_and_guarded_fields(self):
        self.assertEqual(self.patch["batchId"], "related-glossary-045-v2.95.71")
        self.assertEqual(self.ledger["batch"], "045")
        self.assertEqual(self.ledger["release"], "2.95.71")
        self.assertEqual(self.ledger["predecessorRelease"], "2.95.70")
        self.assertEqual(self.ledger["count"], 23)
        self.assertEqual({x["term"].casefold() for x in self.patch["operations"]}, EXPECTED_TERMS)
        self.assertEqual({x["term"].casefold() for x in self.ledger["records"]}, EXPECTED_TERMS)
        for op in self.patch["operations"]:
            self.assertEqual(set(op["set"]), ALLOWED_FIELDS)
            self.assertEqual(set(op["expect"]), ALLOWED_FIELDS | {"term", "meaning_vi"})

    def test_existing_targets_only_with_canonical_relation_anchor(self):
        ledger = {x["term"].casefold(): x for x in self.ledger["records"]}
        for term in EXPECTED_TERMS:
            self.assertIn(term, self.rows)
            self.assertNotIn(term, self.headwords)
            anchors = {(x["headword"].casefold(), x["type"]) for x in ledger[term]["relationAnchors"]}
            actual = {(h.casefold(), kind) for h, kind in self.targets.get(term, set())}
            self.assertTrue(anchors)
            self.assertEqual(actual, anchors, term)

    def test_definitions_pos_and_cambridge_provenance(self):
        for term in EXPECTED_TERMS:
            row = self.rows[term]
            self.assertIn(row.get("pos"), {"n", "n pl", "v", "adj", "adv", "n/v"}, term)
            definition = row.get("definition_en", "")
            self.assertGreaterEqual(len(definition.split()), 5, term)
            self.assertNotRegex(definition, re.compile(r"placeholder|reference gloss|todo|tbd|definition pending", re.I))
            self.assertTrue(str(row.get("source", "")).startswith("Cambridge Dictionary"), term)
            self.assertEqual(row.get("sourceRelease"), "2.95.71")
            urls = row.get("sourceUrls", [])
            self.assertEqual(len(urls), 1)
            self.assertRegex(urls[0], r"^https://dictionary\.cambridge\.org/dictionary/english/")
            self.assertIn("independent editorial review pending", row["source"].lower())

    def test_historical_reconstruction_matches_v270_base_hash(self):
        restored = restore_batch_045(self.glossary, ROOT)
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        reconstructed = hashlib.sha256(payload).hexdigest()
        self.assertEqual(reconstructed, self.patch["baseFileSha256"])
        self.assertEqual(reconstructed, self.ledger["baseRelatedTermsSha256"])

    def test_vietnamese_meaning_and_relation_graph_are_unchanged(self):
        ledger = {x["term"].casefold(): x for x in self.ledger["records"]}
        restored = restore_batch_045(self.glossary, ROOT)
        restored_rows = {x["term"].casefold(): x for x in restored["terms"]}
        for term in EXPECTED_TERMS:
            row = self.rows[term]
            self.assertEqual(row["meaning_vi"], ledger[term]["meaning_vi_preserved"])
            self.assertEqual(row["meaning_vi"], restored_rows[term]["meaning_vi"])
            anchors = {(x["headword"].casefold(), x["type"]) for x in ledger[term]["relationAnchors"]}
            self.assertEqual({(h.casefold(), kind) for h, kind in self.targets[term]}, anchors)
        self.assertEqual(len(self.rows), 567)

    def test_research_method_and_editorial_gate_are_explicit(self):
        self.assertIn("web-indexed entry excerpts", self.ledger["sourceReviewMethod"])
        self.assertIn("Direct page fetch was not consistently available", self.ledger["sourceReviewMethod"])
        for record in self.ledger["records"]:
            self.assertEqual(record["editorialStatus"], "independent-editorial-review-pending")
            self.assertEqual(record["sourcePublisher"], "Cambridge University Press")
            self.assertTrue(record["sourceUrl"].startswith("https://dictionary.cambridge.org/dictionary/english/"))


if __name__ == "__main__":
    unittest.main()
