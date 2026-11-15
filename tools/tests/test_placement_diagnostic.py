"""Regression checks for the short, non-certifying placement diagnostic."""
import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class PlacementDiagnosticTests(unittest.TestCase):
 def test_question_bank_is_balanced_and_valid(self):
  data=json.loads((ROOT/"data/learning-path/placement-diagnostic.json").read_text(encoding="utf-8"))
  qs=data["questions"]; self.assertEqual(len(qs),16)
  self.assertEqual([sum(q["level"]==lv for q in qs) for lv in ("PRE-A1","A1","A2","B1")],[4,4,4,4])
  self.assertEqual(len({q["id"] for q in qs}),16)
  for q in qs:
   self.assertEqual(len(q["choices"]),4); self.assertIn(q["answerIndex"],range(4)); self.assertTrue(q["rationale"])
 def test_diagnostic_is_not_claimed_as_cefr_or_four_skill_test(self):
  data=json.loads((ROOT/"data/learning-path/placement-diagnostic.json").read_text(encoding="utf-8"))
  self.assertIn("không phải chứng chỉ",data["description"])
  js=(ROOT/"assets/js/app.js").read_text(encoding="utf-8")
  self.assertIn("chưa đánh giá nghe, nói, viết",js)
  self.assertIn("toeic:placement-diagnostic:v1",js)
 def test_user_must_apply_recommendation_and_can_retry(self):
  js=(ROOT/"assets/js/app.js").read_text(encoding="utf-8")
  self.assertIn("data-placement-apply",js); self.assertIn("data-placement-retry",js)
  self.assertIn("toeic:learning-start-level:v1",js)
 def test_service_worker_precaches_diagnostic(self):
  sw=(ROOT/"sw.js").read_text(encoding="utf-8")
  self.assertEqual(sw.count("./data/learning-path/placement-diagnostic.json"),2)

 def test_objective_map_covers_every_question_and_reports_domains(self):
  diagnostic=json.loads((ROOT/"data/learning-path/placement-diagnostic.json").read_text(encoding="utf-8"))
  mapping=json.loads((ROOT/"data/learning-path/placement-objective-map.json").read_text(encoding="utf-8"))
  mapped=mapping["questionMappings"]
  self.assertEqual({x["questionId"] for x in mapped},{q["id"] for q in diagnostic["questions"]})
  self.assertTrue({x["domain"] for x in mapped}>={"vocabulary","grammar","reading"})
  self.assertTrue(all(x.get("objectiveId") and x.get("domainLabel") for x in mapped))
  js=(ROOT/"assets/js/app.js").read_text(encoding="utf-8")
  self.assertIn("Kết quả theo nhóm nội dung",js)
  self.assertIn("placementObjectiveMap",js)
 def test_service_worker_precaches_objective_map(self):
  sw=(ROOT/"sw.js").read_text(encoding="utf-8")
  self.assertEqual(sw.count("./data/learning-path/placement-objective-map.json"),2)

if __name__=="__main__": unittest.main()
