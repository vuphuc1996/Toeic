#!/usr/bin/env python3
"""Validate TOEIC learning libraries (Listening, Reading, Grammar) before release."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

def read_json(rel: str):
    path = ROOT / rel
    if not path.is_file():
        ERRORS.append(f"Missing file: {rel}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"Invalid JSON {rel}: {exc}")
        return {}

def unique_ids(items, label):
    seen=set()
    for item in items:
        ident=item.get('id')
        if not ident:
            ERRORS.append(f"{label}: record without id")
        elif ident in seen:
            ERRORS.append(f"{label}: duplicate id {ident}")
        seen.add(ident)

def validate_question(q, where, choices_expected=4):
    choices=q.get('choices')
    if not isinstance(choices,list) or len(choices)!=choices_expected:
        ERRORS.append(f"{where}: expected {choices_expected} choices, found {len(choices) if isinstance(choices,list) else 'non-list'}")
    elif any(not isinstance(x,str) or not x.strip() for x in choices):
        ERRORS.append(f"{where}: blank/non-text choice")
    answer=q.get('answerIndex')
    if not isinstance(answer,int) or not isinstance(choices,list) or not (0<=answer<len(choices)):
        ERRORS.append(f"{where}: invalid answerIndex {answer!r}")
    if not str(q.get('question','')).strip():
        ERRORS.append(f"{where}: empty question prompt")
    if not str(q.get('explanation','')).strip():
        ERRORS.append(f"{where}: missing explanation")

def main():
    listening=read_json('data/listening/listening-library.json').get('listening',[])
    reading=read_json('data/readings/reading-library.json').get('readings',[])
    grammar=read_json('data/grammar/lessons.json').get('lessons',[])
    unique_ids(listening,'Listening'); unique_ids(reading,'Reading'); unique_ids(grammar,'Grammar')

    listen_counts={f'Part {i}':0 for i in range(1,5)}
    listen_questions={f'Part {i}':0 for i in range(1,5)}
    part1_correct=[]
    for item in listening:
        ident=item.get('id','?'); part=item.get('part')
        if part not in listen_counts:
            ERRORS.append(f"Listening {ident}: unknown part {part!r}")
            continue
        listen_counts[part]+=1
        segments=item.get('segments') or []
        questions=item.get('questions') or []
        listen_questions[part]+=len(questions)
        if not segments:
            ERRORS.append(f"Listening {ident}: no speech segments")
        for j,seg in enumerate(segments):
            if not str(seg.get('text','')).strip(): ERRORS.append(f"Listening {ident}: empty segment {j}")
        for j,q in enumerate(questions):
            expected=3 if part=='Part 2' else 4
            validate_question(q,f"Listening {ident} Q{j+1}",expected)
        if part=='Part 1':
            if len(segments)!=4: ERRORS.append(f"Listening {ident}: Part 1 needs exactly four spoken statements")
            image=item.get('image','')
            if not image.startswith('./'):
                ERRORS.append(f"Listening {ident}: Part 1 image must be a relative ./ path")
            elif not (ROOT/image[2:]).is_file():
                ERRORS.append(f"Listening {ident}: missing image {image}")
            if len(questions)!=1: ERRORS.append(f"Listening {ident}: Part 1 image item should have one answer question")
            elif len(questions[0].get('choices',[]))==4:
                answer_index=questions[0].get('answerIndex')
                part1_correct.append(answer_index)
                if isinstance(answer_index,int) and 0<=answer_index<4:
                    expected_letter='ABCD'[answer_index]
                    if f'Đáp án {expected_letter}' not in str(questions[0].get('explanation','')):
                        ERRORS.append(f"Listening {ident}: Part 1 explanation does not identify the correct answer letter {expected_letter}")
            if item.get('contentSource')!='original-editorial':
                WARNINGS.append(f"Listening {ident}: source type is not marked original-editorial")

    read_counts={f'Part {i}':0 for i in range(5,8)}
    read_questions={f'Part {i}':0 for i in range(5,8)}
    for item in reading:
        ident=item.get('id','?'); part=item.get('part')
        if part not in read_counts:
            ERRORS.append(f"Reading {ident}: unknown/missing part {part!r}")
            continue
        read_counts[part]+=1
        qs=item.get('questions') or []
        read_questions[part]+=len(qs)
        for j,q in enumerate(qs): validate_question(q,f"Reading {ident} Q{j+1}",4)
        if part=='Part 5' and str(item.get('passage','')).strip():
            WARNINGS.append(f"Reading {ident}: Part 5 is expected to be an incomplete-sentence set, not a passage")
        if part=='Part 6':
            markers=set(re.findall(r'\[(\d+)\]',str(item.get('passage',''))))
            if markers and len(markers)!=len(qs):
                ERRORS.append(f"Reading {ident}: {len(markers)} blank markers but {len(qs)} questions")
        if part=='Part 7' and not (str(item.get('passage','')).strip() or item.get('documents')):
            ERRORS.append(f"Reading {ident}: Part 7 requires a passage/document")
        if not item.get('documentType'):
            ERRORS.append(f"Reading {ident}: missing documentType")
        if item.get('contentSource') not in ('original-editorial','licensed','official-permission'):
            WARNINGS.append(f"Reading {ident}: contentSource not explicitly tagged")

    grammar_count=0
    for lesson in grammar:
        for j,q in enumerate(lesson.get('exercises') or []):
            grammar_count+=1
            validate_question(q,f"Grammar {lesson.get('id','?')} Q{j+1}",4)

    # Require practice for all seven parts; the target distribution is documented separately.
    for part,count in {**listen_counts,**read_counts}.items():
        if count==0: ERRORS.append(f"No learning material for {part}")
    if len(part1_correct)<8:
        WARNINGS.append(f"Part 1 has {len(part1_correct)} photograph sets; increase coverage beyond the current starter set and review photo variety")
    if len(set(part1_correct))<3:
        WARNINGS.append("Part 1 answer positions are not sufficiently distributed across A-D")

    print('TOEIC learning content validation')
    print(f'Listening: {len(listening)} units / {sum(listen_questions.values())} questions')
    for p in listen_counts: print(f'  {p}: {listen_counts[p]} units / {listen_questions[p]} questions')
    print(f'Reading: {len(reading)} units / {sum(read_questions.values())} questions')
    for p in read_counts: print(f'  {p}: {read_counts[p]} units / {read_questions[p]} questions')
    print(f'Grammar: {len(grammar)} lessons / {grammar_count} exercises')
    print(f'Errors: {len(ERRORS)} | Warnings: {len(WARNINGS)}')
    for x in ERRORS: print('ERROR:',x)
    for x in WARNINGS: print('WARNING:',x)
    return 1 if ERRORS else 0

if __name__=='__main__': sys.exit(main())
