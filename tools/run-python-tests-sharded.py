#!/usr/bin/env python3
"""Run Python unittest modules in isolated subprocesses with resumable checkpoints.

The runner preserves every module's unittest semantics. It does not skip, filter,
or rewrite tests; it isolates runtime and continues after failure/timeout. A
checkpoint is written after each module, so an interrupted outer process can be
resumed without re-running modules that already passed.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
RUN_RE = re.compile(r"Ran\s+(\d+)\s+tests?\s+in\s+[0-9.]+s", re.IGNORECASE)
SKIP_RE = re.compile(r"OK\s*\(skipped=(\d+)\)", re.IGNORECASE)
FAIL_RE = re.compile(r"FAILED\s*\(([^)]*)\)", re.IGNORECASE)


def discover_modules(root: Path) -> list[str]:
    tests_dir = root / "tools" / "tests"
    return sorted(path.name for path in tests_dir.glob("test_*.py") if path.is_file())


def _as_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value




def discover_test_cases(root: Path, module: str) -> list[tuple[str, str]]:
    """Return (TestCase class, method) pairs using AST without importing the module."""
    path = root / "tools" / "tests" / module
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    cases: list[tuple[str, str]] = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for member in node.body:
            if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)) and member.name.startswith("test_"):
                cases.append((node.name, member.name))
    return cases


def run_isolated_command(command: list[str], root: Path, timeout_seconds: int) -> tuple[int | None, str, bool]:
    """Run one shard in its own process group and reap descendants on timeout."""
    process = subprocess.Popen(
        command, cwd=root, text=True, encoding="utf-8", errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True,
    )
    try:
        output, _ = process.communicate(timeout=timeout_seconds)
        return process.returncode, output or "", False
    except subprocess.TimeoutExpired as exc:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        try:
            output, _ = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            output = _as_text(exc.stdout) + "\n[process group killed; output pipe did not close within 5s]"
        return None, output or "", True


def _run_case_batches(root: Path, module: str, timeout_seconds: int, group_size: int = 4) -> dict:
    """Run large modules in small unittest -k batches to bound per-process resource use."""
    cases = discover_test_cases(root, module)
    commands: list[list[str]] = []
    outputs: list[str] = []
    total_tests = 0
    total_skipped = 0
    elapsed = 0.0
    statuses: list[str] = []
    for offset in range(0, len(cases), group_size):
        group = cases[offset:offset + group_size]
        command = [
            sys.executable, "-m", "unittest", "discover",
            "-s", "tools/tests", "-p", module,
        ]
        for class_name, method_name in group:
            command.extend(["-k", f"{class_name}.{method_name}"])
        command.append("-v")
        commands.append(command)
        started = time.monotonic()
        return_code, output, timed_out = run_isolated_command(command, root, timeout_seconds)
        elapsed += time.monotonic() - started
        ran = RUN_RE.search(output)
        skipped = SKIP_RE.search(output)
        count = int(ran.group(1)) if ran else 0
        total_tests += count
        total_skipped += int(skipped.group(1)) if skipped else 0
        outputs.append(f"### Batch {len(commands)} — {len(group)} cases; exit={return_code if return_code is not None else 'TIMEOUT'}\n{output}")
        if timed_out:
            statuses.append("TIMEOUT")
        elif return_code == 0 and count == len(group):
            statuses.append("PASS")
        elif return_code not in (None, 0):
            statuses.append("FAIL")
        else:
            statuses.append("INCOMPLETE")
    status = "PASS" if statuses and all(x == "PASS" for x in statuses) and total_tests == len(cases) else (
        "FAIL" if "FAIL" in statuses else "TIMEOUT" if "TIMEOUT" in statuses else "INCOMPLETE"
    )
    return {
        "module": module, "command": None, "commands": commands,
        "execution_mode": "case-batched", "status": status,
        "exit_code": 0 if status == "PASS" else 1,
        "tests": total_tests, "skipped": total_skipped,
        "duration_seconds": round(elapsed, 3),
        "output_tail": "\n\n".join(outputs)[-12000:],
    }


def run_module(root: Path, module: str, timeout_seconds: int, *, split_large: bool = False, split_threshold: int = 25, group_size: int = 4) -> dict:
    if split_large and len(discover_test_cases(root, module)) > split_threshold:
        return _run_case_batches(root, module, timeout_seconds, group_size=group_size)
    command = [
        sys.executable, "-m", "unittest", "discover",
        "-s", "tools/tests", "-p", module, "-v",
    ]
    started = time.monotonic()
    record = {
        "module": module,
        "command": command,
        "status": "ERROR",
        "exit_code": None,
        "tests": 0,
        "skipped": 0,
        "duration_seconds": 0.0,
        "output_tail": "",
    }
    try:
        return_code, output, timed_out = run_isolated_command(command, root, timeout_seconds)
        ran = RUN_RE.search(output)
        failed = FAIL_RE.search(output)
        skipped = SKIP_RE.search(output)
        record["exit_code"] = return_code
        record["tests"] = int(ran.group(1)) if ran else 0
        record["skipped"] = int(skipped.group(1)) if skipped else 0
        if timed_out:
            record["status"] = "TIMEOUT"
            record["output_tail"] = output[-12000:] + f"\nTIMEOUT after {timeout_seconds}s\n"
        elif return_code == 0 and ran:
            record["status"] = "PASS"
        else:
            record["status"] = "FAIL" if return_code not in (None, 0) or failed else "INCOMPLETE"
            record["output_tail"] = output[-12000:]
    except OSError as exc:
        record["status"] = "ERROR"
        record["output_tail"] = f"{type(exc).__name__}: {exc}"
    record["duration_seconds"] = round(time.monotonic() - started, 3)
    return record


def run_modules(root: Path, modules: Iterable[str], timeout_seconds: int) -> list[dict]:
    """Run all requested modules serially; never stop after the first failure."""
    results = []
    for module in modules:
        result = run_module(root, module, timeout_seconds)
        results.append(result)
        print(
            f"[{result['status']}] {module}: "
            f"{result['tests']} tests, {result['duration_seconds']:.2f}s",
            flush=True,
        )
    return results


def ordered_results(modules: list[str], result_map: dict[str, dict]) -> tuple[list[dict], list[str]]:
    results = [result_map[name] for name in modules if name in result_map]
    pending = [name for name in modules if name not in result_map]
    return results, pending


def should_run_module(module: str, result_map: dict[str, dict]) -> bool:
    """Resume skips only modules already proven PASS; all other states are retried."""
    return result_map.get(module, {}).get("status") != "PASS"


def summary(results: list[dict], total_modules: int | None = None, pending_modules: int = 0) -> dict:
    total = len(results) if total_modules is None else total_modules
    complete = len(results) == total and pending_modules == 0
    every_pass = complete and all(row["status"] == "PASS" for row in results)
    return {
        "module_count": total,
        "completed_modules": len(results),
        "pending_modules": pending_modules,
        "passed_modules": sum(row["status"] == "PASS" for row in results),
        "failed_modules": sum(row["status"] == "FAIL" for row in results),
        "timed_out_modules": sum(row["status"] == "TIMEOUT" for row in results),
        "incomplete_modules": sum(row["status"] == "INCOMPLETE" for row in results),
        "error_modules": sum(row["status"] == "ERROR" for row in results),
        "discovered_test_cases": sum(row["tests"] for row in results),
        "skipped_test_cases": sum(row["skipped"] for row in results),
        "overall_status": "PASS" if every_pass else "INCOMPLETE / FAIL",
    }


def render_markdown(
    version: str,
    timestamp: str,
    results: list[dict],
    total_modules: int | None = None,
    pending_modules: list[str] | None = None,
) -> str:
    pending_modules = pending_modules or []
    total = len(results) if total_modules is None else total_modules
    stats = summary(results, total, len(pending_modules))
    lines = [
        f"# Sharded Python Test Run — v{version}",
        "",
        f"- Timestamp (UTC): {timestamp}",
        f"- Overall: **{stats['overall_status']}**",
        f"- Modules: {stats['passed_modules']}/{stats['module_count']} passed; "
        f"{stats['failed_modules']} failed; {stats['timed_out_modules']} timed out; "
        f"{stats['incomplete_modules']} incomplete; {stats['error_modules']} errors; "
        f"{stats['pending_modules']} not yet run",
        f"- Test cases reported by completed modules: {stats['discovered_test_cases']}",
        f"- Skipped tests reported by completed modules: {stats['skipped_test_cases']}",
        "",
        "| Module | Mode | Status | Cases | Skipped | Exit | Seconds |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for row in results:
        exit_code = row["exit_code"] if row["exit_code"] is not None else "—"
        lines.append(
            f"| `{row['module']}` | {row.get('execution_mode', 'module')} | {row['status']} | {row['tests']} | {row['skipped']} | "
            f"{exit_code} | {row['duration_seconds']:.3f} |"
        )
    if pending_modules:
        lines += ["", "## Not yet run", ""]
        lines.extend(f"- `{module}`" for module in pending_modules)
    for row in results:
        if row["output_tail"]:
            lines += ["", f"## Diagnostic output — {row['module']}", "", "```text", row["output_tail"].rstrip(), "```"]
    lines += [
        "",
        "Policy: modules run in separate subprocesses, but their tests are not changed or skipped. "
        "A module is PASS only when unittest returns exit code 0 and emits a valid `Ran N tests` summary. "
        "Overall PASS requires every discovered module to PASS.",
        "",
    ]
    return "\n".join(lines)


def write_checkpoint(
    report_dir: Path,
    version: str,
    timestamp: str,
    modules: list[str],
    result_map: dict[str, dict],
) -> tuple[Path, Path]:
    report_dir.mkdir(parents=True, exist_ok=True)
    results, pending = ordered_results(modules, result_map)
    stats = summary(results, len(modules), len(pending))
    stem = f"PYTHON_TEST_SHARDS_v{version}"
    json_path = report_dir / f"{stem}.json"
    md_path = report_dir / f"{stem}.md"
    payload = {
        "version": version,
        "timestamp_utc": timestamp,
        "modules": modules,
        "summary": stats,
        "results": results,
        "pending_modules": pending,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(version, timestamp, results, len(modules), pending), encoding="utf-8")
    return json_path, md_path


def load_checkpoint(path: Path, version: str, modules: list[str]) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("version") != version:
        raise ValueError(f"checkpoint version mismatch: {payload.get('version')} != {version}")
    if payload.get("modules") != modules:
        raise ValueError("checkpoint module inventory differs from the current test inventory")
    results = payload.get("results", [])
    result_map = {}
    for row in results:
        name = row.get("module")
        if name not in modules or name in result_map:
            raise ValueError(f"invalid or duplicate module in checkpoint: {name!r}")
        result_map[name] = row
    return result_map


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--timeout-per-module", type=int, default=180)
    parser.add_argument("--only", action="append", default=[], help="run only this exact test module filename; repeatable")
    parser.add_argument("--list", action="store_true", help="list discovered module names without executing")
    parser.add_argument("--report-dir", type=Path, default=None)
    parser.add_argument("--version", default=None)
    parser.add_argument("--resume", action="store_true", help="resume the versioned checkpoint; PASS modules are not rerun")
    parser.add_argument("--split-large-modules", action="store_true", help="run modules with >25 test methods in isolated batches of four")
    args = parser.parse_args()

    root = args.root.resolve()
    modules = discover_modules(root)
    if args.only:
        unknown = sorted(set(args.only) - set(modules))
        if unknown:
            parser.error(f"unknown test modules: {', '.join(unknown)}")
        selected = [name for name in modules if name in set(args.only)]
    else:
        selected = modules
    if args.list:
        for module in modules:
            print(module)
        print(f"MODULES={len(modules)}")
        return 0

    manifest = json.loads((root / "data/manifest.json").read_text(encoding="utf-8"))
    version = args.version or manifest.get("version", "unknown")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    report_dir = args.report_dir.resolve() if args.report_dir else root / "docs/reports"
    stem = f"PYTHON_TEST_SHARDS_v{version}"
    checkpoint_path = report_dir / f"{stem}.json"
    if args.resume and checkpoint_path.exists():
        result_map = load_checkpoint(checkpoint_path, version, modules)
        print(f"RESUME: {sum(row['status'] == 'PASS' for row in result_map.values())} PASS modules retained from checkpoint")
    else:
        result_map = {}
    write_checkpoint(report_dir, version, timestamp, modules, result_map)

    for module in selected:
        if args.resume and not should_run_module(module, result_map):
            continue
        result = run_module(root, module, max(1, args.timeout_per_module), split_large=args.split_large_modules)
        result_map[module] = result
        print(
            f"[{result['status']}] {module}: "
            f"{result['tests']} tests, {result['duration_seconds']:.2f}s",
            flush=True,
        )
        write_checkpoint(report_dir, version, timestamp, modules, result_map)

    results, pending = ordered_results(modules, result_map)
    stats = summary(results, len(modules), len(pending))
    print(
        f"SUMMARY: {stats['passed_modules']}/{stats['module_count']} modules PASS; "
        f"{stats['discovered_test_cases']} completed test cases; "
        f"{stats['timed_out_modules']} timeout(s); {stats['failed_modules']} failure(s); "
        f"{stats['pending_modules']} pending module(s)"
    )
    return 0 if stats["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
