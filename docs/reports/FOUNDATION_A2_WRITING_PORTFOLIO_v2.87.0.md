# Foundation A2 Writing Portfolio — v2.87.0

## Release change

The A2 writing portfolio now offers an explicit **Xuất nhật ký (.md)** action. The exported Markdown file contains only A2 tasks with stored learner responses. Per task it records the scenario, instruction, word minimum, requirements, sentence frame, task-specific self-review rubric, each saved response, timestamp, word count, learner self-ratings, guided-revision checks, prior response used for comparison, model answer and revision hint.

## Privacy and evidence boundary

- Export is initiated by the learner from the portfolio interface. No automatic/background export runs.
- The export builder is pure and read-only; it does not mutate the progress object.
- File generation uses the existing browser download flow. The content is not posted to a server, API, Google AI or third party.
- Only `level === A2` lessons and their current `productionTask` IDs are included. Legacy `applicationTask` evidence is excluded.
- Self-ratings remain learner self-reports. The app does not automatically judge grammar, award a CEFR level or infer an ETS score.
- IndexedDB v1, localStorage progress key `toeic:foundation-progress:v1`, migration behavior and existing task IDs are unchanged.

## Editorial correction

The `a2-polite-requests` scenario now says that the learner needs the colleague to send the meeting notes. This aligns the scenario with the existing instruction and model answer. The exact one-field correction is recorded in `tools/foundation-a2-production-refresh-v2.87.0.json`; the v2.78.0 baseline file remains unchanged.

## Learner test steps

1. Open Foundation and select the A2 progress/outcome summary.
2. Open **Nhật ký viết A2**. The export action is disabled until at least one A2 production response is saved.
3. Open an A2 lesson, complete the production response, select all three self-review ratings and save.
4. Use guided revision, confirm its three review checks and self-ratings, then save the revision.
5. Return to the portfolio and choose **Xuất nhật ký (.md)**.
6. Open the downloaded Markdown file and verify that both original and revised responses appear in order with their own ratings and timestamps.

Expected result: the export includes only saved A2 writing evidence; it does not affect the portfolio counts or any existing progress.
