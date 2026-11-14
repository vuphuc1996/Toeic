"""Regression tests for the two-generation documentation rotation policy."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "rotate-release-files.py"


class ReleaseRotationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "tools").mkdir()
        shutil.copy2(SCRIPT, self.root / "tools" / SCRIPT.name)
        (self.root / "data").mkdir()
        (self.root / "data/manifest.json").write_text(json.dumps({"version": "2.30.0"}), encoding="utf-8")
        (self.root / "docs/archive").mkdir(parents=True)
        (self.root / "docs/archive/PROJECT_HISTORY.md").write_text("# Consolidated Project History\n", encoding="utf-8")
        for folder in ("batches", "reports", "sources"):
            (self.root / "docs" / folder).mkdir()
        self.old_batch = self.root / "docs/batches/OLD_BATCH_v2.28.0.md"
        self.previous_report = self.root / "docs/reports/REPORT_v2.29.0.md"
        self.current_report = self.root / "docs/reports/REPORT_v2.30.0.md"
        self.legacy_source = self.root / "docs/sources/OLD_SOURCE_v2.10.2.md"
        self.old_batch.write_text("# Old Flashcard Batch\n\n- Replaced a legacy interaction.\n- Added an old test.\n", encoding="utf-8")
        self.previous_report.write_text("# Previous release report\n", encoding="utf-8")
        self.current_report.write_text("# Current release report\n", encoding="utf-8")
        self.legacy_source.write_text("# Legacy source audit\n\n- Source URLs reviewed.\n", encoding="utf-8")
        for version in ("2.28.0", "2.29.0", "2.30.0"):
            (self.root / f"V{version}_UPDATE_NOTES.txt").write_text(f"Release v{version}\n", encoding="utf-8")
        (self.root / "assets").mkdir()
        (self.root / "assets/user-photo.jpg").write_bytes(b"keep-me")

    def tearDown(self):
        self.temp.cleanup()

    def run_rotation(self, *args):
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / SCRIPT.name), *args],
            cwd=self.root, text=True, capture_output=True, check=True,
        )

    def test_dry_run_does_not_change_files(self):
        result = self.run_rotation()
        self.assertIn("keep=['2.29.0', '2.30.0']", result.stdout)
        self.assertIn("DRY RUN", result.stdout)
        self.assertTrue(self.old_batch.exists())
        self.assertTrue((self.root / "V2.28.0_UPDATE_NOTES.txt").exists())

    def test_apply_keeps_two_release_generations_and_compacts_history(self):
        result = self.run_rotation("--apply")
        self.assertIn("archived 2 markdown files", result.stdout)
        self.assertFalse(self.old_batch.exists())
        self.assertFalse(self.legacy_source.exists())
        self.assertTrue(self.previous_report.exists())
        self.assertTrue(self.current_report.exists())
        self.assertFalse((self.root / "V2.28.0_UPDATE_NOTES.txt").exists())
        self.assertTrue((self.root / "V2.29.0_UPDATE_NOTES.txt").exists())
        self.assertTrue((self.root / "V2.30.0_UPDATE_NOTES.txt").exists())
        history = (self.root / "docs/archive/PROJECT_HISTORY.md").read_text(encoding="utf-8")
        self.assertIn("OLD_BATCH_v2.28.0.md", history)
        self.assertIn("OLD_SOURCE_v2.10.2.md", history)
        self.assertTrue((self.root / "assets/user-photo.jpg").exists())
        self.assertEqual((self.root / "assets/user-photo.jpg").read_bytes(), b"keep-me")


if __name__ == "__main__":
    unittest.main()
