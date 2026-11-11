"""Tests for the eight locally hosted Listening Part 1 Pexels photo assets."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'tools/validate-part1-photo-assets.py'
spec = importlib.util.spec_from_file_location('validate_part1_photo_assets', SCRIPT)
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(validator)

class Part1PhotoAssetTests(unittest.TestCase):
    def test_all_part1_photo_paths_match_the_attribution_manifest(self):
        data = json.loads((ROOT / 'data/listening/listening-library.json').read_text(encoding='utf-8'))
        p1 = [item for item in data['listening'] if item.get('part') == 'Part 1']
        self.assertEqual(len(p1), 8)
        import csv
        with (ROOT / 'assets/listening/ATTRIBUTION.csv').open(encoding='utf-8-sig', newline='') as handle:
            rows = {row['question_id']: row for row in csv.DictReader(handle)}
        self.assertEqual(set(rows), {item['id'] for item in p1})
        for item in p1:
            self.assertEqual(Path(item['photo']).name, rows[item['id']]['filename'])
            self.assertTrue(rows[item['id']]['photographer'])
            self.assertIn('pexels.com/license', rows[item['id']]['license'])

    def test_valid_jpeg_dimensions_are_read(self):
        # A minimal JPEG SOF fixture is enough to exercise the dimension parser without Pillow.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'photo.jpg'
            path.write_bytes(bytes.fromhex('FFD8 FFC0 0011 08 03C0 0500 03 01 11 00 02 11 00 03 11 00 FFD9'))
            self.assertEqual(validator.jpeg_dimensions(path), (1280, 960))

    def test_non_jpeg_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'not-a-photo.jpg'
            path.write_bytes(b'not a jpeg')
            with self.assertRaises(ValueError):
                validator.jpeg_dimensions(path)

    def test_missing_photos_are_warnings_only_in_explicit_local_mode(self):
        errors, warnings, valid = validator.validate(allow_missing=True)
        self.assertFalse(errors)
        self.assertEqual(valid + len(warnings), 8)

if __name__ == '__main__':
    unittest.main()
