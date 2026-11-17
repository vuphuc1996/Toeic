# Foundation A2 Extended Reading — v2.89.0

## Scope

- Add one supplementary longer Reading passage to each of the 13 Foundation A2 lessons.
- Keep the original 23 Foundation Reading passages / 59 questions unchanged.
- Add 13 supplementary passages / 39 questions, each with 90–110 words, three questions, four distinct options, one answer index, rationale and an exact source-evidence pointer.
- Support email, memo, comparison note, incident report, team update, notice, directions, invitation, procedure, plan and staff-information formats.
- Record a separate progress scope (`{lessonId}::reading2`) inside the existing `toeic:foundation-reading-progress:v1` local ledger; no new key or database version.
- Show the content in a collapsed extension panel and preserve its open state across answer selection/re-render.
- Explicitly label the new materials as pending independent review and prevent their practice evidence from being combined with original/core A2 outcome metrics.

## Content inventory

| Metric | Result |
|---|---:|
| A2 lessons covered | 13/13 |
| New passages | 13 |
| New questions | 39 |
| Words per passage | 90–104 |
| Questions per passage | 3 |
| Distinct answer options per question | 4 |
| Exact `evidenceText` pointers | 39/39 |
| Stable IDs | `lessonId::reading2` and `::q1`–`::q3` |
| Independent editorial review | Pending for all 13 passages |

Passage content is protected by `tools/foundation-a2-reading-extended-v2.89.0.json`, a SHA-256 registry over the complete passage objects.

## Evidence and policy

- Original reading progress remains keyed by the existing lesson ID.
- Extended reading progress is keyed under the same existing storage object using `{lessonId}::reading2`.
- Re-answering a question appends an attempt but does not inflate unique-question count; the latest answer remains the one used for the current practice summary.
- The threshold calculation is aligned with the rounded percentage displayed to the learner. For a 0.67 threshold, 2/3 is displayed as 67% and qualifies after the three-independent-question minimum is met.
- Supplementary evidence is practice-only, not a CEFR certificate, mastery claim, official TOEIC question pool or Mock Exam evidence.

## Preservation

- Original 23 Foundation Reading passages, original A2 q1/q2 canonical baseline, their stable IDs and progress remain unchanged.
- No IndexedDB v1 schema migration, localStorage key addition, profile reset or data export occurs.
- No backend, server, external API or learning-data transfer is introduced.
- Service Worker `REQUIRED` and `APP_SHELL` both include `foundation-reading-extended.json` for offline availability.

## Review status

All 13 passages are still `pending-independent-editorial-review`. Automated checks validate structure, unique IDs, answer index range, distinct options, exact source evidence, question mapping, word count, hash registry and app integration. They do not substitute for a second human linguistic reviewer or empirical A2 learner validation.
