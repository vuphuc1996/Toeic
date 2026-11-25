"""Integration tests for the dependency-free Git commit-readiness audit."""
from __future__ import annotations

import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SOURCE_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = SOURCE_ROOT / "tools/audit-git-commit-readiness.py"
spec = importlib.util.spec_from_file_location("git_commit_readiness_audit", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

GITIGNORE = """__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.tox/
.venv/
venv/
.coverage
.coverage.*
coverage.xml
logs/
*.log
.DS_Store
Thumbs.db
*.zip
*.sha256
*.tar
*.tar.gz
"""
GITATTRIBUTES = """* text=auto eol=lf
*.jpg binary
"""


class GitCommitReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
        (self.root / ".gitattributes").write_text(GITATTRIBUTES, encoding="utf-8")
        (self.root / "index.html").write_text("<html>ok</html>\n", encoding="utf-8")
        (self.root / "sw.js").write_text("const ok = true;\n", encoding="utf-8")
        (self.root / "tools").mkdir()
        (self.root / "tools/audit-git-commit-readiness.py").write_text("# audit\n", encoding="utf-8")
        (self.root / "assets/listening").mkdir(parents=True)
        (self.root / "assets/listening/part1-office-cleaning.jpg").write_bytes(b"\xff\xd8\xff\xd9")
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Git Audit Test")
        self.git("config", "user.email", "git-audit@example.invalid")
        self.git("add", "-A")
        self.git("commit", "-m", "baseline")
        (self.root / "CHANGELOG.md").write_text("# Test baseline\n", encoding="utf-8")
        self.git("add", "CHANGELOG.md")
        self.git("commit", "-m", "second baseline commit")

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args, check=True):
        return subprocess.run(
            ["git", *args], cwd=self.root, capture_output=True, text=True,
            check=check,
        )

    def run_audit(self, *args):
        output = io.StringIO()
        argv = [str(SCRIPT), *args]
        with patch.object(audit, "ROOT", self.root), patch.object(sys, "argv", argv), redirect_stdout(output):
            code = audit.main()
        return code, output.getvalue()

    def test_clean_commit_passes(self):
        code, output = self.run_audit("--require-clean")
        self.assertEqual(code, 0, output)
        self.assertIn("RESULT: PASS", output)

    def test_dirty_tracked_file_fails_clean_mode(self):
        (self.root / "index.html").write_text("<html>changed</html>\n", encoding="utf-8")
        code, output = self.run_audit("--require-clean")
        self.assertEqual(code, 1)
        self.assertIn("working tree is not clean", output)

    def test_staged_change_passes_staged_mode(self):
        (self.root / "index.html").write_text("<html>staged</html>\n", encoding="utf-8")
        self.git("add", "index.html")
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 0, output)

    def test_unstaged_change_fails_staged_mode(self):
        (self.root / "index.html").write_text("<html>staged</html>\n", encoding="utf-8")
        self.git("add", "index.html")
        (self.root / "index.html").write_text("<html>not staged</html>\n", encoding="utf-8")
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 1)
        self.assertIn("unstaged working-tree change remains", output)

    def test_untracked_file_fails_staged_mode(self):
        (self.root / "new-file.txt").write_text("untracked\n", encoding="utf-8")
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 1)
        self.assertIn("untracked file is not part", output)


    def test_committed_trailing_whitespace_in_latest_commit_fails(self):
        (self.root / "docs").mkdir()
        (self.root / "docs/trailing.md").write_text("new line with space \n", encoding="utf-8")
        self.git("add", "docs/trailing.md")
        self.git("commit", "-m", "introduce whitespace")
        code, output = self.run_audit("--require-clean")
        self.assertEqual(code, 1)
        self.assertIn("whitespace/conflict-marker check failed", output)

    def test_staged_trailing_whitespace_fails(self):
        (self.root / "index.html").write_text("<html>bad</html>   \n", encoding="utf-8")
        self.git("add", "index.html")
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 1)
        self.assertIn("whitespace/conflict-marker check failed", output)

    def test_case_insensitive_path_collision_fails(self):
        folder = self.root / "assets/case-test"
        folder.mkdir(parents=True)
        (folder / "Entry.js").write_text("export {};\n", encoding="utf-8")
        (folder / "entry.js").write_text("export {};\n", encoding="utf-8")
        self.git("add", "-A")
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 1)
        self.assertIn("case-insensitive path collision", output)

    def test_windows_reserved_path_fails(self):
        bad = self.root / "tools/CON.py"
        bad.write_text("# invalid on windows\n", encoding="utf-8")
        self.git("add", str(bad.relative_to(self.root)))
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 1)
        self.assertIn("Windows reserved device name", output)

    def test_release_artifact_cannot_be_committed(self):
        (self.root / "release.zip").write_bytes(b"zip")
        self.git("add", "-f", "release.zip")
        code, output = self.run_audit("--staged")
        self.assertEqual(code, 1)
        self.assertIn("release/package artifact must not be committed", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
