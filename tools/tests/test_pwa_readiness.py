import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class PWAReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sw = (ROOT / "sw.js").read_text(encoding="utf-8")
        cls.manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))

    def array(self, name):
        match = re.search(rf"const {name} = (\[.*?\]);", self.sw, re.S)
        self.assertIsNotNone(match, f"{name} array missing")
        return json.loads(match.group(1))

    def test_required_and_app_shell_resources_exist(self):
        required = self.array("REQUIRED")
        shell = self.array("APP_SHELL")
        self.assertTrue(set(required).issubset(set(shell)))
        missing = [p for p in shell if p != "./" and not (ROOT / p.removeprefix("./")).is_file()]
        self.assertEqual(missing, [])
        self.assertIn("./data/listening/listening-library.json", required)
        self.assertIn("./assets/js/mock-engine.js", required)
        self.assertIn("./assets/js/practice-progress.js", required)
        self.assertIn("./assets/js/sentence-completion.js", required)
        self.assertIn("./data/practice/part5-sentence-completion.json", required)
        self.assertIn("./data/learning-path/foundation-reading-extended.json", required)

    def test_part1_uses_jpg_only_and_has_no_svg_fallback_assets(self):
        required = self.array("REQUIRED")
        shell = self.array("APP_SHELL")
        optional = self.array("OPTIONAL")
        part1 = [item for item in json.loads((ROOT / "data/listening/listening-library.json").read_text(encoding="utf-8"))["listening"] if item.get("part") == "Part 1"]
        self.assertEqual(len(part1), 9)
        photo_paths = {item.get("photo") for item in part1}
        self.assertEqual(len(photo_paths), len(part1))
        self.assertTrue(all(path and path.startswith("./assets/listening/") and path.endswith(".jpg") for path in photo_paths))
        self.assertTrue(photo_paths.issubset(set(optional)))
        self.assertTrue(all(not item.get("image") for item in part1))
        for resources in (required, shell, optional):
            self.assertFalse([path for path in resources if path.startswith("./assets/listening/part1-") and path.endswith(".svg")])
        listening_assets = ROOT / "assets/listening"
        self.assertEqual(list(listening_assets.glob("part1-*.svg")), [])

    def test_cache_version_matches_data_manifest(self):
        version = self.manifest["version"]
        self.assertIn(f"const VERSION = '{version}'", self.sw)
        self.assertIn(f"toeic-vocab-github-only-v${{VERSION}}", self.sw)

if __name__ == "__main__":
    unittest.main()
