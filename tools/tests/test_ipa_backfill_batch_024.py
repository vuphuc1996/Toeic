"""Regression checks for the v2.95.18 US IPA backfill batch 024."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class UsIpaBackfillBatch024Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = read_json("data/manifest.json")
        cls.records = {}
        cls.ids = set()
        for entry in manifest["letters"]:
            rows = read_json(entry["file"].removeprefix("./"))["words"]
            for row in rows:
                cls.records[row["id"]] = row
                cls.ids.add(row["id"])
        cls.batch = read_json("data/vocabulary/batch-024.json")
        cls.patch = read_json("patches/v2.95.18/batch-001-ipa.json")

    def test_batch_metadata_matches_release(self):
        self.assertEqual(self.batch["batch"], "024")
        self.assertEqual(self.batch["release"], "2.95.18")
        self.assertEqual(self.batch["count"], 13)
        self.assertIn("independent phonetic review pending", self.batch["editorialStatus"])

    def test_every_ipa_matches_canonical_record_and_source_evidence(self):
        self.assertEqual(len(self.batch["records"]), 13)
        seen = set()
        for row in self.batch["records"]:
            rid = row["id"]
            self.assertIn(rid, self.records)
            self.assertNotIn(rid, seen)
            seen.add(rid)
            canonical = self.records[rid]
            self.assertEqual(canonical["word"], row["word"])
            self.assertEqual(canonical["phonetic"]["us"], row["phonetic"]["us"])
            ipa = row["phonetic"]["us"]
            self.assertTrue(ipa.startswith("/") and ipa.endswith("/"), (rid, ipa))
            self.assertTrue(row["sourceUrl"].startswith("https://dictionary.cambridge.org/"))
            self.assertIn("pronunciation/english/", row["sourceUrl"])

    def test_patch_uses_only_approved_ipa_path_and_blank_preconditions(self):
        self.assertEqual(self.patch["baseDataVersion"], "2.95.17")
        self.assertEqual(self.patch["targetDataVersion"], "2.95.18")
        self.assertEqual(self.patch["allowedPaths"], ["/phonetic/us"])
        self.assertEqual(len(self.patch["operations"]), 13)
        for op in self.patch["operations"]:
            self.assertEqual(op["path"], "/phonetic/us")
            self.assertEqual(op["expect"], {"old": ""})
            self.assertEqual(self.records[op["id"]]["phonetic"]["us"], op["new"])

    def test_patch_sources_and_provenance_are_one_to_one(self):
        sources = {item["id"]: item for item in self.patch["sourceEvidence"]}
        ledger = {item["id"]: item for item in self.batch["records"]}
        self.assertEqual(set(sources), set(ledger))
        for rid, source in sources.items():
            self.assertEqual(source["word"], ledger[rid]["word"])
            self.assertEqual(source["ipa"], ledger[rid]["phonetic"]["us"])
            self.assertEqual(source["url"], ledger[rid]["sourceUrl"])

    def test_canonical_inventory_identity_is_preserved(self):
        baseline = read_json("tools/baseline-ids.json")
        baseline_ids = set(baseline["ids"])
        self.assertEqual(len(baseline_ids), baseline["count"])
        self.assertTrue(baseline_ids.issubset(self.ids), "A protected canonical ID from the release baseline is missing")
        self.assertEqual(self.ids, set(self.records))
        batch_028_ids = {row["id"] for row in read_json("data/vocabulary/batch-028.json")["words"]}
        self.assertTrue(batch_028_ids.issubset(self.ids), "Batch 028 additions must be present without replacing historical IDs")

    def test_ci_registers_this_batch_test(self):
        workflow = (ROOT / ".github/workflows/validate-data.yml").read_text(encoding="utf-8")
        self.assertIn("-p 'test_ipa_backfill_batch_024.py'", workflow)
        self.assertIn("Unit tests — US IPA backfill batch 024", workflow)

if __name__ == "__main__":
    unittest.main()
