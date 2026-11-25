# Related Glossary — Batch 041 (v2.95.52)

## Scope and source policy

- Enriched **11 existing relation-target rows** selected from the frequency-ranked queue.
- Source pages: Cambridge Dictionary entries checked 2026-11-24; English definitions are paraphrases, not copied dictionary text.
- Each update records its Cambridge URL, source release, previous values, selected POS and sense-alignment note in `patches-related-terms/v2.95.52/batch-041-glossary-ledger.json`.
- `related-terms-041.json` guards every update with exact old values and the SHA-256 of the pre-batch `data/related-terms.json`.
- Vietnamese glosses, term identities and all relation arrays are preserved. No new glossary identities or canonical vocabulary headwords are created.

## Enriched rows

| Term | POS | Existing relation anchors | Sense scope |
|---|---|---|---|
| present | adj/v | current, introduce, submit | being in a place/current; showing or introducing |
| associate | n | colleague, partner | person connected through work/business |
| contender | n | candidate, competitor | person/organization competing to win |
| daily | adj/adv | monthly, weekly | every day; excludes newspaper noun |
| deal | n | contract, transaction | business agreement/arrangement |
| deny | v | claim, confirm | say untrue; refuse/withhold |
| direction | n | guidance, instruction | orientation; instructions |
| endpoint | n | destination, terminal | end/result of a process |
| fee | n | charge, payment | payment for service/work/right |
| legitimate | adj | legal, valid | lawful; reasonable/acceptable |
| occupation | n | career, employment | person's job/type of work |

## Quality delta

| Metric | v2.95.51 | v2.95.52 | Change |
|---|---:|---:|---:|
| English definitions present | 362 | 373 | +11 |
| Missing English definitions | 136 | 131 | -5 |
| Placeholder definitions | 69 | 63 | -6 |
| Missing POS | 201 | 190 | -11 |
| Missing source provenance | 71 | 65 | -6 |
| Entries with quality flags | 209 | 198 | -11 |
| Relation-target coverage | 556/804 | 556/804 | unchanged |

The 11 updates include five previously blank definitions and six placeholder definitions. They also fill all 11 POS gaps and six provenance gaps. The quality audit remains read-only and still identifies 198 entries for review.

## Editorial review boundary

**Source checked; independent editorial review pending.** Multi-sense terms (`present`, `deal`, `deny`, `direction`, `endpoint`, `legitimate`, `occupation`) have explicit inclusion/exclusion notes. Relation anchors are a prioritization signal, not proof that every target is a perfect semantic synonym or antonym. Review before promoting these paraphrases to approved learner content.
