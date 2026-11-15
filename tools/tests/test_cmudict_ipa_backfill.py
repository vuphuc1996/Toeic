"""Regression coverage for the source-linked CMUdict IPA cumulative backfill in v2.70.0."""
import json
import unittest
from pathlib import Path

from tools.cmudict_ipa import LEDGER, ROOT, arpabet_to_ipa, load_records


class CmudictIpaBackfillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        cls.records, _ = load_records()

    def test_backfill_has_the_audited_record_count(self):
        self.assertEqual(self.ledger["recordCount"], 298)
        self.assertEqual(len(self.ledger["records"]), 298)

    def test_every_ledger_entry_matches_canonical_record_and_conversion(self):
        seen = set()
        for row in self.ledger["records"]:
            self.assertNotIn(row["id"], seen)
            seen.add(row["id"])
            record = self.records[row["id"]]
            self.assertEqual(record["word"].casefold(), row["word"].casefold())
            self.assertEqual(arpabet_to_ipa(row["arpabet"]), row["phoneticUs"], row["id"])
            self.assertEqual(record["phonetic"]["us"], row["phoneticUs"], row["id"])

    def test_ledger_documents_source_conversion_and_caveat(self):
        source = self.ledger["source"]
        conversion = self.ledger["conversion"]
        self.assertIn("cmusphinx/cmudict", source["upstream"])
        self.assertIn("ARPABET", source["notation"])
        self.assertIn("may contain errors", source["caveat"])
        self.assertTrue((ROOT / "docs/licenses/CMUdict-DATA-LICENSE.txt").exists())
        self.assertIn("markers placed before syllable onset", conversion["stress"])

    def test_ambiguous_or_unmatched_entries_are_not_auto_filled(self):
        excluded = self.ledger["excluded"]
        self.assertEqual(excluded["multiple_pronunciations"], 60)
        self.assertEqual(excluded["no_exact_CMUdict_entry"], 25)
        self.assertEqual(excluded["multiple_primary_stress"], 6)
        self.assertIn("Leave phonetic.us blank", excluded["policy"])

    def test_ipa_format_uses_supported_project_symbols(self):
        allowed = set(" ()./;abdefhijklmnoprstuvwzæðŋɑɔəɚɝɡɪʃʊʌʒˈˌː\u032cθ")
        for row in self.ledger["records"]:
            ipa = row["phoneticUs"]
            self.assertTrue(ipa.startswith("/") and ipa.endswith("/"), row["id"])
            self.assertFalse(set(ipa) - allowed, (row["id"], set(ipa) - allowed))


if __name__ == "__main__":
    unittest.main()
