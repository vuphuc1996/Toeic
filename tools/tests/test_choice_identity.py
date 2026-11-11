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
    def test_progress_migration_maps_stable_choice_id_to_current_index(self):
        app=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn('await migrateChoiceIdentity();',app)
        self.assertIn('saved.choiceId=choiceId;',app)
        self.assertIn('const currentIndex=currentIds.indexOf(storedId);',app)
        self.assertIn('const currentIndex=currentIds.indexOf(choiceId);',app)
        self.assertIn('saved.previousChoiceIndex=oldIndex;',app)
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


    def test_reordered_questions_have_complete_v216_snapshots(self):
        mapping=json.loads((ROOT/'tools/answer-position-balance-v2.17.0.json').read_text(encoding='utf-8'))
        self.assertEqual(len(mapping['changes']),27)
        for change in mapping['changes']:
            file=ROOT/change['file']
            key='listening' if 'listening' in change['file'] else 'readings'
            data=json.loads(file.read_text(encoding='utf-8'))
            item=next(x for x in data[key] if x['id']==change['itemId'])
            question=item['questions'][change['question']-1]
            self.assertEqual(question['previousChoices'][change['oldIndex']],change['answer'])
            self.assertEqual(question['previousChoiceIds'][change['oldIndex']],change['choiceId'])
            self.assertEqual(question['choices'][change['newIndex']],change['answer'])
            self.assertEqual(question['choiceIds'][change['newIndex']],change['choiceId'])
            self.assertEqual(question['answerIndex'],change['newIndex'])
            self.assertEqual(question['previousAnswerIndex'],change['previousAnswerIndex'])
            self.assertEqual(question['choiceOrderRevision'],'2.17.0')

    def test_all_choice_ids_remain_unique_after_reorder(self):
        for file,key in [('data/listening/listening-library.json','listening'),('data/readings/reading-library.json','readings'),('data/grammar/lessons.json','lessons')]:
            data=json.loads((ROOT/file).read_text(encoding='utf-8'))
            qkey='exercises' if key=='lessons' else 'questions'
            for item in data[key]:
                for q in item[qkey]:
                    self.assertEqual(len(q['choices']),len(q['choiceIds']))
                    self.assertEqual(len(set(q['choiceIds'])),len(q['choiceIds']))
                    self.assertIn(q['answerIndex'],range(len(q['choices'])))

if __name__=='__main__': unittest.main()
