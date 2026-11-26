#!/usr/bin/env python3
"""Generate a transparent, weighted build-progress index from canonical project data."""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "tools/project-progress-plan-v2.95.71.json"


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def load_glossary_audit():
    spec = importlib.util.spec_from_file_location("glossary_quality_audit", ROOT / "tools/audit-related-glossary-quality.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load glossary quality audit implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.audit(load("data/related-terms.json").get("terms", []))


def ratio(n: int, d: int) -> float:
    return 0.0 if not d else n / d


def build():
    plan = load("tools/project-progress-plan-v2.95.71.json")
    manifest = load("data/manifest.json")
    vocab = sum(x["count"] for x in manifest["letters"])
    vocab_records = []
    for entry in manifest["letters"]:
        vocab_records.extend(load(entry["file"].replace("./", "", 1)).get("words", []))

    related_keys = {str(x.get("term", "")).strip().casefold() for x in load("data/related-terms.json").get("terms", [])}
    relation_targets = {
        str(term).strip().casefold()
        for record in vocab_records
        for sense in record.get("senses", [])
        for field in ("synonyms", "antonyms")
        for term in (sense.get(field) or [])
    }

    glossary_audit = load_glossary_audit()
    glossary_records = glossary_audit["entries"]
    glossary_unflagged = glossary_records - glossary_audit["flagged_entries"]

    foundation = load("data/learning-path/pre-a1-a1.json")["lessons"]
    stages = {str(x.get("level", "")).upper() for x in foundation}
    stage_order = plan["denominators"]["guided_pathway_stages"]
    stage_count = sum(1 for stage in stage_order if stage in stages)

    objective_map = load("data/learning-path/objective-resource-map.json")["objectives"]
    objective_total = sum(len(load(rel)[collection]) for rel, collection in {(v["resourceFile"], v["resourceCollection"]) for v in objective_map})
    objective_mapped = len({(x["resourceFile"], x["resourceCollection"], resource_id) for x in objective_map for resource_id in x.get("resourceIds", [])})

    registry = load("data/learning-path/objective-outcomes.json")["objectives"]
    outcome_total = sum(len(x.get("outcomes", [])) for x in registry)
    outcome_instrumented = sum(1 for x in registry for outcome in x.get("outcomes", []) if str(outcome.get("status", "")).startswith("instrumented_"))

    foundation_reading = load("data/learning-path/foundation-reading.json")["passages"]
    foundation_listening = [x for x in load("data/learning-path/foundation-listening.json")["clips"] if not x.get("supplementary")]
    alphabet = load("data/learning-path/alphabet-sounds.json")["letters"]
    foundation_parts = [
        (len(foundation_reading), len(foundation_reading)),
        (len(foundation_listening), len(foundation)),
        (len(alphabet), 26),
    ]
    foundation_coverage = sum(ratio(n, d) for n, d in foundation_parts) / len(foundation_parts)

    definitions = [
        ("Vocabulary headwords vs 3,000 minimum", vocab, plan["denominators"]["vocabulary_target"], ratio(vocab, plan["denominators"]["vocabulary_target"]), plan["weights"]["vocabulary_headwords_minimum"], "Inventory coverage only; editorial quality separate."),
        ("Related glossary exact-join coverage", len(relation_targets & related_keys), len(relation_targets), ratio(len(relation_targets & related_keys), len(relation_targets)), plan["weights"]["related_glossary_join_coverage"], "Exact case-insensitive relation-target join; no sense-quality claim."),
        ("Related glossary records without automated flags", glossary_unflagged, glossary_records, ratio(glossary_unflagged, glossary_records), plan["weights"]["related_glossary_unflagged_records"], "Automated screening only; not independent editorial approval."),
        ("Guided pathway stage presence", stage_count, len(stage_order), ratio(stage_count, len(stage_order)), plan["weights"]["guided_pathway_stage_presence"], "Stage presence, not full-stage or lesson completion."),
        ("Canonical objective-resource mapping", objective_mapped, objective_total, ratio(objective_mapped, objective_total), plan["weights"]["objective_resource_id_mapping"], "Stable resource-ID mapping only; not mastery."),
        ("Outcome criteria with evidence instrumentation", outcome_instrumented, outcome_total, ratio(outcome_instrumented, outcome_total), plan["weights"]["outcome_evidence_instrumentation"], "Evidence collection path; not learner attainment."),
        ("Foundation core content coverage (3 equally weighted banks)", round(foundation_coverage * 10000), 10000, foundation_coverage, plan["weights"]["foundation_core_content_coverage"], "Reading passages, core Listening scripts and A–Z records; within existing Foundation scope only."),
    ]
    total_weight = sum(x[4] for x in definitions)
    score = sum(x[3] * x[4] for x in definitions) / total_weight * 100 if total_weight else 0
    return {
        "schemaVersion": 1,
        "sourceVersion": manifest["version"],
        "modelId": plan["modelId"],
        "status": plan["status"],
        "weightedIndexPercent": round(score, 2),
        "totalWeight": total_weight,
        "metrics": [
            {"name": name, "numerator": numerator, "denominator": denominator, "percent": round(value * 100, 2), "weight": weight, "contributionPoints": round(value * weight, 2), "interpretation": interpretation}
            for name, numerator, denominator, value, weight, interpretation in definitions
        ],
        "glossaryAudit": {
            "entries": glossary_records,
            "flagged": glossary_audit["flagged_entries"],
            "unflagged": glossary_unflagged,
            "priorityCounts": glossary_audit["priority_counts"],
            "issueCounts": glossary_audit["issue_counts"],
            "duplicateGroups": len(glossary_audit["duplicates"]),
        },
        "explicitExclusions": plan["exclusions"],
        "warning": "This is a transparent provisional index of selected measurable build areas, not an official total-system completion, production acceptance, learner mastery or TOEIC readiness score."
    }


def render(report: dict) -> str:
    lines = [
        f"# Project Progress Dashboard — TOEIC Dictionary v{report['sourceVersion']}",
        "",
        f"**Weighted measurable curriculum-build index: {report['weightedIndexPercent']:.2f}%**",
        "",
        f"Model: `{report['modelId']}` · Status: `{report['status']}` · Total weight: {report['totalWeight']}",
        "",
        "| Workstream | Numerator / denominator | Coverage | Weight | Contribution | Interpretation |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for item in report["metrics"]:
        n, d = item["numerator"], item["denominator"]
        numerator = f"{n / 10000:.2f}" if d == 10000 else f"{n:,}"
        denominator = "1.00" if d == 10000 else f"{d:,}"
        lines.append(f"| {item['name']} | {numerator}/{denominator} | **{item['percent']:.1f}%** | {item['weight']}% | {item['contributionPoints']:.2f} pts | {item['interpretation']} |")
    qa = report["glossaryAudit"]
    lines += [
        "",
        "## Related Glossary quality audit",
        "",
        f"- {qa['unflagged']}/{qa['entries']} records without automated flags ({qa['unflagged']/qa['entries']*100:.1f}%).",
        f"- {qa['flagged']} records remain flagged; priority: {qa['priorityCounts']}; duplicate normalized groups: {qa['duplicateGroups']}.",
        f"- Issue counts: `{json.dumps(qa['issueCounts'], ensure_ascii=False, sort_keys=True)}`.",
        "- No automated flag is treated as independent editorial approval.",
        "",
        "## Explicitly excluded from the index",
        "",
    ]
    lines += [f"- {x}." for x in report["explicitExclusions"]]
    lines += ["", f"> **Interpretation warning:** {report['warning']}", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--markdown-output", type=Path)
    args = parser.parse_args()
    report = build()
    markdown = render(report)
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(markdown, encoding="utf-8")
    print(markdown)


if __name__ == "__main__":
    main()
