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
  self.assertTrue(all(o['status']=='criteria_defined_not_yet_instrumented' for x in registry['objectives'] for o in x['outcomes']))
 def test_outcome_registry_is_precached(self):
  sw=(ROOT/'sw.js').read_text()
  self.assertEqual(sw.count('./data/learning-path/objective-outcomes.json'),2)
if __name__=='__main__': unittest.main()
