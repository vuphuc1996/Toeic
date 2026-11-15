"""Tests the canonical design profile and its generated CSS token block."""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILE_PATH = ROOT / "design" / "design-profile.json"
CSS_PATH = ROOT / "assets" / "css" / "design-system.css"


class DesignProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        cls.css = CSS_PATH.read_text(encoding="utf-8")

    def test_profile_defines_all_semantic_design_roles(self):
        self.assertEqual(self.profile["profileId"], "calm-study-blue")
        variables = self.profile["cssVariables"]
        for token in (
            "--ds-font-family", "--ds-font-body", "--ds-font-support",
            "--ds-font-caption", "--ds-font-label", "--ds-font-control",
            "--ds-font-button", "--ds-font-card-title", "--ds-font-section-title",
            "--ds-font-page-title", "--ds-color-canvas", "--ds-color-surface",
            "--ds-color-ink", "--ds-color-muted", "--ds-color-border",
            "--ds-color-brand", "--ds-radius-card", "--ds-radius-panel",
            "--ds-touch-target", "--ds-content-max",
        ):
            self.assertIn(token, variables)

    def test_profile_has_content_first_responsive_widths(self):
        self.assertEqual(self.profile["breakpoints"]["phoneMaxPx"], 640)
        self.assertEqual(self.profile["breakpoints"]["compactTabletMaxPx"], 850)
        widths = self.profile["breakpoints"]["validationWidthsPx"]
        self.assertEqual(widths, sorted(widths))
        self.assertIn(320, widths)
        self.assertIn(1920, widths)

    def test_profile_and_generated_typography_floor_match_the_source_of_truth(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "sync-design-profile.py"), "--check"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_new_modules_are_forced_to_shared_semantic_type_roles(self):
        for token in ("--ds-font-body", "--ds-font-support", "--ds-font-caption",
                      "--ds-font-label", "--ds-font-control", "--ds-font-button",
                      "--ds-font-card-title", "--ds-font-section-title", "--ds-font-page-title"):
            self.assertIn(token, self.css)
        for selector in (".objective-progress-card", ".foundation-card",
                         ".recall-queue-item", ".practice-mode-tile", ".mock-mode-card",
                         ".mock-question-line h4", ".mock-choice-button"):
            self.assertIn(selector, self.css)

    def test_legacy_aliases_use_canonical_profile_tokens(self):
        for declaration in (
            "--font: var(--ds-font-family)",
            "--canvas: var(--ds-color-canvas)",
            "--ink: var(--ds-color-ink)",
            "--muted: var(--ds-color-muted)",
            "--line: var(--ds-color-border)",
        ):
            self.assertIn(declaration, self.css)

    def test_design_document_has_explicit_no_design_islands_governance(self):
        guide = (ROOT / "docs" / "DESIGN_SYSTEM.md").read_text(encoding="utf-8")
        self.assertIn("Visual governance — do not create design islands", guide)
        self.assertIn("design/design-profile.json", guide)
        self.assertIn("12.5 px is the enforced lower limit", guide)
        self.assertIn("DESIGN_LEGACY_FONT_FLOOR", self.css)


if __name__ == "__main__":
    unittest.main()
