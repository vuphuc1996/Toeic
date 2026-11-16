# Foundation A2 Contextual Production Tasks — v2.78.0

## Scope

This release adds one learner-authored writing task to each of the 13 guided A2 lessons. The tasks are contextualized around ordinary workplace interactions. Each has a stable task ID (`<lesson-id>::produce1`), scenario, instruction, three content requirements, a sentence frame, three task-specific self-review criteria and a collapsed model-answer example.

- Task definitions: **13/13**.
- Minimum response length: **8 words** for A2.
- Model answers: hidden in a collapsed disclosure until opened by the learner.
- Assessment: learner self-report only; no automatic grammar scoring, CEFR certification or mastery inference.
- Storage: existing `productionEvidence` collection in `toeic:foundation-progress:v1`; no new localStorage key or IndexedDB migration.

## Task inventory

| Lesson | Context / communicative purpose | Language focus |
|---|---|---|
| Polite requests | Ask a coworker to send meeting notes before a deadline | Could you please; Thank you |
| Quantities | Report remaining folders and printer ink | a few; a little; countable / uncountable nouns |
| Comparisons | Recommend one of three delivery routes by duration | comparative and superlative forms |
| Past work events | Report completing and sending a sales report yesterday | Past Simple |
| Present Continuous | Describe two coworkers' current activities | am/is/are + V-ing |
| Obligation and permission | Explain visitor registration and escorted access | must; can |
| Directions | Guide a visitor from reception to a training room | go straight; turn left; opposite |
| Invitations and offers | Offer to make copies and invite a colleague to review | Shall I; Would you like |
| Sequencing | Explain a three-step document approval workflow | first; next; finally |
| Plans and intentions | Tell the team about a Friday system update | be going to / present plan |
| Present Perfect | Confirm a newly uploaded report and ask about review | have/has + V3; current result |
| Passive Voice | Explain badge checks and replacements | present/past be + V3 |
| Defining Relative Clauses | Identify a records colleague and a shared-drive form | who; which; that |

## Evidence and backward compatibility

The new A2 writing task uses a new `::produce1` task ID; the pre-existing general application task remains `::apply1`. The application stores the new and old records inside the existing local Foundation progress structure. Existing `::apply1` responses are neither deleted nor overwritten and are not credited as completion of the new task. The lesson UI explains this distinction when a legacy response exists.

Pre-A1/A1 continues to use the prior `::apply1` task and generic three-word minimum. A2 requires eight words and uses its own tailored rubric. The writing prompt, sentence frame and model answer are authored support; a learner may write a different valid response. Self-ratings do not represent machine evaluation.

## Integrity and tests

- Immutable task-content digest baseline: `tools/foundation-a2-production-baseline-v2.78.0.json`.
- Dedicated JavaScript evidence/UI test: `tools/tests/foundation-a2-production.mjs`.
- Dedicated Python tests: `tools/tests/test_foundation_a2_production.py`.
- Outcome evidence regression: `tools/tests/foundation-outcome-evidence.mjs` and `test_foundation_outcome_evidence.py`.
- The tests validate all 13 task contracts, separate IDs, minimum-word validation, tailored rubric/model-answer completeness, production evidence aggregation, and preservation/non-reuse of legacy records.

## Limitations

The model answer is illustrative rather than exclusive. The app does not automatically assess grammar, vocabulary range, coherence, naturalness or task completion. These 13 tasks need independent linguistic/editorial review and learner usability testing before they can be treated as validated assessment material.
