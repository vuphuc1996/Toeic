import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class ObjectiveCriterionMapTests(unittest.TestCase):
    def test_canonical_question_mapping_audit(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/audit-objective-criterion-map.py")],
            cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("1082 question-to-criterion links", result.stdout)
        self.assertIn("638 unique stable question IDs", result.stdout)
        self.assertIn("22/27 TOEIC criteria mapped", result.stdout)
        self.assertIn("0 Listening reserve items mapped", result.stdout)

    def test_registry_and_mapping_counts_are_reconciled(self):
        import json
        mapping = json.loads((ROOT / "data/learning-path/objective-criterion-map.json").read_text(encoding="utf-8"))
        registry = json.loads((ROOT / "data/learning-path/objective-outcomes.json").read_text(encoding="utf-8"))
        outcomes = {outcome["id"]: (group["objectiveId"], outcome) for group in registry["objectives"] for outcome in group["outcomes"]}
        counts = {}
        for row in mapping["mappings"]:
            counts[row["criterionId"]] = counts.get(row["criterionId"], 0) + 1
            self.assertIn(row["criterionId"], outcomes)
            self.assertEqual(outcomes[row["criterionId"]][0], row["objectiveId"])
        self.assertEqual(counts, mapping["mappingCountsByCriterion"])
        self.assertEqual(len({row["questionKey"] for row in mapping["mappings"]}), mapping["uniqueQuestionCount"])
        self.assertEqual(len(counts), 22)
        toeic = [outcome for group in registry["objectives"] if not group["objectiveId"].startswith("foundation-") for outcome in group["outcomes"]]
        self.assertEqual(sum(outcome["status"].startswith("instrumented_") for outcome in toeic), 22)
        self.assertEqual(sum(outcome["status"] == "criteria_defined_not_yet_instrumented" for outcome in toeic), 5)

if __name__ == "__main__":
    unittest.main()
