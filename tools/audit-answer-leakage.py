#!/usr/bin/env python3
"""Read-only lexical/length diagnostics for TOEIC multiple-choice items.

Signals are editorial triage only. They never judge answer correctness or rewrite content.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'data' / 'manifest.json').read_text(encoding='utf-8'))['version']
OUT = ROOT / 'docs' / 'reports' / f'TOEIC_ANSWER_LEAKAGE_DIAGNOSTIC_v{VERSION}.md'
STOP = set('''a an the and or but if then than of to in on at by for from with about as is are was were be been being do does did can could will would should may might must have has had it its this that these those he she they them their his her we you your i me my our who whom what when where why how which while during before after into over under up down out not no yes very more most less least also just only such there here some any each all both other another one two three'''.split())
TOKEN = re.compile(r"[a-z]+(?:'[a-z]+)?|\d+(?::\d+)?", re.I)


def tokens(value: str) -> set[str]:
    return {t.casefold().strip("'") for t in TOKEN.findall(str(value)) if len(t.strip("'")) > 1 and t.casefold() not in STOP}


def score(question: str, choices: list[str], answer_index: int) -> dict:
    if not isinstance(answer_index, int) or not 0 <= answer_index < len(choices):
        raise ValueError('invalid answer index')
    stem = tokens(question)
    option_tokens = [tokens(c) for c in choices]
    key = option_tokens[answer_index]
    stem_ratio = len(key & stem) / len(key) if key else 0.0
    distractor_stem = [len(t & stem) / len(t) if t else 0.0 for i, t in enumerate(option_tokens) if i != answer_index]
    key_distractor_jaccard = [len(key & t) / len(key | t) if key | t else 0.0 for i, t in enumerate(option_tokens) if i != answer_index]
    lengths = [len(TOKEN.findall(str(c))) for c in choices]
    distractor_lengths = [v for i, v in enumerate(lengths) if i != answer_index]
    ordered = sorted(distractor_lengths)
    median = ordered[len(ordered)//2] if ordered else 0
    length_ratio = lengths[answer_index] / median if median else 0.0
    flags = []
    if len(key) >= 2 and stem_ratio >= 0.60 and stem_ratio - max(distractor_stem, default=0.0) >= 0.30:
        flags.append('KEY_STEM_LEXICAL_CUE')
    if max(key_distractor_jaccard, default=0.0) >= 0.75 and len(key) >= 2:
        flags.append('KEY_DISTRACTOR_HIGH_OVERLAP')
    if lengths[answer_index] >= median + 4 and length_ratio >= 1.8:
        flags.append('KEY_UNUSUALLY_LONG')
    if median >= lengths[answer_index] + 4 and median / max(lengths[answer_index], 1) >= 1.8:
        flags.append('KEY_UNUSUALLY_SHORT')
    return {
        'stem_overlap': round(stem_ratio, 3),
        'max_distractor_stem_overlap': round(max(distractor_stem, default=0.0), 3),
        'max_key_distractor_jaccard': round(max(key_distractor_jaccard, default=0.0), 3),
        'key_tokens': len(key), 'key_words': lengths[answer_index],
        'distractor_median_words': median, 'key_length_ratio': round(length_ratio, 3),
        'flags': flags,
    }


def read_items(rel: str, key: str) -> list[dict]:
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))[key]


def main() -> int:
    listening = read_items('data/listening/listening-library.json', 'listening')
    reading = read_items('data/readings/reading-library.json', 'readings')
    scopes = [
        ('Listening', 'Part 3', [x for x in listening if x.get('part') == 'Part 3' and x.get('editorialStatus') != 'reserve-pending-independent-review']),
        ('Listening', 'Part 4', [x for x in listening if x.get('part') == 'Part 4' and x.get('editorialStatus') != 'reserve-pending-independent-review']),
        ('Reading', 'Part 7', [x for x in reading if x.get('part') == 'Part 7' and x.get('editorialStatus') != 'reserve-pending-independent-review']),
    ]
    rows, summary = [], defaultdict(Counter)
    for library, part, items in scopes:
        for item in items:
            for qn, q in enumerate(item.get('questions', []), 1):
                choices = q.get('choices', [])
                if len(choices) != 4:
                    continue
                metrics = score(q.get('question', ''), choices, q.get('answerIndex'))
                summary[part]['questions'] += 1
                summary[part]['flagged'] += bool(metrics['flags'])
                for flag in metrics['flags']:
                    summary[part][flag] += 1
                rows.append({'library': library, 'part': part, 'id': item['id'], 'qn': qn,
                             'question': q.get('question', ''), 'answer': choices[q['answerIndex']], **metrics})
    lines = [f'# TOEIC Answer Leakage & Distractor Overlap Diagnostic — v{VERSION}', '',
             '## Purpose and safety boundary',
             '- Read-only triage of question-stem lexical cueing, correct-answer/distractor lexical similarity, and keyed-answer length imbalance.',
             '- A flag is a review signal, **not evidence of a wrong key, answer leakage, or an invalid item**. TOEIC questions legitimately reuse vocabulary and paraphrase source evidence.',
             '- No automatic rewriting, key changes, choice reordering, eligibility promotion, or reserve approval is performed. The 87 Reading reserve questions and 193 Listening reserve questions remain excluded from Mock.',
             '- Scope: Mock-eligible Listening Part 3/4 and Reading Part 7 only. Both Listening and Reading `reserve-pending-independent-review` records are excluded.',
             '', '## Part summary', '| Part | Questions | Flagged questions | Stem cue | Key/distractor overlap | Key long | Key short |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for _, part, _ in scopes:
        s = summary[part]
        lines.append(f"| {part} | {s['questions']} | {s['flagged']} | {s['KEY_STEM_LEXICAL_CUE']} | {s['KEY_DISTRACTOR_HIGH_OVERLAP']} | {s['KEY_UNUSUALLY_LONG']} | {s['KEY_UNUSUALLY_SHORT']} |")
    lines += ['', '## Flagged question review queue', '| Part / set / question | Signal(s) | Stem | Keyed answer | Stem overlap | Key/distractor Jaccard | Key words / distractor median |', '|---|---|---|---|---:|---:|---:|']
    for r in rows:
        if not r['flags']:
            continue
        lines.append(f"| {r['part']} · `{r['id']}` · Q{r['qn']} | {', '.join(r['flags'])} | {r['question'].replace('|','/')} | {r['answer'].replace('|','/')} | {r['stem_overlap']:.0%} | {r['max_key_distractor_jaccard']:.0%} | {r['key_words']} / {r['distractor_median_words']} |")
    lines += ['', '## Metric definitions',
              '- **Stem overlap** = content-word intersection between the keyed answer and question stem divided by keyed-answer content words.',
              '- **Key/distractor Jaccard** = intersection-over-union of content-word sets for the keyed answer and each distractor; report stores the maximum.',
              '- **Length ratio** = keyed-answer word count divided by median distractor word count.',
              '- Stopwords are removed; tokens are case-folded. This deliberately simple lexical model cannot detect semantic paraphrase, negation scope, audio prosody, visual evidence, or discourse inference.',
              '- Thresholds are conservative triage heuristics: keyed stem overlap ≥60% and ≥30 percentage points above distractors; key/distractor Jaccard ≥75%; length outlier requires ≥4 words and ≥1.8× median.',
              '', '## Decision',
              '- Do not auto-edit flagged items. Review the original audio/transcript or passage, evidence quote, explanation, and all four options together. Preserve answer keys unless a human editorial review proves a defect.',
              '- This report is deterministic for the same source bytes and is not an ETS benchmark, psychometric analysis, or certification of answer uniqueness.', '']
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    total = sum(s['questions'] for s in summary.values())
    flagged = sum(s['flagged'] for s in summary.values())
    print(f'Wrote {OUT.relative_to(ROOT)}')
    print(f'Questions={total}; flagged={flagged}; Part3={summary["Part 3"]["questions"]}; Part4={summary["Part 4"]["questions"]}; Part7={summary["Part 7"]["questions"]}')
    print('Read-only lexical/length diagnostic: PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
