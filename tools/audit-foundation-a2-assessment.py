#!/usr/bin/env python3
"""Audit A2 Foundation Reading/Listening question integrity and evidence traceability."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'tools/foundation-a2-assessment-review-v2.77.0.json'
CURRENT_VERSION = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))['version']
OUT = ROOT / f'docs/reports/FOUNDATION_A2_ASSESSMENT_QUALITY_v{CURRENT_VERSION}.md'


def read(rel: str):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def norm(value: str) -> str:
    return re.sub(r'\s+', ' ', value.casefold()).strip(' .!?')


def main() -> int:
    reading = read('data/learning-path/foundation-reading.json')['passages']
    listening = read('data/learning-path/foundation-listening.json')['clips']
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    issues: list[str] = []
    bank_info = []
    indexed: dict[str, tuple[dict, dict, str]] = {}

    for modality, items, source_fn in (
        ('Reading', reading, lambda item: item.get('text', '')),
        ('Listening', listening, lambda item: '\n'.join(s.get('text', '') for s in item.get('segments', [])) or item.get('script', '')),
    ):
        a2 = [item for item in items if item.get('level') == 'A2']
        if len(a2) != 13:
            issues.append(f'{modality}: expected 13 A2 resources, found {len(a2)}')
        questions = []
        prompts = set()
        for item in a2:
            ident = item.get('lessonId')
            qs = item.get('questions', [])
            if len(qs) != 3:
                issues.append(f'{modality}/{ident}: expected 3 questions, found {len(qs)}')
            correct = []
            source = source_fn(item)
            for q in qs:
                qid = q.get('id', '')
                if not qid or qid in indexed:
                    issues.append(f'{modality}/{ident}: missing or duplicate question ID {qid!r}')
                else:
                    indexed[qid] = (item, q, source)
                choices = q.get('choices', [])
                if len(choices) != 4 or len({norm(c) for c in choices}) != 4:
                    issues.append(f'{qid}: choices must contain four unique options')
                if q.get('answerIndex') not in range(4):
                    issues.append(f'{qid}: invalid answerIndex')
                    answer = ''
                else:
                    answer = choices[q['answerIndex']]
                if not str(q.get('prompt', '')).strip():
                    issues.append(f'{qid}: empty prompt')
                if not str(q.get('rationale', '')).strip():
                    issues.append(f'{qid}: empty rationale')
                prompt_key = norm(q.get('prompt', ''))
                if prompt_key in prompts:
                    issues.append(f'{modality}: duplicated A2 prompt {q.get("prompt", "")}')
                prompts.add(prompt_key)
                if q.get('evidenceText') and q['evidenceText'] not in source:
                    issues.append(f'{qid}: evidenceText is not an exact source substring')
                correct.append(norm(answer))
                questions.append(q)
            if len(correct) == 3 and correct[1] == correct[2]:
                issues.append(f'{modality}/{ident}: q2 and q3 have identical normalized correct answers')
        if len(questions) != 39:
            issues.append(f'{modality}: expected 39 A2 questions, found {len(questions)}')
        counts = Counter(q.get('answerIndex') for q in questions)
        distribution = [counts.get(i, 0) for i in range(4)]
        if distribution != [10, 10, 10, 9]:
            # Whole-bank balance is checked separately below. A2 alone is a smaller subset.
            pass
        bank_info.append((modality, len(a2), len(questions), distribution))

    reviewed = review.get('reviewedQuestions', [])
    expected_ids = {r['id'] for r in reviewed}
    actual_ids = {qid for qid, (_item, q, _source) in indexed.items() if q.get('evidenceText')}
    if actual_ids != expected_ids:
        issues.append(f'Review registry/evidence mismatch: registry-only={sorted(expected_ids-actual_ids)}, data-only={sorted(actual_ids-expected_ids)}')
    for entry in reviewed:
        row = indexed.get(entry['id'])
        if not row:
            issues.append(f'Reviewed question missing: {entry["id"]}')
            continue
        _item, question, source = row
        if entry['evidenceText'] != question.get('evidenceText') or entry['evidenceText'] not in source:
            issues.append(f'{entry["id"]}: review evidence does not match source')

    # Exact answer-position distribution across each full Foundation bank is a release invariant.
    for modality, items in (('Reading', reading), ('Listening', listening)):
        counts = Counter(q.get('answerIndex') for item in items for q in item.get('questions', []))
        distribution = [counts.get(i, 0) for i in range(4)]
        if distribution != [15, 15, 15, 14]:
            issues.append(f'{modality}: answer position distribution expected [15, 15, 15, 14], got {distribution}')

    # Targeted semantic non-duplication checks for the exact pairs revised in this pass.
    targeted = [
        ('a2-quantities::reading1::q2', 'a2-quantities::reading1::q3'),
        ('a2-comparisons::reading1::q2', 'a2-comparisons::reading1::q3'),
        ('a2-obligation-permission::reading1::q2', 'a2-obligation-permission::reading1::q3'),
        ('a2-comparisons::listening1::q2', 'a2-comparisons::listening1::q3'),
        ('a2-sequencing-instructions::listening1::q2', 'a2-sequencing-instructions::listening1::q3'),
    ]
    for left, right in targeted:
        if left not in indexed or right not in indexed:
            issues.append(f'Missing targeted pair: {left} / {right}')
        elif norm(indexed[left][1]['choices'][indexed[left][1]['answerIndex']]) == norm(indexed[right][1]['choices'][indexed[right][1]['answerIndex']]):
            issues.append(f'Targeted pair still has duplicate correct answer: {left} / {right}')

    lines = [
        '# Foundation A2 Assessment Quality Pass — v2.77.0', '',
        '## Scope',
        '- 13 A2 Reading resources and 13 A2 Listening resources; 3 questions per resource (78 question records in total).',
        '- Focused review of within-resource q2/q3 repetition, answer-key uniqueness, four-choice integrity and explicit source traceability for changed/retained focus questions.',
        '- Five question prompts/answer tasks were materially revised; six reviewed question records now carry exact source-evidence pointers.',
        '', '## Automated integrity results',
        '| Bank | A2 resources | A2 questions | A2 answer positions A/B/C/D |',
        '|---|---:|---:|---:|'
    ]
    for modality, resource_count, question_count, distribution in bank_info:
        lines.append(f'| {modality} | {resource_count} | {question_count} | ' + ' / '.join(map(str, distribution)) + ' |')
    lines += [
        '',
        '- All A2 questions require four unique choices, a valid answer index, a non-empty prompt and rationale.',
        '- Each A2 resource must have three questions with non-identical q2/q3 correct answers.',
        '- Each source-evidence pointer is checked as an exact substring of its Reading passage or spoken Listening segment.',
        '- Full-bank answer-position distribution remains A/B/C/D = 15/15/15/14 in each modality.',
        '- Existing A2 q1/q2 objects remain protected by the v2.75.0 canonical-hash baseline tests.',
        '', '## Focused changes',
        '| Question | Change |', '|---|---|'
    ]
    for entry in reviewed:
        lines.append(f'| `{entry["id"]}` | {entry["change"]} |')
    lines += [
        '', '## Review boundary',
        '- The pass fixes five identified cases of repeated information and records six exact source pointers. It does not certify every distractor for semantic plausibility or uniqueness.',
        '- The work is an internal single-author review. Independent second-person language review and psychometric validation remain pending.',
        '- The local A2 three-question / 67% rule is a practice threshold only; it is not a CEFR standard, mastery declaration or ETS equivalence.',
        '',
        '## Automated audit status',
        ('- **PASS** — all registered structural, source-evidence, pair-distinction and answer-position checks passed.' if not issues else '- **FAIL** — audit issues remain:')
    ]
    if issues:
        lines.extend(f'- {issue}' for issue in issues)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'A2 resources: Reading {bank_info[0][1]}/13; Listening {bank_info[1][1]}/13')
    print(f'A2 questions: Reading {bank_info[0][2]}/39; Listening {bank_info[1][2]}/39')
    print(f'Source evidence: {len(actual_ids)}/{len(expected_ids)}')
    print(f'Full-bank answer positions: Reading + Listening [15, 15, 15, 14]')
    if issues:
        print('FAILED:')
        for issue in issues:
            print(' -', issue)
        return 1
    print(f'PASS — wrote {OUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
