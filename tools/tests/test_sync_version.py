import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from helpers import SYNC, run_tool

INDEX = (
    "<title>TOEIC Dictionary v{v} – Flashcard Learning</title>\n"
    '<div class="sidebar-version">Phase 5 · v{v} · GitHub-only</div>\n'
    "<p><strong>GitHub-only v{v}:</strong> note</p>\n"
    "<span>GitHub-only · v{v}</span>\n"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SyncVersionTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "docs").mkdir(parents=True, exist_ok=True)
        self.build("1.2.3")

    def build(self, v, readme=None, master=None, sw=None, index=None, changelog=None):
        (self.root / "data").mkdir(exist_ok=True)
        (self.root / "docs").mkdir(exist_ok=True)
        (self.root / "data" / "manifest.json").write_text(json.dumps({"version": v, "x": 1}, indent=2) + "\n", encoding="utf-8")
        (self.root / "sw.js").write_text(sw or f"const VERSION = '{v}'; // @version\n", encoding="utf-8")
        (self.root / "index.html").write_text(index or INDEX.format(v=v), encoding="utf-8")
        (self.root / "docs" / "README.md").write_text(readme or f"# TOEIC Dictionary v{v}\n\ntext v0.0.1 stays\n", encoding="utf-8")
        (self.root / "docs" / "MASTER_STATUS.md").write_text(
            master or f"- **Phiên bản mã nguồn đang kiểm kê:** v{v} (draft)\nold v9.9.9 stays\n", encoding="utf-8")
        (self.root / "docs" / "CHANGELOG.md").write_text(changelog or f"# Changelog\n\n## v{v} — x\n- y\n\n## v0.1.0 — old\n", encoding="utf-8")

    def tool(self, *args):
        return run_tool(SYNC, "--root", str(self.root), *args)

    def hashes(self):
        return {p.name: sha(p) for p in self.root.rglob("*") if p.is_file()}

    def test_in_sync_passes(self):
        code, out = self.tool("--check")
        self.assertEqual(code, 0, out)
        self.assertIn("PASS", out)

    def test_mismatch_is_listed_and_fails(self):
        self.build("1.2.3", readme="# TOEIC Dictionary v1.0.0\n")
        code, out = self.tool("--check")
        self.assertEqual(code, 1)
        self.assertIn("LỆCH] docs/README.md title: 1.0.0", out)

    def test_changelog_missing_entry_fails_check(self):
        self.build("1.2.3", changelog="# Changelog\n\n## v0.1.0\n")
        code, out = self.tool("--check")
        self.assertEqual(code, 1)
        self.assertIn("docs/CHANGELOG.md", out)

    def test_dry_run_changes_nothing(self):
        self.build("1.2.3", readme="# TOEIC Dictionary v1.0.0\n")
        before = self.hashes()
        code, out = self.tool("--dry-run")
        self.assertEqual(code, 0, out)
        self.assertIn("1.0.0 -> 1.2.3", out)
        self.assertEqual(before, self.hashes())

    def test_apply_edits_only_markers_then_check_passes(self):
        self.build("1.2.3", readme="# TOEIC Dictionary v1.0.0\n\ntext v0.0.1 stays\n",
                   master="- **Phiên bản mã nguồn đang kiểm kê:** v1.1.0 (draft)\nold v9.9.9 stays\n")
        changelog_before = sha(self.root / "docs" / "CHANGELOG.md")
        code, out = self.tool("--apply")
        self.assertEqual(code, 0, out)
        self.assertEqual((self.root / "docs" / "README.md").read_text(encoding="utf-8"),
                         "# TOEIC Dictionary v1.2.3\n\ntext v0.0.1 stays\n")
        self.assertIn("old v9.9.9 stays", (self.root / "docs" / "MASTER_STATUS.md").read_text(encoding="utf-8"))
        self.assertEqual(changelog_before, sha(self.root / "docs" / "CHANGELOG.md"))
        self.assertEqual(self.tool("--check")[0], 0)

    def test_duplicate_marker_stops_before_writing(self):
        idx = INDEX.format(v="1.2.3") + "<title>TOEIC Dictionary v1.2.3 – again</title>\n"
        self.build("1.2.3", index=idx, readme="# TOEIC Dictionary v1.0.0\n")
        before = self.hashes()
        code, out = self.tool("--apply")
        self.assertEqual(code, 2, out)
        self.assertIn("2 lần", out)
        self.assertEqual(before, self.hashes())

    def test_missing_marker_stops(self):
        self.build("1.2.3", index="<html></html>\n")
        code, out = self.tool("--apply")
        self.assertEqual(code, 2, out)

    def test_legacy_service_worker_layout_is_accepted(self):
        self.build("1.2.3", sw="const CACHE_NAME = 'toeic-vocab-github-only-v1.2.3';\n")
        self.assertEqual(self.tool("--check")[0], 0)

    def test_two_service_worker_layouts_at_once_is_a_structure_error(self):
        self.build("1.2.3", sw="const VERSION = '1.2.3';\nconst CACHE_NAME = 'toeic-vocab-github-only-v1.2.3';\n")
        code, out = self.tool("--check")
        self.assertEqual(code, 2, out)

    def test_set_updates_manifest_and_markers(self):
        (self.root / "docs" / "CHANGELOG.md").write_text("# Changelog\n\n## v1.3.0 — new\n\n## v1.2.3\n", encoding="utf-8")
        code, out = self.tool("--set", "1.3.0", "--apply")
        self.assertEqual(code, 0, out)
        self.assertEqual(json.loads((self.root / "data" / "manifest.json").read_text())["version"], "1.3.0")
        self.assertEqual(self.tool("--check")[0], 0)

    def test_set_with_broken_marker_does_not_touch_manifest(self):
        self.build("1.2.3", index="<html></html>\n")
        before = sha(self.root / "data" / "manifest.json")
        code, out = self.tool("--set", "1.3.0", "--apply")
        self.assertEqual(code, 2, out)
        self.assertEqual(before, sha(self.root / "data" / "manifest.json"))

    def test_apply_preserves_crlf(self):
        self.build("1.2.3", readme="# TOEIC Dictionary v1.0.0\r\n\r\nbody\r\n")
        self.tool("--apply")
        raw = (self.root / "docs" / "README.md").read_bytes()
        self.assertEqual(raw, b"# TOEIC Dictionary v1.2.3\r\n\r\nbody\r\n")


if __name__ == "__main__":
    unittest.main()
