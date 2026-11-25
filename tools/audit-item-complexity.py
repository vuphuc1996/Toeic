#!/usr/bin/env python3
"""Create a transparent, non-calibrated TOEIC item-complexity review queue.

This tool reports observable structural features only. It does not assign CEFR,
ETS difficulty, item-response parameters, or Mock approval. Reserve status is
always preserved and displayed as an exclusion from Mock.
"""
from __future__ import annotations
import json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))['version']
OUT = ROOT / 'docs/reports' / f'TOEIC_ITEM_COMPLEXITY_REVIEW_v{VERSION}.md'
INFERENCE = re.compile(r'\b(infer(?:red|ence)?|imply|suggest|most likely|indicate|probably|purpose|main idea|primarily|intended to)\b', re.I)
MULTI_DOC = re.compile(r'\b(both|according to (?:the )?(?:two|both)|in (?:the )?(?:first|second|another) (?:email|notice|document)|cross[- ]document)\b', re.I)
QUESTION_KIND = [
    ('inference_or_purpose', re.compile(r'\b(infer(?:red|ence)?|imply|suggest|most likely|indicate|probably|purpose|main idea|primarily|intended to)\b', re.I)),
    ('detail_or_location', re.compile(r'\b(what|when|where|who|which|how many|how much|how long|how often)\b', re.I)),
    ('other_or_response_fit', re.compile(r'.', re.S)),
]

def words(s: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", str(s or ''))

def source_text(item: dict, kind: str) -> str:
    if kind == 'Listening':
        return ' '.join(str(x.get('text', '')) for x in item.get('segments', []))
    docs = item.get('documents', [])
    return ' '.join([str(item.get('passage', ''))] + [str(x.get('content', '')) for x in docs])

def classify_question(q: dict) -> str:
    prompt = str(q.get('question', ''))
    if QUESTION_KIND[0][1].search(prompt):
        return 'inference_or_purpose'
    if QUESTION_KIND[1][1].search(prompt):
        return 'detail_or_location'
    return 'other_or_response_fit'

def main() -> int:
    libs = [
        ('Listening', json.loads((ROOT/'data/listening/listening-library.json').read_text(encoding='utf-8')).get('listening', [])),
        ('Reading', json.loads((ROOT/'data/readings/reading-library.json').read_text(encoding='utf-8')).get('readings', [])),
    ]
    rows=[]; part_counts=Counter(); flags=Counter(); status_counts=Counter(); errors=[]
    for kind, items in libs:
        for item in items:
            source = source_text(item, kind)
            source_wc = len(words(source))
            docs = item.get('documents', [])
            for qn, q in enumerate(item.get('questions', []), 1):
                choices=q.get('choices', [])
                ai=q.get('answerIndex')
                if not isinstance(ai,int) or not 0 <= ai < len(choices):
                    errors.append(f"{kind}/{item.get('id')}/Q{qn}: invalid answerIndex")
                    continue
                prompt_wc=len(words(q.get('question','')))
                option_wc=[len(words(x)) for x in choices]
                option_spread=(max(option_wc)-min(option_wc)) if option_wc else 0
                kind_label=classify_question(q)
                cues=[]
                if source_wc >= 250: cues.append('long_source_250_plus')
                if prompt_wc >= 18: cues.append('long_question_18_plus')
                if option_spread >= 8: cues.append('option_length_spread_8_plus')
                if kind_label == 'inference_or_purpose': cues.append('inference_or_purpose_wording')
                if len(docs) >= 2 or MULTI_DOC.search(str(item.get('title',''))+' '+source): cues.append('multi_document_language_cue')
                reserve=item.get('editorialStatus') == 'reserve-pending-independent-review'
                rows.append({'kind':kind,'part':item.get('part','unknown'),'id':item.get('id',''),'qn':qn,'source_wc':source_wc,'prompt_wc':prompt_wc,'option_spread':option_spread,'question_kind':kind_label,'cues':cues,'reserve':reserve,'level':item.get('level','unspecified')})
                part_counts[(kind,item.get('part','unknown'))]+=1
                status_counts['reserve' if reserve else 'non_reserve']+=1
                for c in cues: flags[c]+=1
    if not rows: errors.append('No questions were discovered')
    cue_n=sum(bool(r['cues']) for r in rows)
    lines=[f'# TOEIC Item Complexity Review Queue — v{VERSION}','',
      '## Purpose and limits',
      '- This is a transparent structural triage report, not a difficulty score or calibrated item model.',
      '- It does not assign CEFR/ETS difficulty, estimate discrimination/difficulty parameters, certify answer correctness, or approve Mock eligibility.',
      '- Signals are review prompts only. Long sources, inference wording, option-length spread and multi-document indicators may be legitimate and require expert judgment.',
      '- Existing `level` metadata is shown as supplied; it is not validated or reinterpreted here.',
      '- All reserve-pending items remain reserve-pending and excluded from Mock; this report never changes source content or eligibility.','',
      '## Inventory', '', '| Library | Part | Questions |','|---|---|---:|']
    for (kind,part),n in sorted(part_counts.items()): lines.append(f'| {kind} | {part} | {n} |')
    lines += ['',f'- Total questions indexed: **{len(rows)}**',f'- Reserve-pending across both libraries: **{status_counts["reserve"]}**',
      f'- Listening reserve-pending: **{sum(len(x.get('questions', [])) for x in libs[0][1] if x.get('editorialStatus') == 'reserve-pending-independent-review')}**',
      f'- Reading reserve-pending: **{sum(len(x.get('questions', [])) for x in libs[1][1] if x.get('editorialStatus') == 'reserve-pending-independent-review')}**',f'- Other editorial states: **{status_counts["non_reserve"]}**',f'- Questions with one or more structural review signals: **{cue_n}/{len(rows)}**','', '## Signal counts','', '| Signal | Questions |','|---|---:|']
    labels={'long_source_250_plus':'Source text >=250 words','long_question_18_plus':'Question prompt >=18 words','option_length_spread_8_plus':'Choice word-count spread >=8','inference_or_purpose_wording':'Inference / purpose wording','multi_document_language_cue':'Multi-document language cue (e.g. both / first / second document)'}
    for key,label in labels.items(): lines.append(f'| {label} | {flags[key]} |')
    lines += ['', '## Question-level review queue', '', '| Library / Part / ID / Q | Supplied level | Source words | Prompt words | Option spread | Question form | Review signals | Eligibility note |','|---|---|---:|---:|---:|---|---|---|']
    for r in rows:
        signals=', '.join(labels[x] for x in r['cues']) or 'none detected'
        eligibility='RESERVE — not Mock eligible' if r['reserve'] else 'Existing status unchanged'
        lines.append(f"| {r['kind']} / {r['part']} / `{r['id']}` / Q{r['qn']} | {r['level']} | {r['source_wc']} | {r['prompt_wc']} | {r['option_spread']} | {r['question_kind']} | {signals} | {eligibility} |")
    lines += ['', '## Decision boundary', '- Use this queue to prioritize human review, not to rank questions from easy to hard.', '- Before any future calibrated difficulty label is introduced, require a documented pilot sample, response-level anonymized outcome data, minimum sample thresholds, item facility/discrimination analysis, subgroup/bias review, versioned method and independent sign-off.', '- No response data or psychometric parameters are inferred from static content in this report.','']
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text('\n'.join(lines),encoding='utf-8')
    print(f'Wrote {OUT.relative_to(ROOT)}')
    print(f'Questions: {len(rows)}; reserve: {status_counts["reserve"]}; signalled: {cue_n}; errors: {len(errors)}')
    for k in labels: print(f'{k}: {flags[k]}')
    if errors:
        for e in errors: print('ERROR:',e)
        return 1
    return 0

if __name__ == '__main__': raise SystemExit(main())
