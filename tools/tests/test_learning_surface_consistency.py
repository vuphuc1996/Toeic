"""Shared visual-system checks for Foundation and Spaced Recall surfaces."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")


class LearningSurfaceConsistencyTests(unittest.TestCase):
    def test_recall_queue_uses_shared_panel_header_and_learning_card_components(self):
        self.assertIn('class="panel recall-queue-panel"', HTML)
        self.assertIn('class="panel-header recall-queue-header"', HTML)
        self.assertIn('class="library-count recall-queue-count"', HTML)
        self.assertIn('class="learning-card recall-queue-item"', APP)
        self.assertIn('data-recall-open=', APP)

    def test_foundation_path_uses_shared_panel_and_learning_card_components(self):
        self.assertIn('class="panel foundation-intro"', HTML)
        self.assertIn('class="learning-card-grid foundation-card-grid"', HTML)
        self.assertIn('class="learning-card foundation-card"', APP)
        self.assertIn('class="page-heading compact-heading"', HTML)

    def test_learning_surface_typography_has_readable_floors(self):
        for selector in (".foundation-card h3", ".foundation-card>p", ".foundation-card-evidence span", ".recall-queue-heading h2", ".recall-queue-item>p"):
            matches = re.findall(re.escape(selector) + r"\s*\{([^}]+)\}", CSS)
            self.assertTrue(matches, selector)
            self.assertIn("clamp(", matches[-1], selector)

    def test_learning_surfaces_use_viewport_and_content_width_breakpoints(self):
        self.assertIn("grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr))", CSS)
        self.assertIn("@media(max-width:760px)", CSS)
        self.assertIn("@media(max-width:380px)", CSS)
        self.assertNotRegex(CSS, r"@media\s*\([^)]*(?:device-width|device-height)")

    def test_recall_list_does_not_expose_internal_stable_ids_as_copy(self):
        block = re.search(r"function renderRecallQueue\(\) \{([\s\S]*?)\n\}", APP)
        self.assertIsNotNone(block)
        self.assertNotIn(">${escapeHtml(item.itemId)}<", block.group(1))
        self.assertIn('data-recall-item="${escapeHtml(item.itemId)}"', block.group(1))


if __name__ == "__main__":
    unittest.main()
