import hashlib
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FoundationProductionRevisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'data/learning-path/pre-a1-a1.json').read_text(encoding='utf-8'))
        cls.a2 = [item for item in cls.data['lessons'] if item.get('level') == 'A2']
        cls.base = json.loads((ROOT / 'tools/foundation-a2-production-baseline-v2.78.0.json').read_text(encoding='utf-8'))
        cls.refresh = json.loads((ROOT / 'tools/foundation-a2-production-refresh-v2.87.0.json').read_text(encoding='utf-8'))
        cls.revision_base = json.loads((ROOT / 'tools/foundation-a2-revision-baseline-v2.79.0.json').read_text(encoding='utf-8'))

    def test_all_a2_tasks_have_individual_revision_checklists_and_hints(self):
        self.assertEqual(len(self.a2), 13)
        for lesson in self.a2:
            task = lesson['productionTask']
            with self.subTest(lesson=lesson['id']):
                self.assertEqual(len(task.get('revisionChecklist', [])), 3)
                self.assertTrue(all(len(item.strip()) >= 12 for item in task['revisionChecklist']))
                self.assertGreaterEqual(len(task.get('revisionHint', '')), 50)

    def test_v278_production_content_remains_unchanged_except_logged_v287_scenario_refresh(self):
        rows = {row['lessonId']: row for row in self.base['tasks']}
        refresh = self.refresh
        self.assertEqual(refresh['baselineVersion'], self.base['version'])
        self.assertTrue(refresh['onlyDeclaredFieldChanged'])
        for lesson in self.a2:
            task = dict(lesson['productionTask'])
            task.pop('revisionChecklist', None)
            task.pop('revisionHint', None)
            canonical = json.dumps(task, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            digest = hashlib.sha256(canonical).hexdigest()
            if lesson['id'] == refresh['lessonId']:
                self.assertEqual(rows[lesson['id']]['sha256'], refresh['oldSha256'])
                reconstructed = dict(task)
                reconstructed[refresh['fieldChanged']] = refresh['oldValue']
                old_payload = json.dumps(reconstructed, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
                self.assertEqual(hashlib.sha256(old_payload).hexdigest(), refresh['oldSha256'])
                self.assertEqual(digest, refresh['newSha256'])
            else:
                self.assertEqual(digest, rows[lesson['id']]['sha256'])

    def test_revision_guide_matches_v279_integrity_baseline(self):
        rows = {row['lessonId']: row for row in self.revision_base['tasks']}
        self.assertEqual(len(rows), 13)
        for lesson in self.a2:
            task = lesson['productionTask']
            material = {'id': task['id'], 'revisionChecklist': task['revisionChecklist'], 'revisionHint': task['revisionHint']}
            canonical = json.dumps(material, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            with self.subTest(lesson=lesson['id']):
                self.assertEqual(rows[lesson['id']]['id'], task['id'])
                self.assertEqual(rows[lesson['id']]['sha256'], hashlib.sha256(canonical).hexdigest())

    def test_initial_response_history_is_additive_and_non_destructive(self):
        source = (ROOT / 'assets/js/foundation-evidence.js').read_text(encoding='utf-8')
        self.assertIn('attempts.push({ response, ratings:', source)
        self.assertIn('initialResponse: item.initialResponse || item.latestResponse || response', source)
        self.assertIn('recordFoundationProductionRevision', source)
        self.assertIn('basedOnResponse: previousResponse', source)

    def test_revision_ui_requires_review_and_self_assessment(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn('data-foundation-production-revision-save', app)
        self.assertIn('data-foundation-revision-check', app)
        self.assertIn('data-foundation-revision-text', app)
        self.assertIn('reviewChecks.some(value=>!value)', app)
        self.assertIn('ratings.some(value=>value===null)', app)
        self.assertIn('Bản trước để đối chiếu', app)

    def test_javascript_revision_engine_passes(self):
        result = subprocess.run(
            ['node', str(ROOT / 'tools/tests/foundation-production-revision.mjs')],
            cwd=ROOT, capture_output=True, text=True, timeout=30
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('PASS:', result.stdout)


if __name__ == '__main__':
    unittest.main()
