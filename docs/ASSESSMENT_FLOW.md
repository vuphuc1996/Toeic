# Assessment Flow Contract

## 1. Product rule
All formative assessments follow the same two-phase interaction: **answer first → summary → explicit confirmation → answer review**. A learner may see which choice they selected, but must not see correctness, correct-answer markers, explanatory text, transcripts, scores by item, or feedback while still answering. The completion summary may show aggregate correct/incorrect/total counts only after the entire set is answered.

## 2. Draft and commit
- Multi-question Grammar, Reading, Listening and Foundation sets write selection-only drafts. Draft records must not contain `correct`, `answerIndex`, answer text, or explanations.
- Draft choices may persist locally so a refresh does not discard work. Draft persistence does not count as learning evidence. Removing the post-completion return action does not delete or migrate existing draft records.
- `isPracticeDraftSetComplete()` (or the equivalent Foundation set check) must pass before the summary is displayed. Once the summary is displayed, it is a one-way confirmation step; there is no secondary return-to-check action.
- Only the single **Xác nhận & xem đáp án** action may call the existing record/progress/evidence functions and reveal answer explanations. The completed-result surface has no return-to-edit/recheck action; learners can change a draft only while they are still answering, before the completion summary is opened. The Learning Focus X/Escape close affordance routes through the same confirmation handler rather than creating a second outcome.
- Existing committed attempt history remains intact; retries archive it using the existing attempt-history mechanism.

## 3. One-question practice
Smart Review and single-question Part 5 use the same two-phase contract: a selected answer creates `pendingSinglePractice`; the summary is shown; confirmation updates study progress/objective evidence and opens the existing explanation review. `pendingSinglePractice` is stored additively in `practiceSession` so the summary can be restored after reload.

## 4. Flash Quiz and Placement
Flash Quiz collects every selection before revealing its aggregate result. Confirmation updates spaced-review progress and opens a per-question answer comparison. Placement diagnostics auto-open the summary immediately after the final question; level recommendations and per-question explanations are revealed only after confirmation.

## 5. Mock Exam
- Mock answers are stored as selected indices only; the active test UI must not compute/show correctness.
- Manual submit or deadline expiry creates a pending result. It shows aggregate correct/incorrect/total counts but withholds answer keys, transcript and explanations.
- The pending result persists under `toeic:mock-pending-review:v1` so a reload cannot expose a detailed result prematurely. Only confirmation marks the history record as `completed` and opens detailed review.
- Empty timed-test answers are allowed and count as unanswered/incorrect at final scoring; the mock timer is the exam constraint.
- `mock-flow.js` schedules all questions across the exact Listening/Reading section deadlines. Weights include group audio/passage context, per-question work and a 2.4-second transition allowance. The last slot ends exactly at the section deadline.
- Reading transitions announce the current section-local question and Part. Listening transitions announce the question; the group audio is played once at group entry and not restarted for subsequent questions in the same conversation.

## 6. Dashboard progress model
Progress is grouped by `exam → skill → Part`, not by a fixed two-column layout. TOEIC Listening and Reading occupy separate rows; future IELTS and Writing/Speaking tracks can be added as new exam/skill groups without changing the Part grid component.

## 7. Regression gates
- `node tools/tests/assessment-deferred-workflow.mjs`
- `node tools/tests/practice-progress.mjs`
- `node tools/tests/mock-guided-flow.mjs`
- `node tools/tests/mock-exam-engine.mjs`
- `node tools/tests/mock-ui-integrity.mjs`
- `python tools/sync-version.py --check`
- `python tools/sync-design-profile.py --check`

Real browser rendering, speech synthesis behavior and remote deployment remain separate release verification steps.
