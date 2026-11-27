"""Regression tests for canonical-sense related-term Glossary Batch 028."""
from __future__ import annotations
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
EXPECTED={'adherence','agreement','appraise','assign','assumption','authorization','breakdown'}
def read(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
class RelatedGlossaryBatch028Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.ledger=read('patches-related-terms/v2.95.25/batch-028-glossary-ledger.json')
  cls.patch=read('patches-related-terms/v2.95.25/related-terms-028.json')
  cls.related=read('data/related-terms.json')['terms']
  cls.by_term={row['term'].casefold():row for row in cls.related}
  cls.words={}
  manifest=read('data/manifest.json')
  for letter in manifest['letters']:
   for word in read(letter['file'].removeprefix('./'))['words']:
    cls.words[word['word'].casefold()]=word
 def test_batch_metadata_and_selected_terms(self):
  self.assertEqual(self.ledger['batch'],'028')
  self.assertEqual(self.ledger['release'],'2.95.25')
  self.assertEqual(self.ledger['count'],7)
  self.assertEqual({r['term'] for r in self.ledger['records']},EXPECTED)
 def test_patch_is_absent_only_and_matches_ledger(self):
  ledger={r['term'].casefold():r for r in self.ledger['records']}
  self.assertEqual(len(self.patch['operations']),7)
  for op in self.patch['operations']:
   self.assertEqual(op['expect'],{'absent':True})
   self.assertEqual(op['new'],ledger[op['term'].casefold()])
 def test_entries_match_exact_canonical_sense_and_provenance(self):
  for row in self.ledger['records']:
   current=self.by_term[row['term'].casefold()]
   for key,value in row.items(): self.assertEqual(current.get(key),value,row['term'])
   word=self.words[row['sourceHeadword'].casefold()]
   sense=next(s for s in word['senses'] if s.get('definition_en')==row['definition_en'] and s.get('meaning_vi')==row['meaning_vi'] and s.get('pos')==row['pos'])
   self.assertTrue(sense)
   self.assertEqual(row['source'],'canonical-vocabulary-glossary-addition')
   self.assertEqual(row['sourceRelease'],'2.95.25')
 def test_no_relation_or_canonical_vocab_mutations(self):
  baseline=read('tools/baseline-ids.json')
  current_ids={row['id'] for row in self.words.values()}
  baseline_ids=set(baseline['ids'])
  self.assertEqual(len(baseline_ids),baseline['count'])
  self.assertTrue(baseline_ids.issubset(current_ids),'A protected canonical vocabulary ID is missing')
  self.assertEqual(len(current_ids),len(self.words))
  self.assertGreaterEqual(len(self.related),519)
  self.assertEqual(len({r['term'].casefold() for r in self.related}),len(self.related))
if __name__=='__main__': unittest.main()
