"""Structural regression tests for the v2.71.0 TOEIC vocabulary batch."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class VocabularyBatch012Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.batch = json.loads((ROOT / 'data/vocabulary/batch-012.json').read_text(encoding='utf-8'))
        cls.current_batch = json.loads((ROOT / 'data/vocabulary/batch-028.json').read_text(encoding='utf-8'))
        cls.manifest = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))
        cls.records = {}
        for entry in cls.manifest['letters']:
            data = json.loads((ROOT / entry['file'].removeprefix('./')).read_text(encoding='utf-8'))
            for row in data['words']:
                cls.records[row['id']] = row
        cls.ledger = json.loads((ROOT / 'docs/reports/CMUDICT_IPA_BACKFILL_v2.71.0.json').read_text(encoding='utf-8'))
        cls.ledger_ids = {row['id'] for row in cls.ledger['records']}

    def test_batch_metadata_and_size(self):
        self.assertEqual(self.batch['version'], '2.71.0')
        self.assertEqual(self.batch['batch'], '012')
        self.assertEqual(self.batch['count'], 37)
        self.assertEqual(len(self.batch['words']), 37)
        self.assertIn('Contracts', self.batch['focus'])
        self.assertIn('Facilities', self.batch['focus'])

    def test_each_record_has_editorial_content_and_three_collocations(self):
        ids = set()
        for item in self.batch['words']:
            self.assertNotIn(item['id'], ids)
            ids.add(item['id'])
            record = self.records[item['id']]
            self.assertEqual(record['word'], item['word'])
            self.assertTrue(record['senses'][0]['definition_en'].strip())
            self.assertTrue(record['senses'][0]['meaning_vi'].strip())
            self.assertGreaterEqual(len(record['collocations']), 3, record['word'])
            self.assertTrue(record['examples'][0]['en'].strip())
            self.assertTrue(record['examples'][0]['vi'].strip())
            self.assertEqual(record['examples'][0]['sense_index'], 0)

    def test_only_source_linked_ipa_is_present(self):
        self.assertEqual(self.batch['ipaSummary']['populated'], 35)
        self.assertEqual(self.batch['ipaSummary']['leftBlank'], 2)
        blank = {row['word'] for row in self.batch['words'] if not row['phonetic']['us']}
        self.assertEqual(blank, {'ventilation', 'dispute'})
        for row in self.batch['words']:
            if row['phonetic']['us']:
                self.assertIn(row['id'], self.ledger_ids, row['word'])

    def test_release_delta_and_migration_profile_are_exact(self):
        self.assertEqual(self.manifest['totalWords'], 1221)
        self.assertEqual(self.manifest['previousReleaseTotalWords'], 1181)
        self.assertEqual(self.manifest['releaseAdditionIds'], [row['id'] for row in self.current_batch['words']])
        profile = next(x for x in self.manifest['releaseRepairProfiles'] if x['previousTotalWords'] == 1100)
        self.assertEqual(profile['releaseAdditionIds'][:37], [row['id'] for row in self.batch['words']])
        self.assertEqual(len(profile['releaseAdditionIds']), 81, 'legacy 1100-word snapshots restore Batch 012, 013, and 026 additions')


if __name__ == '__main__':
    unittest.main()
