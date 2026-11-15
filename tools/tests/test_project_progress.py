import subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ProjectProgressTests(unittest.TestCase):
    def test_report_uses_explicit_targets_and_marks_unknown_targets(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        out=result.stdout
        self.assertIn('992 | 3,000 minimum | **33.1%**',out)
        self.assertIn('992 | 5,000 planning ceiling | **19.8%**',out)
        self.assertIn('16/16 | All diagnostic questions | **100.0%**',out)
        self.assertIn('Chưa đo được',out)
        self.assertIn('not editorial approval',out)
    def test_report_does_not_mislabel_inventory_as_completion(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Content counts do not equal completed learning outcomes.',result.stdout)
        self.assertIn('independent review',result.stdout)
if __name__=='__main__': unittest.main()
