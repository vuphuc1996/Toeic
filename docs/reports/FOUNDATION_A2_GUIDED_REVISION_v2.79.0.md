# Foundation A2 Guided Writing Revision — v2.79.0

## Scope

v2.79.0 adds a learner-led review and rewrite flow to the 13 A2 contextual production tasks introduced in v2.78.0. It extends the existing local evidence store; it does not create a second tracker, server service, AI grader or new storage schema.

## Learner workflow

1. Complete the original contextual writing task and save the first response with the existing three self-report ratings.
2. Review the previous response displayed by the task.
3. Read the three task-specific review checks and confirm each one.
4. Use the topic-specific revision hint as optional guidance.
5. Write a changed second version (at least eight words) and complete the same three self-report ratings for the revision.
6. Save. The revision is linked to the response it replaces; the next revision is linked to the immediately preceding response.

## Data contract

- Store remains `toeic:foundation-progress:v1` in local storage.
- Existing production task IDs and legacy `::apply1` application evidence remain unchanged and separate.
- Existing A2 `::produce1` task IDs remain unchanged.
- New attempt rows store `response`; guided revision rows also store `basedOnResponse`, `reviewChecks`, `ratings`, `score`, `wordCount`, `minimumWords`, `assessedAt` and `assessmentType: guided_revision`.
- Evidence item metadata retains `initialResponse`, `lastRevisionSource`, `latestRevisionChecks`, `revisionCount`, `latestResponse` and latest self-report fields.
- Revision writes are rejected if the revised text is under the configured minimum, is identical to the preceding response after whitespace/case normalization, lacks all three review confirmations, or lacks all three boolean self-ratings.
- Historical attempts from before response capture are preserved. The application does not invent or backfill historical text that was never stored.
- Self-ratings are learner reports only. No automatic grammar, lexical, fluency, CEFR or ETS score is generated.

## Task coverage

All 13 A2 tasks have their own three-point `revisionChecklist` and `revisionHint`; the revision workspace is not added to Pre-A1/A1 tasks. The v2.78.0 contextual production payload remains unchanged outside the two additive revision-guide fields.

## Verification

- Dedicated Python revision tests: 6/6 PASS.
- Existing A2 production tests: 7/7 PASS.
- Dedicated JavaScript revision regression: PASS.
- JavaScript regression suite: 24/24 PASS.
- The selected broader Python regression set is recorded in `TEST_REPORT_TOEIC_Dictionary_v2.79.0.md`.
- Local validators pass; remote GitHub Actions, Pages deployment and physical-device QA are not claimed.

## Limits

A checked review item means the learner confirms that they reviewed it. It does not prove that the revision is linguistically correct. Model answers and hints are supports, not authoritative automated marking. Older response text that was not persisted before v2.79.0 cannot be reconstructed.
