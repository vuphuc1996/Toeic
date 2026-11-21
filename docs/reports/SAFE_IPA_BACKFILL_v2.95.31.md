# Safe IPA backfill report — v2.95.31

## Change
- Canonical word `dispute` (`dispute-n`) received US IPA `/dɪ.ˈspjut/` from an exact CMUdict single-pronunciation entry, after conversion validation.
- Cumulative source-linked ledger now contains 334 records (up from 333).
- Missing US IPA decreased 80 → 79 (1,062/1,141 records have US IPA; 93%).
- Converter onset allowlist now includes the `spj` cluster so the glide remains attached to the stressed onset. Regression expectation: `D IH0 S P Y UW1 T` → `/dɪ.ˈspjut/`.

## Candidate review
- 80 previous missing records examined.
- 1 unique candidate passed converter and was applied.
- 5 unique candidates failed conversion (multi-primary stress) and remain review-only.
- 49 records have multiple CMUdict variants and remain review-only.
- 25 exact headwords are not present in CMUdict.

## New pipeline
`tools/backfill_missing_ipa_from_cmudict.py` is preview-only by default. `--apply` only adds exact, single-variant candidates that pass the converter; it never overwrites existing IPA. Case-insensitive dictionary-key normalization, duplicate variant collapse, stable queue ordering and failure-to-review routing are covered by 8 tests.

## Test limitations
The CMUdict-derived entry is not independent dictionary verification. CMUdict itself may contain errors and omissions; converter output is project-normalized IPA. Ambiguous and converter-failing candidates were not forced into canonical data. No physical-device test, GitHub Actions run or Pages deployment was performed.
