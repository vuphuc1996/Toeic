# Foundation A2 — Extended Writing Tasks v2.88.0

## Scope delivered

- Added one extended learner-authored production task to each of the 13 A2 lessons, raising the A2 writing inventory from 13 to 26 distinct tasks.
- Original task IDs remain `::produce1` with the original 8-word minimum. New tasks use independent `::produce2` IDs with a 20-word minimum.
- Formats include a polite workplace email, purchasing note, delivery proposal, incident report, live progress update, visitor notice, directions, invitation/offer, process instructions, system update notice, status email, invoice process notice and new-staff introduction.
- Each new task has scenario, instruction, three requirements, sentence frame, three self-review criteria, model answer, three revision checks and a topic-specific revision hint.
- The extended block is collapsed by default. Existing lesson content and the original writing prompt remain in their original position. After a revision, the first response and its first self-ratings remain displayed as the baseline; the latest revision appears in its separate guided-revision workspace.

## Evidence, storage and privacy

- Each new `::produce2` task is independently saved beside the corresponding `::produce1` entry in `toeic:foundation-progress:v1`.
- The original task IDs, existing learner histories, legacy `::apply1` application evidence and IndexedDB v1 are preserved.
- Initial responses, revision responses, self-ratings and review confirmations remain device-local. No automatic grammar evaluation occurs.
- The writing portfolio and Markdown export enumerate all 26 A2 production tasks and include only tasks with saved response evidence. Legacy `::apply1` application records are not included as A2 production tasks.
- The SHA-256 registry `tools/foundation-a2-extended-production-v2.88.0.json` records all new IDs, content fingerprints and review states.

## Editorial status and limitations

- All 13 new tasks have `reviewState: pending-independent-editorial-review`. Structural checks and model-answer feature checks do not replace independent linguistic review.
- A2 is not marked complete and is not CEFR-certified. Varied/extended Reading and Listening, second-person editorial review and empirical learner validation remain open.
- The 20-word minimum is a local task gate, not a proficiency threshold. Self-ratings are not automated grading.

## Learner test steps

1. Open Foundation and choose any A2 lesson.
2. Complete the original production prompt and save all three self-ratings.
3. Open **Thử thách viết mở rộng** below it. The section should be collapsed until opened.
4. Write at least 20 words, complete the three self-ratings and save.
5. Reopen the lesson. The original and extended tasks should display their own saved responses/status independently.
6. Use guided revision on the extended task: confirm all three review checks, write a different response of at least 20 words, complete its three self-ratings and save.
7. Open **Nhật ký viết A2**, verify both tasks appear separately, then export the Markdown diary.

Expected result: both tasks and their revision histories are retained separately; the portfolio shows a maximum of 26 available tasks; exported Markdown lists saved responses and revisions, without changing progress or uploading content.
