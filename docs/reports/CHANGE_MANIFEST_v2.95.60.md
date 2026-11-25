# Change Manifest — v2.95.60

## Exact source

- Base archive: `TOEIC_Dictionary_v2.95.59_FullSource.zip`
- Base SHA-256: `b5dbb4e7c974814c8d59fc6bf653737f7208e7da2c2d49141078efff385d993c`
- Base file count: 703

## Changes

- Added `tools/render_missing_ipa_review_queue.py` and its regression test.
- Extended the CMUdict queue generator to record source package/version metadata.
- Added a Markdown missing-IPA review queue for 79 canonical entries missing US IPA.
- Regenerated Related Glossary quality flags, candidate audit and relation-frequency enrichment queue.
- Regenerated item complexity review report for v2.95.60.
- Registered the new renderer test in CI and its Python syntax preflight.
- Updated version markers, Master Status, changelogs, test report and command log.

## Canonical content preservation

No vocabulary A–Z JSON, Related Glossary data, Listening/Reading question libraries, learner records, IndexedDB schema, answer keys, choice identities or Mock eligibility were changed. The release contains no automatic IPA or glossary backfill.
