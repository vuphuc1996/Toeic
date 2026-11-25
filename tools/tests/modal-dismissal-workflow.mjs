import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const nodes = new Map();
function makeNode() {
  const classes = new Set();
  return {
    hidden: true,
    disabled: false,
    innerHTML: '',
    textContent: '',
    dataset: {},
    attributes: {},
    classList: {
      add: (...values) => values.forEach(value => classes.add(value)),
      remove: (...values) => values.forEach(value => classes.delete(value)),
      contains: value => classes.has(value),
    },
    setAttribute(name, value) { this.attributes[name] = String(value); },
    removeAttribute(name) { delete this.attributes[name]; },
    focus() { this.focused = true; },
  };
}
function $(selector) {
  if (!nodes.has(selector)) nodes.set(selector, makeNode());
  return nodes.get(selector);
}
const context = {
  state: {
    modalActionInProgress: false,
    pendingPracticeBatch: null,
    pendingFoundationAssessment: null,
    pendingSinglePractice: null,
    pendingFlashQuizResult: null,
    pendingPlacementResult: false,
    pendingMockResult: null,
    practiceReviewPending: false,
    autoAdvanceWaiting: false,
    autoAdvanceCancelled: false,
    questionAnswered: true,
    reminder: { enabled: false },
    currentQuestion: { wordId: 'w-1', id: 'q-1', mode: 'word-to-meaning' },
    lastFeedback: { correct: true, input: 'invoice', expected: 'invoice' },
    progress: { 'w-1': { streak: 1 } },
    sessionSeenIds: [],
    sentenceCompletionSeenIds: [],
  },
  $, stopSpeech() {}, toast(message) { context.toasts.push(message); }, toasts: [],
  clearAutoAdvance() { context.clearedTimers = (context.clearedTimers || 0) + 1; },
  async savePracticeSession() { context.savedSession = true; },
  renderQuestion() { context.renderedQuestion = true; },
  updateAutoAdvanceUI() { context.updatedAutoAdvance = true; },
  async updatePracticeProgress() { context.updatedProgress = true; },
  renderReminderStatus() {},
  openPracticeReviewModal() { context.openedReview = true; },
  closeAssessmentResultModal() { $('#modalBackdrop').hidden = true; },
  async confirmPracticeBatchResult() { context.confirmedBatch = true; },
  getPracticeBatch() { return { progress: {}, questions: Array.from({ length: 10 }, () => ({})) }; },
  isPracticeDraftSetComplete() { return true; },
  summarizePracticeDraftSet() { return { answered: 10, correct: 8, incorrect: 2, total: 10 }; },
  async confirmFoundationAssessmentResult() { context.confirmedFoundation = true; },
  async confirmFlashQuizResult() { context.confirmedFlash = true; },
  async confirmMockExamResult() { context.confirmedMock = true; },
  finalizePlacementDiagnostic() { context.finalizedPlacement = true; },
  escapeHtml: value => String(value ?? ''),
  assessmentConfettiMarkup: () => '<div class="confetti"></div>',
  console: { error() {} },
};
vm.createContext(context);

function expose(name, endMarker) {
  const start = source.indexOf(`function ${name}(`);
  const asyncStart = source.indexOf(`async function ${name}(`);
  const actualStart = asyncStart >= 0 && (start < 0 || asyncStart < start) ? asyncStart : start;
  assert.ok(actualStart >= 0, `missing ${name}`);
  const end = source.indexOf(endMarker, actualStart);
  assert.ok(end > actualStart, `missing end marker for ${name}`);
  vm.runInContext(`${source.slice(actualStart, end)}\nglobalThis.__exposed = ${name};`, context, { timeout: 1000 });
  return context.__exposed;
}

expose('resetModalBackdrop', 'async function confirmPendingAssessmentResult');
expose('confirmPendingAssessmentResult', 'async function dismissPracticeReviewModal');
expose('dismissPracticeReviewModal', 'function closeModal');
expose('closeModal', 'function downloadFile');
expose('closeAutoAdvanceWaitModal', 'function showAutoAdvanceWaitModal');
expose('cancelAutoAdvanceWait', 'async function acknowledgePracticeReview');
expose('showAssessmentResultModal', 'function closeAssessmentResultModal');
expose('maybeShowPracticeBatchResult', 'async function stagePracticeBatchAnswer');
expose('confirmSinglePracticeResult', 'async function nextQuestion');
expose('showSinglePracticeResult', 'async function confirmSinglePracticeResult');

// A completed single answer shows a real results modal with the three requested statistics.
context.state.pendingSinglePractice = { wordId: 'w-1', correct: true, mode: 'word-to-meaning' };
context.showSinglePracticeResult();
assert.equal($('#modalBackdrop').hidden, false);
assert.equal($('#modalBackdrop').dataset.modalType, 'assessment-result');
assert.equal($('#closeModal').hidden, false, 'result modal must expose a safe close action');
assert.equal($('#closeModal').focused, true, 'result modal must put keyboard focus on the close control');
assert.match($('#modalContent').innerHTML, /<strong>1<\/strong><span>Đúng<\/span>/);
assert.match($('#modalContent').innerHTML, /<strong>0<\/strong><span>Chưa đúng<\/span>/);
assert.match($('#modalContent').innerHTML, /<strong>1<\/strong><span>Tổng câu<\/span>/);

// Completing a multi-question practice set displays aggregate completion statistics.
context.state.pendingSinglePractice = null;
assert.equal(context.maybeShowPracticeBatchResult('grammar', 'lesson-1'), true);
assert.equal($('#modalBackdrop').hidden, false);
assert.equal(context.state.pendingPracticeBatch.kind, 'grammar');
assert.match($('#modalContent').innerHTML, /<strong>8<\/strong><span>Đúng<\/span>/);
assert.match($('#modalContent').innerHTML, /<strong>2<\/strong><span>Chưa đúng<\/span>/);
assert.match($('#modalContent').innerHTML, /<strong>10<\/strong><span>Tổng câu<\/span>/);
context.state.pendingPracticeBatch = null;

// Closing a pending single-answer result commits it without opening another blocking modal.
context.state.pendingSinglePractice = { wordId: 'w-1', correct: true, input: 'invoice', answeredAt: 100, responseDurationMs: 20 };
context.state.practiceReviewPending = true;
await context.confirmSinglePracticeResult({ openReview: false });
assert.equal(context.state.pendingSinglePractice, null);
assert.equal(context.state.practiceReviewPending, false);
assert.equal(context.state.autoAdvanceCancelled, true);
assert.equal(context.openedReview, undefined, 'safe close keeps feedback inline instead of reopening a modal');
assert.equal(context.renderedQuestion, true);
assert.equal(context.savedSession, true);

// The modal-aware close dispatcher commits a pending single answer and closes the overlay.
context.state.pendingSinglePractice = { wordId: 'w-1', correct: false, input: 'invoices', answeredAt: 200, responseDurationMs: 30 };
context.state.practiceReviewPending = true;
context.state.lastFeedback = { correct: false, input: 'invoices', expected: 'invoice' };
context.state.progress = { 'w-1': { streak: 0 } };
$('#modalBackdrop').hidden = false;
$('#modalBackdrop').dataset.modalType = 'assessment-result';
context.closeModal();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(context.state.pendingSinglePractice, null);
assert.equal(context.state.practiceReviewPending, false);
assert.equal($('#modalBackdrop').hidden, true, 'closing a completed-answer result must actually hide modalBackdrop');
assert.equal(context.renderedQuestion, true, 'answer explanation remains available inline after safe close');

// The modal-aware close dispatcher maps each remaining modal to a safe next action.
context.state.pendingPracticeBatch = { id: 'batch' };
$('#modalBackdrop').hidden = false;
$('#modalBackdrop').dataset.modalType = 'assessment-result';
context.closeModal();
await Promise.resolve();
assert.equal(context.confirmedBatch, true, 'closing assessment result confirms and commits the staged batch');
context.state.pendingPracticeBatch = null;

context.state.practiceReviewPending = true;
$('#modalBackdrop').hidden = false;
$('#modalBackdrop').dataset.modalType = 'practice-review';
context.closeModal();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(context.state.practiceReviewPending, false);
assert.equal(context.state.autoAdvanceCancelled, true);
assert.equal($('#modalBackdrop').hidden, true);
assert.equal(context.updatedAutoAdvance, true);
assert.equal(context.savedSession, true, 'closing explanation modal must persist the current answered question');

context.state.autoAdvanceWaiting = true;
$('#modalBackdrop').hidden = false;
$('#modalBackdrop').dataset.modalType = 'practice-wait';
context.closeModal();
await Promise.resolve();
assert.equal(context.state.autoAdvanceWaiting, false, 'closing the wait modal cancels the timer');
assert.equal(context.state.autoAdvanceCancelled, true);
assert.equal($('#modalBackdrop').hidden, true, 'closing the wait modal must hide the backdrop');

// A modal with no pending workflow still closes and clears every transient visual state.
context.state.autoAdvanceWaiting = false;
$('#modalBackdrop').hidden = false;
$('#modalBackdrop').dataset.modalType = 'ordinary';
$('#modalBackdrop').classList.add('is-practice-review', 'is-auto-advance-wait', 'is-learning-detail');
context.closeModal();
assert.equal($('#modalBackdrop').hidden, true);
assert.equal($('#modalBackdrop').dataset.modalType, undefined);
for (const cls of ['is-practice-review', 'is-auto-advance-wait', 'is-learning-detail']) {
  assert.equal($('#modalBackdrop').classList.contains(cls), false, `stale modal class must be removed: ${cls}`);
}
assert.match(source, /#closeModal'\)\.addEventListener\('click',closeModal\)/, 'the close control must be wired to the state-aware dispatcher');
assert.match(source, /else if\(\$\('#modalBackdrop'\)&&!\$\('#modalBackdrop'\)\.hidden\)\{e\.preventDefault\(\);closeModal\(\);\}/, 'Escape must close the visible modal through the same safe dispatcher');
console.log('Modal dismissal workflow PASS: single- and multi-question completion statistics render; keyboard focus reaches the close control; X/Escape dispatch safely commits or dismisses each pending state; learning progress remains saved; stale backdrop classes are cleared.');
