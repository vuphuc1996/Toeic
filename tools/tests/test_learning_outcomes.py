import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class LearningOutcomeTests(unittest.TestCase):
 def test_audit_passes(self):
  r=subprocess.run([sys.executable,str(ROOT/'tools/audit-learning-outcomes.py')],capture_output=True,text=True)
  self.assertEqual(r.returncode,0,r.stdout+r.stderr)
 def test_all_objectives_have_three_criteria_and_no_mastery_claim(self):
  mapping=json.loads((ROOT/'data/learning-path/objective-resource-map.json').read_text())['objectives']
  registry=json.loads((ROOT/'data/learning-path/objective-outcomes.json').read_text())
  self.assertEqual({x['objectiveId'] for x in registry['objectives']},{x['id'] for x in mapping})
  self.assertTrue(all(len(x['outcomes'])==3 for x in registry['objectives']))
  allowed={'criteria_defined_not_yet_instrumented','instrumented_practice_evidence','instrumented_learner_self_report','instrumented_delayed_recall'}
  self.assertTrue(all(o['status'] in allowed for x in registry['objectives'] for o in x['outcomes']))
  foundation=[o for x in registry['objectives'] if x['objectiveId'].startswith('foundation-') for o in x['outcomes']]
  self.assertEqual(len(foundation),6)
  self.assertTrue(all(o['status'].startswith('instrumented_') for o in foundation))
  self.assertTrue(all(isinstance(x.get('runtimeWiring'), dict) for x in registry['objectives']))
 def test_evidence_report_maps_all_33_criteria_reproducibly(self):
  import tempfile
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'evidence.md'
   r=subprocess.run([sys.executable,str(ROOT/'tools/audit-learning-outcome-evidence.py'),'--markdown-output',str(out)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stdout+r.stderr)
   text=out.read_text(encoding='utf-8')
   self.assertIn('29/33 (87.9%)',text)
   self.assertIn('23/27',text)
   self.assertIn('1,119',text)
   self.assertIn('638 unique question IDs',text)
   self.assertIn('11/11',text)
   for obj in json.loads((ROOT/'data/learning-path/objective-outcomes.json').read_text())['objectives']:
    for o in obj['outcomes']:
     self.assertIn(o['id'],text)
 def test_outcome_registry_is_precached(self):
  sw=(ROOT/'sw.js').read_text()
  self.assertEqual(sw.count('./data/learning-path/objective-outcomes.json'),2)
  self.assertEqual(sw.count('./data/learning-path/objective-criterion-map.json'),2)
 def test_criterion_statuses_match_the_question_map(self):
  mapping=json.loads((ROOT/'data/learning-path/objective-criterion-map.json').read_text())
  registry=json.loads((ROOT/'data/learning-path/objective-outcomes.json').read_text())
  mapped={row['criterionId'] for row in mapping['mappings']}
  toeic=[o for group in registry['objectives'] if not group['objectiveId'].startswith('foundation-') for o in group['outcomes']]
  self.assertEqual(mapped,{o['id'] for o in toeic if o['status'].startswith('instrumented_')})
  self.assertEqual(sum(o['status'].startswith('instrumented_') for o in toeic),23)
  self.assertEqual(sum(o['status']=='criteria_defined_not_yet_instrumented' for o in toeic),4)
if __name__=='__main__': unittest.main()
