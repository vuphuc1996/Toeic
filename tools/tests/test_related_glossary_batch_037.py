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
    """Reconstruct the v2.95.44 protected-bank snapshot by reversing allowlisted later additions."""
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

            # v2.95.83 appends one practice-only Part 4 question to each of
            # ten allowlisted, pre-existing non-reserve talks. Strip only
            # those rows when reconstructing the historical v2.95.44 hash.
            practice_only_part4_ids = {
                "part4-office-announcement",
                "part4-conference-update",
                "part4-safety-announcement",
                "part4-product-launch",
                "part4-quarterly-town-hall",
                "part4-customer-voicemail",
                "part4-warehouse-safety-briefing",
                "part4-training-registration",
                "part4-travel-service-update",
                "part4-quarterly-inventory-report",
            }
            practice_only_seen = set()
            for unit in document["listening"]:
                if unit.get("id") not in practice_only_part4_ids:
                    continue
                questions = unit.get("questions") or []
                if len(questions) < 4 or any(q.get("mockEligible") is False for q in questions[:3]) or any(q.get("mockEligible") is not False for q in questions[3:]):
                    raise AssertionError(f"Unexpected Part 4 practice-only addition: {unit.get('id')}")
                practice_only_seen.add(unit["id"])
                unit["questions"] = questions[:3]
            if practice_only_seen != practice_only_part4_ids:
                raise AssertionError(f"Part 4 practice-only IDs differ: {sorted(practice_only_seen ^ practice_only_part4_ids)}")

            # v2.95.86 adds exactly three Part 1 photo reserve records.
            # Validate the fail-closed fields before excluding them from this
            # historical v2.95.44 protected-bank hash reconstruction.
            batch_018_part1_ids = {
                "part1-construction-plans",
                "part1-laboratory-bench",
                "part1-supermarket-shelf",
            }
            batch_018_seen = set()
            restored_units = []
            for unit in document["listening"]:
                if unit.get("id") not in batch_018_part1_ids:
                    restored_units.append(unit)
                    continue
                questions = unit.get("questions") or []
                if (
                    unit.get("part") != "Part 1"
                    or unit.get("editorialBatch") != "018"
                    or unit.get("editorialStatus") != "reserve-pending-independent-review"
                    or len(questions) != 1
                    or questions[0].get("mockEligible") is not False
                ):
                    raise AssertionError(f"Unexpected Batch 018 Part 1 reserve record: {unit.get('id')}")
                batch_018_seen.add(unit["id"])
            if batch_018_seen != batch_018_part1_ids:
                raise AssertionError(f"Batch 018 Part 1 IDs differ: {sorted(batch_018_seen ^ batch_018_part1_ids)}")
            document["listening"] = restored_units
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


    def test_part4_question_level_practice_additions_are_exactly_expected(self):
        listening = read_json("data/listening/listening-library.json")["listening"]
        expected_ids = {
            "part4-office-announcement", "part4-conference-update",
            "part4-safety-announcement", "part4-product-launch",
            "part4-quarterly-town-hall", "part4-customer-voicemail",
            "part4-warehouse-safety-briefing", "part4-training-registration",
            "part4-travel-service-update", "part4-quarterly-inventory-report",
        }
        resources = {item["id"]: item for item in listening}
        self.assertTrue(expected_ids.issubset(resources))
        for resource_id in expected_ids:
            resource = resources[resource_id]
            self.assertGreaterEqual(len(resource["questions"]), 4, resource_id)
            self.assertTrue(all(q.get("mockEligible") is False for q in resource["questions"][3:]), resource_id)
            added = resource["questions"][3]
            self.assertIs(added.get("mockEligible"), False, resource_id)
            self.assertEqual(len(added["choices"]), 4, resource_id)
            self.assertEqual(added["choiceIds"], [f"listening:{resource_id}:4:choice:{i}" for i in range(1, 5)])

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
