"""Word Family reciprocal-link and self-reference remediation tests across historical v2.95.73 and current v2.95.76."""
from __future__ import annotations
import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/tests"))
from glossary_test_helpers import reverse_batch_027_word_family

SPEC = importlib.util.spec_from_file_location("word_family_audit", ROOT / "tools/audit-word-family-graph.py")
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)

EXPECTED_HISTORICAL_LINKS = [
    ("accessible", "access", "n", "quyền truy cập; lối vào"),
    ("authenticate", "authentic", "adj", "xác thực; chân thực; đáng tin là thật"),
    ("conference", "confer", "v", "trao; cấp; hội ý; bàn bạc"),
    ("consumer", "consume", "v", "tiêu thụ; sử dụng hết; tiêu hao"),
    ("consumption", "consume", "v", "tiêu thụ; sử dụng hết; tiêu hao"),
    ("flexibility", "flexible", "adj", "linh hoạt; mềm dẻo"),
    ("guide", "guidance", "n", "sự hướng dẫn; chỉ dẫn"),
    ("guideline", "guidance", "n", "sự hướng dẫn; chỉ dẫn"),
    ("month", "monthly", "adj", "hằng tháng"),
    ("utilize", "utilization", "n", "việc sử dụng; mức độ tận dụng"),
]


def load_documents():
    manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))
    documents = {}
    records = {}
    for item in manifest["letters"]:
        rel = item["file"].replace("./", "", 1)
        path = (ROOT / rel).resolve()
        doc = json.loads(path.read_text(encoding="utf-8"))
        documents[path] = doc
        for row in doc["words"]:
            records[row["word"].casefold()] = row
    return manifest, documents, records


class VocabularyBatch027Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.documents, cls.records = load_documents()
        cls.pkg = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        cls.patch = json.loads((ROOT / "patches/v2.95.73/batch-001-word-family-reciprocity.json").read_text(encoding="utf-8"))
        cls.ledger_74 = json.loads((ROOT / "patches/v2.95.74/word-family-audit-ledger.json").read_text(encoding="utf-8"))
        cls.batch_028 = json.loads((ROOT / "data/vocabulary/batch-028.json").read_text(encoding="utf-8"))

    def _build_v29573_snapshot(self):
        documents = copy.deepcopy(self.documents)
        later_ids = {row["id"] for row in self.batch_028["words"]}
        for document in documents.values():
            document["words"] = [row for row in document["words"] if row["id"] not in later_ids]
        restored_ids = reverse_batch_027_word_family(documents, ROOT)
        self.assertEqual(len(restored_ids), 12)
        by_id = {}
        by_word = {}
        for doc in documents.values():
            for row in doc["words"]:
                by_id[row["id"]] = row
                by_word[row["word"].casefold()] = row
        for removed in self.patch["removedSelfLinks"]:
            owner = by_id[removed["ownerId"]]
            family = owner.get("word_family") or []
            owner["word_family"] = [
                entry for entry in family
                if not (
                    str(entry.get("word", "")).casefold() == removed["target"].casefold()
                    and str(entry.get("pos", "")) == removed["pos"]
                )
            ]
        for added in self.patch["addedLinks"]:
            owner = by_id[added["ownerId"]]
            family = owner.setdefault("word_family", [])
            if not any(str(entry.get("word", "")).casefold() == added["target"].casefold() for entry in family):
                family.append({
                    "word": added["target"],
                    "pos": added["pos"],
                    "meaning_vi": added["meaning_vi"],
                })
        return documents, by_word

    def test_release_and_patch_metadata(self):
        self.assertEqual(self.manifest["version"], self.pkg["version"])
        self.assertEqual(self.manifest["version"], "2.95.76")
        version = self.manifest["version"]
        for marker_rel in ("index.html", "assets/js/app.js", "sw.js", "docs/versions/CURRENT_VERSION.md"):
            self.assertIn(version, (ROOT / marker_rel).read_text(encoding="utf-8"), marker_rel)
        self.assertEqual(self.manifest["totalWords"], 1221)
        self.assertEqual(self.patch["baseDataVersion"], "2.95.72")
        self.assertEqual(self.patch["targetDataVersion"], "2.95.73")
        self.assertEqual(self.patch["canonicalHeadwordCount"], 1181)
        self.assertEqual(self.patch["changedRecordCount"], 12)
        self.assertEqual(len(self.patch["addedLinks"]), 10)
        self.assertEqual(len(self.patch["removedSelfLinks"]), 2)

    def test_all_ten_historical_links_match_canonical_target_senses_in_isolated_v29573_snapshot(self):
        documents, by_word = self._build_v29573_snapshot()
        for owner_word, target_word, pos, meaning_vi in EXPECTED_HISTORICAL_LINKS:
            with self.subTest(owner=owner_word, target=target_word):
                owner = by_word[owner_word]
                target = by_word[target_word]
                links = [row for row in owner.get("word_family", [])
                         if row.get("word", "").casefold() == target_word]
                self.assertEqual(len(links), 1)
                self.assertEqual(links[0]["pos"], pos)
                self.assertEqual(links[0]["meaning_vi"], meaning_vi)
                matching_senses = [sense for sense in target["senses"] if sense.get("pos") == pos]
                self.assertTrue(matching_senses)
                self.assertIn(meaning_vi, [sense.get("meaning_vi") for sense in matching_senses])
        report_73 = AUDIT.audit_data([(path.name, doc) for path, doc in documents.items()])
        self.assertEqual(len(report_73["self_references"]), 0)
        self.assertEqual(len(report_73["nonreciprocal_links"]), 0)
        self.assertEqual(len(report_73["pos_mismatches"]), 0)

    def test_two_self_referential_links_are_removed_in_historical_and_current_snapshots(self):
        _, by_word_73 = self._build_v29573_snapshot()
        for snapshot in (by_word_73, self.records):
            for owner_word in ("hire", "utilization"):
                with self.subTest(owner=owner_word):
                    owner = snapshot[owner_word]
                    self.assertFalse(any(row.get("word", "").casefold() == owner_word
                                         for row in owner.get("word_family", [])))

    def test_current_v29576_accessible_to_access_uses_verb_sense_and_zero_structural_defects(self):
        accessible = self.records["accessible"]
        access = self.records["access"]
        access_links = [row for row in accessible.get("word_family", [])
                        if row.get("word", "").casefold() == "access"]
        self.assertEqual(len(access_links), 1)
        self.assertEqual(access_links[0]["pos"], "v")
        self.assertEqual(access_links[0]["meaning_vi"], "truy cập; tiếp cận")
        verb_senses = [s for s in access["senses"] if s.get("pos") == "v"]
        self.assertTrue(verb_senses)
        self.assertIn("truy cập; tiếp cận", [s.get("meaning_vi") for s in verb_senses])

        report = AUDIT.load_source(ROOT)
        self.assertEqual(report["headwords"], 1221)
        self.assertEqual(report["headwords_with_family"], 331)
        self.assertEqual(report["link_count"], 428)
        self.assertEqual(len(report["missing_targets"]), 50)
        self.assertEqual(len(report["pos_mismatches"]), 0)
        self.assertEqual(len(report["meaning_mismatches"]), 70)
        self.assertEqual(len(report["nonreciprocal_links"]), 0)
        self.assertEqual(len(report["self_references"]), 0)
        self.assertEqual(len(report["duplicate_links"]), 0)
        self.assertEqual(len(report["duplicate_headwords"]), 0)
        self.assertEqual(len(report["malformed"]), 0)

    def test_v29574_ledger_covers_all_12_v29573_owners_and_rejects_double_reversal(self):
        ids_74 = [row["id"] for row in self.ledger_74["reconciliationRecords"]]
        ids_73 = (
            {row["ownerId"] for row in self.patch["addedLinks"]}
            | {row["ownerId"] for row in self.patch["removedSelfLinks"]}
        )
        self.assertEqual(len(ids_74), 12)
        self.assertEqual(set(ids_74), ids_73)

        documents = copy.deepcopy(self.documents)
        seen: set[str] = set()
        restored = reverse_batch_027_word_family(documents, ROOT, restored_ids=seen)
        self.assertEqual(restored, ids_73)
        self.assertEqual(seen, ids_73)
        with self.assertRaises(AssertionError):
            reverse_batch_027_word_family(documents, ROOT, restored_ids=seen)


if __name__ == "__main__":
    unittest.main()
