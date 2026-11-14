"""Focused content checks for the TOEIC Part 5 sentence-completion practice bank."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


class SentenceCompletionBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = load('data/practice/part5-sentence-completion.json')
        cls.questions = cls.bank['questions']
        cls.words = [
            word
            for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for word in load(f'data/vocabulary/{letter}.json').get('words', [])
        ]
        cls.word_by_id = {word['id']: word for word in cls.words}

    def test_bank_metadata_remains_editorial_and_pending(self):
        self.assertEqual(self.bank['questionType'], 'sentence-completion')
        self.assertEqual(self.bank['contentSource'], 'original-editorial')
        self.assertEqual(self.bank['editorialStatus'], 'reserve-pending-independent-review')
        self.assertEqual(self.bank['reviewNote'], 'internal-author-check; independent-second-review-pending')

    def test_question_and_target_ids_are_unique(self):
        ids = [item['id'] for item in self.questions]
        targets = [item['wordId'] for item in self.questions]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(targets), len(set(targets)))
        self.assertEqual(len(self.questions), 80)

    def test_batch_016_adds_45_new_items_without_promoting_pending_content(self):
        batch = [item for item in self.questions if item.get('editorialBatch') == '016']
        self.assertEqual(len(batch), 45)
        self.assertEqual({item.get('contentBatch') for item in batch}, {'batch-016-part5-grammar-expansion'})
        self.assertTrue(all(item['editorialStatus'] == 'reserve-pending-independent-review' for item in batch))
        self.assertTrue(all(item['reviewNote'] == 'internal-author-check; independent-second-review-pending' for item in batch))

    def test_answer_key_positions_are_balanced(self):
        counts = [sum(item['answerIndex'] == index for item in self.questions) for index in range(4)]
        self.assertEqual(counts, [20, 20, 20, 20])

    def test_grammar_categories_are_present_and_cover_multiple_skills(self):
        categories = {item.get('grammarCategory') for item in self.questions}
        self.assertGreaterEqual(len(categories), 10)
        self.assertTrue({'Verb Tense and Aspect', 'Subject–Verb Agreement', 'Passive Voice', 'Prepositions and Collocations', 'Articles and Determiners'}.issubset(categories))
        groups = self.bank['questionGroups']
        self.assertEqual(sum(group['questionCount'] for group in groups), 80)

    def test_each_item_has_four_unique_choices_and_one_blank(self):
        for item in self.questions:
            with self.subTest(item=item['id']):
                self.assertEqual(item['sentence'].count('_____'), 1)
                self.assertEqual(len(item['choices']), 4)
                self.assertEqual(len({choice.casefold() for choice in item['choices']}), 4)
                self.assertIn(item['answerIndex'], range(4))
                self.assertTrue(all(choice.strip() for choice in item['choices']))

    def test_each_item_links_to_a_canonical_vocabulary_headword(self):
        for item in self.questions:
            with self.subTest(item=item['id']):
                self.assertIn(item['wordId'], self.word_by_id)
                self.assertTrue(self.word_by_id[item['wordId']]['word'].strip())

    def test_explanations_translation_and_unique_answer_rationale_exist(self):
        for item in self.questions:
            with self.subTest(item=item['id']):
                for field in ('grammarPoint', 'explanation', 'translationVi', 'singleAnswerReason'):
                    self.assertTrue(item[field].strip(), field)
                self.assertEqual(len(item['optionExplanations']), 4)
                self.assertTrue(all(note.strip() for note in item['optionExplanations']))
                self.assertTrue(all(note.startswith('Sai:') for index, note in enumerate(item['optionExplanations']) if index != item['answerIndex']))
                correct_note = item['optionExplanations'][item['answerIndex']].casefold()
                self.assertTrue(correct_note.startswith('đúng:'))
                self.assertTrue(all(note.casefold().startswith('sai:') for index, note in enumerate(item['optionExplanations']) if index != item['answerIndex']))

    def test_context_topics_cover_common_toeic_work_situations(self):
        topics = {item['topic'] for item in self.questions}
        self.assertGreaterEqual(len(topics), 8)
        self.assertTrue({'Office Administration', 'Finance', 'Shipping and Logistics', 'Recruitment'}.issubset(topics))

    def test_refined_department_and_shipment_questions_have_matching_rationales(self):
        department = next(q for q in self.questions if q['id'] == 'p5-sc-026')
        self.assertIn('department', department['sentence'])
        self.assertIn('department', department['singleAnswerReason'])
        shipment = next(q for q in self.questions if q['id'] == 'p5-sc-034')
        self.assertEqual(shipment['grammarPoint'], 'Article + adjective + singular count noun')
        self.assertIn('a single', shipment['singleAnswerReason'])

    def test_ambiguity_sensitive_preposition_items_have_one_keyed_construction(self):
        beneficial = next(q for q in self.questions if q['id'] == 'p5-sc-057')
        self.assertNotIn('for', beneficial['choices'])
        self.assertEqual(beneficial['choices'][beneficial['answerIndex']], 'to')
        notify = next(q for q in self.questions if q['id'] == 'p5-sc-063')
        self.assertNotIn('about', notify['choices'])
        self.assertEqual(notify['choices'][notify['answerIndex']], 'of')
        purpose = next(q for q in self.questions if q['id'] == 'p5-sc-042')
        self.assertIn('purpose of _____', purpose['sentence'])
        self.assertEqual(purpose['choices'][purpose['answerIndex']], 'confirming')
        reserved = next(q for q in self.questions if q['id'] == 'p5-sc-070')
        self.assertIn('kept available', reserved['sentence'])
        self.assertEqual(reserved['choices'][reserved['answerIndex']], 'for')

    def test_sample_modal_infinitive_question_is_unambiguous(self):
        item = next(q for q in self.questions if q['id'] == 'p5-sc-018')
        self.assertIn('plans to _____', item['sentence'])
        self.assertEqual(item['choices'][item['answerIndex']], 'order')
        self.assertIn('nguyên mẫu', item['singleAnswerReason'])
        self.assertIn('đặt thêm máy tính', item['translationVi'])


if __name__ == '__main__':
    unittest.main()
