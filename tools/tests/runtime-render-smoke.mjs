import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const appSource = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const nodes = new Map();
function $(selector) {
  if (!nodes.has(selector)) {
    const classes = new Set();
    nodes.set(selector, {
      value: '', hidden: true, textContent: '', innerHTML: '',
      classList: { add: (...names) => names.forEach(name => classes.add(name)), remove: (...names) => names.forEach(name => classes.delete(name)), contains: name => classes.has(name) },
    });
  }
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
    listening: [], listeningProgress: {},
  },
  $,
  normalizeText: value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(),
  escapeHtml: value => String(value ?? '').replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[ch]),
  displayWord: value => String(value || ''),
  choiceIdAt: (question, index) => Array.isArray(question?.choiceIds) ? String(question.choiceIds[index] || '') : '',
  savedChoiceWrongClass: () => false,
  savedChoiceHistoryMarkup: () => '',
  icon: () => '<span></span>',
  stopSpeech: () => {},
  openLearningFocus: () => {},
  dbSet: async (key, value) => { context.persisted ??= {}; context.persisted[key] = structuredClone(value); context.persistedWrites = (context.persistedWrites || 0) + 1; },
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
exposeFunction('openLearningDetail', 'function closeLearningFocus(');
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
assert.equal($('#modalBackdrop').hidden, true, 'learning detail must use the common focus shell, not the legacy detail modal');
assert.match($('#modalContent').innerHTML, /learning-detail-surface/);

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
assert.match($('#modalContent').innerHTML, /learning-detail-surface/);

context.state.grammarLessons = [{
  id: 'grammar-runtime-smoke', category: 'Tenses', level: 'A2', title: 'Present simple',
  summary: 'Present simple lesson', formula: 'S + V(s/es)', explanation: 'Diễn tả thói quen.',
  examples: [], tips: [], exercises: [{ question: 'She ___ to work.', choices: ['go', 'goes', 'going', 'gone'], answerIndex: 1, explanation: 'She là ngôi thứ ba số ít.' }]
}];
openGrammarLesson('grammar-runtime-smoke');
assert.match($('#modalContent').innerHTML, /goes/);
assert.match($('#modalContent').innerHTML, /BÀI TẬP 1/);
assert.match($('#modalContent').innerHTML, /learning-detail-surface/);


const migrationStart = appSource.indexOf('async function migrateChoiceIdentity(');
const migrationEnd = appSource.indexOf('function emptyPersonalVocabulary(', migrationStart);
assert.notEqual(migrationStart, -1);
assert.notEqual(migrationEnd, -1);
vm.runInContext(`${appSource.slice(migrationStart, migrationEnd)}\nglobalThis.__migrate = migrateChoiceIdentity;`, context, { timeout: 1000 });
const oldReading = { answered: true, choiceIndex: 1, choiceText: 'old distractor', correct: false, answeredAt: 123 };
context.state.readings = [{ id: 'legacy-reading', questions: [{ choices: ['A', 'new distractor', 'C', 'D'], choiceIds: ['r-a', 'r-b', 'r-c', 'r-d'], legacyChoices: ['A', 'old distractor', 'C', 'D'], legacyChoiceIds: ['legacy:r-a', 'legacy:r-b', 'legacy:r-c', 'legacy:r-d'] }, { choices: ['A', 'new distractor', 'C', 'D'], choiceIds: ['r-a2', 'r-b2', 'r-c2', 'r-d2'], legacyChoices: ['A', 'old distractor', 'C', 'D'], legacyChoiceIds: ['legacy:r-a2', 'legacy:r-b2', 'legacy:r-c2', 'legacy:r-d2'] }] }];
context.state.readingProgress = { 'legacy-reading': { answers: { 0: oldReading, 1: { answered: true, choiceIndex: 1, choiceText: 'C', correct: true, answeredAt: 124 }, 2: { answered: true, choiceIndex: 1, choiceText: 'unmapped historical text', correct: false, answeredAt: 125 } } } };
context.state.listening = [{ id: 'legacy-listening', questions: [{ choices: ['A', 'B', 'C', 'D'], choiceIds: ['l-a', 'l-b', 'l-c', 'l-d'] }] }];
context.state.listeningProgress = { 'legacy-listening': { answers: { 0: { answered: true, choiceIndex: 2, correct: true, answeredAt: 456 } } } };
context.state.grammarLessons = [{ id: 'legacy-grammar', exercises: [{ choices: ['A', 'B', 'C', 'D'], choiceIds: ['g-a', 'g-b', 'g-c', 'g-d'] }] }];
context.state.grammarProgress = { 'legacy-grammar': { answers: { 0: { answered: true, choiceIndex: 3, correct: false, answeredAt: 789 } } } };

// A pre-v2.16 profile without choiceId must resolve through the stored v2.16 option snapshot.
const readingLibrary = JSON.parse(fs.readFileSync(new URL('../../data/readings/reading-library.json', import.meta.url), 'utf8'));
const movedOld = readingLibrary.readings.find(item => item.id === 'office-schedule');
const movedOldQuestion = movedOld.questions[1];
context.state.readings.push(movedOld);
context.state.readingProgress['office-schedule'] = { answers: { 1: { answered: true, choiceIndex: 1, correct: true, answeredAt: 234 } } };

// A v2.16 profile already has a stable ID, but its saved index still points to the old position.
const movedCurrent = readingLibrary.readings.find(item => item.id === 'part7-single-training-email');
const movedCurrentQuestion = movedCurrent.questions[1];
const currentChoiceId = movedCurrentQuestion.previousChoiceIds[1];
context.state.readings.push(movedCurrent);
context.state.readingProgress['part7-single-training-email'] = { answers: { 1: { answered: true, choiceIndex: 1, choiceId: currentChoiceId, choiceText: movedCurrentQuestion.previousChoices[1], correct: true, answeredAt: 345 } } };

// Exercise a moved Listening item and an unchanged Grammar item through the same migration path.
const listeningLibrary = JSON.parse(fs.readFileSync(new URL('../../data/listening/listening-library.json', import.meta.url), 'utf8'));
const movedListening = listeningLibrary.listening.find(item => item.id === 'part3-shipping-delay');
context.state.listening.push(movedListening);
context.state.listeningProgress[movedListening.id] = { answers: { 1: { answered: true, choiceIndex: 1, correct: true, answeredAt: 567 } } };

await context.__migrate();
assert.equal(context.state.readingProgress['legacy-reading'].answers[0].choiceId, 'legacy:r-b');
assert.equal(context.state.readingProgress['legacy-reading'].answers[0].choiceIndex, 1);
assert.equal(context.state.readingProgress['legacy-reading'].answers[0].choiceText, 'old distractor');
assert.equal(context.state.readingProgress['legacy-reading'].answers[1].choiceId, 'r-c2');
assert.equal(context.state.readingProgress['legacy-reading'].answers[1].choiceIndex, 2);
assert.equal(context.state.readingProgress['legacy-reading'].answers[2].choiceId, undefined);
assert.equal(context.state.readingProgress['legacy-reading'].answers[2].choiceText, 'unmapped historical text');
assert.equal(context.state.listeningProgress['legacy-listening'].answers[0].choiceId, 'l-c');
assert.equal(context.state.grammarProgress['legacy-grammar'].answers[0].choiceId, 'g-d');
assert.equal(context.state.readingProgress['office-schedule'].answers[1].choiceId, movedOldQuestion.previousChoiceIds[1]);
assert.equal(context.state.readingProgress['office-schedule'].answers[1].choiceIndex, 3);
assert.equal(context.state.readingProgress['office-schedule'].answers[1].previousChoiceIndex, 1);
assert.equal(context.state.readingProgress['office-schedule'].answers[1].choiceText, movedOldQuestion.previousChoices[1]);
assert.equal(context.state.readingProgress['part7-single-training-email'].answers[1].choiceIndex, 3);
assert.equal(context.state.readingProgress['part7-single-training-email'].answers[1].previousChoiceIndex, 1);
assert.equal(context.state.readingProgress['part7-single-training-email'].answers[1].correct, true);
assert.equal(context.state.readingProgress['part7-single-training-email'].answers[1].answeredAt, 345);
assert.equal(context.state.listeningProgress[movedListening.id].answers[1].choiceIndex, 3);
assert.equal(context.persisted.readingProgress['office-schedule'].answers[1].choiceIndex, 3);
assert.equal(context.persisted.listeningProgress[movedListening.id].answers[1].choiceIndex, 3);

// Migration is idempotent: an immediate second startup must not write progress again.
const writesAfterFirstMigration = context.persistedWrites;
await context.__migrate();
assert.equal(context.persistedWrites, writesAfterFirstMigration);

// A stable ID identifies the selected option even when a saved index is stale.
const selectedOldDId = movedCurrentQuestion.previousChoiceIds[3];
const savedWrongChoice = { answered: true, choiceIndex: 3, choiceId: selectedOldDId, choiceText: movedCurrentQuestion.previousChoices[3], correct: false };
const wrongBlockStart = appSource.indexOf('function savedChoiceIsArchived(');
const wrongBlockEnd = appSource.indexOf('function displayWord(', wrongBlockStart);
vm.runInContext(`${appSource.slice(wrongBlockStart, wrongBlockEnd)}\nglobalThis.__wrongClass = savedChoiceWrongClass;`, context, { timeout: 1000 });
assert.equal(context.__wrongClass(movedCurrentQuestion, savedWrongChoice, 1), true);
assert.equal(context.__wrongClass(movedCurrentQuestion, savedWrongChoice, 3), false);

console.log('Runtime render/migration smoke PASS: Reading/Listening/Grammar, archived options, v2.15→v2.17 and v2.16→v2.17 choice-ID migration, stale-index rendering and idempotency.');
