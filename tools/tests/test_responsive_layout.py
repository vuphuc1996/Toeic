"""Regression checks for viewport-first responsive layout behavior."""
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CSS=(ROOT/'assets/css/app.css').read_text(encoding='utf-8')
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
 def test_small_width_and_short_landscape_fallbacks(self):
  self.assertIn('@media(max-width:560px)',CSS)
  self.assertIn('@media(max-width:360px)',CSS)
  self.assertIn('@media(orientation:landscape) and (max-height:520px)',CSS)
 def test_dialogs_fit_dynamic_viewport(self):
  self.assertIn('100dvh',CSS)
  self.assertIn('overscroll-behavior:contain',CSS)
if __name__=='__main__': unittest.main()
