"""Prevent newly added regression suites from being silently omitted from CI."""
import fnmatch
import re
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
        patterns = [pattern for line in commands for pattern in re.findall(r"-p ['\"]([^'\"]+)['\"]", line)]
        missing = [path.name for path in files if not any(fnmatch.fnmatchcase(path.name, pattern) for pattern in patterns)]
        self.assertEqual(missing, [], f"Python test modules missing from CI: {missing}")

    def test_batch_035_pattern_covers_cambridge_split_module(self):
        patterns = re.findall(r"-p ['\"]([^'\"]+)['\"]", self.workflow)
        relative = Path('tools/tests/test_related_glossary_batch_035_cambridge.py')
        self.assertTrue(any(relative.match(pattern) for pattern in patterns),
                        "Batch 035 Cambridge split tests must be selected by a unittest discover glob used by the repository preflight")

    def test_every_javascript_regression_suite_is_invoked_by_workflow(self):
        files = sorted(TESTS.glob("*.mjs"))
        missing = [path.name for path in files if f"node tools/tests/{path.name}" not in self.workflow]
        self.assertEqual(missing, [], f"JavaScript regression suites missing from CI: {missing}")

    def test_editorial_review_has_one_explicit_ci_execution_step(self):
        command = "python -m unittest discover -s tools/tests -p 'test_editorial_review.py' -v"
        matches = [line.strip() for line in self.workflow.splitlines() if command in line]
        self.assertEqual(len(matches), 1, "editorial_review must run exactly once as a dedicated CI step")
        self.assertIn('"tools/**"', self.workflow)
        self.assertIn(".github/workflows/validate-data.yml", self.workflow)


if __name__ == "__main__":
    unittest.main()
