"""Release-aware Word Family graph audit report contract."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class WordFamilyGraphAuditTests(unittest.TestCase):
    def test_report_heading_uses_current_manifest_release(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "word-family-audit.md"
            subprocess.run(
                [sys.executable, "tools/audit-word-family-graph.py", "--output", str(output)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            heading = output.read_text(encoding="utf-8").splitlines()[0]
            version = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))["version"]
            self.assertEqual(heading, f"# Word Family Graph Audit — v{version}")


if __name__ == "__main__":
    unittest.main()
