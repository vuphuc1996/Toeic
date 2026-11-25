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
        app_stylesheet = re.search(r'href="(\\./assets/css/app\\.css(?:\\?[^"]*)?)"', HTML)
        design_stylesheet = re.search(r'href="(\\./assets/css/design-system\\.css(?:\\?[^"]*)?)"', HTML)
        self.assertIsNotNone(app_stylesheet, "Feature stylesheet must be linked")
        self.assertIsNotNone(design_stylesheet, "Design-system stylesheet must be linked")
        self.assertLess(app_stylesheet.start(), design_stylesheet.start())
        # Version query parameters are required for release cache coherence.
        self.assertIn("?v=", app_stylesheet.group(1))
        self.assertIn("?v=", design_stylesheet.group(1))

    def test_shared_type_scale_and_system_font_stack_are_defined(self):
        self.assertIn("--ds-text:", CSS)
        self.assertIn("-apple-system", CSS)
        self.assertIn("Roboto", CSS)
        self.assertIn("Noto Sans", CSS)

    def test_phone_uses_safe_area_aware_bottom_navigation(self):
        self.assertRegex(CSS, r"@media \(max-width: 640px\)[\s\S]*?env\(safe-area-inset-bottom\)")
        self.assertRegex(CSS, r"grid-template-columns: repeat\(5, minmax\(0, 1fr\)\)")

    def test_tablet_landscape_uses_sidebar_while_portrait_uses_phone_navigation(self):
        self.assertRegex(CSS, r"@media \(min-width: 641px\) and \(max-width: 850px\)[\s\S]*?\.mobile-bottom-nav \{ display: none")
        portrait = re.search(r"@media screen and \(orientation: portrait\) and \(min-width: 641px\) and \(max-width: 850px\) \{([\s\S]*?)\n\}", CSS)
        self.assertIsNotNone(portrait)
        self.assertIn(".sidebar { display: none; }", portrait.group(1))
        self.assertIn(".mobile-bottom-nav {", portrait.group(1))
        self.assertIn("display: grid;", portrait.group(1))
        self.assertIn("grid-template-columns: repeat(5, minmax(0, 1fr));", portrait.group(1))

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
        self.assertIn(".modal-layer:not([hidden]) .modal { animation: ds-modal-in 220ms", CSS)
        reduce_block = CSS.split("@media (prefers-reduced-motion: reduce)", 1)[1]
        self.assertIn("animation-duration: .01ms !important", reduce_block)

    def test_design_system_is_precached_by_service_worker(self):
        self.assertIn("./assets/css/design-system.css", SW)
        self.assertIn("design-system.css", SW)

    def test_ui_controls_have_a_consistent_accessible_focus_ring(self):
        self.assertIn(":focus-visible", CSS)
        self.assertIn("--ds-focus", CSS)

    def test_legacy_metadata_uses_the_shared_caption_role(self):
        self.assertIn("Content floor: important text never inherits a legacy micro-size", CSS)
        self.assertIn("font-size: max(var(--ds-font-caption), 1em) !important", CSS)
        self.assertRegex(CSS, r"\.mobile-bottom-nav button small\s*\{\s*font-size: 12px !important")

    def test_compact_buttons_use_the_canonical_button_role(self):
        self.assertIn(".pronunciation-toolbar .secondary-button", CSS)
        self.assertIn("font-size: var(--ds-font-button) !important", CSS)
        self.assertIn("min-height: var(--ds-touch-target)", CSS)

    def test_touch_icon_actions_use_full_target_size(self):
        self.assertRegex(CSS, r"@media \(pointer: coarse\)[\s\S]*?\.icon-action,[\s\S]*?min-width: 44px; min-height: 44px")
        self.assertIn(".alphabet-chip { min-width: 44px; min-height: 44px; }", CSS)


    def test_requested_learning_sections_use_the_shared_readable_scale(self):
        for token in ("--ds-font-card-title", "--ds-font-section-title", "--ds-font-caption"):
            self.assertIn(token, CSS)
        for selector in (".objective-progress-top strong", ".objective-progress-meta", ".foundation-intro-header h2", ".foundation-level-picker select", ".practice-mode-tile strong", ".practice-mode-tile small", ".mock-mode-label", ".mock-mode-card > p"):
            self.assertIn(selector, CSS, selector)

    def test_application_wide_typography_floor_covers_legacy_feature_copy(self):
        self.assertIn("Content floor: important text never inherits a legacy micro-size", CSS)
        self.assertIn("font-size: max(var(--ds-font-support), 1em) !important", CSS)
        self.assertIn("font-size: max(var(--ds-font-caption), 1em) !important", CSS)
        for selector in (".objective-progress-meta", ".practice-mode-tile small", ".mock-mode-label", ".mock-exam-timer span", ".mock-result-note", ".mobile-bottom-nav button small"):
            self.assertIn(selector, CSS, selector)

    def test_foundation_intro_resets_legacy_two_column_template(self):
        self.assertRegex(CSS, r"\.foundation-intro\.panel\s*\{[^}]*grid-template-columns:\s*minmax\(0,\s*1fr\)")

    def test_practice_and_mock_cards_reflow_without_microcopy(self):
        self.assertIn("grid-template-columns: repeat(auto-fit, minmax(min(100%, 225px), 1fr))", CSS)
        self.assertRegex(CSS, r"@media \(max-width: 1100px\)[\s\S]*?\.mock-mode-grid \{ grid-template-columns: repeat\(2, minmax\(0, 1fr\)\); ")
        self.assertRegex(CSS, r"\.practice-mode-tile small \{ font-size: var\(--ds-font-support\) !important")

if __name__ == "__main__":
    unittest.main()
