"""CI contract for local references and workflow coverage."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class RepositoryIntegrityTests(unittest.TestCase):
    def test_repository_integrity_preflight_passes(self):
        result = subprocess.run(
            [sys.executable, 'tools/audit-repository-integrity.py'],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('Errors: 0', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
