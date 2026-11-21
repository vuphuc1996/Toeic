import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

class RelatedTermExplanationContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')

    def test_synonym_and_antonym_context_are_filtered_by_relation_type(self):
        start=self.app.index('function getChoiceExplanation(q, choice, isCorrect) {')
        end=self.app.index('function renderChoiceReview(q, feedback) {',start)
        body=self.app[start:end]
        self.assertIn("const relationKey=q.mode==='synonym'?'synonyms':'antonyms';",body)
        self.assertIn('const refs=findRelatedSources(choice,relationKey);',body)
        self.assertNotIn('const refs=findRelatedSources(choice);',body)

    def test_glossary_alias_explanation_includes_available_definition_metadata(self):
        start=self.app.index('function getChoiceExplanation(q, choice, isCorrect) {')
        end=self.app.index('function renderChoiceReview(q, feedback) {',start)
        body=self.app[start:end]
        self.assertIn('alias.pos?',body)
        self.assertIn('Loại từ:',body)
        self.assertIn('alias.definition_en?',body)
        self.assertIn('English:',body)
        self.assertIn('alias.meaning_vi',body)

    def test_related_source_context_label_is_relation_specific(self):
        self.assertIn("relationKey==='synonyms'?'đồng nghĩa':'trái nghĩa'",self.app)

if __name__=='__main__': unittest.main()
