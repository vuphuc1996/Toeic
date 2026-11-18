import subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ProjectProgressTests(unittest.TestCase):
    def test_report_uses_explicit_targets_and_marks_unknown_targets(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        out=result.stdout
        self.assertIn('1,141 | 3,000 minimum | **38.0%**',out)
        self.assertIn('1,141 | 5,000 planning ceiling | **22.8%**',out)
        self.assertIn('16/16 | All diagnostic questions | **100.0%**',out)
        self.assertIn('Chưa đo được',out)
        self.assertIn('not editorial approval',out)
        self.assertIn('US IPA | 1,048/1,141 | **91.8%**',out)
        self.assertIn('Word family | 276/1,141 | **24.2%**',out)
        self.assertIn('Word-family directed links | 374 links',out)
        self.assertIn('| Guided pathway stages represented | 3/6 | Pre-A1, A1, A2, B1, B2, C1 | **50.0%** |',out)
        self.assertIn('| Canonical objective-resource links | 339/339 |',out)
        self.assertIn('| Foundation outcome evidence wired | 6/6 | 100.0% |',out)
        self.assertIn('| Outcomes with evidence instrumentation | 6/33 | 18.2% |',out)
        self.assertIn('Foundation outcome evidence now records recognition',out)
    def test_report_includes_foundation_listening_bank_coverage(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Foundation Listening core scripts mapped | 23/23 | **100.0%**',result.stdout)
        self.assertIn('Foundation Listening questions | 59 core + 39 supplementary | Chưa đo được',result.stdout)
        self.assertIn('Foundation Reading | 23/23 passages / 59 questions',result.stdout)
        self.assertIn('Foundation Listening | 23/23 core scripts / 59 core questions + 13 supplementary A2 scripts / 39 questions',result.stdout)
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
