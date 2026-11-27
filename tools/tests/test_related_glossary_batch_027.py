"""Regression tests for related-term glossary Batch 027."""
from __future__ import annotations
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_TERMS = {
    "activity", "answer", "carry out", "combination", "common", "continue",
    "decrease", "employee", "funding", "goal", "inaction", "make", "minor",
    "objective", "oppose", "send", "study", "support", "work",
    "maximum", "different", "determine", "approach",
}

def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

class RelatedGlossaryBatch027Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batch = read_json("patches-related-terms/v2.95.21/batch-027-glossary-ledger.json")
        cls.patch = read_json("patches-related-terms/v2.95.21/related-terms-027.json")
        cls.related = read_json("data/related-terms.json")
        cls.terms = {row["term"].casefold(): row for row in cls.related["terms"]}
        cls.words = []
        manifest = read_json("data/manifest.json")
        for letter in manifest["letters"]:
            cls.words.extend(read_json(letter["file"].removeprefix("./"))["words"])
        cls.frequency = Counter(
            term.casefold()
            for word in cls.words
            for sense in word.get("senses", [])
            for field in ("synonyms", "antonyms")
            for term in (sense.get(field) or [])
        )

    def test_batch_metadata_and_priority_selection(self):
        self.assertEqual(self.batch["batch"], "027")
        self.assertEqual(self.batch["release"], "2.95.21")
        self.assertEqual(self.batch["count"], 23)
        self.assertEqual({row["term"] for row in self.batch["records"]}, EXPECTED_TERMS)
        self.assertTrue(all(self.frequency[row["term"].casefold()] == 2 for row in self.batch["records"]))

    def test_patch_is_absent_only_and_matches_provenance_ledger(self):
        ledger = {row["term"].casefold(): row for row in self.batch["records"]}
        self.assertEqual(len(self.patch["operations"]), 23)
        for operation in self.patch["operations"]:
            self.assertEqual(operation["expect"], {"absent": True})
            self.assertEqual(operation["new"], ledger[operation["term"].casefold()])

    def test_all_glosses_are_present_and_have_cambridge_sources(self):
        for row in self.batch["records"]:
            current = self.terms[row["term"].casefold()]
            for key, value in row.items():
                self.assertEqual(current.get(key), value, row["term"])
            self.assertTrue(row["meaning_vi"])
            self.assertTrue(row["definition_en"])
            self.assertEqual(row["source"], "Cambridge Dictionary")
            self.assertTrue(row["sourceUrls"])
            for url in row["sourceUrls"]:
                self.assertTrue(url.startswith("https://dictionary.cambridge.org/dictionary/english/"), url)

    def test_relationship_graph_is_unchanged_and_terms_are_referenced(self):
        for row in self.batch["records"]:
            self.assertEqual(self.frequency[row["term"].casefold()], 2, row["term"])
        baseline = read_json("tools/baseline-ids.json")
        baseline_ids = set(baseline["ids"])
        current_ids = {word["id"] for word in self.words}
        self.assertEqual(len(baseline_ids), baseline["count"])
        self.assertTrue(baseline_ids.issubset(current_ids), "A protected canonical vocabulary ID is missing")
        self.assertEqual(len(current_ids), len(self.words))

    def test_glossary_and_exact_reference_coverage(self):
        keys = [row["term"].casefold() for row in self.related["terms"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertGreaterEqual(len(keys), 519)
        covered = len(set(self.frequency) & set(keys))
        covered_occurrences = sum(count for term, count in self.frequency.items() if term in set(keys))
        backlog = read_json("docs/reports/related-glossary-backlog.json")
        self.assertEqual(len(keys), backlog["glossaryCount"])
        self.assertEqual(covered + backlog["uniqueUnglossedTerms"], len(self.frequency))
        self.assertEqual(sum(self.frequency.values()) - covered_occurrences, backlog["uncoveredReferenceCount"])

if __name__ == "__main__":
    unittest.main()
