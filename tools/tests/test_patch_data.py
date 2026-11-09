import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "patch-data.py"


def sha(ids):
    return hashlib.sha256("\n".join(sorted(ids)).encode()).hexdigest()


class PatchDataTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "data/vocabulary").mkdir(parents=True)
        words_a = [{"id": "alpha-n", "word": "alpha", "senses": [{"pos": "n", "definition_en": "old alpha"}], "examples": [{"en": "old sentence", "vi": "old translation"}]}]
        words_b = [{"id": "beta-v", "word": "beta", "senses": [{"pos": "v", "definition_en": "old beta"}], "examples": [{"en": "old beta sentence", "vi": "old beta translation"}]}]
        (self.root / "data/vocabulary/A.json").write_text(json.dumps({"words": words_a}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        (self.root / "data/vocabulary/B.json").write_text(json.dumps({"words": words_b}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        (self.root / "data/manifest.json").write_text(json.dumps({"version": "2.9.8", "letters": [{"letter": "A", "file": "./data/vocabulary/A.json"}, {"letter": "B", "file": "./data/vocabulary/B.json"}]}, indent=2)+"\n", encoding="utf-8")
        self.patch_path = self.root / "patch.json"
        self.patch = {"schemaVersion": 1, "batchId": "test", "baseDataVersion": "2.9.8", "targetDataVersion": "2.9.9", "idSetSha256": sha(["alpha-n", "beta-v"]), "operations": [
            {"id": "alpha-n", "path": "/senses/0/definition_en", "expect": {"old": "old alpha", "pos": "n"}, "new": "new alpha"},
            {"id": "beta-v", "path": "/examples/0/en", "expect": {"old": "old beta sentence", "verbSense": True}, "new": "new beta sentence"}
        ]}
        self.save_patch()

    def tearDown(self):
        self.tmp.cleanup()

    def save_patch(self):
        self.patch_path.write_text(json.dumps(self.patch, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    def run_tool(self, flag):
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), "--patch", str(self.patch_path), flag], text=True, capture_output=True)

    def get_word(self, letter, rid):
        doc=json.loads((self.root/f"data/vocabulary/{letter}.json").read_text(encoding="utf-8"))
        return next(w for w in doc["words"] if w["id"]==rid)

    def test_dry_run_changes_nothing(self):
        before=(self.root/"data/vocabulary/A.json").read_bytes()
        result=self.run_tool("--dry-run")
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        self.assertIn("alpha-n /senses/0/definition_en", result.stdout)
        self.assertEqual(before,(self.root/"data/vocabulary/A.json").read_bytes())

    def test_apply_updates_all_files_and_rollback_restores(self):
        result=self.run_tool("--apply")
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.get_word("A","alpha-n")["senses"][0]["definition_en"],"new alpha")
        self.assertEqual(self.get_word("B","beta-v")["examples"][0]["en"],"new beta sentence")
        manifest=json.loads((self.root/"data/manifest.json").read_text());manifest["version"]="2.9.9"
        (self.root/"data/manifest.json").write_text(json.dumps(manifest),encoding="utf-8")
        result=self.run_tool("--rollback")
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(self.get_word("A","alpha-n")["senses"][0]["definition_en"],"old alpha")
        self.assertEqual(self.get_word("B","beta-v")["examples"][0]["en"],"old beta sentence")

    def test_old_value_mismatch_aborts_without_any_write(self):
        self.patch["operations"][1]["expect"]["old"]="wrong"
        self.save_patch()
        before=[(self.root/f"data/vocabulary/{x}.json").read_bytes() for x in "AB"]
        result=self.run_tool("--apply")
        self.assertNotEqual(result.returncode,0)
        after=[(self.root/f"data/vocabulary/{x}.json").read_bytes() for x in "AB"]
        self.assertEqual(before,after)

    def test_id_set_hash_mismatch_aborts(self):
        self.patch["idSetSha256"]="0"*64;self.save_patch()
        self.assertNotEqual(self.run_tool("--apply").returncode,0)

    def test_wrong_base_version_aborts(self):
        self.patch["baseDataVersion"]="2.9.7";self.save_patch()
        self.assertNotEqual(self.run_tool("--apply").returncode,0)

    def test_duplicate_operation_aborts(self):
        self.patch["operations"].append(dict(self.patch["operations"][0]));self.save_patch()
        self.assertNotEqual(self.run_tool("--apply").returncode,0)

    def test_missing_id_aborts(self):
        self.patch["operations"][0]["id"]="missing-v";self.save_patch()
        self.assertNotEqual(self.run_tool("--apply").returncode,0)

    def test_pos_mismatch_aborts(self):
        self.patch["operations"][0]["expect"]["pos"]="v";self.save_patch()
        self.assertNotEqual(self.run_tool("--apply").returncode,0)

    def test_verb_sense_precondition_accepts_verb_record(self):
        result=self.run_tool("--dry-run")
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)

    def test_verb_sense_precondition_rejects_changed_pos(self):
        doc=json.loads((self.root/"data/vocabulary/B.json").read_text(encoding="utf-8"))
        doc["words"][0]["senses"][0]["pos"]="n"
        (self.root/"data/vocabulary/B.json").write_text(json.dumps(doc),encoding="utf-8")
        before=(self.root/"data/vocabulary/A.json").read_bytes()
        result=self.run_tool("--apply")
        self.assertNotEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertIn("verb-sense mismatch",result.stdout+result.stderr)
        self.assertEqual(before,(self.root/"data/vocabulary/A.json").read_bytes())

    def test_rollback_refuses_to_overwrite_intervening_edit(self):
        self.assertEqual(self.run_tool("--apply").returncode,0)
        manifest=json.loads((self.root/"data/manifest.json").read_text());manifest["version"]="2.9.9"
        (self.root/"data/manifest.json").write_text(json.dumps(manifest),encoding="utf-8")
        doc=json.loads((self.root/"data/vocabulary/A.json").read_text())
        doc["words"][0]["senses"][0]["definition_en"]="manual later edit"
        (self.root/"data/vocabulary/A.json").write_text(json.dumps(doc),encoding="utf-8")
        before=(self.root/"data/vocabulary/B.json").read_bytes()
        result=self.run_tool("--rollback")
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(before,(self.root/"data/vocabulary/B.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
