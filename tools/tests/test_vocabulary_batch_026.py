"""Structural, IPA, provenance, and Word Family regression tests for Batch 026 (v2.95.72)."""
from __future__ import annotations
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from cmudict_ipa import arpabet_to_ipa

wf_spec = importlib.util.spec_from_file_location("wf_audit", ROOT / "tools/audit-word-family-graph.py")
wf_mod = importlib.util.module_from_spec(wf_spec)
assert wf_spec.loader is not None
wf_spec.loader.exec_module(wf_mod)


def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


class VocabularyBatch026Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read_json("data/manifest.json")
        cls.batch = read_json("data/vocabulary/batch-026.json")
        cls.cmu_ledger = read_json("tools/vocabulary-batch-026-cmudict-v2.95.72.json")
        cls.patch = read_json("patches/v2.95.72/batch-001-word-family-expansion.json")
        cls.records = {}
        cls.by_word = {}
        for item in cls.manifest["letters"]:
            data = read_json(item["file"].removeprefix("./"))
            for row in data["words"]:
                cls.records[row["id"]] = row
                cls.by_word[row["word"].casefold()] = row

    def test_batch_metadata_and_release_delta(self):
        self.assertEqual(self.batch["batch"], "026")
        self.assertEqual(self.batch["version"], "2.95.72")
        self.assertEqual(self.batch["count"], 40)
        self.assertEqual(len(self.batch["words"]), 40)
        self.assertEqual(self.manifest["totalWords"], 1181)
        self.assertEqual(self.manifest["previousReleaseTotalWords"], 1141)
        batch_ids = [w["id"] for w in self.batch["words"]]
        self.assertEqual(self.manifest["releaseAdditionIds"], batch_ids)
        self.assertEqual(self.patch["count"], 40)
        self.assertEqual([r["id"] for r in self.patch["records"]], batch_ids)
        profile_1141 = next(p for p in self.manifest["releaseRepairProfiles"] if p["previousTotalWords"] == 1141)
        self.assertEqual(profile_1141["releaseAdditionIds"], batch_ids)

    def test_every_batch_record_matches_canonical_inventory_and_schema(self):
        for entry in self.batch["words"]:
            rid = entry["id"]
            self.assertIn(rid, self.records)
            canonical = self.records[rid]
            self.assertEqual(canonical, entry)
            self.assertEqual(canonical["cefr_level"], canonical["senses"][0]["cefr_level"])
            self.assertFalse(canonical["senses"][0]["definition_en"].casefold().startswith(canonical["word"].casefold()))
            self.assertGreaterEqual(len(canonical["collocations"]), 3, rid)
            self.assertGreaterEqual(len(canonical["examples"][0]["en"].split()), 5, rid)
            self.assertIsNone(canonical["verb_forms"])
            self.assertTrue(canonical["word_family"])

    def test_cmudict_ipa_provenance_matches_every_record(self):
        self.assertEqual(self.batch["ipaSummary"]["populated"], 40)
        self.assertEqual(self.batch["ipaSummary"]["leftBlank"], 0)
        self.assertEqual(self.cmu_ledger["recordCount"], 40)
        ledger_by_id = {row["id"]: row for row in self.cmu_ledger["records"]}
        self.assertEqual(set(ledger_by_id), {w["id"] for w in self.batch["words"]})
        for rid, row in ledger_by_id.items():
            computed = arpabet_to_ipa(row["arpabet"])
            self.assertEqual(computed, row["phoneticUs"], rid)
            self.assertEqual(self.records[rid]["phonetic"]["us"], computed, rid)

    def test_word_family_graph_improvement_and_zero_new_mismatches(self):
        report = wf_mod.load_source(ROOT)
        self.assertEqual(report["headwords"], 1181)
        self.assertEqual(report["headwords_with_family"], 322)
        self.assertEqual(report["link_count"], 420)
        self.assertEqual(len(report["missing_targets"]), 50)
        self.assertEqual(len(report["pos_mismatches"]), 1)
        self.assertEqual(len(report["meaning_mismatches"]), 72)
        self.assertEqual(len(report["nonreciprocal_links"]), 10)
        self.assertEqual(len(report["duplicate_links"]), 0)
        self.assertEqual(len(report["duplicate_headwords"]), 0)
        self.assertEqual(len(report["malformed"]), 0)
        for excluded in ("convention", "purchaser", "employ"):
            self.assertNotIn(excluded, self.by_word)

    def test_ci_registers_this_batch_test(self):
        workflow = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
        self.assertIn("-p 'test_vocabulary_batch_026.py'", workflow)


if __name__ == "__main__":
    unittest.main()
