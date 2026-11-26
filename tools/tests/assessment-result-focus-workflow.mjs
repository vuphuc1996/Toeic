import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const nodes = new Map();

class FakeNode {
  constructor() {
    this.hidden = true;
    this.inert = false;
    this.disabled = false;
    this.innerHTML = '';
    this.textContent = '';
    this.className = '';
    this.scrollTop = 0;
    this.dataset = {};
    this.attributes = {};
    this.children = [];
    this.parentNode = null;
    this.confirmButton = { focused: false, focus() { this.focused = true; } };
    const classes = new Set();
    this.classList = {
      add: (...values) => values.forEach(value => classes.add(value)),
      remove: (...values) => values.forEach(value => classes.delete(value)),
      contains: value => classes.has(value),
      toggle: (value, force) => {
        if (force === undefined ? !classes.has(value) : force) classes.add(value);
        else classes.delete(value);
        return classes.has(value);
      },
    };
  }
  append(node) { node.parentNode = this; this.children.push(node); }
  remove() {
    if (!this.parentNode) return;
    this.parentNode.children = this.parentNode.children.filter(child => child !== this);
    this.parentNode = null;
  }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  getAttribute(name) { return Object.hasOwn(this.attributes, name) ? this.attributes[name] : null; }
  removeAttribute(name) { delete this.attributes[name]; }
  focus() { this.focused = true; }
  querySelector(selector) { return selector === '[data-assessment-confirm]' ? this.confirmButton : null; }
}

function $(selector) {
  if (!nodes.has(selector)) nodes.set(selector, new FakeNode());
  return nodes.get(selector);
}

const context = {
  learningFocusState: { active: true, kind: 'learning-detail', nodes: [] },
  assessmentResultFocusState: null,
  state: {
    modalActionInProgress: false,
    pendingPracticeBatch: null,
    pendingFoundationAssessment: null,
    pendingSinglePractice: null,
    pendingFlashQuizResult: null,
    pendingPlacementResult: false,
    pendingMockResult: null,
  },
  $, document: {
    createElement() { return new FakeNode(); },
    body: { classList: { add() {}, remove() {}, contains() { return false; } } },
  },
  setLearningFocusHeader(title, subtitle, eyebrow) {
    $('#learningFocusTitle').textContent = title;
    $('#learningFocusSubtitle').textContent = subtitle;
    $('#learningFocusEyebrow').textContent = eyebrow;
  },
  hideModalLayer() {
    $('#modalLayer').hidden = true;
    $('#modalLayer').setAttribute('aria-hidden', 'true');
    $('#learningFocusDialog').setAttribute('aria-hidden', 'false');
    context.modalLayerHideCount = (context.modalLayerHideCount || 0) + 1;
  },
  assessmentConfettiMarkup: () => '<div class="assessment-result-confetti"></div>',
  escapeHtml: value => String(value ?? ''),
  async confirmPendingAssessmentResult(options) {
    context.confirmed = true;
    context.confirmationOptions = [...(context.confirmationOptions || []), options];
  },
  returnToPracticeBatch() { context.returnedToPractice = true; },
  returnToFoundationAssessment() { context.returnedToFoundation = true; },
  renderPlacementQuestion() { context.renderedPlacement = true; },
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

expose('closeLearningFocus', 'function syncPracticeModeSelection');
expose('assessmentResultBodyMarkup', 'function showAssessmentResultInLearningFocus');
expose('showAssessmentResultInLearningFocus', 'function restoreAssessmentResultLearningFocus');
expose('restoreAssessmentResultLearningFocus', 'function showAssessmentResultModal');
expose('showAssessmentResultModal', 'function closeAssessmentResultModal');
expose('closeAssessmentResultModal', 'function getPracticeBatch');
expose('handleAssessmentResultSurfaceAction', 'function bindEvents');

$('#learningFocusBackdrop').hidden = false;
$('#learningFocusDialog').setAttribute('aria-hidden', 'false');
$('#learningFocusTitle').textContent = 'Bài học đang làm';
$('#learningFocusSubtitle').textContent = 'Nội dung hiện tại';
$('#learningFocusEyebrow').textContent = 'FOUNDATION';
$('#learningFocusClose').setAttribute('aria-label', 'Thoát phiên học');
$('#modalLayer').hidden = false;
$('#modalLayer').setAttribute('aria-hidden', 'false');
const lessonPanel = new FakeNode();
lessonPanel.hidden = false;
lessonPanel.inert = false;
$('#learningFocusContent').append(lessonPanel);

context.showAssessmentResultModal({
  eyebrow: 'LISTENING · SESSION COMPLETE',
  title: 'Bạn đã hoàn thành lượt học',
  correct: 8,
  incorrect: 2,
  total: 10,
  description: 'Đã hoàn thành toàn bộ câu hỏi.',
});

assert.equal($('#modalLayer').hidden, true, 'active learning focus must not open the redundant modal layer');
assert.equal(context.modalLayerHideCount, 1, 'any prior modal layer is closed before the inline result is displayed');
assert.equal($('#modalLayer').attributes['aria-hidden'], 'true');
assert.equal($('#modalLayer').dataset.modalType, undefined, 'inline result must not register itself as a modal-layer result');
assert.equal($('#learningFocusBackdrop').hidden, false, 'the single existing focus backdrop remains active');
assert.equal($('#learningFocusDialog').attributes['aria-hidden'], 'false');
assert.equal($('#learningFocusTitle').textContent, 'Bạn đã hoàn thành lượt học');
assert.equal($('#learningFocusEyebrow').textContent, 'LISTENING · SESSION COMPLETE');
assert.equal(lessonPanel.hidden, true, 'previous lesson content is temporarily hidden, not destroyed');
assert.equal(lessonPanel.inert, true, 'hidden lesson content is removed from keyboard interaction');
assert.equal(lessonPanel.attributes['aria-hidden'], 'true');
assert.equal($('#learningFocusContent').children.length, 2);
const resultPanel = $('#learningFocusContent').children[1];
assert.match(resultPanel.className, /assessment-result-inline/);
assert.match(resultPanel.innerHTML, /data-assessment-confirm/);
assert.equal($('#learningFocusClose').attributes['aria-label'], 'Xác nhận kết quả');
assert.equal(resultPanel.confirmButton.focused, true, 'keyboard focus moves to the primary confirmation action');

context.closeLearningFocus();
await Promise.resolve();
assert.equal(context.confirmationOptions.at(-1).openReviewForSingle, false, 'the Learning Focus close control confirms pending results safely');
context.confirmed = false;

await context.handleAssessmentResultSurfaceAction({ target: { closest: selector => selector === '[data-assessment-confirm]' ? {} : null } });
assert.equal(context.confirmed, true, 'inline confirmation uses the existing safe result-commit handler');

context.closeAssessmentResultModal();
assert.equal(assessmentStateIsCleared(), true);
assert.equal($('#modalLayer').hidden, true);
assert.equal($('#learningFocusBackdrop').hidden, false, 'restoring the result does not close the learning workspace');
assert.equal($('#learningFocusTitle').textContent, 'Bài học đang làm');
assert.equal($('#learningFocusSubtitle').textContent, 'Nội dung hiện tại');
assert.equal($('#learningFocusEyebrow').textContent, 'FOUNDATION');
assert.equal($('#learningFocusClose').attributes['aria-label'], 'Thoát phiên học');
assert.equal(lessonPanel.hidden, false);
assert.equal(lessonPanel.inert, false);
assert.equal(lessonPanel.getAttribute('aria-hidden'), null);
assert.deepEqual($('#learningFocusContent').children, [lessonPanel]);

function assessmentStateIsCleared() {
  return context.assessmentResultFocusState === null;
}

console.log('Assessment result focus workflow PASS: active sessions reuse learningFocusDialog; prior modal is hidden; X/confirm actions use the existing safe confirmation path; previous content is restored.');
