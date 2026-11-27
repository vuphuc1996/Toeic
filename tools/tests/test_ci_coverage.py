"""Prevent newly added regression suites from being silently omitted from CI."""
import fnmatch
from collections import Counter
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
        files = sorted(TESTS.rglob("test_*.py"))
        commands = [line for line in self.workflow.splitlines() if "python -m unittest discover" in line]
        patterns = []
        for line in commands:
            explicit = re.findall(r"-p ['\"]([^'\"]+)['\"]", line)
            patterns.extend(explicit or ["test*.py"])  # unittest's documented default
        missing = [path.name for path in files if not any(fnmatch.fnmatchcase(path.name, pattern) for pattern in patterns)]
        self.assertEqual(missing, [], f"Python test modules missing from CI: {missing}")

    def test_github_actions_are_pinned_to_verified_full_commit_shas(self):
        expected = {
            "actions/checkout": "3d3c42e5aac5ba805825da76410c181273ba90b1",
            "actions/setup-python": "6d4fd22b20465ccc0f7354476588e8df7c9ca0e0",
            "actions/setup-node": "949feb2413d6458794dcd2491c4babbbce0c15c1",
        }
        uses = dict(re.findall(r"uses:\s+([\w.-]+/[\w.-]+)@([0-9a-f]{40})", self.workflow))
        for action, sha in expected.items():
            self.assertEqual(uses.get(action), sha, f"{action} must stay pinned to the reviewed immutable commit")

    def test_unittest_patterns_and_step_names_are_not_duplicated(self):
        commands = [line for line in self.workflow.splitlines() if "python -m unittest discover" in line]
        explicit_patterns = [pattern for line in commands for pattern in re.findall(r"-p ['\"]([^'\"]+)['\"]", line)]
        duplicate_patterns = {pattern: count for pattern, count in Counter(explicit_patterns).items() if count > 1}
        self.assertEqual(duplicate_patterns, {}, f"Duplicate Python test invocations: {duplicate_patterns}")
        step_names = [name.strip() for name in re.findall(r"^\s*- name:\s*(.+)$", self.workflow, re.MULTILINE)]
        duplicate_names = {name: count for name, count in Counter(step_names).items() if count > 1}
        self.assertEqual(duplicate_names, {}, f"Duplicate GitHub Actions step names: {duplicate_names}")

    def test_git_commit_preflight_runs_before_repository_validation(self):
        preflight = self.workflow.index("python tools/audit-git-commit-readiness.py --require-clean")
        integrity = self.workflow.index("python tools/audit-repository-integrity.py")
        self.assertLess(preflight, integrity)

    def test_python_syntax_check_compiles_the_entire_tools_tree(self):
        self.assertIn("python -m compileall -q tools", self.workflow)

    def test_batch_035_pattern_covers_cambridge_split_module(self):
        patterns = re.findall(r"-p ['\"]([^'\"]+)['\"]", self.workflow)
        relative = Path('tools/tests/test_related_glossary_batch_035_cambridge.py')
        self.assertTrue(any(relative.match(pattern) for pattern in patterns),
                        "Batch 035 Cambridge split tests must be selected by a unittest discover glob used by the repository preflight")

    def test_every_javascript_regression_suite_is_invoked_by_workflow(self):
        files = sorted(TESTS.glob("*.mjs"))
        missing = [path.name for path in files if f"node tools/tests/{path.name}" not in self.workflow]
        self.assertEqual(missing, [], f"JavaScript regression suites missing from CI: {missing}")

    def test_word_family_report_path_uses_manifest_release_dynamically(self):
        self.assertIn('release-keyed report', self.workflow)
        self.assertIn('Path("data/manifest.json")', self.workflow)
        self.assertIn('WORD_FAMILY_GRAPH_AUDIT_v{version}.md', self.workflow)
        self.assertIn('WORD_FAMILY_GRAPH_AUDIT_v{version}.json', self.workflow)
        self.assertNotIn('WORD_FAMILY_GRAPH_AUDIT_v2.95.68', self.workflow)

    def test_editorial_review_has_one_explicit_ci_execution_step(self):
        command = "python -m unittest discover -s tools/tests -p 'test_editorial_review.py' -v"
        matches = [line.strip() for line in self.workflow.splitlines() if command in line]
        self.assertEqual(len(matches), 1, "editorial_review must run exactly once as a dedicated CI step")
        self.assertIn('"tools/**"', self.workflow)
        self.assertIn(".github/workflows/validate-data.yml", self.workflow)

    def test_candidate_branch_is_in_push_validation_trigger(self):
        self.assertIn("branches: [main, master, candidate]", self.workflow)

    def test_root_runtime_and_project_files_are_in_path_filters(self):
        required_paths = [".env.example", "README.md", "metadata.json", "package.json", "server.js"]
        for path in required_paths:
            with self.subTest(path=path):
                self.assertGreaterEqual(self.workflow.count(f'"{path}"'), 2,
                                        f"{path} must trigger validation on push and pull request")

    def test_preview_server_serves_only_public_runtime_directories(self):
        server = (ROOT / "server.js").read_text(encoding="utf-8")
        self.assertIn('express.static(path.join(__dirname, "assets")', server)
        self.assertIn('express.static(path.join(__dirname, "data")', server)
        self.assertNotIn("express.static(__dirname", server)
        self.assertIn('app.get(["/", "/index.html"]', server)
        self.assertIn("app.use((req, res) => res.status(404).end())", server)


if __name__ == "__main__":
    unittest.main()
