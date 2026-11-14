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

    def test_part1_fallbacks_are_required_and_jpgs_are_optional(self):
        required = self.array("REQUIRED")
        optional = self.array("OPTIONAL")
        for jpg in [p for p in optional if p.endswith(".jpg")]:
            self.assertNotIn(jpg, required)
        svg = [p for p in required if p.startswith("./assets/listening/part1-") and p.endswith(".svg")]
        self.assertEqual(len(svg), 8)

    def test_cache_version_matches_data_manifest(self):
        version = self.manifest["version"]
        self.assertIn(f"const VERSION = '{version}'", self.sw)
        self.assertIn(f"toeic-vocab-github-only-v${{VERSION}}", self.sw)

if __name__ == "__main__":
    unittest.main()
