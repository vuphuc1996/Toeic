"""Regression for v2.95.40's guarded correction of one stale canonical gloss."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import unittest
from pathlib import Path
from glossary_test_helpers import restore_batch_039

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / 'patches-related-terms/v2.95.40/related-terms-034.json'
LEDGER_PATH = ROOT / 'patches-related-terms/v2.95.40/batch-034-glossary-ledger.json'
DATA_PATH = ROOT / 'data/related-terms.json'
UPDATER_SPEC = importlib.util.spec_from_file_location('update_related_terms', ROOT / 'tools/update-related-terms.py')
UPDATER = importlib.util.module_from_spec(UPDATER_SPEC)
UPDATER_SPEC.loader.exec_module(UPDATER)


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


class RelatedGlossaryBatch034Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.data = read_json(DATA_PATH)
        cls.rows = {row['term'].casefold(): row for row in cls.data['terms']}
        cls.canonical = read_json(ROOT / 'data/vocabulary/R.json')
        cls.revision_source = next(row for row in cls.canonical['words'] if row['word'] == 'revision')
        cls.revision = cls.rows['revision']

    def test_batch_is_single_exact_headword_correction(self):
        self.assertEqual(self.ledger['batch'], '034')
        self.assertEqual(self.ledger['release'], '2.95.40')
        self.assertEqual(self.ledger['count'], 1)
        self.assertEqual(self.patch['batchId'], 'related-glossary-034-v2.95.40')
        self.assertEqual([op['term'] for op in self.patch['operations']], ['revision'])
        record = self.ledger['records'][0]
        self.assertEqual(record['term'], 'revision')
        self.assertEqual(record['definition_en'], self.revision_source['senses'][0]['definition_en'])
        self.assertEqual(record['previousDefinitionEn'], self.patch['operations'][0]['expect']['definition_en'])

    def test_current_gloss_matches_canonical_and_preserves_identity_fields(self):
        sense = self.revision_source['senses'][0]
        self.assertEqual(self.revision['definition_en'], sense['definition_en'])
        self.assertEqual(self.revision['pos'], sense['pos'])
        self.assertEqual(self.revision['meaning_vi'], self.ledger['records'][0]['meaning_vi_preserved'])
        self.assertEqual(self.revision['sourceHeadword'], 'revision')
        self.assertEqual(self.revision['sourceRelease'], '2.95.32')
        self.assertEqual(self.revision['sourceSenseIndex'], 0)

    def test_patch_hash_and_old_value_guard_are_reproducible(self):
        # Reconstruct the v2.95.40 baseline without any later additive glossary
        # batches before reversing this guarded correction. Historical patch hashes
        # remain replayable as new batch ledgers are added.
        current = restore_batch_039(json.loads(DATA_PATH.read_text(encoding='utf-8')), ROOT)
        later_terms = set()
        for ledger_path in (ROOT / 'patches-related-terms').glob('**/batch-*-glossary-ledger.json'):
            later = read_json(ledger_path)
            if 34 < int(later.get('batch', 0)) < 39:
                later_terms.update(r['term'].casefold() for r in later.get('records', []))
        current['terms'] = [r for r in current['terms'] if r['term'].casefold() not in later_terms]
        raw = (json.dumps(current, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        old = self.patch['operations'][0]['expect']['definition_en'].encode('utf-8')
        new = self.patch['operations'][0]['set']['definition_en'].encode('utf-8')
        restored = raw.replace(new, old)
        self.assertNotEqual(restored, raw)
        self.assertEqual(hashlib.sha256(restored).hexdigest(), self.patch['baseFileSha256'])

    def test_update_helper_is_atomic_and_does_not_mutate_input(self):
        source = {'schemaVersion': 1, 'terms': [{'term': 'revision', 'definition_en': 'old', 'meaning_vi': 'nghĩa', 'pos': 'n'}]}
        patch = {'schemaVersion': 1, 'operations': [{'term': 'revision', 'expect': {'definition_en': 'old', 'meaning_vi': 'nghĩa'}, 'set': {'definition_en': 'new'}}]}
        updated, changed = UPDATER.update_document(source, patch)
        self.assertEqual(changed, ['revision'])
        self.assertEqual(source['terms'][0]['definition_en'], 'old')
        self.assertEqual(updated['terms'][0]['definition_en'], 'new')

    def test_update_helper_rejects_stale_expectations_and_identity_changes(self):
        source = {'schemaVersion': 1, 'terms': [{'term': 'revision', 'definition_en': 'current'}]}
        stale = {'schemaVersion': 1, 'operations': [{'term': 'revision', 'expect': {'definition_en': 'old'}, 'set': {'definition_en': 'new'}}]}
        with self.assertRaisesRegex(ValueError, 'stale expectation'):
            UPDATER.update_document(source, stale)
        identity_change = {'schemaVersion': 1, 'operations': [{'term': 'revision', 'expect': {'definition_en': 'current'}, 'set': {'term': 'other'}}]}
        with self.assertRaisesRegex(ValueError, 'unsupported or immutable'):
            UPDATER.update_document(source, identity_change)

    def test_update_helper_rejects_duplicate_glossary_identities(self):
        source = {'schemaVersion': 1, 'terms': [{'term': 'revision', 'definition_en': 'old'}, {'term': ' REVISION ', 'definition_en': 'duplicate'}]}
        patch = {'schemaVersion': 1, 'operations': [{'term': 'revision', 'expect': {'definition_en': 'old'}, 'set': {'definition_en': 'new'}}]}
        with self.assertRaisesRegex(ValueError, 'duplicate existing glossary term'):
            UPDATER.update_document(source, patch)

if __name__ == '__main__':
    unittest.main()
