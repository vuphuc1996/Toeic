# Project Progress Baseline — v2.79.0

**Source version:** `2.79.0`  
**Baseline date:** 2026-11-16  
**Immediate base:** v2.78.0

## Product inventory

| Area | Inventory / state | Interpretation |
|---|---:|---|
| Vocabulary | 1,137 headwords | 37.9% of the internal 3,000 minimum; 22.7% of the 5,000 planning ceiling |
| Guided Foundation | 23 lessons: 10 Pre-A1/A1 + 13 A2 | Stage presence is 3/6; not stage completion |
| Foundation Reading | 23 passages / 59 questions | A2: 13 passages / 39 questions |
| Foundation Listening | 23 device-TTS scripts / 59 questions | A2: 13 four-turn dialogues / 39 questions; synthesized speech, not ETS audio |
| A2 contextual production | 13 task definitions / 13 lesson links | Each task requires at least eight words and three self-review ratings |
| Objective-resource map | 294/294 records; 11/11 objectives linked | Structural mapping coverage only |
| Learning-outcome framework | 33 criteria defined; 6 have an evidence path | 6/33 = 18.2% instrumentation, not mastery |
| Foundation outcomes | 6/6 evidence paths wired | Recognition, self-reported explanation/production and delayed recall |
| Foundation A–Z | 26/26 letters | Data coverage, not pronunciation mastery |

## Vocabulary field coverage

| Field | Records | Coverage |
|---|---:|---:|
| US IPA | 1,044/1,137 | 91.8% (93 blank; left unresolved rather than guessed) |
| Word family | 276/1,137 | 24.3% |
| Verb forms | 325/1,137 | 28.6% |
| Collocations | 967/1,137 | 85.0% |
| Synonyms | 404/1,137 | 35.5% |
| Antonyms | 213/1,137 | 18.7% |
| Word-family directed links | 374 | Relationship count, not headword count |

## A2 change in this release

The 13 A2 production prompts use distinct `::produce1` keys, while former `::apply1` records remain preserved. v2.79.0 adds three task-specific revision checks and response-to-response history. New attempts save response text; revisions store the previous and revised text with learner self-review. Historical attempt rows are not backfilled. No IndexedDB schema or localStorage key change is made.

## Reporting boundaries

There is no defensible single overall product-completion percentage. Counts and instrumentation ratios do not establish editorial approval, learner completion, CEFR attainment or ETS equivalence. See `PROJECT_PROGRESS_SNAPSHOT_v2.79.0.md` for the generated inventory and quality caveats.
