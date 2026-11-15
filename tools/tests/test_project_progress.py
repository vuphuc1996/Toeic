import subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ProjectProgressTests(unittest.TestCase):
    def test_report_uses_explicit_targets_and_marks_unknown_targets(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        out=result.stdout
        self.assertIn('1,063 | 3,000 minimum | **35.4%**',out)
        self.assertIn('1,063 | 5,000 planning ceiling | **21.3%**',out)
        self.assertIn('16/16 | All diagnostic questions | **100.0%**',out)
        self.assertIn('Chưa đo được',out)
        self.assertIn('not editorial approval',out)
    def test_report_includes_foundation_listening_bank_coverage(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Foundation Listening scripts mapped | 10/10 | **100.0%**',result.stdout)
        self.assertIn('Foundation Listening questions | 20/20 | **100.0%**',result.stdout)
        self.assertIn('not authentic ETS recordings',result.stdout)
    def test_report_includes_alphabet_sound_bank_coverage_without_mastery_claim(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Foundation A–Z letter records | 26/26 | **100.0%**',result.stdout)
        self.assertIn('action count is not pronunciation mastery',result.stdout)
        self.assertIn('toeic:alphabet-sound-progress:v1',result.stdout)
    def test_report_does_not_mislabel_inventory_as_completion(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Content counts do not equal completed learning outcomes.',result.stdout)
        self.assertIn('independent review',result.stdout)
if __name__=='__main__': unittest.main()
