#!/usr/bin/env python3
"""Generate the reconciled 33-criterion question-level learning-outcome report."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load_json(root: Path, rel: str) -> Any:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def count_questions_for_objective(root: Path, obj_map: dict[str, Any]) -> tuple[int, int, str]:
    data = load_json(root, obj_map["resourceFile"])
    items = data.get(obj_map["resourceCollection"], [])
    by_id = {item.get("id"): item for item in items if isinstance(item, dict)}
    rids = obj_map.get("resourceIds", [])
    if obj_map["id"].startswith("foundation-"):
        count = sum(len(by_id.get(rid, {}).get("questionBank", [])) for rid in rids)
        return len(rids), count, f"{len(rids)} lessons ({count} recognition items)"
    if obj_map["id"] == "grammar-core":
        count = sum(len(by_id.get(rid, {}).get("exercises", [])) for rid in rids)
        return len(rids), count, f"{len(rids)} lessons / {count} exercises"
    if obj_map["id"] == "part5-sentence-completion":
        reserve = sum(1 for rid in rids if by_id.get(rid, {}).get("editorialStatus", data.get("editorialStatus")) == "reserve-pending-independent-review")
        return len(rids), len(rids), f"{len(rids)} questions ({reserve} reserve practice-only)"
    approved = reserve = 0
    for rid in rids:
        unit = by_id.get(rid, {})
        count = len(unit.get("questions", []))
        if unit.get("editorialStatus") == "reserve-pending-independent-review":
            reserve += count
        else:
            approved += count
    return len(rids), approved + reserve, f"{len(rids)} units / {approved + reserve}Q ({approved} non-reserve, {reserve} reserve)"


def build_report(root: Path = ROOT) -> dict[str, Any]:
    manifest = load_json(root, "data/manifest.json")
    rmap = load_json(root, "data/learning-path/objective-resource-map.json")
    outcomes = load_json(root, "data/learning-path/objective-outcomes.json")
    criterion_map = load_json(root, "data/learning-path/objective-criterion-map.json")
    map_by_id = {obj["id"]: obj for obj in rmap["objectives"]}
    mapping_counts: dict[str, int] = {}
    sample_keys: dict[str, list[str]] = {}
    for row in criterion_map.get("mappings", []):
        criterion_id = row["criterionId"]
        mapping_counts[criterion_id] = mapping_counts.get(criterion_id, 0) + 1
        sample_keys.setdefault(criterion_id, [])
        if len(sample_keys[criterion_id]) < 4 and row["questionKey"] not in sample_keys[criterion_id]:
            sample_keys[criterion_id].append(row["questionKey"])

    rows = []
    group_wired = 0
    total_instrumented = 0
    toeic_instrumented = 0
    toeic_uninstrumented = 0
    for group in outcomes["objectives"]:
        objective_id = group["objectiveId"]
        resource = map_by_id[objective_id]
        _resource_count, _question_count, inventory_note = count_questions_for_objective(root, resource)
        wiring = group["runtimeWiring"]
        group_wired += bool(wiring.get("groupLevelWired"))
        for outcome in group["outcomes"]:
            is_instrumented = str(outcome.get("status", "")).startswith("instrumented_")
            total_instrumented += is_instrumented
            is_toeic = not objective_id.startswith("foundation-")
            if is_toeic:
                toeic_instrumented += is_instrumented
                toeic_uninstrumented += not is_instrumented
            rows.append({
                "objectiveId": objective_id,
                "objectiveTitle": resource["title"],
                "toeicPart": resource.get("part") or ("Foundation" if not is_toeic else "Grammar / Support"),
                "outcomeId": outcome["id"],
                "outcomeTitle": outcome["title"],
                "evidenceMetric": outcome["evidenceMetric"],
                "threshold": f">={int(outcome['masteryThreshold'] * 100)}% & >={outcome['minimumUniqueItems']} unique",
                "inventory": inventory_note,
                "mappingCount": mapping_counts.get(outcome["id"], 0),
                "sampleKeys": sample_keys.get(outcome["id"], []),
                "evidenceSource": wiring["evidenceSource"],
                "measurementRule": outcome["measurementRule"],
                "status": outcome["status"],
                "runtimeStatusNote": outcome["runtimeStatusNote"],
                "limitations": wiring["limitations"],
                "reviewState": resource.get("reviewState", "")
            })
    return {
        "version": manifest["version"],
        "policy": outcomes["policy"],
        "objectiveCount": len(outcomes["objectives"]),
        "criteriaCount": len(rows),
        "criterionLevelInstrumentedCount": total_instrumented,
        "toeicInstrumentedCount": toeic_instrumented,
        "toeicUninstrumentedCount": toeic_uninstrumented,
        "groupLevelWiredObjectives": group_wired,
        "mappingCount": len(criterion_map.get("mappings", [])),
        "uniqueQuestionCount": criterion_map.get("uniqueQuestionCount", 0),
        "mappingCounts": mapping_counts,
        "rows": rows
    }


def render_markdown(report: dict[str, Any]) -> str:
    policy = report["policy"]
    lines = [
        f"# TOEIC Learning Outcome Evidence & Reconciliation — v{report['version']}",
        "",
        "Read-only report generated from the outcome registry, the canonical objective map, "
        "the stable question-to-criterion map, and the underlying question banks.",
        "",
        "## 1. Reconciliation summary",
        "",
        f"- Learning objectives: **{report['objectiveCount']}**",
        f"- Outcome criteria: **{report['criteriaCount']}**",
        f"- Criterion-level local evidence paths: **{report['criterionLevelInstrumentedCount']}/{report['criteriaCount']} "
        f"({report['criterionLevelInstrumentedCount'] / report['criteriaCount'] * 100:.1f}%)** — includes the six existing Foundation criteria.",
        f"- TOEIC sub-skill criteria with explicit stable-question instrumentation: **{report['toeicInstrumentedCount']}/27**",
        f"- TOEIC criteria deliberately not instrumented: **{report['toeicUninstrumentedCount']}/27**",
        f"- Stable question-to-criterion links: **{report['mappingCount']:,}** across **{report['uniqueQuestionCount']:,} unique question IDs**",
        f"- Objective groups with group-level runtime tracking: **{report['groupLevelWiredObjectives']}/{report['objectiveCount']}**",
        f"- Local evidence policy: at least **{policy['minimumUniqueItems']} unique items** and **{int(policy['defaultThreshold'] * 100)}%** for ordinary accuracy criteria; outcome-specific rules take precedence.",
        "",
        "### Interpretation and safeguards",
        "",
        "- A mapping is an available content link, not proof that a learner has completed the question or achieved the criterion.",
        "- Evidence is stored on-device in the existing IndexedDB `objectiveProgress` workspace. No database schema migration is introduced.",
        "- Explanation rubrics are optional learner self-reports; they are not automatically graded or externally verified.",
        "- Separate Part 5 timed accuracy uses a **30-second internal practice target**, not an ETS timing or score standard.",
        "- Listening reserve items are excluded from the criterion map. Reading Part 7 retains its second-review gate; Separate Part 5 retains its independent-review gate.",
        "- The five uninstrumented TOEIC criteria remain visible but receive no criterion-specific score until suitable evidence exists.",
        "- These local practice signals do not certify CEFR level, ETS mastery, official TOEIC score or production readiness.",
        "",
        "### TOEIC criteria still awaiting a defensible measurement path",
        "",
    ]
    for row in report["rows"]:
        if row["status"] == "criteria_defined_not_yet_instrumented":
            lines.append(f"- `{row['outcomeId']}` — {row['outcomeTitle']}")
    lines += [
        "",
        "## 2. Full 33-criterion evidence matrix",
        "",
        "| # | Objective / criterion | Part | Metric | Mapped questions | Learner evidence rule | Runtime state / limitation |",
        "|---:|---|---|---|---:|---|---|"
    ]
    for index, row in enumerate(report["rows"], 1):
        keys = ", ".join(f"`{key}`" for key in row["sampleKeys"])
        status = f"`{row['status']}` — {row['runtimeStatusNote']}"
        if row["reviewState"]:
            status += f" Review gate: {row['reviewState']}"
        if row["limitations"]:
            status += f" Limitation: {row['limitations']}"
        escape = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {index} | `{escape(row['objectiveId'])}` / `{escape(row['outcomeId'])}` — {escape(row['outcomeTitle'])} | "
            f"{escape(row['toeicPart'])} | `{row['evidenceMetric']}` | "
            f"**{row['mappingCount']}**" + (f" — {keys}" if keys else " — none") + " | "
            f"{escape(row['measurementRule'])} | " + escape(status) + " |"
        )
    lines += [
        "",
        "## 3. Mapping inventory by criterion",
        "",
        "| Criterion ID | Mapped stable question links |",
        "|---|---:|"
    ]
    for criterion_id, count in sorted(report["mappingCounts"].items()):
        lines.append(f"| `{criterion_id}` | {count} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown-output", type=Path)
    args = parser.parse_args()
    report = build_report(ROOT)
    output = args.markdown_output or (ROOT / "docs/reports" / f"TOEIC_LEARNING_OUTCOME_EVIDENCE_v{report['version']}.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_markdown(report), encoding="utf-8")
    print(
        f"Wrote {output.relative_to(ROOT) if output.is_relative_to(ROOT) else output} "
        f"({report['objectiveCount']} objectives, {report['criteriaCount']} criteria, "
        f"{report['criterionLevelInstrumentedCount']}/{report['criteriaCount']} total instrumented, "
        f"{report['toeicInstrumentedCount']}/27 TOEIC, {report['mappingCount']} question links)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
