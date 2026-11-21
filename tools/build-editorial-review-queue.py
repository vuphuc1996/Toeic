#!/usr/bin/env python3
"""Generate a compact, source-grounded second-review packet for TOEIC reserve items."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))['version']
OUT = ROOT / 'docs' / 'reports' / f'TOEIC_INDEPENDENT_REVIEW_QUEUE_v{VERSION}.md'

def read(path: str):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def md(value) -> str:
    return str(value or '').replace('|', '\\|').replace('\r', ' ').replace('\n', ' ').strip()

def options(choices, answer_index):
    return '<br>'.join(f"{'**' if i == answer_index else ''}{'ABCD'[i]}. {md(choice)}{'**' if i == answer_index else ''}" for i, choice in enumerate(choices))

def main() -> int:
    listening = read('data/listening/listening-library.json')['listening']
    readings = read('data/readings/reading-library.json')['readings']
    p5 = read('data/practice/part5-sentence-completion.json')
    listen_rows = [u for u in listening if u.get('editorialStatus') == 'reserve-pending-independent-review']
    p7_rows = [u for u in readings if u.get('part') == 'Part 7' and u.get('editorialStatus') == 'reserve-pending-independent-review']
    p5_rows = [q for q in p5['questions'] if q.get('editorialStatus', p5.get('editorialStatus')) == 'reserve-pending-independent-review']
    listen_count = sum(len(u.get('questions', [])) for u in listen_rows)
    p7_count = sum(len(u.get('questions', [])) for u in p7_rows)

    lines = [
        f'# TOEIC Independent Editorial Review Queue — v{VERSION}', '',
        '> Mục đích: chuyển nội dung reserve cho người rà soát độc lập. Đây là phiếu làm việc, không phải chứng nhận đã duyệt. Không đổi `editorialStatus` sang `approved-for-mock` cho đến khi reviewer ghi quyết định và ngày rà soát.', '',
        '## Queue summary', '',
        '| Bank | Items pending | Resources | Required review |',
        '|---|---:|---:|---|',
        f'| Listening Parts 1–4 | {listen_count} | {len(listen_rows)} units | Source/key fit, response fit, distractor uniqueness; P1 photo/action match |',
        f'| Reading Part 7 | {p7_count} | {len(p7_rows)} resources | Document evidence, inference, cross-document links, one-best-answer uniqueness |',
        f'| Separate Part 5 sentence completion | {len(p5_rows)} | 1 bank | Grammar, naturalness, distractors, translation and one-answer uniqueness |',
        f'| **Total** | **{listen_count + p7_count + len(p5_rows)}** | **{len(listen_rows) + len(p7_rows) + 1}** | **Independent review required** |', '',
        '## Reviewer record', '',
        '- Reviewer name / role: ____________________________________',
        '- Review date: _____________________________________________',
        '- Review method / reference material: ________________________',
        '- Decision key: `APPROVE` / `REVISE` / `REJECT` (record per item; do not approve a whole batch by default).',
        '- For approval: confirm one defensible key, all distractors are wrong in context, source evidence supports the key, and explanation/translation are accurate.',
        '- For revision: record the exact field and proposed correction; keep the item out of Mock until the correction is retested.',
        '',
        '## A. Listening reserve', '',
        'For Part 2, assess speech act, polarity, indirect response and naturalness. For Parts 3–4, assess transcript support and distractor plausibility. For Part 1, inspect the photo itself as well as the spoken statements.', '',
    ]
    for unit in listen_rows:
        source = ' '.join(seg.get('text', '') for seg in unit.get('segments', []))
        lines += [f"### {md(unit.get('part'))} · `{md(unit['id'])}` · {md(unit.get('title'))}", '',
                  f"- Batch: `{md(unit.get('editorialBatch', 'legacy'))}` · Status: `{md(unit.get('editorialStatus'))}`",
                  f'- Transcript: {md(source)}']
        if unit.get('transcriptTranslation'):
            label = 'Spoken-statement translation / A–D mapping' if unit.get('part') == 'Part 1' else 'Transcript translation'
            lines.append(f"- {label}: {md(unit.get('transcriptTranslation'))}")
        if unit.get('part') == 'Part 1':
            lines.append(f"- Photo: `{md(unit.get('photo'))}` · Alt: {md(unit.get('imageAlt'))}")
            lines.append(f"- Internal visual note (not independent approval): {md(unit.get('visualEvidenceNote'))}")
        for qn, q in enumerate(unit.get('questions', []), 1):
            key = q.get('answerIndex', -1)
            choices = q.get('choices', [])
            keyed = choices[key] if isinstance(key, int) and 0 <= key < len(choices) else '[INVALID KEY]'
            lines += ['', f"**Q{qn}. {md(q.get('question'))}**", '',
                      f"- Choices: {options(choices, key)}",
                      f'- Current keyed answer: **{"ABCD"[key] if isinstance(key, int) and 0 <= key < min(4, len(choices)) else "?"}. {md(keyed)}**',
                      f'- Source pointer: {md(q.get("evidenceText"))}',
                      f'- Current explanation: {md(q.get("explanation"))}',
                      '- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer',
                      '- Decision: `________` · Correction / notes: __________________________________________']
        lines.append('')

    lines += ['## B. Reading Part 7 reserve', '', 'Review source text and all documents together. Confirm that each selected answer is supported by the cited document(s), that the question does not require outside assumptions, and that no other option is also defensible.', '']
    for unit in p7_rows:
        lines += [f"### `{md(unit['id'])}` · {md(unit.get('title'))}", '',
                  f"- Document type: {md(unit.get('documentType'))} · Status: `{md(unit.get('editorialStatus'))}`"]
        if unit.get('passage'):
            lines.append(f"- Passage: {md(unit['passage'])}")
        for doc in unit.get('documents', []):
            lines.append(f"- {md(doc.get('label'))}: {md(doc.get('content'))}")
        for qn, q in enumerate(unit.get('questions', []), 1):
            key = q.get('answerIndex', -1)
            choices = q.get('choices', [])
            keyed = choices[key] if isinstance(key, int) and 0 <= key < len(choices) else '[INVALID KEY]'
            evidence = q.get('evidence', {})
            refs = '; '.join(f"{md(label)} — {' / '.join(md(x) for x in evidence.get('quotes', []))}" for label in evidence.get('sourceLabels', []))
            lines += ['', f"**Q{qn}. {md(q.get('question'))}**", '',
                      f'- Choices: {options(choices, key)}',
                      f'- Current keyed answer: **{"ABCD"[key] if isinstance(key, int) and 0 <= key < min(4, len(choices)) else "?"}. {md(keyed)}**',
                      f'- Evidence reference: {refs}',
                      f'- Current explanation: {md(q.get("explanation"))}',
                      '- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer',
                      '- Decision: `________` · Correction / notes: __________________________________________']
        lines.append('')

    lines += ['## C. Separate TOEIC Part 5 sentence-completion reserve', '', 'This 80-question bank is separate from Reading Part 5 and must not be counted as Mock-eligible. Check the complete sentence, grammar focus, distractors, translation and every option explanation.', '']
    for q in p5_rows:
        key = q.get('answerIndex', -1)
        choices = q.get('choices', [])
        keyed = choices[key] if isinstance(key, int) and 0 <= key < len(choices) else '[INVALID KEY]'
        sentence = str(q.get('sentence', '')).replace('_____', '__________')
        lines += [f"### `{md(q.get('id'))}` · {md(q.get('grammarCategory'))}", '',
                  f'- Sentence: {md(sentence)}',
                  f'- Choices: {options(choices, key)}',
                  f'- Current keyed answer: **{"ABCD"[key] if isinstance(key, int) and 0 <= key < min(4, len(choices)) else "?"}. {md(keyed)}**',
                  f'- Grammar point: {md(q.get("grammarPoint"))}',
                  f'- Single-answer rationale: {md(q.get("singleAnswerReason"))}',
                  f'- Vietnamese translation: {md(q.get("translationVi"))}',
                  '- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer',
                  '- Decision: `________` · Correction / notes: __________________________________________', '']

    lines += ['## Release rule', '',
              '- The current 102 eligible Listening questions remain the only approved Listening pool; the 137 reserve questions are not promoted by this packet.',
              '- Part 7 reserve remains excluded from Mock approval until item-level independent review is recorded.',
              '- Part 5 sentence completion remains separate practice content; its review status must be changed only after item-level sign-off.',
              '- A structural pass, traceable evidence quote or AI-assisted audit is not a substitute for the independent reviewer decision.', '']
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote {OUT.relative_to(ROOT)}')
    print(f'Listening={listen_count}; Part7={p7_count}; Part5={len(p5_rows)}; total={listen_count+p7_count+len(p5_rows)}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
