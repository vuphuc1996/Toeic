import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('answer_leakage_audit', ROOT / 'tools/audit-answer-leakage.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AnswerLeakageAuditTests(unittest.TestCase):
    def test_question_stem_lexical_cue_is_flagged_but_not_called_invalid(self):
        result = MODULE.score('When is the meeting scheduled?',
                              ['The meeting is scheduled Thursday', 'By Friday', 'Next month', 'At noon'], 0)
        self.assertIn('KEY_STEM_LEXICAL_CUE', result['flags'])
        self.assertNotIn('invalid', ' '.join(result['flags']).casefold())

    def test_semantic_paraphrase_is_not_claimed_to_be_detected(self):
        result = MODULE.score('What caused the delay?',
                              ['Road construction near the center', 'A billing error', 'A staff meeting', 'A product return'], 0)
        self.assertIsInstance(result['stem_overlap'], float)
        self.assertNotIn('SEMANTIC_ERROR', result['flags'])

    def test_high_key_distractor_overlap_is_flagged(self):
        result = MODULE.score('Which item was ordered?',
                              ['Office supply delivery', 'Office supply delivery date', 'Customer refund request', 'Staff training session'], 0)
        self.assertIn('KEY_DISTRACTOR_HIGH_OVERLAP', result['flags'])

    def test_unusually_long_key_is_flagged(self):
        result = MODULE.score('What is requested?',
                              ['Please submit the completed application form before the end of the business day', 'A refund', 'A new desk', 'More staff'], 0)
        self.assertIn('KEY_UNUSUALLY_LONG', result['flags'])

    def test_invalid_answer_index_is_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.score('Question?', ['A', 'B', 'C', 'D'], 4)

    def test_reading_reserve_questions_are_excluded_from_mock_triage_scope(self):
        reading = json.loads((ROOT / 'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']
        part7 = [x for x in reading if x.get('part') == 'Part 7']
        eligible = [x for x in part7 if x.get('editorialStatus') != 'reserve-pending-independent-review']
        reserve = [x for x in part7 if x.get('editorialStatus') == 'reserve-pending-independent-review']
        self.assertEqual(sum(len(x.get('questions', [])) for x in eligible), 108)
        self.assertEqual(sum(len(x.get('questions', [])) for x in reserve), 87)

    def test_audit_does_not_mutate_question_libraries(self):
        paths = [ROOT / 'data/listening/listening-library.json', ROOT / 'data/readings/reading-library.json']
        before = [hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
        for p in paths:
            json.loads(p.read_text(encoding='utf-8'))
        after = [hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
        self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main()
