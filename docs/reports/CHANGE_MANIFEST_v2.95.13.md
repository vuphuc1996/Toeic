# Change Manifest — v2.95.13 candidate

## Which version Claude must review

- **Baseline to compare:** v2.95.12 at Git commit `85be68a`.
- **Candidate to review:** v2.95.13 at the final candidate commit recorded in the one-shot handoff.
- **Historical predecessor:** v2.95.11, retained for context only. Claude does not need to re-audit v2.95.11 wholesale; review the v2.95.12 → v2.95.13 delta and verify unchanged contracts where relevant.
- **Release status:** local candidate only; no GitHub push, Actions run or Pages deployment is claimed.

## In-scope changes

| Area | Files/data | Change |
|---|---|---|
| Vocabulary meanings/examples | `data/vocabulary/{B,C,D,E,F,H,M,O,S,V}.json` | 10 existing headwords expanded into 24 sense-linked examples; 20 patch operations; no new headwords |
| Glossary | `data/related-terms.json` | Four additional Vietnamese glosses with Cambridge source URLs |
| Word-family precision | `data/vocabulary/V.json` | `valuable → value (n)` and `valuation → value (v)` aligned to the separated senses |
| Patch provenance | `patches/v2.95.13/`, `patches-related-terms/v2.95.13/`, `data/vocabulary/batch-017.json` … `batch-020.json` | Expect-value, allowlist, stable-ID hash, identity/source guards, dry-run/apply logs and provenance snapshots |
| Regression tests | `tools/tests/test_vocabulary_detail_examples.py`, `tools/tests/test_vocabulary_family_links.py`, `tools/tests/vocabulary-release-integrity.mjs`, `tools/tests/flashcard-senses.mjs` | Verify new source data, `sense_index`, specific POS-linked family meanings, and Flashcard rendering of multi-sense entries |
| Documentation/release | `docs/MASTER_STATUS.md`, `docs/README.md`, `docs/CHANGELOG.md`, `docs/versions/*`, release reports | Version, release notes, evidence, coverage and owner acceptance checklist |

## Explicitly unchanged

- 1,141 canonical IDs, headwords and topic arrays.
- Question banks, question IDs, answer keys, Listening/Reading Mock eligibility and Foundation content.
- Flashcard runtime helper, 10-card maximum contract, Robot Buddy, TTS timing, Service Worker update consent and CSS design-token rules.
- Learner records, IndexedDB database/schema, localStorage keys, migrations and external data transfer.
- No new backend, AI API, GAS, iframe or Cloudflare runtime.

## Required Claude review

1. Compare the baseline and candidate source; verify only the declared files/contracts changed.
2. Re-run each applicable command in the attached test evidence and report exact command, duration, exit code and test count.
3. Inspect all three vocabulary data patches and the related-term patch for `expect.old`, narrow allowlists, stable-ID hash, source references and replay safety.
4. Verify the 10 meanings, 24 examples, four glossary entries and two family-link corrections; distinguish source evidence from editorial approval.
5. Verify Flashcard rendering tests and cross-check that the UI displays sense-linked examples without changing learner storage.
6. Report PASS / FAIL / NOT RUN / INCONCLUSIVE. Do not edit files, change baselines, modify IDs/headwords/topics or push GitHub.

## Review boundary

This package is a code/data review candidate, not a request to approve content automatically. All newly added language material remains pending an independent lexical reviewer. Real browser/device checks remain owner acceptance items.
