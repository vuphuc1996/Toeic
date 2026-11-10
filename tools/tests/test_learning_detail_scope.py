"""Regression tests for runtime variable scope in learning-detail renderers."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP_JS = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")


def function_block(name: str, next_name: str) -> str:
    start = APP_JS.index(f"function {name}(")
    end = APP_JS.index(f"function {next_name}(", start)
    return APP_JS[start:end]


class LearningDetailScopeTests(unittest.TestCase):
    def test_grammar_detail_does_not_reference_out_of_scope_item(self):
        block = function_block("openGrammarLesson", "answerGrammarExercise")
        self.assertIsNone(re.search(r"\bitem\s*\.", block))
        self.assertIn("${escapeHtml(choice)}", block)

    def test_reading_detail_does_not_reference_out_of_scope_item(self):
        block = function_block("openReadingDetail", "answerReadingQuestion")
        self.assertIsNone(re.search(r"\bitem\s*\.", block))
        self.assertIn("${escapeHtml(choice)}", block)

    def test_reading_card_word_count_supports_part5_without_passage(self):
        block = function_block("renderReadingLibrary", "openReadingDetail")
        self.assertIn("const sourceText=item.passage||", block)
        self.assertIn("sourceText.split(/\\s+/).filter(Boolean).length", block)
        self.assertIn("item.part==='Part 5'?", block)
        self.assertIn("${wordMeta}", block)
        self.assertNotIn("item.passage.split(/\\s+/)", block)


if __name__ == "__main__":
    unittest.main()
