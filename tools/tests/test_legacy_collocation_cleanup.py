"""Regression guards for the v2.21.0 cleanup of eight known FD001 collocation debts."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "apprentice-n": ["apprentice electrician", "apprentice mechanic"],
    "event-coordinator-n": ["event coordinator", "assistant event coordinator"],
    "fare-n": ["bus fare", "one-way fare"],
    "replace-v": ["replace a device", "replace a battery"],
    "reserve-v": ["reserve a room", "reserve a seat"],
    "warehouseman-n": ["assistant warehouseman", "bonded warehouseman"],
    "zero-based-budgeting-n": ["zero-based budgeting process", "zero-based budgeting method"],
}


class LegacyCollocationCleanupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))
        cls.records = {}
        for item in manifest["letters"]:
            path = ROOT / item["file"].removeprefix("./")
            for record in json.loads(path.read_text(encoding="utf-8"))["words"]:
                cls.records[record["id"]] = record
        cls.baseline = json.loads((ROOT / "tools/quality-baseline.json").read_text(encoding="utf-8"))

    def test_all_seven_target_records_have_reviewed_collocations(self):
        for record_id, expected in EXPECTED.items():
            self.assertEqual(self.records[record_id]["collocations"], expected, record_id)

    def test_no_fd001_legacy_debt_remains(self):
        self.assertEqual(self.baseline["rules"]["FD001"]["violations"], [])

    def test_stable_vocabulary_identity_keeps_928_baseline_plus_batch_017(self):
        ids = set(self.records)
        baseline = set(json.loads((ROOT / "tools/baseline-ids.json").read_text(encoding="utf-8"))["ids"])
        batch = json.loads((ROOT / "data/vocabulary/batch-006.json").read_text(encoding="utf-8"))
        self.assertTrue(baseline.issubset(ids))
        self.assertEqual(len(batch["words"]), 43)
        self.assertEqual(len(ids), 971)


if __name__ == "__main__":
    unittest.main()
