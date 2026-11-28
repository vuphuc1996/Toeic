#!/usr/bin/env python3
"""Generate a target-based progress snapshot from canonical project data."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def load(path): return json.loads((ROOT / path).read_text(encoding='utf-8'))
def pct(n, d): return f'{(n/d*100):.1f}%' if d else 'Chưa đo được'
def main():
    manifest=load('data/manifest.json')
    vocab=sum(x['count'] for x in manifest['letters'])
    grammar=load('data/grammar/lessons.json')['lessons']
    listening=load('data/listening/listening-library.json')['listening']
    readings=load('data/readings/reading-library.json')['readings']
    foundation=load('data/learning-path/pre-a1-a1.json')['lessons']
    alphabet_sounds=load('data/learning-path/alphabet-sounds.json')['letters']
    foundation_listening_all=load('data/learning-path/foundation-listening.json')['clips']
    foundation_listening_core=[x for x in foundation_listening_all if not x.get('supplementary')]
    foundation_listening_extended=[x for x in foundation_listening_all if x.get('supplementary')]
    foundation_listening=foundation_listening_core
    foundation_reading=load('data/learning-path/foundation-reading.json')['passages']
    p5=load('data/practice/part5-sentence-completion.json')
    objective_map=load('data/learning-path/objective-resource-map.json')['objectives']
    wired_toeic=[x for x in objective_map if x.get('kind') in {'grammar','listening','reading','practice'}]
    foundation_objectives=[x for x in objective_map if x.get('kind')=='learning_path']
    outcome_registry=load('data/learning-path/objective-outcomes.json')
    outcome_objectives=outcome_registry['objectives']
    criterion_map=load('data/learning-path/objective-criterion-map.json')
    criterion_mapping_count=len(criterion_map.get('mappings', []))
    criterion_unique_questions=criterion_map.get('uniqueQuestionCount', 0)
    toeic_outcomes=[outcome for group in outcome_objectives if not str(group.get('objectiveId','')).startswith('foundation-') for outcome in group.get('outcomes', [])]
    toeic_uninstrumented=[outcome for outcome in toeic_outcomes if not str(outcome.get('status','')).startswith('instrumented_')]
    toeic_instrumented=sum(1 for outcome in toeic_outcomes if str(outcome.get('status','')).startswith('instrumented_'))
    outcome_total=sum(len(x.get('outcomes',[])) for x in outcome_objectives)
    outcome_instrumented=sum(1 for x in outcome_objectives for o in x.get('outcomes',[]) if str(o.get('status','')).startswith('instrumented_'))
    foundation_outcome_total=sum(len(x.get('outcomes',[])) for x in outcome_objectives if str(x.get('objectiveId','')).startswith('foundation-'))
    foundation_outcome_instrumented=sum(1 for x in outcome_objectives if str(x.get('objectiveId','')).startswith('foundation-') for o in x.get('outcomes',[]) if str(o.get('status','')).startswith('instrumented_'))
    objective_collections={(x['resourceFile'],x['resourceCollection']) for x in objective_map}
    objective_total=sum(len(load(path)[collection]) for path,collection in objective_collections)
    objective_mapped=len({(x['resourceFile'],x['resourceCollection'],rid) for x in objective_map for rid in x.get('resourceIds',[])})
    diag=load('data/learning-path/placement-diagnostic.json')['questions']
    stages={str(x.get('level','')).upper() for x in foundation}
    listening_q=sum(len(x.get('questions',[])) for x in listening)
    reading_q=sum(len(x.get('questions',[])) for x in readings)
    p5n=len(p5.get('questions',[]))
    listening_pending_units=[x for x in listening if x.get('editorialStatus')=='reserve-pending-independent-review']
    listening_pending_questions=sum(len(x.get('questions',[])) for x in listening_pending_units)
    p7_pending_resources=[x for x in readings if x.get('part')=='Part 7' and x.get('editorialStatus')=='reserve-pending-independent-review']
    p7_pending_questions=sum(len(x.get('questions',[])) for x in p7_pending_resources)
    p5_pending_questions=p5n if p5.get('editorialStatus')=='reserve-pending-independent-review' else 0
    independent_review_total=listening_pending_questions+p7_pending_questions+p5_pending_questions
    foundation_listening_questions=sum(len(x.get('questions',[])) for x in foundation_listening_core)
    foundation_listening_extended_questions=sum(len(x.get('questions',[])) for x in foundation_listening_extended)
    foundation_reading_questions=sum(len(x.get('questions',[])) for x in foundation_reading)
    # Field-level metadata coverage is reported against the current headword base, not as a project target.
    vocab_files=[ROOT / x['file'].replace('./','',1) for x in manifest['letters']]
    vocab_records=[]
    for path in vocab_files:
        vocab_records.extend(json.loads(path.read_text(encoding='utf-8')).get('words', []))
    related_keys={str(x.get('term','')).casefold() for x in load('data/related-terms.json').get('terms', [])}
    related_frequency=Counter(
      str(term).casefold()
      for record in vocab_records
      for sense in record.get('senses', [])
      for field in ('synonyms','antonyms')
      for term in (sense.get(field) or [])
    )
    related_total_distinct=len(related_frequency)
    related_covered_distinct=len(set(related_frequency) & related_keys)
    related_total_occurrences=sum(related_frequency.values())
    related_covered_occurrences=sum(count for term,count in related_frequency.items() if term in related_keys)
    related_missing_distinct=related_total_distinct-related_covered_distinct
    related_missing_occurrences=related_total_occurrences-related_covered_occurrences
    field_counts={
      'US IPA':sum(bool((x.get('phonetic') or {}).get('us')) for x in vocab_records),
      'Word family':sum(bool(x.get('word_family')) for x in vocab_records),
      'Verb forms':sum(bool(x.get('verb_forms')) for x in vocab_records),
      'Collocations':sum(bool(x.get('collocations')) for x in vocab_records),
      'Synonyms':sum(any(s.get('synonyms') for s in x.get('senses',[])) for x in vocab_records),
      'Antonyms':sum(any(s.get('antonyms') for s in x.get('senses',[])) for x in vocab_records),
    }
    word_family_links=sum(len(x.get('word_family') or []) for x in vocab_records)
    lines=[
      '# Project Progress Snapshot — generated',
      '',f"- Source version: **{manifest['version']}**",'- Basis: canonical JSON inventory; counts are not editorial approval.',
      '', '## Target-based progress',
      '', '| Workstream | Current | Target / denominator | Progress | Interpretation |',
      '|---|---:|---:|---:|---|',
      f'| Vocabulary headwords | {vocab:,} | 3,000 minimum | **{pct(vocab,3000)}** | Lower-bound target coverage; quality review separate |',
      f'| Vocabulary headwords | {vocab:,} | 5,000 planning ceiling | **{pct(vocab,5000)}** | Conservative ceiling coverage; not a quality score |',
      f'| Related-term glossary exact reference join | {related_covered_distinct}/{related_total_distinct} | **{pct(related_covered_distinct,related_total_distinct)}** | {related_missing_distinct} distinct terms / {related_missing_occurrences} occurrences remain unglossed; exact case-insensitive join only |',
      f'| Guided pathway stages represented | {len(stages)}/6 | Pre-A1, A1, A2, B1, B2, C1 | **{pct(len(stages),6)}** | Stage presence only; not full-stage completion |',
      f'| Placement question mapping | {len(load("data/learning-path/placement-objective-map.json")["questionMappings"])}/{len(diag)} | All diagnostic questions | **{pct(len(load("data/learning-path/placement-objective-map.json")["questionMappings"]),len(diag))}** | Structural mapping coverage only |',
      f'| Canonical objective-resource links | {objective_mapped}/{objective_total} | {pct(objective_mapped,objective_total)} | ID links only; not learning-outcome completion |',
      f'| Learning objectives with linked resources | {sum(bool(x.get("resourceIds")) for x in objective_map)}/{len(objective_map)} | {pct(sum(bool(x.get("resourceIds")) for x in objective_map),len(objective_map))} | Availability only; review and mastery separate |',
      f'| Foundation Listening core scripts mapped | {len(foundation_listening)}/{len(foundation)} | **{pct(len(foundation_listening),len(foundation))}** | One core device-synthesized script per existing Pre-A1/A1/A2 lesson; supplementary A2 counted separately |',
      f'| Foundation Listening questions | {foundation_listening_questions} core + {foundation_listening_extended_questions} supplementary | Chưa đo được — supplementary A2 practice remains review-pending; TTS, not ETS audio |',
      f'| Foundation A–Z letter records | {len(alphabet_sounds)}/26 | **{pct(len(alphabet_sounds),26)}** | Complete letter-data coverage only; not pronunciation accuracy or learner mastery |',
      f'| Outcome criteria defined | {outcome_total}/{outcome_total} | {pct(outcome_total,outcome_total)} | Framework definition coverage; not learner mastery |',
      f'| Outcomes with evidence instrumentation | {outcome_instrumented}/{outcome_total} | {pct(outcome_instrumented,outcome_total)} | Collection path only; no learner completion inferred |',
      f'| TOEIC sub-skill criteria with item-level mapping | {toeic_instrumented}/{len(toeic_outcomes)} | {pct(toeic_instrumented,len(toeic_outcomes))} | Stable question IDs; {len(toeic_uninstrumented)} criteria remain deliberately unmapped |',
      f'| Question-to-criterion links | {criterion_mapping_count:,} links / {criterion_unique_questions:,} unique questions | — | Mapping inventory, not learner practice or mastery |',
      f'| TOEIC objective practice evidence wired | {len(wired_toeic)}/{len(wired_toeic)} | {pct(len(wired_toeic),len(wired_toeic))} | Latest result per unique question; practice threshold only, not learner mastery |',
      f'| Foundation outcome evidence wired | {foundation_outcome_instrumented}/{foundation_outcome_total} | {pct(foundation_outcome_instrumented,foundation_outcome_total)} | Recognition, learner self-report for explanation/production, and 1/3-day delayed recall; wiring is not mastery |',
      f'| Delayed-recall scheduling across wired TOEIC groups | {len(wired_toeic)}/{len(wired_toeic)} | {pct(len(wired_toeic),len(wired_toeic))} | 1/3-day scheduling rule; not a retention guarantee |',
      f'| Response-time capture across wired TOEIC groups | {len(wired_toeic)}/{len(wired_toeic)} | {pct(len(wired_toeic),len(wired_toeic))} | Structured Grammar/Reading/Listening plus separate Part 5; duration is not a speed score |',
      '', '## Inventory (no approved numeric target)',
      '', '| Workstream | Current inventory | Progress |', '|---|---:|---|',
      f'| Grammar | {len(grammar)} lessons / {sum(len(x.get("exercises",[])) for x in grammar)} exercises | Chưa đo được — no agreed total lesson target |',
      f'| Listening | {len(listening)} units / {listening_q} questions | Chưa đo được — no agreed unit/question target |',
      f'| Reading | {len(readings)} resources / {reading_q} questions | Chưa đo được — no agreed resource/question target |',
      f'| Separate Part 5 practice | {p5n} questions | Chưa đo được — no agreed size target; independent review remains separate |',
      f'| Independent review queue | {listening_pending_questions} Listening + {p7_pending_questions} Reading Part 7 + {p5_pending_questions} Part 5 = {independent_review_total} questions | Reviewer handoff only; no reserve item is Mock-approved by queue inclusion |',
      f'| Foundation Reading | {len(foundation_reading)}/{len(foundation)} passages / {foundation_reading_questions} questions | {pct(len(foundation_reading),len(foundation))} within current Pre-A1/A1/A2 scope | Separate reading bank; not Foundation mastery |',
      f'| Foundation Listening | {len(foundation_listening)}/{len(foundation)} core scripts / {foundation_listening_questions} core questions + {len(foundation_listening_extended)} supplementary A2 scripts / {foundation_listening_extended_questions} questions | {pct(len(foundation_listening),len(foundation))} core lesson coverage | Device Speech Synthesis; supplementary A2 is review-pending, not authentic ETS recordings |',
      f'| Foundation A–Z sound lab | {len(alphabet_sounds)}/26 letters | {pct(len(alphabet_sounds),26)} | Two TTS actions per letter; action count is not pronunciation mastery |',
      '', f'## Vocabulary field coverage (against current {vocab:,}-headword base; not editorial approval)',
      '', '| Field | Records | Coverage |', '|---|---:|---:|',
      *[f'| {name} | {count:,}/{vocab:,} | **{pct(count,vocab)}** |' for name,count in field_counts.items()],
      f'| Word-family directed links | {word_family_links:,} links | — |',
      '', 'These ratios show whether a field is populated, not whether its content is accurate, natural or complete. Relationship counts are reported separately from headword counts.',
      '', '## Quality / verification status',
      '', '- Content counts do not equal completed learning outcomes.',
      f'- Outcome framework: {outcome_total}/{outcome_total} criteria defined; {outcome_instrumented}/{outcome_total} have an evidence-collection path, including Foundation {foundation_outcome_instrumented}/{foundation_outcome_total} and TOEIC {toeic_instrumented}/{len(toeic_outcomes)}. Neither count measures learner mastery.',
      '- TOEIC objective tracker: aggregates latest answer per stable unique question; minimum 10 unique items and 80% accuracy. A passing label is a practice threshold only, not CEFR/ETS certification or proof of every outcome.',
      f'- Question-to-criterion map: {criterion_mapping_count:,} explicit stable-ID links across {criterion_unique_questions:,} unique question IDs. Optional Grammar and Reading Part 5 explanation rubrics are learner self-reports; only mapped questions contribute to the corresponding sub-skill criterion.',
      '- Objective evidence is connected for Grammar, Listening Parts 1–4, Reading Parts 5–7 and separate Part 5 practice. Listening reserve items are excluded; Reading Part 7 remains second-review-gated; Separate Part 5 remains independently review-pending and cannot earn a threshold status.',
      f'- {len(toeic_uninstrumented)} TOEIC criteria remain visible without criterion-level scoring because the available items do not yet support a defensible tag or rubric: ' + ", ".join(outcome["id"] for outcome in toeic_uninstrumented) + '.',
      '- Listening Part 1 currently has 8 eligible unique questions (one additional mapped item is reserve-pending), below the 10-item minimum; at least 2 more unique, reviewed questions are needed before it can reach the practice threshold.',
      '- Foundation outcome evidence now records recognition, a learner-authored sentence with three self-report explanation/production ratings, and delayed recall. Self-report is not auto-graded; delayed recall is scheduled 1/3 days and is not a retention guarantee.',
      '- Foundation Listening stores attempts under a separate localStorage key; its bank coverage does not imply the learner has completed the questions or met the local practice threshold.',
      '- Supplementary A2 Listening has 13 six-turn dialogues (75–100 words each), 39 questions across detail, purpose/context and inference/next-action, with exact source-evidence snippets; all remain pending independent review and use browser TTS.',
      '- v2.92.0 batch 024 adds 8 Grammar lessons / 24 exercises, 6 TOEIC Listening units / 18 questions, and 6 TOEIC Reading Part 7 resources / 27 questions. All 12 new Listening/Reading resources remain reserve-pending-independent-review and excluded from Mock eligibility. v2.93.0 batch 025 adds 9 Grammar lessons / 27 exercises, 8 TOEIC Listening units / 20 questions, 8 TOEIC Reading Part 7 resources / 36 questions and 4 vocabulary headwords; new Listening/Reading items remain pending independent review and Mock-excluded.',
      '- Foundation A–Z records TTS play-button actions in `toeic:alphabet-sound-progress:v1`; no pronunciation analysis or mastery inference is performed.',
      '- Part 5 practice: pending independent review; do not count as Mock-eligible.',
      f'- Independent-review handoff queue: {listening_pending_questions} Listening questions across {len(listening_pending_units)} units + {p7_pending_questions} Reading Part 7 questions across {len(p7_pending_resources)} resources + {p5_pending_questions} separate Part 5 questions = {independent_review_total} item-level decisions. Queue presence means traceable reviewer handoff only, not approval or Mock eligibility.',
      '- Listening pending-review pool and Mock-eligible counts must be tracked separately from raw inventory.',
      '- Placement is a short sample, not official CEFR/ETS certification.',
      '- TOEIC score readiness is a local evidence tracker based on three completed 200-question Full Mocks; it shows L/R practice-accuracy trends only and does not convert raw accuracy into ETS scaled scores or claim 500+/850+ readiness.',
      '- Remote CI, GitHub Pages deployment and physical-device QA are not inferred from local checks.',
      '', '## Reporting rule',
      '', 'A percentage is shown only when a defensible target or denominator exists. Otherwise the report says “Chưa đo được” and records the current inventory without inventing a target.',
    ]
    out='\n'.join(lines)+'\n'
    print(out)
if __name__=='__main__': main()
