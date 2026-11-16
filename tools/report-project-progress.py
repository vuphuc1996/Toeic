#!/usr/bin/env python3
"""Generate a target-based progress snapshot from canonical project data."""
from __future__ import annotations
import json
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
    foundation_listening=load('data/learning-path/foundation-listening.json')['clips']
    foundation_reading=load('data/learning-path/foundation-reading.json')['passages']
    p5=load('data/practice/part5-sentence-completion.json')
    objective_map=load('data/learning-path/objective-resource-map.json')['objectives']
    wired_toeic=[x for x in objective_map if x.get('kind') in {'grammar','listening','reading','practice'}]
    foundation_objectives=[x for x in objective_map if x.get('kind')=='learning_path']
    outcome_registry=load('data/learning-path/objective-outcomes.json')
    outcome_objectives=outcome_registry['objectives']
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
    foundation_listening_questions=sum(len(x.get('questions',[])) for x in foundation_listening)
    foundation_reading_questions=sum(len(x.get('questions',[])) for x in foundation_reading)
    # Field-level metadata coverage is reported against the current headword base, not as a project target.
    vocab_files=[ROOT / x['file'].replace('./','',1) for x in manifest['letters']]
    vocab_records=[]
    for path in vocab_files:
        vocab_records.extend(json.loads(path.read_text(encoding='utf-8')).get('words', []))
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
      f'| Guided pathway stages represented | {len(stages)}/6 | Pre-A1, A1, A2, B1, B2, C1 | **{pct(len(stages),6)}** | Stage presence only; not full-stage completion |',
      f'| Placement question mapping | {len(load("data/learning-path/placement-objective-map.json")["questionMappings"])}/{len(diag)} | All diagnostic questions | **{pct(len(load("data/learning-path/placement-objective-map.json")["questionMappings"]),len(diag))}** | Structural mapping coverage only |',
      f'| Canonical objective-resource links | {objective_mapped}/{objective_total} | {pct(objective_mapped,objective_total)} | ID links only; not learning-outcome completion |',
      f'| Learning objectives with linked resources | {sum(bool(x.get("resourceIds")) for x in objective_map)}/{len(objective_map)} | {pct(sum(bool(x.get("resourceIds")) for x in objective_map),len(objective_map))} | Availability only; review and mastery separate |',
      f'| Foundation Listening scripts mapped | {len(foundation_listening)}/{len(foundation)} | **{pct(len(foundation_listening),len(foundation))}** | One device-synthesized script per existing Pre-A1/A1/A2 lesson |',
      f'| Foundation Listening questions | {foundation_listening_questions} | Chưa đo được — current inventory is 3 questions per A2 lesson and 2 per Pre-A1/A1 lesson; TTS practice, not ETS audio |',
      f'| Foundation A–Z letter records | {len(alphabet_sounds)}/26 | **{pct(len(alphabet_sounds),26)}** | Complete letter-data coverage only; not pronunciation accuracy or learner mastery |',
      f'| Outcome criteria defined | {outcome_total}/{outcome_total} | {pct(outcome_total,outcome_total)} | Framework definition coverage; not learner mastery |',
      f'| Outcomes with evidence instrumentation | {outcome_instrumented}/{outcome_total} | {pct(outcome_instrumented,outcome_total)} | Collection path only; no learner completion inferred |',
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
      f'| Foundation Reading | {len(foundation_reading)}/{len(foundation)} passages / {foundation_reading_questions} questions | {pct(len(foundation_reading),len(foundation))} within current Pre-A1/A1/A2 scope | Separate reading bank; not Foundation mastery |',
      f'| Foundation Listening | {len(foundation_listening)}/{len(foundation)} scripts / {foundation_listening_questions} questions | {pct(len(foundation_listening),len(foundation))} within current Pre-A1/A1/A2 scope | Device Speech Synthesis; not authentic ETS recordings |',
      f'| Foundation A–Z sound lab | {len(alphabet_sounds)}/26 letters | {pct(len(alphabet_sounds),26)} | Two TTS actions per letter; action count is not pronunciation mastery |',
      '', f'## Vocabulary field coverage (against current {vocab:,}-headword base; not editorial approval)',
      '', '| Field | Records | Coverage |', '|---|---:|---:|',
      *[f'| {name} | {count:,}/{vocab:,} | **{pct(count,vocab)}** |' for name,count in field_counts.items()],
      f'| Word-family directed links | {word_family_links:,} links | — |',
      '', 'These ratios show whether a field is populated, not whether its content is accurate, natural or complete. Relationship counts are reported separately from headword counts.',
      '', '## Quality / verification status',
      '', '- Content counts do not equal completed learning outcomes.',
      f'- Outcome framework: {outcome_total}/{outcome_total} criteria defined; {outcome_instrumented}/{outcome_total} have an evidence-collection path. Neither count measures learner mastery.',
      '- TOEIC objective tracker: aggregates latest answer per stable unique question; minimum 10 unique items and 80% accuracy. A passing label is a practice threshold only, not CEFR/ETS certification or proof of every outcome.',
      '- Objective evidence is connected for Grammar, Listening Parts 1–4, Reading Parts 5–7 and separate Part 5 practice. Reserve Listening items are excluded until editorial review; Reading Part 7 remains second-review-gated; the separate 80-item Part 5 practice pool is review-pending and cannot earn a threshold status.',
      '- Listening Part 1 currently has 8 eligible unique questions (one additional mapped item is reserve-pending), below the 10-item minimum; at least 2 more unique, reviewed questions are needed before it can reach the practice threshold.',
      '- Foundation outcome evidence now records recognition, a learner-authored sentence with three self-report explanation/production ratings, and delayed recall. Self-report is not auto-graded; delayed recall is scheduled 1/3 days and is not a retention guarantee.',
      '- Foundation Listening stores attempts under a separate localStorage key; its bank coverage does not imply the learner has completed the questions or met the local practice threshold.',
      '- Foundation A–Z records TTS play-button actions in `toeic:alphabet-sound-progress:v1`; no pronunciation analysis or mastery inference is performed.',
      '- Part 5 practice: pending independent review; do not count as Mock-eligible.',
      '- Listening pending-review pool and Mock-eligible counts must be tracked separately from raw inventory.',
      '- Placement is a short sample, not official CEFR/ETS certification.',
      '- Remote CI, GitHub Pages deployment and physical-device QA are not inferred from local checks.',
      '', '## Reporting rule',
      '', 'A percentage is shown only when a defensible target or denominator exists. Otherwise the report says “Chưa đo được” and records the current inventory without inventing a target.',
    ]
    out='\n'.join(lines)+'\n'
    print(out)
if __name__=='__main__': main()
