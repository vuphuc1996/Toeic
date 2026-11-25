"""Regression tests for isolated, non-fail-fast Python test execution."""
from __future__ import annotations
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/run-python-tests-sharded.py"
spec = importlib.util.spec_from_file_location("python_test_shard_runner", SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class PythonTestShardRunnerTests(unittest.TestCase):
    def test_discovery_is_sorted_and_limited_to_test_modules(self):
        names = runner.discover_modules(ROOT)
        self.assertEqual(names, sorted(names))
        self.assertTrue(names)
        self.assertTrue(all(name.startswith("tools/tests/test_") and name.endswith(".py") for name in names))

    def test_module_pass_requires_exit_zero_and_unittest_summary(self):
        output = "test_one (sample.Test) ... ok\n\nRan 1 test in 0.001s\n\nOK\n"
        with patch.object(runner, "run_isolated_command", return_value=(0, output, False)):
            result = runner.run_module(ROOT, "test_sample.py", 5)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["tests"], 1)
        self.assertEqual(result["exit_code"], 0)

    def test_large_module_can_be_run_in_case_batches(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            test_dir = root / "tools" / "tests"
            test_dir.mkdir(parents=True)
            (test_dir / "test_large.py").write_text(
                "import unittest\nclass DemoTests(unittest.TestCase):\n"
                "    def test_one(self): pass\n    def test_two(self): pass\n"
                "    def test_three(self): pass\n", encoding="utf-8"
            )
            results = [(0, "Ran 2 tests in 0.001s\n\nOK\n", False), (0, "Ran 1 test in 0.001s\n\nOK\n", False)]
            with patch.object(runner, "run_isolated_command", side_effect=results) as run:
                result = runner.run_module(root, "test_large.py", 5, split_large=True, split_threshold=2, group_size=2)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["execution_mode"], "case-batched")
            self.assertEqual(result["tests"], 3)
            self.assertEqual(len(result["commands"]), 2)
            self.assertEqual(run.call_count, 2)

    def test_zero_exit_without_unittest_summary_is_not_pass(self):
        with patch.object(runner, "run_isolated_command", return_value=(0, "no tests discovered", False)):
            result = runner.run_module(ROOT, "test_empty.py", 5)
        self.assertEqual(result["status"], "INCOMPLETE")

    def test_timeout_is_recorded_without_raising(self):
        with patch.object(runner, "run_isolated_command", return_value=(None, "partial", True)):
            result = runner.run_module(ROOT, "test_slow.py", 1)
        self.assertEqual(result["status"], "TIMEOUT")
        self.assertIn("TIMEOUT after 1s", result["output_tail"])


    def test_module_timeout_kills_child_process_group(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tests = root / "tools" / "tests"
            tests.mkdir(parents=True)
            (tests / "test_hanging.py").write_text(
                "import subprocess, sys, time, unittest\n"
                "class HangingTests(unittest.TestCase):\n"
                "    def test_child_inherits_pipe(self):\n"
                "        subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'])\n"
                "        time.sleep(30)\n",
                encoding="utf-8",
            )
            result = runner.run_module(root, "test_hanging.py", 1)
            self.assertEqual(result["status"], "TIMEOUT")
            self.assertEqual(result["exit_code"], None)
            self.assertIn("TIMEOUT after 1s", result["output_tail"])

    def test_nonzero_exit_is_failure_and_output_is_retained(self):
        with patch.object(runner, "run_isolated_command", return_value=(2, "FAILED (errors=1)", False)):
            result = runner.run_module(ROOT, "test_broken.py", 5)
        self.assertEqual(result["status"], "ERROR")
        self.assertIn("FAILED", result["output_tail"])

    def test_runner_continues_after_timeout_and_failure(self):
        records = [
            {"status": "TIMEOUT", "module": "test_a.py", "tests": 0, "duration_seconds": 1.0},
            {"status": "PASS", "module": "test_b.py", "tests": 2, "duration_seconds": 0.2},
        ]
        with patch.object(runner, "run_module", side_effect=records) as run_one:
            result = runner.run_modules(ROOT, ["test_a.py", "test_b.py"], 1)
        self.assertEqual([row["status"] for row in result], ["TIMEOUT", "PASS"])
        self.assertEqual(run_one.call_count, 2)

    def test_overall_pass_requires_every_module_to_pass(self):
        stats = runner.summary([
            {"status": "PASS", "tests": 3, "skipped": 0},
            {"status": "TIMEOUT", "tests": 0, "skipped": 0},
        ])
        self.assertEqual(stats["overall_status"], "INCOMPLETE / FAIL")
        self.assertEqual(stats["discovered_test_cases"], 3)
        self.assertEqual(stats["timed_out_modules"], 1)

    def test_resume_toggle_does_not_change_checkpoint_execution_identity(self):
        inventory_delta = {"baseline_status": "COMPARED", "added": [], "removed": []}
        first_run = runner.build_execution_config(180, ["tools/tests/test_a.py"], False, inventory_delta)
        resumed_run = runner.build_execution_config(180, ["tools/tests/test_a.py"], False, inventory_delta)
        self.assertEqual(first_run, resumed_run)
        self.assertNotIn("resume", first_run)
        self.assertNotIn("exact_runner_arguments", first_run)

    def test_checkpoint_persists_partial_results_and_pending_modules(self):
        with tempfile.TemporaryDirectory() as directory:
            modules = ["test_a.py", "test_b.py"]
            result_map = {"test_a.py": {"module": "test_a.py", "status": "PASS", "tests": 2, "skipped": 0,
                                       "exit_code": 0, "duration_seconds": 0.1, "command": [], "output_tail": ""}}
            json_path, md_path = runner.write_checkpoint(Path(directory), "2.95.43", "2026-11-23T00:00:00Z", modules, result_map)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["completed_modules"], 1)
            self.assertEqual(payload["summary"]["pending_modules"], 1)
            self.assertEqual(payload["summary"]["overall_status"], "INCOMPLETE / FAIL")
            self.assertIn("test_b.py", md_path.read_text(encoding="utf-8"))

    def test_checkpoint_resume_retries_nonpass_but_skips_pass(self):
        statuses = {"test_a.py": {"status": "PASS"}, "test_b.py": {"status": "TIMEOUT"},
                    "test_c.py": {"status": "PASS WITH SKIPS", "skip_policy_status": "ACCEPTED"},
                    "test_d.py": {"status": "PASS WITH SKIPS", "skip_policy_status": "UNAPPROVED"}}
        self.assertFalse(runner.should_run_module("test_a.py", statuses))
        self.assertTrue(runner.should_run_module("test_b.py", statuses))
        self.assertFalse(runner.should_run_module("test_c.py", statuses))
        self.assertTrue(runner.should_run_module("test_d.py", statuses))
        self.assertTrue(runner.should_run_module("test_e.py", statuses))

    def test_checkpoint_rejects_changed_inventory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.json"
            path.write_text(json.dumps({"version": "2.95.43", "modules": ["test_a.py"], "results": []}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "inventory differs"):
                runner.load_checkpoint(path, "2.95.43", ["test_a.py", "test_b.py"])


    def test_inventory_reports_added_removed_and_content_modified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tools/tests").mkdir(parents=True)
            (root / "tools/test-inventory-policy.json").write_text(json.dumps({
                "baseline_inventory": "tools/baseline.json"
            }), encoding="utf-8")
            (root / "tools/baseline.json").write_text(json.dumps({
                "baselineVersion": "2.95.45",
                "modules": [
                    {"path": "tools/tests/test_keep.py", "sha256": "old", "size": 3},
                    {"path": "tools/tests/test_removed.py", "sha256": "gone", "size": 3},
                ],
            }), encoding="utf-8")
            (root / "tools/tests/test_keep.py").write_text("new", encoding="utf-8")
            (root / "tools/tests/test_added.py").write_text("add", encoding="utf-8")
            delta = runner.compare_inventory_to_baseline(root, [
                "tools/tests/test_keep.py", "tools/tests/test_added.py"
            ])
            self.assertEqual(delta["added"], ["tools/tests/test_added.py"])
            self.assertEqual(delta["removed"], ["tools/tests/test_removed.py"])
            self.assertEqual(delta["modified"], ["tools/tests/test_keep.py"])

    def test_unapproved_skips_do_not_reuse_checkpoint_results(self):
        result_map = {"test_a.py": {"status": "PASS WITH SKIPS", "skip_policy_status": "UNAPPROVED"}}
        self.assertTrue(runner.should_run_module("test_a.py", result_map))


    def test_inventory_reports_added_removed_and_content_modified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tools/tests").mkdir(parents=True)
            (root / "tools/test-inventory-policy.json").write_text(json.dumps({
                "baseline_inventory": "tools/baseline.json"
            }), encoding="utf-8")
            (root / "tools/baseline.json").write_text(json.dumps({
                "baselineVersion": "2.95.45",
                "modules": [
                    {"path": "tools/tests/test_keep.py", "sha256": "old", "size": 3},
                    {"path": "tools/tests/test_removed.py", "sha256": "gone", "size": 3},
                ],
            }), encoding="utf-8")
            (root / "tools/tests/test_keep.py").write_text("new", encoding="utf-8")
            (root / "tools/tests/test_added.py").write_text("add", encoding="utf-8")
            delta = runner.compare_inventory_to_baseline(root, [
                "tools/tests/test_keep.py", "tools/tests/test_added.py"
            ])
            self.assertEqual(delta["added"], ["tools/tests/test_added.py"])
            self.assertEqual(delta["removed"], ["tools/tests/test_removed.py"])
            self.assertEqual(delta["modified"], ["tools/tests/test_keep.py"])

    def test_unapproved_skips_do_not_reuse_checkpoint_results(self):
        result_map = {"test_a.py": {"status": "PASS WITH SKIPS", "skip_policy_status": "UNAPPROVED"}}
        self.assertTrue(runner.should_run_module("test_a.py", result_map))


    def test_simulated_timeout_log_does_not_mark_completed_module_as_timeout(self):
        output = (
            "[TIMEOUT] test_fake.py: 0 tests, 1.00s\n"
            "test_runner_continues_after_timeout_and_failure (sample.Test) ... ok\n\n"
            "Ran 17 tests in 1.758s\n\nOK\n"
        )
        counts = runner.parse_test_counts(output, 0)
        self.assertEqual(counts["status"], "PASS")
        self.assertEqual(counts["tests"], 17)
        self.assertEqual(counts["passed"], 17)

    def test_test_case_counts_and_skip_reasons_are_parsed(self):
        output = (
            "test_one (sample.Test) ... ok\n"
            "test_two (sample.Test) ... skipped 'environment lacks capability'\n\n"
            "Ran 2 tests in 0.001s\n\nOK (skipped=1)\n"
        )
        counts = runner.parse_test_counts(output, 0)
        self.assertEqual(counts["tests"], 2)
        self.assertEqual(counts["passed"], 1)
        self.assertEqual(counts["skipped"], 1)
        self.assertEqual(counts["skip_details"], [{"test": "test_two (sample.Test)", "reason": "environment lacks capability"}])


    def test_checkpoint_rejects_changed_source_and_environment_fingerprints(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.json"
            modules = ["tools/tests/test_a.py"]
            expected = {
                "source_release_fingerprint": "source-a",
                "fingerprint": "input-a",
                "environment_fingerprint": "env-a",
                "inventory_fingerprint": "inventory-a",
            }
            path, _ = runner.write_checkpoint(Path(directory), "2.95.46", "2026-11-23T00:00:00Z", modules, {}, expected, {"args": ["-v"]})
            with self.assertRaisesRegex(ValueError, "source_release_fingerprint"):
                runner.load_checkpoint(path, "2.95.46", modules, {**expected, "source_release_fingerprint": "source-b"}, {"args": ["-v"]})
            with self.assertRaisesRegex(ValueError, "environment_fingerprint"):
                runner.load_checkpoint(path, "2.95.46", modules, {**expected, "environment_fingerprint": "env-b"}, {"args": ["-v"]})

    def test_inventory_discovery_error_is_written_as_error_not_empty_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report_dir = root / "test-evidence"
            old_argv = __import__("sys").argv
            try:
                __import__("sys").argv = [str(SCRIPT), "--root", str(root), "--report-dir", str(report_dir)]
                self.assertEqual(runner.main(), 1)
            finally:
                __import__("sys").argv = old_argv
            files = list(report_dir.glob("PYTHON_TEST_INVENTORY_ERROR_v*.json"))
            self.assertEqual(len(files), 1)
            payload = json.loads(files[0].read_text(encoding="utf-8"))
            self.assertEqual(payload["overall_status"], "ERROR")
            self.assertEqual(payload["discovered_modules"], 0)
            self.assertEqual(payload["test_cases"]["passed"], 0)


if __name__ == "__main__":
    unittest.main()
