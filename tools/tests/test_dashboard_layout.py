"""Static regression tests for the TOEIC dashboard diagnostic layout."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")


class DashboardLayoutTests(unittest.TestCase):
    def test_diagnostics_section_is_not_wrapped_in_generic_panel_frame(self):
        match = re.search(r'<section class="([^"]*)" id="toeicProgressPanel"', HTML)
        self.assertIsNotNone(match, "dashboard diagnostic section is missing")
        classes = set(match.group(1).split())
        self.assertIn("toeic-progress-panel", classes)
        self.assertNotIn("panel", classes)

    def test_diagnostics_has_a_clear_title_and_description_hierarchy(self):
        self.assertIn('class="toeic-progress-header"', HTML)
        self.assertIn('<p class="eyebrow">TOEIC LEARNING DIAGNOSTICS</p>', HTML)
        self.assertIn('<h2>Tiến độ theo 7 Parts</h2>', HTML)
        self.assertIn('class="toeic-progress-description"', HTML)

    def test_listening_and_reading_groups_have_separate_mount_points(self):
        self.assertIn('id="toeicListeningParts"', HTML)
        self.assertIn('id="toeicReadingParts"', HTML)
        self.assertIn('aria-label="Listening Part 1 đến 4"', HTML)
        self.assertIn('aria-label="Reading Part 5 đến 7"', HTML)

    def test_priority_recommendation_is_announced_accessibly(self):
        self.assertRegex(HTML, r'id="toeicPriorityText"[^>]*role="status"[^>]*aria-live="polite"')

    def test_layout_has_tablet_and_mobile_breakpoints(self):
        self.assertIn('@media(max-width:900px){.toeic-progress-columns{grid-template-columns:1fr', CSS)
        self.assertIn('@media(max-width:600px){.toeic-progress-panel', CSS)
        self.assertIn('.toeic-progress-group:last-child .toeic-part-grid{grid-template-columns:repeat(2,minmax(0,1fr))', CSS)

    def test_part_cards_prevent_grid_overflow_and_have_keyboard_focus(self):
        self.assertRegex(CSS, r'\.toeic-part-card\{[^}]*min-width:0')
        self.assertIn('.toeic-part-card:focus-visible', CSS)


if __name__ == "__main__":
    unittest.main()
