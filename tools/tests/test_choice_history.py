"""Regression tests protecting saved answers across distractor text revisions."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_LEGACY_CHOICES = {'listening:part3-hotel-reservation:0': ['To reserve a meeting room', "To extend a guest's stay", 'To report a lost suitcase', 'To cancel an airport transfer'], 'listening:part3-client-presentation:2': ['Call the client', 'Book a conference room', 'Add a comparison chart to the slides', 'Print the delivery labels'], 'listening:part4-training-registration:0': ['Employees who respond to customer inquiries', 'Newly hired accountants', 'Warehouse delivery drivers', 'Managers attending a budget meeting'], 'readings:business-travel:1': ['Boarding passes and hotel receipts', 'Business cards only', 'The presentation slides', 'The shuttle timetable'], 'readings:customer-refund-email:0': ['A refund for a hotel', 'A replacement or return instructions', 'A new delivery address', 'A discount on shipping'], 'readings:supplier-invoice-followup:0': ['The goods have not arrived', 'The invoice quantity needs verification', 'The bank account is closed', 'The purchasing manager is absent'], 'readings:double-passage-order:0': ['A missing payment', 'An incorrectly labeled carton', 'A vehicle breakdown', 'A customs inspection'], 'readings:part7-double-equipment-order:0': ['To ask whether an order will arrive on schedule', 'To request a discount on office rent', 'To cancel a damaged desk', 'To change the billing contact'], 'readings:part7-single-training-email:0': ['Employees who handle customer accounts and inquiries', 'Newly hired accounting staff', 'External suppliers of office equipment', 'Employees who manage building security'], 'readings:training-announcement:0': ['New suppliers', 'Employees who communicate with customers', 'External auditors', 'Job applicants'], 'readings:part7-triple-regional-sales-meeting:0': ['A customer-retention report', 'A parking receipt', 'A printed hotel reservation', 'A product sample'], 'readings:part7-triple-facility-renovation:2': ['Notify Security in advance', 'Ask IT to keep Wi-Fi on', 'Use the south loading entrance', 'Reschedule all meetings']}
TARGETS = {
    'data/listening/listening-library.json': ('listening', [
        ('part3-hotel-reservation', 0),
        ('part3-client-presentation', 2),
        ('part4-training-registration', 0),
    ]),
    'data/readings/reading-library.json': ('readings', [
        ('business-travel', 1),
        ('customer-refund-email', 0),
        ('supplier-invoice-followup', 0),
        ('double-passage-order', 0),
        ('part7-double-equipment-order', 0),
        ('part7-single-training-email', 0),
        ('training-announcement', 0),
        ('part7-triple-regional-sales-meeting', 0),
        ('part7-triple-facility-renovation', 2),
    ]),
}


class ChoiceHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')

    def test_all_twelve_legacy_choice_snapshots_match_v214_baseline(self):
        checked = 0
        for rel, (key, targets) in TARGETS.items():
            current = json.loads((ROOT / rel).read_text(encoding='utf-8'))[key]
            current_by_id = {item['id']: item for item in current}
            lib = 'listening' if key == 'listening' else 'readings'
            for item_id, question_index in targets:
                question = current_by_id[item_id]['questions'][question_index]
                fixture_key = f'{lib}:{item_id}:{question_index}'
                self.assertEqual(question['legacyChoices'], EXPECTED_LEGACY_CHOICES[fixture_key], fixture_key)
                self.assertEqual(len(question['legacyChoices']), 4, fixture_key)
                self.assertIn(question['answerIndex'], range(4))
                checked += 1
        self.assertEqual(checked, 12)

    def test_legacy_choice_text_is_used_before_current_option_text(self):
        self.assertIn("if(typeof saved.choiceText==='string'&&saved.choiceText.trim())return saved.choiceText;", self.app)
        self.assertIn('const legacy=question?.legacyChoices?.[index];', self.app)
        self.assertIn('return question?.choices?.[index]??\'\';', self.app)

    def test_archived_answer_does_not_mark_replacement_distractor_as_selected(self):
        self.assertIn('!savedChoiceIsArchived(question,saved)', self.app)
        self.assertIn('savedChoiceWrongClass(q,saved,j)?\'is-wrong\':\'\'', self.app)
        self.assertIn('Lựa chọn đã lưu trước lần cập nhật:', self.app)

    def test_new_reading_and_listening_attempts_store_selected_text(self):
        self.assertIn('choiceText:question.choices[choiceIndex],correct,answeredAt:Date.now()};state.readingProgress', self.app)
        self.assertIn('choiceText:question.choices[choiceIndex],correct,answeredAt:Date.now()};state.listeningProgress', self.app)

    def test_archived_text_is_html_escaped_and_rendered_in_both_libraries(self):
        self.assertIn('escapeHtml(savedChoiceText(question,saved))', self.app)
        self.assertGreaterEqual(self.app.count('${savedChoiceHistoryMarkup(q,saved)}'), 2)


if __name__ == '__main__':
    unittest.main()
