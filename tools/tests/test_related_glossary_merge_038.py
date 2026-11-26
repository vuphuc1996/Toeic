"""Regression for the merged v2.95.45 Related Glossary additions and sense fixes."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path
from glossary_test_helpers import composite_sha_reversing_vocabulary_patch, restore_batch_044

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "ask for": ("v phr", "request"),
    "change": ("n", "transition"),
    "comments": ("n pl", "feedback"),
    "communicate with": ("v phr", "contact"),
    "connection": ("n", "network"),
}

def read_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def composite_sha(paths):
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
        digest.update(b"\n")
    return digest.hexdigest()

class RelatedGlossaryMerge038Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = read_json("patches-related-terms/v2.95.45/batch-038-glossary-ledger.json")
        cls.add_patch = read_json("patches-related-terms/v2.95.45/related-terms-038.json")
        cls.correction_patch = read_json("patches-related-terms/v2.95.45/glossary-corrections-038.json")
        cls.glossary = read_json("data/related-terms.json")
        cls.rows = {row["term"].casefold(): row for row in cls.glossary["terms"]}
        cls.targets = {}
        cls.headwords = set()
        for path in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
            for word in read_json(path.relative_to(ROOT).as_posix())["words"]:
                cls.headwords.add(word["word"].casefold())
                for sense in word.get("senses", []):
                    for relation in ("synonyms", "antonyms"):
                        for target in sense.get(relation, []) or []:
                            cls.targets.setdefault(str(target).strip().casefold(), set()).add(word["word"].casefold())

    def test_addition_inventory_is_exact_and_guarded(self):
        expected = set(EXPECTED)
        self.assertEqual(self.ledger["batch"], "038")
        self.assertEqual(self.ledger["release"], "2.95.45")
        self.assertEqual(self.ledger["count"], len(expected))
        self.assertEqual({row["term"].casefold() for row in self.ledger["records"]}, expected)
        self.assertEqual({op["term"].casefold() for op in self.add_patch["operations"]}, expected)
        self.assertTrue(all(op["expect"] == {"absent": True} for op in self.add_patch["operations"]))

    def test_each_added_term_is_an_existing_relation_target_not_a_headword(self):
        for term, (pos, anchor) in EXPECTED.items():
            self.assertIn(term, self.targets, term)
            self.assertIn(anchor, self.targets[term], term)
            self.assertNotIn(term, self.headwords, term)
            self.assertEqual(self.rows[term]["pos"], pos, term)

    def test_new_entries_have_cambridge_provenance_and_no_placeholders(self):
        for term in EXPECTED:
            row = self.rows[term]
            self.assertTrue(row["definition_en"].strip(), term)
            self.assertTrue(row["source"].startswith("Cambridge Dictionary"), term)
            self.assertTrue(row["sourceUrls"], term)
            self.assertTrue(all(url.startswith("https://dictionary.cambridge.org/dictionary/english/") for url in row["sourceUrls"]), term)
            self.assertNotRegex(row["definition_en"], r"(?i)placeholder|reference gloss|todo|tbd")

    def test_sense_corrections_follow_existing_relation_anchors(self):
        expectations = {
            "caller": ("visitor", "người đến thăm; khách ghé thăm"),
            "article": ("item", "món đồ; vật phẩm; mặt hàng"),
            "assume": ("undertake", "đảm nhận; nhận trách nhiệm"),
        }
        ledger = {row["term"]: row for row in self.ledger["corrections"]}
        for term, (anchor, meaning) in expectations.items():
            self.assertIn(anchor, self.targets[term], term)
            self.assertEqual(self.rows[term]["meaning_vi"], meaning, term)
            self.assertEqual(ledger[term]["anchor"], anchor, term)
            self.assertIn("sense", ledger[term]["reason"].lower(), term)

    def _restore_batch039(self, glossary):
        # Reverse Batch 044 first, then later batches in descending order before
        # reconstructing the historical Batch 038 base.
        glossary = restore_batch_044(glossary, ROOT)
        by = {row["term"].casefold(): row for row in glossary["terms"]}
        # Reverse Batch 043 before Batch 042 when rebuilding the historical Batch 038 base.
        batch_043 = read_json("patches-related-terms/v2.95.62/related-terms-043.json")
        for op in batch_043["operations"]:
            row = by[op["term"].casefold()]
            for field, value in op["expect"].items():
                if field == "term":
                    continue
                if value is None:
                    row.pop(field, None)
                else:
                    row[field] = value
        batch_042 = read_json("patches-related-terms/v2.95.61/related-terms-042.json")
        for op in batch_042["operations"]:
            row = by[op["term"].casefold()]
            for field, value in op["expect"].items():
                if field == "term":
                    continue
                if value is None:
                    row.pop(field, None)
                else:
                    row[field] = value
        batch_041 = read_json("patches-related-terms/v2.95.52/related-terms-041.json")
        for op in batch_041["operations"]:
            row = by[op["term"].casefold()]
            for field, value in op["expect"].items():
                if field == "term":
                    continue
                if value is None:
                    row.pop(field, None)
                else:
                    row[field] = value
        batch_040 = read_json("patches-related-terms/v2.95.51/related-terms-040.json")
        for op in batch_040["operations"]:
            row = by[op["term"].casefold()]
            for field, value in op["expect"].items():
                if field == "term":
                    continue
                if value is None:
                    row.pop(field, None)
                else:
                    row[field] = value
        patch = json.loads((ROOT / "patches-related-terms/v2.95.50/related-terms-039.json").read_text(encoding="utf-8"))
        by = {row["term"].casefold(): row for row in glossary["terms"]}
        for op in patch["operations"]:
            row = by[op["term"].casefold()]
            for field, value in op["expect"].items():
                if field == "term":
                    continue
                if value is None:
                    row.pop(field, None)
                else:
                    row[field] = value
            for field in op["set"]:
                if field not in op["expect"]:
                    row.pop(field, None)
        return glossary

    def test_correction_patch_is_exact_guarded_and_base_hash_is_reconstructable(self):
        glossary = json.loads((ROOT / "data/related-terms.json").read_text(encoding="utf-8"))
        glossary = self._restore_batch039(glossary)
        # Reverse additions first, then reverse only the guarded fields for the three corrections.
        glossary["terms"] = [row for row in glossary["terms"] if row["term"].casefold() not in EXPECTED]
        by = {row["term"].casefold(): row for row in glossary["terms"]}
        for op in self.correction_patch["operations"]:
            row = by[op["term"].casefold()]
            for field, value in op["expect"].items():
                if field != "term":
                    row[field] = value
        payload = (json.dumps(glossary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.correction_patch["baseFileSha256"])

    def test_addition_patch_base_hash_follows_corrected_glossary(self):
        glossary = json.loads((ROOT / "data/related-terms.json").read_text(encoding="utf-8"))
        glossary = self._restore_batch039(glossary)
        glossary["terms"] = [row for row in glossary["terms"] if row["term"].casefold() not in EXPECTED]
        payload = (json.dumps(glossary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.add_patch["baseFileSha256"])

    def test_canonical_and_learning_banks_match_protected_hashes(self):
        vocabulary = list((ROOT / "data/vocabulary").glob("[A-Z].json"))
        protected = [ROOT / "data/grammar/lessons.json", ROOT / "data/listening/listening-library.json", ROOT / "data/readings/reading-library.json", ROOT / "data/practice/part5-sentence-completion.json"]
        self.assertEqual(composite_sha_reversing_vocabulary_patch(vocabulary, ROOT, "patches/v2.95.54/independent-audit-stage-1-data.json"), self.ledger["canonicalVocabularySha256"])
        self.assertEqual(composite_sha(protected), self.ledger["protectedLearningBankSha256"])

    def test_glossary_identity_is_unique(self):
        keys = [row["term"].strip().casefold() for row in self.glossary["terms"]]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(len(keys), 567)

if __name__ == "__main__":
    unittest.main()
