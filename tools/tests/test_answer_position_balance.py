import json
import unittest
from collections import Counter
from pathlib import Path

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
            part = item.get('part')
            if part in actual:
                for q in item.get('questions', []):
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
        self.assertEqual(sum(len(x.get('questions', [])) for x in self.listening), 102)
        self.assertEqual(sum(len(x.get('questions', [])) for x in self.reading), 109)


if __name__ == '__main__':
    unittest.main()
