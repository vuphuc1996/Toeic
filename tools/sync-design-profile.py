#!/usr/bin/env python3
"""Synchronize the design profile and legacy typography floor into design-system.css.

Usage:
  python tools/sync-design-profile.py --check
  python tools/sync-design-profile.py --apply

The JSON profile owns design tokens. A generated selector block catches legacy
app.css rules with fixed text sizes below the profile's caption floor. If a new
feature adds microtext, CI detects drift until the shared floor is regenerated.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "design" / "design-profile.json"
APP_CSS = ROOT / "assets" / "css" / "app.css"
CSS = ROOT / "assets" / "css" / "design-system.css"
START = "/* DESIGN_PROFILE_TOKENS:BEGIN */"
END = "/* DESIGN_PROFILE_TOKENS:END */"
FLOOR_START = "/* DESIGN_LEGACY_FONT_FLOOR:BEGIN */"
FLOOR_END = "/* DESIGN_LEGACY_FONT_FLOOR:END */"


def expected_block(profile: dict) -> str:
    variables = profile.get("cssVariables")
    if not isinstance(variables, dict) or not variables:
        raise ValueError("cssVariables must be a non-empty object")
    lines = [START, ":root {"]
    for name, value in variables.items():
        if not re.fullmatch(r"--ds-[a-z0-9-]+", name):
            raise ValueError(f"invalid design token name: {name}")
        if not isinstance(value, str) or any(char in value for char in "{};") or "\n" in value:
            raise ValueError(f"invalid CSS token value for {name}")
        lines.append(f"  {name}: {value};")
    lines.extend(["}", END])
    return "\n".join(lines)


def expected_legacy_floor(profile: dict) -> tuple[str, int]:
    caption = profile.get("cssVariables", {}).get("--ds-font-caption", "12.5px")
    m = re.fullmatch(r"\s*([0-9.]+)px\s*", caption)
    if not m:
        raise ValueError("--ds-font-caption must be a fixed px value to audit legacy floors")
    floor_px = float(m.group(1))

    # Include feature styles and the legacy pre-profile section of design-system.css.
    # Only scan the prefix before generated/shared rules to avoid self-reference.
    css_text = CSS.read_text(encoding="utf-8")
    legacy_prefix = css_text.split(START, 1)[0]
    sources = [APP_CSS.read_text(encoding="utf-8"), legacy_prefix]
    rule_pattern = re.compile(r"(?P<selector>[^{}]+)\{(?P<body>[^{}]*)\}", re.S)
    font_pattern = re.compile(r"font-size\s*:\s*([0-9.]+)\s*(px|rem)\b", re.I)
    selectors: set[str] = set()
    for source in sources:
        source = re.sub(r"/\*[\s\S]*?\*/", "", source)
        for rule in rule_pattern.finditer(source):
            selector = rule.group("selector").strip()
            if not selector or selector.startswith("@"):
                continue
            for declaration in font_pattern.finditer(rule.group("body")):
                value = float(declaration.group(1))
                unit = declaration.group(2).lower()
                value_px = value * (16 if unit == "rem" else 1)
                if value_px < floor_px:
                    selectors.add(selector)
                    break

    ordered = sorted(selectors)
    lines = [
        FLOOR_START,
        "/* Generated from fixed sub-caption font rules in app.css. Do not hand-edit. */",
        "body :where(",
    ]
    for index, selector in enumerate(ordered):
        suffix = "," if index < len(ordered) - 1 else ""
        lines.append(f"  {selector}{suffix}")
    lines.extend([
        ") {",
        "  font-size: var(--ds-font-caption) !important;",
        "  line-height: var(--ds-line-caption);",
        "}",
        FLOOR_END,
    ])
    return "\n".join(lines), len(ordered)


def replace_region(css: str, start: str, end: str, expected: str) -> str:
    if css.count(start) != 1 or css.count(end) != 1:
        raise SystemExit(f"ERROR: {start}/{end} markers must each appear exactly once")
    pattern = re.compile(re.escape(start) + r"[\s\S]*?" + re.escape(end))
    current = pattern.search(css)
    if not current:
        raise SystemExit(f"ERROR: generated block was not found: {start}")
    return css[:current.start()] + expected + css[current.end():]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    expected_tokens = expected_block(profile)
    expected_floor, selector_count = expected_legacy_floor(profile)
    css = CSS.read_text(encoding="utf-8")

    token_pattern = re.compile(re.escape(START) + r"[\s\S]*?" + re.escape(END))
    floor_pattern = re.compile(re.escape(FLOOR_START) + r"[\s\S]*?" + re.escape(FLOOR_END))
    token_match = token_pattern.search(css)
    floor_match = floor_pattern.search(css)
    if not token_match or not floor_match:
        raise SystemExit("ERROR: generated design profile/floor region is missing")

    if args.check:
        failures = []
        if token_match.group(0) != expected_tokens:
            failures.append("design tokens")
        if floor_match.group(0) != expected_floor:
            failures.append("legacy font-floor selectors")
        if failures:
            print("DESIGN PROFILE OUT OF SYNC (" + ", ".join(failures) + "): run python tools/sync-design-profile.py --apply")
            return 1
        print(f"DESIGN PROFILE PASS — {len(profile['cssVariables'])} tokens and {selector_count} legacy font-floor selector groups synchronized")
        return 0

    updated = replace_region(css, START, END, expected_tokens)
    updated = replace_region(updated, FLOOR_START, FLOOR_END, expected_floor)
    CSS.write_text(updated, encoding="utf-8")
    print(f"Updated {CSS.relative_to(ROOT)}: {len(profile['cssVariables'])} tokens, {selector_count} legacy font-floor selector groups")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
