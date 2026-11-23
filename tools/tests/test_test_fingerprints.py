"""Security and determinism tests for release/test fingerprint scopes."""
from __future__ import annotations
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from test_fingerprints import environment_fingerprint, source_release_fingerprint, test_input_fingerprint


class TestFingerprintsTests(unittest.TestCase):
    def make_root(self, directory: str) -> Path:
        root = Path(directory)
        (root / "tools").mkdir()
        (root / "tools/source-fingerprint-policy.json").write_text(
            '{"schemaVersion":1,"exclude_directories":["__pycache__"],"exclude_directory_prefixes":[],"exclude_paths":["logs"],"exclude_patterns":["docs/reports/TEST_REPORT_*.md"],"exclude_suffixes":[".log",".pyc"],"include_file_metadata":["relative_path","kind","size","mode","content_sha256"],"timestamps_in_fingerprint":false,"owner_metadata_in_fingerprint":false,"symlink_policy":"reject_outside"}',
            encoding="utf-8",
        )
        (root / "tools/a.py").write_text("one", encoding="utf-8")
        return root

    def test_source_fingerprint_changes_when_file_content_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            before = source_release_fingerprint(root)["fingerprint"]
            (root / "tools/a.py").write_text("two", encoding="utf-8")
            self.assertNotEqual(before, source_release_fingerprint(root)["fingerprint"])

    def test_source_fingerprint_changes_when_executable_mode_changes(self):
        if os.name == "nt":
            self.skipTest("POSIX executable permission bits are unavailable on Windows")
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            before = source_release_fingerprint(root)["fingerprint"]
            target = root / "tools/a.py"
            target.chmod(0o755)
            self.assertNotEqual(before, source_release_fingerprint(root)["fingerprint"])

    def test_generated_logs_are_outside_source_fingerprint_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            before = source_release_fingerprint(root)["fingerprint"]
            (root / "logs").mkdir()
            (root / "logs/output.log").write_text("generated", encoding="utf-8")
            self.assertEqual(before, source_release_fingerprint(root)["fingerprint"])

    def test_symlink_escape_is_rejected(self):
        if not hasattr(os, "symlink"):
            self.skipTest("symlinks unavailable")
        with tempfile.TemporaryDirectory() as directory, tempfile.TemporaryDirectory() as outside:
            root = self.make_root(directory)
            link = root / "tools/external-link"
            try:
                link.symlink_to(Path(outside), target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"cannot create symlink in this environment: {exc}")
            with self.assertRaisesRegex(ValueError, "absolute symbolic link target|escapes approved source root"):
                source_release_fingerprint(root)

    def test_environment_fingerprint_does_not_include_secret_values(self):
        marker = "DO_NOT_LEAK_SECRET_VALUE_93811"
        old = os.environ.get("TOEIC_TEST_SECRET")
        os.environ["TOEIC_TEST_SECRET"] = marker
        try:
            metadata = str(environment_fingerprint()["metadata"])
        finally:
            if old is None:
                os.environ.pop("TOEIC_TEST_SECRET", None)
            else:
                os.environ["TOEIC_TEST_SECRET"] = old
        self.assertNotIn(marker, metadata)

    def test_test_input_fingerprint_binds_modules_and_command_arguments(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            (root / "tools/tests").mkdir()
            (root / "tools/tests/test_a.py").write_text("import unittest\nclass T(unittest.TestCase):\n def test_ok(self): pass\n", encoding="utf-8")
            a = test_input_fingerprint(root, ["tools/tests/test_a.py"], {"args": ["-v"]})
            b = test_input_fingerprint(root, ["tools/tests/test_a.py"], {"args": ["-q"]})
            self.assertNotEqual(a["fingerprint"], b["fingerprint"])


    def test_normalized_unicode_path_collision_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            (root / "tools/café.txt").write_text("nfc", encoding="utf-8")
            (root / "tools/cafe\u0301.txt").write_text("nfd", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "path collision"):
                source_release_fingerprint(root)

    def test_dependency_lockfile_content_is_bound_to_test_input_fingerprint(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            (root / "requirements-test.txt").write_text("pytest==1.0\n", encoding="utf-8")
            a = test_input_fingerprint(root, [], {"args": []})
            (root / "requirements-test.txt").write_text("pytest==2.0\n", encoding="utf-8")
            b = test_input_fingerprint(root, [], {"args": []})
            self.assertNotEqual(a["fingerprint"], b["fingerprint"])


    def test_generated_release_evidence_reports_are_excluded_but_other_docs_are_included(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            reports = root / "docs/reports"
            reports.mkdir(parents=True)
            before = source_release_fingerprint(root)["fingerprint"]
            (reports / "TEST_REPORT_v2.95.46.md").write_text("generated evidence", encoding="utf-8")
            self.assertEqual(before, source_release_fingerprint(root)["fingerprint"])
            (reports / "EDITORIAL_POLICY.md").write_text("governance source", encoding="utf-8")
            self.assertNotEqual(before, source_release_fingerprint(root)["fingerprint"])


if __name__ == "__main__":
    unittest.main()
