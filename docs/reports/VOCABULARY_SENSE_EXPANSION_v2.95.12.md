# Vocabulary Sense Expansion — v2.95.12

## Scope and baseline

- Baseline source: v2.95.11.
- Candidate: v2.95.12.
- Canonical inventory remains 1,141 headwords across A–Z.
- No new canonical headword was added.
- No `id`, `word` or `topics` field was changed. The patch identity guards capture the prior identity/topic values for the affected records.
- All additions/corrections are provisional and **pending independent lexical review**. Dictionary references are source evidence, not a claim of second-person editorial approval.

## Nine existing headwords with separated meanings

| Headword | Meaning distinctions introduced | Added examples |
|---|---|---:|
| `address` | noun: contact/mail location; verb: deal with a matter or problem | 1 |
| `application` | noun: formal written request; noun: software application | 1 |
| `claim` | noun: request for compensation/benefit; verb: assert that something is true | 1 |
| `draft` | noun: preliminary document version; verb: write the first version | 1 |
| `issue` | noun: problem or matter; verb: formally issue/provide a document | 1 |
| `order` | noun: purchase order; verb: request goods/services; noun: official instruction | 1 |
| `record` | noun: stored written information; verb: store information for later use | 1 |
| `position` | noun: job/rank; noun: situation or standing | 1 |
| `term` | noun: contract condition; noun: fixed period/tenure; noun: school semester | 2 |

The project-wide multi-sense count increased from 30 to 39. Dedicated examples associated with multi-sense records increased from 61 to 81. Each added example has a `sense_index` pointing to its intended sense.

## Precision and cross-link corrections

- `order`'s goods-order noun sense now uses `purchase order` rather than `purchase request`. Cambridge describes a purchase order as a document requesting goods or services from a supplier and setting out transaction details. Source: https://dictionary.cambridge.org/dictionary/english/purchase-order
- `claimant` now links back to the `n` sense of `claim`, with the noun-specific Vietnamese gloss. This avoids the former ambiguous `n/v` family link after `claim` was split into separate noun and verb senses.
- 22 supporting terms received Vietnamese glosses and Cambridge source URLs in `data/related-terms.json` so newly referenced synonyms/antonyms are not presented without a gloss.

## Data patch trail

1. `patches/v2.95.12/batch-001.json` — 18 operations across the nine target headwords; allowed paths `/senses` and `/examples` only.
2. `patches/v2.95.12/batch-002-family-link.json` — claimant reverse family link narrowed to `claim` noun.
3. `patches/v2.95.12/batch-003-family-gloss.json` — reverse link gloss aligned with the full noun-sense gloss.
4. `patches/v2.95.12/batch-004-order-synonym.json` — `purchase request` corrected to `purchase order`.
5. `patches-related-terms/v2.95.12/related-terms-001.json` — 22 sourced glossary additions using `tools/patch-related-terms.py` with a base-file SHA-256 precondition.

Each vocabulary patch has `expect.old`, a stable ID-set hash, a narrow `allowedPaths` list, and dry-run/apply records. The related-term patch accepts only absent terms with HTTPS Cambridge Dictionary source URLs; rollback removes only the exact entries introduced by that patch.

## Measured changes

| Measure | v2.95.11 baseline | v2.95.12 candidate |
|---|---:|---:|
| Canonical headwords | 1,141 | 1,141 |
| Stable ID set | 1,141 | 1,141; 0 added / 0 missing |
| Multi-sense headwords | 30 | 39 |
| Examples associated with multi-sense records | 61 | 81 |
| Related-term glossary entries | 347 | 369 |
| Unmatched synonym/antonym occurrences (exact-term comparison) | 546 | 528 |

The 546 → 528 comparison counts synonym/antonym occurrences across canonical senses whose case-folded term is absent from `related-terms.json`. It is a custom comparison script, not a separate validator field; the built-in validator reports its own distinct `333/817` summary after the change. Do not conflate the two measures.

## Sources

- Cambridge Dictionary — address: https://dictionary.cambridge.org/dictionary/english/address
- Cambridge Dictionary — application: https://dictionary.cambridge.org/dictionary/english/application
- Cambridge Dictionary — application software: https://dictionary.cambridge.org/dictionary/english/application-software
- Cambridge Dictionary — claim: https://dictionary.cambridge.org/dictionary/english/claim
- Cambridge Dictionary — draft: https://dictionary.cambridge.org/dictionary/english/draft
- Cambridge Dictionary — issue: https://dictionary.cambridge.org/dictionary/english/issue
- Cambridge Dictionary — order: https://dictionary.cambridge.org/dictionary/english/order
- Cambridge Dictionary — purchase order: https://dictionary.cambridge.org/dictionary/english/purchase-order
- Cambridge Dictionary — record: https://dictionary.cambridge.org/dictionary/english/record
- Cambridge Dictionary — position: https://dictionary.cambridge.org/dictionary/english/position
- Cambridge Dictionary — term: https://dictionary.cambridge.org/dictionary/english/term
- Cambridge Dictionary supporting terms: https://dictionary.cambridge.org/dictionary/english/assert ; https://dictionary.cambridge.org/dictionary/english/cancel ; https://dictionary.cambridge.org/dictionary/english/directive ; https://dictionary.cambridge.org/dictionary/english/duration ; https://dictionary.cambridge.org/dictionary/english/erase ; https://dictionary.cambridge.org/dictionary/english/handle ; https://dictionary.cambridge.org/dictionary/english/instruction ; https://dictionary.cambridge.org/dictionary/english/log ; https://dictionary.cambridge.org/dictionary/english/matter ; https://dictionary.cambridge.org/dictionary/english/prepare ; https://dictionary.cambridge.org/dictionary/english/problem ; https://dictionary.cambridge.org/dictionary/english/provide ; https://dictionary.cambridge.org/dictionary/english/request ; https://dictionary.cambridge.org/dictionary/english/role ; https://dictionary.cambridge.org/dictionary/english/semester ; https://dictionary.cambridge.org/dictionary/english/situation ; https://dictionary.cambridge.org/dictionary/english/standing ; https://dictionary.cambridge.org/dictionary/english/state

## Review status and limitations

- All nine sense expansions and 22 related-term glosses remain pending independent lexical review.
- No real browser rendered the detail modal during this local work. Automated tests cover the canonical data structure and existing rendering hooks; owner acceptance is still required.
- No GitHub Actions run or GitHub Pages deployment is claimed.
