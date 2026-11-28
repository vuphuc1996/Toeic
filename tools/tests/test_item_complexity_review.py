"""Contract tests for the non-calibrated item-complexity triage report."""
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SCRIPT=ROOT/'tools/audit-item-complexity.py'
VERSION=json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8'))['version']
REPORT=ROOT/'docs/reports'/f'TOEIC_ITEM_COMPLEXITY_REVIEW_v{VERSION}.md'
SPEC=importlib.util.spec_from_file_location('item_complexity_audit',SCRIPT)
AUDIT=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(AUDIT)

class ItemComplexityReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run=subprocess.run([sys.executable,str(SCRIPT)],cwd=ROOT,text=True,capture_output=True)
        if run.returncode: raise RuntimeError(run.stdout+'\n'+run.stderr)
        cls.report=REPORT.read_text(encoding='utf-8')
        cls.listening=json.loads((ROOT/'data/listening/listening-library.json').read_text(encoding='utf-8'))['listening']
        cls.reading=json.loads((ROOT/'data/readings/reading-library.json').read_text(encoding='utf-8'))['readings']

    def test_every_listening_and_reading_question_is_indexed(self):
        expected=sum(len(x.get('questions',[])) for x in self.listening+self.reading)
        self.assertIn(f'Total questions indexed: **{expected}**',self.report)
        self.assertEqual(self.report.count('| Listening /'),sum(len(x.get('questions',[])) for x in self.listening))
        self.assertEqual(self.report.count('| Reading /'),sum(len(x.get('questions',[])) for x in self.reading))

    def test_all_listening_reserve_items_remain_excluded(self):
        reserve=[x for x in self.listening if x.get('editorialStatus')=='reserve-pending-independent-review']
        expected=sum(len(x.get('questions',[])) for x in reserve)
        self.assertIn(f'Listening reserve-pending: **{expected}**',self.report)
        reading_reserve=sum(len(x.get('questions',[])) for x in self.reading if x.get('editorialStatus')=='reserve-pending-independent-review')
        self.assertIn(f'Reading reserve-pending: **{reading_reserve}**',self.report)
        self.assertIn('RESERVE — not Mock eligible',self.report)
        self.assertEqual(expected,196)
        self.assertEqual(reading_reserve,87)

    def test_report_does_not_claim_calibrated_difficulty(self):
        self.assertIn('not a difficulty score or calibrated item model',self.report)
        self.assertIn('does not assign CEFR/ETS difficulty',self.report)
        self.assertIn('No response data or psychometric parameters are inferred',self.report)

    def test_complexity_signals_are_transparent_and_deterministic(self):
        self.assertEqual(AUDIT.classify_question({'question':'What can be inferred from the notice?'}),'inference_or_purpose')
        self.assertEqual(AUDIT.classify_question({'question':'When will the shipment arrive?'}),'detail_or_location')
        self.assertEqual(AUDIT.classify_question({'question':'Choose the most appropriate response.'}),'other_or_response_fit')
        self.assertIn('Source text >=250 words',self.report)
        self.assertIn('Choice word-count spread >=8',self.report)
        self.assertIn('Multi-document language cue',self.report)

    def test_no_source_question_or_answer_mutation(self):
        # Audit is read-only by construction; source files are not written by the script.
        source=SCRIPT.read_text(encoding='utf-8')
        self.assertIn('read_text',source)
        self.assertIn('OUT.write_text',source)  # only the generated report is written
        self.assertNotIn('json.dump',source)
        self.assertNotIn('open(.*\'w\'',source)

if __name__=='__main__': unittest.main()
