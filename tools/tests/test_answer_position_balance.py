import json
import unittest
from collections import Counter
from pathlib import Path

from helpers import PART7_BASELINE_QUESTION_COUNTS_V232

ROOT = Path(__file__).resolve().parents[2]

# Current canonical Listening inventory after v2.95.86 Part 1 reserve expansion.
# Batch 018 added three reserve questions; they remain excluded from Mock.
EXPECTED_LISTENING_ELIGIBLE_BY_PART = {
    'Part 1': 8, 'Part 2': 25, 'Part 3': 39, 'Part 4': 30,
}
EXPECTED_LISTENING_RESERVE_BY_PART = {
    'Part 1': 4, 'Part 2': 36, 'Part 3': 84, 'Part 4': 72,
}
EXPECTED_LISTENING_BATCH_027_BY_PART = {
    'Part 2': 8, 'Part 3': 12, 'Part 4': 12,
}


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
                if q.get('mockEligible') is False:
                    continue
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
        eligible_listening = [
            x for x in self.listening
            if not x.get('editorialStatus') or x.get('editorialStatus') == 'approved-for-mock'
        ]
        reserve_listening = [
            x for x in self.listening
            if x.get('editorialStatus') == 'reserve-pending-independent-review'
        ]
        unexpected_statuses = {
            x.get('editorialStatus') for x in self.listening
            if x not in eligible_listening and x not in reserve_listening
        }
        self.assertFalse(unexpected_statuses, f'Unclassified Listening editorial statuses: {unexpected_statuses}')

        def part_counts(items):
            counts = Counter()
            for item in items:
                counts[item['part']] += sum(
                    1 for q in item.get('questions', []) if q.get('mockEligible') is not False
                )
            return counts

        eligible_counts = part_counts(eligible_listening)
        reserve_counts = Counter({
            part: sum(len(item.get('questions', [])) for item in reserve_listening if item['part'] == part)
            for part in {item['part'] for item in reserve_listening}
        })
        self.assertEqual(dict(eligible_counts), EXPECTED_LISTENING_ELIGIBLE_BY_PART)
        self.assertEqual(dict(reserve_counts), EXPECTED_LISTENING_RESERVE_BY_PART)
        self.assertEqual(sum(eligible_counts.values()), 102)
        self.assertEqual(sum(reserve_counts.values()), 196)
        # Question-level mockEligible=false in approved resources denotes the
        # 13 Part 4 practice-only items. Reserve questions also carry this
        # fail-closed flag, but are not part of the practice-only certificate.
        practice_only = [
            (item, question)
            for item in eligible_listening
            for question in item.get('questions', [])
            if question.get('mockEligible') is False
        ]
        self.assertEqual(len(practice_only), 13)
        self.assertTrue(all(item.get('part') == 'Part 4' for item, _ in practice_only))
        self.assertEqual(sum(len(x.get('questions', [])) for x in self.listening), 311)
        self.assertEqual(sum(len(x.get('questions', [])) for x in self.reading), 287)

        # Batch 027 added 32 questions in 16 reserve resources. All must remain
        # pending independent review, not silently become Mock-eligible.
        batch_027 = [x for x in reserve_listening if x.get('editorialBatch') == '027']
        self.assertEqual(len(batch_027), 16)
        batch_027_counts = part_counts(batch_027)
        self.assertEqual(dict(batch_027_counts), EXPECTED_LISTENING_BATCH_027_BY_PART)
        self.assertEqual(sum(batch_027_counts.values()), 32)
        self.assertTrue(all(x.get('editorialStatus') == 'reserve-pending-independent-review' for x in batch_027))

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
