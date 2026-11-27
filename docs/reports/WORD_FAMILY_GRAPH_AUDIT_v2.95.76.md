# Word Family Graph Audit — v2.95.76

- Canonical headwords: **1221**
- Headwords with at least one family link: **331**
- Directed family links: **428**
- Missing canonical targets: **50**
- Target POS mismatches: **0**
- Vietnamese sense-anchor mismatches: **70**
- Non-reciprocal links: **0**
- Self-referential links: **0**
- Duplicate links: **0**
- Duplicate headwords: **0**
- Malformed records/links: **0**

> This is a read-only structural and sense-anchor audit. Non-reciprocal links and meaning mismatches are editorial review flags, not automatic proof that a relationship is wrong. Batch 028 adds no Word Family links, and its headwords do not resolve any of the 50 outstanding referenced targets. Therefore the pre-existing graph counts remain unchanged except for total canonical headwords increasing by 40.

## Batch 028 effect

- 40 new headwords added; all 40 have empty `word_family` arrays.
- 0 new directed links; 0 existing links rewritten.
- Missing-target list remains the same 50 terms as v2.95.75.
- Existing graph anomalies remain queued for sense-level review; no automatic repair is performed.
