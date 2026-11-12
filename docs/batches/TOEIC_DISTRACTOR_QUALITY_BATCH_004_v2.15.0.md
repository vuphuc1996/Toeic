# TOEIC Distractor Quality Batch 004 — v2.15.0

**Date:** 10/11/2026  
**Scope:** TOEIC Listening Part 3–4 and Reading Part 7; distractor plausibility and answer uniqueness.  
**Baseline:** v2.14.0.  
**Status:** Applied locally; 126/126 unit-test methods and local validators/audits pass; final ZIP verification is documented in the release report; not deployed.

## Work completed

- Manually reviewed 132 questions with their full transcript/passage, keyed response and three distractors: Listening Part 3 (39), Part 4 (30), Reading Part 7 (63). This scope contains the 126 direct/lexical source-evidence items and six paraphrase/inference questions identified by the prior evidence map.
- Reviewed the key's source support, whether only one option is defensible, grammar/semantic fit, distractor relevance and possible second-correct-answer risk.
- Rewrote 12 question option groups to use distractors closer to the same context: hotel booking, presentation preparation, intended employee groups, travel reimbursement records, refund/return requests, invoice verification, supplier/order enquiries, meeting materials and visitor-access arrangements.
- Kept each updated question's original `answerIndex`, correct answer text, question ID, item order and question count. Added `legacyChoices` snapshots for the 12 revised questions and a backwards-compatible `choiceText` field on new Reading/Listening attempts, so older `choiceIndex` history continues to display the exact original distractor text. No IndexedDB object-store/schema migration or progress reset was performed.
- Added `tools/audit-distractors.py`, generated `docs/reports/TOEIC_DISTRACTOR_AUDIT_v2.15.0.md`, and added five distractor plus five saved-choice-history regression tests.

## Important answer-position finding

Current answer-index distribution is uneven:

| Part | A | B | C | D |
|---|---:|---:|---:|---:|
| Listening Part 3 | 10 | 18 | 10 | 1 |
| Listening Part 4 | 9 | 12 | 7 | 2 |
| Reading Part 7 | 13 | 27 | 19 | 4 |

The answer positions were **not shuffled** in this batch. The runtime stores historical selections as `choiceIndex` in `readingProgress` and `listeningProgress`; changing choice order without stable choice IDs and migration would corrupt how historical selections are displayed. Future rebalancing must first migrate to stable option identity/choice text and convert legacy saved indices safely.

## Scope protection

- Listening remains 102 questions; Reading remains 109 questions; all IDs, question order and answer keys remain stable.
- The 928 vocabulary records, 26 A–Z files, grammar lessons, design system and PWA app shell remain unchanged except version metadata and audit/test tooling.
- The review is internal editorial work on original-authored questions. It is not a second independent editor's signoff, psychometric analysis, difficulty calibration, official ETS content or proof of score equivalence.

## Next actions

1. Design a stable `choiceId`/choice-text progress format and a non-destructive migration for legacy `choiceIndex` records.
2. Only after migration tests pass, rebalance answer positions by Part with no obvious pattern and verify saved progress/history.
3. Complete second-editor review, physical responsive/audio QA and then implement the timed Full Mock engine.
