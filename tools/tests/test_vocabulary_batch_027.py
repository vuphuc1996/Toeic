"""Word Family reciprocal-link and self-reference remediation for v2.95.73."""
from __future__ import annotations
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("word_family_audit", ROOT / "tools/audit-word-family-graph.py")
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)

EXPECTED_LINKS = [
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


def load_records():
    manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))
    records = {}
    for item in manifest["letters"]:
        path = ROOT / item["file"].replace("./", "", 1)
        for row in json.loads(path.read_text(encoding="utf-8"))["words"]:
            records[row["word"].casefold()] = row
    return manifest, records


class VocabularyBatch027Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.records = load_records()
        cls.patch = json.loads((ROOT / "patches/v2.95.73/batch-001-word-family-reciprocity.json").read_text(encoding="utf-8"))

    def test_release_and_patch_metadata(self):
        self.assertEqual(self.manifest["version"], "2.95.73")
        self.assertEqual(self.manifest["totalWords"], 1181)
        self.assertEqual(self.manifest["previousReleaseTotalWords"], 1181)
        self.assertEqual(self.manifest["releaseAdditionIds"], [])
        self.assertEqual(self.patch["baseDataVersion"], "2.95.72")
        self.assertEqual(self.patch["targetDataVersion"], "2.95.73")
        self.assertEqual(self.patch["canonicalHeadwordCount"], 1181)
        self.assertEqual(self.patch["changedRecordCount"], 12)
        self.assertEqual(len(self.patch["addedLinks"]), 10)
        self.assertEqual(len(self.patch["removedSelfLinks"]), 2)

    def test_all_ten_reverse_links_match_the_canonical_target_sense(self):
        for owner_word, target_word, pos, meaning_vi in EXPECTED_LINKS:
            with self.subTest(owner=owner_word, target=target_word):
                owner = self.records[owner_word]
                target = self.records[target_word]
                links = [row for row in owner.get("word_family", [])
                         if row.get("word", "").casefold() == target_word]
                self.assertEqual(len(links), 1)
                self.assertEqual(links[0]["pos"], pos)
                self.assertEqual(links[0]["meaning_vi"], meaning_vi)
                matching_senses = [sense for sense in target["senses"] if sense.get("pos") == pos]
                self.assertTrue(matching_senses)
                self.assertIn(meaning_vi, [sense.get("meaning_vi") for sense in matching_senses])

    def test_two_self_referential_links_are_removed(self):
        for owner_word in ("hire", "utilization"):
            with self.subTest(owner=owner_word):
                owner = self.records[owner_word]
                self.assertFalse(any(row.get("word", "").casefold() == owner_word
                                     for row in owner.get("word_family", [])))

    def test_complete_word_family_audit_has_no_structural_graph_defects(self):
        report = AUDIT.load_source(ROOT)
        self.assertEqual(report["headwords"], 1181)
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


if __name__ == "__main__":
    unittest.main()
