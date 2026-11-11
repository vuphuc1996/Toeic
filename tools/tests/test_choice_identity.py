import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class ChoiceIdentityTests(unittest.TestCase):
    def test_every_reading_question_has_unique_choice_ids(self):
        data=json.loads((ROOT/'data/readings/reading-library.json').read_text(encoding='utf-8'))
        self.assertTrue(all(len(q.get('choiceIds',[]))==len(q['choices']) and len(set(q['choiceIds']))==len(q['choiceIds']) for item in data['readings'] for q in item['questions']))
    def test_every_listening_question_has_unique_choice_ids(self):
        data=json.loads((ROOT/'data/listening/listening-library.json').read_text(encoding='utf-8'))
        self.assertTrue(all(len(q.get('choiceIds',[]))==len(q['choices']) and len(set(q['choiceIds']))==len(q['choiceIds']) for item in data['listening'] for q in item['questions']))
    def test_every_grammar_exercise_has_unique_choice_ids(self):
        data=json.loads((ROOT/'data/grammar/lessons.json').read_text(encoding='utf-8'))
        self.assertTrue(all(len(q.get('choiceIds',[]))==len(q['choices']) and len(set(q['choiceIds']))==len(q['choiceIds']) for item in data['lessons'] for q in item['exercises']))
    def test_progress_migration_preserves_index_and_adds_id(self):
        app=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn('await migrateChoiceIdentity();',app)
        self.assertIn('saved.choiceId=choiceId;',app)
        self.assertIn('choiceId:choiceIdAt(question,choiceIndex)',app)
        self.assertIn('choiceId:choiceIdAt(exercise,choiceIndex)',app)
    def test_choice_ids_are_rendered_on_all_learning_controls(self):
        app=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
        self.assertGreaterEqual(app.count('data-choice-id="${escapeHtml(choiceIdAt('),3)
    def test_archived_legacy_choices_keep_separate_historical_ids(self):
        for file,key in [('data/readings/reading-library.json','readings'),('data/listening/listening-library.json','listening')]:
            data=json.loads((ROOT/file).read_text(encoding='utf-8'))
            archived=[q for item in data[key] for q in item['questions'] if 'legacyChoices' in q]
            for q in archived:
                self.assertEqual(len(q['legacyChoices']),len(q['legacyChoiceIds']))
                self.assertTrue(set(q['legacyChoiceIds']).isdisjoint(set(q['choiceIds'])))

    def test_duplicate_text_choices_keep_distinct_ids(self):
        data=json.loads((ROOT/'data/readings/reading-library.json').read_text(encoding='utf-8'))
        # The identity scheme is position-specific; duplicate display strings must not collapse.
        item=data['readings'][0]
        item['questions'][0]['choices']=['same','same','other','last']
        ids=item['questions'][0]['choiceIds']
        self.assertEqual(len(set(ids)),4)

if __name__=='__main__': unittest.main()
