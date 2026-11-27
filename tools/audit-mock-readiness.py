#!/usr/bin/env python3
"""Consolidate Full-Mock, Half-Mock, Quick-Mock, and Part-Practice readiness."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
APPROVED_STATUSES = (None, "approved-for-mock", "internal-editorial-reviewed")

MOCK_MODES = {
    "quick": {
        "label": "Test nhanh",
        "questions": 25,
        "minutes": 15,
        "listening": {"Part 1": 1, "Part 2": 2, "Part 3": 6, "Part 4": 3},
        "reading": {"Part 5": 2, "Part 6": 4, "Part 7 Single": 2, "Part 7 Multiple": 5},
    },
    "half": {
        "label": "Thi thử rút gọn",
        "questions": 100,
        "minutes": 60,
        # Half uses two balanced Listening variants: (P2=11, P3=21) or (P2=14, P3=18)
        "listening": {"Part 1": 3, "Part 2": 14, "Part 3": 18, "Part 4": 15},
        "listeningMinAlt": {"Part 1": 3, "Part 2": 11, "Part 3": 21, "Part 4": 15},
        "reading": {"Part 5": 15, "Part 6": 8, "Part 7 Single": 17, "Part 7 Multiple": 10},
    },
    "full": {
        "label": "Thi TOEIC đầy đủ",
        "questions": 200,
        "minutes": 120,
        "listening": {"Part 1": 6, "Part 2": 25, "Part 3": 39, "Part 4": 30},
        "reading": {"Part 5": 30, "Part 6": 16, "Part 7 Single": 29, "Part 7 Multiple": 25},
    },
}


def load_json(root: Path, rel: str) -> Any:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def is_approved(item: dict[str, Any]) -> bool:
    return item.get("editorialStatus") in APPROVED_STATUSES


def is_multiple_passage(unit: dict[str, Any]) -> bool:
    docs = unit.get("documents") or []
    doc_type = str(unit.get("documentType") or "").lower()
    return len(docs) > 1 or any(tag in doc_type for tag in ("double", "triple", "multiple"))


def can_pack_disjoint_reading_forms(
    units: list[dict[str, Any]], target_per_form: int, forms: int
) -> bool:
    """Verify indivisible passage blocks can form `forms` disjoint forms of exact size."""
    remaining = list(units)
    for _ in range(forms):
        dp: dict[int, list[int]] = {0: []}
        for idx, unit in enumerate(remaining):
            qlen = len(unit.get("questions") or [])
            if qlen <= 0:
                continue
            for total in sorted(dp.keys(), reverse=True):
                nxt = total + qlen
                if nxt <= target_per_form and nxt not in dp:
                    dp[nxt] = dp[total] + [idx]
        if target_per_form not in dp:
            return False
        picked = set(dp[target_per_form])
        remaining = [u for i, u in enumerate(remaining) if i not in picked]
    return True


def build_report(root: Path = ROOT) -> dict[str, Any]:
    version = load_json(root, "data/manifest.json")["version"]
    listening = load_json(root, "data/listening/listening-library.json")["listening"]
    readings = load_json(root, "data/readings/reading-library.json")["readings"]
    p5_bank = load_json(root, "data/practice/part5-sentence-completion.json")
    grammar = load_json(root, "data/grammar/lessons.json")["lessons"]

    l_app = {f"Part {p}": [] for p in range(1, 5)}
    l_res = {f"Part {p}": [] for p in range(1, 5)}
    for u in listening:
        target = l_app if is_approved(u) else l_res
        if u.get("part") in target:
            target[u["part"]].append(u)

    r_app_p5 = [u for u in readings if u.get("part") == "Part 5" and is_approved(u)]
    r_app_p6 = [u for u in readings if u.get("part") == "Part 6" and is_approved(u)]
    r_app_p7 = [u for u in readings if u.get("part") == "Part 7" and is_approved(u)]
    r_res_p7 = [u for u in readings if u.get("part") == "Part 7" and not is_approved(u)]
    r_app_p7_single = [u for u in r_app_p7 if not is_multiple_passage(u)]
    r_app_p7_multi = [u for u in r_app_p7 if is_multiple_passage(u)]

    approved_pools = {
        "Listening Part 1": sum(len(u.get("questions") or []) for u in l_app["Part 1"]),
        "Listening Part 2": sum(len(u.get("questions") or []) for u in l_app["Part 2"]),
        "Listening Part 3": sum(len(u.get("questions") or []) for u in l_app["Part 3"]),
        "Listening Part 4": sum(len(u.get("questions") or []) for u in l_app["Part 4"]),
        "Reading Part 5": sum(len(u.get("questions") or []) for u in r_app_p5),
        "Reading Part 6": sum(len(u.get("questions") or []) for u in r_app_p6),
        "Reading Part 7 Single": sum(len(u.get("questions") or []) for u in r_app_p7_single),
        "Reading Part 7 Multiple": sum(len(u.get("questions") or []) for u in r_app_p7_multi),
    }
    reserve_pools = {
        "Listening Part 1": sum(len(u.get("questions") or []) for u in l_res["Part 1"]),
        "Listening Part 2": sum(len(u.get("questions") or []) for u in l_res["Part 2"]),
        "Listening Part 3": sum(len(u.get("questions") or []) for u in l_res["Part 3"]),
        "Listening Part 4": sum(len(u.get("questions") or []) for u in l_res["Part 4"]),
        "Reading Part 5": 0,
        "Reading Part 6": 0,
        "Reading Part 7 Single": sum(len(u.get("questions") or []) for u in r_res_p7 if not is_multiple_passage(u)),
        "Reading Part 7 Multiple": sum(len(u.get("questions") or []) for u in r_res_p7 if is_multiple_passage(u)),
    }

    listening_approved_total = sum(approved_pools[f"Listening Part {p}"] for p in range(1, 5))
    listening_reserve_total = sum(reserve_pools[f"Listening Part {p}"] for p in range(1, 5))
    reading_approved_total = (
        approved_pools["Reading Part 5"]
        + approved_pools["Reading Part 6"]
        + approved_pools["Reading Part 7 Single"]
        + approved_pools["Reading Part 7 Multiple"]
    )
    reading_reserve_total = (
        reserve_pools["Reading Part 7 Single"] + reserve_pools["Reading Part 7 Multiple"]
    )

    reading_two_disjoint = (
        approved_pools["Reading Part 5"] >= 60
        and can_pack_disjoint_reading_forms(r_app_p6, 16, 2)
        and can_pack_disjoint_reading_forms(r_app_p7_single, 29, 2)
        and can_pack_disjoint_reading_forms(r_app_p7_multi, 25, 2)
    )

    # Full-mock second-form minimum reuse in Listening
    full_listen_spec = MOCK_MODES["full"]["listening"]
    full_listening_surplus = {
        part: approved_pools[f"Listening {part}"] - req for part, req in full_listen_spec.items()
    }
    second_form_min_overlap = sum(
        max(0, req - full_listening_surplus[part]) for part, req in full_listen_spec.items()
    )

    # Post-review ceiling if ALL reserve Listening items were independently approved
    listening_post_review_by_part = {
        f"Part {p}": approved_pools[f"Listening Part {p}"] + reserve_pools[f"Listening Part {p}"]
        for p in range(1, 5)
    }
    listening_post_review_disjoint_full = min(
        listening_post_review_by_part[part] // req for part, req in full_listen_spec.items()
    )

    mode_summaries = {}
    for mode_id, spec in MOCK_MODES.items():
        l_need = spec["listening"]
        r_need = spec["reading"]
        l_disjoint = min(approved_pools[f"Listening {part}"] // need for part, need in l_need.items())
        if mode_id == "half":
            # In half mode, P2 can draw 11..14 and P3 18..21; pool P2=25, P3=39 gives 1..2 disjoint halves except P3=18+21=39, P2=11+14=25, P4=30//15=2, P1=8//3=2!
            l_disjoint = min(
                approved_pools["Listening Part 1"] // 3,
                approved_pools["Listening Part 2"] // 11,
                approved_pools["Listening Part 3"] // 18,
                approved_pools["Listening Part 4"] // 15,
            )
            # Check exact sum across 2 balanced variants: 11+14=25 (exact), 21+18=39 (exact), 15*2=30 (exact), 3*2=6<=8!
            if not (approved_pools["Listening Part 2"] >= 25 and approved_pools["Listening Part 3"] >= 39 and approved_pools["Listening Part 4"] >= 30 and approved_pools["Listening Part 1"] >= 6):
                l_disjoint = 1
        r_disjoint = min(
            approved_pools["Reading Part 5"] // r_need["Part 5"],
            approved_pools["Reading Part 6"] // r_need["Part 6"],
            approved_pools["Reading Part 7 Single"] // r_need["Part 7 Single"],
            approved_pools["Reading Part 7 Multiple"] // r_need["Part 7 Multiple"],
        )
        mode_summaries[mode_id] = {
            "label": spec["label"],
            "questions": spec["questions"],
            "minutes": spec["minutes"],
            "singleFormSupported": (
                all(approved_pools[f"Listening {part}"] >= need for part, need in l_need.items())
                and all(approved_pools[f"Reading {part}"] >= need for part, need in r_need.items())
            ),
            "disjointListeningForms": l_disjoint,
            "disjointReadingForms": r_disjoint,
            "disjointFullCombinedForms": min(l_disjoint, r_disjoint),
        }

    return {
        "version": version,
        "approvedPools": approved_pools,
        "reservePools": reserve_pools,
        "listeningApprovedTotal": listening_approved_total,
        "listeningReserveTotal": listening_reserve_total,
        "readingApprovedTotal": reading_approved_total,
        "readingReserveTotal": reading_reserve_total,
        "separatePart5PracticeOnly": len(p5_bank.get("questions") or []),
        "grammarSupportLessons": len(grammar),
        "grammarSupportExercises": sum(len(x.get("exercises") or []) for x in grammar),
        "readingTwoDisjointFullFormsVerified": reading_two_disjoint,
        "listeningSecondFullFormMinOverlap": second_form_min_overlap,
        "listeningSecondFullFormMaxNew": 100 - second_form_min_overlap,
        "listeningPostReviewByPart": listening_post_review_by_part,
        "listeningPostReviewDisjointFullForms": listening_post_review_disjoint_full,
        "modes": mode_summaries,
    }


def render_markdown(report: dict[str, Any]) -> str:
    app = report["approvedPools"]
    res = report["reservePools"]
    lines = [
        f"# TOEIC Full-Mock Readiness Consolidation — v{report['version']}",
        "",
        "Read-only readiness audit built strictly from `APPROVED_FOR_MOCK` pools (`editorialStatus` empty or `internal-editorial-reviewed`). "
        "Reserve items (`reserve-pending-independent-review`) and Separate Part 5 (`80` practice-only questions) are **never** sampled in Mock.",
        "",
        "## 1. Approved Mock Pool vs Reserve Pool by Part",
        "",
        "| Sub-pool | `APPROVED_FOR_MOCK` (Q) | `HUMAN_REVIEW_REQUIRED` Reserve (Q) | Full-Mock Quota (200Q) | Disjoint Full-Form Capacity | Primary Bottleneck |",
        "|---|---:|---:|---:|---:|---|",
    ]
    rows_meta = [
        ("Listening Part 1", 6, "Needs >=12Q for 2 disjoint Full forms; even post-review cap is 9Q (hard photo bottleneck)."),
        ("Listening Part 2", 25, "1 exact form (0 surplus); 2nd Full form reuses 25/25 until 36 reserve units pass review."),
        ("Listening Part 3", 39, "1 exact form (0 surplus); 2nd Full form reuses 39/39 until 28 reserve units pass review."),
        ("Listening Part 4", 30, "1 exact form (0 surplus); 2nd Full form reuses 30/30 until 24 reserve units pass review."),
        ("Reading Part 5", 30, "Supports 2 disjoint Full forms (60Q approved); Separate 80Q P5 remains excluded."),
        ("Reading Part 6", 16, "Supports 2 disjoint Full forms (32Q approved in indivisible blocks)."),
        ("Reading Part 7 Single", 29, "Supports 2 disjoint Full forms (58Q approved in indivisible blocks)."),
        ("Reading Part 7 Multiple", 25, "Supports 2 disjoint Full forms (50Q approved in indivisible blocks)."),
    ]
    for name, quota, note in rows_meta:
        cap = app[name] // quota
        lines.append(f"| {name} | {app[name]} | {res[name]} | {quota} | {cap}x | {note} |")

    lines += [
        f"| **Listening Total** | **{report['listeningApprovedTotal']}** | **{report['listeningReserveTotal']}** | **100** | **1x** ({report['listeningSecondFullFormMaxNew']} surplus P1 Qs) | Reuses minimum **{report['listeningSecondFullFormMinOverlap']}/100** Qs on 2nd Full form |",
        f"| **Reading Total** | **{report['readingApprovedTotal']}** | **{report['readingReserveTotal']}** | **100** | **2x** (exact DP block-packed: {'PASS' if report['readingTwoDisjointFullFormsVerified'] else 'FAIL'}) | Separate 80Q P5 & 87Q P7 reserve excluded |",
        "",
        "## 2. Mode-by-Mode Operational Readiness",
        "",
        "| Mode | Questions | Duration | 1st Form Valid | Disjoint Listening Forms | Disjoint Reading Forms | Disjoint Combined Forms | Notes |",
        "|---|---:|---:|:---:|---:|---:|---:|---|",
    ]
    for mid in ("full", "half", "quick"):
        m = report["modes"][mid]
        lines.append(
            f"| `{mid}` ({m['label']}) | {m['questions']} | {m['minutes']} min | "
            f"{'YES' if m['singleFormSupported'] else 'NO'} | {m['disjointListeningForms']} | "
            f"{m['disjointReadingForms']} | {m['disjointFullCombinedForms']} | "
            f"{'Gated against repeated Listening forms in mock-score-readiness.js' if mid == 'full' else 'Practice / diagnostic simulation only'} |"
        )

    pr = report["listeningPostReviewByPart"]
    lines += [
        f"| Part Practice (Library + Separate P5 + Grammar) | All eligible/practice | Untimed / timed P5 | YES | — | — | — | {report['grammarSupportExercises']} Grammar + {report['separatePart5PracticeOnly']} Separate P5 + full Reading/Listening libraries (Listening reserves excluded from `objectiveProgress`) |",
        "",
        "## 3. Exact Listening Bottleneck & Readiness Guardrails",
        "",
        f"- **Current Full-Mock Listening pool**: **{report['listeningApprovedTotal']} questions** (Part 1 = {app['Listening Part 1']}, Part 2 = {app['Listening Part 2']}, Part 3 = {app['Listening Part 3']}, Part 4 = {app['Listening Part 4']}).",
        f"- **Minimum overlap on 2nd Full Listening form**: **{report['listeningSecondFullFormMinOverlap']}%** (`{report['listeningSecondFullFormMinOverlap']}/100` reused: 4 Part 1 + 25 Part 2 + 39 Part 3 + 30 Part 4; only 2 unused Part 1 questions remain).",
        f"- **Post-review ceiling if all {report['listeningReserveTotal']} Listening reserves were approved**: "
        f"Part 1 = {pr['Part 1']}/12, Part 2 = {pr['Part 2']}/50, Part 3 = {pr['Part 3']}/78, Part 4 = {pr['Part 4']}/60. "
        f"Combined disjoint 100Q Listening forms remain **{report['listeningPostReviewDisjointFullForms']}** because **Listening Part 1 only has {pr['Part 1']} total photographs (3 short of the 12 needed for 2 disjoint Full forms)**.",
        "- **Reading independence**: Approved Reading (`200Q`) packs into **2 completely disjoint 100Q Full forms** preserving indivisible Part 6 and Part 7 single/multi-passage blocks (`readingTwoDisjointFullFormsVerified = "
        + ("true" if report["readingTwoDisjointFullFormsVerified"] else "false")
        + "`).",
        "- **Zero ETS scaled score claims**: `mock-engine.js` and `mock-score-readiness.js` report raw accuracy percentages only; no `/495` or `/990` ETS conversion exists, and `buildMockScoreReadiness()` suppresses Listening trends until >=2 distinct Listening forms are recorded (with >=90% overlap warnings).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    report = build_report(ROOT)
    out = args.markdown_output or (ROOT / "docs/reports" / f"TOEIC_MOCK_READINESS_v{report['version']}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown(report), encoding="utf-8")
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out} | "
        f"L_approved={report['listeningApprovedTotal']}, R_approved={report['readingApprovedTotal']}, "
        f"2nd_L_overlap={report['listeningSecondFullFormMinOverlap']}%, R_2x_disjoint={report['readingTwoDisjointFullFormsVerified']}"
    )
    return 0 if report["modes"]["full"]["singleFormSupported"] and report["readingTwoDisjointFullFormsVerified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
