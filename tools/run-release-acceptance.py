#!/usr/bin/env python3
"""Run a reproducible release acceptance sequence with per-command timeout/logging.

This runner does not mutate learning content. Audit scripts may refresh their own
report outputs, as they do when invoked directly.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parents[1]
SHARDER_PATH = ROOT / "tools/run-python-tests-sharded.py"
_SHARDER_SPEC = importlib.util.spec_from_file_location("release_acceptance_sharder", SHARDER_PATH)
if _SHARDER_SPEC is None or _SHARDER_SPEC.loader is None:
    raise RuntimeError(f"cannot load Python test sharder: {SHARDER_PATH}")
SHARDER = importlib.util.module_from_spec(_SHARDER_SPEC)
_SHARDER_SPEC.loader.exec_module(SHARDER)
COMMANDS = [
    ("repository_integrity", [sys.executable, "tools/audit-repository-integrity.py"]),
    ("data_validator", [sys.executable, "tools/validate-data.py"]),
    ("learning_content_validator", [sys.executable, "tools/validate-learning-content.py"]),
    ("version_sync", [sys.executable, "tools/sync-version.py", "--check"]),
    ("listening_readiness", [sys.executable, "tools/audit-listening-readiness.py"]),
    ("question_evidence", [sys.executable, "tools/audit-question-evidence.py"]),
    ("distractor_audit", [sys.executable, "tools/audit-distractors.py"]),
    ("learning_outcomes", [sys.executable, "tools/audit-learning-outcomes.py"]),
    ("major_release_audit", [sys.executable, "tools/audit-major-release.py"]),
    ("related_glossary_backlog", [sys.executable, "tools/build-related-glossary-backlog.py"]),
    ("editorial_review_queue", [sys.executable, "tools/build-editorial-review-queue.py"]),
    ("full_python_suite", [sys.executable, "tools/run-python-tests-sharded.py", "--timeout-per-module", "180", "--resume"]),
]


def format_command(command: list[str]) -> str:
    return " ".join(command)


def resolve_version(root: Path, requested: str | None = None) -> str:
    """Use the explicit version or the repository manifest; never a stale default."""
    if requested:
        return requested
    manifest = json.loads((root / "data/manifest.json").read_text(encoding="utf-8"))
    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError(f"invalid data/manifest.json version: {version!r}")
    return version



def run_commands(root: Path, timeout_seconds: int, dry_run: bool = False) -> list[dict]:
    results = []
    for name, command in COMMANDS:
        record = {"name": name, "command": format_command(command), "status": "NOT_RUN", "exit_code": None, "duration_seconds": 0.0, "output": ""}
        if dry_run:
            results.append(record)
            continue
        start = time.monotonic()
        try:
            return_code, output, timed_out = SHARDER.run_isolated_command(
                command, root, timeout_seconds
            )
            record["exit_code"] = return_code
            record["output"] = output
            if timed_out:
                record["output"] = output + f"\nTIMEOUT after {timeout_seconds}s; process group terminated\n"
                record["status"] = "TIMEOUT"
            else:
                record["status"] = "PASS" if return_code == 0 else "FAIL"
        except OSError as exc:
            record["output"] = f"{type(exc).__name__}: {exc}"
            record["status"] = "ERROR"
        record["duration_seconds"] = round(time.monotonic() - start, 3)
        results.append(record)
        if record["status"] != "PASS":
            break
    return results


def render_markdown(results: list[dict], version: str, timestamp: str) -> str:
    all_pass = bool(results) and all(item["status"] == "PASS" for item in results)
    lines = [f"# Release Acceptance Run — v{version}", "", f"- Timestamp (UTC): {timestamp}",
             f"- Overall status: **{'PASS' if all_pass else 'INCOMPLETE / FAIL'}**", "",
             "| Check | Status | Exit | Duration (s) |", "|---|---|---:|---:|"]
    for item in results:
        lines.append(f"| {item['name']} | {item['status']} | {item['exit_code'] if item['exit_code'] is not None else '—'} | {item['duration_seconds']:.3f} |")
    lines += ["", "## Commands", ""]
    for item in results:
        lines += [f"### {item['name']}", "", f"`{item['command']}`", "", f"Status: **{item['status']}**", ""]
        if item.get("output"):
            lines += ["```text", item["output"].rstrip(), "```", ""]
    lines += ["", "Full suite is PASS only if the runner reaches it and returns exit code 0. A timeout is never converted to PASS.", ""]
    return "\n".join(lines)



def write_reports(report_dir: Path, results: list[dict], version: str, timestamp: str) -> tuple[Path, Path]:
    """Persist JSON and Markdown reports using the resolved version consistently."""
    report_dir.mkdir(parents=True, exist_ok=True)
    stem = f"RELEASE_ACCEPTANCE_v{version}"
    json_path = report_dir / f"{stem}.json"
    md_path = report_dir / f"{stem}.md"
    json_path.write_text(
        json.dumps({"version": version, "timestamp_utc": timestamp, "results": results}, indent=2) + "\n",
        encoding="utf-8",
    )
    md_path.write_text(render_markdown(results, version, timestamp) + "\n", encoding="utf-8")
    return json_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--timeout", type=int, default=1800, help="timeout in seconds for each acceptance command (default: 1800)")
    parser.add_argument("--dry-run", action="store_true", help="list acceptance commands without executing")
    parser.add_argument("--report-dir", type=Path, default=None)
    parser.add_argument("--version", default=None, help="report version (defaults to data/manifest.json)")
    args = parser.parse_args()
    root = args.root.resolve()
    version = resolve_version(root, args.version)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    results = run_commands(root, max(1, args.timeout), args.dry_run)
    if not args.dry_run:
        report_dir = args.report_dir if args.report_dir is not None else root / "logs/release-acceptance"
        write_reports(report_dir, results, version, stamp)
    for result in results:
        print(f"[{result['status']}] {result['name']}: {result['command']}")
    if args.dry_run:
        return 0
    return 0 if results and all(r["status"] == "PASS" for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
