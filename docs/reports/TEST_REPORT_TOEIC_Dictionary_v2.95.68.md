# Test Report — TOEIC Dictionary v2.95.68

## Source baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.67_FullSource(1).zip`.
- Predecessor SHA-256: `1f262ac4d67d8d244facf397b9ea1d179c6a741f50e561b3d3e9805efef31754`.
- Baseline archive: 807 files; ZIP CRC integrity check passed.
- Release version: `2.95.68`.
- The source was not pushed to GitHub or deployed to GitHub Pages during this local run.

## Requested fixes and focused evidence

| Area | Result | Evidence |
|---|---:|---|
| Assessment result inside active Learning Focus | **PASS** | `assessment-result-focus-workflow.mjs`; `test_single_overlay_contract.py` |
| Redundant `modalLayer` result popup | **PASS** | In active Learning Focus, `#modalLayer` remains hidden; result uses existing `#learningFocusDialog` |
| Restore prior Learning Focus content/header/ARIA | **PASS** | Node workflow simulation verifies hidden/inert/ARIA state and exact restoration |
| Confirmation action | **PASS** | Inline confirm and Learning Focus X dispatch through existing `confirmPendingAssessmentResult` path |
| Confetti duration | **PASS** | CSS duration 2.4 s + stagger up to 0.48 s (approximately 2.88 s overall); reduced-motion rule retained |
| Batch 036 historical checksum | **PASS** | 6/6; reconstructed canonical SHA matches ledger `8c35a6fce159d056832f1e7c6ab395a5dd1d1b34d94e371cb464d6ae1bef11a2` |
| Word Family audit release heading | **PASS** | 1/1; heading now reads current manifest release `v2.95.68` |

A previously visible `modalLayer` is hidden before the inline result is shown. The HTML `#modalLayer` host remains in the app because other modal-only and nested-review workflows use it. This fix prevents the assessment-result flow from opening that host over an active Learning Focus dialog; it does not remove the shared modal infrastructure used elsewhere.

## Validators and syntax

| Check | Result |
|---|---:|
| `python tools/validate-data.py` | **PASS** — 1,141 records; IDs +0 / -0; 0 errors / 0 warnings |
| `python tools/validate-learning-content.py` | **PASS** — 0 errors / 0 warnings |
| `python tools/validate-part1-photo-assets.py` | **PASS** — 9/9 |
| `python tools/sync-version.py --check` | **PASS** — all 18 release markers |
| `python tools/audit-repository-integrity.py` | **PASS** — 408 references/data files; 0 errors / 0 optional warnings |
| `python tools/audit-design-tokens.py` | **PASS** — 0 new violations; 2,773 legacy warnings remain |
| `python -m compileall -q tools` | **PASS** |
| `node --check sw.js` and every `assets/js/*.js` (ES-module syntax check) | **PASS** |
| Node regression scripts | **PASS** — 44/44; 0 failed |

## Python suites completed

| Test module | Result |
|---|---:|
| `test_vocabulary_family_batch_025.py` | 5/5 PASS |
| `test_related_glossary_batch_036.py` | 6/6 PASS |
| `test_related_glossary_batch_037.py` | 7/7 PASS |
| `test_related_glossary_merge_038.py` | 8/8 PASS |
| `test_single_overlay_contract.py` | 3/3 PASS |
| `test_baseline_ids.py` | 13/13 PASS |
| `test_word_family_graph_audit.py` | 1/1 PASS |
| `test_choice_identity.py` | 9/9 PASS |
| `test_choice_history.py` | 5/5 PASS |
| `test_answer_position_balance.py` | 4/4 PASS |
| `test_learning_content.py` | 34/34 PASS |
| **Total focused Python** | **95/95 PASS** |

## Full Python discovery — incomplete

- `python -m unittest discover -s tools/tests -v` was attempted against the complete discovered test suite.
- The process exceeded the available execution window before emitting the final unittest summary. The partial stream contained running test cases but no terminal `Ran ...` / `OK` / `FAILED` summary.
- Therefore, the full Python test inventory is **INCOMPLETE**. The 95 focused Python tests above are completed results only; they are not represented as full-suite coverage.

## Data preservation

- The `data/` subtree contains 68 files. Relative paths are identical to the uploaded predecessor; after normalizing only `data/manifest.json.version` back to `2.95.67`, the complete data-tree composite SHA is identical.
- 1,141 canonical IDs remain exactly equal to the pinned baseline; no additions, removals or duplicate headwords.
- The four protected Grammar, Listening, Reading and Part 5 bank files match their existing historical composite SHA. Choice-identity, answer-position, choice-history and learning-content test modules also pass.
- No learner IndexedDB schema/records, question/choice IDs, answer keys, Mock eligibility, or Robot Buddy privacy boundary were changed.

## External / device acceptance — unverified

- GitHub-hosted Actions, GitHub Pages deployment, service-worker update behavior on an already-installed PWA, real offline/cache propagation and physical iOS/iPadOS/Android device behavior were not executed in this local session.
- No claim of production deployment acceptance is made.
