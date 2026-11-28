"""Regression checks for TOEIC vocabulary expansion Batch 028."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

class VocabularyBatch028Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read_json("data/manifest.json")
        cls.batch = read_json("data/vocabulary/batch-028.json")
        cls.canonical = {}
        cls.canonical_letter = {}
        cls.by_word = {}
        for item in cls.manifest["letters"]:
            doc = read_json(item["file"].removeprefix("./"))
            for row in doc["words"]:
                cls.canonical[row["id"]] = row
                cls.canonical_letter[row["id"]] = item["letter"]
                cls.by_word[row["word"].casefold()] = row

    def test_batch_metadata_and_inventory_delta(self):
        self.assertEqual(self.batch["batch"], "028")
        self.assertEqual(self.batch["version"], "2.95.76")
        self.assertEqual(self.batch["count"], 40)
        self.assertEqual(len(self.batch["words"]), 40)
        ids = [row["id"] for row in self.batch["words"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(self.manifest["totalWords"], 1221)
        self.assertEqual(self.manifest["previousReleaseTotalWords"], 1181)
        self.assertEqual(self.manifest["releaseAdditionIds"], ids)
        self.assertEqual(set(self.batch["ipaSummary"]["blankWords"]), {row["word"] for row in self.batch["words"]})
        self.assertEqual(self.batch["ipaSummary"]["populated"], 0)
        self.assertEqual(self.batch["ipaSummary"]["leftBlank"], 40)
        self.assertEqual(self.batch["reciprocalLinksSummary"]["addedReciprocalLinks"], 0)

    def test_every_batch_record_matches_its_canonical_letter_inventory(self):
        for row in self.batch["words"]:
            self.assertIn(row["id"], self.canonical)
            self.assertEqual(self.canonical[row["id"]], row)
            self.assertEqual(row["word"][0].upper(), self.canonical_letter[row["id"]])
            self.assertEqual(row["cefr_level"], row["senses"][0]["cefr_level"])
            self.assertEqual(row["word_family"], [])
            self.assertIsNone(row["verb_forms"])
            self.assertFalse(row["phonetic"].get("us"))
            self.assertGreaterEqual(len(row["collocations"]), 3)
            self.assertTrue(row["examples"][0]["en"].strip())
            self.assertTrue(row["examples"][0]["vi"].strip())
            self.assertEqual(row["examples"][0]["sense_index"], 0)

    def test_new_headwords_are_unique_and_topics_are_canonical(self):
        words = [row["word"].casefold() for row in self.batch["words"]]
        self.assertEqual(len(words), len(set(words)))
        categories = {item["id"] for item in read_json("data/categories.json")["categories"]}
        for row in self.batch["words"]:
            self.assertTrue(row["topics"])
            self.assertTrue(set(row["topics"]).issubset(categories))
            self.assertTrue(all(sense["definition_en"].strip() and sense["meaning_vi"].strip() for sense in row["senses"]))
