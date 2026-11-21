# Test Report — TOEIC Dictionary v2.95.36


## Scope
Related Glossary Batch 032: sourced definition/POS recovery for six existing terms. No UI, canonical vocabulary IDs, relation arrays, learning questions/answers, or IndexedDB schema/progress was intentionally modified.

## Changes
- `account`, `acknowledgment`, `acquire`, `adaptable`, `advance`, `advantage` receive paraphrased English definitions, POS, source label, and source URLs.
- Vietnamese meanings preserved exactly.
- Batch ledger and four focused regression tests added.

## Source and editorial status
Cambridge Dictionary/Learner's/School Dictionary excerpts or pages were consulted for the definitions. Definitions are paraphrases rather than copied entries. External independent review is still pending; these additions are not marked independently reviewed.

## Validation status
Focused tests and project validators are run during this release build. Full Python discovery, browser/device acceptance, live Pages deployment, and independent review are not claimed unless their results are explicitly appended below.

## Validation results
- Batch 032, candidate audit, and glossary quality audit focused tests: **19/19 PASS**.
- JavaScript regression files: **39/39 PASS**.
- Vocabulary validator: **0 errors, 0 warnings**.
- Learning-content validator: **0 errors, 0 warnings**.
- Repository integrity preflight: **407 files/references checked, 0 errors, 0 warnings**.
- Version synchronization: **PASS**.
- Full Python discovery: **incomplete; command exceeded the execution window while running test_patch_related_terms. No full-suite pass is claimed**.
- Browser/device testing, remote CI and Pages deployment: **not run**.

## Glossary audit after batch
- 519 terms; 150 missing definitions; 73 placeholder definitions; 217 missing POS; 75 entries flagged for missing source; 0 duplicate normalized terms.
- Quality report flags 227 entries; priority counts High 223 / Medium 2 / Low 2 (categories overlap at issue-level; priority categories are exclusive).

## Source evidence
- Account/acquire: Cambridge Learner's Dictionary sample excerpt (mirror/excerpt): https://www.yumpu.com/en/document/view/11808737/cambridge-university-press-9781107660151-cambridge- ; https://drupal-s3fs-prod.s3.eu-west-1.amazonaws.com/files/9113/8071/5737/cambridge-learners-dictionary4-intermediate-paperback-with-cd-rom-sample-pages.pdf
- Acknowledgment: Cambridge Learner's Dictionary sample excerpt: https://fliphtml5.com/uydxs/lmob/9781107660151/14/
- Adaptable: Cambridge School Dictionary sample: https://api.pageplace.de/preview/DT0400.9780511451270_A25081870/preview-9780511451270_A25081870.pdf
- Advance / advantage: Cambridge Dictionary pages: https://dictionary.cambridge.org/dictionary/english/advance ; https://dictionary.cambridge.org/dictionary/english/advantage

Source snippets/pages were inspected during this run. Entries remain pending independent editorial review.

## Final package verification
- FullSource: **543 files**; ZIP CRC PASS; one root; exclusions PASS.
- Update Patch: **19 changed/replaced files**, **0 deletions**; ZIP CRC PASS.
- Patch replay against v2.95.35 baseline: **543/543 files byte-identical** to FullSource v2.95.36.
- SHA-256 generated for both archives; see release manifest.
