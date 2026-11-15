"""Regression checks for user-selected learning start levels."""
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class LearningStartLevelTests(unittest.TestCase):
 def test_supported_levels_and_stable_pre_a1_lessons(self):
  data=json.loads((ROOT/'data/learning-path/pre-a1-a1.json').read_text(encoding='utf-8'))
  self.assertEqual([x['id'] for x in data['lessons'][:3]],['pa1-alphabet','pa1-greetings','pa1-pronouns'])
  self.assertTrue({'PRE-A1','A1'}.issubset({x['level'] for x in data['lessons']}))
  js=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
  self.assertIn("['ALL','PRE-A1','A1','A2','B1','B2','C1']",js)
  self.assertIn("toeic:learning-start-level:v1",js)
 def test_higher_level_selection_does_not_force_beginner_lessons(self):
  js=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
  self.assertIn("(rank[x.level]??99)>=(rank[selected]??0)",js)
  self.assertIn('Chặng ${escapeHtml(selected)} đang được xây dựng',js)
  self.assertIn('data-go="dictionary"',js)
 def test_dictionary_remains_separate_from_learning_start_level(self):
  js=(ROOT/'assets/js/app.js').read_text(encoding='utf-8')
  dictionary=js[js.index('function filteredWords()'):js.index('function ',js.index('function filteredWords()')+10)]
  self.assertNotIn('foundationStartLevel',dictionary)
 def test_ui_has_all_levels_and_pathway_entry(self):
  html=(ROOT/'index.html').read_text(encoding='utf-8')
  for level in ('PRE-A1','A1','A2','B1','B2','C1'):
   self.assertIn(f'<option value="{level}"',html)
  self.assertIn('id="page-foundation"',html)
  self.assertIn('data-page="foundation"',html)
if __name__=='__main__':unittest.main()
