"""Quality and integration checks for Foundation short reading."""
import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
class FoundationReadingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/'data/learning-path/foundation-reading.json').read_text(encoding='utf-8'))
        cls.app=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
        cls.sw=(ROOT/'sw.js').read_text(encoding='utf-8')
    def test_ten_passages_map_one_to_each_stable_lesson(self):
        lessons=json.loads((ROOT/'data/learning-path/pre-a1-a1.json').read_text(encoding='utf-8'))['lessons']
        lesson_ids={x['id'] for x in lessons}
        self.assertEqual(len(self.data['passages']),10)
        self.assertEqual({x['lessonId'] for x in self.data['passages']},lesson_ids)
    def test_each_passage_has_two_independent_questions(self):
        ids=[]
        for passage in self.data['passages']:
            self.assertGreaterEqual(len(passage['text'].split()),20)
            self.assertLessEqual(len(passage['text'].split()),90)
            self.assertEqual(len(passage['questions']),2)
            for q in passage['questions']:
                self.assertEqual(len(q['choices']),4)
                self.assertIn(q['answerIndex'],range(4))
                self.assertTrue(q['rationale'])
                ids.append(q['id'])
        self.assertEqual(len(ids),20)
        self.assertEqual(len(ids),len(set(ids)))
    def test_answer_positions_are_not_biased(self):
        counts=[0,0,0,0]
        for p in self.data['passages']:
            for q in p['questions']: counts[q['answerIndex']]+=1
        self.assertEqual(counts,[5,5,5,5])
    def test_evidence_is_separate_and_integrated(self):
        self.assertIn("toeic:foundation-reading-progress:v1",self.app)
        self.assertIn('recordFoundationReadingAttempt',self.app)
        self.assertIn('data-foundation-reading-answer',self.app)
        self.assertIn('./assets/js/foundation-reading-evidence.js',self.sw)
        self.assertIn('./data/learning-path/foundation-reading.json',self.sw)
    def test_threshold_is_explicit_and_not_cefr(self):
        policy=self.data['evidencePolicy']
        self.assertEqual(policy['minimumUniqueQuestions'],2)
        self.assertEqual(policy['practiceAccuracyThreshold'],0.8)
        self.assertIn('not CEFR',policy['scope'])
if __name__=='__main__': unittest.main()
