"""Regression contract for Related Glossary Batch 043 (v2.95.62)."""
from __future__ import annotations
import copy
import hashlib
import json
import re
import unittest
from glossary_test_helpers import restore_batch_044
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / "patches-related-terms/v2.95.62/related-terms-043.json"
LEDGER_PATH = ROOT / "patches-related-terms/v2.95.62/batch-043-glossary-ledger.json"
EXPECTED = {
    "apparatus": ("n", "equipment", "synonym"),
    "approximation": ("n", "estimate", "synonym"),
    "arrive": ("v", "depart", "antonym"),
    "assurance": ("n", "guarantee", "synonym"),
    "attempt": ("n", "effort", "synonym"),
    "buy": ("v", "purchase", "synonym"),
    "calendar month": ("n", "month", "synonym"),
    "chance": ("n", "opportunity", "synonym"),
    "cautious": ("adj", "careful", "synonym"),
    "coaching": ("n", "training", "synonym"),
    "collaborator": ("n", "partner", "synonym"),
    "commerce": ("n", "trade", "synonym"),
    "coworker": ("n", "colleague", "synonym"),
    "criterion": ("n", "standard", "synonym"),
    "danger": ("n", "risk", "synonym"),
    "distinctive": ("adj", "unique", "synonym"),
    "edition": ("n", "version", "synonym"),
    "endeavor": ("n/v", "effort", "synonym"),
    "evade": ("v", "avoid", "synonym"),
    "financial institution": ("n", "bank", "synonym"),
    "convention": ("n", "conference", "synonym"),
}
ALLOWED_FIELDS = {"pos", "definition_en", "source", "sourceUrls", "sourceRelease"}
PLACEHOLDER = "Reference gloss for practice distractors."


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class RelatedGlossaryBatch043Tests(unittest.TestCase):
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
        self.assertEqual(self.patch["batchId"], "related-glossary-043-v2.95.62")
        self.assertEqual(self.ledger["batch"], "043")
        self.assertEqual(self.ledger["release"], "2.95.62")
        self.assertEqual(self.ledger["predecessorRelease"], "2.95.61")
        self.assertEqual(self.ledger["count"], len(EXPECTED))
        self.assertEqual({row["term"].casefold() for row in self.ledger["records"]}, set(EXPECTED))
        self.assertEqual({op["term"].casefold() for op in self.patch["operations"]}, set(EXPECTED))
        for term, (_, anchor, relation_type) in EXPECTED.items():
            self.assertIn(term, self.rows)
            self.assertNotIn(term, self.headwords, f"{term} must remain relation-only")
            self.assertIn((anchor, relation_type), {(h.casefold(), kind) for h, kind in self.targets[term]})

    def test_definitions_pos_and_cambridge_provenance_are_complete(self):
        self.assertEqual(self.ledger["sourcePublisher"], "Cambridge University Press")
        for term, (pos, _anchor, _kind) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row["pos"], pos, term)
            self.assertTrue(row["definition_en"].strip(), term)
            self.assertNotEqual(row["definition_en"], PLACEHOLDER, term)
            self.assertNotRegex(row["definition_en"], r"(?i)placeholder|reference gloss|todo|tbd|definition pending")
            self.assertTrue(row["source"].startswith("Cambridge Dictionary"), term)
            self.assertEqual(row["sourceRelease"], "2.95.62")
            self.assertEqual(row["sourceUrls"], [f"https://dictionary.cambridge.org/dictionary/english/{term.replace(' ', '-')}"])
            self.assertIn("independent editorial review pending", row["source"].lower())

    def test_exact_guards_reconstruct_predecessor_glossary(self):
        restored = restore_batch_044(self.glossary, ROOT)
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

    def test_updates_are_limited_to_approved_glossary_metadata(self):
        for operation in self.patch["operations"]:
            self.assertEqual(set(operation["set"]), ALLOWED_FIELDS)
            self.assertEqual(operation["set"]["pos"], EXPECTED[operation["term"].casefold()][0])
            self.assertEqual(operation["expect"].get("term", "").casefold(), operation["term"].casefold())
        self.assertEqual(len(self.rows), 567)

    def test_meanings_and_relation_graph_are_unchanged(self):
        ledger = {row["term"].casefold(): row for row in self.ledger["records"]}
        for term, (_pos, anchor, relation_type) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row["meaning_vi"], ledger[term]["meaning_vi_preserved"], term)
            self.assertIn((anchor, relation_type), {(h.casefold(), kind) for h, kind in self.targets[term]})
            self.assertEqual(ledger[term]["relationAnchors"], [
                {"headword": headword, "type": kind}
                for headword, kind in sorted(self.targets[term], key=lambda x:(x[0].casefold(),x[1]))
            ])

    def test_ledger_explicitly_marks_source_review_method_and_editorial_gate(self):
        self.assertIn("indexed dictionary entry excerpts", self.ledger["sourceReviewMethod"])
        self.assertIn("Direct page fetch status was not asserted", self.ledger["sourceReviewMethod"])
        for record in self.ledger["records"]:
            self.assertEqual(record["editorialStatus"], "independent-editorial-review-pending")
            self.assertEqual(record["sourcePublisher"], "Cambridge University Press")
            self.assertTrue(record["sourceUrl"].startswith("https://dictionary.cambridge.org/dictionary/english/"))


if __name__ == "__main__":
    unittest.main()
