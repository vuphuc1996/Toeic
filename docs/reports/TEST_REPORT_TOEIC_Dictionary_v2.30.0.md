# Test Report — TOEIC Dictionary v2.30.0

**Base:** v2.29.0  
**Scope:** repeatable Reading/Listening/Grammar attempts with history, Vocabulary Batch 020, release/version rotation and regression protection.  
**Status:** local release candidate. Remote CI/Pages and physical-device QA are not claimed.

## Implemented

### Practice retry and attempt history

- Reading, Listening and Grammar now expose **Làm lại câu này** after a submitted answer.
- Each lesson exposes **Làm lại toàn bộ bài** when there are current submitted answers; a confirmation names the number of answers to reopen.
- Reopening a question archives its former answer instead of deleting it. The choice buttons become available again.
- Each attempt stores selected choice, stable `choiceId`, correctness, expected answer, explanation, timestamp and attempt number. Earlier attempts are shown under the question.
- Progress coverage counts unique question indices, not attempts. Part accuracy uses each question's latest submitted attempt; a separate attempt count is displayed.
- The old `answers` layout remains compatible. Additive `attemptHistory` is stored inside the same existing progress object; IndexedDB stays `toeic-vocabulary-phase1`, version 1, store `workspace`.
- Choice-identity reconciliation covers both current answers and archived attempts.

### Vocabulary Batch 020

- Adds 13 non-duplicate headwords; canonical total 979 → 992.
- Existing IDs preserved; 13 new IDs added.
- A–Z JSON remains the only runtime vocabulary store; `batch-008.json` is provenance.
- US IPA is omitted for `consignor` and `receivable` because the checked Cambridge pronunciation entries do not provide a US transcription. Other IPA is included only where source-backed.
- CEFR remains an editorial estimate pending review.

## Verification record

| Check | Result | Notes |
|---|---|---|
| JavaScript syntax (`app.js`, `practice-progress.js`, `sw.js`) | PASS | All three files pass `node --check` |
| Practice attempt helper tests | PASS | `practice-progress.mjs`: per-question/full-set retry, history, latest-result analytics and legacy v1 compatibility |
| Shared learning workspace regression | PASS | Batch 020 inclusion, retry controls, common learning shell and stable IDs |
| Runtime render smoke | PASS | End-to-end retry for Reading, Listening and Grammar; attempt history and choice-ID migration |
| Listening/TTS regression | PASS | Voice selection, pauses, playback rate, safe cancellation unchanged |
| Mock engine and UI integrity | PASS | 15/60/120-minute modes, blueprint, unique form IDs and persistent usage ledger unchanged |
| Targeted Python unit tests | PASS — 147 tests across 18 modules | Design System, learning scope, dashboard, version sync, learning content, vocabulary examples, patch data, rotation, choice history/identity, baseline IDs, editorial, distractor, evidence, remaining content, answer balance, collocation cleanup and Part 1 photo checks |
| `python tools/validate-data.py` | PASS | 992 canonical headwords, 0 errors / 0 legacy warnings; 642 US IPA records, 822 collocations |
| `python tools/validate-learning-content.py` | PASS with 8 warnings | 0 errors; warnings are the 8 Part 1 JPG binaries absent from this snapshot |
| `python tools/sync-version.py --check` | PASS | Every registered version marker is 2.30.0 |
| Release rotation dry-run | PASS | Only v2.28.0 batch/report notes are planned for retirement; v2.29.0 + v2.30.0 retained |
| Release rotation apply | PASS | Historical entries are compacted into `archive/PROJECT_HISTORY.md`; old release docs retired |
| Part 1 asset validator (`--allow-missing`) | PASS with 8 warnings | All 8 records and attribution rows are valid; 0/8 JPG bytes in this snapshot. Strict photo gate is NOT passed |

The complete `test_validator.py` unittest module was not included in the 147-test count: its long subprocess-based run exceeded the execution window. The production CLI validator above completed successfully. No claim of full `unittest discover` is made.

## Package verification

- Full Source: 160 files (excludes transient Python cache directories).
- Update Overlay: 37 changed/added files (8 new + 29 modified); no delete directives.
- Four v2.28.0 release-specific notes are retired by the documented release-rotation script after the overlay is applied; the ZIP itself contains no direct delete operations.
- **PASS:** ZIP CRC and clean extraction for both archives; applying the 37-file overlay to a clean v2.29.0 Full Source, then running the release rotator, produced a tree that matches the 160-file v2.30.0 Full Source byte-for-byte.
- SHA-256 sidecars are included for integrity verification.

## Not verified / blockers

- Physical desktop, tablet, iPhone Safari and Android Chrome interaction remains pending.
- Remote GitHub Actions and GitHub Pages deployment remain pending.
- Snapshot lacks the eight Part 1 JPG binaries. Preserve copies already on the user's GitHub repository; SVG fallbacks remain in the shell. Strict photo validation is not passed here.
- No personal IndexedDB profile was imported, exported, inspected, reset or migrated.
- Vocabulary CEFR and editorial quality still require review; automated validation proves structure, not semantic correctness.
