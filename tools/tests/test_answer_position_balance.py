import json
import unittest
from collections import Counter
from pathlib import Path

from helpers import PART7_BASELINE_QUESTION_COUNTS_V232

ROOT = Path(__file__).resolve().parents[2]


class AnswerPositionBalanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.listening = json.loads((ROOT / 'data/listening/listening-library.json').read_text(encoding='utf-8'))['listening']
        cls.reading = json.loads((ROOT / 'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']
        cls.mapping = json.loads((ROOT / 'tools/answer-position-balance-v2.17.0.json').read_text(encoding='utf-8'))

    def test_answer_position_targets_are_exact_and_part_totals_unchanged(self):
        expected = {
            'Part 3': [10, 10, 10, 9],
            'Part 4': [8, 8, 7, 7],
            'Part 7': [16, 16, 16, 15],
        }
        actual = {part: Counter() for part in expected}
        for item in self.listening + self.reading:
            if item.get('editorialStatus') == 'reserve-pending-independent-review':
                continue
            part = item.get('part')
            if part not in actual:
                continue
            questions = item.get('questions', [])
            if part == 'Part 7':
                # Keep the historical v2.17 certificate scoped to the original v2.32.0 items.
                questions = questions[:PART7_BASELINE_QUESTION_COUNTS_V232.get(item.get('id'), 0)]
            for q in questions:
                actual[part][q['answerIndex']] += 1
        for part, distribution in expected.items():
            self.assertEqual([actual[part][index] for index in range(4)], distribution, part)
            self.assertEqual(sum(actual[part].values()), sum(distribution), part)

    def test_exactly_27_keys_move_and_stable_identity_follows_each_option(self):
        self.assertEqual(self.mapping['from'], '2.16.0')
        self.assertEqual(self.mapping['to'], '2.17.0')
        self.assertEqual(len(self.mapping['changes']), 27)
        old_to_new = Counter()
        for change in self.mapping['changes']:
            key = 'listening' if 'listening' in change['file'] else 'readings'
            data = self.listening if key == 'listening' else self.reading
            item = next(x for x in data if x['id'] == change['itemId'])
            question = item['questions'][change['question'] - 1]
            old, new = change['oldIndex'], change['newIndex']
            self.assertEqual(question['previousChoices'][old], change['answer'])
            self.assertEqual(question['previousChoiceIds'][old], change['choiceId'])
            self.assertEqual(question['previousAnswerIndex'], old)
            self.assertEqual(question['choices'][new], change['answer'])
            self.assertEqual(question['choiceIds'][new], change['choiceId'])
            self.assertEqual(question['answerIndex'], new)
            self.assertEqual(question['choiceOrderRevision'], '2.17.0')
            self.assertCountEqual(question['choices'], question['previousChoices'])
            self.assertCountEqual(question['choiceIds'], question['previousChoiceIds'])
            old_to_new[change['part']] += 1
        self.assertEqual(old_to_new, Counter({'Part 3': 8, 'Part 4': 5, 'Part 7': 14}))

    def test_no_question_or_choice_identity_is_removed_by_reorder(self):
        for item in self.listening:
            expected = 3 if item.get('part') == 'Part 2' else 4
            for q in item.get('questions', []):
                self.assertEqual(len(q['choices']), expected, item['id'])
                self.assertEqual(len(q['choiceIds']), expected, item['id'])
                self.assertEqual(len(set(q['choiceIds'])), expected, item['id'])
                self.assertIn(q['answerIndex'], range(expected), item['id'])
        for item in self.reading:
            for q in item.get('questions', []):
                self.assertEqual(len(q['choices']), 4, item['id'])
                self.assertEqual(len(q['choiceIds']), 4, item['id'])
                self.assertEqual(len(set(q['choiceIds'])), 4, item['id'])
                self.assertIn(q['answerIndex'], range(4), item['id'])
        historical_listening = [x for x in self.listening if x.get('editorialStatus') != 'reserve-pending-independent-review']
        reserve_listening = [x for x in self.listening if x.get('editorialStatus') == 'reserve-pending-independent-review']
        self.assertEqual(sum(len(x.get('questions', [])) for x in historical_listening), 102)
        self.assertEqual(sum(len(x.get('questions', [])) for x in reserve_listening), 98)
        self.assertEqual(sum(len(x.get('questions', [])) for x in self.listening), 200)
        self.assertEqual(sum(len(x.get('questions', [])) for x in self.reading), 200)

    def test_v233_new_part7_answer_balance_keeps_choice_identity(self):
        mapping = json.loads((ROOT / 'tools/answer-position-balance-v2.33.0.json').read_text(encoding='utf-8'))
        self.assertEqual(len(mapping['changes']), 6)
        self.assertEqual(mapping['beforeDistribution'], {'A': 11, 'B': 13, 'C': 15, 'D': 6})
        self.assertEqual(mapping['afterDistribution'], {'A': 11, 'B': 11, 'C': 11, 'D': 12})
        for change in mapping['changes']:
            item = next(x for x in self.reading if x['id'] == change['itemId'])
            q = item['questions'][change['question'] - 1]
            self.assertEqual(q['previousChoices'][change['oldIndex']], change['answer'])
            self.assertEqual(q['previousChoiceIds'][change['oldIndex']], change['choiceId'])
            self.assertEqual(q['previousAnswerIndex'], change['previousAnswerIndex'])
            self.assertEqual(q['choices'][change['newIndex']], change['answer'])
            self.assertEqual(q['choiceIds'][change['newIndex']], change['choiceId'])
            self.assertEqual(q['answerIndex'], change['newIndex'])
            self.assertEqual(q['choiceOrderRevision'], '2.33.0')
            self.assertCountEqual(q['choices'], q['previousChoices'])
            self.assertCountEqual(q['choiceIds'], q['previousChoiceIds'])


if __name__ == '__main__':
    unittest.main()
