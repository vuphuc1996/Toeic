"""Shared card geometry and Part 1 media frame regression checks."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSS = (ROOT / "assets/css/design-system.css").read_text(encoding="utf-8")
APP_CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
PROFILE = json.loads((ROOT / "design/design-profile.json").read_text(encoding="utf-8"))


class VisualCompositionTests(unittest.TestCase):
    def test_part1_photo_uses_one_shared_frame_ratio_and_cover_behavior(self):
        self.assertEqual(PROFILE["cssVariables"]["--ds-image-ratio"], "4 / 3")
        self.assertIn(".part1-illustration-frame img {", CSS)
        self.assertIn("aspect-ratio: var(--ds-image-ratio);", CSS)
        self.assertIn("object-fit: cover;", CSS)
        self.assertNotIn('img[data-photo-id="part1-photocopier"]', CSS)

    def test_photocopier_image_is_identified_and_attribution_is_preserved(self):
        self.assertIn('data-photo-id="${escapeHtml(item.id)}"', APP)
        self.assertIn('data-photo-id="${escapeHtml(group.unitId)}"', APP)
        self.assertNotIn('data-photo-id="part1-photocopier"', CSS)
        self.assertIn(".mock-part1-frame img {", CSS)
        self.assertIn("part1-photocopier.jpg", (ROOT / "assets/listening/ATTRIBUTION.csv").read_text(encoding="utf-8"))

    def test_learning_and_mock_exam_part1_frames_share_geometry(self):
        self.assertIn(".part1-illustration-frame img {", CSS)
        self.assertIn(".mock-part1-frame img {", CSS)
        self.assertIn("aspect-ratio: var(--ds-image-ratio);", CSS)
        self.assertIn("object-fit: cover;", CSS)
        self.assertNotIn('.mock-part1-frame img[data-photo-id="part1-photocopier"]', CSS)
        self.assertIn(".part1-illustration-frame figcaption,\n.mock-part1-frame figcaption {", CSS)

    def test_learning_cards_share_equal_row_height_and_footer_baseline(self):
        self.assertIn("grid-auto-rows: 1fr;", CSS)
        for selector in (".learning-card-grid", ".foundation-card-grid", ".practice-mode-grid", ".mock-mode-grid", ".objective-progress-grid"):
            self.assertIn(selector, CSS)
        self.assertIn(".learning-card-footer,\n.foundation-card-footer", CSS)
        self.assertIn("margin-top: auto;", CSS)

    def test_long_content_wraps_and_buttons_do_not_force_single_line(self):
        self.assertIn("overflow-wrap: anywhere;", CSS)
        self.assertIn("white-space: normal;", CSS)
        self.assertIn("text-wrap: balance;", CSS)
        self.assertNotIn("overflow: hidden;\n}\n.learning-card h3,", CSS)

    def test_foundation_evidence_chips_use_balanced_grid(self):
        self.assertIn(".foundation-card-evidence {", CSS)
        self.assertIn("grid-template-columns: repeat(2, minmax(0, 1fr));", CSS)
        self.assertIn(".foundation-card-evidence > span {", CSS)

    def test_mock_mode_and_practice_cards_keep_shared_button_baseline(self):
        self.assertIn(".mock-mode-card > .primary-button { margin-top: auto; }", CSS)
        self.assertIn(".practice-mode-tile {", CSS)
        self.assertIn("min-height: 96px;", CSS)

    def test_success_and_error_toasts_are_dismissible_and_accessible(self):
        self.assertIn("toast-close", APP)
        self.assertIn("setAttribute('aria-label','Đóng thông báo')", APP)
        self.assertIn("setAttribute('role',type==='error'?'alert':'status')", APP)
        self.assertIn("addEventListener('click',()=>el.remove())", APP)
        self.assertIn("setTimeout(()=>el.remove(),5000)", APP)
        self.assertIn(".toast-close:focus-visible", APP_CSS)
        self.assertIn(".toast-message", APP_CSS)
        self.assertIn("border-radius:var(--ds-radius-control)", APP_CSS)
        self.assertIn("font-size:var(--ds-font-button)", APP_CSS)
        self.assertIn("color-mix(in srgb,var(--ds-color-surface) 12%,transparent)", APP_CSS)

    def test_responsive_rules_cover_desktop_tablet_and_phone_layouts(self):
        self.assertIn("grid-template-columns: repeat(4, minmax(0, 1fr));", CSS)
        self.assertIn("@media (min-width: 641px) and (max-width: 1100px)", CSS)
        self.assertIn("@media (min-width: 641px) and (max-width: 850px)", CSS)
        self.assertIn("grid-template-columns: repeat(3, minmax(0, 1fr));", CSS)
        self.assertIn("grid-template-columns: repeat(2, minmax(0, 1fr));", CSS)
        self.assertIn("@media (max-width: 640px)", CSS)
        self.assertIn("@media (max-width: 360px)", CSS)


if __name__ == "__main__":
    unittest.main()
