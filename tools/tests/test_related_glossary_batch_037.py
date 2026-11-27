"""Regression contract for Cambridge Dictionary Related Glossary batch 037."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path
from glossary_test_helpers import restore_batch_039, composite_sha_reversing_vocabulary_patch

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "begin": ("v", "embark"),
    "book": ("v", "reserve"),
    "bring": ("v", "deliver"),
    "characteristic": ("n", "feature"),
    "clothing": ("n", "attire"),
    "comparable": ("adj", "similar"),
    "compute": ("v", "calculate"),
    "consequence": ("n", "outcome"),
    "currency": ("n", "cash"),
    "down payment": ("n", "deposit"),
    "disturbance": ("n", "disruption"),
    "development": ("n", "progress"),
    "declaration": ("n", "statement"),
    "eager": ("adj", "willing"),
    "entire": ("adj", "complete"),
    "eventuality": ("n", "contingency"),
}


def read_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def composite_sha(paths):
    digest = hashlib.sha256()
    for path in sorted(paths):
        relative = path.relative_to(ROOT).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
        digest.update(b"\n")
    return digest.hexdigest()


def composite_sha_reversing_listening_translations(paths):
    """Reconstruct the v2.95.44 protected-bank hash excluding only eight later transcript additions."""
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
    digest = hashlib.sha256()
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
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(data).digest())
        digest.update(b"\n")
    return digest.hexdigest()


class RelatedGlossaryBatch037Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json("patches-related-terms/v2.95.44/batch-037-glossary-ledger.json")
        cls.patch = read_json("patches-related-terms/v2.95.44/related-terms-037.json")
        cls.glossary = read_json("data/related-terms.json")
        cls.rows = {row["term"].casefold(): row for row in cls.glossary["terms"]}
        cls.canonical = []
        cls.targets = {}
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            data = read_json(path.relative_to(ROOT).as_posix())
            for word in data["words"]:
                cls.canonical.append(word["word"].casefold())
                for sense in word.get("senses", []):
                    for relation in ("synonyms", "antonyms"):
                        for term in sense.get(relation, []) or []:
                            cls.targets.setdefault(str(term).strip().casefold(), set()).add(word["word"].casefold())

    def test_batch_inventory_and_patch_are_exact(self):
        expected = set(EXPECTED)
        self.assertEqual(self.ledger["batch"], "037")
        self.assertEqual(self.ledger["release"], "2.95.44")
        self.assertEqual(self.ledger["count"], len(expected))
        self.assertEqual({row["term"].casefold() for row in self.ledger["records"]}, expected)
        self.assertEqual({op["term"].casefold() for op in self.patch["operations"]}, expected)
        self.assertEqual(self.patch["batchId"], "related-glossary-037-v2.95.44")
        self.assertTrue(all(op["expect"] == {"absent": True} for op in self.patch["operations"]))

    def test_patch_base_hash_reconstructs_pre_batch_glossary(self):
        restored = restore_batch_039(self.glossary, ROOT)
        later_terms = set()
        for path in (ROOT / "patches-related-terms").glob("**/batch-*-glossary-ledger.json"):
            batch = json.loads(path.read_text(encoding="utf-8"))
            if 37 <= int(batch.get("batch", 0)) < 39:
                later_terms.update(row["term"].casefold() for row in batch.get("records", []))
        baseline = dict(restored)
        baseline["terms"] = [row for row in restored["terms"] if row["term"].casefold() not in later_terms]
        # Reverse only post-Batch-037 exact-guarded glossary corrections.
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

    def test_each_record_matches_ledger_and_cambridge_provenance(self):
        for record in self.ledger["records"]:
            term = record["term"]
            row = self.rows[term.casefold()]
            for field in ("meaning_vi_preserved", "pos", "definition_en", "source", "sourceUrls"):
                actual = row["meaning_vi"] if field == "meaning_vi_preserved" else row.get(field)
                self.assertEqual(actual, record[field], term)
            self.assertGreaterEqual(len(row["definition_en"].split()), 6, term)
            self.assertTrue(row["source"].startswith("Cambridge "), term)
            self.assertTrue(row["sourceUrls"], term)
            for url in row["sourceUrls"]:
                self.assertTrue(url.startswith("https://dictionary.cambridge.org/dictionary/english/"), term)
            self.assertNotRegex(row["definition_en"], r"(?i)\b(?:placeholder|reference gloss|tbd|todo)\b")

    def test_all_terms_are_existing_relation_targets_not_new_headwords(self):
        for term in EXPECTED:
            self.assertIn(term, self.targets, f"{term} must already be referenced by a relation")
            self.assertNotIn(term, self.canonical, f"{term} must not be inserted as a canonical headword")

    def test_relation_anchor_mapping_and_pos_are_preserved(self):
        for term, (pos, anchor) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row["pos"], pos, term)
            self.assertIn(anchor, self.targets[term], term)

    def test_canonical_vocabulary_and_learning_banks_match_hashes_outside_eight_listening_translations(self):
        vocabulary = list((ROOT / "data/vocabulary").glob("[A-Z].json"))
        protected = [
            ROOT / "data/grammar/lessons.json",
            ROOT / "data/listening/listening-library.json",
            ROOT / "data/readings/reading-library.json",
            ROOT / "data/practice/part5-sentence-completion.json",
        ]
        self.assertEqual(composite_sha_reversing_vocabulary_patch(vocabulary, ROOT, "patches/v2.95.54/independent-audit-stage-1-data.json"), self.ledger["canonicalVocabularySha256"])
        self.assertEqual(composite_sha_reversing_listening_translations(protected), self.ledger["protectedLearningBankSha256"])

    def test_glossary_has_no_duplicate_casefolded_identities(self):
        keys = [row["term"].strip().casefold() for row in self.glossary["terms"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(self.glossary["terms"]), 567)


if __name__ == "__main__":
    unittest.main()
