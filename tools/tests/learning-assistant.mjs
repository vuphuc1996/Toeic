import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { hasLearningFootprint, summarizePartProgress, summarizeCollectionProgress, summarizeEvidenceLedger, buildCompanionSnapshot, buildCompanionMessage } from '../../assets/js/learning-assistant.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const moduleSource = read('assets/js/learning-assistant.js');
const app = read('assets/js/app.js');
const sw = read('sw.js');

assert.equal(hasLearningFootprint({}), false, 'A new device with no evidence must be recognized as first run.');
assert.equal(hasLearningFootprint({ wordProgress: { w1: { reviewCount: 1 } } }), true, 'Vocabulary practice must identify returning learners.');
assert.equal(hasLearningFootprint({ flashProgress: { w1: { lapses: 1 } } }), true, 'Flashcard practice must identify returning learners.');
assert.equal(hasLearningFootprint({ readingProgress: { r1: { answers: { 0: { answered: true, correct: false } } } } }), true, 'Reading answers must identify returning learners.');
assert.equal(hasLearningFootprint({ foundationProgress: { lesson1: { evidence: { q1: { attempts: [{ correct: true }] } } } } }), true, 'Foundation evidence must identify returning learners.');
assert.equal(hasLearningFootprint({ mockHistory: [{ status: 'completed' }] }), true, 'Completed mock exam must identify returning learners.');
assert.equal(hasLearningFootprint({ placementResult: { completedAt: 123 } }), true, 'A completed Placement Diagnostic must identify returning learners.');

const parts = summarizePartProgress(
  [{ id: 'read1', part: 'Part 5', questions: [{}, {}] }],
  { read1: { answers: { '0': { answered: true, correct: false } }, attemptHistory: { '0': [{ answered: true, correct: true }, { answered: true, correct: false }], '1': [{ answered: true, correct: true }] } } },
  ['Part 5']
);
assert.deepEqual(parts[0], { part: 'Part 5', total: 2, answered: 2, correct: 1, attempts: 4, accuracy: 50 });

const grammarSummary = summarizeCollectionProgress(
  [{ id: 'g1', exercises: [{}, {}, {}] }],
  { g1: { answers: { '0': { answered: true, correct: true }, '1': { answered: true, correct: false }, '2': { answered: true, correct: false } } } },
  'exercises'
);
assert.deepEqual(grammarSummary, { total: 3, answered: 3, correct: 1, attempts: 3, lessonsStarted: 1, accuracy: 33 });
const foundationEvidenceSummary = summarizeEvidenceLedger({ lesson1: { evidence: { q1: { latestCorrect: true, attempts: [{}, {}] }, q2: { latestCorrect: false, attempts: [{}] } } } });
assert.deepEqual(foundationEvidenceSummary, { lessonsStarted: 1, uniqueQuestions: 2, correct: 1, attempts: 3, accuracy: 50 });

const snapshot = buildCompanionSnapshot({
  words: [
    { id: 'a', word: 'arrange', senses: [{ meaning_vi: 'sắp xếp' }] },
    { id: 'b', word: 'invoice', senses: [{ meaning_vi: 'hóa đơn' }] },
    { id: 'c', word: 'confirm', senses: [{ meaning_vi: 'xác nhận' }] }
  ],
  wordProgress: {
    a: { reviewCount: 4, correctCount: 1, wrongCount: 3, dueAt: 100 },
    b: { reviewCount: 2, correctCount: 2, wrongCount: 0, dueAt: 900000 },
    c: { reviewCount: 1, correctCount: 1, wrongCount: 0, dueAt: 900000 }
  },
  readings: [{ id: 'r5', part: 'Part 5', questions: [{}, {}, {}] }],
  readingProgress: { r5: { answers: { '0': { answered: true, correct: false }, '1': { answered: true, correct: true }, '2': { answered: true, correct: false } } } },
  foundationDue: 2,
  a2Portfolio: { startedTasks: 5, totalTasks: 13, revisedTasks: 2, selfReportedImproved: 1, selfReportedUnchanged: 1, selfReportedReduced: 0 },
  latestMock: { score: { total: { accuracy: 72, correct: 144, questions: 200 } } },
  mockHistory: [{ status: 'completed' }],
  placementResult: { recommended: 'A1' },
  grammarLessons: [{ id: 'g1', title: 'Present Perfect', exercises: [{}, {}, {}] }],
  grammarProgress: { g1: { answers: { '0': { answered: true, correct: true }, '1': { answered: true, correct: false }, '2': { answered: true, correct: false } } } },
  foundationReadingProgress: { lesson1: { evidence: { q1: { latestCorrect: true } } } },
  foundationListeningProgress: { lesson2: { evidence: { q2: { latestCorrect: false } } } },
  flashProgress: { f1: { reps: 3, lastQuiz: 100 }, f2: { reps: 1, lapses: 1 } }
}, 1000);
assert.equal(snapshot.reviewedWords, 3);
assert.equal(snapshot.reviewed, 7);
assert.equal(snapshot.accuracy, 57);
assert.equal(snapshot.dueWords, 1);
assert.equal(snapshot.weakWords[0].word, 'arrange');
assert.equal(snapshot.weakestPart.part, 'Part 5');
assert.equal(snapshot.foundationDue, 2);
assert.equal(snapshot.a2Portfolio.revisedTasks, 2);
assert.equal(snapshot.latestMock.accuracy, 72);
assert.equal(snapshot.placementLevel, 'A1');
assert.equal(snapshot.weakestGrammarLesson.title, 'Present Perfect');
assert.equal(snapshot.grammarSummary.answered, 3);
assert.equal(snapshot.foundationReading.uniqueQuestions, 1);
assert.equal(snapshot.foundationListening.uniqueQuestions, 1);
assert.equal(snapshot.flashReviewedCards, 2);
assert.equal(snapshot.flashRepetitions, 4);

assert.equal(buildCompanionMessage(snapshot, 'reading').tone, 'encourage');
assert.match(buildCompanionMessage(snapshot, 'mock').message, /72%/);
assert.match(buildCompanionMessage(snapshot, 'foundation').message, /2 câu Foundation/);
assert.match(buildCompanionMessage(snapshot, 'dashboard', { title: 'Chúc mừng', message: 'Đã hoàn thành.', tone: 'success' }).title, /Chúc mừng/);

for (const forbidden of ['fetch(', 'XMLHttpRequest', 'google.com', 'buildWordAIPrompt', 'promptToGoogle']) assert.ok(!moduleSource.includes(forbidden), `Local companion must not use external AI/network: ${forbidden}`);
assert.ok(app.includes("from './learning-assistant.js'"), 'The application must use the shared local companion module.');
assert.ok(app.includes('grammarLessons:state.grammarLessons') && app.includes('foundationReadingProgress:state.foundationReadingProgress') && app.includes('foundationListeningProgress:state.foundationListeningProgress'), 'Robot context must include the existing Grammar and Foundation Reading/Listening ledgers.');
assert.ok(app.includes("case 'review-words'") && app.includes("$('#weakWordList')"), 'The word review recommendation must point to the existing weak-word list.');
assert.ok(sw.includes('./assets/js/learning-assistant.js'), 'The module must be available offline.');
assert.ok(sw.includes('./assets/js/quick-help.js'), 'The retired helper path must remain cached as a compatibility tombstone for stale GitHub checkouts.');
assert.ok(fs.readFileSync(path.join(root, 'assets/js/quick-help.js'), 'utf8').match(/intentionally executes nothing/i), 'The stale Quick Help JS file must be overwritten by a safe no-op tombstone.');

console.log('PASS: local evidence detection, latest-attempt part statistics, weak-area/writing/mock summary, first-run signals and strictly offline Robot Buddy.');
