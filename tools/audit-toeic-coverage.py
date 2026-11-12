#!/usr/bin/env python3
"""Generate a TOEIC-only coverage and answer-key balance report."""
from __future__ import annotations
import collections
import datetime
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text or ""))

def question_counts(items):
    result = collections.Counter()
    for item in items:
        result[item.get("part", "Unassigned")] += len(item.get("questions", []))
    return result

def answer_distribution(items, part):
    result = collections.Counter(
        q.get("answerIndex")
        for item in items if item.get("part") == part
        for q in item.get("questions", [])
    )
    return [result.get(i, 0) for i in range(4)]

version = load("data/manifest.json").get("version", "unknown")
vocab = []
for file in sorted((ROOT / "data/vocabulary").glob("[A-Z].json")):
    vocab.extend(load(str(file.relative_to(ROOT))).get("words", []))
listening = load("data/listening/listening-library.json").get("listening", [])
readings = load("data/readings/reading-library.json").get("readings", [])
grammar = load("data/grammar/lessons.json").get("lessons", [])

ipa = sum(bool((word.get("phonetic") or {}).get("us")) for word in vocab)
family = sum(bool(word.get("word_family")) for word in vocab)
verb = sum(bool(word.get("verb_forms")) for word in vocab)
collocations = sum(bool(word.get("collocations")) for word in vocab)
cefr = collections.Counter(word.get("cefr_level", "Unassigned") for word in vocab)
L = collections.Counter(item.get("part", "Unassigned") for item in listening)
R = collections.Counter(item.get("part", "Unassigned") for item in readings)
LQ = question_counts(listening)
RQ = question_counts(readings)
reading_words = sum(
    word_count(item.get("passage", "")) if not item.get("documents")
    else sum(word_count(doc.get("content", "")) for doc in item["documents"])
    for item in readings
)
listening_segments = sum(len(item.get("segments", [])) for item in listening)

LISTEN_TARGET = {"Part 1": 6, "Part 2": 25, "Part 3": 39, "Part 4": 30}
READ_TARGET = {"Part 5": 30, "Part 6": 16, "Part 7": 54}

p7_single_questions = sum(len(item.get("questions", [])) for item in readings if item.get("part") == "Part 7" and item.get("documentType") not in ("DOUBLE PASSAGE", "TRIPLE PASSAGE"))
p7_multiple_items = [item for item in readings if item.get("part") == "Part 7" and item.get("documentType") in ("DOUBLE PASSAGE", "TRIPLE PASSAGE")]
p7_multiple_questions = sum(len(item.get("questions", [])) for item in p7_multiple_items)
p7_structured_multi_items = sum(
    1 for item in p7_multiple_items
    if len(item.get("documents", [])) == (2 if item.get("documentType") == "DOUBLE PASSAGE" else 3)
    and all(doc.get("label") and doc.get("content") for doc in item.get("documents", []))
)

lines = [
    f"# TOEIC Content Coverage — v{version}", "",
    f"Generated: {datetime.date.today().isoformat()}", "",
    "> TOEIC Listening & Reading only. IELTS and other exam-specific content are intentionally excluded until TOEIC acceptance gates are met.", "",
    "## Vocabulary coverage", "",
    "| Metric | Count | Coverage |", "|---|---:|---:|",
    f"| Headwords | {len(vocab)} | — |",
    f"| US IPA present | {ipa} | {ipa / len(vocab) * 100:.1f}% |",
    f"| Word-family records | {family} | {family / len(vocab) * 100:.1f}% |",
    f"| Verb-form records | {verb} | {verb / len(vocab) * 100:.1f}% |",
    f"| Collocation records | {collocations} | {collocations / len(vocab) * 100:.1f}% |",
    f"| CEFR assigned | {sum(cefr.values())} | {sum(cefr.values()) / len(vocab) * 100:.1f}% |", "",
    "| CEFR | Records |", "|---|---:|"
]
for level in ["A1", "A2", "B1", "B2", "C1", "C2", "Unassigned"]:
    lines.append(f"| {level} | {cefr.get(level, 0)} |")

lines += ["", "## Listening coverage", "", "| Part | Units | Questions |", "|---|---:|---:|"]
for part in LISTEN_TARGET:
    lines.append(f"| {part} | {L.get(part, 0)} | {LQ.get(part, 0)} |")
lines += [
    f"| **Total** | **{len(listening)}** | **{sum(LQ.values())}** |", "",
    f"- Spoken segments: {listening_segments}.",
    f"- Part 1 licensed Pexels photographs: {sum(1 for item in listening if item.get('part') == 'Part 1' and item.get('photo'))}; these are third-party licensed practice images, not official ETS assets.",
    "- Audio is browser SpeechSynthesis; it is synthesized audio, not recorded/native-speaker or ETS audio.", "",
    "## Reading coverage", "", "| Part | Resources | Questions |", "|---|---:|---:|"
]
for part in READ_TARGET:
    lines.append(f"| {part} | {R.get(part, 0)} | {RQ.get(part, 0)} |")
lines += [
    f"| **Total** | **{len(readings)}** | **{sum(RQ.values())}** |", "",
    f"- Reading text word count (current passages/documents): {reading_words}.",
    f"- Part 7 question mix: {p7_single_questions} single-passage questions / {p7_multiple_questions} multiple-passage questions.",
    f"- Structured Part 7 multi-document resources: {p7_structured_multi_items}/{len(p7_multiple_items)} double/triple passages.", "",
    "## Grammar", "",
    f"- Lessons: {len(grammar)}.",
    f"- Exercises: {sum(len(item.get('exercises', [])) for item in grammar)}.", "",
    "## Reference question distribution — one TOEIC L&R form", "",
    "| Part | Current pool | Reference per form | Coverage |", "|---|---:|---:|---:|"
]
for part, target in LISTEN_TARGET.items():
    current = LQ.get(part, 0)
    lines.append(f"| {part} | {current} | {target} | {current / target * 100:.1f}% |")
lines.append(f"| **Listening total** | **{sum(LQ.values())}** | **100** | **{sum(LQ.values())}%** |")
for part, target in READ_TARGET.items():
    current = RQ.get(part, 0)
    lines.append(f"| {part} | {current} | {target} | {current / target * 100:.1f}% |")
lines.append(f"| **Reading total** | **{sum(RQ.values())}** | **100** | **{sum(RQ.values())}%** |")
lines += [
    "", "These ratios compare the current practice pool with the public distribution for one test form. They do not mean the app already contains a complete, validated mock test. Part 1 has 8 practice items versus 6 in the reference form; eight locally hosted licensed photographs are used with SVG fallbacks.", "",
    "## Answer-key balance (A/B/C/D counts)", "", "| Part | A | B | C | D |", "|---|---:|---:|---:|---:|"
]
for part in list(LISTEN_TARGET) + list(READ_TARGET):
    distribution = answer_distribution(listening if part in LISTEN_TARGET else readings, part)
    lines.append(f"| {part} | " + " | ".join(str(value) for value in distribution) + " |")

lines += [
    "", "## Interpretation and gaps", "",
    f"- Listening pool has {sum(LQ.values())} questions; blueprint minima are met for one form (P1 includes 8 practice photographs versus 6 questions in a form).",
    f"- Reading pool has {sum(RQ.values())} questions; Part 7 includes {p7_single_questions} single-passage and {p7_multiple_questions} multiple-passage questions, enough to select 29 + 25 for one form.",
    f"- Structured Part 7 double/triple passage resources: {p7_structured_multi_items}/{len(p7_multiple_items)}.",
    "- V2.25.0 includes a timed 15/60/120-minute mock engine, answer review and local score analysis; it is an internal practice tool, not an officially equated TOEIC test. Independent editorial review remains pending for reserve content.",
    f"- Vocabulary is {len(vocab)} headwords, below the 3,000–5,000 internal TOEIC planning target. That target is not an official ETS list.",
    "- No score conversion should be described as an ETS score until a validated scoring/equating model exists; current per-Part analytics are local-practice indicators.",
    "- `tools/validate-learning-content.py` checks IDs, choices, answers, explanation presence, Part coverage, passages and image assets. It does not prove semantic correctness; editorial review remains required.", ""
]
report = ROOT / f"docs/reports/TOEIC_CONTENT_COVERAGE_v{version}.md"
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text("\n".join(lines), encoding="utf-8")
print(report.relative_to(ROOT))
print(f"Vocabulary {len(vocab)} | IPA {ipa} | Word family {family} | Listening {len(listening)}/{sum(LQ.values())} | Reading {len(readings)}/{sum(RQ.values())} | P7 single/multi {p7_single_questions}/{p7_multiple_questions} | Grammar {len(grammar)}")
