"""Regression tests for runtime variable scope in learning-detail renderers."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP_JS = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")


def function_block(name: str) -> str:
    """Return one top-level function, stopping at the next declaration.

    Do not use a caller-supplied later function name: new helper functions may
    legitimately be inserted between the two functions being tested.
    """
    declaration = re.compile(rf"(?m)^(?:async\s+)?function\s+{re.escape(name)}\s*\(")
    match = declaration.search(APP_JS)
    if not match:
        raise AssertionError(f"Top-level function {name} was not found")
    next_declaration = re.compile(r"(?m)^(?:async\s+)?function\s+[A-Za-z_$][\w$]*\s*\(")
    following = next_declaration.search(APP_JS, match.end())
    end = following.start() if following else len(APP_JS)
    return APP_JS[match.start():end]


class LearningDetailScopeTests(unittest.TestCase):
    def test_grammar_detail_does_not_reference_out_of_scope_item(self):
        block = function_block("openGrammarLesson")
        self.assertIsNone(re.search(r"\bitem\s*\.", block))
        self.assertIn("${escapeHtml(choice)}", block)
        self.assertNotIn("function renderRecallQueue(", block)

    def test_recall_renderer_remains_outside_grammar_detail_scope(self):
        recall = function_block("renderRecallQueue")
        self.assertIn("due.map(item =>", recall)
        self.assertNotIn("renderRecallQueue", function_block("openGrammarLesson"))

    def test_reading_detail_does_not_reference_out_of_scope_item(self):
        block = function_block("openReadingDetail")
        self.assertIsNone(re.search(r"\bitem\s*\.", block))
        self.assertIn("${escapeHtml(choice)}", block)

    def test_reading_card_word_count_supports_part5_without_passage(self):
        block = function_block("renderReadingLibrary")
        self.assertIn("const sourceText=item.passage||", block)
        self.assertIn("sourceText.split(/\\s+/).filter(Boolean).length", block)
        self.assertIn("item.part==='Part 5'?", block)
        self.assertIn("${wordMeta}", block)
        self.assertNotIn("item.passage.split(/\\s+/)", block)


if __name__ == "__main__":
    unittest.main()
