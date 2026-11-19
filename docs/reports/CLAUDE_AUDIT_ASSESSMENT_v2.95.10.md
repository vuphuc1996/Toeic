# Independent assessment of Claude's audit — v2.95.10

**Assessment date:** 2026-11-19  
**Code basis:** v2.95.9 source plus v2.95.10 local commits listed in the release logs.  
**Purpose:** distinguish reproducible measurements, reasonable interpretations and decisions that still require the project owner.

## 1. Executive assessment

Claude's three P0 findings are technically valid and are now addressed in separate commits. The proposed P1/P2 work is directionally sound, but not all numerical estimates should be treated as a release score. The strongest evidence is per-bank inventory, validator output, stable-ID protection, CI coverage and independent-review status—not a single “50% complete” number.

## 2. P0 — findings and disposition

| Claude finding | Independent evidence | Disposition |
|---|---|---|
| Vocabulary ID baseline has 928 IDs while current data has 1,141 | Before update: 1,141 unique current IDs, 213 additions and 0 missing. After update: baseline count 1,141; validator reports 0 additions / 0 missing; set SHA-256 `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b` | Fixed in its own commit. No vocabulary record was edited. |
| `patch-data.py` accepts protected paths and lacks per-patch whitelist | Test suite now rejects `/id`, `/word`, `/topics` (including descendants), missing `allowedPaths`, and any operation outside the allowlist; the whole batch is rejected. Every operation is written to the JSONL audit log. Historical patch allowlists were added without changing operation payloads. | Fixed in its own commit; 17/17 patch-data tests PASS. An additional safety fix restores original file bytes if the final `APPLIED`/`ROLLED_BACK` audit record fails after the atomic data replacement. |
| Service Worker calls `skipWaiting()` automatically | New worker waits on existing installations; only first install may auto-activate. `SKIP_WAITING` is sent from the explicit update-banner action. Simulator covers failed install/cache preservation, optional failures, namespace cleanup and 404 fallback. | Fixed in its own commit. Two-tab real-browser verification remains NOT TESTED. |

The fixes preserve the user's rules: immutable `/id`, `/word`, `/topics`; expected-old preconditions; dry-run; operation logs; rollback protection; no relaxation of validators; and version updates only via `tools/sync-version.py`.

## 3. Comparison of automated test inventory

- Claude reported 34 JavaScript suites and 427 Python tests on v2.95.8. The current source contains **37 JavaScript `.mjs` suites** and **54 Python test modules / 433 statically declared `test_*` methods** (counted via Python AST). The increase is consistent with three new JS suites since that baseline (`robot-buddy-streaming`, `flashcard-fixed-batch`, `service-worker-update`) and six additional patch-data safety tests.
- The current 37/37 JavaScript suites were executed and passed. The focused Python modules listed in the release test report completed and passed 67 cases. The entire 433-method Python inventory was **not** fully executed in this environment; `test_validator.py` and broad discovery exceeded execution limits. A static test-method count is inventory, not a pass claim.
- Therefore Claude's historical `427 passed in 7.9 seconds` result cannot be independently reproduced from the current environment; it should remain attributed to Claude's Python 3.12.3 / Node 22 execution. The current direct data validator itself passes against all 1,141 vocabulary records.

## 4. P1 — design-system assessment

The supplied counts (979 hex color values, 127 font-size values, 550/650/750/850/950 font weights, 46 border-radius values, 69 box shadows, 114 `!important` occurrences and 25 media-query widths) are plausible static-scan indicators of CSS fragmentation. They are **not independently reproducible from the Claude summary alone**, because the exact scan script, parser rules, selector normalization and treatment of repeated declarations were not supplied. They should be recorded as an initial scan, not a UI-quality score.

What is verified in the project source:

- `design/design-profile.json` contains 54 tokens and is named `Calm Study Blue` (`calm-study-blue`).
- Its status remains `proposed-default-awaiting-user-preferences`; it has not been approved or promoted by this release.
- Responsive behavior has three width boundaries: 640, 850 and 1,199 px. These boundaries form **four responsive bands** (phone, compact tablet, tablet/small desktop, large desktop); they are not four breakpoint boundary values.
- `python tools/sync-design-profile.py --check` passes with 54 tokens and 406 legacy typography-floor selector groups after the PWA banner was changed to use shared font tokens.

Recommendation: approve Calm Study Blue as the initial product design system, subject to actual browser review. Do not bulk-rewrite the CSS before desktop/mobile visual acceptance. Once approved, document token scales and add a selector/property-identified ratchet: legacy violations are warnings, only new violations are errors; then migrate one screen group at a time and tighten the baseline after each reviewed batch. The ratchet must not add exceptions or weaken existing validators.

## 5. P1 — external verification

Local simulation cannot prove GitHub Actions, GitHub Pages cache behavior, first/offline installation, update transitions in two real tabs, iOS Safari/Android Chrome TTS, or physical-device responsive behavior. Keep each item as `Chưa kiểm` until a dated browser/device result is recorded. Do not infer deployment success from a local green validator.

## 6. P2 — actual content coverage

### Vocabulary

- Current canonical vocabulary is 1,141 headwords. Against the project's 3,000 minimum planning target this is 38.0%; against 5,000 it is 22.8%. These are planning ratios, not an official ETS word-list completion score.
- Audited field coverage: US IPA 1,048/1,141 (91.8%); word-family 276 (24.2%); verb forms 329 (28.8%); collocations 971 (85.1%); synonyms 404 (35.4%); antonyms 213 (18.7%). Missing values are not automatically defects: add information only when it is supported by a reliable source and useful for learners.
- The 338/809 related-term entries without a definition are an editorial enrichment queue, not a reason to invent meanings.

### Listening and reading

- Listening inventory: 121 units / 239 questions. Current Mock-eligible pool: 102; independent-review pending: 137. Only one complete 100-question Listening form can be assembled without reusing question IDs; a second form would reuse 98 questions at the current eligible count.
- By Part: eligible P1/P2/P3/P4 = 8/25/39/30; pending = 1/28/60/48. The Part 1 learning-outcome tracker has a 10-unique-question practice threshold, while one Listening mock blueprint uses 6 Part 1 questions. These are different thresholds. Two non-repeating full forms require 12 Part 1 questions; even after all currently pending questions are approved, the bank would have 9 and remain short by 3.
- Reading inventory: 65 resources / 263 questions. The Part 7 bank contains 86 single-passage and 85 multiple-passage questions. Second review remains a separate editorial gate.
- Separate Part 5 practice has 80 questions and remains practice-only pending independent review. Supplementary Foundation A2 Listening/Reading (39 questions each) also remains review-pending. Automated structure checks do not approve these items for Mock use.

## 7. Recommendations for the project owner

1. **Visual style:** approve `Calm Study Blue` as the initial shared design profile. It already exists as a proposed 54-token profile; approval should follow a real browser review. No profile status has been changed by this release.
2. **Listening Mock target:** recommend a minimum of **two distinct, non-repeating 100-question forms** before describing the Listening Mock bank as broadly ready. This requires independent review of suitable pending items and at least three more approved Part 1 questions beyond the projected nine. Until then, label current capability as one eligible form, not two.
3. **Foundation / Sound Lab / outcome tracker vs vocabulary:** keep existing modules and learner evidence; do not delete them or discard work. Freeze expansion of new feature surfaces for now and prioritize (a) independent review of Listening/Reading/Part 5/Foundation reserves, then (b) vocabulary batches of 100–150 with reliable-source evidence and controlled patches. Do not fill metadata fields merely to reach 100%.

These are recommendations, not silent changes to approved scope. The design-profile status and the two-form target remain owner decisions. Detailed regenerated inventories are in `TOEIC_CONTENT_COVERAGE_v2.95.10.md`, `TOEIC_LISTENING_READINESS_v2.95.10.md` and `PROJECT_PROGRESS_SNAPSHOT_v2.95.10.md`.
