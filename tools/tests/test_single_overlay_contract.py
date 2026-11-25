"""The learning workspace and modal panels share exactly one viewport backdrop."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class SingleOverlayContractTests(unittest.TestCase):
    def test_modal_layer_is_nested_in_learning_focus_backdrop(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        root_start = html.index('id="learningFocusBackdrop"')
        layer_start = html.index('id="modalLayer"')
        root_end = html.index('</div>', layer_start)
        self.assertLess(root_start, layer_start)
        self.assertGreater(root_end, layer_start)
        self.assertNotIn('id="modalBackdrop"', html)
        self.assertNotIn('class="modal-backdrop"', html)
        self.assertEqual(html.count('class="learning-focus-backdrop"'), 1)

    def test_runtime_has_no_second_backdrop_identifier_or_class(self):
        app = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
        css = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")
        design = (ROOT / "assets/css/design-system.css").read_text(encoding="utf-8")
        self.assertNotIn("modalBackdrop", app)
        self.assertNotIn("modal-backdrop", app + css + design)
        self.assertIn("function showModalLayer()", app)
        self.assertIn("function hideModalLayer()", app)
        self.assertIn("body.has-modal-overlay{overflow:hidden}", css)


if __name__ == "__main__":
    unittest.main()
