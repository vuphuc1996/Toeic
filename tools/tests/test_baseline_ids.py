"""Integrity of tools/baseline-ids.json (DQ003): count, SHA-256, duplicates, tampering."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from helpers import Repo, rec


def sha_of(ids):
    return hashlib.sha256("\n".join(sorted(ids)).encode("utf-8")).hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class BaselineIdsIntegrityTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.repo = Repo(Path(self._tmp.name))
        code, out = self.repo.init_baseline()
        self.assertEqual(code, 0, out)
        self.ids_path = self.repo.root / "tools" / "baseline-ids.json"

    def load(self):
        return json.loads(self.ids_path.read_text(encoding="utf-8"))

    def save(self, doc):
        self.ids_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def fix_metadata(self, doc):
        doc["count"] = len(doc["ids"])
        doc["idSetSha256"] = sha_of(doc["ids"])

    def new_record(self):
        return rec("apple", id="apple-n", examples=[
            {"en": "She ate an apple after lunch yesterday.", "vi": "Cô ấy ăn một quả táo sau bữa trưa hôm qua."}])

    # ---- the requested cases
    def test_hash_tampered_is_structural_error(self):
        doc = self.load()
        doc["idSetSha256"] = "0" * 64
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("[ERROR] DQ003", out)
        self.assertIn("idSetSha256", out)

    def test_count_tampered_is_structural_error(self):
        doc = self.load()
        doc["count"] += 1
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("count", out)

    def test_id_removed_from_baseline_ids_is_error_not_a_new_id(self):
        doc = self.load()
        doc["ids"].remove("bravo-n")  # count and hash left as they were
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("DQ003", out)
        self.assertIn("KHÔNG so sánh được", out)
        self.assertNotIn("thêm 1", out, "a damaged list must not make a real ID look new")

    def test_duplicate_id_in_baseline_ids_is_error(self):
        doc = self.load()
        doc["ids"].append("alpha-n")
        self.fix_metadata(doc)  # metadata consistent with the list, so only the duplicate is wrong
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("ID trùng trong danh sách baseline", out)
        self.assertIn("alpha-n", out)

    def test_valid_baseline_still_accepts_new_ids_by_design(self):
        self.repo.words["A"].append(self.new_record())
        self.repo.save()
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("thêm 1", out)
        self.assertNotIn("không toàn vẹn", out)

    # ---- further hardening
    def test_reviewed_edit_with_consistent_metadata_is_accepted(self):
        # Editing baseline-ids together with its metadata is a reviewed Git change, not tampering.
        doc = self.load()
        doc["ids"].remove("bravo-n")
        self.fix_metadata(doc)
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("thêm 1", out)

    def test_wrong_schema_version(self):
        doc = self.load()
        doc["schemaVersion"] = 2
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("schemaVersion", out)

    def test_ids_must_be_a_list_of_strings(self):
        doc = self.load()
        doc["ids"] = "alpha-n"
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("ids phải là mảng", out)

    def test_corrupt_json(self):
        self.ids_path.write_text("{not json", encoding="utf-8")
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)
        self.assertIn("không đọc được", out)

    def test_boolean_count_is_rejected(self):
        doc = self.load()
        doc["count"] = True
        self.save(doc)
        code, out = self.repo.run()
        self.assertEqual(code, 1, out)

    # ---- --update-ids must not be a way to hide damage
    def test_update_ids_refuses_on_corrupt_file_and_leaves_it_untouched(self):
        doc = self.load()
        doc["idSetSha256"] = "0" * 64
        self.save(doc)
        before = file_sha(self.ids_path)
        self.repo.words["A"].append(self.new_record())
        self.repo.save()
        code, out = self.repo.run("--update-ids")
        self.assertEqual(code, 1, out)
        self.assertEqual(before, file_sha(self.ids_path))

    def test_update_ids_accepts_pure_additions_and_result_validates(self):
        self.repo.words["A"].append(self.new_record())
        self.repo.save()
        code, out = self.repo.run("--update-ids")
        self.assertEqual(code, 0, out)
        doc = self.load()
        self.assertEqual(doc["count"], 3)
        self.assertEqual(doc["idSetSha256"], sha_of(doc["ids"]))
        code, out = self.repo.run()
        self.assertEqual(code, 0, out)
        self.assertIn("thêm 0", out)

    def test_update_ids_refuses_when_ids_went_missing(self):
        self.repo.words["B"] = []
        self.repo.save()
        before = file_sha(self.ids_path)
        code, out = self.repo.run("--update-ids")
        self.assertEqual(code, 1, out)
        self.assertEqual(before, file_sha(self.ids_path))


if __name__ == "__main__":
    unittest.main()
