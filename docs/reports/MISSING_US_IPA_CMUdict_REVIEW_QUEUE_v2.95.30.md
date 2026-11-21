# Missing US IPA CMUdict review queue — v2.95.31

- Canonical vocabulary records: 1,141.
- Existing US IPA: 1,062.
- Missing US IPA queued: 79.
- After safe backfill: 5 single-pronunciation candidates fail the current converter and remain review-only; 49 multi-pronunciation records require editorial review; 25 exact headwords are absent from CMUdict.
- Exact headword matching, deduplicated variants and no automatic selection of ambiguous pronunciations are enforced.
- Output JSON: `MISSING_US_IPA_CMUdict_REVIEW_QUEUE.json`.
- Source: CMUdict via the `cmudict` package; attribution/license retained at `docs/licenses/CMUdict-DATA-LICENSE.txt`. The project does not redistribute the full CMUdict dataset.
- Safety: only `dispute` was added after unique-variant and conversion validation. Existing IPA, meanings, learner records, questions, answers, relations and UI are preserved.
