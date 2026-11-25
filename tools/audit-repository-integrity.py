#!/usr/bin/env python3
"""Fail-fast local reference audit for assets, PWA cache lists and GitHub Actions.

This is a structural preflight, not a substitute for browser/production QA.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []
CHECKED = 0


def record_path(raw: str, base: Path, label: str, *, directory: bool = False, optional: bool = False) -> None:
    global CHECKED
    value = raw.strip().strip("\"'")
    if not value or value.startswith(("#", "http://", "https://", "data:", "blob:", "mailto:", "tel:", "javascript:")):
        return
    value = value.split("#", 1)[0].split("?", 1)[0]
    if not value:
        return
    target = (base / value).resolve()
    CHECKED += 1
    exists = target.is_dir() if directory or value.endswith("/") else target.is_file()
    if not exists:
        message = f"{label}: missing local reference {raw!r} -> {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}"
        (WARNINGS if optional else ERRORS).append(message)


def parse_js_array(source: str, name: str) -> list[str]:
    match = re.search(rf"const\s+{re.escape(name)}\s*=\s*(\[.*?\]);", source, re.S)
    if not match:
        ERRORS.append(f"sw.js: cannot locate {name} asset array")
        return []
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as error:
        ERRORS.append(f"sw.js: {name} is not valid JSON-compatible array: {error}")
        return []




def configured_unittest_patterns(workflow: str) -> list[str]:
    """Return explicit unittest patterns plus Python's default discovery pattern.

    `python -m unittest discover` defaults to `test*.py`; ignoring that default
    caused the integrity audit to report modules that the final full-suite step
    already discovered and executed.
    """
    patterns: list[str] = []
    for line in workflow.splitlines():
        if "python -m unittest discover" not in line:
            continue
        matches = re.findall(r"(?:^|\s)-p\s+['\"]([^'\"]+)['\"]", line)
        if matches:
            patterns.extend(matches)
        else:
            patterns.append("test*.py")
    return patterns


def main() -> int:
    global CHECKED
    sw_path = ROOT / "sw.js"
    workflow_path = ROOT / ".github/workflows/validate-data.yml"
    html_path = ROOT / "index.html"
    css_path = ROOT / "assets/css/app.css"
    for path in (sw_path, workflow_path, html_path, css_path):
        if not path.is_file():
            ERRORS.append(f"Required repository control file is missing: {path.relative_to(ROOT)}")

    if sw_path.is_file():
        sw = sw_path.read_text(encoding="utf-8")
        required = parse_js_array(sw, "REQUIRED")
        app_shell = parse_js_array(sw, "APP_SHELL")
        optional = parse_js_array(sw, "OPTIONAL")
        for path in required:
            record_path(path, ROOT, "sw.js REQUIRED", directory=path in ("./",), optional=False)
        for path in app_shell:
            record_path(path, ROOT, "sw.js APP_SHELL", directory=path in ("./",), optional=False)
        for path in optional:
            record_path(path, ROOT, "sw.js OPTIONAL", directory=path.endswith("/"), optional=True)
        for path in set(required) - set(app_shell):
            ERRORS.append(f"sw.js: REQUIRED asset is not in APP_SHELL: {path}")

    # HTML local href/src references. Anchors, remote URLs and data URIs are not local files.
    if html_path.is_file():
        html = html_path.read_text(encoding="utf-8")
        for attr, _quote, value in re.findall(r"\b(href|src|poster)\s*=\s*([\"'])(.*?)\2", html, re.I):
            record_path(value, ROOT, f"index.html {attr}")

    # CSS url(...) paths are relative to the stylesheet, not the repository root.
    for path in (ROOT / "assets/css").glob("*.css"):
        css = path.read_text(encoding="utf-8")
        for value in re.findall(r"url\(\s*(['\"]?)(.*?)\1\s*\)", css, re.I):
            record_path(value[1], path.parent, f"{path.relative_to(ROOT)} url()")

    # Static ES-module imports and literal runtime data URL references.
    for path in (ROOT / "assets/js").glob("*.js"):
        source = path.read_text(encoding="utf-8")
        for value in re.findall(r"\bfrom\s*['\"](\.{1,2}/[^'\"]+)['\"]|\bimport\s*['\"](\.{1,2}/[^'\"]+)['\"]", source):
            relative = value[0] or value[1]
            record_path(relative, path.parent, f"{path.relative_to(ROOT)} import")
        for value in re.findall(r"releaseDataUrl\(\s*['\"](\./[^'\"]+)['\"]\s*\)", source):
            record_path(value, ROOT, f"{path.relative_to(ROOT)} releaseDataUrl")

    # CI scripts/test patterns must resolve before the test runner starts.
    if workflow_path.is_file():
        workflow = workflow_path.read_text(encoding="utf-8")
        explicit_paths = set(re.findall(r"(?<![\w./-])((?:tools|assets|data)/[\w./-]+\.(?:py|mjs|js))\b", workflow))
        for value in sorted(explicit_paths):
            record_path(value, ROOT, "GitHub Actions command")
        patterns = configured_unittest_patterns(workflow)
        test_files = list((ROOT / "tools/tests").rglob("test_*.py"))
        for test in test_files:
            relative = test.relative_to(ROOT).as_posix()
            if not any(test.match(pattern) for pattern in patterns):
                ERRORS.append(f"GitHub Actions: Python test is not selected by any unittest pattern: {relative}")
        for test in (ROOT / "tools/tests").glob("*.mjs"):
            relative = test.relative_to(ROOT).as_posix()
            if relative not in workflow:
                ERRORS.append(f"GitHub Actions: Node regression suite is not invoked: {relative}")

    # Validate every shipped JSON data file, so malformed content cannot be overlooked after a change.
    json_files = list((ROOT / "data").rglob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
            CHECKED += 1
        except Exception as error:  # noqa: BLE001 - report malformed repository input with path.
            ERRORS.append(f"Invalid JSON: {path.relative_to(ROOT)}: {error}")

    print(f"Repository integrity preflight: {CHECKED} local references/data files inspected")
    print(f"Errors: {len(ERRORS)} | Optional warnings: {len(WARNINGS)}")
    for item in ERRORS:
        print(f"ERROR: {item}")
    for item in WARNINGS:
        print(f"WARNING: {item}")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
