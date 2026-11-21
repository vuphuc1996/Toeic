import hashlib
import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
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
        self.patch = {"schemaVersion": 1, "batchId": "test", "baseDataVersion": "2.9.8", "targetDataVersion": "2.9.9", "idSetSha256": sha(["alpha-n", "beta-v"]), "allowedPaths": ["/examples/0/en", "/senses/0/definition_en"], "operations": [
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



    def test_repository_patch_files_have_exact_path_allowlists(self):
        repository = SCRIPT.resolve().parents[1]
        patch_files = sorted((repository / "patches").rglob("*.json"))
        self.assertGreater(len(patch_files), 0)
        for patch_file in patch_files:
            with self.subTest(patch=patch_file.relative_to(repository).as_posix()):
                doc = json.loads(patch_file.read_text(encoding="utf-8"))
                expected = sorted({op["path"] for op in doc["operations"]})
                self.assertEqual(doc.get("allowedPaths"), expected)
                self.assertFalse(any(path.split("/", 2)[1] in {"id", "word", "topics"} for path in expected))

    def test_forbidden_root_paths_are_rejected_even_when_listed(self):
        for pointer in ("/id", "/word", "/topics"):
            with self.subTest(pointer=pointer):
                self.patch["operations"][0]["path"] = pointer
                self.patch["allowedPaths"] = [pointer, "/examples/0/en"]
                self.save_patch()
                before = [(self.root/f"data/vocabulary/{x}.json").read_bytes() for x in "AB"]
                result = self.run_tool("--dry-run")
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("Đường dẫn bị cấm", result.stdout + result.stderr)
                after = [(self.root/f"data/vocabulary/{x}.json").read_bytes() for x in "AB"]
                self.assertEqual(before, after)

    def test_operation_outside_allowed_paths_rejects_entire_batch(self):
        self.patch["allowedPaths"] = ["/senses/0/definition_en"]
        self.save_patch()
        before = [(self.root/f"data/vocabulary/{x}.json").read_bytes() for x in "AB"]
        result = self.run_tool("--dry-run")
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("không nằm trong allowedPaths", result.stdout + result.stderr)
        after = [(self.root/f"data/vocabulary/{x}.json").read_bytes() for x in "AB"]
        self.assertEqual(before, after)

    def test_missing_allowed_paths_rejects_batch(self):
        self.patch.pop("allowedPaths")
        self.save_patch()
        result = self.run_tool("--dry-run")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("phải khai báo allowedPaths", result.stdout + result.stderr)

    def test_operation_log_records_dry_run_apply_and_values(self):
        result = self.run_tool("--dry-run")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        log_path = self.root / "logs/patch-data/operations.jsonl"
        rows = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["batchId"], "test")
        self.assertEqual(rows[0]["id"], "alpha-n")
        self.assertEqual(rows[0]["pointer"], "/senses/0/definition_en")
        self.assertEqual(rows[0]["old"], "old alpha")
        self.assertEqual(rows[0]["new"], "new alpha")
        self.assertEqual(rows[0]["result"], "DRY_RUN_PASS")
        self.assertEqual(rows[0]["mode"], "dry-run")
        self.assertIn("recordedAt", rows[0])


    def test_apply_audit_log_records_apply_mode(self):
        result = self.run_tool("--apply")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        log_path = self.root / "logs/patch-data/operations.jsonl"
        rows = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual({row["mode"] for row in rows}, {"apply"})
        self.assertIn("APPLIED", {row["result"] for row in rows})

    def test_rollback_audit_log_records_rollback_mode(self):
        self.assertEqual(self.run_tool("--apply").returncode, 0)
        manifest = json.loads((self.root / "data/manifest.json").read_text(encoding="utf-8"))
        manifest["version"] = "2.9.9"
        (self.root / "data/manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        result = self.run_tool("--rollback")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        log_path = self.root / "logs/patch-data/operations.jsonl"
        rows = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
        rollback_rows = [row for row in rows if row["result"] == "ROLLED_BACK"]
        self.assertTrue(rollback_rows)
        self.assertTrue(all(row["mode"] == "rollback" for row in rollback_rows))

    def test_repository_gitignore_excludes_audit_logs(self):
        repository = SCRIPT.resolve().parents[1]
        if not (repository / ".git").exists():
            self.skipTest("source archive has no Git metadata; gitignore assertion requires a clone")
        gitignore = (repository / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn("logs/", gitignore)
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "logs/patch-data/operations.jsonl"],
            cwd=repository, text=True, capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_final_audit_log_failure_restores_all_files(self):
        spec = importlib.util.spec_from_file_location("patch_data_under_test", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        real_append = module.append_audit_log

        def fail_only_after_write(root, patch, mode, result, error=None):
            if result == "APPLIED":
                raise OSError("simulated final audit log disk failure")
            return real_append(root, patch, mode, result, error)

        before = [(self.root / f"data/vocabulary/{letter}.json").read_bytes() for letter in "AB"]
        argv = [str(SCRIPT), "--root", str(self.root), "--patch", str(self.patch_path), "--apply"]
        with mock.patch.object(module, "append_audit_log", side_effect=fail_only_after_write), mock.patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()) as output:
            result = module.main()

        self.assertEqual(result, 1, output.getvalue())
        after = [(self.root / f"data/vocabulary/{letter}.json").read_bytes() for letter in "AB"]
        self.assertEqual(after, before, "all source files must be restored when the final audit record cannot be written")
        log_path = self.root / "logs/patch-data/operations.jsonl"
        rows = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual({row["result"] for row in rows}, {"VALIDATED", "REJECTED"})
        self.assertTrue(all("recordedAt" in row and row["batchId"] == "test" for row in rows))
        self.assertIn("đã phục hồi nguyên trạng 2 file", output.getvalue())

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
