import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import { ensurePracticeProgress, countAttemptedPracticeQuestions, getPracticeAttemptHistory, getPracticeAttemptCount, recordPracticeAnswer, archivePracticeAnswerForRetry, archiveAllPracticeAnswersForRetry, stagePracticeChoice, getPracticeDraftChoice, getPracticeDraftEntries, isPracticeDraftSetComplete } from '../../assets/js/practice-progress.js';
import { ensureObjectiveProgress, recordObjectiveAttempt } from '../../assets/js/learning-outcome-progress.js';

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
    listening: [], listeningProgress: {}, objectiveProgress: {}, objectiveResourceIndex: { 'part7-runtime-smoke': ['reading-part-7'], 'grammar-runtime-smoke': ['grammar-core'], 'listening-runtime-smoke': ['listening-part-2'] }, objectiveResourceMap: null,
  },
  $,
  normalizeText: value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(),
  escapeHtml: value => String(value ?? '').replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[ch]),
  displayWord: value => String(value || ''),
  choiceIdAt: (question, index) => Array.isArray(question?.choiceIds) ? String(question.choiceIds[index] || '') : '',
  savedChoiceWrongClass: () => false,
  savedChoiceHistoryMarkup: () => '',
  icon: () => '<span></span>',
  ensurePracticeProgress, countAttemptedPracticeQuestions, getPracticeAttemptHistory, getPracticeAttemptCount, recordPracticeAnswer, archivePracticeAnswerForRetry, archiveAllPracticeAnswersForRetry, stagePracticeChoice, getPracticeDraftChoice, getPracticeDraftEntries, isPracticeDraftSetComplete, ensureObjectiveProgress, recordObjectiveAttempt, renderLearningObjectiveProgress: () => {},
  practiceDraftToolbar: (kind,id,progress,questions) => { const count=getPracticeDraftEntries(progress).filter(entry=>entry.index<questions.length).length; return count ? `<div class=\"assessment-draft-toolbar\">Đã chọn tạm ${count}/${questions.length} câu</div>` : ''; }, maybeShowPracticeBatchResult: (kind,id) => { context.lastPracticeBatch = { kind, id }; },
  requestAnimationFrame: callback => callback(),
  renderToeicPartInsights: () => {}, renderReadingLibrary: () => {}, renderListeningLibrary: () => {}, renderGrammarLibrary: () => {},
  toast: () => {}, window: { confirm: () => true },
  stopSpeech: () => {},
  openLearningFocus: () => {},
  dbSet: async (key, value) => { context.persisted ??= {}; context.persisted[key] = structuredClone(value); context.persistedWrites = (context.persistedWrites || 0) + 1; },
};
vm.createContext(context);

function exposeFunction(name, nextToken) {
  const asyncStart = appSource.indexOf(`async function ${name}(`);
  const normalStart = appSource.indexOf(`function ${name}(`);
  const start = asyncStart >= 0 && (normalStart < 0 || asyncStart < normalStart) ? asyncStart : normalStart;
  assert.notEqual(start, -1, `missing ${name}`);
  const next = appSource.indexOf(nextToken, start);
  assert.notEqual(next, -1, `missing boundary after ${name}`);
  // Extract only the top-level function body; adjacent helper declarations must
  // not be accidentally re-evaluated into the shared VM context.
  const close = appSource.indexOf('\n}', start);
  const end = close >= 0 && close + 2 <= next ? close + 2 : next;
  const source = appSource.slice(start, end);
  vm.runInContext(`${source}\nglobalThis.__render = ${name};`, context, { timeout: 1000 });
  return context.__render;
}

exposeFunction('trackObjectivePractice', 'async function saveObjectivePractice(');
exposeFunction('saveObjectivePractice', 'function renderLearningObjectiveProgress(');
exposeFunction('practiceAttemptHistoryMarkup', 'function practiceRetryActionMarkup');
exposeFunction('practiceRetryActionMarkup', 'function practiceRetryAllToolbar');
exposeFunction('practiceRetryAllToolbar', 'async function retryPracticeQuestion');
const renderReadingLibrary = exposeFunction('renderReadingLibrary', 'function openReadingDetail(');
const openReadingDetail = exposeFunction('openReadingDetail', 'async function answerReadingQuestion(');
const answerReadingQuestion = exposeFunction('answerReadingQuestion', 'function renderListeningLibrary(');
context.openReadingDetail = openReadingDetail;
const retryPracticeQuestion = exposeFunction('retryPracticeQuestion', 'async function retryAllPracticeQuestions(');
const retryAllPracticeQuestions = exposeFunction('retryAllPracticeQuestions', 'function renderGrammarLibrary(');
exposeFunction('openLearningDetail', 'function closeLearningFocus(');
const openGrammarLesson = exposeFunction('openGrammarLesson', 'async function answerGrammarExercise(');
context.openGrammarLesson = openGrammarLesson;
const answerGrammarExercise = exposeFunction('answerGrammarExercise', 'function renderReadingLibrary(');
const openListeningDetail = exposeFunction('openListeningDetail', 'let listeningPlaybackToken');
context.openListeningDetail = openListeningDetail;
const answerListeningQuestion = exposeFunction('answerListeningQuestion', 'function buildListeningAIPrompt(');
context.stagePracticeBatchAnswer = async (kind, id, index, choiceIndex) => {
  const config = { reading: ['readingProgress', 'openReadingDetail'], grammar: ['grammarProgress', 'openGrammarLesson'], listening: ['listeningProgress', 'openListeningDetail'] }[kind];
  assert.ok(config, `unknown staged practice kind ${kind}`);
  const progressStore = context.state[config[0]];
  const progress = ensurePracticeProgress(progressStore[id] || {});
  const now = Date.now();
  assert.equal(stagePracticeChoice(progress, index, choiceIndex, now, now), true);
  progressStore[id] = progress;
  context.lastStagedAnswer = { kind, id, index, choiceIndex };
  await context.dbSet(config[0], progressStore);
  context[config[1]](id);
};

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


// Exercise Reading/Grammar/Listening answer handlers: choices must remain drafts until confirmation.
context.readingProgress = {};
await answerReadingQuestion({ dataset: { readingId: part7.id, questionIndex: '0', choiceIndex: '0' } });
assert.equal(context.lastStagedAnswer.kind, 'reading');
assert.equal(context.state.readingProgress[part7.id].answers[0], undefined, 'Reading must not commit correctness when a choice is selected');
assert.equal(context.state.readingProgress[part7.id].draftAnswers['0'].choiceIndex, 0, 'Reading stores the selected choice as a draft');
assert.match($('#modalContent').innerHTML, /is-selected/, 'the selected Reading choice remains visibly selected');
assert.doesNotMatch($('#modalContent').innerHTML, /Thông tin nằm trong thư trả lời/, 'Reading explanation stays hidden before confirmation');

context.state.grammarProgress = {};
await answerGrammarExercise({ dataset: { lessonId: 'grammar-runtime-smoke', exerciseIndex: '0', choiceIndex: '0' } });
assert.equal(context.lastStagedAnswer.kind, 'grammar');
assert.equal(context.state.grammarProgress['grammar-runtime-smoke'].answers[0], undefined, 'Grammar must not commit correctness when a choice is selected');
assert.equal(context.state.grammarProgress['grammar-runtime-smoke'].draftAnswers['0'].choiceIndex, 0);
assert.doesNotMatch($('#modalContent').innerHTML, /She là ngôi thứ ba số ít/, 'Grammar explanation stays hidden before confirmation');

context.state.listening = [{ id: 'listening-runtime-smoke', part: 'Part 2', type: 'question-response', topic: 'Workplace', level: 'A2', title: 'Part 2 retry smoke', segments: [{ speaker: 'Woman', text: 'When will the report be ready?' }], vocabulary: [], questions: [{ question: 'When will the report be ready?', choices: ['By noon', 'At reception', 'The finance team'], answerIndex: 0, explanation: 'The response gives a time.' }] }];
context.state.listeningProgress = {};
openListeningDetail('listening-runtime-smoke');
await answerListeningQuestion({ dataset: { listeningId: 'listening-runtime-smoke', questionIndex: '0', choiceIndex: '1' } });
assert.equal(context.lastStagedAnswer.kind, 'listening');
assert.equal(context.state.listeningProgress['listening-runtime-smoke'].answers[0], undefined, 'Listening must not commit correctness when a choice is selected');
assert.equal(context.state.listeningProgress['listening-runtime-smoke'].draftAnswers['0'].choiceIndex, 1);
assert.doesNotMatch($('#modalContent').innerHTML, /The response gives a time/, 'Listening explanation stays hidden before confirmation');



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

console.log('Runtime render/migration smoke PASS: Reading/Listening/Grammar rendering, deferred answer drafts without correctness or explanations, archived options, stable choice-ID migration and idempotency.');
