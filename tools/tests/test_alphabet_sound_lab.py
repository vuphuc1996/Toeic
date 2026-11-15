"""Foundation alphabet sound lab schema, UI and offline-shell contract."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "data/learning-path/alphabet-sounds.json").read_text(encoding="utf-8"))
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/design-system.css").read_text(encoding="utf-8")
SW = (ROOT / "sw.js").read_text(encoding="utf-8")


class AlphabetSoundLabTests(unittest.TestCase):
    def test_all_26_letters_are_present_once_in_alphabet_order(self):
        letters = DATA["letters"]
        self.assertEqual([item["letter"] for item in letters], list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertEqual(len({item["id"] for item in letters}), 26)

    def test_every_letter_has_name_example_ipa_and_translation(self):
        for item in DATA["letters"]:
            for field in ("id", "lowercase", "letterNameIpa", "exampleWord", "exampleIpa", "exampleMeaning", "focusSound", "note"):
                self.assertTrue(str(item.get(field, "")).strip(), f"{item.get('letter')}: missing {field}")

    def test_data_explains_that_progress_is_exposure_not_mastery(self):
        policy = DATA["practicePolicy"]
        self.assertEqual(policy["audio"], "browser-speech-synthesis")
        self.assertIn("not pronunciation accuracy or mastery", policy["progressMeaning"])
        self.assertEqual(policy["progressStorageKey"], "toeic:alphabet-sound-progress:v1")

    def test_app_loads_lab_and_keeps_progress_in_separate_local_storage_key(self):
        self.assertIn("alphabet-sounds.json", APP)
        self.assertIn("toeic:alphabet-sound-progress:v1", APP)
        self.assertIn("recordAlphabetSoundPractice", APP)
        self.assertIn("summarizeAlphabetSoundProgress", APP)

    def test_lab_is_attached_only_to_alphabet_foundation_lesson(self):
        self.assertIn("id==='pa1-alphabet'?renderAlphabetSoundLab():''", APP)
        self.assertIn("data-alphabet-play", APP)

    def test_sw_precaches_module_and_data(self):
        self.assertIn("./assets/js/alphabet-sound-progress.js", SW)
        self.assertIn("./data/learning-path/alphabet-sounds.json", SW)

    def test_letter_cards_share_responsive_grid_and_content_roles(self):
        self.assertIn(".alphabet-sound-grid", CSS)
        self.assertIn(".alphabet-sound-card", CSS)
        self.assertIn("grid-template-columns: repeat(4, minmax(0, 1fr));", CSS)
        self.assertIn("@media (min-width: 641px) and (max-width: 1100px)", CSS)
        self.assertIn("@media (min-width: 641px) and (max-width: 850px)", CSS)
        self.assertIn("grid-template-columns: repeat(3, minmax(0, 1fr));", CSS)
        self.assertIn("grid-template-columns: repeat(2, minmax(0, 1fr));", CSS)
        self.assertIn("@media (max-width: 360px)", CSS)


if __name__ == "__main__":
    unittest.main()
