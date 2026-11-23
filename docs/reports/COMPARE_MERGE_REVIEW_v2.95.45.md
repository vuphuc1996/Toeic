# Alternate Full Source Comparison & Selective Merge — v2.95.45

## Inputs and identity

| Source | Files | ZIP size | SHA-256 |
|---|---:|---:|---|
| Released v2.95.44 FullSource | 664 | 5,639,150 bytes | `8a5331f7ee63ced28fef5329b04bd0ba36de07b34871a44b70878809132f6898` |
| Owner-uploaded alternate v2.95.44 FullSource | 683 | 5,654,805 bytes | `08144b096865d4023808474930760cf4c03856d04936b2de09fb36d51748b89f` |

These are two different v2.95.44 source branches, not equivalent packages. No branch was treated as a drop-in replacement.

## Exact tree comparison

| Difference | Count |
|---|---:|
| Byte-identical common paths | 594 |
| Changed common paths | 43 |
| Paths only in uploaded branch | 46 |
| Paths only in released branch | 27 |
| Uploaded tree | 683 |
| Released tree | 664 |

The 43 shared-path changes include glossary data, release documentation/audits, CI coverage, tests, and release ledgers. The branch also differs in patch history and report provenance, so wholesale copying would have replaced newer released history with a divergent branch snapshot.

## Glossary comparison

| Inventory | Uploaded branch | Released baseline |
|---|---:|---:|
| Raw rows | 554 | 562 |
| Normalized unique terms | 554 | 562 |
| Duplicate normalized terms | 0 | 0 |

Six terms existed only in the upload: `ask for`, `change`, `comments`, `communicate with`, `connection`, `consideration`. Fourteen terms existed only in the released baseline, including the more recent additions and retained glossary records. The upload therefore did not provide a higher-coverage glossary as a whole.

### Merged from the upload

Five missing terms were added because they are exact existing relation targets with compatible part of speech and useful senses:

- `ask for` — request something (verb phrase)
- `change` — transition/result of becoming different (noun)
- `comments` — remarks or feedback (plural noun)
- `communicate with` — exchange information with (verb phrase)
- `connection` — relation/link between entities (noun)

The sixth upload-only term, `consideration`, was not imported: it is a noun while its linked canonical headword `consider` is a verb. That derivational relationship is not enough to treat the noun as a direct synonym gloss for the verb; it remains a review candidate.

Three existing records were corrected with exact old-value guards, while preserving term identity and relation arrays:

| Term | Existing canonical relation anchor | Selected sense |
|---|---|---|
| `caller` | `visitor` | person visiting a house/building, not telephone caller |
| `article` | `item` | object/article of a type, not newspaper/grammar article |
| `assume` | `undertake` | take responsibility/control, not accept a proposition as true |

The upload's additional wording/source-claim differences across other common rows were reviewed but not mass-copied. Most were equivalent paraphrases, broader/narrower senses, or POS changes without a demonstrated relation-specific advantage. Existing released definitions were retained where the evidence did not justify an exact sense change.

## Engineering improvements adopted

1. `tools/run-python-tests-sharded.py` and its regression suite. It runs test modules in isolated processes, can split large modules into method batches, terminates child process groups on timeout, keeps diagnostic output, and writes a version + test-inventory bound checkpoint. Resume skips only modules explicitly marked PASS.
2. `tools/run-release-acceptance.py` and its regression suite. It sequences local release gates, has explicit timeout/failure statuses, resolves the default version from `data/manifest.json`, and now reuses the sharder process-group cleanup helper. A follow-up fix ensures JSON and Markdown reports both store the resolved version rather than `null` when the version argument is omitted.

The uploaded `run-validator-test-batches.py` was not merged. It overlaps with the generalized sharder, is hard-wired to `test_validator.py` and a v2.95.44 progress filename, and maintains a second independent checkpoint protocol. The alternate branch also contained Batch 035/036-specific tests and ledgers. Those were not copied wholesale because their 554-row branch baseline and historical patch hashes do not match the released 562-row source. The `alert` record was already present in the released glossary, so its alternate one-row addition was not reapplied. New v2.95.45 tests validate the selected merge against the actual released baseline. The generalized sharder subsumes the useful isolation/resume behavior without that version-specific implementation.

## Resulting v2.95.45 inventory

- Related Glossary: 567 rows / 567 normalized unique / 0 duplicates.
- Exact relation coverage: 556/804 (69.2%).
- Remaining: 248 unique terms / 249 relation occurrences.
- No canonical headwords or IDs were added.

## Preservation and UI

Protected canonical vocabulary and learning-bank files were byte-identical to v2.95.44. The only runtime/UI file differences are the release/cache marker `2.95.44` → `2.95.45` in `assets/js/app.js`, `index.html` and `sw.js`; no stylesheet, layout, visual component, learner-storage code or navigation behavior was changed. No backend or Cloudflare runtime was added.

## Decision

Adopt the two generalized QA runners, five relation-aligned glossary additions and three sense-aligned guarded corrections. Retain the released v2.95.44 baseline and its later Batch 037 data, rather than replacing it with the smaller alternate tree. Defer `consideration` and the upload's unproven/equivalent wording changes.
