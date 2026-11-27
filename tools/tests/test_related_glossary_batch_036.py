"""Regression contract for Cambridge-indexed related-glossary coverage batch 036."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path
from glossary_test_helpers import restore_batch_039, composite_sha_reversing_vocabulary_patch

ROOT = Path(__file__).resolve().parents[2]


def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def composite_sha(paths):
    h = hashlib.sha256()
    for path in sorted(paths):
        rel = path.relative_to(ROOT).as_posix()
        data = path.read_bytes()
        h.update(rel.encode())
        h.update(b"\0")
        h.update(hashlib.sha256(data).digest())
        h.update(b"\n")
    return h.hexdigest()


def composite_sha_reversing_listening_translations(paths):
    """Hash protected learning banks after removing only the eight v2.95.76 translation additions."""
    added_ids = {
        "batch026-part3-vendor-call",
        "batch026-part3-training-room",
        "batch026-part3-invoice-correction",
        "batch026-part3-access-card",
        "batch026-part4-building-notice",
        "batch026-part4-travel-update",
        "batch026-part4-product-launch",
        "batch026-part4-policy-reminder",
    }
    h = hashlib.sha256()
    seen = set()
    for path in sorted(paths):
        data = path.read_bytes()
        if path.name == "listening-library.json":
            document = json.loads(data.decode("utf-8"))
            for unit in document["listening"]:
                if unit.get("id") in added_ids:
                    if not unit.get("transcriptTranslation", "").strip():
                        raise AssertionError(f"Missing v2.95.76 transcript translation: {unit.get('id')}")
                    seen.add(unit["id"])
                    del unit["transcriptTranslation"]
            if seen != added_ids:
                raise AssertionError(f"Listening remediation IDs differ: {sorted(seen ^ added_ids)}")
            data = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        h.update(path.relative_to(ROOT).as_posix().encode())
        h.update(b"\0")
        h.update(hashlib.sha256(data).digest())
        h.update(b"\n")
    return h.hexdigest()


class RelatedGlossaryBatch036Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json("patches-related-terms/v2.95.43/batch-036-glossary-ledger.json")
        cls.patch = read_json("patches-related-terms/v2.95.43/related-terms-036.json")
        cls.data = read_json("data/related-terms.json")
        cls.current = {row["term"].casefold(): row for row in cls.data["terms"]}

    def test_inventory_and_patch_are_consistent(self):
        expected = {"able", "accuracy", "actual", "assume", "business", "caller", "capable", "car", "carry", "choice", "company"}
        self.assertEqual(self.ledger["batch"], "036")
        self.assertEqual(self.ledger["release"], "2.95.43")
        self.assertEqual(self.ledger["count"], 11)
        self.assertEqual({r["term"] for r in self.ledger["records"]}, expected)
        self.assertEqual({op["term"] for op in self.patch["operations"]}, expected)
        self.assertEqual(self.patch["batchId"], "related-glossary-036-v2.95.43")
        self.assertTrue(all(op["expect"] == {"absent": True} for op in self.patch["operations"]))

    def test_patch_base_hash_reconstructs_pre_batch_glossary(self):
        restored = restore_batch_039(self.data, ROOT)
        added = {r["term"].casefold() for r in self.ledger["records"]}
        # Remove this and all later additive glossary batches before reconstructing
        # the original v2.95.43 baseline. Historical patch hashes remain stable as
        # new releases append further records.
        for ledger_path in (ROOT / "patches-related-terms").glob("**/batch-*-glossary-ledger.json"):
            later = json.loads(ledger_path.read_text(encoding="utf-8"))
            if 36 < int(later.get("batch", 0)) < 39:
                added.update(record["term"].casefold() for record in later.get("records", []))
        baseline = dict(restored)
        baseline["terms"] = [r for r in restored["terms"] if r["term"].casefold() not in added]
        # Later exact-guarded sense corrections must be reversed as well when
        # reconstructing the pre-Batch-036 file. Terms added by Batch 036 are
        # already absent here; corrections to older Batch 035 rows (e.g. article) remain.
        for correction_path in (ROOT / "patches-related-terms").glob("**/glossary-corrections-*.json"):
            correction = json.loads(correction_path.read_text(encoding="utf-8"))
            rows = {row["term"].casefold(): row for row in baseline["terms"]}
            for operation in correction.get("operations", []):
                row = rows.get(operation["term"].casefold())
                if row is None:
                    continue
                for field, value in operation.get("expect", {}).items():
                    if field != "term":
                        row[field] = value
        payload = (json.dumps(baseline, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch["baseFileSha256"])

    def test_rows_match_ledger_and_have_cambridge_provenance(self):
        for record in self.ledger["records"]:
            row = self.current[record["term"].casefold()]
            later_values = {}
            for correction_path in (ROOT / "patches-related-terms").glob("**/glossary-corrections-*.json"):
                correction = json.loads(correction_path.read_text(encoding="utf-8"))
                for operation in correction.get("operations", []):
                    if operation["term"].casefold() == record["term"].casefold():
                        later_values.update(operation.get("set", {}))
            for field in ("meaning_vi_preserved", "pos", "definition_en", "source", "sourceUrls"):
                actual_field = "meaning_vi" if field == "meaning_vi_preserved" else field
                expected = later_values.get(actual_field, record[field])
                actual = row.get(actual_field)
                self.assertEqual(actual, expected, record["term"])
            self.assertGreaterEqual(len(row["definition_en"].split()), 6)
            self.assertTrue(row["source"].startswith("Cambridge "), record["term"])
            self.assertEqual(row["sourceUrls"], [f"https://dictionary.cambridge.org/dictionary/english/{record['term']}" ])

    def test_terms_are_relation_targets_and_not_canonical_headwords(self):
        canonical = set()
        targets = set()
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            canonical.update(row["word"].casefold() for row in data["words"])
            for word in data["words"]:
                for sense in word.get("senses", []):
                    for rel in ("synonyms", "antonyms"):
                        targets.update(str(term).strip().casefold() for term in (sense.get(rel) or []))
        self.assertTrue(all(r["term"].casefold() not in canonical for r in self.ledger["records"]))
        self.assertTrue(all(r["term"].casefold() in targets for r in self.ledger["records"]))

    def test_definitions_are_nonplaceholder_and_urls_are_cambridge_https(self):
        for record in self.ledger["records"]:
            self.assertNotIn("placeholder", record["definition_en"].casefold())
            self.assertNotIn("reference gloss", record["definition_en"].casefold())
            self.assertTrue(record["sourceUrls"])
            for url in record["sourceUrls"]:
                self.assertTrue(url.startswith("https://dictionary.cambridge.org/dictionary/english/"))

    def test_canonical_vocabulary_and_learning_banks_are_unchanged_outside_eight_listening_translations(self):
        vocabulary = list((ROOT / "data/vocabulary").glob("[A-Z].json"))
        protected = [
            ROOT / "data/grammar/lessons.json",
            ROOT / "data/listening/listening-library.json",
            ROOT / "data/readings/reading-library.json",
            ROOT / "data/practice/part5-sentence-completion.json",
        ]
        self.assertEqual(composite_sha_reversing_vocabulary_patch(vocabulary, ROOT, "patches/v2.95.54/independent-audit-stage-1-data.json"), self.ledger["canonicalVocabularySha256"])
        self.assertEqual(composite_sha_reversing_listening_translations(protected), self.ledger["protectedLearningBankSha256"])



if __name__ == "__main__":
    unittest.main()
