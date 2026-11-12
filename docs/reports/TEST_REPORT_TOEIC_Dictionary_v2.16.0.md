# Test Report — TOEIC Dictionary v2.16.0

Date: 2026-11-10

## Main changes
- Stable `choiceIds` on 109 Reading questions, 102 Listening questions and 54 Grammar exercises.
- `legacyChoiceIds` retained for the 12 edited option groups so historical options do not collapse into replacement-option identities.
- Startup migration adds `choiceId` to valid existing progress records while retaining all prior fields and leaving invalid records untouched.
- GitHub Actions unit tests split into independently named steps; slow validator/version-sync steps have explicit 15-minute limits.

## Test accounting
- Baseline ID: 13/13 PASS
- Guarded patch: 11/11 PASS
- Version sync: 12/12 PASS
- Vocabulary validator unit tests: 33/33 PASS (24 completed in module run; remaining 9 executed individually because the sandbox module run stalled after the 24th test)
- Learning content: 24/24 PASS
- Dashboard layout: 6/6 PASS
- Design system: 13/13 PASS
- Question evidence: 4/4 PASS
- Distractor quality: 5/5 PASS
- Choice history: 5/5 PASS
- Learning detail scope: 3/3 PASS
- Choice identity: 7/7 PASS

Runtime render/migration smoke: PASS (Reading Part 5, Reading Part 7 multi-document, Grammar, legacy Reading/Listening/Grammar progress migration including archived choice identity).

Total: 136/136 test methods PASS. Note: the complete vocabulary-validator module did not finish in the local sandbox in one uninterrupted run; all 33 test methods were accounted for through module and isolated execution. GitHub Actions now runs that suite in its own step with a 15-minute timeout.

## Validators and audits
- `validate-data.py`: 928 vocabulary records, 0 errors, 12 known legacy warnings; 0 added/missing IDs.
- `validate-learning-content.py`: 0 errors, 0 warnings; Listening 102, Reading 109, Grammar 25/54.
- Coverage, answer-to-source evidence and distractor structural audits: PASS.
- `sync-version.py --check`: PASS at 2.16.0.

## Data safety
- 928 vocabulary IDs and 26 A–Z files preserved.
- No question order, answerIndex or option order changes.
- No IndexedDB version/store changes; no progress reset.
- Migration adds only `choiceId`; preserves `choiceIndex`, `choiceText`, `correct`, `answeredAt`; invalid records remain untouched.
- Archived option identities are separate from replacement option IDs for all 12 legacy-edited question groups.

## Remote/physical QA
- Remote GitHub Actions has not yet been re-run after push; the old one-line annotation does not expose its failing command.
- GitHub Pages deployment and physical iOS/Android/iPad/desktop QA remain pending.
