"""Regression for Cambridge-sourced, guarded Related Glossary enrichment batch 039."""
from __future__ import annotations
import copy
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATCH_PATH = ROOT / 'patches-related-terms/v2.95.50/related-terms-039.json'
LEDGER_PATH = ROOT / 'patches-related-terms/v2.95.50/batch-039-glossary-ledger.json'
EXPECTED = {
    'plan': ('n', {'agenda', 'proposal', 'strategy'}),
    'neglect': ('v', {'handle', 'maintain', 'oversee', 'perform', 'prepare'}),
    'amount': ('n', {'quantity', 'supply', 'volume'}),
    'bill': ('n/v', {'charge', 'invoice'}),
    'customer': ('n', {'buyer', 'client'}),
    'division': ('n', {'branch', 'department', 'section'}),
    'essential': ('adj', {'indispensable', 'key', 'necessary'}),
    'file': ('n/v', {'document', 'record', 'submit'}),
    'gain': ('n/v', {'benefit', 'profit'}),
    'loss': ('n', {'profit', 'retention', 'revenue'}),
    'meeting': ('n', {'appointment', 'interview', 'minute'}),
    'refuse': ('v', {'accept', 'offer', 'reject'}),
}

def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

class RelatedGlossaryBatch039Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch = read_json(PATCH_PATH)
        cls.ledger = read_json(LEDGER_PATH)
        cls.glossary = read_json(ROOT / 'data/related-terms.json')
        cls.rows = {row['term'].casefold(): row for row in cls.glossary['terms']}
        cls.targets = {}
        cls.headwords = set()
        for path in sorted((ROOT / 'data/vocabulary').glob('[A-Z].json')):
            for word in read_json(path)['words']:
                cls.headwords.add(word['word'].casefold())
                for sense in word.get('senses', []):
                    for field in ('synonyms', 'antonyms'):
                        for target in sense.get(field, []) or []:
                            cls.targets.setdefault(str(target).strip().casefold(), set()).add(word['word'].casefold())

    def test_inventory_is_exact_and_every_term_is_an_existing_relation_target(self):
        self.assertEqual(self.ledger['batch'], '039')
        self.assertEqual(self.ledger['release'], '2.95.50')
        self.assertEqual(self.ledger['count'], len(EXPECTED))
        self.assertEqual({x['term'].casefold() for x in self.patch['operations']}, set(EXPECTED))
        for term, (_, anchors) in EXPECTED.items():
            self.assertIn(term, self.targets)
            self.assertTrue(anchors.issubset(self.targets[term]), (term, anchors, self.targets[term]))

    def test_definitions_pos_and_provenance_are_present_and_non_placeholder(self):
        for term, (pos, _) in EXPECTED.items():
            row = self.rows[term]
            self.assertEqual(row['pos'], pos, term)
            self.assertTrue(row['definition_en'].strip(), term)
            self.assertTrue(row['source'].startswith('Cambridge Dictionary'), term)
            self.assertEqual(row['sourceRelease'], '2.95.50')
            self.assertEqual(len(row['sourceUrls']), 1)
            self.assertTrue(row['sourceUrls'][0].startswith('https://dictionary.cambridge.org/dictionary/english/'))
            self.assertNotRegex(row['definition_en'], r'(?i)placeholder|reference gloss|todo|tbd|definition pending')

    def test_patch_has_exact_guards_and_reconstructs_original_glossary_hash(self):
        self.assertEqual(self.patch['batchId'], 'related-glossary-039-v2.95.50')
        restored = copy.deepcopy(self.glossary)
        by = {row['term'].casefold(): row for row in restored['terms']}
        # Reverse later Batch 041 and Batch 040 in descending order before
        # reconstructing the Batch 039 base snapshot.
        batch_041_path = ROOT / 'patches-related-terms/v2.95.52/related-terms-041.json'
        batch_041 = read_json(batch_041_path)
        for op in batch_041['operations']:
            row = by[op['term'].casefold()]
            for field, old_value in op['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        batch_040_path = ROOT / 'patches-related-terms/v2.95.51/related-terms-040.json'
        batch_040 = read_json(batch_040_path)
        for op in batch_040['operations']:
            row = by[op['term'].casefold()]
            for field, old_value in op['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
        for op in self.patch['operations']:
            self.assertEqual(op['expect'].get('term', '').casefold(), op['term'].casefold())
            row = by[op['term'].casefold()]
            for field, old_value in op['expect'].items():
                if field == 'term':
                    continue
                if old_value is None:
                    row.pop(field, None)
                else:
                    row[field] = old_value
            for field in op['set']:
                if field not in op['expect']:
                    row.pop(field, None)
        payload = (json.dumps(restored, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        self.assertEqual(hashlib.sha256(payload).hexdigest(), self.patch['baseFileSha256'])
        self.assertEqual(self.ledger['baseRelatedTermsSha256'], self.patch['baseFileSha256'])

    def test_only_glossary_rows_were_targeted(self):
        for op in self.patch['operations']:
            self.assertEqual(set(op['set']), {'pos', 'definition_en', 'source', 'sourceUrls', 'sourceRelease'})
        self.assertEqual(len(self.rows), 567)

if __name__ == '__main__':
    unittest.main()
