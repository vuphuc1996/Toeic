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
            (self.root / f"V{version}_OVERLAY_MANIFEST.txt").write_text(f"Overlay manifest v{version}\n", encoding="utf-8")
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
        self.assertTrue((self.root / "V2.28.0_OVERLAY_MANIFEST.txt").exists())

    def test_apply_keeps_two_release_generations_and_compacts_history(self):
        result = self.run_rotation("--apply")
        self.assertIn("archived 2 markdown files", result.stdout)
        self.assertFalse(self.old_batch.exists())
        self.assertFalse(self.legacy_source.exists())
        self.assertTrue(self.previous_report.exists())
        self.assertTrue(self.current_report.exists())
        self.assertFalse((self.root / "V2.28.0_UPDATE_NOTES.txt").exists())
        self.assertFalse((self.root / "V2.28.0_OVERLAY_MANIFEST.txt").exists())
        self.assertTrue((self.root / "V2.29.0_UPDATE_NOTES.txt").exists())
        self.assertTrue((self.root / "V2.30.0_UPDATE_NOTES.txt").exists())
        self.assertTrue((self.root / "V2.29.0_OVERLAY_MANIFEST.txt").exists())
        self.assertTrue((self.root / "V2.30.0_OVERLAY_MANIFEST.txt").exists())
        history = (self.root / "docs/archive/PROJECT_HISTORY.md").read_text(encoding="utf-8")
        self.assertIn("OLD_BATCH_v2.28.0.md", history)
        self.assertIn("OLD_SOURCE_v2.10.2.md", history)
        self.assertIn("V2.28.0_OVERLAY_MANIFEST.txt", history)
        self.assertTrue((self.root / "assets/user-photo.jpg").exists())
        self.assertEqual((self.root / "assets/user-photo.jpg").read_bytes(), b"keep-me")



    def test_rotation_uses_explicit_previous_release_ledger(self):
        versions = self.root / "docs/versions"
        versions.mkdir(parents=True)
        (versions / "PREVIOUS_VERSION.md").write_text(
            "# Previous version\n\n- Version: **v2.29.2**\n", encoding="utf-8"
        )
        exact_previous = self.root / "docs/reports/REPORT_v2.29.2.md"
        exact_previous.write_text("# Exact previous release report\n", encoding="utf-8")
        patch_neighbor = self.root / "docs/reports/REPORT_v2.29.0.md"
        patch_neighbor.write_text("# Older patch report\n", encoding="utf-8")
        result = self.run_rotation()
        self.assertIn("keep=['2.29.2', '2.30.0']", result.stdout)
        self.assertIn("REPORT_v2.29.0.md", result.stdout)
        self.assertNotIn("ARCHIVE + RETIRE docs/reports/REPORT_v2.29.2.md", result.stdout)
        self.assertTrue(exact_previous.exists())
        self.assertTrue(patch_neighbor.exists())

    def test_rotation_preserves_historical_docs_referenced_by_active_tests(self):
        required = self.root / "docs/reports/REVIEW_CHECKLIST_v2.28.0.md"
        required.write_text("# Active review handoff\n", encoding="utf-8")
        tests = self.root / "tools/tests"
        tests.mkdir(parents=True)
        (tests / "test_review_reference.py").write_text(
            "CHECKLIST = \"docs/reports/REVIEW_CHECKLIST_v2.28.0.md\"\n",
            encoding="utf-8",
        )
        result = self.run_rotation("--apply")
        self.assertIn("KEEP (referenced by active tests/tools/docs) docs/reports/REVIEW_CHECKLIST_v2.28.0.md", result.stdout)
        self.assertTrue(required.exists())
        self.assertNotIn("REVIEW_CHECKLIST_v2.28.0.md", (self.root / "docs/archive/PROJECT_HISTORY.md").read_text(encoding="utf-8"))

    def test_rotation_preserves_docs_relative_links_from_master_and_readme(self):
        required = self.root / "docs/reports/ACTIVE_HANDOFF_v2.28.0.md"
        required.write_text("# Active handoff linked relative to docs\n", encoding="utf-8")
        (self.root / "docs/MASTER_STATUS.md").write_text(
            "Current handoff: `reports/ACTIVE_HANDOFF_v2.28.0.md`\n", encoding="utf-8"
        )
        (self.root / "docs/CHANGELOG.md").write_text(
            "Historical release reference: `reports/ACTIVE_HANDOFF_v2.28.0.md`\n", encoding="utf-8"
        )
        result = self.run_rotation("--apply")
        self.assertIn("KEEP (referenced by active tests/tools/docs) docs/reports/ACTIVE_HANDOFF_v2.28.0.md", result.stdout)
        self.assertTrue(required.exists())
        history = (self.root / "docs/archive/PROJECT_HISTORY.md").read_text(encoding="utf-8")
        self.assertNotIn("ACTIVE_HANDOFF_v2.28.0.md", history)


    def test_rotation_preserves_pinned_current_unversioned_reports(self):
        manual = self.root / "docs/reports/MANUAL_ACCEPTANCE_CHECKLIST.md"
        backlog = self.root / "docs/reports/RELATED_GLOSSARY_BACKLOG.md"
        manual.write_text("# Current manual acceptance checklist\n", encoding="utf-8")
        backlog.write_text("# Current generated glossary backlog\n", encoding="utf-8")
        result = self.run_rotation("--apply")
        self.assertIn("KEEP (referenced by active tests/tools/docs) docs/reports/MANUAL_ACCEPTANCE_CHECKLIST.md", result.stdout)
        self.assertIn("KEEP (referenced by active tests/tools/docs) docs/reports/RELATED_GLOSSARY_BACKLOG.md", result.stdout)
        self.assertTrue(manual.exists())
        self.assertTrue(backlog.exists())


    def test_rotation_preserves_reports_linked_only_by_changelog_or_master_contract(self):
        changelog_report = self.root / "docs/reports/CHANGELOG_LINK_v2.28.0.md"
        master_report = self.root / "docs/reports/MASTER_LINK_v2.28.0.md"
        changelog_report.write_text("# Referenced only by changelog\n", encoding="utf-8")
        master_report.write_text("# Referenced only by master contract\n", encoding="utf-8")
        (self.root / "docs/CHANGELOG.md").write_text(
            "Historical reference: `reports/CHANGELOG_LINK_v2.28.0.md`\n", encoding="utf-8"
        )
        (self.root / "docs/MASTER_DEVELOPMENT_PROMPT.md").write_text(
            "Contract reference: `reports/MASTER_LINK_v2.28.0.md`\n", encoding="utf-8"
        )
        result = self.run_rotation("--apply")
        self.assertIn("KEEP (referenced by active tests/tools/docs) docs/reports/CHANGELOG_LINK_v2.28.0.md", result.stdout)
        self.assertIn("KEEP (referenced by active tests/tools/docs) docs/reports/MASTER_LINK_v2.28.0.md", result.stdout)
        self.assertTrue(changelog_report.exists())
        self.assertTrue(master_report.exists())

    def test_apply_consolidates_repeated_history_headings(self):
        history_path = self.root / "docs/archive/PROJECT_HISTORY.md"
        history_path.write_text(
            "# Consolidated Project History\n\n"
            "## Newly retired documents\n\n- Older record A\n\n"
            "## Newly retired documents\n\n- Older record B\n",
            encoding="utf-8",
        )
        self.run_rotation("--apply")
        history = history_path.read_text(encoding="utf-8")
        self.assertEqual(history.count("## Newly retired documents"), 1)
        self.assertIn("Older record A", history)
        self.assertIn("Older record B", history)
        self.assertIn("OLD_BATCH_v2.28.0.md", history)


    def test_archived_documents_preserve_full_content_and_original_hash(self):
        old_content = "# Historical detail\n\nA complete test log and provenance record.\n"
        self.old_batch.write_text(old_content, encoding="utf-8")
        self.run_rotation("--apply")
        history = (self.root / "docs/archive/PROJECT_HISTORY.md").read_text(encoding="utf-8")
        self.assertIn("A complete test log and provenance record.", history)
        self.assertIn("ARCHIVED-DOCUMENT: docs/batches/OLD_BATCH_v2.28.0.md SHA256:", history)
        self.assertFalse(self.old_batch.exists())


if __name__ == "__main__":
    unittest.main()
