#!/usr/bin/env python3
"""Audit stable question-to-outcome mappings against the canonical TOEIC banks."""
from __future__ import annotations
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = "data/learning-path/objective-criterion-map.json"
REGISTRY_PATH = "data/learning-path/objective-outcomes.json"
RESOURCE_PATH = "data/learning-path/objective-resource-map.json"


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def stable_question_key(question: dict) -> str | None:
    ids = question.get("choiceIds")
    if not isinstance(ids, list) or not ids or not isinstance(ids[0], str):
        return None
    return re.sub(r":choice:\d+$", "", ids[0])


def main() -> int:
    mapping_doc = load(MAP_PATH)
    registry = load(REGISTRY_PATH)
    resource_doc = load(RESOURCE_PATH)
    objectives = {row["id"]: row for row in resource_doc.get("objectives", [])}
    outcomes = {
        outcome["id"]: group["objectiveId"]
        for group in registry.get("objectives", [])
        for outcome in group.get("outcomes", [])
    }
    rows = mapping_doc.get("mappings", [])
    errors: list[str] = []
    counts: Counter[str] = Counter()
    unique_questions: set[str] = set()
    unique_rows: set[tuple[str, str, str]] = set()
    verified = 0
    listening_reserve_mappings = 0

    source_cache = {}
    for index, row in enumerate(rows):
        label = f"mappings[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{label}: mapping row is not an object")
            continue
        objective_id = row.get("objectiveId")
        criterion_id = row.get("criterionId")
        resource_id = row.get("resourceId")
        question_key = row.get("questionKey")
        basis = row.get("evidenceBasis")
        if objective_id not in objectives:
            errors.append(f"{label}: unknown objective {objective_id!r}")
            continue
        if criterion_id not in outcomes:
            errors.append(f"{label}: unknown outcome criterion {criterion_id!r}")
            continue
        if outcomes[criterion_id] != objective_id:
            errors.append(f"{label}: criterion {criterion_id} belongs to {outcomes[criterion_id]}, not {objective_id}")
            continue
        parent = objectives[objective_id]
        if resource_id not in (parent.get("resourceIds") or []):
            errors.append(f"{label}: resource {resource_id!r} is outside {objective_id}")
            continue
        if not isinstance(question_key, str) or not question_key.strip():
            errors.append(f"{label}: missing stable questionKey")
            continue
        if not isinstance(basis, str) or not basis.strip():
            errors.append(f"{label}: missing evidenceBasis")
            continue
        triple = (objective_id, criterion_id, question_key)
        if triple in unique_rows:
            errors.append(f"{label}: duplicate objective/criterion/question tuple {triple}")
            continue
        unique_rows.add(triple)
        counts[criterion_id] += 1
        unique_questions.add(question_key)

        rel = parent["resourceFile"]
        if rel not in source_cache:
            source = load(rel)
            source_cache[rel] = source.get(parent["resourceCollection"], [])
        items = source_cache[rel]
        if objective_id == "part5-sentence-completion":
            question = next((item for item in items if item.get("id") == resource_id), None)
            if question is None or question.get("id") != row.get("questionId") or question_key != f"part5:{resource_id}" or row.get("questionIndex") != 0:
                errors.append(f"{label}: Separate Part 5 stable question identity/index does not match {resource_id}")
                continue
        else:
            resource = next((item for item in items if item.get("id") == resource_id), None)
            if resource is None:
                errors.append(f"{label}: missing resource record {resource_id}")
                continue
            if objective_id == "grammar-core":
                questions = resource.get("exercises", [])
            else:
                questions = resource.get("questions", [])
            question = next((item for item in questions if stable_question_key(item) == question_key), None)
            if question is None:
                errors.append(f"{label}: stable question key {question_key!r} not found in {resource_id}")
                continue
            actual_index = questions.index(question)
            if row.get("questionIndex") != actual_index:
                errors.append(f"{label}: questionIndex {row.get('questionIndex')} does not match canonical index {actual_index}")
                continue
            if question.get("id") and row.get("questionId") != question.get("id"):
                errors.append(f"{label}: optional questionId does not match canonical question ID")
                continue
            if objective_id.startswith("listening-") and resource.get("editorialStatus") == "reserve-pending-independent-review":
                listening_reserve_mappings += 1
                errors.append(f"{label}: Listening reserve item {resource_id} is mapped")
                continue
        verified += 1

    declared_counts = mapping_doc.get("mappingCountsByCriterion", {})
    if declared_counts != dict(sorted(counts.items())):
        if declared_counts != dict(counts):
            errors.append("mappingCountsByCriterion does not exactly match the mapping rows")
    if mapping_doc.get("uniqueQuestionCount") != len(unique_questions):
        errors.append(f"uniqueQuestionCount is {mapping_doc.get('uniqueQuestionCount')}, calculated {len(unique_questions)}")

    mapped_criteria = set(counts)
    instrumented_toeic = {
        outcome["id"]
        for group in registry.get("objectives", [])
        if not str(group.get("objectiveId", "")).startswith("foundation-")
        for outcome in group.get("outcomes", [])
        if str(outcome.get("status", "")).startswith("instrumented_")
    }
    if mapped_criteria != instrumented_toeic:
        errors.append("TOEIC instrumented outcome IDs must exactly match criteria with question mappings")
    uninstrumented_toeic = {
        outcome["id"]
        for group in registry.get("objectives", [])
        if not str(group.get("objectiveId", "")).startswith("foundation-")
        for outcome in group.get("outcomes", [])
        if outcome.get("status") == "criteria_defined_not_yet_instrumented"
    }
    if mapped_criteria & uninstrumented_toeic:
        errors.append("an uninstrumented criterion has question mappings")
    if len(instrumented_toeic) != 22:
        errors.append(f"expected 22 TOEIC criteria with a mapping; found {len(instrumented_toeic)}")
    if len(uninstrumented_toeic) != 5:
        errors.append(f"expected 5 TOEIC criteria to remain uninstrumented; found {len(uninstrumented_toeic)}")
    if listening_reserve_mappings:
        errors.append(f"{listening_reserve_mappings} Listening reserve mappings were detected")

    part7 = next((row for row in resource_doc["objectives"] if row["id"] == "reading-part-7"), {})
    part5 = next((row for row in resource_doc["objectives"] if row["id"] == "part5-sentence-completion"), {})
    if "requires_second_review" not in str(part7.get("reviewState", "")):
        errors.append("Reading Part 7 second-review gate is not present")
    if "pending_independent_review" not in str(part5.get("reviewState", "")):
        errors.append("Separate Part 5 independent-review gate is not present")

    total_outcomes = sum(len(group.get("outcomes", [])) for group in registry.get("objectives", []))
    total_instrumented = sum(
        1 for group in registry.get("objectives", [])
        for outcome in group.get("outcomes", [])
        if str(outcome.get("status", "")).startswith("instrumented_")
    )
    if errors:
        print("\n".join(f"FAIL: {error}" for error in errors))
        return 1
    print(
        f"PASS: {verified}/{len(rows)} question-to-criterion links match canonical bank IDs; "
        f"{len(unique_questions)} unique stable question IDs; {len(mapped_criteria)}/27 TOEIC criteria mapped; "
        f"{total_instrumented}/{total_outcomes} total criteria have a local evidence path; "
        f"{len(uninstrumented_toeic)} TOEIC criteria deliberately remain uninstrumented; "
        "0 Listening reserve items mapped."
    )
    print("PASS: Part 7 second-review gate and Separate Part 5 independent-review gate remain active.")
    print("NOTE: Mapping inventory is not learner practice evidence, editorial approval, CEFR/ETS mastery or TOEIC score readiness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
