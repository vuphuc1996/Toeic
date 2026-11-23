import importlib.util
import unittest
from unittest.mock import patch
import json
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/run-release-acceptance.py"
spec = importlib.util.spec_from_file_location("release_acceptance_runner", SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def json_version():
    return json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))["version"]


class ReleaseAcceptanceRunnerTests(unittest.TestCase):

    def test_report_version_defaults_to_manifest_version(self):
        self.assertEqual(runner.resolve_version(ROOT), json_version())

    def test_explicit_report_version_overrides_manifest(self):
        self.assertEqual(runner.resolve_version(ROOT, "9.9.9"), "9.9.9")

    def test_command_names_are_unique(self):
        names = [name for name, _ in runner.COMMANDS]
        self.assertEqual(len(names), len(set(names)))

    def test_commands_include_full_suite_and_core_gates(self):
        names = {name for name, _ in runner.COMMANDS}
        self.assertTrue({"repository_integrity", "data_validator", "learning_content_validator", "version_sync", "full_python_suite"}.issubset(names))
        full_suite = next(command for name, command in runner.COMMANDS if name == "full_python_suite")
        self.assertIn("tools/run-python-tests-sharded.py", full_suite)
        self.assertIn("--timeout-per-module", full_suite)
        self.assertIn("--resume", full_suite)
        self.assertIn("--split-large-modules", full_suite)
        self.assertEqual(runner.COMMANDS[-1][0], "full_python_suite")

    def test_dry_run_records_not_run_without_execution(self):
        records = runner.run_commands(ROOT, 1, dry_run=True)
        self.assertEqual(len(records), len(runner.COMMANDS))
        self.assertTrue(all(record["status"] == "NOT_RUN" for record in records))

    def test_command_format_is_readable(self):
        self.assertEqual(runner.format_command(["python", "-m", "unittest"]), "python -m unittest")

    def test_nonzero_command_is_fail_and_runner_stops(self):
        with patch.object(runner, "COMMANDS", [("broken", ["fake"]), ("later", ["fake2"])]), \
             patch.object(runner.SHARDER, "run_isolated_command", return_value=(7, "bad", False)):
            records = runner.run_commands(ROOT, 1, dry_run=False)
        self.assertEqual([record["status"] for record in records], ["FAIL"])
        self.assertEqual(records[0]["exit_code"], 7)


    def test_timeout_is_explicit_and_runner_stops(self):
        with patch.object(runner, "COMMANDS", [("slow", ["fake"]), ("later", ["fake2"])]), \
             patch.object(runner.SHARDER, "run_isolated_command", return_value=(None, "partial", True)):
            records = runner.run_commands(ROOT, 1, dry_run=False)
        self.assertEqual([record["status"] for record in records], ["TIMEOUT"])
        self.assertIn("TIMEOUT after 1s; process group terminated", records[0]["output"])


    def test_report_does_not_promote_timeout_to_pass(self):
        report = runner.render_markdown([{"name": "suite", "command": "python tests", "status": "TIMEOUT", "exit_code": None, "duration_seconds": 2, "output": "timeout"}], "2.95.42", "2026-11-21T00:00:00Z")
        self.assertIn("INCOMPLETE / FAIL", report)
        self.assertIn("TIMEOUT", report)
        self.assertNotIn("Overall status: **PASS**", report)


    def test_json_report_uses_resolved_manifest_version(self):
        stamp = "2026-11-23T00:00:00Z"
        with TemporaryDirectory() as temp:
            json_path, md_path = runner.write_reports(Path(temp), [], json_version(), stamp)
            self.assertEqual(json.loads(json_path.read_text(encoding="utf-8"))["version"], json_version())
            self.assertIn(f"v{json_version()}", md_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
