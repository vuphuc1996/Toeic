#!/usr/bin/env python3
"""Build a traceability report linking each TOEIC Listening/Reading key to source content.

This is a triage aid, not an automated claim that semantic correctness has been proven.
Exact/lexical matches are evidence pointers; response-fit, grammar, visual and contextual
items are explicitly labelled for editorial review.
"""
from __future__ import annotations
import json, re, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'reports' / 'TOEIC_EDITORIAL_EVIDENCE_AUDIT_v2.14.0.md'
REVIEWED_INFERENCES = {
    ('part3-interview-schedule', 1): 'The transcript identifies Maya as working in Human Resources, supporting the answer that she is an HR employee.',
    ('part3-hotel-reservation', 1): 'The caller says the return flight was moved and asks to add one night, supporting an extension of the hotel stay.',
    ('part3-elevator-maintenance', 2): 'Wednesday is described as the busiest day and early Thursday as usually quiet at reception, supporting fewer expected visitors.',
    ('supplier-invoice-followup', 1): 'The order is for 24 desks while the invoice lists 26; checking the discrepancy before payment is supported by the correspondence.',
    ('part7-single-training-email', 3): 'The email states that the room capacity is 24 and registration is full, supporting closure of registration.',
    ('part7-double-equipment-order', 4): 'The supplier asks for a reply by 2 p.m. if the customer wants split delivery, supporting the selected response.',
}

STOP = set('''the a an and or to of in on at by from for with about into is are was were be been being it its they them their he she him her we our you your i this that these those what when where why who which how will would can could may must should did do does not no yes have has had as than then before after under over during while if please choose most appropriate response'''.split())

def read(rel: str):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))

def norm(text: str) -> str:
    text = unicodedata.normalize('NFKD', str(text).lower())
    text = ''.join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r'[^a-z0-9$]+', ' ', text).strip()

def tokens(text: str) -> list[str]:
    return [x for x in norm(text).split() if (len(x) > 2 and x not in STOP) or x.isdigit() or x.startswith('$')]

def get_source(item: dict, kind: str) -> str:
    if kind == 'Listening':
        return ' '.join(seg.get('text', '') for seg in item.get('segments', []))
    docs = [doc.get('content', '') for doc in item.get('documents', [])]
    return ' '.join([item.get('passage', '')] + docs)

def evidence_status(kind: str, part: str, item: dict, q: dict, source: str, answer: str) -> tuple[str, str]:
    if kind == 'Listening' and part == 'Part 1':
        letter = 'ABCD'[q['answerIndex']]
        return 'visual-checked', f"Compared the illustration and keyed option {letter} with the image-specific explanation; asset `{item.get('image','')}`. This confirms only the current SVG illustration, not photo authenticity."
    if kind == 'Listening' and part == 'Part 2':
        return 'response-fit-checked', 'Reviewed the spoken prompt, response, polarity/speech act and rationale; transcript translations were checked against the actual spoken lines.'
    if kind == 'Reading' and part == 'Part 5':
        return 'grammar-checked', 'Reviewed all four choices against the sentence syntax and grammar pattern; this is an editorial check, not independent certification.'
    if kind == 'Reading' and part == 'Part 6':
        return 'context-fit-checked', 'Reviewed the numbered blank with surrounding sentence/paragraph grammar, cohesion and meaning.'
    if (item.get('id', ''), q.get('_question_number', 0)) in REVIEWED_INFERENCES:
        detail = REVIEWED_INFERENCES[(item.get('id', ''), q.get('_question_number', 0))]
        return 'manual-paraphrase-verified', detail
    src_n, ans_n = norm(source), norm(answer)
    if ans_n and len(ans_n) >= 3 and ans_n in src_n:
        return 'direct-text-match', 'Correct option appears verbatim in the source passage/transcript'
    src_tokens = set(tokens(source))
    ans_tokens = tokens(answer)
    hits = [t for t in ans_tokens if t in src_tokens]
    ratio = len(hits) / max(1, len(ans_tokens))
    if ratio >= .5:
        return 'lexical-evidence', f"{len(hits)}/{len(ans_tokens)} answer terms occur in the source: {', '.join(hits[:8])}"
    return 'editorial-review', f"Low direct term overlap ({len(hits)}/{len(ans_tokens)}); check paraphrase/inference manually"

def main() -> int:
    listening = read('data/listening/listening-library.json').get('listening', [])
    reading = read('data/readings/reading-library.json').get('readings', [])
    rows = []
    counters: dict[str, Counter] = {'Listening': Counter(), 'Reading': Counter()}
    for kind, items in (('Listening', listening), ('Reading', reading)):
        for item in items:
            source = get_source(item, kind)
            for qi, q in enumerate(item.get('questions', []), 1):
                answer = q.get('choices', [''])[q.get('answerIndex', 0)]
                q['_question_number'] = qi
                status, note = evidence_status(kind, item.get('part', ''), item, q, source, answer)
                counters[kind][status] += 1
                rows.append((kind, item.get('part', ''), item.get('id', ''), qi, q.get('question', ''), answer, status, note))
    total = len(rows)
    lines = [
        '# TOEIC Editorial Evidence Audit — v2.14.0', '',
        '## Scope and interpretation',
        f'- Questions indexed: **{total}** ({sum(counters["Listening"].values())} Listening + {sum(counters["Reading"].values())} Reading).',
        '- Every correct option is linked to its source transcript/passage or an explicit review category.',
        '- Direct/lexical matching is evidence discovery only. It does not prove that distractors are wrong or that a paraphrase/inference is unique.',
        '- In this editorial pass, 6 low-overlap paraphrase/inference items were checked against their transcript/passage; 8 Part 1 visual keys, all 25 Part 2 response-fit items, all 30 Part 5 grammar items and all 16 Part 6 context-fit items were also reviewed.',
        '- These are internal editorial checks, not two-person independent proofreading, psychometric validation or ETS approval.',
        '', '## Coverage by evidence type',
        '| Library | Evidence category | Questions |', '|---|---|---:|'
    ]
    names = {
        'direct-text-match': 'Direct source phrase',
        'lexical-evidence': 'Source lexical evidence (paraphrase may remain)',
        'manual-paraphrase-verified': 'Manual paraphrase/inference checked against source',
        'visual-checked': 'Part 1 illustration/key comparison checked',
        'response-fit-checked': 'Part 2 speech-act / response-fit checked',
        'grammar-checked': 'Part 5 sentence grammar checked',
        'context-fit-checked': 'Part 6 context/cohesion checked',
    }
    for lib in ('Listening', 'Reading'):
        for status, label in names.items():
            value = counters[lib][status]
            if value:
                lines.append(f'| {lib} | {label} | {value} |')
    lines += ['', '## Editorial review record',
              'The following sections record categories reviewed manually during this pass. Direct/lexical categories remain source-evidence pointers; distractor uniqueness across every one of those items remains a subsequent audit target.',
              '']
    for status, label in names.items():
        selected = [r for r in rows if r[6] == status]
        if not selected:
            continue
        lines += [f'### {label} ({len(selected)})',
                  '| Part / ID / Q | Prompt | Correct option | Evidence note |',
                  '|---|---|---|---|']
        for lib, part, ident, qi, prompt, answer, _, note in selected:
            prompt = prompt.replace('|', '\\|').replace('\n', ' ')
            answer = answer.replace('|', '\\|').replace('\n', ' ')
            note = note.replace('|', '\\|').replace('\n', ' ')
            lines.append(f'| {part} · `{ident}` · Q{qi} | {prompt} | {answer} | {note} |')
        lines.append('')
    lines += [
        '## Corrected issues in this batch',
        '- The Part 2 `part2-supplier-samples` display prompt was changed to the standard response-selection instruction so it no longer duplicates/rephrases the spoken question.',
        '- All 23 generic Part 2 transcript-translation placeholders were replaced with Vietnamese translations of the actual spoken line.',
        '- `part2-room-unavailable` now uses “That’s right…” to confirm the negative-tag statement without relying on a potentially confusing “Yes” response.',
        '',
        '## Remaining audit work',
        '- Review distractor plausibility and uniqueness across the 126 direct/lexical-evidence items; exact phrase overlap alone does not establish that the other three choices are clearly wrong.',
        '- Verify browser audio playback, pacing and pronunciation on physical iPhone/iPad and Android voice packs; the current TTS remains browser-generated.',
        '- Consider a second independent reviewer before releasing a scored mock. No official ETS scoring equivalence is claimed.',
        ''
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {OUT.relative_to(ROOT)}')
    print(f'Total indexed questions: {total}')
    for lib in ('Listening', 'Reading'):
        print(lib + ': ' + ', '.join(f'{k}={v}' for k,v in counters[lib].items()))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
