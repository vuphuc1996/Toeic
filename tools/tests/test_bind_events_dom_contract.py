"""Verify all non-optional bindEvents listeners have matching unique DOM nodes."""
from __future__ import annotations
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")


class BindEventsDomContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start = APP.index("function bindEvents(){")
        end = APP.index("\n}\n\n", start)
        cls.bind_block = APP[start:end]
        cls.dom_ids = re.findall(r'\bid="([^"]+)"', HTML)
        cls.id_counts = Counter(cls.dom_ids)
        listener_pattern = r'''\$\(['"]#([^'"]+)['"]\)(\?)?\.addEventListener'''
        cls.listeners = [
            {"id": match.group(1), "optional": bool(match.group(2))}
            for match in re.finditer(listener_pattern, cls.bind_block)
        ]

    def test_bind_events_has_a_discoverable_listener_inventory(self):
        self.assertGreaterEqual(len(self.listeners), 70)
        self.assertGreaterEqual(sum(not item["optional"] for item in self.listeners), 40)

    def test_all_required_listener_targets_exist_in_index_html(self):
        missing = sorted({item["id"] for item in self.listeners if not item["optional"] and self.id_counts[item["id"]] == 0})
        self.assertEqual(missing, [], f"Required bindEvents DOM targets are missing: {missing}")

    def test_listener_targets_do_not_use_duplicated_dom_ids(self):
        duplicated = sorted({item["id"] for item in self.listeners if self.id_counts[item["id"]] > 1})
        self.assertEqual(duplicated, [], f"bindEvents selectors resolve to duplicated DOM ids: {duplicated}")

    def test_single_modal_layer_listener_is_guarded_and_present(self):
        self.assertIn('id="modalLayer"', HTML)
        self.assertRegex(self.bind_block, r"\$\('#modalLayer'\)\?\.addEventListener\('click'")
        self.assertNotIn("$('#modalBackdrop')", self.bind_block)


if __name__ == "__main__":
    unittest.main(verbosity=2)
