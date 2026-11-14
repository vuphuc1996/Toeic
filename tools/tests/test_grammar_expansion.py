"""Regression checks for the TOEIC Grammar expansion in v2.31.0."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH_IDS = {
    'determiners-quantifiers-toeic',
    'advanced-subject-verb-agreement-toeic',
    'dependent-prepositions-business-toeic',
    'pronouns-reference-agreement-toeic',
    'perfect-tense-sequence-toeic',
    'reduced-relative-participial-clauses-toeic',
    'transition-connectors-part6-toeic',
    'text-cohesion-part6-toeic',
}


class GrammarExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = json.loads((ROOT / 'data/grammar/lessons.json').read_text(encoding='utf-8'))
        cls.lessons = payload.get('lessons', [])
        cls.by_id = {item.get('id'): item for item in cls.lessons}
        cls.batch = [cls.by_id[x] for x in BATCH_IDS if x in cls.by_id]

    def test_all_batch_lessons_are_present(self):
        self.assertEqual(BATCH_IDS, set(self.by_id) & BATCH_IDS)
        self.assertEqual(8, len(self.batch))

    def test_batch_has_32_exercises(self):
        self.assertEqual(32, sum(len(item.get('exercises', [])) for item in self.batch))

    def test_every_batch_lesson_is_tagged_for_part_5_or_6(self):
        for lesson in self.batch:
            self.assertTrue(lesson.get('parts'), lesson['id'])
            self.assertTrue(set(lesson['parts']).issubset({'Part 5', 'Part 6'}), lesson['id'])

    def test_part_5_and_part_6_both_have_content(self):
        part5 = [x for x in self.batch if 'Part 5' in x.get('parts', [])]
        part6 = [x for x in self.batch if 'Part 6' in x.get('parts', [])]
        self.assertGreaterEqual(len(part5), 6)
        self.assertGreaterEqual(len(part6), 3)

    def test_exercise_ids_choices_and_explanations_are_valid(self):
        seen = set()
        for lesson in self.batch:
            self.assertTrue(lesson.get('summary', '').strip(), lesson['id'])
            self.assertTrue(lesson.get('explanation', '').strip(), lesson['id'])
            self.assertTrue(lesson.get('examples'), lesson['id'])
            for index, question in enumerate(lesson.get('exercises', []), 1):
                self.assertEqual(4, len(question.get('choices', [])), lesson['id'])
                self.assertEqual(4, len(set(question['choices'])), lesson['id'])
                self.assertIn(question.get('answerIndex'), range(4), lesson['id'])
                self.assertTrue(question.get('question', '').strip(), lesson['id'])
                self.assertTrue(question.get('explanation', '').strip(), lesson['id'])
                self.assertEqual(4, len(question.get('choiceIds', [])), lesson['id'])
                for choice_id in question['choiceIds']:
                    self.assertNotIn(choice_id, seen)
                    seen.add(choice_id)

    def test_prompts_are_not_exact_duplicates_in_existing_grammar_bank(self):
        all_prompts = {}
        duplicates = []
        for lesson in self.lessons:
            for question in lesson.get('exercises', []):
                normalized = re.sub(r'\s+', ' ', question.get('question', '')).strip().casefold()
                if normalized in all_prompts:
                    duplicates.append((all_prompts[normalized], lesson.get('id')))
                else:
                    all_prompts[normalized] = lesson.get('id')
        self.assertEqual([], duplicates)

    def test_data_and_ui_expose_part_filter(self):
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        css = (ROOT / 'assets/css/app.css').read_text(encoding='utf-8')
        self.assertIn('id="grammarPartFilter"', html)
        self.assertIn('.grammar-library-toolbar{grid-template-columns:minmax(220px,1.5fr)', css)
        self.assertIn('@media(max-width:980px){.grammar-library-toolbar{grid-template-columns:1fr 1fr}', css)
        self.assertIn("item.parts", app)
        self.assertIn("parts.includes(part)", app)


if __name__ == '__main__':
    unittest.main()
