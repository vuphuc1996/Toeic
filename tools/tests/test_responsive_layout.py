"""Regression checks for viewport-first responsive layout behavior."""
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CSS=(ROOT/'assets/css/app.css').read_text(encoding='utf-8')
DESIGN_CSS=(ROOT/'assets/css/design-system.css').read_text(encoding='utf-8')
HTML=(ROOT/'index.html').read_text(encoding='utf-8')
class ResponsiveLayoutTests(unittest.TestCase):
 def test_viewport_meta_and_no_device_inch_assumptions(self):
  self.assertIn('name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"',HTML)
  self.assertIn('viewport-first responsive layout system',CSS)
  self.assertNotRegex(CSS,r'@media\s*\([^)]*(?:device-width|device-height)')
 def test_fluid_intrinsic_layout_and_overflow_protection(self):
  for token in ('--page-gutter:clamp(', 'grid-template-columns:repeat(auto-fit,minmax(', 'overflow-x:clip', 'overflow-wrap:anywhere', 'min-width:0'):
   self.assertIn(token,CSS)
 def test_tablet_compact_navigation_and_safe_areas(self):
  self.assertRegex(CSS,r'@media\(max-width:820px\)\{[\s\S]*?\.sidebar\{display:none\}[\s\S]*?\.mobile-bottom-nav\{display:grid')
  self.assertIn('env(safe-area-inset-bottom)',CSS)
 def test_ipad_portrait_uses_phone_navigation_and_landscape_keeps_desktop_sidebar(self):
  self.assertIn('v2.95.53 — iPad/tablet portrait uses the proven phone navigation model',DESIGN_CSS)
  self.assertRegex(DESIGN_CSS,r'@media screen and \(orientation: portrait\) and \(min-width: 641px\) and \(max-width: 850px\)')
  self.assertRegex(DESIGN_CSS,r'@media screen and \(orientation: portrait\) and \(min-width: 641px\) and \(max-width: 850px\) \{[\s\S]*?\.sidebar \{ display: none; \}[\s\S]*?\.main-area \{[\s\S]*?margin-left: 0;[\s\S]*?\.mobile-bottom-nav \{[\s\S]*?display: grid;[\s\S]*?grid-template-columns: repeat\(5, minmax\(0, 1fr\)\)')
  self.assertIn('border: 0;',DESIGN_CSS[DESIGN_CSS.index('v2.95.53 — iPad/tablet portrait'):])
  self.assertIn('background: transparent;',DESIGN_CSS[DESIGN_CSS.index('v2.95.53 — iPad/tablet portrait'):])
  self.assertIn('env(safe-area-inset-bottom)',DESIGN_CSS)
  self.assertIn('iPad Pro 11-inch (M1) CSS viewport: approximately 834px portrait / 1194px landscape',DESIGN_CSS)
  # The portrait-only query must not match the 1194px landscape viewport.
  self.assertIn('orientation: portrait',DESIGN_CSS)
  self.assertIn('@media (min-width: 851px) and (max-width: 1199px)',DESIGN_CSS)

 def test_small_width_and_short_landscape_fallbacks(self):
  self.assertIn('@media(max-width:560px)',CSS)
  self.assertIn('@media(max-width:360px)',CSS)
  self.assertIn('@media(orientation:landscape) and (max-height:520px)',CSS)
 def test_dialogs_fit_dynamic_viewport(self):
  self.assertIn('100dvh',CSS)
  self.assertIn('overscroll-behavior:contain',CSS)
 def test_mobile_robot_input_prevents_focus_zoom_without_disabling_user_zoom(self):
  self.assertIn('@media (hover:none) and (pointer:coarse)',CSS)
  self.assertRegex(CSS,r'#quickHelp \.robot-chat-form input\{[^}]*font-size:16px!important')
  self.assertRegex(CSS,r'#quickHelp \.robot-chat-form input\{[^}]*min-height:42px')
  self.assertNotRegex(HTML,r'user-scalable\s*=\s*no')
 def test_robot_progress_dashboard_is_responsive_and_accessible(self):
  self.assertIn('.robot-progress-dashboard{',CSS)
  self.assertIn('.robot-progress-track span{',CSS)
  self.assertIn('@media(max-width:430px){.robot-progress-dashboard',CSS)
  self.assertIn("setAttribute('role','progressbar')", (ROOT/'assets/js/app.js').read_text(encoding='utf-8'))

if __name__=='__main__': unittest.main()
