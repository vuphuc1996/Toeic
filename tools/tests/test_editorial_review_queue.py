"""Coverage tests for the generated, item-level independent editorial review queue."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class EditorialReviewQueueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manifest = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))
        cls.report = ROOT / 'docs/reports' / f"TOEIC_INDEPENDENT_REVIEW_QUEUE_v{manifest['version']}.md"
        run = subprocess.run([sys.executable, str(ROOT / 'tools/build-editorial-review-queue.py')], cwd=ROOT, capture_output=True, text=True)
        if run.returncode:
            raise RuntimeError(run.stdout + run.stderr)
        cls.text = cls.report.read_text(encoding='utf-8')
        cls.listening = json.loads((ROOT / 'data/listening/listening-library.json').read_text(encoding='utf-8'))['listening']
        cls.reading = json.loads((ROOT / 'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']
        cls.p5 = json.loads((ROOT / 'data/practice/part5-sentence-completion.json').read_text(encoding='utf-8'))

    def test_queue_covers_all_listening_reserve_questions(self):
        pending = [u for u in self.listening if u.get('editorialStatus') == 'reserve-pending-independent-review']
        count = sum(len(u.get('questions', [])) for u in pending)
        self.assertEqual(count, 161)
        for unit in pending:
            self.assertIn(f"`{unit['id']}`", self.text)

    def test_queue_covers_all_part7_reserve_questions(self):
        pending = [u for u in self.reading if u.get('part') == 'Part 7' and u.get('editorialStatus') == 'reserve-pending-independent-review']
        count = sum(len(u.get('questions', [])) for u in pending)
        self.assertEqual(count, 87)
        for unit in pending:
            self.assertIn(f"`{unit['id']}`", self.text)

    def test_queue_covers_all_separate_part5_reserve_questions(self):
        questions = self.p5['questions']
        self.assertEqual(len(questions), 80)
        for question in questions:
            self.assertIn(f"`{question['id']}`", self.text)

    def test_part1_photo_review_includes_the_spoken_statement_a_to_d_mapping(self):
        section = self.text.split('### Part 1 · `part1-office-cleaning`', 1)[1].split('### Part 2 ·', 1)[0]
        self.assertIn('Spoken-statement translation / A–D mapping:', section)
        self.assertIn('A. Một nhân viên bảo trì đang quét sàn hành lang.', section)
        self.assertIn('B. Một nhân viên vệ sinh đang lau cửa kính bằng khăn.', section)
        self.assertIn('C. Một công nhân đang đẩy xe vệ sinh dọc hành lang.', section)
        self.assertIn('D. Một số chiếc ghế đang được sắp xếp gần lối vào.', section)

    def test_packet_does_not_claim_review_or_promote_mock_reserves(self):
        self.assertIn('Independent review required', self.text)
        self.assertIn('the 137 reserve questions are not promoted', self.text)
        self.assertIn('AI-assisted audit is not a substitute', self.text)


if __name__ == '__main__':
    unittest.main()
