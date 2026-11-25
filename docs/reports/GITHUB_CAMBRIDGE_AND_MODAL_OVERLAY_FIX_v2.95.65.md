# GitHub Batch 035 and single modal overlay repair — v2.95.65

## Source of truth

- Predecessor: `TOEIC_Dictionary_v2.95.64_FullSource.zip`
- SHA-256: `03ec4c80e88bc76e435cfc0782e933474be882a4f271318a23375a35e9242673`
- ZIP integrity: PASS before extraction and editing.
- No older FullSource, alternate branch, stale extracted folder or Patch was used as a source baseline.

## 1. GitHub Batch 035 test failures

The hosted run selected two files via `test_related_glossary_batch_035*.py`. The split module `test_related_glossary_batch_035_cambridge.py` was absent from the official v2.95.64 FullSource but existed in the hosted checkout. Its three failed assumptions were historical-data errors:

1. It compared the current `article` glossary row with the original Batch 035 `new` operation, ignoring the subsequent reviewed correction operation. The replacement reconstructs the original row from the Batch 035 ledger and then applies later correction sets before comparing with current data.
2. It expected the 553-row glossary snapshot and an old base hash without reversing subsequent batches/corrections. The replacement reverses the later glossary additions and correction operations through the historical helper and verifies the resulting exact Batch 035-era inventory/hash.
3. It expected current glossary size to equal the historical count. The test now asserts the historical post-Batch-035 count separately and only requires current normalized terms to remain unique and include the historical terms.

The eight original Batch 035 Cambridge records, original canonical relationship anchors, source URLs, ledger parity, patch inventory and pre-batch hash remain strictly asserted. No glossary data was rewritten to satisfy the tests. The GitHub workflow selector remains `test_related_glossary_batch_035*.py` and the replacement module now exists in FullSource.

## 2. Single shared modal overlay

- Removed the separate `modalBackdrop` element and `.modal-backdrop` visual selector.
- `learningFocusBackdrop` remains the one full-screen dimming/blur root.
- `modalLayer` is nested inside that root and acts only as a transparent panel layer.
- In modal-only mode, `is-modal-only` hides the learning-focus dialog and shows the modal panel within the shared root.
- During focused learning, a modal overlays the active workspace; closing that modal does not close the workspace.
- Shared show/hide logic updates `hidden`, `aria-hidden` and body scroll state. The `[hidden]` CSS specificity prevents stale visible layers without introducing new `!important` overrides.
- Added `test_single_overlay_contract.py`, the Node modal-dismissal simulation and a focused workflow step.

## 3. Data and UI boundaries

No vocabulary/Related Glossary records, headwords, IDs, synonyms/antonyms, question IDs, choice IDs/order, answer keys, Mock eligibility, learner IndexedDB data/schema or Robot Buddy data boundary changed. UI layout was not redesigned. GitHub Pages/GitHub-only hosting remains; no Cloudflare/backend was introduced.

## 4. Manual acceptance steps

1. Open a normal vocabulary detail/editor modal; verify one dimming layer, modal content and close button.
2. Start a Flashcard or Practice focused session, then open an explanation/result modal; verify only one dimming layer is visible.
3. Close the nested modal using X and Escape; verify the same focused session/question remains.
4. Close the focused session; verify the shared overlay disappears and body scrolling is restored.
5. Complete a practice set; verify the result modal still shows Đúng / Chưa đúng / Tổng câu and the existing confirmation flow.
6. On GitHub, run the exact command `python -m unittest discover -s tools/tests -p 'test_related_glossary_batch_035*.py' -v`; expected: 10 tests, zero failures.

## 5. Verification boundary

Local regression and validator results are in `TEST_REPORT_TOEIC_Dictionary_v2.95.65.md`. GitHub-hosted Actions, deployed GitHub Pages, installed-PWA cache/offline and physical device behavior are not claimed as tested in this environment.
