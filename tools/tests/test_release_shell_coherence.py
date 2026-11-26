"""Guard against mixed HTML/JavaScript/CSS releases in a cache-first PWA."""
from __future__ import annotations
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
SW = (ROOT / "sw.js").read_text(encoding="utf-8")
MANIFEST = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))


def read_array(name: str):
    match = re.search(rf"const {name} = (\[.*?\]);", SW, re.S)
    if not match:
        raise AssertionError(f"Service Worker {name} array missing")
    return json.loads(match.group(1))


class ReleaseShellCoherenceTests(unittest.TestCase):
    def test_manifest_html_javascript_and_worker_share_one_release(self):
        version = MANIFEST["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"const APP_RELEASE_VERSION = '{version}'", APP)
        self.assertIn(f"const VERSION = '{version}'", SW)
        self.assertIn(f'<meta name="app-release" content="{version}">', HTML)

    def test_entry_document_uses_release_keyed_module_styles_and_manifest(self):
        version = MANIFEST["version"]
        for asset in (
            "./manifest.webmanifest",
            "./assets/css/app.css",
            "./assets/css/design-system.css",
            "./assets/js/app.js",
        ):
            self.assertIn(f'{asset}?__release={version}', HTML, asset)

    def test_every_local_module_edge_is_release_keyed_and_precached(self):
        version = MANIFEST["version"]
        imports = re.findall(r"""\bfrom\s*['\"](\./[^'\"]+\.js)\?__release=([0-9.]+)['\"]""", APP)
        self.assertGreaterEqual(len(imports), 15)
        required = set(read_array("REQUIRED"))
        shell = set(read_array("APP_SHELL"))
        for path, import_version in imports:
            self.assertEqual(import_version, version, path)
            asset_path = "./assets/js/" + path.removeprefix("./")
            versioned = f"{asset_path}?__release={version}"
            self.assertIn(versioned, required, f"not required at install: {versioned}")
            self.assertIn(versioned, shell, f"not in offline app shell: {versioned}")
            self.assertTrue((ROOT / asset_path.removeprefix("./")).is_file(), asset_path)

    def test_all_service_worker_precache_release_keys_match_manifest(self):
        version = MANIFEST["version"]
        keys = re.findall(r"__release=([0-9.]+)", SW)
        self.assertGreaterEqual(len(keys), 30, "expected versioned REQUIRED/APP_SHELL URLs")
        self.assertEqual(set(keys), {version}, "stale or mixed Service Worker precache cache keys")

    def test_versioned_core_assets_are_required_and_offline_available(self):
        version = MANIFEST["version"]
        required = set(read_array("REQUIRED"))
        shell = set(read_array("APP_SHELL"))
        for path in (
            "./manifest.webmanifest",
            "./assets/css/app.css",
            "./assets/css/design-system.css",
            "./assets/js/app.js",
        ):
            versioned = f"{path}?__release={version}"
            self.assertIn(versioned, required)
            self.assertIn(versioned, shell)
            self.assertTrue((ROOT / path.removeprefix("./")).is_file())

    def test_release_data_urls_have_legacy_and_current_worker_cache_keys(self):
        self.assertIn("url.searchParams.set('__release', version)", APP)
        self.assertIn("url.searchParams.set('__shell', version)", APP)
        # The old worker strips only __release, leaving __shell to bypass its
        # stale unversioned data cache. The current worker strips both keys to
        # reuse its own precached canonical data files.
        self.assertIn("cacheUrl.searchParams.delete('__release')", SW)
        self.assertIn("cacheUrl.searchParams.delete('__shell')", SW)

    def test_startup_checks_html_javascript_release_alignment(self):
        self.assertIn('document.querySelector(\'meta[name="app-release"]\')?.content', APP)
        self.assertIn("HTML/JavaScript release mismatch", APP)
        init_start = APP.index("async function init()")
        init_end = APP.index("init();", init_start)
        init = APP[init_start:init_end]
        self.assertLess(init.index("shellRelease!==APP_RELEASE_VERSION"), init.index("bindEvents()"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
