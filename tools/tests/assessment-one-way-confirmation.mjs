import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const context = {
  assessmentConfettiMarkup: () => '<div class="confetti"></div>',
  escapeHtml: value => String(value ?? ''),
};
vm.createContext(context);
const markupStart = source.indexOf('function assessmentResultBodyMarkup(');
const markupEnd = source.indexOf('function showAssessmentResultInLearningFocus(', markupStart);
assert.ok(markupStart >= 0 && markupEnd > markupStart);
vm.runInContext(`${source.slice(markupStart, markupEnd)}\nglobalThis.__markup = assessmentResultBodyMarkup;`, context);
const markup = context.__markup({ correct: 8, incorrect: 2, total: 10, description: 'Đã hoàn thành.' });
assert.equal((markup.match(/<button\b/g) || []).length, 1, 'result prompt must expose one action only');
assert.match(markup, /data-assessment-confirm/);
assert.match(markup, /Xác nhận &amp; xem đáp án/);
assert.doesNotMatch(markup, /data-assessment-return|Quay lại kiểm tra/);
assert.doesNotMatch(source, /allowReturn|data-assessment-return|returnToPracticeBatch|returnToFoundationAssessment|Các lựa chọn tạm đã được lưu/);

// The click dispatcher must no longer recognize the deleted return action.
const actionStart = source.indexOf('async function handleAssessmentResultSurfaceAction(');
const actionEnd = source.indexOf('\nfunction bindEvents(', actionStart);
assert.ok(actionStart >= 0 && actionEnd > actionStart);
assert.doesNotMatch(source.slice(actionStart, actionEnd), /assessment-return|renderPlacementQuestion/);

// Foundation persistence failure must leave the pending submission and staged selections intact.
const foundationStart = source.indexOf('function confirmFoundationAssessmentResult(');
const foundationEnd = source.indexOf('\nfunction renderLearningObjectiveProgress(', foundationStart);
assert.ok(foundationStart >= 0 && foundationEnd > foundationStart);
const failedState = {
  pendingFoundationAssessment: { kind: 'foundation-recognition', lessonId: 'lesson-1', questions: [{ id: 'q1', answerIndex: 1 }], key: 'foundation-recognition::lesson-1' },
  foundationAssessmentDrafts: { 'foundation-recognition::lesson-1': { answers: { q1: 1 }, answeredAt: { q1: 100 } } },
  foundationProgress: { existing: { attempted: true } },
};
let persistedFailure = false;
const failedContext = {
  state: failedState,
  recordFoundationAttempt: (progress, lesson, question, correct, at) => ({ ...progress, [lesson]: { evidence: { [question]: { correct, at } } } }),
  recordFoundationApplicationAttempt: (progress) => progress,
  recordFoundationReadingAttempt: (progress) => progress,
  recordFoundationListeningAttempt: (progress) => progress,
  localStorage: { setItem() { persistedFailure = true; throw new Error('quota'); } },
  console: { warn() {} },
  toast() {},
  saveFoundationAssessmentDrafts() {},
  closeAssessmentResultModal() { throw new Error('must not close on failed save'); },
  openFoundationLesson() { throw new Error('must not reopen on failed save'); },
  renderFoundationPath() {},
};
vm.createContext(failedContext);
vm.runInContext(`${source.slice(foundationStart, foundationEnd)}\nglobalThis.__confirm = confirmFoundationAssessmentResult;`, failedContext);
assert.throws(() => failedContext.__confirm(), /Lựa chọn tạm vẫn được giữ/);
assert.equal(persistedFailure, true);
assert.deepEqual(failedState.foundationProgress, { existing: { attempted: true } }, 'failed persistence must not mutate in-memory committed progress');
assert.equal(failedState.pendingFoundationAssessment.key, 'foundation-recognition::lesson-1');
assert.deepEqual(failedState.foundationAssessmentDrafts['foundation-recognition::lesson-1'].answers, { q1: 1 });

// Successful confirmation writes the updated ledger before clearing the pending result.
const successState = {
  pendingFoundationAssessment: { kind: 'foundation-recognition', lessonId: 'lesson-2', questions: [{ id: 'q2', answerIndex: 0 }], key: 'foundation-recognition::lesson-2' },
  foundationAssessmentDrafts: { 'foundation-recognition::lesson-2': { answers: { q2: 0 }, answeredAt: { q2: 200 } } },
  foundationProgress: { prior: { attempted: true } },
};
const writes = [];
const successContext = {
  state: successState,
  recordFoundationAttempt: (progress, lesson, question, correct, at) => ({ ...progress, [lesson]: { evidence: { [question]: { correct, at } } } }),
  recordFoundationApplicationAttempt: progress => progress,
  recordFoundationReadingAttempt: progress => progress,
  recordFoundationListeningAttempt: progress => progress,
  localStorage: { setItem(key, value) { writes.push([key, value]); } },
  console,
  toast() {},
  saveFoundationAssessmentDrafts() { successContext.draftSaveObserved = Object.hasOwn(successState.foundationAssessmentDrafts, 'foundation-recognition::lesson-2') === false; },
  closeAssessmentResultModal() { successContext.closed = true; },
  openFoundationLesson(lessonId) { successContext.openedLesson = lessonId; },
  renderFoundationPath() { successContext.rendered = true; },
};
vm.createContext(successContext);
vm.runInContext(`${source.slice(foundationStart, foundationEnd)}\nglobalThis.__confirm = confirmFoundationAssessmentResult;`, successContext);
successContext.__confirm();
assert.equal(writes.length, 1);
assert.equal(writes[0][0], 'toeic:foundation-progress:v1');
assert.deepEqual(JSON.parse(writes[0][1]).prior, { attempted: true });
assert.equal(JSON.parse(writes[0][1])['lesson-2'].evidence.q2.correct, true);
assert.equal(successState.pendingFoundationAssessment, null);
assert.equal(Object.hasOwn(successState.foundationAssessmentDrafts, 'foundation-recognition::lesson-2'), false);
assert.equal(successContext.draftSaveObserved, true);
assert.equal(successContext.closed, true);
assert.equal(successContext.openedLesson, 'lesson-2');
assert.equal(successContext.rendered, true);

console.log('Assessment one-way confirmation PASS: exactly one result action; deleted return routes are absent; Foundation save failure preserves drafts/pending state; successful confirmation persists before revealing review.');
