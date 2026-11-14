#!/usr/bin/env python3
"""Validate TOEIC learning libraries (Listening, Reading, Grammar) before release."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []
SENTENCE_GRAMMAR_CATEGORIES = {
    'Adjectives and Adverbs', 'Articles and Determiners', 'Conjunctions and Clauses',
    'Gerunds and Infinitives', 'Imperatives and Verb Forms', 'Infinitives and Verb Patterns',
    'Linking Verbs', 'Modal Verbs', 'Participles and Reduced Relative Clauses',
    'Passive Voice', 'Prepositions and Collocations', 'Subject–Verb Agreement',
    'Verb Tense and Aspect', 'Word Forms and Nouns'
}

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
    sentence_bank=read_json('data/practice/part5-sentence-completion.json')
    sentence_questions=sentence_bank.get('questions',[]) if isinstance(sentence_bank,dict) else []
    vocabulary_manifest=read_json('data/manifest.json')
    vocabulary_ids=set()
    for entry in vocabulary_manifest.get('letters',[]):
        letter_data=read_json(entry.get('file','').removeprefix('./').replace('\\','/')) if entry.get('file') else {}
        vocabulary_ids.update(word.get('id') for word in letter_data.get('words',[]) if isinstance(word,dict) and word.get('id'))
    unique_ids(listening,'Listening'); unique_ids(reading,'Reading'); unique_ids(grammar,'Grammar')
    unique_ids(sentence_questions,'Sentence Completion')
    if sentence_bank.get('editorialStatus') != 'reserve-pending-independent-review':
        ERRORS.append('Sentence Completion: bank must remain pending independent review')
    if sentence_bank.get('reviewNote') != 'internal-author-check; independent-second-review-pending':
        ERRORS.append('Sentence Completion: independent review note is missing or inconsistent')
    groups=sentence_bank.get('questionGroups',[])
    if not isinstance(groups,list) or sum(group.get('questionCount',0) for group in groups if isinstance(group,dict)) != len(sentence_questions):
        ERRORS.append('Sentence Completion: questionGroups count does not match the bank inventory')
    seen_sentence_targets=set()
    for item in sentence_questions:
        ident=item.get('id','?')
        if item.get('wordId') not in vocabulary_ids:
            ERRORS.append(f'Sentence Completion {ident}: wordId does not resolve to canonical vocabulary')
        if item.get('wordId') in seen_sentence_targets:
            ERRORS.append(f'Sentence Completion {ident}: duplicate target wordId')
        seen_sentence_targets.add(item.get('wordId'))
        sentence=str(item.get('sentence',''))
        if sentence.count('_____') != 1:
            ERRORS.append(f'Sentence Completion {ident}: sentence must contain exactly one blank marker')
        choices=item.get('choices')
        if not isinstance(choices,list) or len(choices)!=4 or any(not isinstance(x,str) or not x.strip() for x in choices):
            ERRORS.append(f'Sentence Completion {ident}: exactly four non-empty choices are required')
        elif len({x.strip().casefold() for x in choices}) != 4:
            ERRORS.append(f'Sentence Completion {ident}: choices must be unique')
        if not isinstance(item.get('answerIndex'),int) or item.get('answerIndex') not in range(4):
            ERRORS.append(f'Sentence Completion {ident}: invalid answerIndex')
        notes=item.get('optionExplanations')
        if not isinstance(notes,list) or len(notes)!=4 or any(not str(x).strip() for x in notes):
            ERRORS.append(f'Sentence Completion {ident}: four option-specific explanations are required')
        elif isinstance(item.get('answerIndex'),int) and item.get('answerIndex') in range(4):
            if not str(notes[item['answerIndex']]).startswith('Đúng:'):
                ERRORS.append(f'Sentence Completion {ident}: correct option explanation must start with Đúng:')
            if any(not str(notes[index]).startswith('Sai:') for index in range(4) if index != item['answerIndex']):
                ERRORS.append(f'Sentence Completion {ident}: distractor explanations must start with Sai:')
        if item.get('grammarCategory') not in SENTENCE_GRAMMAR_CATEGORIES: ERRORS.append(f'Sentence Completion {ident}: missing or unsupported grammarCategory')
        if item.get('editorialBatch') == '016' and item.get('contentBatch') != 'batch-016-part5-grammar-expansion': ERRORS.append(f'Sentence Completion {ident}: Batch 016 contentBatch is missing or inconsistent')
        for field in ('grammarPoint','explanation','translationVi','singleAnswerReason'):
            if not str(item.get(field,'')).strip(): ERRORS.append(f'Sentence Completion {ident}: missing {field}')
        if item.get('contentSource')!='original-editorial': ERRORS.append(f'Sentence Completion {ident}: source must be original-editorial')
        if item.get('editorialStatus')!='reserve-pending-independent-review': ERRORS.append(f'Sentence Completion {ident}: item must remain pending independent review')
        if item.get('reviewNote')!='internal-author-check; independent-second-review-pending': ERRORS.append(f'Sentence Completion {ident}: independent-review note is missing or inconsistent')

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
        if part=='Part 2' and len(questions)!=1:
            ERRORS.append(f"Listening {ident}: Part 2 item must contain exactly one question")
        if part in ('Part 3','Part 4') and len(questions)!=3:
            ERRORS.append(f"Listening {ident}: {part} set must contain exactly three questions")
        if item.get('contentSource') not in ('original-editorial','licensed','official-permission'):
            WARNINGS.append(f"Listening {ident}: contentSource is not explicitly tagged")
        editorial_status=item.get('editorialStatus')
        if editorial_status and editorial_status not in ('reserve-pending-independent-review','approved-for-mock'):
            ERRORS.append(f"Listening {ident}: unsupported editorialStatus {editorial_status!r}")
        if item.get('editorialBatch') == '015':
            if editorial_status != 'reserve-pending-independent-review':
                ERRORS.append(f"Listening {ident}: Batch 015 must remain pending independent review")
            if item.get('reviewNote') != 'internal-author-check; independent-second-review-pending':
                ERRORS.append(f"Listening {ident}: Batch 015 reviewNote is missing or inconsistent")
            source_text=' '.join(str(seg.get('text','')) for seg in segments).casefold()
            for qi,question in enumerate(questions,1):
                pointer=str(question.get('evidenceText','')).strip().casefold()
                if not pointer:
                    ERRORS.append(f"Listening {ident} Q{qi}: Batch 015 evidenceText is required")
                elif part == 'Part 2' and pointer not in source_text:
                    ERRORS.append(f"Listening {ident} Q{qi}: Part 2 evidenceText must identify the spoken prompt in the transcript")
                elif part in ('Part 3','Part 4') and pointer not in source_text:
                    ERRORS.append(f"Listening {ident} Q{qi}: transcript evidenceText not found in source audio transcript")
        if not segments:
            ERRORS.append(f"Listening {ident}: no speech segments")
        if part=='Part 3':
            speakers={str(seg.get('speaker','')).strip() for seg in segments if str(seg.get('speaker','')).strip()}
            if len(speakers)<2:
                ERRORS.append(f"Listening {ident}: Part 3 conversation requires at least two named speakers")
        for j,seg in enumerate(segments):
            if not str(seg.get('text','')).strip(): ERRORS.append(f"Listening {ident}: empty segment {j}")
        for j,q in enumerate(questions):
            expected=3 if part=='Part 2' else 4
            validate_question(q,f"Listening {ident} Q{j+1}",expected)
            if part == 'Part 2' and str(q.get('question','')).strip() != 'Choose the most appropriate response.':
                ERRORS.append(f"Listening {ident}: Part 2 display prompt must use the standard response-selection instruction")
        translation = str(item.get('transcriptTranslation','')).strip()
        if part == 'Part 2' and re.search(r'nghe câu hỏi|lời nói tiếng anh|chọn phản hồi phù hợp nhất', translation, re.I):
            ERRORS.append(f"Listening {ident}: Part 2 transcriptTranslation is a generic instruction, not a Vietnamese translation")
        if part=='Part 1':
            if len(segments)!=4: ERRORS.append(f"Listening {ident}: Part 1 needs exactly four spoken statements")
            image=item.get('image','')  # SVG fallback remains part of the base package
            photo=item.get('photo','')
            if not image.startswith('./'):
                ERRORS.append(f"Listening {ident}: Part 1 fallback image must be a relative ./ path")
            elif not (ROOT/image[2:]).is_file():
                ERRORS.append(f"Listening {ident}: missing fallback image {image}")
            if not photo.startswith('./assets/listening/') or not photo.lower().endswith('.jpg'):
                ERRORS.append(f"Listening {ident}: licensed photo must use a local ./assets/listening/*.jpg path")
            elif not (ROOT/photo[2:]).is_file():
                WARNINGS.append(f"Listening {ident}: licensed photo is not present in this source snapshot; SVG fallback remains available ({photo})")
            if item.get('visualType') != 'photograph':
                ERRORS.append(f"Listening {ident}: local Pexels asset must be labelled as photograph")
            if len(questions)!=1: ERRORS.append(f"Listening {ident}: Part 1 image item should have one answer question")
            elif len(questions[0].get('choices',[]))==4:
                answer_index=questions[0].get('answerIndex')
                part1_correct.append(answer_index)
                if isinstance(answer_index,int) and 0<=answer_index<4:
                    expected_letter='ABCD'[answer_index]
                    if f'Đáp án {expected_letter}' not in str(questions[0].get('explanation','')):
                        ERRORS.append(f"Listening {ident}: Part 1 explanation does not identify the correct answer letter {expected_letter}")
            if image.lower().endswith('.svg') and not photo and item.get('visualType') not in ('illustration', 'diagram'):
                WARNINGS.append(f"Listening {ident}: SVG visual should be explicitly labelled as an illustration/diagram")

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
        if part=='Part 7' and item.get('documentType') in ('DOUBLE PASSAGE','TRIPLE PASSAGE'):
            expected_docs=2 if item.get('documentType')=='DOUBLE PASSAGE' else 3
            docs=item.get('documents')
            if not isinstance(docs,list) or len(docs)!=expected_docs:
                ERRORS.append(f"Reading {ident}: {item.get('documentType')} requires {expected_docs} structured documents")
            else:
                for di,doc in enumerate(docs):
                    if not str(doc.get('label','')).strip() or not str(doc.get('content','')).strip():
                        ERRORS.append(f"Reading {ident}: document {di+1} needs a label and content")
        if not item.get('documentType'):
            ERRORS.append(f"Reading {ident}: missing documentType")
        if item.get('contentSource') not in ('original-editorial','licensed','official-permission'):
            WARNINGS.append(f"Reading {ident}: contentSource not explicitly tagged")

    p7_single_questions=0
    p7_multiple_questions=0
    for item in reading:
        if item.get('part')!='Part 7':
            continue
        count=len(item.get('questions') or [])
        if item.get('documentType') in ('DOUBLE PASSAGE','TRIPLE PASSAGE'):
            p7_multiple_questions+=count
        else:
            p7_single_questions+=count

    grammar_count=0
    grammar_part_counts = {'Part 5': {'lessons': 0, 'exercises': 0}, 'Part 6': {'lessons': 0, 'exercises': 0}}
    for lesson in grammar:
        parts = lesson.get('parts', [])
        if parts and (not isinstance(parts, list) or not set(parts).issubset(grammar_part_counts)):
            ERRORS.append(f"Grammar {lesson.get('id','?')}: parts must contain only Part 5 and/or Part 6")
        for part in parts if isinstance(parts, list) else []:
            grammar_part_counts[part]['lessons'] += 1
            grammar_part_counts[part]['exercises'] += len(lesson.get('exercises') or [])
        for j,q in enumerate(lesson.get('exercises') or []):
            grammar_count+=1
            validate_question(q,f"Grammar {lesson.get('id','?')} Q{j+1}",4)

    # Require practice for all seven parts; the target distribution is documented separately.
    for part,count in {**listen_counts,**read_counts}.items():
        if count==0: ERRORS.append(f"No learning material for {part}")
    if len(part1_correct)<8:
        WARNINGS.append(f"Part 1 has {len(part1_correct)} image-description sets; increase coverage and review visual variety")
    if len(set(part1_correct))<3:
        WARNINGS.append("Part 1 answer positions are not sufficiently distributed across A-D")

    # The pool gate is stronger than simple Part presence: it must be large enough
    # to select the official blueprint for one form without fabricating questions.
    listening_targets={'Part 1':6,'Part 2':25,'Part 3':39,'Part 4':30}
    reading_targets={'Part 5':30,'Part 6':16}
    for part,target in listening_targets.items():
        if listen_questions[part] < target:
            ERRORS.append(f"Question pool below blueprint: {part} has {listen_questions[part]}, needs at least {target}")
    for part,target in reading_targets.items():
        if read_questions[part] < target:
            ERRORS.append(f"Question pool below blueprint: {part} has {read_questions[part]}, needs at least {target}")
    if p7_single_questions < 29:
        ERRORS.append(f"Part 7 single-passage pool has {p7_single_questions}, needs at least 29 questions")
    if p7_multiple_questions < 25:
        ERRORS.append(f"Part 7 multiple-passage pool has {p7_multiple_questions}, needs at least 25 questions")

    print('TOEIC learning content validation')
    print(f'Listening: {len(listening)} units / {sum(listen_questions.values())} questions')
    for p in listen_counts: print(f'  {p}: {listen_counts[p]} units / {listen_questions[p]} questions')
    print(f'Reading: {len(reading)} units / {sum(read_questions.values())} questions')
    for p in read_counts: print(f'  {p}: {read_counts[p]} units / {read_questions[p]} questions')
    print(f'Part 7 passage mix: {p7_single_questions} single-passage / {p7_multiple_questions} multiple-passage questions')
    print(f'Grammar: {len(grammar)} lessons / {grammar_count} exercises')
    print(f'TOEIC Part 5 Sentence Completion: {len(sentence_questions)} curated questions (practice only; pending independent review)')
    for part, counts in grammar_part_counts.items():
        print(f"  {part} tagged: {counts['lessons']} lessons / {counts['exercises']} exercises")
    print(f'Errors: {len(ERRORS)} | Warnings: {len(WARNINGS)}')
    for x in ERRORS: print('ERROR:',x)
    for x in WARNINGS: print('WARNING:',x)
    return 1 if ERRORS else 0

if __name__=='__main__': sys.exit(main())
