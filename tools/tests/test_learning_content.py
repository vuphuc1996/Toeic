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
        self.assertTrue(all(x.get('visualType') == 'illustration' for x in p1 if x.get('image', '').lower().endswith('.svg')))

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

    def test_question_pool_meets_one_form_blueprint(self):
        listen = {f'Part {i}': 0 for i in range(1, 5)}
        for item in self.listening:
            listen[item['part']] += len(item.get('questions', []))
        self.assertGreaterEqual(listen['Part 1'], 6)
        self.assertGreaterEqual(listen['Part 2'], 25)
        self.assertGreaterEqual(listen['Part 3'], 39)
        self.assertGreaterEqual(listen['Part 4'], 30)
        self.assertGreaterEqual(sum(listen.values()), 100)

        read = {f'Part {i}': 0 for i in range(5, 8)}
        p7_single = p7_multiple = 0
        for item in self.reading:
            count = len(item.get('questions', []))
            read[item['part']] += count
            if item['part'] == 'Part 7':
                if item.get('documentType') in ('DOUBLE PASSAGE', 'TRIPLE PASSAGE'):
                    p7_multiple += count
                else:
                    p7_single += count
        self.assertGreaterEqual(read['Part 5'], 30)
        self.assertGreaterEqual(read['Part 6'], 16)
        self.assertGreaterEqual(p7_single, 29)
        self.assertGreaterEqual(p7_multiple, 25)
        self.assertGreaterEqual(sum(read.values()), 100)

    def test_part3_and_part4_sets_have_three_questions(self):
        for item in self.listening:
            if item.get('part') in ('Part 3', 'Part 4'):
                self.assertEqual(len(item.get('questions', [])), 3, item.get('id'))

    def test_part3_conversations_have_multiple_speakers(self):
        for item in self.listening:
            if item.get('part') == 'Part 3':
                speakers = {s.get('speaker') for s in item.get('segments', []) if s.get('speaker')}
                self.assertGreaterEqual(len(speakers), 2, item.get('id'))

    def test_all_part7_multi_document_questions_are_tagged(self):
        multi = [x for x in self.reading if x.get('part') == 'Part 7' and x.get('documentType') in ('DOUBLE PASSAGE', 'TRIPLE PASSAGE')]
        self.assertGreaterEqual(sum(len(x.get('questions', [])) for x in multi), 25)
        self.assertTrue(all(len(x.get('documents', [])) == (2 if x.get('documentType') == 'DOUBLE PASSAGE' else 3) for x in multi))
        self.assertTrue(all(all(d.get('label', '').strip() and d.get('content', '').strip() for d in x['documents']) for x in multi))

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
