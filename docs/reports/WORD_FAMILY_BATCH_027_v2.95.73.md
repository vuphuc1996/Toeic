# Word Family Batch 027 — v2.95.73

## Change summary

- Added 10 reciprocal links for existing, already-canonical headwords.
- Removed 2 self-referential links: `hire → hire` and `utilization → utilization`.
- Updated the read-only graph audit to report self-referential links explicitly.
- Added a regression suite that checks the reciprocal links against canonical POS and Vietnamese sense anchors.

## Resulting graph metrics

| Metric | v2.95.72 | v2.95.73 |
|---|---:|---:|
| Canonical headwords | 1,181 | 1,181 |
| Headwords with family links | 322 | 331 |
| Directed family links | 420 | 428 |
| Missing canonical targets | 50 | 50 |
| Target POS mismatches | 1 | 0 |
| Vietnamese sense-anchor review flags | 72 | 70 |
| Non-reciprocal links | 10 | 0 |
| Self-referential links | 2 | 0 |

## Data boundaries

No headword, canonical ID, IPA, definition, topic, synonym/antonym, TOEIC question, choice ID, answer key, learner IndexedDB schema/record, Mock eligibility, or UI layout was changed. The 50 missing Word Family targets and 70 remaining Vietnamese sense-anchor flags stay visible for editorial review; none were auto-filled.

The 1,181-word inventory is unchanged. This is a data-quality repair release, not a vocabulary-expansion release.
