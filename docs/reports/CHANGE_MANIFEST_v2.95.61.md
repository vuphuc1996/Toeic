# Change Manifest — TOEIC Dictionary v2.95.61

## Source of truth

- Exact predecessor: `TOEIC_Dictionary_v2.95.60_FullSource.zip`.
- Predecessor SHA-256: `b4e5404b824991208d99babb3f471b45e9e27fded1d31327854ae3a15ce58838`.
- Predecessor ZIP CRC: PASS; archive was uniquely identified as the latest v2.95.60 FullSource by conversation upload time and its matching SHA-256 sidecar.

## Substantive implementation

- `data/related-terms.json`: guarded updates to 20 existing relation-target rows only.
- `patches-related-terms/v2.95.61/related-terms-042.json`: exact old-value and base-file-SHA guarded update patch.
- `patches-related-terms/v2.95.61/batch-042-glossary-ledger.json`: per-term source, POS, sense-alignment, preserved Vietnamese gloss and existing relation-anchor evidence.
- `tools/tests/test_related_glossary_batch_042.py`: five regression cases for inventory, provenance, source type, identity/meaning preservation and exact pre-batch reconstruction.
- Historical reconstruction tests/helpers updated to reverse Batch 042 before replaying older Batch 038–041 ledgers; existing assertions remain active.
- `.github/workflows/validate-data.yml`: registers Batch 042 test in syntax compilation and the dedicated CI test sequence.

## Documentation and reports

- Root and docs changelogs; Master Status; Current/Previous Version ledgers.
- Related Glossary Batch 042, quality audit, enrichment queue and candidate audit.
- Regenerated current-version Foundation A2 assessment-quality and TOEIC independent editorial review queue reports; these are report artifacts only and do not change question content or approval state.
- Test report, command-log index, package verification and Python shard evidence.

## Package delta

- Exact patch from v2.95.60: 17 adds / 18 modifies / 0 deletes; 35 changed paths.
- FullSource target: 737 files under one versioned root.
- Exact patch replay: 737/737 files byte-identical; no missing, extra or mismatched files.

## Preservation checks

- 567 glossary term identities preserved; 20 existing rows enriched, 0 added, 0 deleted.
- `meaning_vi` preserved for all 20 rows.
- No canonical headword or relation array changed; no IPA/examples auto-generated.
- No question, choice, answer-key, Mock eligibility, learner-data, IndexedDB, Robot Buddy, UI layout or hosting changes.
