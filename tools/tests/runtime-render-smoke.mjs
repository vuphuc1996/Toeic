import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const appSource = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const nodes = new Map();
function $(selector) {
  if (!nodes.has(selector)) nodes.set(selector, { value: '', hidden: true, textContent: '', innerHTML: '' });
  return nodes.get(selector);
}
const context = {
  state: {
    readings: [],
    readingProgress: {},
    grammarLessons: [],
    grammarProgress: {},
    activeReading: null,
    activeGrammarLesson: null,
  },
  $,
  normalizeText: value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(),
  escapeHtml: value => String(value ?? '').replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[ch]),
  displayWord: value => String(value || ''),
  savedChoiceWrongClass: () => false,
  savedChoiceHistoryMarkup: () => '',
  icon: () => '<span></span>',
};
vm.createContext(context);

function exposeFunction(name, nextToken) {
  const start = appSource.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `missing ${name}`);
  const end = appSource.indexOf(nextToken, start);
  assert.notEqual(end, -1, `missing boundary after ${name}`);
  const source = appSource.slice(start, end);
  vm.runInContext(`${source}\nglobalThis.__render = ${name};`, context, { timeout: 1000 });
  return context.__render;
}

const renderReadingLibrary = exposeFunction('renderReadingLibrary', 'function openReadingDetail(');
const openReadingDetail = exposeFunction('openReadingDetail', 'async function answerReadingQuestion(');
const openGrammarLesson = exposeFunction('openGrammarLesson', 'async function answerGrammarExercise(');

const part5 = {
  id: 'part5-runtime-smoke', part: 'Part 5', topic: 'Workplace', documentType: 'Incomplete sentences',
  level: 'A2', title: 'Part 5 runtime smoke', wordCount: 0, questions: [{
    question: 'The manager ___ the report.', choices: ['review', 'reviews', 'reviewed', 'reviewing'], answerIndex: 1,
    explanation: 'Chủ ngữ số ít dùng động từ thêm -s.'
  }]
};
context.state.readings = [part5];
renderReadingLibrary();
assert.match($('#readingCardList').innerHTML, /1 câu luyện/);
assert.match($('#readingCardList').innerHTML, /1 câu đã làm/);
openReadingDetail(part5.id);
assert.match($('#modalContent').innerHTML, /reviews/);
assert.match($('#modalContent').innerHTML, /PART 5 · INCOMPLETE SENTENCES/);
assert.equal($('#modalBackdrop').hidden, false);

const part7 = {
  id: 'part7-runtime-smoke', part: 'Part 7', topic: 'Orders', documentType: 'Double passage', level: 'B1',
  title: 'Part 7 document smoke', wordCount: 18, passage: '',
  documents: [{ label: 'EMAIL', content: 'Please review the purchase order.' }, { label: 'REPLY', content: 'We will ship the items tomorrow.' }],
  questions: [{ question: 'When will the items ship?', choices: ['Today', 'Tomorrow', 'Friday', 'Next week'], answerIndex: 1, explanation: 'Thông tin nằm trong thư trả lời.' }]
};
context.state.readings = [part7];
renderReadingLibrary();
openReadingDetail(part7.id);
assert.match($('#modalContent').innerHTML, /Please review the purchase order/);
assert.match($('#modalContent').innerHTML, /We will ship the items tomorrow/);
assert.match($('#modalContent').innerHTML, /Tomorrow/);

context.state.grammarLessons = [{
  id: 'grammar-runtime-smoke', category: 'Tenses', level: 'A2', title: 'Present simple',
  summary: 'Present simple lesson', formula: 'S + V(s/es)', explanation: 'Diễn tả thói quen.',
  examples: [], tips: [], exercises: [{ question: 'She ___ to work.', choices: ['go', 'goes', 'going', 'gone'], answerIndex: 1, explanation: 'She là ngôi thứ ba số ít.' }]
}];
openGrammarLesson('grammar-runtime-smoke');
assert.match($('#modalContent').innerHTML, /goes/);
assert.match($('#modalContent').innerHTML, /BÀI TẬP 1/);

console.log('Runtime render smoke PASS: Reading Part 5, Reading Part 7 multi-document, Grammar detail.');
