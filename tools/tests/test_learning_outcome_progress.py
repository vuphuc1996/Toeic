import subprocess
import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class LearningOutcomeProgressTests(unittest.TestCase):
    def test_objective_progress_runtime(self):
        result = subprocess.run(['node', str(ROOT / 'tools/tests/learning-outcome-progress.mjs')], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_runtime_is_wired_to_all_toeic_practice_areas(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn("dbGet('objectiveProgress')", app)
        self.assertIn('function stagePracticeBatchAnswer(', app)
        self.assertIn('async function confirmPracticeBatchResult(', app)
        self.assertIn('trackObjectivePractice(batch.id,{...question,__index:row.index}', app)
        self.assertIn('trackObjectivePractice(q.id,{id:q.id,choiceIds:[`part5:${q.id}`]},pending.correct', app)
        self.assertIn('grammar:{items:state.grammarLessons', app)
        self.assertIn('reading:{items:state.readings', app)
        self.assertIn('listening:{items:state.listening', app)
        self.assertIn('function objectiveCriterionQuestionKey(question)', app)
        self.assertIn('state.objectiveCriterionIndex=buildObjectiveCriterionIndex', app)
        self.assertIn("recordObjectiveAttempt(state.objectiveProgress, criterionIds, criterionKey", app)
        self.assertIn("document.addEventListener('click',async e=>{\n    const save=e.target.closest('[data-save-outcome-rubric]')", app)
        self.assertIn("q.mode==='sentence-completion'", app)
        self.assertIn("dbSet('objectiveProgress'", app)
        self.assertIn('function renderLearningOutcomeCriteria()', app)
        self.assertIn('function findStableChoiceQuestionIndex(', app)
        self.assertIn('state.foundationOutcomeRegistry, state.objectiveCriterionMap', app)
        self.assertIn('learningOutcomeCriteria', html)

    def test_dashboard_and_service_worker_include_tracker(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        sw = (ROOT / 'sw.js').read_text(encoding='utf-8')
        self.assertIn('id="learningObjectiveProgress"', html)
        required = json.loads(sw.split("const REQUIRED = ", 1)[1].split(";", 1)[0])
        shell = json.loads(sw.split("const APP_SHELL = ", 1)[1].split(";", 1)[0])
        version = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))['version']
        for resources in (required, shell):
            self.assertIn('./assets/js/learning-outcome-progress.js', resources)
            self.assertIn(f'./assets/js/learning-outcome-progress.js?__release={version}', resources)
            self.assertIn('./data/learning-path/objective-criterion-map.json', resources)

    def test_criterion_runtime_regressions(self):
        result = subprocess.run(['node', str(ROOT / 'tools/tests/learning-outcome-criterion-progress.mjs')], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

if __name__ == '__main__':
    unittest.main()
