"""Coverage tests for the generated, item-level independent editorial review queue."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from editorial_inventory import collect_editorial_inventory


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
        cls.metrics = collect_editorial_inventory(ROOT)
        cls.baseline = json.loads((ROOT / 'tools/editorial-inventory-baseline-v2.95.45.json').read_text(encoding='utf-8'))

    def test_queue_covers_all_listening_reserve_questions(self):
        pending = [u for u in self.listening if u.get('editorialStatus') == 'reserve-pending-independent-review']
        count = sum(len(u.get('questions', [])) for u in pending)
        self.assertEqual(count, self.metrics['listening']['reserve_questions'])
        self.assertIn(f"Listening: **{self.metrics['listening']['eligible_questions']} eligible + {count} reserve = {self.metrics['listening']['total_questions']} total**.", self.text)
        for unit in pending:
            self.assertIn(f"`{unit['id']}`", self.text)

    def test_queue_covers_all_part7_reserve_questions(self):
        pending = [u for u in self.reading if u.get('part') == 'Part 7' and u.get('editorialStatus') == 'reserve-pending-independent-review']
        count = sum(len(u.get('questions', [])) for u in pending)
        self.assertEqual(count, self.metrics['part7']['reserve_questions'])
        self.assertIn(f"Part 7 reserve: **{count} questions**", self.text)
        for unit in pending:
            self.assertIn(f"`{unit['id']}`", self.text)

    def test_queue_covers_all_separate_part5_reserve_questions(self):
        questions = self.p5['questions']
        self.assertEqual(len(questions), self.metrics['part5']['total_questions'])
        self.assertIn(f"Separate Part 5 practice-only bank: **{len(questions)} questions**", self.text)
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
        self.assertIn(f"the {self.metrics['listening']['reserve_questions']} reserve questions are not promoted", self.text)
        self.assertNotIn('137 reserve questions', self.text)
        self.assertIn('AI-assisted audit is not a substitute', self.text)


    def test_live_metrics_match_the_reviewed_baseline_snapshot(self):
        self.assertEqual(self.metrics['listening']['eligible_questions'], self.baseline['listening']['eligibleQuestions'])
        self.assertEqual(self.metrics['listening']['reserve_questions'], self.baseline['listening']['reserveQuestions'])
        self.assertEqual(self.metrics['listening']['total_questions'], self.baseline['listening']['totalQuestions'])
        self.assertEqual(self.metrics['part7']['reserve_questions'], self.baseline['part7']['reserveQuestions'])
        self.assertEqual(self.metrics['part5']['total_questions'], self.baseline['part5']['totalQuestions'])
        self.assertTrue(self.metrics['part5']['practice_only'])
        self.assertEqual(self.metrics['part5']['review_pending_questions'], self.baseline['part5']['reviewPendingQuestions'])

    def test_listening_eligible_and_reserve_question_ids_are_disjoint(self):
        eligible = set(self.metrics['listening']['eligible_question_ids'])
        reserve = set(self.metrics['listening']['reserve_question_ids'])
        self.assertFalse(eligible & reserve)
        self.assertEqual(len(eligible), self.metrics['listening']['eligible_questions'])
        self.assertEqual(len(reserve), self.metrics['listening']['reserve_questions'])

    def test_part7_and_part5_remain_separate_from_listening(self):
        self.assertEqual(self.metrics['part7']['reserve_questions'], 87)
        self.assertEqual(self.metrics['part5']['total_questions'], 80)
        self.assertTrue(self.metrics['part5']['practice_only'])
        self.assertNotIn('approved-for-mock', self.p5.get('editorialStatus', ''))


if __name__ == '__main__':
    unittest.main()
