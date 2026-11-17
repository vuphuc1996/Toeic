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
        cls.refresh = json.loads((ROOT / 'tools/foundation-a2-production-refresh-v2.87.0.json').read_text(encoding='utf-8'))

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
        refresh = self.refresh
        self.assertEqual(len(rows), 13)
        self.assertEqual(refresh['version'], '2.87.0')
        self.assertEqual(refresh['baselineVersion'], self.baseline['version'])
        self.assertTrue(refresh['onlyDeclaredFieldChanged'])
        self.assertTrue(refresh['taskIdUnchanged'])
        self.assertTrue(refresh['applicationTaskUnchanged'])
        self.assertTrue(refresh['questionBankUnchanged'])
        self.assertFalse(refresh['learnerProgressTouched'])
        self.assertFalse(refresh['indexedDbSchemaChanged'])
        self.assertFalse(refresh['automaticLanguageGradingAdded'])
        for lesson in self.a2:
            task = dict(lesson['productionTask'])
            task.pop('revisionChecklist', None)
            task.pop('revisionHint', None)
            canonical = json.dumps(task, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            digest = hashlib.sha256(canonical).hexdigest()
            with self.subTest(lesson=lesson['id']):
                self.assertEqual(rows[lesson['id']]['id'], task['id'])
                if lesson['id'] == refresh['lessonId']:
                    self.assertEqual(rows[lesson['id']]['sha256'], refresh['oldSha256'])
                    self.assertEqual(task['id'], refresh['taskId'])
                    self.assertEqual(task[refresh['fieldChanged']], refresh['newValue'])
                    reconstructed = dict(task)
                    reconstructed[refresh['fieldChanged']] = refresh['oldValue']
                    reconstructed_digest = hashlib.sha256(json.dumps(reconstructed, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
                    self.assertEqual(reconstructed_digest, refresh['oldSha256'])
                    self.assertEqual(digest, refresh['newSha256'])
                else:
                    self.assertEqual(rows[lesson['id']]['sha256'], digest)

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
