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
import difflib
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from test_fingerprints import test_input_fingerprint
except ModuleNotFoundError:  # Imported from a test harness rather than executed as a script.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from test_fingerprints import test_input_fingerprint
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
RUN_RE = re.compile(r"Ran\s+(\d+)\s+tests?\s+in\s+[0-9.]+s", re.IGNORECASE)
SKIP_RE = re.compile(r"OK\s*\(skipped=(\d+)\)", re.IGNORECASE)
FAIL_RE = re.compile(r"FAILED\s*\(([^)]*)\)", re.IGNORECASE)
FAILURE_COUNT_RE = re.compile(r"failures=(\d+)", re.IGNORECASE)
ERROR_COUNT_RE = re.compile(r"errors=(\d+)", re.IGNORECASE)
SKIPPED_COUNT_RE = re.compile(r"skipped=(\d+)", re.IGNORECASE)
SKIP_LINE_RE = re.compile(r"^(.*?)\s+\.\.\.\s+skipped ['\"](.*?)['\"]\s*$", re.MULTILINE)
IMPORT_ERROR_RE = re.compile(r"(?:ImportError|ModuleNotFoundError|SyntaxError|Failed to import test module|could not be imported)", re.IGNORECASE)


def discover_modules(root: Path) -> list[str]:
    """Dynamically discover test modules beneath the approved test root(s).

    The current policy has one approved root (tools/tests). Discovery is recursive
    so future nested test packages are not silently omitted. IDs are root-relative
    POSIX paths and remain unique even when two folders use the same basename.
    """
    policy_path = root / "tools" / "test-inventory-policy.json"
    if policy_path.exists():
        policy = json.loads(policy_path.read_text(encoding="utf-8"))
        roots = policy.get("approved_roots", [])
        patterns = policy.get("include_patterns", ["test_*.py"])
        exclusions = policy.get("exclude_paths", [])
    else:
        roots, patterns, exclusions = ["tools/tests"], ["test_*.py"], []
    found: set[str] = set()
    for root_name in roots:
        test_root = (root / root_name).resolve()
        if not test_root.is_dir() or not test_root.is_relative_to(root.resolve()):
            raise ValueError(f"approved test root is missing or escapes source root: {root_name}")
        for pattern in patterns:
            for path in test_root.rglob(pattern):
                if path.is_symlink():
                    raise ValueError(f"discovered test module is a symbolic link and cannot be silently excluded: {path.relative_to(root).as_posix()}")
                if not path.is_file():
                    continue
                relative = path.relative_to(root).as_posix()
                normalized = relative.replace("\\", "/")
                if any(normalized == item or normalized.startswith(item.rstrip("/") + "/") for item in exclusions):
                    continue
                found.add(normalized)
    return sorted(found, key=lambda item: item.encode("utf-8"))


def build_execution_config(
    timeout_per_module: int,
    selected_modules: list[str],
    split_large_modules: bool,
    inventory_delta: dict,
) -> dict:
    """Build checkpoint identity from test semantics, not resume mechanics.

    The --resume flag only controls whether a compatible checkpoint is loaded;
    it does not change the tests, environment, timeout, or command being tested.
    Including it here would make a first run (without --resume) impossible to
    continue on a later invocation (with --resume).
    """
    return {
        "timeout_per_module": max(1, timeout_per_module),
        "selected_modules": selected_modules,
        "split_large_modules": bool(split_large_modules),
        "split_threshold": 25,
        "group_size": 4,
        "python_executable_name": Path(sys.executable).name,
        "python_executable_path": Path(sys.executable).resolve().as_posix(),
        "command_template": [sys.executable, "-m", "unittest", "discover", "-s", "<module-parent>", "-p", "<module-pattern>", "-v"],
        "inventory_delta": inventory_delta,
    }


def load_test_policy(root: Path) -> dict:
    path = root / "tools" / "test-inventory-policy.json"
    if not path.exists():
        return {"accepted_environment_skip_reasons": [], "baseline_inventory": None}
    return json.loads(path.read_text(encoding="utf-8"))


def compare_inventory_to_baseline(root: Path, modules: list[str]) -> dict:
    policy = load_test_policy(root)
    baseline_name = policy.get("baseline_inventory")
    if not baseline_name:
        return {"baseline_status": "NOT_CONFIGURED", "baseline_version": None, "added": modules, "removed": [], "modified": [], "confirmed_renames": [], "suspected_renames": []}
    path = root / baseline_name
    if not path.is_file():
        raise FileNotFoundError(f"test inventory baseline missing: {baseline_name}")
    baseline = json.loads(path.read_text(encoding="utf-8"))
    baseline_rows = {row["path"]: row for row in baseline.get("modules", [])}
    current_rows = {}
    for module in modules:
        module_path = root / module
        current_rows[module] = {
            "path": module,
            "sha256": __import__("hashlib").sha256(module_path.read_bytes()).hexdigest(),
            "size": module_path.stat().st_size,
        }
    old_paths, new_paths = set(baseline_rows), set(current_rows)
    added, removed = sorted(new_paths - old_paths), sorted(old_paths - new_paths)
    old_by_hash: dict[str, list[str]] = {}
    new_by_hash: dict[str, list[str]] = {}
    for name in removed:
        old_by_hash.setdefault(baseline_rows[name]["sha256"], []).append(name)
    for name in added:
        new_by_hash.setdefault(current_rows[name]["sha256"], []).append(name)
    confirmed = []
    for digest in sorted(set(old_by_hash) & set(new_by_hash)):
        if len(old_by_hash[digest]) == len(new_by_hash[digest]) == 1:
            confirmed.append({"from": old_by_hash[digest][0], "to": new_by_hash[digest][0], "sha256": digest})
    renamed_old = {row["from"] for row in confirmed}
    renamed_new = {row["to"] for row in confirmed}
    added_remaining = [name for name in added if name not in renamed_new]
    removed_remaining = [name for name in removed if name not in renamed_old]
    modified = sorted(name for name in old_paths & new_paths if baseline_rows[name]["sha256"] != current_rows[name]["sha256"])
    suspected = []
    for old_name in removed_remaining:
        old_stem = Path(old_name).stem
        candidates = []
        for new_name in added_remaining:
            new_stem = Path(new_name).stem
            ratio = difflib.SequenceMatcher(a=old_stem, b=new_stem).ratio()
            same_basename = Path(old_name).name == Path(new_name).name
            if same_basename or ratio >= 0.82:
                candidates.append({"to": new_name, "similarity": round(ratio, 3), "same_basename": same_basename})
        if candidates:
            candidates.sort(key=lambda item: (not item["same_basename"], -item["similarity"], item["to"]))
            suspected.append({"from": old_name, "candidates": candidates[:3], "requires_manual_confirmation": True})
    return {
        "baseline_status": "COMPARED",
        "baseline_version": baseline.get("baselineVersion"),
        "baseline_module_count": len(baseline_rows),
        "current_module_count": len(current_rows),
        "added": added_remaining,
        "removed": removed_remaining,
        "modified": modified,
        "confirmed_renames": confirmed,
        "suspected_renames": suspected,
    }


def apply_skip_policy(result: dict, policy: dict) -> dict:
    details = result.get("skip_details", [])
    if not result.get("skipped", 0):
        result["skip_policy_status"] = "NOT_APPLICABLE"
        return result
    accepted = policy.get("accepted_environment_skip_reasons", [])
    reasons = [item.get("reason", "") for item in details]
    approved = bool(reasons) and all(any(re.fullmatch(pattern, reason) for pattern in accepted) for reason in reasons)
    result["skip_policy_status"] = "ACCEPTED" if approved else "UNAPPROVED"
    if not approved:
        result["skip_policy_note"] = "One or more skip reasons are missing or not allowed by tools/test-inventory-policy.json."
    return result


def _as_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value




def discover_test_cases(root: Path, module: str) -> list[tuple[str, str]]:
    """Return (TestCase class, method) pairs using AST without importing the module."""
    module_path = Path(module)
    if not module_path.as_posix().startswith("tools/tests/"):
        module_path = Path("tools/tests") / module_path
    path = root / module_path
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


def _module_command(module: str, filters: list[tuple[str, str]] | None = None) -> list[str]:
    module_path = Path(module)
    if not module_path.as_posix().startswith("tools/tests/"):
        module_path = Path("tools/tests") / module_path
    test_root = module_path.parent
    command = [sys.executable, "-m", "unittest", "discover", "-s", test_root.as_posix(), "-p", module_path.name]
    if filters:
        for class_name, method_name in filters:
            command.extend(["-k", f"{class_name}.{method_name}"])
    command.append("-v")
    return command


def parse_test_counts(output: str, return_code: int | None) -> dict:
    ran = RUN_RE.search(output)
    failed_summary = FAIL_RE.search(output)
    failures = int(FAILURE_COUNT_RE.search(failed_summary.group(1)).group(1)) if failed_summary and FAILURE_COUNT_RE.search(failed_summary.group(1)) else 0
    errors = int(ERROR_COUNT_RE.search(failed_summary.group(1)).group(1)) if failed_summary and ERROR_COUNT_RE.search(failed_summary.group(1)) else 0
    skipped_match = SKIPPED_COUNT_RE.search(failed_summary.group(1)) if failed_summary else None
    if skipped_match:
        skipped = int(skipped_match.group(1))
    else:
        skipped_match = SKIP_RE.search(output)
        skipped = int(skipped_match.group(1)) if skipped_match else 0
    total = int(ran.group(1)) if ran else 0
    passed = max(0, total - failures - errors - skipped)
    skip_details = [{"test": name.strip(), "reason": reason.strip()} for name, reason in SKIP_LINE_RE.findall(output)]
    if total and skipped > len(skip_details):
        skip_details.append({"test": "<skip details unavailable>", "reason": f"unittest reported {skipped} skipped test(s); verbose detail was incomplete"})
    # Timeout is determined by the process supervisor's explicit timed_out flag
    # in run_module/_run_case_batches. Do not infer it from arbitrary output: a
    # regression test may legitimately print a simulated "[TIMEOUT]" log line.
    if ran and return_code == 0 and failures == 0 and errors == 0 and total > 0:
        status = "PASS WITH SKIPS" if skipped else "PASS"
    elif ran and (failures or errors or return_code not in (None, 0)):
        status = "FAIL"
    elif IMPORT_ERROR_RE.search(output) or return_code not in (None, 0):
        status = "ERROR"
    else:
        status = "INCOMPLETE"
    return {
        "tests": total,
        "passed": passed,
        "failed": failures,
        "skipped": skipped,
        "errors": errors,
        "collected": total,
        "deselected": 0,
        "skip_details": skip_details,
        "discovery_status": "DISCOVERED",
        "collection_status": "COLLECTED" if ran else ("FAILED" if status == "ERROR" else "INCOMPLETE"),
        "execution_status": "COMPLETED" if ran else status,
        "status": status,
    }


def _run_case_batches(root: Path, module: str, timeout_seconds: int, group_size: int = 4) -> dict:
    """Run all discovered test methods in deterministic, isolated case batches."""
    cases = discover_test_cases(root, module)
    commands: list[list[str]] = []
    outputs: list[str] = []
    totals = {"tests": 0, "passed": 0, "failed": 0, "skipped": 0, "errors": 0, "collected": 0, "deselected": 0}
    skip_details: list[dict] = []
    elapsed = 0.0
    statuses: list[str] = []
    for offset in range(0, len(cases), group_size):
        group = cases[offset:offset + group_size]
        command = _module_command(module, group)
        commands.append(command)
        started = time.monotonic()
        return_code, output, timed_out = run_isolated_command(command, root, timeout_seconds)
        elapsed += time.monotonic() - started
        counts = parse_test_counts(output, return_code)
        for key in totals:
            totals[key] += counts[key]
        skip_details.extend(counts["skip_details"])
        outputs.append(f"### Batch {len(commands)} — {len(group)} cases; exit={return_code if return_code is not None else 'TIMEOUT'}\n{output}")
        statuses.append("TIMEOUT" if timed_out else counts["status"])
    expected = len(cases)
    actual = totals["tests"]
    if not cases:
        status = "INCOMPLETE"
    elif "TIMEOUT" in statuses:
        status = "TIMEOUT"
    elif "ERROR" in statuses:
        status = "ERROR"
    elif "FAIL" in statuses:
        status = "FAIL"
    elif actual != expected:
        status = "INCOMPLETE"
    elif any(s == "PASS WITH SKIPS" for s in statuses):
        status = "PASS WITH SKIPS"
    else:
        status = "PASS"
    return {
        "module": module, "command": None, "commands": commands,
        "execution_mode": "case-batched", **totals, "skip_details": skip_details,
        "discovery_status": "DISCOVERED", "collection_status": "COLLECTED" if actual else "INCOMPLETE",
        "execution_status": "COMPLETED" if status in {"PASS", "PASS WITH SKIPS", "FAIL"} else status,
        "status": status, "exit_code": 0 if status in {"PASS", "PASS WITH SKIPS"} else 1,
        "duration_seconds": round(elapsed, 3),
        "output_tail": "\n\n".join(outputs)[-12000:],
    }

def run_module(root: Path, module: str, timeout_seconds: int, *, split_large: bool = False, split_threshold: int = 25, group_size: int = 4) -> dict:
    if split_large and len(discover_test_cases(root, module)) > split_threshold:
        return _run_case_batches(root, module, timeout_seconds, group_size=group_size)
    command = _module_command(module)
    started = time.monotonic()
    record = {
        "module": module, "command": command, "status": "ERROR", "exit_code": None,
        "tests": 0, "passed": 0, "failed": 0, "skipped": 0, "errors": 0,
        "collected": 0, "deselected": 0, "skip_details": [],
        "discovery_status": "DISCOVERED", "collection_status": "NOT STARTED", "execution_status": "NOT STARTED",
        "duration_seconds": 0.0, "output_tail": "",
    }
    try:
        return_code, output, timed_out = run_isolated_command(command, root, timeout_seconds)
        counts = parse_test_counts(output + (f"\nTIMEOUT after {timeout_seconds}s" if timed_out else ""), return_code)
        record.update({key: counts[key] for key in (
            "tests", "passed", "failed", "skipped", "errors", "collected", "deselected", "skip_details",
            "discovery_status", "collection_status", "execution_status", "status",
        )})
        record["exit_code"] = return_code
        if timed_out:
            record["status"] = "TIMEOUT"
            record["output_tail"] = output[-12000:] + f"\nTIMEOUT after {timeout_seconds}s\n"
        elif record["status"] in {"FAIL", "ERROR", "INCOMPLETE"}:
            record["output_tail"] = output[-12000:]
    except OSError as exc:
        record["status"] = "ERROR"
        record["discovery_status"] = "DISCOVERED"
        record["collection_status"] = "ERROR"
        record["execution_status"] = "ERROR"
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
    row = result_map.get(module, {})
    status = row.get("status")
    if status == "PASS":
        return False
    if status == "PASS WITH SKIPS" and row.get("skip_policy_status") in {"ACCEPTED", "NOT_APPLICABLE"}:
        return False
    return True


def summary(results: list[dict], total_modules: int | None = None, pending_modules: int = 0) -> dict:
    total = len(results) if total_modules is None else total_modules
    complete = len(results) == total and pending_modules == 0
    terminal_pass = {"PASS", "PASS WITH SKIPS"}
    every_pass = complete and all(
        row["status"] == "PASS" or (row["status"] == "PASS WITH SKIPS" and row.get("skip_policy_status") == "ACCEPTED")
        for row in results
    )
    unapproved_skips = sum(1 for row in results if row.get("status") == "PASS WITH SKIPS" and row.get("skip_policy_status") != "ACCEPTED")
    return {
        "module_count": total,
        "discovered_modules": total,
        "completed_modules": len(results),
        "pending_modules": pending_modules,
        "passed_modules": sum(row["status"] == "PASS" for row in results),
        "passed_with_skips_modules": sum(row["status"] == "PASS WITH SKIPS" for row in results),
        "failed_modules": sum(row["status"] == "FAIL" for row in results),
        "timed_out_modules": sum(row["status"] == "TIMEOUT" for row in results),
        "incomplete_modules": sum(row["status"] == "INCOMPLETE" for row in results),
        "error_modules": sum(row["status"] == "ERROR" for row in results),
        "unapproved_skip_modules": unapproved_skips,
        "discovered_test_cases": sum(row.get("tests", 0) for row in results),
        "total_test_cases": sum(row.get("tests", 0) for row in results),
        "collected_test_cases": sum(row.get("collected", row.get("tests", 0)) for row in results),
        "passed_test_cases": sum(row.get("passed", 0) for row in results),
        "failed_test_cases": sum(row.get("failed", 0) for row in results),
        "skipped_test_cases": sum(row.get("skipped", 0) for row in results),
        "errored_test_cases": sum(row.get("errors", 0) for row in results),
        "deselected_test_cases": sum(row.get("deselected", 0) for row in results),
        "overall_status": "PASS WITH SKIPS" if every_pass and any(row.get("skipped", 0) for row in results) else ("PASS" if every_pass else "INCOMPLETE / FAIL"),
    }

def render_markdown(
    version: str,
    timestamp: str,
    results: list[dict],
    total_modules: int | None = None,
    pending_modules: list[str] | None = None,
    fingerprints: dict | None = None,
) -> str:
    pending_modules = pending_modules or []
    total = len(results) if total_modules is None else total_modules
    stats = summary(results, total, len(pending_modules))
    lines = [
        f"# Sharded Python Test Run — v{version}", "", f"- Timestamp (UTC): {timestamp}",
        f"- Overall: **{stats['overall_status']}**",
        f"- Modules: {stats['passed_modules']} PASS; {stats['passed_with_skips_modules']} PASS WITH SKIPS; "
        f"{stats['failed_modules']} FAIL; {stats['timed_out_modules']} TIMEOUT; {stats['incomplete_modules']} INCOMPLETE; "
        f"{stats['error_modules']} ERROR; {stats['pending_modules']} NOT RUN",
        f"- Test cases: {stats['discovered_test_cases']} collected; {stats['passed_test_cases']} passed; "
        f"{stats['failed_test_cases']} failed; {stats['skipped_test_cases']} skipped; "
        f"{stats['errored_test_cases']} errored; {stats['deselected_test_cases']} deselected", "",
    ]
    if fingerprints:
        lines += ["## Fingerprints", "", f"- Source release: `{fingerprints.get('source_release_fingerprint')}`",
                  f"- Test input: `{fingerprints.get('fingerprint')}`",
                  f"- Environment: `{fingerprints.get('environment_fingerprint')}`", ""]
    lines += ["| Module | Discovery | Collection | Execution | Final | Cases | PASS | FAIL | SKIP | ERR | Exit | Seconds |",
              "|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for row in results:
        exit_code = row.get("exit_code") if row.get("exit_code") is not None else "—"
        lines.append(
            f"| `{row['module']}` | {row.get('discovery_status', '—')} | {row.get('collection_status', '—')} | "
            f"{row.get('execution_status', '—')} | {row['status']} | {row.get('tests', 0)} | {row.get('passed', 0)} | "
            f"{row.get('failed', 0)} | {row.get('skipped', 0)} | {row.get('errors', 0)} | {exit_code} | {row['duration_seconds']:.3f} |"
        )
        if row.get("skip_policy_status") not in (None, "NOT_APPLICABLE"):
            lines.append(f"  - Skip policy: **{row['skip_policy_status']}** {row.get('skip_policy_note', '')}")
        for skipped in row.get("skip_details", []):
            lines.append(f"  - SKIP `{skipped.get('test')}`: {skipped.get('reason')}")
    if pending_modules:
        lines += ["", "## Not yet run", ""]
        lines.extend(f"- `{module}`" for module in pending_modules)
    for row in results:
        if row.get("output_tail"):
            lines += ["", f"## Diagnostic output — {row['module']}", "", "```text", row['output_tail'].rstrip(), "```"]
    lines += ["", "Policy: every dynamically discovered module is accounted for. A module PASS requires exit code 0 and a valid unittest summary with at least one collected case. PASS WITH SKIPS is distinct from PASS. Overall success requires all discovered modules to reach an accepted terminal state; pending modules are never hidden.", ""]
    return "\n".join(lines)

def write_checkpoint(
    report_dir: Path,
    version: str,
    timestamp: str,
    modules: list[str],
    result_map: dict[str, dict],
    fingerprints: dict | None = None,
    execution_config: dict | None = None,
) -> tuple[Path, Path]:
    report_dir.mkdir(parents=True, exist_ok=True)
    results, pending = ordered_results(modules, result_map)
    stats = summary(results, len(modules), len(pending))
    stem = f"PYTHON_TEST_SHARDS_v{version}"
    json_path = report_dir / f"{stem}.json"
    md_path = report_dir / f"{stem}.md"
    payload = {
        "schemaVersion": 2,
        "version": version,
        "timestamp_utc": timestamp,
        "modules": modules,
        "inventory_fingerprint": __import__("hashlib").sha256(json.dumps(modules, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest(),
        "fingerprints": fingerprints or {},
        "execution_config": execution_config or {},
        "summary": stats,
        "results": results,
        "pending_modules": pending,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(version, timestamp, results, len(modules), pending, fingerprints) + "\n", encoding="utf-8")
    return json_path, md_path


def load_checkpoint(path: Path, version: str, modules: list[str], fingerprints: dict | None = None, execution_config: dict | None = None) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("version") != version:
        raise ValueError(f"checkpoint version mismatch: {payload.get('version')} != {version}")
    if payload.get("modules") != modules:
        raise ValueError("checkpoint module inventory differs from the current test inventory")
    if fingerprints is not None:
        saved = payload.get("fingerprints")
        if not saved:
            raise ValueError("checkpoint has no source/environment fingerprints; invalidating legacy checkpoint")
        for key in ("source_release_fingerprint", "fingerprint", "environment_fingerprint", "inventory_fingerprint"):
            if saved.get(key) != fingerprints.get(key):
                raise ValueError(f"checkpoint fingerprint mismatch: {key}")
    if execution_config is not None and payload.get("execution_config") != execution_config:
        raise ValueError("checkpoint execution command/arguments differ from the current run")
    results = payload.get("results", [])
    result_map = {}
    for row in results:
        name = row.get("module")
        if name not in modules or name in result_map:
            raise ValueError(f"invalid or duplicate module in checkpoint: {name!r}")
        if row.get("status") not in {"PASS", "PASS WITH SKIPS", "FAIL", "TIMEOUT", "ERROR", "INCOMPLETE"}:
            raise ValueError(f"invalid terminal status in checkpoint for {name!r}")
        result_map[name] = row
    return result_map


def write_inventory_failure(report_dir: Path, version: str, stage: str, error: BaseException, command: list[str]) -> tuple[Path, Path]:
    """Persist discovery/policy/inventory failures instead of silently aborting."""
    report_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "schemaVersion": 1,
        "version": version,
        "timestamp_utc": timestamp,
        "overall_status": "ERROR",
        "discovery_status": "ERROR" if stage == "discovery" else "NOT RUN",
        "collection_status": "ERROR" if stage == "collection" else "NOT RUN",
        "stage": stage,
        "command": command,
        "error_type": type(error).__name__,
        "error_message": str(error),
        "discovered_modules": 0,
        "test_cases": {"total": 0, "collected": 0, "passed": 0, "failed": 0, "skipped": 0, "errored": 0, "deselected": 0},
    }
    stem = f"PYTHON_TEST_INVENTORY_ERROR_v{version}"
    json_path = report_dir / f"{stem}.json"
    md_path = report_dir / f"{stem}.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(
        f"# Python Test Inventory Failure — v{version}\n\n"
        f"- Status: **ERROR**\n- Stage: `{stage}`\n- Error: `{type(error).__name__}: {error}`\n"
        f"- Discovered modules: 0 (inventory could not be trusted)\n- Test cases: 0; no PASS is claimed\n"
        f"- Command: `{' '.join(command)}`\n",
        encoding="utf-8",
    )
    return json_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--timeout-per-module", type=int, default=180)
    parser.add_argument("--only", action="append", default=[], help="run only this exact test module path; repeatable")
    parser.add_argument("--list", action="store_true", help="list discovered module paths without executing")
    parser.add_argument("--report-dir", type=Path, default=None)
    parser.add_argument("--version", default=None)
    parser.add_argument("--resume", action="store_true", help="resume only from a source/environment/command-compatible checkpoint")
    parser.add_argument("--split-large-modules", action="store_true", help="legacy diagnostic mode; not recommended for full-module regression semantics")
    args = parser.parse_args()

    root = args.root.resolve()
    report_dir = args.report_dir.resolve() if args.report_dir else root / "logs" / "test-shards"
    preliminary_version = args.version or "unknown"
    manifest_path = root / "data/manifest.json"
    if preliminary_version == "unknown" and manifest_path.is_file():
        try:
            preliminary_version = json.loads(manifest_path.read_text(encoding="utf-8")).get("version", "unknown")
        except (OSError, json.JSONDecodeError):
            pass
    try:
        modules = discover_modules(root)
        policy = load_test_policy(root)
        inventory_delta = compare_inventory_to_baseline(root, modules)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        write_inventory_failure(report_dir, preliminary_version, "discovery", exc, sys.argv)
        print(f"TEST INVENTORY ERROR: {type(exc).__name__}: {exc}", flush=True)
        return 1
    print("TEST INVENTORY: " + json.dumps(inventory_delta, ensure_ascii=False, sort_keys=True), flush=True)
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

    try:
        manifest = json.loads((root / "data/manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        write_inventory_failure(report_dir, preliminary_version, "collection", exc, sys.argv)
        print(f"TEST MANIFEST ERROR: {type(exc).__name__}: {exc}", flush=True)
        return 1
    version = args.version or manifest.get("version", "unknown")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    execution_config = build_execution_config(
        args.timeout_per_module, selected, args.split_large_modules, inventory_delta
    )
    fingerprints = test_input_fingerprint(root, modules, execution_config)
    fingerprints["inventory_fingerprint"] = __import__("hashlib").sha256(
        json.dumps(modules, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    fingerprints["inventory_delta"] = inventory_delta
    stem = f"PYTHON_TEST_SHARDS_v{version}"
    checkpoint_path = report_dir / f"{stem}.json"
    result_map: dict[str, dict] = {}
    if args.resume and checkpoint_path.exists():
        try:
            result_map = load_checkpoint(checkpoint_path, version, modules, fingerprints, execution_config)
            print(f"RESUME: retained {sum(row['status'] in {'PASS', 'PASS WITH SKIPS'} for row in result_map.values())} compatible completed module result(s)")
        except (ValueError, OSError, json.JSONDecodeError) as exc:
            print(f"RESUME INVALIDATED: {exc}; all modules in the selected run will be rerun")
            result_map = {}
    write_checkpoint(report_dir, version, timestamp, modules, result_map, fingerprints, execution_config)

    for module in selected:
        if args.resume and not should_run_module(module, result_map):
            continue
        result = run_module(root, module, max(1, args.timeout_per_module), split_large=args.split_large_modules)
        result = apply_skip_policy(result, policy)
        result_map[module] = result
        print(
            f"[{result['status']}] {module}: {result['tests']} cases "
            f"({result.get('passed', 0)} passed, {result.get('failed', 0)} failed, "
            f"{result.get('skipped', 0)} skipped, {result.get('errors', 0)} errors), "
            f"{result['duration_seconds']:.2f}s",
            flush=True,
        )
        write_checkpoint(report_dir, version, timestamp, modules, result_map, fingerprints, execution_config)

    results, pending = ordered_results(modules, result_map)
    stats = summary(results, len(modules), len(pending))
    print(
        f"SUMMARY: {stats['passed_modules']} PASS + {stats['passed_with_skips_modules']} PASS WITH SKIPS / {stats['module_count']} modules; "
        f"{stats['passed_test_cases']} passed, {stats['failed_test_cases']} failed, {stats['skipped_test_cases']} skipped, "
        f"{stats['errored_test_cases']} errored; {stats['timed_out_modules']} timeout(s); "
        f"{stats['error_modules']} error(s); {stats['unapproved_skip_modules']} unapproved-skip module(s); {stats['pending_modules']} NOT RUN",
        flush=True,
    )
    return 0 if stats["overall_status"] in {"PASS", "PASS WITH SKIPS"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
