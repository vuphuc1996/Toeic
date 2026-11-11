"""Cross-device design-system regression tests."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/design-system.css").read_text(encoding="utf-8")
APP_CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")
SW = (ROOT / "sw.js").read_text(encoding="utf-8")

class DesignSystemTests(unittest.TestCase):
    def test_desktop_sidebar_footer_stays_visible_and_navigation_scrolls(self):
        self.assertRegex(APP_CSS, r"@media \(min-width: 851px\)[\s\S]*?\.side-nav \{[\s\S]*?overflow-y: auto;[\s\S]*?\.sidebar-bottom \{[\s\S]*?flex: 0 0 auto;")
        self.assertRegex(APP_CSS, r"\.sidebar-bottom \{[\s\S]*?margin-top: auto;")

    def test_short_laptop_viewports_use_compact_sidebar_without_hiding_status(self):
        compact = re.search(r"@media \(min-width: 851px\) and \(max-height: 820px\) \{([\s\S]*?)\n\}", APP_CSS)
        self.assertIsNotNone(compact)
        self.assertIn(".local-state { padding: 8px 10px; }", compact.group(1))
        self.assertIn(".sidebar-version { padding-top: 7px;", compact.group(1))
        self.assertNotIn("display: none", compact.group(1))

    def test_design_system_stylesheet_is_linked_after_feature_styles(self):
        self.assertIn('href="./assets/css/app.css"', HTML)
        self.assertIn('href="./assets/css/design-system.css"', HTML)
        self.assertLess(HTML.index('href="./assets/css/app.css"'), HTML.index('href="./assets/css/design-system.css"'))

    def test_shared_type_scale_and_system_font_stack_are_defined(self):
        self.assertIn("--ds-text:", CSS)
        self.assertIn("-apple-system", CSS)
        self.assertIn("Roboto", CSS)
        self.assertIn("Noto Sans", CSS)

    def test_phone_uses_safe_area_aware_bottom_navigation(self):
        self.assertRegex(CSS, r"@media \(max-width: 640px\)[\s\S]*?env\(safe-area-inset-bottom\)")
        self.assertRegex(CSS, r"grid-template-columns: repeat\(5, minmax\(0, 1fr\)\)")

    def test_tablet_does_not_use_phone_bottom_navigation(self):
        self.assertRegex(CSS, r"@media \(min-width: 641px\) and \(max-width: 850px\)[\s\S]*?\.mobile-bottom-nav \{ display: none !important")

    def test_compact_tablet_rail_hides_wordmark_and_centers_icon_controls(self):
        self.assertRegex(CSS, r"@media \(min-width: 641px\) and \(max-width: 850px\)[\s\S]*?\.brand-copy,[\s\S]*?display: none !important")
        self.assertRegex(CSS, r"\.nav-item \{ width: 100%; min-height: 48px; justify-content: center")

    def test_small_laptop_topbar_is_compacted_before_desktop_breakpoint(self):
        self.assertRegex(CSS, r"@media \(min-width: 851px\) and \(max-width: 1199px\)[\s\S]*?\.global-search \{ width: clamp\(140px, 18vw, 210px\)")

    def test_touch_controls_and_reduced_motion_are_supported(self):
        self.assertIn("@media (pointer: coarse)", CSS)
        self.assertIn("@media (prefers-reduced-motion: reduce)", CSS)
        self.assertIn("--ds-touch: 44px", CSS)

    def test_page_and_modal_effects_are_short_and_reduced_motion_safe(self):
        self.assertIn(".page.active { animation: ds-page-in", CSS)
        self.assertIn(".modal-backdrop:not([hidden]) .modal { animation: ds-modal-in 220ms", CSS)
        reduce_block = CSS.split("@media (prefers-reduced-motion: reduce)", 1)[1]
        self.assertIn("animation-duration: .01ms !important", reduce_block)

    def test_design_system_is_precached_by_service_worker(self):
        self.assertIn("./assets/css/design-system.css", SW)
        self.assertIn("design-system.css", SW)

    def test_ui_controls_have_a_consistent_accessible_focus_ring(self):
        self.assertIn(":focus-visible", CSS)
        self.assertIn("--ds-focus", CSS)

    def test_legacy_micro_labels_have_a_readability_floor(self):
        self.assertIn("Readability floor", CSS)
        self.assertIn("font-size: max(11px, .86em) !important", CSS)
        self.assertRegex(CSS, r"\.mobile-bottom-nav button small\s*\{\s*font-size: 11px")

    def test_compact_buttons_are_not_shrunk_to_microtext(self):
        self.assertRegex(CSS, r"\.pronunciation-toolbar \.secondary-button\s*\{\s*font-size: 14px !important")
        self.assertIn("min-height: var(--ds-touch)", CSS)

    def test_touch_icon_actions_use_full_target_size(self):
        self.assertRegex(CSS, r"@media \(pointer: coarse\)[\s\S]*?\.icon-action,[\s\S]*?min-width: 44px; min-height: 44px")
        self.assertIn(".alphabet-chip { min-width: 44px; min-height: 44px; }", CSS)

if __name__ == "__main__":
    unittest.main()
