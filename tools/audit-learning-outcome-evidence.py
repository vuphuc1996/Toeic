#!/usr/bin/env python3
"""Generate the reconciled 33-criterion learning-outcome evidence mapping report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load_json(root: Path, rel: str) -> Any:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def count_questions_for_objective(root: Path, obj_map: dict[str, Any]) -> tuple[int, int, str]:
    rel = obj_map["resourceFile"]
    data = load_json(root, rel)
    col = obj_map["resourceCollection"]
    items = data.get(col, [])
    by_id = {item.get("id"): item for item in items if isinstance(item, dict)}
    rids = obj_map.get("resourceIds", [])

    if obj_map["id"].startswith("foundation-"):
        recognition_q = 0
        for rid in rids:
            lesson = by_id.get(rid, {})
            recognition_q += len(lesson.get("questionBank", []))
        return len(rids), recognition_q, f"{len(rids)} lessons ({recognition_q} recognition items)"

    if obj_map["id"] == "grammar-core":
        q_count = sum(len(by_id.get(rid, {}).get("exercises", [])) for rid in rids)
        return len(rids), q_count, f"{len(rids)} lessons / {q_count} exercises"

    if obj_map["id"] == "part5-sentence-completion":
        reserve = sum(
            1
            for rid in rids
            if by_id.get(rid, {}).get("editorialStatus", data.get("editorialStatus"))
            == "reserve-pending-independent-review"
        )
        return len(rids), len(rids), f"{len(rids)} questions ({reserve} reserve practice-only)"

    approved_q = 0
    reserve_q = 0
    for rid in rids:
        unit = by_id.get(rid, {})
        qs = len(unit.get("questions", []))
        if unit.get("editorialStatus") == "reserve-pending-independent-review":
            reserve_q += qs
        else:
            approved_q += qs
    return (
        len(rids),
        approved_q + reserve_q,
        f"{len(rids)} units / {approved_q + reserve_q}Q ({approved_q} approved, {reserve_q} reserve)",
    )


def build_report(root: Path = ROOT) -> dict[str, Any]:
    manifest = load_json(root, "data/manifest.json")
    version = manifest["version"]
    rmap = load_json(root, "data/learning-path/objective-resource-map.json")
    outcomes_doc = load_json(root, "data/learning-path/objective-outcomes.json")
    map_by_id = {obj["id"]: obj for obj in rmap["objectives"]}

    rows = []
    instrumented_criteria = 0
    group_wired_objectives = 0
    for obj in outcomes_doc["objectives"]:
        oid = obj["objectiveId"]
        m = map_by_id[oid]
        r_count, q_count, inventory_note = count_questions_for_objective(root, m)
        wiring = obj["runtimeWiring"]
        if wiring.get("groupLevelWired"):
            group_wired_objectives += 1
        for out in obj["outcomes"]:
            if str(out.get("status", "")).startswith("instrumented_"):
                instrumented_criteria += 1
            rows.append(
                {
                    "objectiveId": oid,
                    "objectiveTitle": m["title"],
                    "toeicPart": m.get("part") or ("Foundation" if oid.startswith("foundation-") else "Grammar (Part 5/6)"),
                    "outcomeId": out["id"],
                    "outcomeTitle": out["title"],
                    "evidenceMetric": out["evidenceMetric"],
                    "threshold": f">={int(out['masteryThreshold']*100)}% & >={out['minimumUniqueItems']} unique",
                    "resourceScope": f"`{m['resourceFile']}` ({inventory_note}; {len(m['resourceIds'])} IDs)",
                    "sampleIds": ", ".join(f"`{rid}`" for rid in m["resourceIds"][:3])
                    + ("..." if len(m["resourceIds"]) > 3 else ""),
                    "evidenceSource": wiring["evidenceSource"],
                    "measurementRule": out["measurementRule"],
                    "status": out["status"],
                    "runtimeStatusNote": out["runtimeStatusNote"],
                    "objectiveLimitations": wiring["limitations"],
                }
            )

    return {
        "version": version,
        "policy": outcomes_doc["policy"],
        "objectiveCount": len(outcomes_doc["objectives"]),
        "criteriaCount": len(rows),
        "criterionLevelInstrumentedCount": instrumented_criteria,
        "groupLevelWiredObjectives": group_wired_objectives,
        "rows": rows,
    }


def render_markdown(report: dict[str, Any]) -> str:
    p = report["policy"]
    lines = [
        f"# TOEIC Learning Outcome Evidence & Reconciliation — v{report['version']}",
        "",
        "Generated read-only from `data/learning-path/objective-outcomes.json`, "
        "`data/learning-path/objective-resource-map.json`, and canonical banks.",
        "",
        "## 1. Reconciliation Summary (Criterion-Level vs Group-Level Wiring)",
        "",
        f"- Total learning objectives mapped: **{report['objectiveCount']}**",
        f"- Total measurable outcome criteria: **{report['criteriaCount']}**",
        f"- Criterion-level instrumented outcomes (unchanged project-progress numerator): "
        f"**{report['criterionLevelInstrumentedCount']}/{report['criteriaCount']} "
        f"({report['criterionLevelInstrumentedCount'] / report['criteriaCount'] * 100:.1f}%)** — Foundation Pre-A1/A1 & A2 recognition, self-report production, and delayed recall.",
        f"- Objective groups with runtime local evidence tracking in `assets/js/app.js`: "
        f"**{report['groupLevelWiredObjectives']}/{report['objectiveCount']}** "
        "(`foundationProgress*` for Foundation + `objectiveProgress` via `trackObjectivePractice()` / `recordExplanationRubric()` for TOEIC groups).",
        f"- Policy defaults: `minimumUniqueItems = {p['minimumUniqueItems']}`, `defaultThreshold = {int(p['defaultThreshold'] * 100)}%`, `retestPolicy = {p['retestPolicy']}`.",
        "",
        "### Why the 27 TOEIC sub-skill criteria remain `criteria_defined_not_yet_instrumented`",
        "",
        "1. `trackObjectivePractice()` records outcomes by TOEIC Part / objective group (`grammar-core`, `listening-part-1..4`, `reading-part-5..7`, `part5-sentence-completion`) rather than per individual sub-skill tag (e.g., `conversation-purpose` vs `detail-inference`).",
        "2. `recordExplanationRubric()` is currently wired in UI only inside `openPracticeReviewModal()` for Separate Part 5 (`part5-sentence-completion`), not for `grammar-core-error-explanation` or `reading-part-5-distractor-explanation`.",
        "3. `timed_accuracy` records `durationMs` and `averageResponseTimeMs`, without an automated pass/fail speed cutoff.",
        "4. `listening-part-1` contains only **8 mock-eligible items** (1 reserve excluded), below `minimumUniqueItems = 10`.",
        "5. `reading-part-7` (22 reserve units / 87Q) and `part5-sentence-completion` (80Q) are capped at `content_review_pending` in `summarizeAllObjectives()` until independent editorial review is recorded.",
        "6. Neither local threshold attainment nor self-report rubrics certify CEFR levels or official ETS TOEIC scores.",
        "",
        "## 2. Full 33-Criterion Evidence Matrix",
        "",
        "| # | Learning Objective | Outcome Criterion | TOEIC Part | Question / Resource IDs | Evidence Source | Measurement Rule | Runtime Status & Limitations |",
        "|---:|---|---|---|---|---|---|---|",
    ]
    for idx, row in enumerate(report["rows"], 1):
        esc = lambda s: str(s).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {idx} | `{esc(row['objectiveId'])}` ({esc(row['objectiveTitle'])}) | "
            f"`{esc(row['outcomeId'])}` — {esc(row['outcomeTitle'])} (`{row['evidenceMetric']}`) | "
            f"{esc(row['toeicPart'])} | {esc(row['resourceScope'])}; e.g. {esc(row['sampleIds'])} | "
            f"{esc(row['evidenceSource'])} | {esc(row['measurementRule'])} | "
            f"`{row['status']}` — {esc(row['runtimeStatusNote'])} Limit: {esc(row['objectiveLimitations'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown-output", type=Path)
    args = parser.parse_args()

    report = build_report(ROOT)
    out = args.markdown_output or (
        ROOT / "docs/reports" / f"TOEIC_LEARNING_OUTCOME_EVIDENCE_v{report['version']}.md"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown(report), encoding="utf-8")
    print(
        f"Wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out} "
        f"({report['objectiveCount']} objectives, {report['criteriaCount']} criteria, "
        f"{report['criterionLevelInstrumentedCount']}/{report['criteriaCount']} criterion-instrumented, "
        f"{report['groupLevelWiredObjectives']}/{report['objectiveCount']} group-wired)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
