"""Regression contract for sourced Related Glossary Batch 042."""
from __future__ import annotations
import copy
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / 'patches-related-terms/v2.95.61/related-terms-042.json'
LEDGER_PATH = ROOT / 'patches-related-terms/v2.95.61/batch-042-glossary-ledger.json'
EXPECTED = {
    'enter': ('v', {'access', 'penetrate'}),
    'examine': ('v', {'inspect', 'review'}),
    'guarantee': ('n/v', {'ensure', 'warranty'}),
    'mark': ('n/v', {'date', 'label'}),
    'monthly': ('adj/adv', {'weekly', 'yearly'}),
    'observe': ('v', {'monitor', 'notice'}),
    'occasion': ('n', {'event', 'time'}),
    'optional': ('adj', {'necessary', 'voluntary'}),
    'period': ('n', {'term', 'time'}),
    'reach': ('v', {'access', 'contact'}),
    'remove': ('v', {'install', 'withdraw'}),
    'restriction': ('n', {'access', 'limit'}),
    'return': ('n/v', {'profitability', 'yield'}),
    'rule': ('n', {'policy', 'regulation'}),
    'schedule': ('n/v', {'agenda', 'itinerary'}),
    'seller': ('n', {'buyer', 'vendor'}),
    'shift': ('n/v', {'fluctuate', 'transfer'}),
    'validate': ('v', {'confirm', 'verify'}),
    'weekly': ('adj/adv', {'monthly', 'yearly'}),
    'business day': ('n', {'weekday'}),
}
CANONICAL = {'guarantee', 'monthly', 'schedule', 'weekly'}
PLACEHOLDER = 'Reference gloss for practice distractors.'


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


class RelatedGlossaryBatch042Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.glossary = read_json(ROOT / 'data/related-terms.json')
        cls.rows = {row['term'].casefold(): row for row in cls.glossary['terms']}
        cls.targets = {}
        cls.vocab = {}
        cls.headwords = set()
        for path in sorted((ROOT / 'data/vocabulary').glob('[A-Z].json')):
            for word in read_json(path)['words']:
                cls.vocab[word['word'].casefold()] = word
                cls.headwords.add(word['word'].casefold())
                for sense in word.get('senses', []):
                    for field in ('synonyms', 'antonyms'):
                        for target in sense.get(field, []) or []:
                            cls.targets.setdefault(str(target).strip().casefold(), set()).add(word['word'].casefold())

    def test_exact_inventory_and_existing_relation_anchors(self):
        self.assertEqual(self.patch['batchId'], 'related-glossary-042-v2.95.61')
        self.assertEqual(self.ledger['batch'], '042')
        self.assertEqual(self.ledger['release'], '2.95.61')
        self.assertEqual(self.ledger['count'], len(EXPECTED))
        self.assertEqual({row['term'].casefold() for row in self.ledger['records']}, set(EXPECTED))
        self.assertEqual({op['term'].casefold() for op in self.patch['operations']}, set(EXPECTED))
        for term, (_, anchors) in EXPECTED.items():
            self.assertIn(term, self.rows)
            self.assertIn(term, self.targets)
            self.assertTrue(anchors.issubset(self.targets[term]), (term, anchors, self.targets[term]))

    def test_definitions_pos_and_provenance_are_complete(self):
        for term, (pos, _) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row['pos'], pos, term)
            self.assertTrue(row['definition_en'].strip(), term)
            self.assertNotEqual(row['definition_en'], PLACEHOLDER, term)
            self.assertNotRegex(row['definition_en'], r'(?i)placeholder|reference gloss|todo|tbd|definition pending')
            if term in CANONICAL:
                self.assertTrue(row['source'].startswith('canonical-vocabulary-senses'))
                self.assertEqual(row['sourceRelease'], '2.95.60')
                self.assertEqual(row['sourceHeadword'].casefold(), term)
                senses = self.vocab[term]['senses']
                self.assertEqual(row['definition_en'], '; '.join(s['definition_en'] for s in senses))
                self.assertNotIn('sourceUrls', row)
            else:
                self.assertTrue(row['source'].startswith('Cambridge Dictionary'), term)
                self.assertEqual(row['sourceRelease'], '2.95.61')
                self.assertEqual(row['sourceUrls'], [f'https://dictionary.cambridge.org/dictionary/english/{term.replace(" ", "-")}'])

    def test_patch_guards_reconstruct_exact_pre_batch_glossary(self):
        restored = copy.deepcopy(self.glossary)
        by = {row['term'].casefold(): row for row in restored['terms']}
        # Reverse the newer Batch 043 first to restore the exact Batch 042 output.
        batch_043_path = ROOT / 'patches-related-terms/v2.95.62/related-terms-043.json'
        batch_043 = read_json(batch_043_path)
        for later_op in batch_043['operations']:
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
            self.assertEqual(row['term'].casefold(), op['expect']['term'].casefold())
            for field, old_value in op['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch['baseFileSha256'])
        self.assertEqual(self.ledger['baseRelatedTermsSha256'], self.patch['baseFileSha256'])

    def test_only_approved_mutable_glossary_fields_are_set(self):
        allowed = {'pos', 'definition_en', 'source', 'sourceUrls', 'sourceHeadword', 'sourceRelease'}
        for op in self.patch['operations']:
            self.assertLessEqual(set(op['set']), allowed)
            self.assertEqual(op['set']['pos'], EXPECTED[op['term'].casefold()][0])
        self.assertEqual(len(self.rows), 567)

    def test_vietnamese_meanings_and_relation_arrays_are_preserved(self):
        for record in self.ledger['records']:
            row = self.rows[record['term'].casefold()]
            self.assertEqual(row['meaning_vi'], record['meaning_vi_preserved'])
            self.assertEqual(sorted(self.targets[record['term'].casefold()]), record['relationAnchors'])
        # No canonical headword was added for any of the 20 relation targets.
        self.assertEqual(set(EXPECTED) & self.headwords, CANONICAL)


if __name__ == '__main__':
    unittest.main()
