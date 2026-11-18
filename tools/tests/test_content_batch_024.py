"""Integrity and editorial-boundary tests for the v2.92.0 content batch."""
import hashlib, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ContentBatch024Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.registry=json.loads((ROOT/'tools/content-batch-024-v2.92.0.json').read_text(encoding='utf-8'))
  cls.grammar=json.loads((ROOT/'data/grammar/lessons.json').read_text(encoding='utf-8'))['lessons']
  cls.listening=json.loads((ROOT/'data/listening/listening-library.json').read_text(encoding='utf-8'))['listening']
  cls.reading=json.loads((ROOT/'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']
 def _hash(self,item):
  return hashlib.sha256(json.dumps(item,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 def test_batch_inventory_and_hashes(self):
  self.assertEqual(len(self.registry['grammar']),8)
  self.assertEqual(len(self.registry['listening']),6)
  self.assertEqual(len(self.registry['reading']),6)
  for group,items in [('listening',self.listening),('reading',self.reading)]:
   by={x['id']:x for x in items}
   for ident,digest in self.registry[group+'_sha256'].items():
    self.assertIn(ident,by)
    self.assertEqual(self._hash(by[ident]),digest,ident)
  # Original 2.92.0 grammar fingerprints remain immutable; this second map
  # fingerprints the current 2.94.0 additive bilingual example enrichment.
  by={x['id']:x for x in self.grammar}
  for ident,digest in self.registry['grammar_sha256_v2_94_enriched'].items():
   self.assertEqual(self._hash(by[ident]),digest,ident)
 def test_grammar_batch_has_24_valid_questions(self):
  by={x['id']:x for x in self.grammar}
  items=[by[x] for x in self.registry['grammar']]
  self.assertEqual(sum(len(x['exercises']) for x in items),24)
  seen=set()
  for item in items:
   self.assertTrue(item.get('parts'))
   self.assertTrue(item.get('examples'))
   for q in item['exercises']:
    self.assertEqual(len(q['choices']),4)
    self.assertIn(q['answerIndex'],range(4))
    self.assertEqual(len(q['choiceIds']),4)
    for cid in q['choiceIds']:
     self.assertNotIn(cid,seen); seen.add(cid)
 def test_listening_batch_is_practice_only_and_evidence_grounded(self):
  by={x['id']:x for x in self.listening}
  items=[by[x] for x in self.registry['listening']]
  self.assertEqual(sum(len(x['questions']) for x in items),18)
  for item in items:
   self.assertEqual(item['editorialStatus'],'reserve-pending-independent-review')
   self.assertEqual(item['editorialBatch'],'024')
   self.assertTrue(item.get('transcriptTranslation'))
   script=' '.join(s['text'] for s in item['segments'])
   for q in item['questions']:
    self.assertEqual(len(q['choices']),4)
    self.assertIn(q['evidenceText'],script)
    self.assertEqual(len(q['choiceIds']),4)
 def test_reading_batch_has_27_grounded_questions_and_translations(self):
  by={x['id']:x for x in self.reading}
  items=[by[x] for x in self.registry['reading']]
  self.assertEqual(sum(len(x['questions']) for x in items),27)
  for item in items:
   self.assertEqual(item['editorialStatus'],'reserve-pending-independent-review')
   self.assertEqual(item['editorialBatch'],'024')
   self.assertTrue(item.get('translation'))
   if item['documentType'] == 'DOUBLE PASSAGE': self.assertEqual(len(item['questions']),5)
   source={d['label']:d['content'] for d in item['documents']}
   for q in item['questions']:
    self.assertEqual(len(q['choices']),4)
    self.assertIn(q['answerIndex'],range(4))
    self.assertTrue(q['evidence']['sourceLabels'])
    for label in q['evidence']['sourceLabels']:
     self.assertIn(label,source)
    for quote in q['evidence']['quotes']:
     self.assertTrue(any(quote in source[label] for label in q['evidence']['sourceLabels']))
 def test_reading_answer_positions_are_balanced(self):
  by={x['id']:x for x in self.reading}
  from collections import Counter
  counts=Counter(q['answerIndex'] for ident in self.registry['reading'] for q in by[ident]['questions'])
  self.assertEqual(counts,{0:7,1:7,2:7,3:6})
 def test_no_new_batch_item_is_promoted_to_mock(self):
  for collection,ids in [(self.listening,self.registry['listening']),(self.reading,self.registry['reading'])]:
   by={x['id']:x for x in collection}
   for ident in ids:
    self.assertEqual(by[ident]['editorialStatus'],'reserve-pending-independent-review')
 def test_review_checklist_covers_all_batch_resources(self):
  text=(ROOT/'docs/reports/TOEIC_BATCH_024_REVIEW_CHECKLIST_v2.92.0.md').read_text(encoding='utf-8')
  for ident in self.registry['grammar']+self.registry['listening']+self.registry['reading']:
   self.assertIn(f'`{ident}`',text)
  self.assertIn('PENDING',text)
  self.assertIn('item-level review',text)
 def test_b1_blueprint_is_explicitly_not_a_completed_pathway(self):
  text=(ROOT/'docs/reports/FOUNDATION_B1_CURRICULUM_BLUEPRINT_v2.92.0.md').read_text(encoding='utf-8')
  self.assertIn('NOT IMPLEMENTED AS A LEARNER PATHWAY',text)
  self.assertIn('No B1 lessons are added to the stage selector',text)
if __name__=='__main__': unittest.main()
