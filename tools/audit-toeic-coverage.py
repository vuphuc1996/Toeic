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

lines = [
    "# TOEIC Content Coverage — v2.11.0", "",
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
    f"- Part 1 original SVG illustrations: {sum(1 for item in listening if item.get('part') == 'Part 1' and item.get('image'))}; they are illustrations, not realistic photographs or official ETS assets.",
    "- Audio is browser SpeechSynthesis; it is synthesized audio, not recorded/native-speaker or ETS audio.", "",
    "## Reading coverage", "", "| Part | Resources | Questions |", "|---|---:|---:|"
]
for part in READ_TARGET:
    lines.append(f"| {part} | {R.get(part, 0)} | {RQ.get(part, 0)} |")
lines += [
    f"| **Total** | **{len(readings)}** | **{sum(RQ.values())}** |", "",
    f"- Reading text word count (current passages/documents): {reading_words}.", "",
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
    "", "These ratios compare the current practice pool with the public distribution for one test form. They do not mean the app already contains a complete, validated mock test. Part 1 has 8 practice items versus 6 in the reference form, but the images are illustrations and need photo-quality improvement.", "",
    "## Answer-key balance (A/B/C/D counts)", "", "| Part | A | B | C | D |", "|---|---:|---:|---:|---:|"
]
for part in list(LISTEN_TARGET) + list(READ_TARGET):
    distribution = answer_distribution(listening if part in LISTEN_TARGET else readings, part)
    lines.append(f"| {part} | " + " | ".join(str(value) for value in distribution) + " |")

lines += [
    "", "## Interpretation and gaps", "",
    "- Current volume is 36 Listening questions / 100 reference questions and 77 Reading questions / 100 reference questions; it is not enough for a full test form.",
    "- Listening P2–P4 remain the largest immediate volume gaps. P1 contains 8 SVG illustration sets, not photographic source material.",
    "- Reading Part 7 has the closest question-count coverage, but needs continued passage diversity, cross-document reasoning and editorial answer review.",
    "- Vocabulary is 928 headwords, below the 3,000–5,000 internal TOEIC planning target. That target is not an official ETS list.",
    "- No score conversion should be described as an ETS score until a validated scoring/equating model exists; current per-Part analytics are local-practice indicators.",
    "- `tools/validate-learning-content.py` checks IDs, choices, answers, explanation presence, Part coverage, passages and image assets. It does not prove semantic correctness; editorial review remains required.", ""
]
report = ROOT / "docs/reports/TOEIC_CONTENT_COVERAGE_v2.11.0.md"
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text("\n".join(lines), encoding="utf-8")
print(report.relative_to(ROOT))
print(f"Vocabulary {len(vocab)} | IPA {ipa} | Word family {family} | Listening {len(listening)}/{sum(LQ.values())} | Reading {len(readings)}/{sum(RQ.values())} | Grammar {len(grammar)}")
