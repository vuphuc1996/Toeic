"""Integrity, review-gating and content checks for Listening expansion batch 027."""
from __future__ import annotations
import json, hashlib, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def read(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
class ContentBatch027Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.batch=read('tools/content-batch-027-v2.95.37.json')
  cls.units=read('data/listening/listening-library.json')['listening']
  cls.by_id={x['id']:x for x in cls.units}
 def test_batch_manifest_and_inventory(self):
  self.assertEqual(self.batch['batch'],'027'); self.assertEqual(self.batch['version'],'2.95.37')
  self.assertEqual(len(self.batch['listening']),16)
  self.assertEqual(self.batch['counts'],{'listeningUnits':16,'listeningQuestions':32,'part2Units':8,'part3Units':4,'part4Units':4})
  document=read('data/listening/listening-library.json')
  remediation_ids={
   'batch026-part3-vendor-call','batch026-part3-training-room',
   'batch026-part3-invoice-correction','batch026-part3-access-card',
   'batch026-part4-building-notice','batch026-part4-travel-update',
   'batch026-part4-product-launch','batch026-part4-policy-reminder',
  }
  present=set()
  for unit in document['listening']:
   if unit.get('id') in remediation_ids:
    self.assertTrue(unit.get('transcriptTranslation','').strip(),unit['id'])
    present.add(unit['id'])
    del unit['transcriptTranslation']
  self.assertEqual(present,remediation_ids)

  # v2.95.83 adds one question-level practice-only item to each of ten
  # allowlisted, pre-existing Part 4 talks. Remove only these exact items
  # when reconstructing the historical listening-library fingerprint.
  practice_only_part4_ids={
   'part4-office-announcement','part4-conference-update',
   'part4-safety-announcement','part4-product-launch',
   'part4-quarterly-town-hall','part4-customer-voicemail',
   'part4-warehouse-safety-briefing','part4-training-registration',
   'part4-travel-service-update','part4-quarterly-inventory-report',
  }
  practice_seen=set()
  for unit in document['listening']:
   if unit.get('id') not in practice_only_part4_ids:
    continue
   questions=unit.get('questions') or []
   if len(questions)!=4 or questions[3].get('mockEligible') is not False:
    raise AssertionError(f"Unexpected Part 4 practice-only addition: {unit.get('id')}")
   practice_seen.add(unit['id'])
   unit['questions']=questions[:3]
  self.assertEqual(practice_seen,practice_only_part4_ids)
  historical=json.dumps(document,ensure_ascii=False,indent=2).encode('utf-8') + bytes([10])
  self.assertEqual(self.batch['listening_sha256'],hashlib.sha256(historical).hexdigest())
  self.assertEqual(len(set(self.batch['listening'])),16)

 def test_v29583_part4_practice_additions_are_exact_and_mock_excluded(self):
  expected_ids={
   'part4-office-announcement','part4-conference-update',
   'part4-safety-announcement','part4-product-launch',
   'part4-quarterly-town-hall','part4-customer-voicemail',
   'part4-warehouse-safety-briefing','part4-training-registration',
   'part4-travel-service-update','part4-quarterly-inventory-report',
  }
  for unit_id in expected_ids:
   unit=self.by_id[unit_id]
   self.assertEqual(len(unit['questions']),4,unit_id)
   added=unit['questions'][3]
   self.assertIs(added.get('mockEligible'),False,unit_id)
   self.assertEqual(added['choiceIds'],[f'listening:{unit_id}:4:choice:{i}' for i in range(1,5)])

 def test_all_batch_units_exist_and_are_review_gated(self):
  for unit_id in self.batch['listening']:
   unit=self.by_id[unit_id]
   self.assertEqual(unit['contentSource'],'original-editorial')
   self.assertEqual(unit['editorialStatus'],'reserve-pending-independent-review')
   self.assertEqual(unit['editorialBatch'],'027')
   self.assertEqual(unit['contentBatch'],'batch-027-listening-expansion')
   self.assertEqual(unit['mockExamEligibility'],'excluded-until-independent-review')
   self.assertTrue(unit.get('reviewNote'))
 def test_parts_and_question_count_are_exact(self):
  counts={part:0 for part in ('Part 2','Part 3','Part 4')}; questions=0
  for unit_id in self.batch['listening']:
   unit=self.by_id[unit_id]; counts[unit['part']]+=1; questions+=len(unit['questions'])
   self.assertTrue(unit['title'].strip()); self.assertTrue(unit['topic'].strip()); self.assertTrue(unit['transcriptTranslation'].strip())
   self.assertGreaterEqual(len(unit['segments']),1); self.assertGreaterEqual(len(unit['vocabulary']),2)
  self.assertEqual(counts,{'Part 2':8,'Part 3':4,'Part 4':4}); self.assertEqual(questions,32)
 def test_question_choices_answers_explanations_and_ids(self):
  ids=set(); total=0
  for unit_id in self.batch['listening']:
   unit=self.by_id[unit_id]
   transcript=' '.join(segment['text'] for segment in unit['segments'])
   for q in unit['questions']:
    total+=1; self.assertTrue(q['question'].strip()); self.assertTrue(q['explanation'].strip())
    self.assertIn(q['answerIndex'],range(len(q['choices']))); self.assertGreaterEqual(len(q['choices']),3)
    self.assertEqual(len(q['choiceIds']),len(q['choices']))
    for cid in q['choiceIds']: self.assertNotIn(cid,ids); ids.add(cid)
    self.assertIn(q['evidenceText'].casefold(),transcript.casefold())
    if unit['part'] in ('Part 3','Part 4'): self.assertGreaterEqual(len(transcript.split()),20)
  self.assertEqual(total,32); self.assertEqual(len(ids),sum(len(q['choices']) for uid in self.batch['listening'] for q in self.by_id[uid]['questions']))
 def test_all_batch_units_are_mapped_to_their_learning_objectives(self):
  objectives=read('data/learning-path/objective-resource-map.json')['objectives']
  mapping={x['id']:set(x['resourceIds']) for x in objectives}
  for unit_id in self.batch['listening']:
   part=self.by_id[unit_id]['part']
   objective_id={'Part 2':'listening-part-2','Part 3':'listening-part-3','Part 4':'listening-part-4'}[part]
   self.assertIn(unit_id,mapping[objective_id],unit_id)

 def test_no_batch_question_id_collision_with_existing_library(self):
  existing={cid for unit in self.units if unit['id'] not in self.batch['listening'] for q in unit.get('questions',[]) for cid in q.get('choiceIds',[])}
  batch={cid for uid in self.batch['listening'] for q in self.by_id[uid]['questions'] for cid in q['choiceIds']}
  self.assertFalse(existing.intersection(batch))
if __name__=='__main__': unittest.main()
