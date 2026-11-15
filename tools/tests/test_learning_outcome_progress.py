import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class LearningOutcomeProgressTests(unittest.TestCase):
    def test_objective_progress_runtime(self):
        result = subprocess.run(['node', str(ROOT / 'tools/tests/learning-outcome-progress.mjs')], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_runtime_is_wired_to_all_toeic_practice_areas(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn("dbGet('objectiveProgress')", app)
        self.assertGreaterEqual(app.count('trackObjectivePractice(id,'), 3)
        self.assertIn("q.mode==='sentence-completion'", app)
        self.assertIn("dbSet('objectiveProgress'", app)

    def test_dashboard_and_service_worker_include_tracker(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        sw = (ROOT / 'sw.js').read_text(encoding='utf-8')
        self.assertIn('id="learningObjectiveProgress"', html)
        self.assertEqual(sw.count('./assets/js/learning-outcome-progress.js'), 2)

if __name__ == '__main__':
    unittest.main()
