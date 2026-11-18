"""Integrity, evidence and editorial-boundary tests for v2.93.0 Batch 025."""
import hashlib, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ContentBatch025Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.registry=json.loads((ROOT/'tools/content-batch-025-v2.93.0.json').read_text(encoding='utf-8'))
  cls.grammar=json.loads((ROOT/'data/grammar/lessons.json').read_text(encoding='utf-8'))['lessons']
  cls.listening=json.loads((ROOT/'data/listening/listening-library.json').read_text(encoding='utf-8'))['listening']
  cls.reading=json.loads((ROOT/'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']
  cls.vocab=json.loads((ROOT/'data/vocabulary/batch-013.json').read_text(encoding='utf-8'))
 def digest(self,item):
  return hashlib.sha256(json.dumps(item,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 def test_registry_hashes_and_counts(self):
  self.assertEqual(len(self.registry['grammar']),9)
  self.assertEqual(len(self.registry['listening']),8)
  self.assertEqual(len(self.registry['reading']),8)
  self.assertEqual(len(self.registry['vocabulary']),4)
  for group,items in [('grammar',self.grammar),('listening',self.listening),('reading',self.reading)]:
   by={x['id']:x for x in items}
   for ident,digest in self.registry[group+'_sha256'].items():
    self.assertIn(ident,by); self.assertEqual(self.digest(by[ident]),digest,ident)
  for row in self.vocab['words']:
   self.assertEqual(self.digest(row),self.registry['vocabulary_sha256'][row['id']])
 def test_grammar_batch_has_27_exercises_and_part_tags(self):
  by={x['id']:x for x in self.grammar}
  items=[by[i] for i in self.registry['grammar']]
  self.assertEqual(sum(len(x['exercises']) for x in items),27)
  seen=set()
  for item in items:
   self.assertTrue(set(item['parts']).issubset({'Part 5','Part 6'}))
   self.assertTrue(item['examples'] and item['explanation'])
   for q in item['exercises']:
    self.assertEqual(len(q['choices']),4); self.assertEqual(len(set(q['choices'])),4)
    self.assertIn(q['answerIndex'],range(4)); self.assertEqual(len(q['choiceIds']),4)
    for cid in q['choiceIds']: self.assertNotIn(cid,seen); seen.add(cid)
 def test_listening_batch_has_20_questions_and_grounded_evidence(self):
  by={x['id']:x for x in self.listening}; items=[by[i] for i in self.registry['listening']]
  self.assertEqual(sum(len(x['questions']) for x in items),20)
  for item in items:
   self.assertEqual(item['editorialStatus'],'reserve-pending-independent-review')
   self.assertEqual(item['editorialBatch'],'025')
   script=' '.join(s['text'] for s in item['segments'])
   expected=3 if item['part']=='Part 2' else 4
   for q in item['questions']:
    self.assertEqual(len(q['choices']),expected)
    self.assertIn(q['evidenceText'],script)
    self.assertEqual(len(q['choiceIds']),expected)
 def test_reading_batch_has_36_questions_and_complete_double_passages(self):
  by={x['id']:x for x in self.reading}; items=[by[i] for i in self.registry['reading']]
  self.assertEqual(sum(len(x['questions']) for x in items),36)
  self.assertEqual(sum(x['documentType']=='SINGLE PASSAGE' for x in items),4)
  self.assertEqual(sum(x['documentType']=='DOUBLE PASSAGE' for x in items),4)
  for item in items:
   self.assertEqual(item['editorialStatus'],'reserve-pending-independent-review')
   self.assertTrue(item['translation'])
   if item['documentType']=='DOUBLE PASSAGE': self.assertEqual(len(item['questions']),5)
   sources={d['label']:d['content'] for d in item['documents']}
   for q in item['questions']:
    self.assertEqual(len(q['choices']),4); self.assertIn(q['answerIndex'],range(4))
    for label in q['evidence']['sourceLabels']: self.assertIn(label,sources)
    for quote in q['evidence']['quotes']: self.assertTrue(any(quote in sources[label] for label in q['evidence']['sourceLabels']))
 def test_reading_batch_answer_positions_are_balanced(self):
  from collections import Counter
  by={x['id']:x for x in self.reading}; items=[by[i] for i in self.registry['reading']]
  distribution=Counter(q['answerIndex'] for item in items for q in item['questions'])
  self.assertEqual(distribution,{0:9,1:9,2:9,3:9})
 def test_new_reading_and_listening_remain_mock_excluded(self):
  for rows,ids in [(self.listening,self.registry['listening']),(self.reading,self.registry['reading'])]:
   by={x['id']:x for x in rows}
   for ident in ids: self.assertEqual(by[ident]['editorialStatus'],'reserve-pending-independent-review')
 def test_vocabulary_batch_uses_only_source_linked_ipa(self):
  self.assertEqual(self.vocab['count'],4)
  self.assertEqual(self.vocab['ipaSummary']['populated'],4)
  self.assertEqual(self.vocab['ipaSummary']['leftBlank'],0)
  self.assertTrue(all(x['phonetic']['us'].startswith('/') for x in self.vocab['words']))
if __name__=='__main__': unittest.main()
