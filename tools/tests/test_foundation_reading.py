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
    def test_all_passages_map_one_to_each_stable_lesson(self):
        lessons=json.loads((ROOT/'data/learning-path/pre-a1-a1.json').read_text(encoding='utf-8'))['lessons']
        lesson_ids={x['id'] for x in lessons}
        self.assertEqual(len(self.data['passages']),23)
        self.assertEqual({x['lessonId'] for x in self.data['passages']},lesson_ids)
    def test_a2_passages_map_one_to_each_a2_lesson(self):
        lessons=json.loads((ROOT/'data/learning-path/pre-a1-a1.json').read_text(encoding='utf-8'))['lessons']
        a2_ids={x['id'] for x in lessons if x['level']=='A2'}
        a2_passages={x['lessonId'] for x in self.data['passages'] if x.get('level')=='A2'}
        self.assertEqual(len(a2_passages),13)
        self.assertEqual(a2_passages,a2_ids)

    def test_each_passage_has_level_appropriate_independent_questions(self):
        ids=[]
        for passage in self.data['passages']:
            expected_questions = 3 if passage.get('level') == 'A2' else 2
            self.assertGreaterEqual(len(passage['text'].split()), 65 if passage.get('level') == 'A2' else 20)
            self.assertLessEqual(len(passage['text'].split()), 90)
            self.assertEqual(len(passage['questions']), expected_questions)
            if passage.get('level') == 'A2':
                self.assertEqual(passage.get('minimumUniqueQuestions'), 3)
                self.assertEqual(passage.get('practiceAccuracyThreshold'), 0.67)
            for q in passage['questions']:
                self.assertEqual(len(q['choices']),4)
                self.assertIn(q['answerIndex'],range(4))
                self.assertTrue(q['rationale'])
                ids.append(q['id'])
        self.assertEqual(len(ids),59)
        self.assertEqual(len(ids),len(set(ids)))
    def test_answer_positions_are_not_biased(self):
        counts=[0,0,0,0]
        for p in self.data['passages']:
            for q in p['questions']: counts[q['answerIndex']]+=1
        self.assertEqual(counts,[15,15,15,14])
    def test_a2_original_question_pairs_match_v275_baseline(self):
        import hashlib
        baseline = json.loads((ROOT / 'tools/foundation-a2-question-baseline-v2.75.0.json').read_text(encoding='utf-8'))
        for passage in self.data['passages']:
            if passage.get('level') != 'A2':
                continue
            payload = json.dumps(passage['questions'][:2], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            self.assertEqual(hashlib.sha256(payload).hexdigest(), baseline['resources']['reading'][passage['lessonId']])

    def test_a2_passages_add_a_third_distinct_comprehension_question(self):
        a2 = [x for x in self.data['passages'] if x.get('level') == 'A2']
        self.assertEqual(len(a2), 13)
        for passage in a2:
            self.assertTrue(65 <= len(passage['text'].split()) <= 90)
            self.assertEqual([q['id'].rsplit('::', 1)[-1] for q in passage['questions']], ['q1', 'q2', 'q3'])
            q3 = passage['questions'][2]
            self.assertIn(q3['skill'], {'infer-from-details','understand-sequence','understand-time-reference','find-detail','understand-condition','understand-purpose-context'})
            self.assertTrue(q3['rationale'].strip())
            self.assertEqual(len(q3['choices']), 4)
            self.assertEqual(len(set(q3['choices'])), 4)

    def test_path_cards_use_per_resource_question_count_and_practice_threshold(self):
        self.assertIn("const readingResource=(state.foundationReadingPassages||[]).find(item=>item.lessonId===lesson.id);", self.app)
        self.assertIn("readingResource?.questions?.length||2", self.app)
        self.assertIn("readingResource?.minimumUniqueQuestions||2", self.app)
        self.assertIn("readingResource?.practiceAccuracyThreshold||0.8", self.app)
        self.assertIn("${reading.uniqueQuestions}/${readingTarget} câu", self.app)

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
        self.assertEqual(policy['a2MinimumUniqueQuestions'], 3)
        self.assertEqual(policy['a2PracticeAccuracyThreshold'], 0.67)
        self.assertIn('not CEFR', policy['scope'])
if __name__=='__main__': unittest.main()
