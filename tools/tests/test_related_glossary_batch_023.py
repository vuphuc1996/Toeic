"""Regression checks for the v2.95.17 related-term glossary backfill."""
from __future__ import annotations
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class RelatedGlossaryBatch023Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = read_json("data/manifest.json")
        cls.words = []
        for item in manifest["letters"]:
            cls.words.extend(read_json(item["file"].removeprefix("./"))["words"])
        cls.related_doc = read_json("data/related-terms.json")
        cls.related = {row["term"].casefold(): row for row in cls.related_doc["terms"]}
        cls.batch = read_json("data/vocabulary/batch-023.json")
        cls.patch = read_json("patches-related-terms/v2.95.17/related-terms-001.json")

    def test_batch_metadata_matches_release(self):
        self.assertEqual(self.batch["batch"], "023")
        self.assertEqual(self.batch["release"], "2.95.17")
        self.assertEqual(self.batch["count"], 9)
        self.assertEqual(
            [row["term"] for row in self.batch["records"]],
            ["choose", "distribution", "effect", "estimate", "former", "inform", "origin", "possibility", "responsibility"],
        )
        self.assertIn("independent lexical review pending", self.batch["editorialStatus"])

    def test_patch_is_absent_only_and_matches_provenance_ledger(self):
        self.assertEqual(self.patch["batchId"], "v2.95.17-related-glossary-001")
        self.assertEqual(len(self.patch["operations"]), 9)
        ledger = {row["term"].casefold(): row for row in self.batch["records"]}
        for operation in self.patch["operations"]:
            self.assertEqual(operation["expect"], {"absent": True})
            self.assertEqual(operation["new"], ledger[operation["term"].casefold()])

    def test_every_new_gloss_is_present_and_cambridge_sourced(self):
        for entry in self.batch["records"]:
            current = self.related[entry["term"].casefold()]
            for key, value in entry.items():
                self.assertEqual(current.get(key), value, entry["term"])
            self.assertTrue(entry["meaning_vi"].strip())
            self.assertTrue(entry["definition_en"].strip())
            self.assertTrue(entry["sourceUrls"])
            self.assertTrue(all(
                url.startswith("https://dictionary.cambridge.org/dictionary/english/")
                for url in entry["sourceUrls"]
            ))

    def test_each_gloss_is_used_by_existing_synonym_or_antonym_fields(self):
        referenced = set()
        for word in self.words:
            for sense in word.get("senses", []):
                for field in ("synonyms", "antonyms"):
                    referenced.update(term.casefold() for term in (sense.get(field) or []))
        for entry in self.batch["records"]:
            self.assertIn(entry["term"].casefold(), referenced, entry["term"])

    def test_pos_labels_match_referenced_senses(self):
        expected = {
            "choose": "v", "distribution": "n", "effect": "n/v", "estimate": "n/v",
            "former": "adj", "inform": "v", "origin": "n", "possibility": "n",
            "responsibility": "n",
        }
        actual = {row["term"].casefold(): row["pos"] for row in self.batch["records"]}
        self.assertEqual(actual, expected)

    def test_terms_meet_repeated_reference_threshold(self):
        frequency = Counter()
        for word in self.words:
            for sense in word.get("senses", []):
                for field in ("synonyms", "antonyms"):
                    frequency.update(term.casefold() for term in (sense.get(field) or []))
        for entry in self.batch["records"]:
            self.assertGreaterEqual(frequency[entry["term"].casefold()], 2, entry["term"])
            self.assertEqual(frequency[entry["term"].casefold()], 2, entry["term"])

    def test_glossary_has_no_duplicate_casefolded_terms(self):
        keys = [row["term"].casefold() for row in self.related_doc["terms"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertGreaterEqual(len(self.related_doc["terms"]), 396)

    def test_canonical_vocabulary_headword_and_relationship_counts_are_preserved(self):
        self.assertEqual(len(self.words), 1181)
        for word in self.words:
            for sense in word.get("senses", []):
                for field in ("synonyms", "antonyms"):
                    self.assertTrue(all(isinstance(term, str) for term in (sense.get(field) or [])))

    def test_ci_registers_the_batch_test(self):
        workflow = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
        expected_command = "python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_023.py' -v"
        self.assertIn(expected_command, workflow)
        self.assertIn("Unit tests — related glossary batch 023", workflow)


if __name__ == "__main__":
    unittest.main()
