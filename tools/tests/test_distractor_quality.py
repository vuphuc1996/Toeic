import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class DistractorQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.listening = json.loads((ROOT / 'data/listening/listening-library.json').read_text(encoding='utf-8'))['listening']
        cls.reading = json.loads((ROOT / 'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']

    @staticmethod
    def find(items, item_id):
        return next(item for item in items if item['id'] == item_id)

    def test_manual_review_scope_contains_132_part3_part4_part7_questions(self):
        p3 = [x for x in self.listening if x.get('part') == 'Part 3' and x.get('editorialStatus') != 'reserve-pending-independent-review']
        p4 = [x for x in self.listening if x.get('part') == 'Part 4' and x.get('editorialStatus') != 'reserve-pending-independent-review']
        p7 = [x for x in self.reading if x.get('part') == 'Part 7']
        self.assertEqual(sum(len(x.get('questions', [])) for x in p3), 39)
        self.assertEqual(sum(len(x.get('questions', [])) for x in p4), 30)
        self.assertEqual(sum(len(x.get('questions', [])) for x in p7), 63)
        self.assertEqual(sum(len(x.get('questions', [])) for x in p3 + p4 + p7), 132)

    def test_reviewed_questions_have_four_unique_choices_and_valid_keys(self):
        scope = [x for x in self.listening if x.get('part') in ('Part 3', 'Part 4')]
        scope += [x for x in self.reading if x.get('part') == 'Part 7']
        for item in scope:
            for qn, question in enumerate(item.get('questions', []), 1):
                choices = question.get('choices', [])
                self.assertEqual(len(choices), 4, f"{item['id']} Q{qn}")
                normalized = [re.sub(r'[^a-z0-9]+', '', choice.casefold()) for choice in choices]
                self.assertEqual(len(normalized), len(set(normalized)), f"{item['id']} Q{qn}")
                self.assertIn(question.get('answerIndex'), range(4), f"{item['id']} Q{qn}")

    def test_twelve_revised_keys_and_original_answer_positions_are_preserved(self):
        expected = [
            (self.listening, 'part3-hotel-reservation', 0, 1, 'extend the guest'),
            (self.listening, 'part3-client-presentation', 2, 2, 'chart comparing'),
            (self.listening, 'part4-training-registration', 0, 0, 'respond to customer inquiries'),
            (self.reading, 'business-travel', 1, 0, 'boarding passes and hotel receipts'),
            (self.reading, 'customer-refund-email', 0, 1, 'replacement or instructions'),
            (self.reading, 'supplier-invoice-followup', 0, 1, 'quantity needs verification'),
            (self.reading, 'double-passage-order', 0, 1, 'incorrectly labeled carton'),
            (self.reading, 'part7-double-equipment-order', 0, 0, 'arrive on schedule'),
            (self.reading, 'part7-single-training-email', 0, 0, 'customer accounts and inquiries'),
            (self.reading, 'training-announcement', 0, 1, 'communicate with customers'),
            (self.reading, 'part7-triple-regional-sales-meeting', 0, 0, 'customer-retention report'),
            (self.reading, 'part7-triple-facility-renovation', 2, 0, 'notify security in advance'),
        ]
        for items, item_id, q_index, expected_index, text in expected:
            item = self.find(items, item_id)
            question = item['questions'][q_index]
            self.assertEqual(question['answerIndex'], expected_index, item_id)
            self.assertIn(text, question['choices'][expected_index].casefold(), item_id)
        self.assertEqual(len(expected), 12)

    def test_answer_positions_are_balanced_after_audited_choice_reorder(self):
        expected = {
            'Part 3': Counter({0: 10, 1: 10, 2: 10, 3: 9}),
            'Part 4': Counter({0: 8, 1: 8, 2: 7, 3: 7}),
            'Part 7': Counter({0: 16, 1: 16, 2: 16, 3: 15}),
        }
        actual = Counter()
        for item in self.listening + self.reading:
            if item.get('part') not in expected or item.get('editorialStatus') == 'reserve-pending-independent-review':
                continue
            for question in item.get('questions', []):
                actual[(item['part'], question['answerIndex'])] += 1
        for part, distribution in expected.items():
            for index in range(4):
                self.assertEqual(actual[(part, index)], distribution[index], (part, index))
        report = (ROOT / 'docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.17.0.md').read_text(encoding='utf-8')
        self.assertIn('previousChoiceIds', report)
        self.assertIn('No random shuffle was used', report)


    def test_batch_013_reserve_questions_are_not_in_the_old_balance_certificate(self):
        reserve = [x for x in self.listening if x.get('editorialStatus') == 'reserve-pending-independent-review']
        self.assertEqual(sum(len(x.get('questions', [])) for x in reserve if x['part'] == 'Part 3'), 3)
        self.assertEqual(sum(len(x.get('questions', [])) for x in reserve if x['part'] == 'Part 4'), 3)
        for item in reserve:
            expected_choice_count = 3 if item['part'] == 'Part 2' else 4
            for q in item['questions']:
                self.assertEqual(len(q['choices']), expected_choice_count, item['id'])
                self.assertEqual(len(q['choices']), len(set(q['choices'])), item['id'])
                self.assertIn(q['answerIndex'], range(expected_choice_count), item['id'])

    def test_learning_progress_persists_selected_choice_index(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn('choiceIndex,choiceId:choiceIdAt(question,choiceIndex),choiceText:question.choices[choiceIndex],correct,answeredAt:Date.now()', app)
        self.assertIn('prog.answers[index]={answered:true,choiceIndex,choiceId:choiceIdAt(question,choiceIndex),choiceText:question.choices[choiceIndex],correct,answeredAt:Date.now()}', app)


if __name__ == '__main__':
    unittest.main()
