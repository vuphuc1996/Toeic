import assert from 'node:assert/strict';
import {
  archiveAllPracticeAnswersForRetry,
  archivePracticeAnswerForRetry,
  countAttemptedPracticeQuestions,
  ensurePracticeProgress,
  getLatestPracticeAttempt,
  getPracticeAttemptCount,
  recordPracticeAnswer,
  summarizePracticeProgress
} from '../../assets/js/practice-progress.js';

const p = ensurePracticeProgress({ answers: {} });
assert.equal(recordPracticeAnswer(p, 0, { choiceIndex: 1, choiceText: 'B', correctChoiceText: 'C', explanation: 'The notice confirms option C.', correct: false, answeredAt: 100 }), true);
assert.equal(p.answers[0].attemptNumber, 1);
assert.equal(recordPracticeAnswer(p, 0, { choiceIndex: 2, choiceText: 'C', correct: true }), false, 'cannot overwrite a locked current attempt');
assert.equal(archivePracticeAnswerForRetry(p, 0, 200), true);
assert.equal(p.answers[0], undefined, 'current answer is cleared to unlock choices');
assert.equal(p.attemptHistory[0].length, 1, 'previous attempt is preserved');
assert.equal(p.attemptHistory[0][0].correctChoiceText, 'C', 'archived attempt retains the correct answer');
assert.equal(p.attemptHistory[0][0].explanation, 'The notice confirms option C.', 'archived attempt retains its explanation');
assert.equal(getLatestPracticeAttempt(p, 0).choiceText, 'B', 'latest historical attempt remains available while retry is open');
assert.equal(countAttemptedPracticeQuestions(p, 2), 1, 'coverage counts unique question indices, not attempts');
assert.equal(getPracticeAttemptCount(p, 0), 1);
assert.equal(recordPracticeAnswer(p, 0, { choiceIndex: 2, choiceText: 'C', correct: true, answeredAt: 300 }), true);
assert.equal(p.answers[0].attemptNumber, 2, 'retry increments attempt number');
assert.equal(getPracticeAttemptCount(p, 0), 2);
assert.equal(getLatestPracticeAttempt(p, 0).correct, true, 'current attempt is the latest result');
assert.deepEqual(summarizePracticeProgress(p, 2), { attempted: 1, correct: 1, totalAttempts: 2, accuracy: 100 });

recordPracticeAnswer(p, 1, { choiceIndex: 0, choiceText: 'A', correct: false, answeredAt: 400 });
assert.equal(archiveAllPracticeAnswersForRetry(p, 500), 2, 'whole-lesson retry archives every active answer');
assert.equal(Object.keys(p.answers).length, 0, 'whole-lesson retry unlocks all active questions');
assert.equal(countAttemptedPracticeQuestions(p, 2), 2, 'history remains counted as attempted question coverage');
assert.equal(getPracticeAttemptCount(p, 1), 1);
assert.equal(archivePracticeAnswerForRetry(p, 1, 600), false, 'retrying an already-unlocked question is a safe no-op');

const legacy = ensurePracticeProgress({ answers: { 0: { answered: true, correct: false, choiceIndex: 3 } } });
assert.equal(countAttemptedPracticeQuestions(legacy, 1), 1, 'legacy IndexedDB progress works without a migration');
assert.equal(getPracticeAttemptCount(legacy, 0), 1);
console.log('Practice retry PASS: per-question retry, full-set retry, historical attempts, latest-result analytics and legacy v1 progress compatibility.');
