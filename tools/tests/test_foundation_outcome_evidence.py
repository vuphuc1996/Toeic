import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class FoundationOutcomeEvidenceTests(unittest.TestCase):
    def test_foundation_outcome_evidence_contract(self):
        result = subprocess.run(
            ['node', str(ROOT / 'tools/tests/foundation-outcome-evidence.mjs')],
            cwd=ROOT, capture_output=True, text=True, timeout=30
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('PASS:', result.stdout)

    def test_existing_foundation_store_is_preserved(self):
        app = (ROOT / 'assets/js/app.js').read_text(encoding='utf-8')
        self.assertIn("toeic:foundation-progress:v1", app)
        self.assertIn("DB_NAME = 'toeic-vocabulary-phase1'", app)


if __name__ == '__main__':
    unittest.main()
