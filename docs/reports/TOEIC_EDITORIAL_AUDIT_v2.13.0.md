# TOEIC Editorial Audit — v2.13.0 (Pass 1)

- **Date:** 2026-11-10
- **Baseline:** v2.12.0
- **Scope:** 211 original TOEIC-style questions — 102 Listening and 109 Reading.
- **Status:** First audit pass completed with targeted editorial corrections; final semantic signoff remains open.

## Audit coverage

| Check | Scope | Result |
|---|---:|---|
| Listening question objects | 102 | Scanned |
| Reading question objects | 109 | Scanned |
| Duplicate option text within an item | 211 items | 0 exact duplicates found after correction |
| Answer choice indexes | 211 | Validated by learning-content validator |
| Rationale text | 211 | Vietnamese wording check strengthened; all tests pass |
| Part 1 illustration consistency | 8 | Prompt now correctly says “illustration”; 8 image-specific rationales name A–D |
| Part 2 invoice distractor quality | 1 targeted item | Reworked two overlapping options |

The automated language gate checks for Vietnamese diacritics **and** Vietnamese explanatory/connective words. This prevents an accented English token such as “résumé” from being treated as a Vietnamese explanation. The gate is a practical regression check, not a full language classifier.

## Corrections recorded

1. `part1-meeting-documents`, `part1-warehouse-box`, `part1-technician-inspection`, `part1-airport-suitcase`, `part1-presentation-room`, `part1-reception-plant`, `part1-restaurant-setting`, `part1-photocopier`: the learner prompt no longer calls SVG illustrations photographs; runtime/CSS naming now uses illustration semantics. Explanations remain specific to each image and identify its correct option letter.
2. `part2-invoice-approval`: removed two distractors that both pointed to the revised total on page two; alternatives now represent distinct invoice workflow actions.
3. `part2-supplier-samples`: changed the tag question to “The supplier promised …, didn't they?” and the response to “They did, but …” to make the agreement unambiguous.
4. `part2-contract-review`: retained an explicit “Yes” plus the fact that final comments were sent, making completed review status clear.
5. Selected Part 2/3/4 explanations were expanded or rewritten in Vietnamese when they were terse or merely repeated an English clue.
6. Remaining legacy English Reading rationales were localized; selected P5/P6/P7 rationales now explain the grammatical, textual or document clue more directly.

## What this audit does not certify

- A string-level scan cannot prove that a transcript or document logically entails every keyed answer.
- A Vietnamese-word heuristic cannot judge translation quality, pedagogy or naturalness.
- It is not an external instructor/native-speaker review and does not establish psychometric difficulty or distractor discrimination.
- Part 1 remains SVG illustration content, and Listening remains browser SpeechSynthesis, not licensed photography or recorded/ETS audio.

## Next editorial gate

Pass 2 must independently cross-check every answer key against the actual transcript or source document(s), especially Part 7 cross-document questions and Part 5 grammar contrasts. Record each verified/corrected stable item ID. Only after that gate should the content pool be approved for Full Mock assembly.
