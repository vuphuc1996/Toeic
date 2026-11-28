#!/usr/bin/env python3
"""Canonical, source-derived editorial inventory metrics for review packets.

This module is the shared source for Editorial Review Queue counts. It is
read-only: it never changes editorialStatus, Mock eligibility or question data.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESERVE_STATUS = "reserve-pending-independent-review"
ELIGIBLE_STATUSES = {None, "approved-for-mock"}


def read_json(root: Path, relative: str) -> dict[str, Any]:
    return json.loads((root / relative).read_text(encoding="utf-8"))


def _question_count(resources: list[dict[str, Any]]) -> int:
    return sum(len(resource.get("questions", [])) for resource in resources)


def _part_counts(resources: list[dict[str, Any]]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for resource in resources:
        counts[str(resource.get("part") or "Unclassified")] += len(resource.get("questions", []))
    return dict(sorted(counts.items()))


def collect_editorial_inventory(root: Path = ROOT) -> dict[str, Any]:
    """Compute current review/eligibility counts from canonical source data.

    Missing Listening editorialStatus retains the established eligible meaning;
    explicit unknown statuses fail closed rather than being counted as eligible.
    Part 7 reserve and the separate Part 5 practice-only bank remain separate.
    """
    listening = read_json(root, "data/listening/listening-library.json")["listening"]
    readings = read_json(root, "data/readings/reading-library.json")["readings"]
    part5_bank = read_json(root, "data/practice/part5-sentence-completion.json")

    eligible_units: list[dict[str, Any]] = []
    reserve_units: list[dict[str, Any]] = []
    unknown_statuses: Counter[str] = Counter()
    eligible_ids: list[str] = []
    reserve_ids: list[str] = []
    practice_only_ids: list[str] = []
    eligible_by_part: Counter[str] = Counter()
    reserve_by_part: Counter[str] = Counter()
    practice_only_by_part: Counter[str] = Counter()

    for unit in listening:
        status = unit.get("editorialStatus")
        part = str(unit.get("part") or "Unclassified")
        unit_id = unit.get("id", "unknown")
        questions = unit.get("questions", [])
        if status in ELIGIBLE_STATUSES:
            eligible_units.append(unit)
            for index, question in enumerate(questions, 1):
                qid = f"{unit_id}#Q{index}"
                if question.get("mockEligible") is False:
                    practice_only_ids.append(qid)
                    practice_only_by_part[part] += 1
                else:
                    eligible_ids.append(qid)
                    eligible_by_part[part] += 1
        elif status == RESERVE_STATUS:
            reserve_units.append(unit)
            for index, question in enumerate(questions, 1):
                if question.get("mockEligible") is False:
                    raise ValueError(f"Reserve Listening unit contains unexpected mockEligible=false question: {unit_id}#Q{index}")
                reserve_ids.append(f"{unit_id}#Q{index}")
                reserve_by_part[part] += 1
        else:
            unknown_statuses[str(status)] += len(questions)

    if unknown_statuses:
        raise ValueError(f"Unclassified Listening editorial statuses: {dict(unknown_statuses)}")
    if len(eligible_ids) != len(set(eligible_ids)):
        raise ValueError("Duplicate question IDs detected in Listening eligible pool")
    if len(reserve_ids) != len(set(reserve_ids)):
        raise ValueError("Duplicate question IDs detected in Listening reserve pool")
    if len(practice_only_ids) != len(set(practice_only_ids)):
        raise ValueError("Duplicate question IDs detected in Listening practice-only pool")
    overlap = sorted((set(eligible_ids) & set(reserve_ids)) | (set(eligible_ids) & set(practice_only_ids)) | (set(reserve_ids) & set(practice_only_ids)))
    if overlap:
        raise ValueError(f"Listening eligible/reserve/practice-only question IDs overlap: {overlap[:10]}")

    READING_ELIGIBLE_STATUSES = {None, "approved-for-mock", "internal-editorial-reviewed"}

    reading_eligible_units: list[dict[str, Any]] = []
    reading_reserve_units: list[dict[str, Any]] = []
    reading_unknown_statuses: Counter[str] = Counter()
    for unit in readings:
        status = unit.get("editorialStatus")
        if status in READING_ELIGIBLE_STATUSES:
            reading_eligible_units.append(unit)
        elif status == RESERVE_STATUS:
            reading_reserve_units.append(unit)
        else:
            reading_unknown_statuses[str(status)] += len(unit.get("questions", []))
    if reading_unknown_statuses:
        raise ValueError(f"Unclassified Reading editorial statuses: {dict(reading_unknown_statuses)}")

    part7_units = [
        unit for unit in reading_reserve_units
        if unit.get("part") == "Part 7"
    ]
    p5_questions = part5_bank.get("questions", [])
    p5_pending = [
        question for question in p5_questions
        if question.get("editorialStatus", part5_bank.get("editorialStatus")) == RESERVE_STATUS
    ]
    p5_other = len(p5_questions) - len(p5_pending)

    return {
        "listening": {
            "eligible_resources": len(eligible_units),
            "reserve_resources": len(reserve_units),
            "eligible_questions": len(eligible_ids),
            "reserve_questions": len(reserve_ids),
            "practice_only_questions": len(practice_only_ids),
            "total_questions": _question_count(listening),
            "eligible_by_part": dict(sorted(eligible_by_part.items())),
            "reserve_by_part": dict(sorted(reserve_by_part.items())),
            "practice_only_by_part": dict(sorted(practice_only_by_part.items())),
            "eligible_question_ids": sorted(eligible_ids),
            "reserve_question_ids": sorted(reserve_ids),
            "practice_only_question_ids": sorted(practice_only_ids),
        },
        "reading": {
            "eligible_resources": len(reading_eligible_units),
            "reserve_resources": len(reading_reserve_units),
            "eligible_questions": _question_count(reading_eligible_units),
            "reserve_questions": _question_count(reading_reserve_units),
            "total_questions": _question_count(readings),
            "eligible_by_part": _part_counts(reading_eligible_units),
            "reserve_by_part": _part_counts(reading_reserve_units),
        },
        "part7": {
            "reserve_resources": len(part7_units),
            "reserve_questions": _question_count(part7_units),
        },
        "part5": {
            "total_questions": len(p5_questions),
            "review_pending_questions": len(p5_pending),
            "other_status_questions": p5_other,
            "practice_only": True,
        },
    }


if __name__ == "__main__":
    result = collect_editorial_inventory()
    print(json.dumps(result, ensure_ascii=False, indent=2))
