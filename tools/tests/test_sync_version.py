import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from helpers import SYNC, run_tool

INDEX = (
    "<meta name=\"app-release\" content=\"{v}\">\n"
    "<link rel=\"manifest\" href=\"./manifest.webmanifest?__release={v}\">\n"
    "<link rel=\"stylesheet\" href=\"./assets/css/app.css?__release={v}\">\n"
    "<link rel=\"stylesheet\" href=\"./assets/css/design-system.css?__release={v}\">\n"
    "<script type=\"module\" src=\"./assets/js/app.js?__release={v}\"></script>\n"
    "<title>TOEIC Dictionary v{v} – Flashcard Learning</title>\n"
    '<div class="sidebar-version">Phase 5 · v{v} · GitHub-only</div>\n'
    "<p><strong>TOEIC Dictionary · GitHub Pages product v{v}:</strong> note</p>\n"
    "<span>GitHub Pages product · v{v}</span>\n"
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

    def build(self, v, readme=None, master=None, sw=None, index=None, changelog=None, package_json=None):
        (self.root / "data").mkdir(exist_ok=True)
        (self.root / "docs").mkdir(exist_ok=True)
        (self.root / "data" / "manifest.json").write_text(json.dumps({"version": v, "x": 1}, indent=2) + "\n", encoding="utf-8")
        package_text = package_json or (json.dumps({"name": "toeic-dictionary", "version": v, "private": True}, indent=2) + "\n")
        (self.root / "package.json").write_text(package_text, encoding="utf-8")
        (self.root / "assets" / "js").mkdir(parents=True, exist_ok=True)
        (self.root / "assets" / "js" / "app.js").write_text(f"const APP_RELEASE_VERSION = '{v}';\n", encoding="utf-8")
        (self.root / "sw.js").write_text(sw or f"const VERSION = '{v}'; // @version\n", encoding="utf-8")
        (self.root / "index.html").write_text(index or INDEX.format(v=v), encoding="utf-8")
        readme_text = readme or f"# TOEIC Dictionary v{v}\n\ntext v0.0.1 stays\n"
        newline = "\r\n" if "\r\n" in readme_text else "\n"
        if "Current release test report:" not in readme_text:
            readme_text += f"- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v{v}.md`." + newline
        if "Current command-log index:" not in readme_text:
            readme_text += f"- Current command-log index: `reports/COMMAND_LOG_INDEX_v{v}.md`." + newline
        (self.root / "docs" / "README.md").write_text(readme_text, encoding="utf-8")
        (self.root / "docs" / "versions").mkdir(parents=True, exist_ok=True)
        (self.root / "docs" / "versions" / "CURRENT_VERSION.md").write_text(
            f"# Current Version\n\n- Current source: **v{v}** — current.\n- Release package: `TOEIC_Dictionary_v{v}_FullSource.zip`.\n- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v{v}.md`.\n",
            encoding="utf-8",
        )
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

    def test_package_version_mismatch_is_reported_and_apply_updates_package_json(self):
        package = json.dumps({"name": "toeic-dictionary", "version": "9.9.9", "private": True}, indent=2) + "\n"
        self.build("1.2.3", package_json=package)

        code, out = self.tool("--check")
        self.assertEqual(code, 1, out)
        self.assertIn("LỆCH] package.json version: 9.9.9", out)

        before = self.hashes()
        code, out = self.tool("--dry-run")
        self.assertEqual(code, 0, out)
        self.assertIn("9.9.9 -> 1.2.3", out)
        self.assertEqual(before, self.hashes())

        code, out = self.tool("--apply")
        self.assertEqual(code, 0, out)
        self.assertEqual(json.loads((self.root / "package.json").read_text(encoding="utf-8"))["version"], "1.2.3")
        self.assertEqual(self.tool("--check")[0], 0)

    def test_missing_or_duplicate_package_version_marker_stops_before_writing(self):
        invalid_packages = {
            "missing": '{\n  "name": "toeic-dictionary",\n  "private": true\n}\n',
            "duplicate": ('{\n  "name": "toeic-dictionary",\n  "version": "1.2.3",\n'
                          '  "version": "1.2.3",\n  "private": true\n}\n'),
        }
        for label, package in invalid_packages.items():
            with self.subTest(marker=label):
                self.build("1.2.3", readme="# TOEIC Dictionary v1.0.0\n", package_json=package)
                before = self.hashes()
                code, out = self.tool("--apply")
                self.assertEqual(code, 2, out)
                self.assertIn("package.json version", out)
                self.assertIn("Dừng: chưa ghi file nào.", out)
                self.assertEqual(before, self.hashes())

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
                         "# TOEIC Dictionary v1.2.3\n\ntext v0.0.1 stays\n"
                         "- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v1.2.3.md`.\n"
                         "- Current command-log index: `reports/COMMAND_LOG_INDEX_v1.2.3.md`.\n")
        current_version = (self.root / "docs" / "versions" / "CURRENT_VERSION.md").read_text(encoding="utf-8")
        self.assertIn("Current source: **v1.2.3**", current_version)
        self.assertIn("TOEIC_Dictionary_v1.2.3_FullSource.zip", current_version)
        self.assertIn("TEST_REPORT_TOEIC_Dictionary_v1.2.3.md", current_version)
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

    def test_apply_updates_all_service_worker_precache_release_keys(self):
        sw = (
            "const VERSION = '1.2.3';\n"
            'const REQUIRED = ["./assets/js/app.js?__release=1.0.0"];\n'
            'const APP_SHELL = ["./assets/css/app.css?__release=1.0.0", "./assets/js/app.js?__release=1.0.0"];\n'
        )
        self.build("1.2.3", sw=sw)
        app_path = self.root / "assets" / "js" / "app.js"
        app_path.write_text(
            "const APP_RELEASE_VERSION = '1.2.3';\n"
            "import { A } from './a.js?__release=1.0.0';\n"
            "import { B } from './b.js?__release=1.0.0';\n",
            encoding="utf-8",
        )
        sw_path = self.root / "sw.js"
        sw_path.write_text(sw, encoding="utf-8")
        code, out = self.tool("--check")
        self.assertEqual(code, 1, out)
        self.assertIn("app.js local module import cache keys", out)
        self.assertIn("sw.js release-keyed precache URLs", out)
        code, out = self.tool("--apply")
        self.assertEqual(code, 0, out)
        updated = sw_path.read_text(encoding="utf-8")
        self.assertEqual(updated.count("?__release=1.2.3"), 3)
        self.assertNotIn("?__release=1.0.0", updated)
        app_updated = app_path.read_text(encoding="utf-8")
        self.assertEqual(app_updated.count("?__release=1.2.3"), 2)
        self.assertNotIn("?__release=1.0.0", app_updated)
        self.assertEqual(self.tool("--check")[0], 0)

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
        self.assertEqual(raw, b"# TOEIC Dictionary v1.2.3\r\n\r\nbody\r\n"
                               b"- Current release test report: `reports/TEST_REPORT_TOEIC_Dictionary_v1.2.3.md`.\r\n"
                               b"- Current command-log index: `reports/COMMAND_LOG_INDEX_v1.2.3.md`.\r\n")

    def test_apply_updates_mock_engine_cache_key_when_present(self):
        mock_engine = self.root / "assets" / "js" / "mock-engine.js"
        mock_engine.write_text("import { buildMockQuestionSchedule } from './mock-flow.js?__release=1.0.0';\n", encoding="utf-8")
        code, out = self.tool("--check")
        self.assertEqual(code, 1, out)
        self.assertIn("mock-engine.js local module import cache keys", out)
        code, out = self.tool("--apply")
        self.assertEqual(code, 0, out)
        self.assertIn("mock-flow.js?__release=1.2.3", mock_engine.read_text(encoding="utf-8"))
        self.assertEqual(self.tool("--check")[0], 0)


if __name__ == "__main__":
    unittest.main()
