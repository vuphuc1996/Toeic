import hashlib
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FoundationA2ProductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.curriculum = json.loads((ROOT / 'data/learning-path/pre-a1-a1.json').read_text(encoding='utf-8'))
        cls.a2 = [lesson for lesson in cls.curriculum['lessons'] if lesson.get('level') == 'A2']
        cls.baseline = json.loads((ROOT / 'tools/foundation-a2-production-baseline-v2.78.0.json').read_text(encoding='utf-8'))

    def test_all_thirteen_a2_lessons_have_individual_production_tasks(self):
        self.assertEqual(len(self.a2), 13)
        ids = [lesson['productionTask']['id'] for lesson in self.a2]
        self.assertEqual(len(ids), len(set(ids)))
        for lesson in self.a2:
            self.assertNotEqual(lesson['productionTask']['id'], lesson['applicationTask']['id'])
            self.assertEqual(lesson['productionTask']['id'], f"{lesson['id']}::produce1")

    def test_task_prompts_are_contextual_and_scaffolded(self):
        for lesson in self.a2:
            task = lesson['productionTask']
            with self.subTest(lesson=lesson['id']):
                self.assertGreaterEqual(len(task['scenario']), 30)
                self.assertGreaterEqual(len(task['instruction']), 30)
                self.assertEqual(len(task['requirements']), 3)
                self.assertTrue(task['sentenceFrame'])
                self.assertEqual(task['minimumWords'], 8)

    def test_custom_rubric_and_model_answer_are_complete(self):
        for lesson in self.a2:
            task = lesson['productionTask']
            with self.subTest(lesson=lesson['id']):
                self.assertEqual(len(task['rubric']), 3)
                self.assertTrue(all(label.strip() for label in task['rubric']))
                self.assertTrue(task['modelAnswer'])
                self.assertGreaterEqual(len(task['requiredFeatures']), 2)
                model = task['modelAnswer'].casefold()
                for feature in task['requiredFeatures']:
                    self.assertIn(feature.casefold(), model)
                self.assertGreaterEqual(len(task['modelAnswer'].split()), task['minimumWords'])

    def test_production_evidence_is_additive_and_distinct_from_application(self):
        for lesson in self.a2:
            task = lesson['productionTask']
            self.assertEqual(task['evidenceType'], 'learner-authored-contextual-production')
            self.assertNotEqual(task['id'], lesson['applicationTask']['id'])


    def test_production_task_content_matches_immutable_release_baseline(self):
        rows = {row['lessonId']: row for row in self.baseline['tasks']}
        self.assertEqual(len(rows), 13)
        for lesson in self.a2:
            task = dict(lesson['productionTask'])
            task.pop('revisionChecklist', None)
            task.pop('revisionHint', None)
            canonical = json.dumps(task, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            with self.subTest(lesson=lesson['id']):
                self.assertEqual(rows[lesson['id']]['id'], task['id'])
                self.assertEqual(rows[lesson['id']]['sha256'], hashlib.sha256(canonical).hexdigest())

    def test_legacy_production_records_are_not_reused_as_new_a2_evidence(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        evidence = (ROOT / 'assets/js/foundation-evidence.js').read_text(encoding='utf-8')
        self.assertIn('legacyProductionSaved', app)
        self.assertIn('Bài tự tạo từ phiên bản trước vẫn được giữ', app)
        self.assertIn('lesson.productionTask?.id || lesson.applicationTask?.id', evidence)

    def test_javascript_evidence_and_rendering_contract(self):
        result = subprocess.run(
            ['node', str(ROOT / 'tools/tests/foundation-a2-production.mjs')],
            cwd=ROOT, capture_output=True, text=True, timeout=30
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('PASS:', result.stdout)


if __name__ == '__main__':
    unittest.main()
