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
      toggle: (value, force) => { if (force === undefined ? !classes.has(value) : force) classes.add(value); else classes.delete(value); return classes.has(value); },
    },
    setAttribute(name, value) { this.attributes[name] = String(value); },
    removeAttribute(name) { delete this.attributes[name]; },
    focus() { this.focused = true; },
    querySelector() { return null; },
  };
}
function $(selector) {
  if (!nodes.has(selector)) nodes.set(selector, makeNode());
  return nodes.get(selector);
}
const context = {
  learningFocusState: { active: false, kind: '', nodes: [] },
  assessmentResultFocusState: null,
  document: { body: { classList: { add() {}, remove() {}, contains() { return false; } } } },
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
  closeAssessmentResultModal() { context.resetModalLayer(); },
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

expose('showModalLayer', 'function hideModalLayer');
expose('hideModalLayer', 'function openLearningFocus');
expose('resetModalLayer', 'async function confirmPendingAssessmentResult');
expose('confirmPendingAssessmentResult', 'async function dismissPracticeReviewModal');
expose('dismissPracticeReviewModal', 'function closeModal');
expose('closeModal', 'function downloadFile');
expose('closeAutoAdvanceWaitModal', 'function showAutoAdvanceWaitModal');
expose('cancelAutoAdvanceWait', 'async function acknowledgePracticeReview');
expose('assessmentResultBodyMarkup', 'function showAssessmentResultInLearningFocus');
expose('showAssessmentResultInLearningFocus', 'function restoreAssessmentResultLearningFocus');
expose('showAssessmentResultModal', 'function closeAssessmentResultModal');
expose('maybeShowPracticeBatchResult', 'async function stagePracticeBatchAnswer');
expose('confirmSinglePracticeResult', 'async function nextQuestion');
expose('showSinglePracticeResult', 'async function confirmSinglePracticeResult');

// A completed single answer shows a real results modal with the three requested statistics.
context.state.pendingSinglePractice = { wordId: 'w-1', correct: true, mode: 'word-to-meaning' };
context.showSinglePracticeResult();
assert.equal($('#modalLayer').hidden, false);
assert.equal($('#modalLayer').dataset.modalType, 'assessment-result');
assert.equal($('#closeModal').hidden, false, 'result modal must expose a safe close action');
assert.equal($('#closeModal').focused, true, 'result modal must put keyboard focus on the close control');
assert.match($('#modalContent').innerHTML, /<strong>1<\/strong><span>Đúng<\/span>/);
assert.match($('#modalContent').innerHTML, /<strong>0<\/strong><span>Chưa đúng<\/span>/);
assert.match($('#modalContent').innerHTML, /<strong>1<\/strong><span>Tổng câu<\/span>/);

// Completing a multi-question practice set displays aggregate completion statistics.
context.state.pendingSinglePractice = null;
assert.equal(context.maybeShowPracticeBatchResult('grammar', 'lesson-1'), true);
assert.equal($('#modalLayer').hidden, false);
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
$('#modalLayer').hidden = false;
$('#modalLayer').dataset.modalType = 'assessment-result';
context.closeModal();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(context.state.pendingSinglePractice, null);
assert.equal(context.state.practiceReviewPending, false);
assert.equal($('#modalLayer').hidden, true, 'closing a completed-answer result must actually hide modalLayer');
assert.equal(context.renderedQuestion, true, 'answer explanation remains available inline after safe close');

// The modal-aware close dispatcher maps each remaining modal to a safe next action.
context.state.pendingPracticeBatch = { id: 'batch' };
$('#modalLayer').hidden = false;
$('#modalLayer').dataset.modalType = 'assessment-result';
context.closeModal();
await Promise.resolve();
assert.equal(context.confirmedBatch, true, 'closing assessment result confirms and commits the staged batch');
context.state.pendingPracticeBatch = null;

context.state.practiceReviewPending = true;
$('#modalLayer').hidden = false;
$('#modalLayer').dataset.modalType = 'practice-review';
context.closeModal();
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(context.state.practiceReviewPending, false);
assert.equal(context.state.autoAdvanceCancelled, true);
assert.equal($('#modalLayer').hidden, true);
assert.equal(context.updatedAutoAdvance, true);
assert.equal(context.savedSession, true, 'closing explanation modal must persist the current answered question');

context.state.autoAdvanceWaiting = true;
$('#modalLayer').hidden = false;
$('#modalLayer').dataset.modalType = 'practice-wait';
context.closeModal();
await Promise.resolve();
assert.equal(context.state.autoAdvanceWaiting, false, 'closing the wait modal cancels the timer');
assert.equal(context.state.autoAdvanceCancelled, true);
assert.equal($('#modalLayer').hidden, true, 'closing the wait modal must hide the backdrop');

// A modal with no pending workflow still closes and clears every transient visual state.
context.state.autoAdvanceWaiting = false;
$('#modalLayer').hidden = false;
$('#modalLayer').dataset.modalType = 'ordinary';
$('#modalLayer').classList.add('is-practice-review', 'is-auto-advance-wait', 'is-learning-detail');
context.closeModal();
assert.equal($('#modalLayer').hidden, true);
assert.equal($('#modalLayer').dataset.modalType, undefined);
for (const cls of ['is-practice-review', 'is-auto-advance-wait', 'is-learning-detail']) {
  assert.equal($('#modalLayer').classList.contains(cls), false, `stale modal class must be removed: ${cls}`);
}
assert.match(source, /#closeModal'\)\.addEventListener\('click',closeModal\)/, 'the close control must be wired to the state-aware dispatcher');
assert.match(source, /else if\(\$\('#modalLayer'\)&&!\$\('#modalLayer'\)\.hidden\)\{e\.preventDefault\(\);closeModal\(\);\}/, 'Escape must close the visible modal through the same safe dispatcher');
assert.doesNotMatch(source, /modalBackdrop|modal-backdrop/, 'the duplicate modal backdrop must be removed from source');
const html = fs.readFileSync(new URL('../../index.html', import.meta.url), 'utf8');
assert.match(html, /id="modalLayer"[^>]*hidden/, 'modal panel layer must live in the shared learning focus overlay');
assert.doesNotMatch(html, /id="modalBackdrop"|class="modal-backdrop"/, 'there must not be a second full-screen backdrop');
assert.equal((html.match(/class="learning-focus-backdrop"/g) || []).length, 1, 'the application must use exactly one full-screen learning backdrop');

// A regular modal activates the shared learning backdrop without a second dimming surface.
context.learningFocusState.active = false;
context.showModalLayer();
assert.equal($('#learningFocusBackdrop').hidden, false);
assert.equal($('#learningFocusBackdrop').classList.contains('is-modal-only'), true);
assert.equal($('#modalLayer').hidden, false);
context.hideModalLayer();
assert.equal($('#learningFocusBackdrop').hidden, true, 'closing a modal-only overlay hides the one shared backdrop');

// A modal opened during a focused session reuses the existing backdrop and keeps the session mounted.
context.learningFocusState.active = true;
$('#learningFocusBackdrop').hidden = false;
context.showModalLayer();
assert.equal($('#learningFocusBackdrop').classList.contains('is-modal-only'), false);
assert.equal($('#learningFocusBackdrop').hidden, false, 'closing a nested modal must not close the active focus session');
assert.equal($('#learningFocusDialog').attributes['aria-hidden'], 'true');
context.hideModalLayer();
assert.equal($('#learningFocusBackdrop').hidden, false);
assert.equal($('#learningFocusDialog').attributes['aria-hidden'], 'false');
context.learningFocusState.active = false;
$('#learningFocusBackdrop').hidden = true;
assert.equal($('#learningFocusDialog').attributes['aria-hidden'], 'false');
console.log('Modal dismissal workflow PASS: assessment statistics render; X/Escape dispatch safely commits or dismisses each pending state; learning progress remains saved; normal and focused modals share one dimming backdrop.');
