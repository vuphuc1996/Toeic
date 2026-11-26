"""Regression contract for Cambridge-sourced Related Glossary Batch 044."""
from __future__ import annotations
import copy
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / "patches-related-terms/v2.95.69/related-terms-044.json"
LEDGER_PATH = ROOT / "patches-related-terms/v2.95.69/batch-044-glossary-ledger.json"
EXPECTED = {
    "products": ("n", {("goods", "synonym"), ("merchandise", "synonym")}),
    "get": ("v", {("obtain", "synonym"), ("receive", "synonym")}),
    "area": ("n", {("zone", "synonym")}),
    "attentive": ("adj", {("careful", "synonym")}),
    "alternative": ("n", {("option", "synonym")}),
    "connect": ("v", {("join", "synonym")}),
    "constantly": ("adv", {("always", "synonym")}),
    "continually": ("adv", {("always", "synonym")}),
    "conveyance": ("n", {("vehicle", "synonym")}),
    "courtyard": ("n", {("yard", "synonym")}),
    "depot": ("n", {("warehouse", "synonym")}),
    "diary": ("n", {("journal", "synonym")}),
    "check": ("n/v", {("inspect", "synonym")}),
    "disadvantage": ("n", {("benefit", "antonym")}),
    "notification": ("n", {("notice", "synonym")}),
}
ALLOWED_FIELDS = {"pos", "definition_en", "source", "sourceUrls", "sourceRelease"}

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

class RelatedGlossaryBatch044Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.glossary = read_json(ROOT / "data/related-terms.json")
        cls.rows = {row["term"].casefold(): row for row in cls.glossary["terms"]}
        cls.targets = {}
        cls.headwords = set()
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            for word in read_json(path)["words"]:
                cls.headwords.add(word["word"].casefold())
                for sense in word.get("senses", []):
                    for field in ("synonyms", "antonyms"):
                        for target in sense.get(field, []) or []:
                            cls.targets.setdefault(str(target).strip().casefold(), set()).add(
                                (word["word"], "synonym" if field == "synonyms" else "antonym")
                            )

    def test_exact_inventory_and_existing_relation_anchors(self):
        self.assertEqual(self.patch["batchId"], "related-glossary-044-v2.95.69")
        self.assertEqual(self.ledger["batch"], "044")
        self.assertEqual(self.ledger["release"], "2.95.69")
        self.assertEqual(self.ledger["predecessorRelease"], "2.95.68")
        self.assertEqual(self.ledger["count"], len(EXPECTED))
        self.assertEqual({row["term"].casefold() for row in self.ledger["records"]}, set(EXPECTED))
        self.assertEqual({row["term"].casefold() for row in self.patch["operations"]}, set(EXPECTED))
        for term, (_pos, expected_edges) in EXPECTED.items():
            self.assertNotIn(term, self.headwords, term)
            actual = {(head.casefold(), kind) for head, kind in self.targets.get(term, set())}
            self.assertTrue(expected_edges.issubset(actual), (term, expected_edges, actual))

    def test_definitions_pos_and_provenance_are_complete(self):
        for term, (pos, _edges) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row["pos"], pos, term)
            self.assertGreaterEqual(len(row["definition_en"].split()), 5, term)
            self.assertNotRegex(row["definition_en"], r"(?i)placeholder|reference gloss|todo|tbd|definition pending")
            self.assertTrue(row["source"].startswith("Cambridge Dictionary"), term)
            self.assertEqual(row["sourceRelease"], "2.95.69")
            self.assertEqual(len(row["sourceUrls"]), 1)
            self.assertTrue(row["sourceUrls"][0].startswith("https://dictionary.cambridge.org/dictionary/english/"))
            self.assertIn("independent editorial review pending", row["source"].lower())

    def test_patch_guards_reconstruct_exact_predecessor_glossary(self):
        restored = copy.deepcopy(self.glossary)
        by = {row["term"].casefold(): row for row in restored["terms"]}
        for operation in self.patch["operations"]:
            row = by[operation["term"].casefold()]
            self.assertEqual(row["term"].casefold(), operation["expect"]["term"].casefold())
            for field, old_value in operation["expect"].items():
                if field == "term":
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch["baseFileSha256"])
        self.assertEqual(self.ledger["baseRelatedTermsSha256"], self.patch["baseFileSha256"])
        for operation in self.patch["operations"]:
            self.assertEqual(set(operation["set"]), ALLOWED_FIELDS)
            self.assertEqual(set(operation["expect"]), ALLOWED_FIELDS | {"term", "meaning_vi"})

    def test_vietnamese_meanings_and_relation_graph_are_unchanged(self):
        ledger = {record["term"].casefold(): record for record in self.ledger["records"]}
        for term, (_pos, expected_edges) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row["meaning_vi"], ledger[term]["meaning_vi_preserved"], term)
            actual = {(head.casefold(), kind) for head, kind in self.targets[term]}
            self.assertTrue(expected_edges.issubset(actual), term)
            expected_ledger = {(edge["headword"].casefold(), edge["type"]) for edge in ledger[term]["relationAnchors"]}
            self.assertEqual(actual, expected_ledger, term)
        self.assertEqual(len(self.rows), 567)

    def test_source_method_and_editorial_gate_are_explicit(self):
        self.assertIn("web-indexed entry excerpts", self.ledger["sourceReviewMethod"])
        self.assertIn("Direct page fetch was not consistently available", self.ledger["sourceReviewMethod"])
        for record in self.ledger["records"]:
            self.assertEqual(record["editorialStatus"], "independent-editorial-review-pending")
            self.assertEqual(record["sourcePublisher"], "Cambridge University Press")
            self.assertTrue(record["sourceUrl"].startswith("https://dictionary.cambridge.org/dictionary/english/"))

if __name__ == "__main__":
    unittest.main()
