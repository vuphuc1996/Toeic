#!/usr/bin/env python3
"""Ratchet audit for CSS design-token drift; legacy findings warn, new findings fail."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

BASELINE_REL = Path("tools/design-token-baseline.json")
RULES_REL = Path("tools/design-token-rules.json")
PROFILE_REL = Path("design/design-profile.json")
HEX_RE = re.compile(r"#(?:[0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})\b", re.I)
MEDIA_WIDTH_RE = re.compile(r"\b(min|max)-width\s*:\s*([0-9]+(?:\.[0-9]+)?)(px|rem|em)\b", re.I)
VAR_RE = re.compile(r"var\(\s*(--[a-z0-9_-]+)", re.I)


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_comments(css: str) -> str:
    return re.sub(r"/\*.*?\*/", lambda match: "\n" * match.group(0).count("\n"), css, flags=re.S)


def find_matching_brace(source: str, start: int) -> int:
    depth = 0
    quote: str | None = None
    escaped = False
    for index in range(start, len(source)):
        char = source[index]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in ("'", '"'):
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    raise ValueError("CSS có block ngoặc nhọn chưa đóng")


def find_next_open_brace(source: str, start: int) -> int:
    quote: str | None = None
    escaped = False
    paren_depth = 0
    for index in range(start, len(source)):
        char = source[index]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in ("'", '"'):
            quote = char
        elif char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth = max(0, paren_depth - 1)
        elif char == "{" and paren_depth == 0:
            return index
    return -1


def split_top_level(source: str, delimiter: str) -> list[str]:
    parts: list[str] = []
    start = 0
    paren_depth = 0
    quote: str | None = None
    escaped = False
    for index, char in enumerate(source):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in ("'", '"'):
            quote = char
        elif char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth = max(0, paren_depth - 1)
        elif char == delimiter and paren_depth == 0:
            parts.append(source[start:index])
            start = index + 1
    parts.append(source[start:])
    return parts


def parse_declarations(body: str) -> list[tuple[str, str]]:
    declarations: list[tuple[str, str]] = []
    # A normal selector block should contain declarations only. Ignore nested CSS rules
    # rather than misreading a nested selector as a declaration.
    for fragment in split_top_level(body, ";"):
        if "{" in fragment or "}" in fragment:
            continue
        if ":" not in fragment:
            continue
        prop, value = fragment.split(":", 1)
        prop = prop.strip().lower()
        value = value.strip()
        if prop and value:
            declarations.append((prop, value))
    return declarations


def walk_css(source: str, contexts: tuple[str, ...] = ()) -> tuple[list[tuple[str, str, str]], list[tuple[str, str]]]:
    """Return (selector/context/declaration tuples, media header tuples)."""
    declarations: list[tuple[str, str, str]] = []
    media_headers: list[tuple[str, str]] = []
    cursor = 0
    source = strip_comments(source)
    while cursor < len(source):
        opening = find_next_open_brace(source, cursor)
        if opening < 0:
            break
        header = source[cursor:opening].strip()
        closing = find_matching_brace(source, opening)
        body = source[opening + 1:closing]
        if not header:
            cursor = closing + 1
            continue
        if header.lower().startswith("@media"):
            media_headers.append((" | ".join((*contexts, header)), header))
            nested_decls, nested_media = walk_css(body, (*contexts, header))
            declarations.extend(nested_decls)
            media_headers.extend(nested_media)
        elif header.lower().startswith(("@supports", "@container", "@layer", "@document", "@keyframes", "@-webkit-keyframes")):
            nested_decls, nested_media = walk_css(body, (*contexts, header))
            declarations.extend(nested_decls)
            media_headers.extend(nested_media)
        elif header.startswith("@"):
            # @font-face and similar at-rules can hold declarations but are not UI selectors.
            for prop, value in parse_declarations(body):
                declarations.append((" | ".join((*contexts, header)), prop, value))
        else:
            selector = " ".join(header.split())
            scoped_selector = " | ".join((*contexts, selector)) if contexts else selector
            for prop, value in parse_declarations(body):
                declarations.append((scoped_selector, prop, value))
            # Handle CSS nesting conservatively; nested blocks are parsed as their own rules.
            if "{" in body:
                nested_decls, nested_media = walk_css(body, (*contexts, selector))
                declarations.extend(nested_decls)
                media_headers.extend(nested_media)
        cursor = closing + 1
    return declarations, media_headers


def normalise_hex(value: str) -> str:
    value = value.lower()
    if len(value) == 4:  # #rgb -> #rrggbb
        return "#" + "".join(char * 2 for char in value[1:])
    if len(value) == 5:  # #rgba -> #rrggbbaa
        return "#" + "".join(char * 2 for char in value[1:])
    return value


def has_allowed_var(value: str, prefixes: Iterable[str]) -> bool:
    return any(name.startswith(tuple(prefixes)) for name in VAR_RE.findall(value))


def violation(rule: str, file: str, selector: str, prop: str, value: str) -> dict[str, str]:
    return {"rule": rule, "file": file, "selector": selector, "property": prop, "value": value.strip()}


def collect_audit(root: Path, rules: dict[str, Any]) -> tuple[list[dict[str, str]], dict[str, Any]]:
    profile_path = root / PROFILE_REL
    profile = json.loads(profile_path.read_text(encoding="utf-8")) if profile_path.exists() else {"cssVariables": {}}
    canonical_colours = {
        name: normalise_hex(str(value))
        for name, value in profile.get("cssVariables", {}).items()
        if name.startswith(rules["color"]["canonicalTokenPrefix"]) and isinstance(value, str) and HEX_RE.fullmatch(value.strip())
    }
    findings: list[dict[str, str]] = []
    metrics: dict[str, Any] = {
        "hexOccurrences": 0, "hexUnique": 0,
        "fontSizeDeclarations": 0, "fontSizeUnique": 0,
        "fontWeightDeclarations": 0, "fontWeightUnique": 0,
        "borderRadiusDeclarations": 0, "borderRadiusUnique": 0,
        "boxShadowDeclarations": 0, "boxShadowUnique": 0,
        "importantOccurrences": 0, "breakpointOccurrences": 0,
        "breakpointUniqueValues": 0, "keyframes": 0,
    }
    all_hex_raw: list[str] = []
    unique_values: dict[str, set[str]] = defaultdict(set)

    for rel in rules["scanFiles"]:
        path = root / rel
        if not path.exists():
            raise FileNotFoundError(f"Thiếu CSS audit target: {rel}")
        source = path.read_text(encoding="utf-8")
        clean = strip_comments(source)
        declarations, media_headers = walk_css(source)
        media_widths: list[tuple[str, str, str]] = []
        for scoped_header, header in media_headers:
            for direction, number, unit in MEDIA_WIDTH_RE.findall(header):
                px = float(number) * (16 if unit.lower() in {"rem", "em"} else 1)
                value = f"{number}{unit}"
                metrics["breakpointOccurrences"] += 1
                unique_values["breakpoint"].add(value)
                if px not in rules["breakpoints"]["allowedBoundaryPx"]:
                    prop = f"{direction.lower()}-width"
                    findings.append(violation("BREAKPOINT", rel, scoped_header, prop, value))

        metrics["keyframes"] += len(re.findall(r"@(?:-webkit-)?keyframes\s+[\w-]+", clean, re.I))
        for selector, prop, raw_value in declarations:
            value = re.sub(r"\s*!important\s*$", "", raw_value, flags=re.I).strip()
            is_custom_prop = prop.startswith("--")
            if prop == "font-size":
                metrics["fontSizeDeclarations"] += 1
                unique_values["fontSize"].add(raw_value.strip())
                prefixes = rules["fontSize"]["tokenPrefixes"]
                if value.lower() not in rules["fontSize"]["allowKeywords"] and not has_allowed_var(value, prefixes):
                    findings.append(violation("FONT-SIZE", rel, selector, prop, value))
            elif prop == "font-weight":
                metrics["fontWeightDeclarations"] += 1
                unique_values["fontWeight"].add(raw_value.strip())
                allowed = {str(item) for item in rules["fontWeight"]["allowed"]}
                if value.lower() not in rules["fontWeight"]["allowKeywords"] and value not in allowed and not has_allowed_var(value, rules["fontWeight"]["tokenPrefixes"]):
                    findings.append(violation("FONT-WEIGHT", rel, selector, prop, value))
            elif prop == "border-radius":
                metrics["borderRadiusDeclarations"] += 1
                unique_values["borderRadius"].add(raw_value.strip())
                atoms = [part.strip().lower() for part in value.split()]
                allowed = set(rules["borderRadius"]["allowedAtoms"])
                allowed_value = value.lower() in rules["borderRadius"]["allowKeywords"] or (bool(atoms) and all(atom in allowed for atom in atoms)) or has_allowed_var(value, rules["borderRadius"]["tokenPrefixes"])
                if not allowed_value:
                    findings.append(violation("BORDER-RADIUS", rel, selector, prop, value))
            elif prop == "box-shadow":
                metrics["boxShadowDeclarations"] += 1
                unique_values["boxShadow"].add(raw_value.strip())
                allowed_value = value.lower() in rules["boxShadow"]["allowKeywords"] or has_allowed_var(value, rules["boxShadow"]["tokenPrefixes"])
                if not allowed_value:
                    findings.append(violation("BOX-SHADOW", rel, selector, prop, value))

            if "!important" in raw_value.lower():
                metrics["importantOccurrences"] += 1
                findings.append(violation("IMPORTANT", rel, selector, prop, raw_value.strip()))

            for hex_value in HEX_RE.findall(raw_value):
                metrics["hexOccurrences"] += 1
                all_hex_raw.append(hex_value.lower())
                if is_custom_prop and prop in canonical_colours and normalise_hex(hex_value) == canonical_colours[prop]:
                    continue
                findings.append(violation("HEX-COLOR", rel, selector, prop, hex_value))

    metrics["hexUnique"] = len(set(all_hex_raw))
    metrics["fontSizeUnique"] = len(unique_values["fontSize"])
    metrics["fontWeightUnique"] = len(unique_values["fontWeight"])
    metrics["borderRadiusUnique"] = len(unique_values["borderRadius"])
    metrics["boxShadowUnique"] = len(unique_values["boxShadow"])
    metrics["breakpointUniqueValues"] = len(unique_values["breakpoint"])
    metrics["importantBaselineFindings"] = sum(1 for item in findings if item["rule"] == "IMPORTANT")
    return findings, metrics


def identity(item: dict[str, str]) -> tuple[str, str, str, str]:
    return item["rule"], item["file"], item["selector"], item["property"]


def grouped_findings(findings: list[dict[str, str]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], set[str]] = defaultdict(set)
    counts: Counter[tuple[str, str, str, str]] = Counter()
    for item in findings:
        key = identity(item)
        grouped[key].add(item["value"])
        counts[key] += 1
    return [
        {"rule": key[0], "file": key[1], "selector": key[2], "property": key[3], "values": sorted(grouped[key]), "occurrences": counts[key]}
        for key in sorted(grouped)
    ]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def audit_project(root: Path, baseline_path: Path | None = None, rules_path: Path | None = None) -> dict[str, Any]:
    baseline_path = baseline_path or root / BASELINE_REL
    rules_path = rules_path or root / RULES_REL
    rules = load_json(rules_path)
    rules_hash = sha256_file(rules_path)
    baseline = load_json(baseline_path)
    drift = baseline.get("rulesSha256") != rules_hash
    findings, metrics = collect_audit(root, rules)
    current_groups = grouped_findings(findings)
    baseline_groups = baseline.get("violations", [])
    baseline_map = {identity(item): item for item in baseline_groups}
    current_map = {identity(item): item for item in current_groups}
    new: list[dict[str, Any]] = []
    legacy: list[dict[str, Any]] = []
    resolved: list[dict[str, Any]] = []
    for key, item in current_map.items():
        known = baseline_map.get(key)
        if known is None:
            new.append(item)
            continue
        known_values = set(known.get("values", []))
        current_values = set(item.get("values", []))
        if not current_values.issubset(known_values) or item.get("occurrences", 0) > known.get("occurrences", 0):
            new.append(item)
        else:
            legacy.append(item)
    for key, item in baseline_map.items():
        if key not in current_map:
            resolved.append(item)
    return {
        "ok": not drift and not new,
        "ruleDrift": drift,
        "rulesSha256": rules_hash,
        "metrics": metrics,
        "legacy": legacy,
        "new": new,
        "resolved": resolved,
        "current": current_groups,
        "baselineCount": len(baseline_groups),
    }


def bootstrap_baseline(root: Path, baseline_path: Path | None = None, rules_path: Path | None = None) -> None:
    baseline_path = baseline_path or root / BASELINE_REL
    rules_path = rules_path or root / RULES_REL
    if baseline_path.exists():
        raise FileExistsError(f"Không ghi đè baseline đã tồn tại: {baseline_path}")
    rules = load_json(rules_path)
    findings, metrics = collect_audit(root, rules)
    baseline = {
        "schemaVersion": 1,
        "rulesetVersion": rules["rulesetVersion"],
        "baselineSource": "TOEIC_Dictionary_v2.95.10",
        "rulesSha256": sha256_file(rules_path),
        "identity": ["rule", "file", "selector", "property"],
        "metricsAtBaseline": metrics,
        "violations": grouped_findings(findings),
    }
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    baseline_path.write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--bootstrap-baseline", action="store_true", help="Tạo baseline lần đầu; từ đó trở đi tool không ghi baseline")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        baseline_path = root / BASELINE_REL
        rules_path = root / RULES_REL
        if args.bootstrap_baseline:
            bootstrap_baseline(root, baseline_path, rules_path)
            print(f"BASELINE BOOTSTRAP PASS — {baseline_path.relative_to(root)}")
            return 0
        result = audit_project(root, baseline_path, rules_path)
        m = result["metrics"]
        print("DESIGN TOKEN AUDIT — v1.0.0")
        print(f"CSS metrics: hex {m['hexUnique']} unique/{m['hexOccurrences']} occurrences; font-size {m['fontSizeUnique']} unique/{m['fontSizeDeclarations']} declarations; font-weight {m['fontWeightUnique']} unique/{m['fontWeightDeclarations']} declarations; border-radius {m['borderRadiusUnique']} unique/{m['borderRadiusDeclarations']} declarations; box-shadow {m['boxShadowUnique']} unique/{m['boxShadowDeclarations']} declarations; breakpoints {m['breakpointUniqueValues']} unique/{m['breakpointOccurrences']} occurrences; !important {m['importantOccurrences']}; @keyframes {m['keyframes']}")
        print(f"Baseline findings: {result['baselineCount']} identities; current legacy: {len(result['legacy'])}; resolved since baseline: {len(result['resolved'])}")
        print(f"New violations: {len(result['new'])}")
        if result["ruleDrift"]:
            print("ERROR RULE-DRIFT: design-token-rules.json changed after baseline creation; do not loosen policy or rewrite baseline automatically.")
        for item in result["new"][:80]:
            print(f"ERROR {item['rule']} {item['file']} :: {item['selector']} :: {item['property']} = {', '.join(item['values'])}")
        if len(result["new"]) > 80:
            print(f"... {len(result['new']) - 80} additional new findings omitted")
        print(f"Legacy findings are WARNING only: {len(result['legacy'])}")
        return 0 if result["ok"] else 1
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
