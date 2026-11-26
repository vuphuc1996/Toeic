"""Regression checks for review mode availability and flashcard result layering."""
import json
import re
import string
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/app.css").read_text(encoding="utf-8")


def load_json(relative_path):
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


class PracticeModeFallbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.words = [
            word
            for letter in string.ascii_uppercase
            for word in load_json(f"data/vocabulary/{letter}.json").get("words", [])
        ]
        cls.word_by_id = {str(word.get("id")): word for word in cls.words}
        cls.bank = load_json("data/practice/part5-sentence-completion.json")
        cls.app = APP

    def test_part5_review_targets_resolve_against_release_vocabulary(self):
        questions = self.bank.get("questions", [])
        self.assertTrue(questions, "Part 5 review bank must not be empty")
        missing = sorted({str(row.get("wordId")) for row in questions if str(row.get("wordId")) not in self.word_by_id})
        self.assertEqual(missing, [], f"Part 5 targets missing from immutable release vocabulary: {missing}")

    def test_part5_question_pool_restores_hidden_local_targets_from_base_release(self):
        start = self.app.index("function getSentenceCompletionWordPool()")
        end = self.app.index("function practiceModeFallbacks(", start)
        helper = self.app[start:end]
        self.assertIn("getPracticeVocabulary()", helper)
        self.assertIn("state.baseWords", helper)
        self.assertIn("state.sentenceCompletionItems", helper)
        self.assertIn("if(id&&!byId.has(id)&&baseById.has(id))byId.set(id,baseById.get(id))", helper)
        self.assertIn("chooseSentenceCompletionQuestion(state.sentenceCompletionItems,getSentenceCompletionWordPool()", self.app)

    def test_vocabulary_review_uses_base_data_when_local_effective_pool_is_empty(self):
        start = self.app.index("function getPracticeVocabulary()")
        end = self.app.index("function getSentenceCompletionWordPool(", start)
        helper = self.app[start:end]
        self.assertIn("state.words", helper)
        self.assertIn("state.baseWords", helper)
        self.assertRegex(helper, r"state\.words\)\s*&&state\.words\.length\?state\.words:\(Array\.isArray\(state\.baseWords\)")
        self.assertIn("const vocabulary=getPracticeVocabulary()", self.app[self.app.index("function choosePracticeWord("):self.app.index("function shuffle(")])

    def test_unavailable_selected_mode_retries_smart_and_common_modes(self):
        start = self.app.index("function practiceModeFallbacks(")
        end = self.app.index("function choosePracticeWord(", start)
        helper = self.app[start:end]
        for mode in ("random", "word-to-meaning", "meaning-to-word", "missing", "pos", "verb", "synonym", "antonym"):
            self.assertIn(f"'{mode}'", helper)
        next_question = self.app[self.app.index("async function nextQuestion("):self.app.index("async function skipQuestion(")]
        self.assertIn("for(const candidate of practiceModeFallbacks(requestedMode))", next_question)
        self.assertIn("if(q){actualMode=candidate;break;}", next_question)
        self.assertIn("syncPracticeModeSelection(actualMode)", next_question)
        self.assertIn("Dạng ${requestedLabel} chưa có câu phù hợp. Đã chuyển sang ${fallbackLabel}", next_question)

    def test_practice_focus_header_uses_the_actual_fallback_question_mode(self):
        start = self.app.index("function startPracticeFocus(")
        end = self.app.index("const ALPHABET", start)
        block = self.app[start:end]
        self.assertIn("nextQuestion(mode,forcedItemId).then(started=>", block)
        self.assertIn("const actualMode=state.currentQuestion?.mode||mode", block)
        self.assertIn("updatePracticeFocusHeader(actualMode)", block)

    def test_flashcard_confirmation_reuses_learning_focus_without_duplicate_modal(self):
        body = self.app[self.app.index("function assessmentResultBodyMarkup("):self.app.index("function showAssessmentResultInLearningFocus(")]
        self.assertIn("data-assessment-confirm", body)
        focus_surface = self.app[self.app.index("function showAssessmentResultInLearningFocus("):self.app.index("function restoreAssessmentResultLearningFocus(")]
        self.assertIn("if(!learningFocusState.active", focus_surface)
        self.assertIn("hideModalLayer()", focus_surface)
        self.assertIn("assessment-result-inline", focus_surface)
        self.assertIn("host.append(panel)", focus_surface)
        self.assertIn("panel.querySelector('[data-assessment-confirm]')?.focus()", focus_surface)
        result_dispatch = self.app[self.app.index("function showAssessmentResultModal("):self.app.index("function closeAssessmentResultModal(")]
        self.assertIn("if(showAssessmentResultInLearningFocus({eyebrow,title,bodyMarkup}))return", result_dispatch)
        self.assertIn("dataset.modalType='assessment-result'", result_dispatch, "Non-Learning-Focus flows retain the modal fallback")
        finish = self.app[self.app.index("async function finishFlashQuiz("):self.app.index("async function confirmFlashQuizResult(")]
        self.assertIn("showAssessmentResultModal", finish)
        self.assertIn("state.flashQuizAnswers.length!==ss.quiz.length", finish)
        confirm = self.app[self.app.index("async function confirmFlashQuizResult("):self.app.index("async function handleAssessmentResultSurfaceAction(")]
        self.assertIn("await dbSet('flashProgress',state.flashProgress)", confirm)
        self.assertIn("closeAssessmentResultModal()", confirm)
        self.assertLess(confirm.index("await dbSet('flashProgress'"), confirm.index("closeAssessmentResultModal()"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
