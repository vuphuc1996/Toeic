import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP = (ROOT / "assets/js/app.js").read_text(encoding="utf-8")


class AssessmentOneWayConfirmationTests(unittest.TestCase):
    def test_result_markup_has_only_confirmation_action(self):
        start = APP.index("function assessmentResultBodyMarkup(")
        end = APP.index("function showAssessmentResultInLearningFocus(", start)
        body = APP[start:end]
        self.assertIn("data-assessment-confirm", body)
        self.assertIn("Xác nhận &amp; xem đáp án", body)
        self.assertNotIn("data-assessment-return", body)
        self.assertNotIn("Quay lại kiểm tra", body)
        self.assertNotIn("allowReturn", body)

    def test_return_routes_and_obsolete_toast_are_removed(self):
        for obsolete in ("data-assessment-return", "returnToPracticeBatch", "returnToFoundationAssessment", "Các lựa chọn tạm đã được lưu", "allowReturn"):
            self.assertNotIn(obsolete, APP)

    def test_confirmation_handler_keeps_only_commit_dispatch(self):
        start = APP.index("async function handleAssessmentResultSurfaceAction(")
        end = APP.index("\nfunction bindEvents(", start)
        handler = APP[start:end]
        self.assertIn("data-assessment-confirm", handler)
        self.assertNotIn("assessment-return", handler)
        self.assertNotIn("returnToPracticeBatch", handler)
        self.assertNotIn("returnToFoundationAssessment", handler)

    def test_foundation_save_failure_does_not_advance_or_reveal(self):
        start = APP.index("function confirmFoundationAssessmentResult(")
        end = APP.index("\nfunction renderLearningObjectiveProgress(", start)
        confirm = APP[start:end]
        self.assertIn("throw new Error('Không thể lưu kết quả Foundation trên thiết bị", confirm)
        self.assertLess(confirm.index("localStorage.setItem(storageKey"), confirm.index("state[progressKey]=nextProgress"))
        self.assertLess(confirm.index("state[progressKey]=nextProgress"), confirm.index("state.pendingFoundationAssessment=null"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
