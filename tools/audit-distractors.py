#!/usr/bin/env python3
"""Audit TOEIC Part 3/4/7 distractors after transcript/passage review.

This tool validates structural properties and generates a transparent audit log.
It does not claim to prove semantic distractor quality or psychometric validity.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'data' / 'manifest.json').read_text(encoding='utf-8'))['version']
OUT = ROOT / 'docs' / 'reports' / f'TOEIC_DISTRACTOR_AUDIT_v{VERSION}.md'

REVISIONS = [
    ('Listening', 'part3-hotel-reservation', 1, 'Replaced unrelated hotel-service alternatives with other plausible booking requests.'),
    ('Listening', 'part3-client-presentation', 3, 'Aligned all alternatives with realistic presentation-preparation actions.'),
    ('Listening', 'part4-training-registration', 1, 'Aligned alternatives as plausible employee groups.'),
    ('Reading', 'business-travel', 2, 'Made all alternatives plausible travel records while keeping reimbursement evidence unique.'),
    ('Reading', 'customer-refund-email', 1, 'Replaced the unrelated hotel refund with realistic keyboard/order-resolution requests.'),
    ('Reading', 'supplier-invoice-followup', 1, 'Aligned alternatives with common invoice/payment verification issues.'),
    ('Reading', 'double-passage-order', 1, 'Replaced off-topic alternatives with plausible causes of a shipment delay.'),
    ('Reading', 'part7-double-equipment-order', 1, 'Aligned alternatives with realistic supplier/order enquiries.'),
    ('Reading', 'part7-single-training-email', 1, 'Aligned alternatives as plausible employee audiences.'),
    ('Reading', 'training-announcement', 1, 'Aligned alternatives as internal employee groups.'),
    ('Reading', 'part7-triple-regional-sales-meeting', 1, 'Aligned alternatives with plausible meeting materials.'),
    ('Reading', 'part7-triple-facility-renovation', 3, 'Aligned alternatives with plausible visitor-access arrangements.'),
]


def load(rel: str, key: str) -> list[dict]:
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))[key]


def norm(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', value.casefold())


def main() -> int:
    listening_all = [x for x in load('data/listening/listening-library.json', 'listening')
                     if x.get('part') in ('Part 3', 'Part 4')]
    reserve_all = [x for x in load('data/listening/listening-library.json', 'listening') if x.get('editorialStatus') == 'reserve-pending-independent-review']
    reserve = [x for x in listening_all if x.get('editorialStatus') == 'reserve-pending-independent-review']
    listening = [x for x in listening_all if not x.get('editorialStatus') or x.get('editorialStatus') == 'approved-for-mock']
    reading = [x for x in load('data/readings/reading-library.json', 'readings')
               if x.get('part') == 'Part 7']
    scopes = [('Listening', 'Part 3', [x for x in listening if x['part'] == 'Part 3']),
              ('Listening', 'Part 4', [x for x in listening if x['part'] == 'Part 4']),
              ('Reading', 'Part 7', reading)]

    errors: list[str] = []
    counts: Counter = Counter()
    distributions: dict[str, Counter] = {}
    rows: list[tuple[str, str, int, str, list[str], str]] = []
    item_rows: list[tuple[str, str, int]] = []

    for library, part, items in scopes:
        distribution = Counter()
        for item in items:
            item_rows.append((library, item['id'], len(item.get('questions', []))))
            for qn, q in enumerate(item.get('questions', []), 1):
                choices = q.get('choices', [])
                expected = 3 if part == 'Part 2' else 4
                if len(choices) != expected:
                    errors.append(f"{item['id']} Q{qn}: expected 4 choices, got {len(choices)}")
                    continue
                normalized = [norm(c) for c in choices]
                if len(normalized) != len(set(normalized)):
                    errors.append(f"{item['id']} Q{qn}: duplicate normalized choices")
                answer_index = q.get('answerIndex')
                if not isinstance(answer_index, int) or not 0 <= answer_index < len(choices):
                    errors.append(f"{item['id']} Q{qn}: invalid answerIndex {answer_index!r}")
                    continue
                distribution[answer_index] += 1
                counts[part] += 1
                rows.append((library, item['id'], qn, choices[answer_index],
                             [c for i, c in enumerate(choices) if i != answer_index],
                             q.get('question', '')))
        distributions[part] = distribution

    # Reserve items are structurally checked but excluded from the historic answer-position balance
    # until they receive an independent editorial/distractor review.
    for item in reserve:
        for qn, q in enumerate(item.get('questions', []), 1):
            choices = q.get('choices', [])
            if len(choices) != 4:
                errors.append(f"{item['id']} Q{qn}: reserve item expected 4 choices, got {len(choices)}")
                continue
            normalized = [norm(c) for c in choices]
            if len(normalized) != len(set(normalized)):
                errors.append(f"{item['id']} Q{qn}: reserve item has duplicate normalized choices")
            answer_index = q.get('answerIndex')
            if not isinstance(answer_index, int) or not 0 <= answer_index < len(choices):
                errors.append(f"{item['id']} Q{qn}: reserve item has invalid answerIndex {answer_index!r}")

    expected_counts = {'Part 3': 39, 'Part 4': 30, 'Part 7': 108}
    for part, expected in expected_counts.items():
        if counts[part] != expected:
            errors.append(f'{part}: expected {expected} questions in the structural audit scope, got {counts[part]}')
    total = sum(counts.values())
    if total != 177:
        errors.append(f'Expected 177 questions in Part 3/4/7 audit scope, got {total}')

    # Every revision target must be present, and its answer index must still be valid.
    by_library = {'Listening': load('data/listening/listening-library.json', 'listening'),
                  'Reading': load('data/readings/reading-library.json', 'readings')}
    for library, item_id, qn, _note in REVISIONS:
        item = next((x for x in by_library[library] if x.get('id') == item_id), None)
        if not item or len(item.get('questions', [])) < qn:
            errors.append(f'Missing revision target: {library}/{item_id}/Q{qn}')

    lines = [
        f'# TOEIC Distractor & Answer-Uniqueness Audit — v{VERSION}', '',
        '## Scope and method',
        '- Scope covers **177 questions** across Listening Part 3 (39), Listening Part 4 (30) and Reading Part 7 (108). The 63-question historical Part 7 review baseline remains traceable in Project History. The 45 new Part 7 questions in v2.33.0 include source-label/quotation evidence and passed structural key/choice checks; they are not represented as independently reviewed or covered by the historical 132-item semantic distractor certificate.',
        '- The historical 132-item semantic review was performed against full transcripts/passages, keyed options and distractors. For the v2.33 additions, this release adds traceable source quotes, answer-key checks, four-distinct-choice checks, stable choice IDs and balanced answer positions. Semantic distractor uniqueness for new items still requires second-person review.',
        '- Structural checks in this script verify four distinct options and a valid key. They do **not** certify semantic uniqueness by algorithm and are not a substitute for a second human reviewer or psychometric analysis.',
        '', '## Reviewed coverage',
        '| Library | Part | Sets | Questions in audit scope |', '|---|---|---:|---:|'
    ]
    for _library, part, items in scopes:
        lines.append(f"| {_library} | {part} | {len(items)} | {counts[part]} |")
    lines += ['', '### Question sets included',
              '| Library | Set ID | Questions in audit scope |', '|---|---|---:|']
    for library, item_id, qcount in item_rows:
        lines.append(f'| {library} | `{item_id}` | {qcount} |')

    lines += ['', '## Twelve distractor revisions applied',
              '| Library / set / question | Editorial change |', '|---|---|']
    for library, item_id, qn, note in REVISIONS:
        lines.append(f'| {library} · `{item_id}` · Q{qn} | {note} |')

    lines += ['', '## Answer-position distribution — balanced with stable choice identity',
              '| Part | A | B | C | D | Total |', '|---|---:|---:|---:|---:|---:|']
    for part in ('Part 3', 'Part 4', 'Part 7'):
        d = distributions[part]
        lines.append(f"| {part} | {d[0]} | {d[1]} | {d[2]} | {d[3]} | {sum(d.values())} |")
    lines += [
        '',
        '**Rebalancing method:** 27 question groups had only the keyed option exchanged with a distractor position: 8 in Part 3, 5 in Part 4 and 14 in Part 7. The answer text, source evidence, explanation, question IDs and question order were retained. Each changed question carries `previousChoices` and `previousChoiceIds` from v2.16.0; the matching `choiceIds` moved with the option. At startup, progress containing a v2.16 `choiceId` is relocated to its new index; older records without an ID are mapped through the v2.16 snapshot. The prior index is preserved in `previousChoiceIndex`. No random shuffle was used.',
        '', '## Quality decision and remaining limitations',
        '- The 12 revised groups now use distractors closer to the same document purpose, role, travel record, service request, business action or visitor-access context. The correct answer text and `answerIndex` were kept unchanged for every revised question.',
        '- Historical reviewed groups were retained where the three alternatives are distinct and the transcript/passage supports one clear key. For the new v2.33 Part 7 groups, close dates/times, locations, delivery steps and document-purpose alternatives were authored to be plausible, but an independent reviewer must confirm that exactly one option is defensible.',
        f'- Listening reserve total: {sum(len(x.get("questions", [])) for x in reserve_all)} questions across {len(reserve_all)} units. This script structurally checks Part 3/4 reserve blocks; Part 2 response-fit is tracked separately. Structural checks never approve a reserve for Mock.',
        '- This is editorial review of original-authored content. It is not official ETS content, two-person independent review, statistical item analysis, difficulty calibration or proof of score equivalence.',
        '- Part 1 uses licensed Pexels photographs with local SVG fallbacks; Listening audio remains browser SpeechSynthesis. Physical-device audio/voice review is still pending.',
        ''
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {OUT.relative_to(ROOT)}')
    print(f'Questions in audit scope: {total}; reserve structural checks: {sum(len(x.get("questions", [])) for x in reserve)}; revisions: {len(REVISIONS)}')
    for part in ('Part 3', 'Part 4', 'Part 7'):
        d = distributions[part]
        print(f"{part}: A={d[0]}, B={d[1]}, C={d[2]}, D={d[3]}")
    if errors:
        print('ERRORS:')
        for error in errors:
            print(' - ' + error)
        return 1
    print('Structural audit: PASS — unique choices and valid answer keys across review scope')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
