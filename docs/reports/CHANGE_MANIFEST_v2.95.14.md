# Change Manifest — TOEIC Dictionary v2.95.14 candidate

## Release boundary

- **Previous source:** v2.95.13, commit `a04a4d97472cb856c2459aab19d2a18090204e40` on `work-v2.95.13`.
- **Candidate:** v2.95.14; glossary-only content expansion plus CI coverage hardening.
- **Status:** local candidate. No GitHub push, remote Actions run or Pages deployment has been performed.
- **Claude review:** the owner has already submitted v2.95.13 to Claude; its result is pending. This manifest records the follow-on v2.95.14 delta and does not replace or alter Claude's v2.95.13 review scope.

## Included changes

| Area | Files | Change |
|---|---|---|
| Related-term glossary | `data/related-terms.json` | Add ten sourced terms; 373 → 383 glossary entries. |
| Provenance | `data/vocabulary/batch-021.json` | Record ten entries, source URLs, release and provisional editorial status. |
| Safe patch | `patches-related-terms/v2.95.14/related-terms-001.json` | Ten `expect.absent=true` operations with base-file SHA-256 guard. |
| Python regression | `tools/tests/test_related_glossary_batch_021.py` | Six tests for metadata, source presence, existing synonym/antonym use, frequency threshold, uniqueness and CI path filters. |
| JavaScript release integrity | `tools/tests/vocabulary-release-integrity.mjs` | Assert current manifest version, glossary count and batch 021 integration. |
| CI workflow | `.github/workflows/validate-data.yml` | Run the new Python test and trigger on `patches-related-terms/**` for push and pull requests. |
| Release metadata/docs | `data/manifest.json`, `assets/js/app.js`, `sw.js`, `index.html`, `docs/**` | Synchronize v2.95.14, update Master/README/Changelog/version page and add evidence reports. |

## Exact content delta

The following terms already appeared in canonical synonym/antonym links; only explanatory glossary records were added: `requirement`, `pay`, `ignore`, `withhold`, `retain`, `earnings`, `duty`, `distribute`, `discourage` and `decline`. Each was referenced at least three times in the existing canonical data.

- New glossary records: **10**.
- Canonical headwords: **1,141**, unchanged.
- Stable vocabulary IDs, headwords, topics and synonym/antonym relationships: unchanged.
- TOEIC Listening/Reading, Grammar, Foundation, answer keys and Mock eligibility: unchanged.
- IndexedDB schema/version, learner records and localStorage learner keys: unchanged.

## Validation requirements and review cautions

1. Confirm exact English sense, Vietnamese gloss, part of speech and fit to the synonym/antonym context for each of the ten new terms.
2. Keep all entries provisional until independent lexical review is recorded. A Cambridge source URL supports the paraphrase; it does not constitute editorial approval for every TOEIC context.
3. Review the v2.95.13 Claude feedback when the owner supplies it, then decide whether any correction is required in v2.95.14.
4. Complete all 21 owner-run checks before release acceptance.
5. Do not deploy until the owner approves the consolidated candidate and remote Actions/Pages are checked.

## Explicitly out of scope

- No new canonical vocabulary headwords or IDs.
- No rewrites of existing synonym/antonym links or meaning records.
- No pronunciation/IPA backfill, word-family changes, grammar/audio/reading changes or UI redesign.
- No learner-storage migration, reset, backend/API or data transfer.
