# TOEIC Dictionary v2.39.0 — Focused Test Report

**Release:** v2.39.0 — TOEIC Part 5 Grammar and Structure Expansion  
**Base:** v2.38.0  
**State:** local candidate; not remote-deployed or device-accepted.

## Change scope

- Separate Part 5 sentence-completion practice grows from 35 to 80 original questions.
- Batch 016 adds 45 items (`p5-sc-036`–`p5-sc-080`), each linked to a distinct pre-existing canonical vocabulary ID.
- All 80 items have a grammar category; 14 groups are represented.
- Stored answer positions are A/B/C/D = 20/20/20/20.
- Grammar category appears in the Focus Workspace question panel and answer-review detail.
- IndexedDB v1, question-ID seen history, vocabulary progress weighting, Reading Mock inventory and vocabulary headword count remain unchanged.

## Focused Python suites

| Suite | Result |
|---|---:|
| `test_sentence_completion.py` | 12/12 PASS |
| `test_pwa_readiness.py` | 3/3 PASS |
| `test_ci_coverage.py` | 2/2 PASS |
| `test_release_rotation.py` | 3/3 PASS |
| `test_sync_version.py` | 12/12 PASS |
| **Total** | **32/32 PASS** |

The Part 5 suite checks all 80 records for unique question/target IDs, canonical vocabulary links, one blank, four unique options, one key, four option-specific explanations, valid grammar tags, batch metadata, review status and A/B/C/D balance. It also checks selected ambiguity-sensitive constructions.

## JavaScript regression suites

All eight scripts passed:

1. `flashcard-image-policy.mjs`
2. `learning-focus-workspace.mjs`
3. `listening-tts-regression.mjs`
4. `mock-exam-engine.mjs`
5. `mock-ui-integrity.mjs`
6. `practice-progress.mjs`
7. `runtime-render-smoke.mjs`
8. `sentence-completion.mjs`

The sentence selector suite now runs each of the 80 records through the shuffle path and verifies that the correct option's explanation remains attached to the answer.

## Data, PWA and syntax validation

- `tools/validate-data.py`: 992 vocabulary records, 0 errors, 0 current warnings; legacy baseline debt remains informational.
- `tools/validate-learning-content.py`: 0 errors; 8 warnings remain because the source snapshot does not contain the user's original Part 1 JPG binaries. The 8 SVG fallbacks are present. These warnings predate v2.39 and are unrelated to Part 5.
- `tools/audit-toeic-coverage.py`: PASS; separate Part 5 practice bank reports 80 questions and 14 grammar groups.
- `tools/sync-version.py --check`: all registered version markers match v2.39.0.
- `tools/tests/test_pwa_readiness.py`: confirms app-shell/required assets, cache version and Part 1 fallback policy.
- `node --check sw.js` and syntax checks for every `assets/js/*.js`: PASS.

## Editorial status and boundary

- All 80 items remain `reserve-pending-independent-review`.
- The author pass corrected ambiguity-sensitive alternatives and confirmed structural/explanation alignment, but this is not a genuinely independent second-person review.
- Passing tests do not certify semantic uniqueness, naturalness or complete TOEIC authenticity for every item. Keep this bank for normal practice only; do not include it in Mock until an independent reviewer records an item-level decision.

## Not verified in this report

- Remote GitHub Actions execution.
- GitHub Pages deployment or cache propagation.
- Browser offline/reconnect behavior in a real browser.
- Physical iPhone/Android/tablet/desktop interaction.
- Second-person editorial approval.

This is targeted release verification, not a full-system acceptance declaration.
