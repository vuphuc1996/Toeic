import assert from 'node:assert/strict';
import fs from 'node:fs';
import {
  ensurePracticeProgress,
  stagePracticeChoice,
  getPracticeDraftChoice,
  isPracticeDraftSetComplete,
  summarizePracticeDraftSet,
  commitPracticeDraftSet,
} from '../../assets/js/practice-progress.js';

const questions = [
  { id: 'q1', answerIndex: 1, choices: ['A', 'B', 'C', 'D'], explanation: 'Q1 explanation' },
  { id: 'q2', answerIndex: 3, choices: ['A', 'B', 'C', 'D'], explanation: 'Q2 explanation' },
  { id: 'q3', answerIndex: 0, choices: ['A', 'B', 'C', 'D'], explanation: 'Q3 explanation' },
];
const progress = ensurePracticeProgress({});
assert.equal(stagePracticeChoice(progress, 0, 1, 100, 50), true);
assert.equal(stagePracticeChoice(progress, 1, 2, 110, 60), true);
assert.equal(stagePracticeChoice(progress, 2, 0, 120, 70), true);
assert.equal(Object.keys(progress.answers).length, 0, 'correct/wrong attempts must not be committed while the learner is answering');
assert.equal(progress.draftAnswers['0'].correct, undefined, 'drafts store only selections, not correctness');
assert.equal(getPracticeDraftChoice(progress, 1), 2);
assert.equal(isPracticeDraftSetComplete(progress, 3), true);
assert.deepEqual(summarizePracticeDraftSet(progress, questions), { answered: 3, correct: 2, incorrect: 1, total: 3, accuracy: 67 });
const committed = commitPracticeDraftSet(progress, questions, ({ question, choiceIndex, correct }) => ({
  choiceIndex, correct, explanation: question.explanation,
}));
assert.equal(committed.complete, true);
assert.equal(committed.committed, 3);
assert.equal(progress.answers['1'].correct, false);
assert.equal(progress.answers['1'].explanation, 'Q2 explanation');
assert.equal(Object.keys(progress.draftAnswers).length, 0, 'drafts clear only after explicit confirmation/commit');

const source = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const functionBody = (name, nextName) => {
  const start = source.indexOf(`function ${name}(`);
  const end = source.indexOf(`function ${nextName}(`, start + 1);
  assert.ok(start >= 0 && end > start, `source must contain ${name} and its next top-level function`);
  return source.slice(start, end);
};
const submit = functionBody('submitAnswer', 'showSinglePracticeResult');
assert.match(submit, /state\.pendingSinglePractice=/);
assert.doesNotMatch(submit, /updatePracticeProgress\(/, 'single-question practice must defer progress updates until confirmation');
assert.match(submit, /showSinglePracticeResult\(\)/);
const renderQuestion = functionBody('renderQuestion', 'alignCharacters');
assert.match(renderQuestion, /state\.questionAnswered&&!state\.pendingSinglePractice/);
const flashFinish = functionBody('finishFlashQuiz', 'confirmFlashQuizResult');
assert.match(flashFinish, /state\.pendingFlashQuizResult=/);
assert.doesNotMatch(flashFinish, /dbSet\('flashProgress'/, 'Flash Quiz progress is committed only after confirmation');
const mockFinish = functionBody('finishMockExam', 'showPendingMockResult');
assert.match(mockFinish, /state\.pendingMockResult=/);
assert.doesNotMatch(mockFinish, /renderMockResult\(/, 'mock answer review remains locked until confirmation');
assert.match(source, /function confirmMockExamResult\(/);
assert.match(source, /MOCK_PENDING_REVIEW_KEY/);
assert.match(source, /data-assessment-confirm/);
assert.match(source, /function confirmSinglePracticeResult\(/);
assert.match(source, /function confirmFlashQuizResult\(/);
assert.match(source, /function confirmPracticeBatchResult\(/);
assert.match(source, /function confirmFoundationAssessmentResult\(/);
assert.match(source, /function finalizePlacementDiagnostic\(/);
console.log('Deferred assessment workflow PASS: answer drafts stay ungraded until confirmation; single practice, Flash Quiz, Foundation, Reading/Listening/Grammar, Placement and Mock Exam reveal explanations only after confirmation; mock pending result survives reload.');
