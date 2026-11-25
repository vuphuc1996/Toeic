"""CI contract for local references and workflow coverage."""
import subprocess
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT_PATH = ROOT / "tools/audit-repository-integrity.py"
_spec = importlib.util.spec_from_file_location("repository_integrity_audit", AUDIT_PATH)
_audit = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_audit)


class RepositoryIntegrityTests(unittest.TestCase):
    def test_default_unittest_discovery_pattern_is_recognized(self):
        patterns = _audit.configured_unittest_patterns(
            "python -m unittest discover -s tools/tests -v\n"
            "python -m unittest discover -s tools/tests -p 'test_focus.py' -v\n"
        )
        self.assertIn("test*.py", patterns)
        self.assertIn("test_focus.py", patterns)

    def test_repository_integrity_preflight_passes(self):
        result = subprocess.run(
            [sys.executable, 'tools/audit-repository-integrity.py'],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('Errors: 0', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
