"""Focused A2 assessment-quality regression checks for v2.77.0."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


class FoundationA2AssessmentQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reading = load('data/learning-path/foundation-reading.json')['passages']
        cls.listening = load('data/learning-path/foundation-listening.json')['clips']
        cls.review = load('tools/foundation-a2-assessment-review-v2.77.0.json')

    def find(self, items, lesson_id):
        return next(item for item in items if item.get('lessonId') == lesson_id)

    def test_a2_questions_have_four_unique_options_valid_keys_and_rationales(self):
        for modality, items in (('Reading', self.reading), ('Listening', self.listening)):
            with self.subTest(modality=modality):
                a2 = [item for item in items if item.get('level') == 'A2']
                self.assertEqual(len(a2), 13)
                for item in a2:
                    self.assertEqual(len(item['questions']), 3, item['lessonId'])
                    for question in item['questions']:
                        self.assertEqual(len(question['choices']), 4, question['id'])
                        self.assertEqual(len({choice.casefold().strip() for choice in question['choices']}), 4, question['id'])
                        self.assertIn(question['answerIndex'], range(4), question['id'])
                        self.assertTrue(question.get('prompt', '').strip(), question['id'])
                        self.assertTrue(question.get('rationale', '').strip(), question['id'])

    def test_each_a2_resource_q2_and_q3_test_different_correct_information(self):
        for modality, items in (('Reading', self.reading), ('Listening', self.listening)):
            for item in items:
                if item.get('level') != 'A2':
                    continue
                q2, q3 = item['questions'][1:3]
                a2 = q2['choices'][q2['answerIndex']].casefold().strip(' .')
                a3 = q3['choices'][q3['answerIndex']].casefold().strip(' .')
                self.assertNotEqual(a2, a3, f'{modality}/{item["lessonId"]}')

    def test_revised_reading_questions_address_prior_repetition(self):
        quantities = self.find(self.reading, 'a2-quantities')['questions'][2]
        comparisons = self.find(self.reading, 'a2-comparisons')['questions'][2]
        visitors = self.find(self.reading, 'a2-obligation-permission')['questions'][2]
        self.assertEqual(quantities['prompt'], 'What does the delivery information allow the training team to do?')
        self.assertEqual(quantities['choices'][quantities['answerIndex']], 'Prepare the materials on time.')
        self.assertEqual(comparisons['choices'][comparisons['answerIndex']], 'The customer values dependable, on-time delivery more than the cheapest option.')
        self.assertEqual(visitors['choices'][visitors['answerIndex']], 'Return the visitor badge to security staff.')

    def test_revised_listening_questions_separate_comparison_and_process_sequence(self):
        comparison = self.find(self.listening, 'a2-comparisons')['questions']
        sequence = self.find(self.listening, 'a2-sequencing-instructions')['questions']
        self.assertEqual(comparison[1]['choices'][comparison[1]['answerIndex']], 'The documents are urgent')
        self.assertEqual(comparison[2]['prompt'], 'What advantage of the second service does Nina mention?')
        self.assertEqual(comparison[2]['choices'][comparison[2]['answerIndex']], 'It is more reliable and usually arrives on time.')
        self.assertEqual(sequence[1]['choices'][sequence[1]['answerIndex']], 'Update the inventory record')
        self.assertEqual(sequence[2]['choices'][sequence[2]['answerIndex']], 'Inspect the product and record its condition.')

    def test_source_evidence_registry_has_five_exactly_supported_questions(self):
        registry = {item['id']: item['evidenceText'] for item in self.review['reviewedQuestions']}
        self.assertEqual(len(registry), 5)
        all_items = {
            q['id']: (item.get('text') or '\n'.join(s.get('text', '') for s in item.get('segments', [])), q)
            for items in (self.reading, self.listening)
            for item in items if item.get('level') == 'A2'
            for q in item['questions']
        }
        self.assertEqual(set(registry), {qid for qid, (_source, q) in all_items.items() if q.get('evidenceText')})
        for qid, evidence in registry.items():
            source, question = all_items[qid]
            self.assertEqual(question['evidenceText'], evidence)
            self.assertIn(evidence, source, qid)

    def test_full_foundation_answer_positions_remain_balanced(self):
        for modality, items in (('Reading', self.reading), ('Listening', self.listening)):
            questions = [q for item in items for q in item['questions']]
            counts = [sum(q['answerIndex'] == i for q in questions) for i in range(4)]
            self.assertEqual(counts, [15, 15, 15, 14], modality)

    def test_a2_question_pairs_from_v275_remain_unchanged(self):
        import hashlib
        baseline = load('tools/foundation-a2-question-baseline-v2.75.0.json')
        for modality, items in (('reading', self.reading), ('listening', self.listening)):
            for item in items:
                if item.get('level') != 'A2':
                    continue
                payload = json.dumps(item['questions'][:2], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
                self.assertEqual(hashlib.sha256(payload).hexdigest(), baseline['resources'][modality][item['lessonId']], item['lessonId'])

    def test_standalone_a2_quality_audit_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'tools/audit-foundation-a2-assessment.py')],
            cwd=ROOT, capture_output=True, text=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('PASS', result.stdout)


if __name__ == '__main__':
    unittest.main()
