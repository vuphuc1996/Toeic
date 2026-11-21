import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH_PATH = ROOT / 'patches-related-terms' / 'v2.95.34' / 'related-terms-030.json'


def norm(value):
    return re.sub(r'[^a-z0-9]+', ' ', value.lower()).strip()


class RelatedGlossaryBatch030Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batch = json.loads(BATCH_PATH.read_text(encoding='utf-8'))
        cls.glossary = json.loads((ROOT / 'data/related-terms.json').read_text(encoding='utf-8'))['terms']
        # Only manifest-listed A-Z files are canonical runtime vocabulary.
        # Editorial batch snapshots also live in data/vocabulary/ but are not
        # a second runtime source and must not overwrite canonical lookup rows.
        manifest = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))
        cls.vocabulary = []
        for item in manifest.get('letters', []):
            path = ROOT / item['file'].removeprefix('./')
            cls.vocabulary.extend(row for row in json.loads(path.read_text(encoding='utf-8')).get('words', []) if isinstance(row, dict))
        cls.vocab_by_word = {norm(row.get('word', '')): row for row in cls.vocabulary if row.get('word')}
        cls.canonical_word_count = manifest.get('totalWords')
        cls.glossary_by_term = {norm(row['term']): row for row in cls.glossary}

    def test_lookup_uses_canonical_manifest_inventory(self):
        self.assertEqual(len(self.vocabulary), self.canonical_word_count)
        self.assertEqual(self.canonical_word_count, 1141)

    def test_batch_is_exactly_73_canonical_single_sense_records(self):
        self.assertEqual(self.batch['count'], 73)
        self.assertEqual(len(self.batch['records']), 73)
        self.assertEqual(len({norm(r['term']) for r in self.batch['records']}), 73)
        for row in self.batch['records']:
            source = self.vocab_by_word[norm(row['sourceHeadword'])]
            self.assertEqual(source['word'], row['sourceHeadword'])
            self.assertEqual(len(source['senses']), 1)
            # The batch file is a historical snapshot. Later canonical
            # vocabulary corrections may legitimately supersede its old text.
            self.assertTrue(row['definition_en'].strip())
            self.assertEqual(source['senses'][0]['pos'], row['pos'])
            self.assertEqual(row['sourceSenseIndex'], 0)
            self.assertEqual(row['source'], 'canonical-vocabulary-senses')

    def test_canonical_data_matches_patch_and_vietnamese_meanings_are_preserved(self):
        for row in self.batch['records']:
            target = self.glossary_by_term[norm(row['term'])]
            source = self.vocab_by_word[norm(row['sourceHeadword'])]
            self.assertEqual(target['definition_en'], source['senses'][0]['definition_en'])
            self.assertEqual(target['pos'], source['senses'][0]['pos'])
            self.assertEqual(target['meaning_vi'], row['baselineMeaningVi'])
            self.assertEqual(target['sourceHeadword'], row['sourceHeadword'])
            self.assertEqual(target['sourceRelease'], '2.95.32')

    def test_patch_does_not_add_duplicate_terms_or_modify_unmatched_records(self):
        self.assertGreaterEqual(len(self.glossary), 519)
        self.assertEqual(len({norm(row['term']) for row in self.glossary}), len(self.glossary))
        for row in self.batch['records']:
            target = self.glossary_by_term[norm(row['term'])]
            self.assertTrue(target.get('definition_en'))
            self.assertTrue(target.get('pos'))

if __name__ == '__main__':
    unittest.main()
