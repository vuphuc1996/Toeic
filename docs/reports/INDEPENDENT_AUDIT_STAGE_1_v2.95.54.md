# Independent audit remediation — Stage 1 (v2.95.54)

## Scope and constraints

- Baseline: v2.95.53 FullSource archive; source archive did not contain upstream Git metadata.
- A local Git baseline was initialized from that exact source tree so each remediation task can be reviewed as a separate commit. These hashes are local reconstructed commits, not upstream GitHub commits.
- No vocabulary IDs, headwords, topics, Vietnamese meanings, synonym/antonym relations, question IDs, answer keys, or Mock eligibility were changed.
- No UI feature or Robot Buddy feature was added.

## Findings and disposition

1. Listening reserve queue: already data-driven in the v2.95.53 source. `test_editorial_review_queue.py` derives the reserve count from the current listening units and `collect_editorial_inventory`; it does not assert a fixed 161 count. Current result: 8 tests PASS. No redundant edit was made.
2. `appliance-n`: `verb_forms` changed from five empty strings to `null` through the guarded patch in `patches/v2.95.54/independent-audit-stage-1-data.json`.
3. CEFR aggregate rule: word-level CEFR is defined as the highest level among its senses using A1 < A2 < B1 < B2 < C1. Eight records were corrected (`host-v`, `supply-v`, `bill-v`, `document-v`, `experience-v`, `minute-n`, `offer-v`, `value-v`). `package-nv` already satisfied the rule (B1 = max(A2, B1)) and was left unchanged. Validator structural rule CE004 enforces this policy. VF003 rejects empty/whitespace-only verb-form strings.
4. Repository root: the two update-note files present in this v2.95.53 source root were moved to `docs/versions/legacy/`. No other root update-note files were present in this archive. CI now includes a final full `unittest discover` step.

## Commits

- Baseline import: `15f45356fcc37fe003c7daa477c07313d76c1f91`
- Data correction: `2225db82f110c9985c1190176e5d5c6b3f40de31`
- Validator + regression tests: `89ead49d8fadab9f5f93475c3aa3178e11e41338`
- Manifest CEFR count synchronization: `a0c7a0b813d224f48044f5a6113f653a938df85a`
- Patch allowlist canonicalization: `934121a2d23d33815b3a00019083728d2157a335`
- Historical glossary hash reconstruction: `f728a1d0d91a437af89e4cfc6831e171712ea2fd`
- Release docs: `5f11b87019638dfa2af99ca2deb1ba7b122cf236`
- Package/acceptance docs: `27a672f6f8689c43f68f418f949a40aac0f40b6b`
- Node regression evidence: `eac47347d47ef81fcf182b649468970628e70951`
- Commit ledger / raw-log references: `bdfc129fd2da2d03b76a95711fbf82e3284db442`
- Clean FullSource archive suite confirmation: `51e1f682fcf0f94ebe4aa66824479e716ffb1114`
- CI / repository root cleanup: `810a78b0e2378bb49e8e690ff1024886c939789a`

## CEFR policy

A headword may contain senses at different CEFR levels. The headword-level aggregate is the highest level represented by any sense. Lower-level senses are expected and are not themselves treated as errors. CE004 only fails when the aggregate headword level is not the maximum valid sense level.

## Acceptance boundary

The full Python discovery command is included in CI. Local full-suite results, per-task commands, elapsed time and exit codes are recorded in the final test report. Remote GitHub Actions and GitHub Pages deployment remain unverified until run by GitHub.
