"""Security and determinism tests for release/test fingerprint scopes."""
from __future__ import annotations
import json
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
            json.dumps({
                "schemaVersion": 1,
                "exclude_directories": ["__pycache__"],
                "exclude_directory_prefixes": [],
                "exclude_paths": ["logs"],
                "exclude_patterns": [
                    "docs/reports/TEST_REPORT_*.md",
                    "docs/reports/TOEIC_LISTENING_READINESS_v*.md",
                    "docs/reports/TOEIC_EDITORIAL_EVIDENCE_AUDIT_v*.md",
                    "docs/reports/TOEIC_DISTRACTOR_AUDIT_v*.md",
                    "docs/reports/TOEIC_INDEPENDENT_REVIEW_QUEUE_v*.md",
                    "docs/reports/TOEIC_CONTENT_COVERAGE_v*.md",
                    "docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v*.md",
                    "docs/reports/MAJOR_RELEASE_QUALITY_AUDIT_v*.md",
                    "docs/reports/LEARNING_OUTCOME_EVIDENCE_MATRIX_v*.md",
                    "docs/reports/major-release-quality-audit-v*.json",
                    "docs/reports/GITHUB_ACTIONS_SHELL_REPLAY_v*.md",
                    "docs/reports/RELATED_GLOSSARY_BACKLOG.md",
                    "docs/reports/related-glossary-backlog.json",
                    "docs/reports/PYTHON_TEST_SHARDS_v*.md",
                    "docs/reports/PYTHON_TEST_SHARDS_v*.json",
                    "docs/reports/CROSS_MODULE_AUDIT_v*.md",
                    "docs/reports/IPAD_RESPONSIVE_ACCEPTANCE_v*.md",
                    "docs/reports/RELATED_GLOSSARY_QUALITY_v*.md",
                    "docs/reports/RELATED_GLOSSARY_CANDIDATES_v*.md",
                    "docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v*.md",
                    "docs/reports/RELATED_GLOSSARY_ENRICHMENT_QUEUE_v*.json",
                    "docs/reports/visual-evidence/v*/*",
                ],
                "exclude_suffixes": [".log", ".pyc"],
                "include_file_metadata": ["relative_path", "kind", "size", "mode", "content_sha256"],
                "timestamps_in_fingerprint": False,
                "owner_metadata_in_fingerprint": False,
                "symlink_policy": "reject_outside",
            }),
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
            generated = [
                "TEST_REPORT_v2.95.46.md",
                "TOEIC_LISTENING_READINESS_v2.95.46.md",
                "TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.95.46.md",
                "TOEIC_DISTRACTOR_AUDIT_v2.95.46.md",
                "TOEIC_INDEPENDENT_REVIEW_QUEUE_v2.95.46.md",
                "TOEIC_CONTENT_COVERAGE_v2.95.46.md",
                "FOUNDATION_A2_ASSESSMENT_QUALITY_v2.95.46.md",
                "MAJOR_RELEASE_QUALITY_AUDIT_v2.95.46.md",
                "LEARNING_OUTCOME_EVIDENCE_MATRIX_v2.95.46.md",
                "major-release-quality-audit-v2.95.46.json",
                "RELATED_GLOSSARY_BACKLOG.md",
                "GITHUB_ACTIONS_SHELL_REPLAY_v2.95.46.md",
                "related-glossary-backlog.json",
            ]
            for name in generated:
                (reports / name).write_text("generated evidence", encoding="utf-8")
            self.assertEqual(before, source_release_fingerprint(root)["fingerprint"])
            (reports / "EDITORIAL_POLICY.md").write_text("governance source", encoding="utf-8")
            self.assertNotEqual(before, source_release_fingerprint(root)["fingerprint"])

    def test_python_shard_and_rendered_visual_evidence_are_excluded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.make_root(directory)
            reports = root / "docs/reports"
            visuals = reports / "visual-evidence/v2.95.46"
            visuals.mkdir(parents=True)
            before = source_release_fingerprint(root)["fingerprint"]
            generated = {
                "PYTHON_TEST_SHARDS_v2.95.46.md": "generated shard report",
                "PYTHON_TEST_SHARDS_v2.95.46.json": "generated shard json",
                "CROSS_MODULE_AUDIT_v2.95.46.md": "cross-module evidence",
                "IPAD_RESPONSIVE_ACCEPTANCE_v2.95.46.md": "viewport evidence",
                "RELATED_GLOSSARY_QUALITY_v2.95.46.md": "quality evidence",
                "RELATED_GLOSSARY_CANDIDATES_v2.95.46.md": "candidate evidence",
                "RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.46.md": "queue evidence",
                "RELATED_GLOSSARY_ENRICHMENT_QUEUE_v2.95.46.json": "queue json",
            }
            for name, content in generated.items():
                (reports / name).write_text(content, encoding="utf-8")
            (visuals / "ipad-portrait.jpg").write_bytes(b"rendered screenshot evidence")
            self.assertEqual(before, source_release_fingerprint(root)["fingerprint"])
            (reports / "EDITORIAL_POLICY.md").write_text("governance source", encoding="utf-8")
            self.assertNotEqual(before, source_release_fingerprint(root)["fingerprint"])


if __name__ == "__main__":
    unittest.main()
