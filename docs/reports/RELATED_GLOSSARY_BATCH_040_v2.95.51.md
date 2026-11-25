# Related Glossary — Batch 040 (v2.95.51)

## Scope

- Updated **6 existing glossary rows** that already occur as synonym/antonym relation targets.
- Source: Cambridge Dictionary entries checked on 2026-11-24; definitions are paraphrases, not copied dictionary text.
- Each row has a Cambridge URL, release provenance and an explicit sense-alignment note in `patches-related-terms/v2.95.51/batch-040-glossary-ledger.json`.
- Every update is guarded by exact old values and the SHA-256 base file hash in `related-terms-040.json`.
- No new glossary identities, vocabulary headwords, relation edges or learner-bank records were created.

## Enriched rows

| Term | POS | Definition scope | Existing relation anchors |
|---|---|---|---|
| charge | n/v | Ask for payment; amount paid for a service | invoice, rate, refund |
| move | v/n | Change position/place; action or relocation | relocation, transfer, transport |
| leave | v/n | Depart; leave something remaining; work absence | depart, join, remain |
| opening | n | Opening event; job/opportunity vacancy; beginning | launch, opportunity, vacancy |
| suggestion | n | Idea or plan offered for consideration | advice, offer, proposal |
| location | n | Particular place or position | address, destination |

## Quality delta

| Metric | v2.95.50 | v2.95.51 | Change |
|---|---:|---:|---:|
| English definitions present | 356 | 362 | +6 |
| Missing English definitions | 140 | 136 | -4 |
| Placeholder definitions | 71 | 69 | -2 |
| Missing POS | 206 | 201 | -5 |
| Missing source provenance | 73 | 71 | -2 |
| Entries with quality flags | 215 | 209 | -6 |
| Relation-target coverage | 556/804 | 556/804 | unchanged |

Six existing entries were improved: four previously blank definitions were filled and two placeholders were replaced. Five entries gained POS metadata and two gained provenance metadata.

## New research queue

`tools/build-related-glossary-enrichment-queue.py` now generates a deterministic, read-only priority queue. It ranks currently flagged glossary entries by relation-reference count, distinct source headwords, then quality priority. Current output: 209 flagged entries; 202 are referenced by existing relations; those entries account for 235 relation references. The queue is for research prioritization only; it does not infer definitions or authorize automatic imports.

## Review status

**Source-checked; independent editorial review pending.** Multi-sense terms (`charge`, `move`, `leave`, `opening`) require careful sense validation against their exact learner context. Cambridge page lookup and relation-anchor matching do not certify every intended sense.
