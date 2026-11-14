"""Prevent newly added regression suites from being silently omitted from CI."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "tools/tests"
WORKFLOW = ROOT / ".github/workflows/validate-data.yml"


class ContinuousIntegrationCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_every_python_test_module_is_invoked_by_workflow(self):
        files = sorted(TESTS.glob("test_*.py"))
        commands = [line for line in self.workflow.splitlines() if "python -m unittest discover" in line]
        missing = [path.name for path in files if not any(f"-p '{path.name}'" in line for line in commands)]
        self.assertEqual(missing, [], f"Python test modules missing from CI: {missing}")

    def test_every_javascript_regression_suite_is_invoked_by_workflow(self):
        files = sorted(TESTS.glob("*.mjs"))
        missing = [path.name for path in files if f"node tools/tests/{path.name}" not in self.workflow]
        self.assertEqual(missing, [], f"JavaScript regression suites missing from CI: {missing}")


if __name__ == "__main__":
    unittest.main()
