"""Ensure recently expanded TOEIC Grammar lessons have complete bilingual analysis."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGET_LESSONS = {
    'conditional-forms-business-toeic',
    'reported-speech-workplace-toeic',
    'comparatives-business-reporting-toeic',
    'countability-quantifiers-toeic',
    'gerund-infinitive-business-verbs-toeic',
    'passive-reporting-process-toeic',
    'relative-clauses-reference-toeic',
    'prepositions-time-deadlines-toeic',
    'batch025-parallel-structure-toeic',
    'batch025-inversion-negative-adverbials-toeic',
    'batch025-subjunctive-recommendation-toeic',
    'batch025-causative-have-get-toeic',
    'batch025-noun-clause-connectors-toeic',
    'batch025-reduced-adverbial-clauses-toeic',
    'batch025-articles-institutional-nouns-toeic',
    'batch025-concessive-contrast-connectors-toeic',
    'batch025-verb-complement-meaning-toeic',
}


class GrammarExamplesQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        payload = json.loads((ROOT / 'data/grammar/lessons.json').read_text(encoding='utf-8'))
        cls.lessons = {item['id']: item for item in payload['lessons']}
        cls.examples = [example for key in TARGET_LESSONS for example in cls.lessons[key]['examples']]

    def test_all_target_lessons_and_expected_example_volume_exist(self):
        self.assertTrue(TARGET_LESSONS.issubset(self.lessons))
        self.assertEqual(42, len(self.examples))

    def test_each_example_has_complete_bilingual_sentence(self):
        for lesson_id in TARGET_LESSONS:
            for example in self.lessons[lesson_id]['examples']:
                with self.subTest(lesson=lesson_id, example=example.get('en')):
                    self.assertTrue(example.get('en', '').strip())
                    self.assertTrue(example.get('vi', '').strip())
                    self.assertNotIn('Chưa có', example['vi'])

    def test_each_example_has_meaningful_sentence_breakdown(self):
        for lesson_id in TARGET_LESSONS:
            for example in self.lessons[lesson_id]['examples']:
                with self.subTest(lesson=lesson_id, example=example.get('en')):
                    chunks = example.get('breakdown', [])
                    self.assertGreaterEqual(len(chunks), 2)
                    joined = ' '.join(chunk.get('text', '') for chunk in chunks)
                    for key in ('part', 'text', 'meaning'):
                        self.assertTrue(all(chunk.get(key, '').strip() for chunk in chunks), key)
                    normalized_sentence = ' '.join(example['en'].split()).casefold()
                    normalized_chunks = ' '.join(joined.split()).casefold()
                    self.assertTrue(all(chunk['text'].casefold() in normalized_sentence for chunk in chunks), lesson_id)
                    self.assertTrue(normalized_chunks)

    def test_grammar_detail_renders_sentence_breakdown(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn('VÍ DỤ VÀ PHÂN TÍCH', app)
        self.assertIn('ex.breakdown.map(part=>', app)
        self.assertIn('part.part', app)
        self.assertIn('part.meaning', app)


if __name__ == '__main__':
    unittest.main(verbosity=2)
