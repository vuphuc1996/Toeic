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


def normalize_source_label(value: object) -> str | None:
    """Normalize source labels without coercing invalid data into valid labels."""
    if not isinstance(value, str):
        return None
    normalized = " ".join(value.split())
    return normalized.casefold() or None


def evidence_basis_names_sources(evidence_basis: str, source_labels: list[str]) -> bool:
    """Match each source label as a whole phrase, not a partial substring."""
    if not isinstance(evidence_basis, str):
        return False
    normalized_basis = " ".join(evidence_basis.split())
    for source_label in source_labels:
        normalized_label = " ".join(source_label.split())
        if not normalized_label or re.search(
            rf"(?<!\w){re.escape(normalized_label)}(?!\w)",
            normalized_basis,
            flags=re.IGNORECASE,
        ) is None:
            return False
    return True


def validate_cross_document_evidence(resource: dict, question: dict) -> list[str]:
    """Require unambiguous, reviewed, multi-source evidence for a Part 7 mapping."""
    if not isinstance(resource, dict) or not isinstance(question, dict):
        return ["Part 7 cross-document resource and question must be objects"]
    errors: list[str] = []
    if resource.get("editorialStatus") != "internal-editorial-reviewed":
        errors.append("Part 7 cross-document mapping requires an internal-editorial-reviewed resource")

    documents = resource.get("documents")
    if not isinstance(documents, list) or not documents:
        return errors + ["Part 7 cross-document resource must declare a non-empty documents list"]

    document_by_label: dict[str, dict] = {}
    for index, document in enumerate(documents):
        if not isinstance(document, dict):
            errors.append(f"Part 7 document[{index}] must be an object")
            continue
        normalized_label = normalize_source_label(document.get("label"))
        if normalized_label is None:
            errors.append(f"Part 7 document[{index}] must have a non-empty string label")
            continue
        if normalized_label in document_by_label:
            errors.append(f"Part 7 resource has duplicate document label {document.get('label')!r}")
            continue
        document_by_label[normalized_label] = document
    if errors:
        return errors

    evidence = question.get("evidence")
    if not isinstance(evidence, dict):
        return ["Part 7 cross-document question is missing its evidence object"]
    labels, quotes = evidence.get("sourceLabels"), evidence.get("quotes")
    if not isinstance(labels, list) or len(labels) < 2:
        return ["Part 7 cross-document evidence must cite at least two distinct sourceLabels"]
    normalized_labels = [normalize_source_label(label) for label in labels]
    if any(label is None for label in normalized_labels):
        return ["Part 7 sourceLabels must contain only non-empty strings"]
    if len(set(normalized_labels)) != len(normalized_labels):
        return ["Part 7 cross-document evidence must not repeat a sourceLabel"]
    if not isinstance(quotes, list) or len(quotes) != len(labels):
        return ["Part 7 cross-document evidence requires one source quote per sourceLabel"]
    if any(not isinstance(quote, str) or not quote.strip() for quote in quotes):
        return ["Part 7 source quotes must contain only non-empty strings"]

    for label, normalized_label, quote in zip(labels, normalized_labels, quotes):
        document = document_by_label.get(normalized_label)
        if document is None:
            errors.append(f"Part 7 evidence sourceLabel {label!r} is not a declared document")
            continue
        quote_text = " ".join(quote.split()).casefold()
        content = document.get("content")
        content_text = " ".join(content.split()).casefold() if isinstance(content, str) else ""
        if not quote_text or quote_text not in content_text:
            errors.append(f"Part 7 evidence quote for {label!r} does not match that document")
    return errors


def listening_prompt_text(resource: dict) -> str:
    """Return the canonical spoken prompt represented by Part 2 segments."""
    segments = resource.get("segments")
    if not isinstance(segments, list):
        return ""
    fragments = []
    for segment in segments:
        if isinstance(segment, str):
            fragments.append(segment)
        elif isinstance(segment, dict):
            for key in ("text", "audioText", "en", "transcript", "content"):
                if isinstance(segment.get(key), str) and segment[key].strip():
                    fragments.append(segment[key])
                    break
    return " ".join(fragments)


def contains_whole_lexical_cue(text: str, cue: str) -> bool:
    """Check for a repeated cue as a whole token or phrase."""
    if not isinstance(text, str) or not isinstance(cue, str) or not cue.strip():
        return False
    return re.search(
        rf"(?<!\w){re.escape(cue.strip())}(?!\w)",
        text,
        flags=re.IGNORECASE,
    ) is not None


def normalize_evidence_text(value: str) -> str:
    return " ".join(value.split()).casefold()


def validate_part2_distractor_evidence(resource: dict, question: dict, row: dict) -> list[str]:
    """Require exact source-backed prompt, wrong option, repeated cue and mismatch note."""
    if not all(isinstance(value, dict) for value in (resource, question, row)):
        return ["Part 2 lexical-trap evidence requires resource, question and mapping objects"]

    errors: list[str] = []
    prompt = listening_prompt_text(resource)
    prompt_quote = row.get("promptQuote")
    if not isinstance(prompt_quote, str) or not prompt_quote.strip():
        errors.append("Part 2 lexical-trap mapping requires a non-empty promptQuote")
    elif normalize_evidence_text(prompt_quote) != normalize_evidence_text(prompt):
        errors.append("Part 2 promptQuote must exactly match the canonical audio segments")

    choices = question.get("choices")
    answer_index = question.get("answerIndex")
    distractor_index = row.get("distractorChoiceIndex")
    if not isinstance(choices, list) or not all(isinstance(choice, str) for choice in choices):
        errors.append("Part 2 lexical-trap question must have string choices")
    elif (
        not isinstance(distractor_index, int) or isinstance(distractor_index, bool)
        or distractor_index < 0 or distractor_index >= len(choices)
    ):
        errors.append("Part 2 distractorChoiceIndex is outside the canonical choices")
    elif distractor_index == answer_index:
        errors.append("Part 2 lexical-trap distractorChoiceIndex must not select the answer key")
    else:
        canonical_distractor = choices[distractor_index]
        distractor_quote = row.get("distractorQuote")
        if distractor_quote != canonical_distractor:
            errors.append("Part 2 distractorQuote does not match the selected canonical wrong choice")
        cue = row.get("lexicalCue")
        if not isinstance(cue, str) or not cue.strip():
            errors.append("Part 2 lexical-trap mapping requires a non-empty lexicalCue")
        else:
            if not contains_whole_lexical_cue(prompt_quote if isinstance(prompt_quote, str) else "", cue):
                errors.append("Part 2 lexicalCue does not appear in promptQuote")
            if not contains_whole_lexical_cue(distractor_quote if isinstance(distractor_quote, str) else "", cue):
                errors.append("Part 2 lexicalCue does not appear in distractorQuote")
        mismatch = row.get("responseMismatch")
        if not isinstance(mismatch, str) or not mismatch.strip():
            errors.append("Part 2 lexical-trap mapping requires a responseMismatch explanation")
        basis = row.get("evidenceBasis")
        if not isinstance(basis, str) or not basis.strip():
            errors.append("Part 2 lexical-trap mapping requires an evidenceBasis")
        else:
            if isinstance(distractor_quote, str) and distractor_quote not in basis:
                errors.append("Part 2 evidenceBasis must reproduce the exact distractorQuote")
            if isinstance(cue, str) and cue.casefold() not in basis.casefold():
                errors.append("Part 2 evidenceBasis must identify the repeated lexicalCue")
            if isinstance(mismatch, str) and mismatch and mismatch not in basis:
                errors.append("Part 2 evidenceBasis must include the responseMismatch explanation")
    return errors


def _normalized_source_text(value: str) -> str:
    return " ".join(value.split()).casefold()


def validate_part4_inference_evidence(resource: dict, question: dict, row: dict) -> list[str]:
    """Require a non-reserve Part 4 item with exact audio evidence and action-inference rationale."""
    errors: list[str] = []
    if not all(isinstance(value, dict) for value in (resource, question, row)):
        return ["Part 4 inference evidence requires resource, question and mapping objects"]
    if resource.get("part") != "Part 4":
        errors.append("Part 4 inference evidence must belong to a Part 4 resource")
    if resource.get("editorialStatus") == "reserve-pending-independent-review":
        errors.append("Part 4 inference evidence must not use a reserve resource")
    prompt = listening_prompt_text(resource)
    quote = row.get("evidenceQuote")
    if not isinstance(quote, str) or not quote.strip():
        errors.append("Part 4 inference mapping requires a non-empty evidenceQuote")
    elif _normalized_source_text(quote) not in _normalized_source_text(prompt):
        errors.append("Part 4 evidenceQuote does not match the canonical audio segments")
    stem = question.get("question")
    if not isinstance(stem, str) or not re.search(r"\b(most likely|should .* next|what .* do next|need to)\b", stem, re.I):
        errors.append("Part 4 inference mapping must ask a next-step or likely-action question")
    allowed_types = {"sequence", "location_after_change", "access_precondition", "prelaunch_action", "post_event_action", "caller_next_step", "safety_response", "expected_follow_up", "schedule_adaptation", "procedure_exception"}
    inference_type = row.get("inferenceType")
    if inference_type not in allowed_types:
        errors.append("Part 4 inferenceType is missing or unsupported")
    rationale = row.get("inferenceRationale")
    if not isinstance(rationale, str) or not rationale.strip():
        errors.append("Part 4 inference mapping requires an inferenceRationale")
    choices = question.get("choices")
    answer_index = question.get("answerIndex")
    if not isinstance(choices, list) or not all(isinstance(choice, str) for choice in choices):
        errors.append("Part 4 inference question must have string choices")
    elif not isinstance(answer_index, int) or isinstance(answer_index, bool) or answer_index < 0 or answer_index >= len(choices):
        errors.append("Part 4 inference answerIndex is outside the canonical choices")
    else:
        answer_quote = row.get("answerQuote")
        if answer_quote != choices[answer_index]:
            errors.append("Part 4 answerQuote does not match the canonical answer choice")
        basis = row.get("evidenceBasis")
        if not isinstance(basis, str) or not basis.strip():
            errors.append("Part 4 inference mapping requires an evidenceBasis")
        else:
            if isinstance(quote, str) and quote not in basis:
                errors.append("Part 4 evidenceBasis must reproduce the exact audio evidenceQuote")
            if isinstance(answer_quote, str) and answer_quote not in basis:
                errors.append("Part 4 evidenceBasis must identify the canonical answer choice")
            if isinstance(rationale, str) and rationale and rationale not in basis:
                errors.append("Part 4 evidenceBasis must include the inferenceRationale")
    return errors


def validate_part6_discourse_evidence(resource: dict, question: dict, row: dict) -> list[str]:
    """Require exact passage evidence from an internally reviewed Part 6 resource."""
    errors: list[str] = []
    if not all(isinstance(value, dict) for value in (resource, question, row)):
        return ["Part 6 discourse evidence requires resource, question and mapping objects"]
    if resource.get("editorialStatus") != "internal-editorial-reviewed":
        errors.append("Part 6 discourse mapping requires an internal-editorial-reviewed resource")
    passage = resource.get("passage")
    quote = row.get("evidenceQuote")
    if not isinstance(passage, str) or not passage.strip():
        errors.append("Part 6 discourse resource requires a non-empty passage")
    elif not isinstance(quote, str) or not quote.strip():
        errors.append("Part 6 discourse mapping requires a non-empty evidenceQuote")
    elif _normalized_source_text(quote) not in _normalized_source_text(passage):
        errors.append("Part 6 evidenceQuote does not match the canonical passage")
    stem = question.get("question")
    if not isinstance(stem, str) or not re.search(r"\bblank\s*\(\d+\)", stem, re.I):
        errors.append("Part 6 discourse mapping must reference a canonical blank question")
    allowed_functions = {"temporal-sequence", "paragraph-continuation", "additive-link", "contrast", "referential-link", "sentence-continuation", "deadline-sequence"}
    function = row.get("discourseFunction")
    if function not in allowed_functions:
        errors.append("Part 6 discourseFunction is missing or unsupported")
    rationale = row.get("discourseRationale")
    if not isinstance(rationale, str) or not rationale.strip():
        errors.append("Part 6 discourse mapping requires a discourseRationale")
    choices = question.get("choices")
    answer_index = question.get("answerIndex")
    if not isinstance(choices, list) or not all(isinstance(choice, str) for choice in choices):
        errors.append("Part 6 discourse question must have string choices")
    elif not isinstance(answer_index, int) or isinstance(answer_index, bool) or answer_index < 0 or answer_index >= len(choices):
        errors.append("Part 6 discourse answerIndex is outside the canonical choices")
    else:
        correct_quote = row.get("correctChoiceQuote")
        if correct_quote != choices[answer_index]:
            errors.append("Part 6 correctChoiceQuote does not match the canonical answer choice")
        basis = row.get("evidenceBasis")
        if not isinstance(basis, str) or not basis.strip():
            errors.append("Part 6 discourse mapping requires an evidenceBasis")
        else:
            if isinstance(quote, str) and quote not in basis:
                errors.append("Part 6 evidenceBasis must reproduce the exact passage evidenceQuote")
            if isinstance(correct_quote, str) and correct_quote not in basis:
                errors.append("Part 6 evidenceBasis must identify the canonical answer choice")
            if isinstance(function, str) and function not in basis:
                errors.append("Part 6 evidenceBasis must name the discourseFunction")
            if isinstance(rationale, str) and rationale and rationale not in basis:
                errors.append("Part 6 evidenceBasis must include the discourseRationale")
    return errors

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
    cross_document_verified = 0
    part2_lexical_trap_verified = 0
    part4_inference_verified = 0
    part6_discourse_verified = 0

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
            actual_index = items.index(question) if question is not None else -1
            if question is None or question.get("id") != row.get("questionId") or question_key != f"part5:{resource_id}" or row.get("questionIndex") != actual_index:
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
            if criterion_id == "reading-part-7-cross-document-link":
                evidence_errors = validate_cross_document_evidence(resource, question)
                if evidence_errors:
                    errors.extend(f"{label}: {error}" for error in evidence_errors)
                    continue
                labels = question.get("evidence", {}).get("sourceLabels", [])
                if not evidence_basis_names_sources(basis, labels):
                    errors.append(f"{label}: evidenceBasis must name every declared cross-document sourceLabel as a whole phrase")
                    continue
                cross_document_verified += 1
            if criterion_id == "listening-part-2-distractor-resistance":
                lexical_errors = validate_part2_distractor_evidence(resource, question, row)
                if lexical_errors:
                    errors.extend(f"{label}: {error}" for error in lexical_errors)
                    continue
                part2_lexical_trap_verified += 1
            if criterion_id == "listening-part-4-inference-action":
                inference_errors = validate_part4_inference_evidence(resource, question, row)
                if inference_errors:
                    errors.extend(f"{label}: {error}" for error in inference_errors)
                    continue
                part4_inference_verified += 1
            if criterion_id == "reading-part-6-discourse-purpose":
                discourse_errors = validate_part6_discourse_evidence(resource, question, row)
                if discourse_errors:
                    errors.extend(f"{label}: {error}" for error in discourse_errors)
                    continue
                part6_discourse_verified += 1
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
    if len(instrumented_toeic) != 25:
        errors.append(f"expected 25 TOEIC criteria with a mapping; found {len(instrumented_toeic)}")
    if len(uninstrumented_toeic) != 2:
        errors.append(f"expected 2 TOEIC criteria to remain uninstrumented; found {len(uninstrumented_toeic)}")
    if listening_reserve_mappings:
        errors.append(f"{listening_reserve_mappings} Listening reserve mappings were detected")
    if counts.get("listening-part-2-distractor-resistance", 0) < 10:
        errors.append("Part 2 distractor-resistance criterion must retain at least 10 unique mapped questions")
    if part2_lexical_trap_verified != counts.get("listening-part-2-distractor-resistance", 0):
        errors.append("every Part 2 distractor-resistance mapping must pass exact audio/distractor evidence validation")
    if counts.get("listening-part-4-inference-action", 0) < 10:
        errors.append("Part 4 inference/action criterion must retain at least 10 unique mapped questions")
    if part4_inference_verified != counts.get("listening-part-4-inference-action", 0):
        errors.append("every Part 4 inference/action mapping must pass exact audio evidence validation")
    if counts.get("reading-part-6-discourse-purpose", 0) < 10:
        errors.append("Part 6 discourse-purpose criterion must retain at least 10 unique mapped questions")
    if part6_discourse_verified != counts.get("reading-part-6-discourse-purpose", 0):
        errors.append("every Part 6 discourse-purpose mapping must pass reviewed passage evidence validation")

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
    print(f"PASS: {cross_document_verified} Part 7 cross-document mappings have internally reviewed, two-source quote evidence.")
    print(f"PASS: {part2_lexical_trap_verified} Part 2 lexical-trap mappings have exact audio, wrong-choice, repeated-cue and mismatch evidence.")
    print(f"PASS: {part4_inference_verified} Part 4 next-step/action mappings have exact audio quote and inference rationale evidence.")
    print(f"PASS: {part6_discourse_verified} Part 6 discourse mappings have internally reviewed passage quote, correct-choice and relation evidence.")
    print("PASS: Part 7 second-review gate and Separate Part 5 independent-review gate remain active.")
    print("NOTE: Mapping inventory is not learner practice evidence, editorial approval, CEFR/ETS mastery or TOEIC score readiness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
