"""Regression contract for Cambridge-sourced Related Glossary Batch 041."""
from __future__ import annotations
import copy
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    'present': ('adj/v', {'current', 'introduce', 'submit'}),
    'associate': ('n', {'colleague', 'partner'}),
    'contender': ('n', {'candidate', 'competitor'}),
    'daily': ('adj/adv', {'monthly', 'weekly'}),
    'deal': ('n', {'contract', 'transaction'}),
    'deny': ('v', {'claim', 'confirm'}),
    'direction': ('n', {'guidance', 'instruction'}),
    'endpoint': ('n', {'destination', 'terminal'}),
    'fee': ('n', {'charge', 'payment'}),
    'legitimate': ('adj', {'legal', 'valid'}),
    'occupation': ('n', {'career', 'employment'}),
}

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

class RelatedGlossaryBatch041Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(ROOT / 'patches-related-terms/v2.95.52/related-terms-041.json')
        cls.ledger = read_json(ROOT / 'patches-related-terms/v2.95.52/batch-041-glossary-ledger.json')
        cls.glossary = read_json(ROOT / 'data/related-terms.json')
        cls.rows = {r['term'].casefold(): r for r in cls.glossary['terms']}
        cls.targets = {}
        cls.headwords = set()
        for path in sorted((ROOT / 'data/vocabulary').glob('[A-Z].json')):
            for word in read_json(path)['words']:
                cls.headwords.add(word['word'].casefold())
                for sense in word.get('senses', []):
                    for field in ('synonyms', 'antonyms'):
                        for target in sense.get(field, []) or []:
                            cls.targets.setdefault(str(target).strip().casefold(), set()).add(word['word'].casefold())

    def test_exact_inventory_and_existing_relation_anchors(self):
        self.assertEqual(self.ledger['batch'], '041')
        self.assertEqual(self.ledger['release'], '2.95.52')
        self.assertEqual(self.ledger['count'], len(EXPECTED))
        self.assertEqual({r['term'].casefold() for r in self.ledger['records']}, set(EXPECTED))
        self.assertEqual({o['term'].casefold() for o in self.patch['operations']}, set(EXPECTED))
        for term, (_, anchors) in EXPECTED.items():
            self.assertIn(term, self.targets)
            self.assertTrue(anchors.issubset(self.targets[term]), (term, anchors, self.targets[term]))
            self.assertNotIn(term, self.headwords)

    def test_definitions_pos_and_provenance_are_complete(self):
        for term, (pos, _) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row['pos'], pos, term)
            self.assertTrue(row['definition_en'].strip(), term)
            self.assertTrue(row['source'].startswith('Cambridge Dictionary'), term)
            self.assertEqual(row['sourceRelease'], '2.95.52')
            self.assertEqual(row['sourceUrls'], [f'https://dictionary.cambridge.org/dictionary/english/{term}'])
            self.assertNotRegex(row['definition_en'], r'(?i)placeholder|reference gloss|todo|tbd|definition pending')

    def test_patch_guards_reconstruct_exact_pre_batch_glossary(self):
        restored = copy.deepcopy(self.glossary)
        by = {r['term'].casefold(): r for r in restored['terms']}
        # Reverse later Batch 043 first, then Batch 042, to reconstruct the Batch 041 base.
        batch_043 = read_json(ROOT / 'patches-related-terms/v2.95.62/related-terms-043.json')
        for later_op in batch_043['operations']:
            row = by[later_op['term'].casefold()]
            for field, old_value in later_op['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        batch_042 = read_json(ROOT / 'patches-related-terms/v2.95.61/related-terms-042.json')
        for later_op in batch_042['operations']:
            row = by[later_op['term'].casefold()]
            for field, old_value in later_op['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        for op in self.patch['operations']:
            row = by[op['term'].casefold()]
            for field, value in op['expect'].items():
                if field == 'term':
                    continue
                if value is None:
                    row.pop(field, None)
                else:
                    row[field] = value
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch['baseFileSha256'])
        self.assertEqual(self.ledger['baseRelatedTermsSha256'], self.patch['baseFileSha256'])
        for op in self.patch['operations']:
            self.assertEqual(op['expect']['term'].casefold(), op['term'].casefold())
            self.assertEqual(set(op['set']), {'pos', 'definition_en', 'source', 'sourceUrls', 'sourceRelease'})

    def test_vietnamese_meanings_and_relation_arrays_are_unchanged(self):
        for record in self.ledger['records']:
            self.assertEqual(self.rows[record['term'].casefold()]['meaning_vi'], record['meaning_vi_preserved'])
        self.assertEqual(len(self.rows), 567)

if __name__ == '__main__':
    unittest.main()
