"""Dataset-level regression tests for the TOEIC L&R libraries."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))

class LearningContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.listening = load('data/listening/listening-library.json').get('listening', [])
        cls.reading = load('data/readings/reading-library.json').get('readings', [])
        cls.grammar = load('data/grammar/lessons.json').get('lessons', [])

    def test_listening_ids_are_unique(self):
        ids = [x.get('id') for x in self.listening]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_all_four_listening_parts_exist(self):
        self.assertEqual({f'Part {i}' for i in range(1, 5)}, {x.get('part') for x in self.listening})

    def test_part1_has_minimum_eight_original_image_sets(self):
        p1 = [x for x in self.listening if x.get('part') == 'Part 1']
        self.assertGreaterEqual(len(p1), 8)
        self.assertTrue(all(x.get('contentSource') == 'original-editorial' for x in p1))

    def test_part1_images_exist_and_have_one_question(self):
        p1 = [x for x in self.listening if x.get('part') == 'Part 1']
        for item in p1:
            image = item.get('image', '')
            self.assertTrue(image.startswith('./assets/listening/'))
            self.assertTrue((ROOT / image[2:]).is_file())
            self.assertEqual(len(item.get('questions', [])), 1)
            self.assertEqual(len(item.get('segments', [])), 4)

    def test_part1_answer_positions_are_distributed(self):
        answers = {x['questions'][0]['answerIndex'] for x in self.listening if x.get('part') == 'Part 1'}
        self.assertGreaterEqual(len(answers), 3)

    def test_part1_explanations_name_the_actual_answer_letter(self):
        for item in self.listening:
            if item.get('part') != 'Part 1':
                continue
            q = item['questions'][0]
            letter = 'ABCD'[q['answerIndex']]
            self.assertIn(f'Đáp án {letter}', q.get('explanation', ''))

    def test_all_listening_questions_have_valid_choices_and_explanations(self):
        for item in self.listening:
            for q in item.get('questions', []):
                expected = 3 if item.get('part') == 'Part 2' else 4
                self.assertEqual(len(q.get('choices', [])), expected, item.get('id'))
                self.assertIn(q.get('answerIndex'), range(expected), item.get('id'))
                self.assertTrue(q.get('question', '').strip())
                self.assertTrue(q.get('explanation', '').strip())

    def test_reading_ids_are_unique_and_every_part_exists(self):
        ids = [x.get('id') for x in self.reading]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual({'Part 5', 'Part 6', 'Part 7'}, {x.get('part') for x in self.reading})

    def test_all_reading_items_have_document_type_and_source(self):
        for item in self.reading:
            self.assertTrue(item.get('documentType'), item.get('id'))
            self.assertIn(item.get('contentSource'), ('original-editorial', 'licensed', 'official-permission'))

    def test_part6_blank_count_matches_question_count(self):
        import re
        for item in self.reading:
            if item.get('part') == 'Part 6':
                markers = re.findall(r'\[(\d+)\]', item.get('passage', ''))
                self.assertEqual(len(markers), len(item.get('questions', [])), item.get('id'))

    def test_part7_has_single_or_multiple_document_text(self):
        p7 = [x for x in self.reading if x.get('part') == 'Part 7']
        self.assertGreaterEqual(len(p7), 10)
        self.assertTrue(all(x.get('passage', '').strip() or x.get('documents') for x in p7))

    def test_all_reading_questions_have_four_choices_and_explanations(self):
        for item in self.reading:
            for q in item.get('questions', []):
                self.assertEqual(len(q.get('choices', [])), 4)
                self.assertIn(q.get('answerIndex'), range(4))
                self.assertTrue(q.get('question', '').strip())
                self.assertTrue(q.get('explanation', '').strip())

    def test_grammar_exercises_have_unique_lesson_ids_and_valid_answers(self):
        ids = [x.get('id') for x in self.grammar]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(self.grammar), 25)
        for lesson in self.grammar:
            for q in lesson.get('exercises', []):
                self.assertEqual(len(q.get('choices', [])), 4)
                self.assertIn(q.get('answerIndex'), range(4))
                self.assertTrue(q.get('explanation', '').strip())

if __name__ == '__main__':
    unittest.main()
