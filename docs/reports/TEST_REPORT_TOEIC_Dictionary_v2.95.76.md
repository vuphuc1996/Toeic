# Test Report — TOEIC Dictionary v2.95.76

## Source changes under test

- Vocabulary Batch 028: 40 new canonical headwords, 0 removals, 0 changes to existing record IDs/headwords/senses.
- Listening translation remediation: 8 existing Part 3/4 units received `transcriptTranslation`; no question/choice IDs or answer keys changed.
- Historical Batch 026/027 regression tests were updated to reconstruct their original 1,181-headword snapshots while recognizing Batch 028 as a later addition.
- Added Batch 028 vocabulary invariants and Listening transcript-translation coverage assertions.

## Acceptance state

This document was authored before the new commit's hosted validation completed. It intentionally does **not** claim a local full-suite result. Use the GitHub Actions Validate and Pages runs attached to the exact v2.95.76 candidate commit as the authoritative remote evidence. Source Release Accepted, Candidate CI Verified and Pages Deployment Verified remain separate states.
