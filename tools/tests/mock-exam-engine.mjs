import assert from 'node:assert/strict';
import fs from 'node:fs';
import {
  createMockExam,
  getExamQuestions,
  getMockSectionForTime,
  scoreMockExam,
  MOCK_MODES,
  isMockEligible,
} from '../../assets/js/mock-engine.js';

const listening = JSON.parse(fs.readFileSync(new URL('../../data/listening/listening-library.json', import.meta.url), 'utf8')).listening;
const readings = JSON.parse(fs.readFileSync(new URL('../../data/readings/reading-library.json', import.meta.url), 'utf8')).readings;
const rand = (() => { let n = 42; return () => { n = (n * 1664525 + 1013904223) % 4294967296; return n / 4294967296; }; })();
const make = (modeId, history = [], usageCounts = null, random = rand) => createMockExam({ modeId, listening, readings, history, usageCounts, random, now: () => 1_800_000_000_000 });
const countByPart = questions => Object.fromEntries(['Part 1','Part 2','Part 3','Part 4','Part 5','Part 6','Part 7'].map(part => [part, questions.filter(q => q.part === part).length]));

// Timing must exactly equal the three user-defined formats.
assert.equal(MOCK_MODES.quick.listeningSeconds + MOCK_MODES.quick.readingSeconds, 15 * 60);
assert.equal(MOCK_MODES.half.listeningSeconds + MOCK_MODES.half.readingSeconds, 60 * 60);
assert.equal(MOCK_MODES.full.listeningSeconds + MOCK_MODES.full.readingSeconds, 120 * 60);

// Reserve-pending questions stay out of mock exams until independent review.
const reservedUnits = listening.filter(item => item.editorialStatus === 'reserve-pending-independent-review');
const reservedUnitIds = new Set(reservedUnits.map(item => item.id));
assert.equal(reservedUnits.reduce((n,item) => n + item.questions.length,0), 98);
assert.equal(reservedUnits.filter(item => item.editorialBatch === '014').reduce((n,item) => n + item.questions.length,0), 17);
assert.equal(reservedUnits.filter(item => item.editorialBatch === '015').reduce((n,item) => n + item.questions.length,0), 70);
assert.equal(reservedUnits.filter(item => !item.editorialBatch).reduce((n,item) => n + item.questions.length,0), 11);
assert.equal(isMockEligible({ id: 'legacy-item' }), true, 'legacy records without editorialStatus remain eligible');
assert.equal(isMockEligible({ id: 'approved-item', editorialStatus: 'approved-for-mock' }), true);
assert.equal(isMockEligible({ id: 'v233-reviewed-item', editorialStatus: 'internal-editorial-reviewed' }), true, 'the previously shipped v2.33 internal-review state remains compatible');
assert.equal(isMockEligible({ id: 'pending-item', editorialStatus: 'reserve-pending-independent-review' }), false);
assert.equal(isMockEligible({ id: 'unknown-item', editorialStatus: 'editorial-review-pending' }), false, 'unknown editorial statuses must fail closed');

// Quick practice: 12 Listening + 13 Reading and exactly 25 unique IDs.
const quick = make('quick');
const quickL = getExamQuestions(quick.sections.listening);
const quickR = getExamQuestions(quick.sections.reading);
assert.equal(quickL.length, 12);
assert.equal(quickR.length, 13);
assert.deepEqual(countByPart([...quickL, ...quickR]), {
  'Part 1': 1, 'Part 2': 2, 'Part 3': 6, 'Part 4': 3,
  'Part 5': 2, 'Part 6': 4, 'Part 7': 7,
});
assert.equal(new Set(quick.questionIds).size, 25);

// Half test: exact 50 + 50 questions. P3/P4 and P6/P7 sets remain indivisible.
const half = make('half');
const halfL = getExamQuestions(half.sections.listening);
const halfR = getExamQuestions(half.sections.reading);
assert.equal(halfL.length, 50);
assert.equal(halfR.length, 50);
assert.equal(halfL.filter(q => q.part === 'Part 3').length % 3, 0);
assert.equal(halfL.filter(q => q.part === 'Part 4').length % 3, 0);
assert.equal(halfR.filter(q => q.part === 'Part 6').length % 4, 0);
assert.equal(halfR.filter(q => q.part === 'Part 7' && q.unitId).length, 27);
assert.equal(new Set(half.questionIds).size, 100);

// Full test: exact TOEIC L&R section/part blueprint.
const full = make('full');
const fullL = getExamQuestions(full.sections.listening);
const fullR = getExamQuestions(full.sections.reading);
assert.equal(fullL.length, 100);
assert.equal(fullR.length, 100);
assert.deepEqual(countByPart([...fullL, ...fullR]), {
  'Part 1': 6, 'Part 2': 25, 'Part 3': 39, 'Part 4': 30,
  'Part 5': 30, 'Part 6': 16, 'Part 7': 54,
});
const fullP7 = full.sections.reading.groups.filter(group => group.part === 'Part 7');
const isMulti = group => group.documents.length > 1 || /double|triple|multiple/i.test(group.documentType);
assert.equal(fullP7.filter(group => !isMulti(group)).reduce((n, group) => n + group.questions.length, 0), 29);
assert.equal(fullP7.filter(isMulti).reduce((n, group) => n + group.questions.length, 0), 25);
assert.equal(fullP7.filter(isMulti).length, 5, 'Part 7 multiple passage section must contain five complete 5-question blocks');
assert.ok(fullP7.filter(group => !isMulti(group)).every(group => group.questions.length >= 2 && group.questions.length <= 4), 'single passages must retain complete 2–4 question blocks');
assert.ok(fullP7.filter(isMulti).every(group => group.questions.length === 5), 'double/triple passages must remain complete 5-question blocks');
assert.equal(new Set(full.questionIds).size, 200);
assert.ok(full.sections.listening.groups.every(group => !reservedUnitIds.has(group.unitId)), 'all reserve units must remain outside Mock Exam until independent review');
assert.equal(full.questionIds.length, 200);

// Every selected multi-question source block preserves all its questions.
for (const group of full.sections.listening.groups.filter(group => ['Part 3','Part 4'].includes(group.part))) {
  assert.equal(group.questions.length, 3, `${group.unitId} must remain a full 3-question audio block`);
}
for (const group of full.sections.reading.groups.filter(group => group.part === 'Part 6')) {
  assert.equal(group.questions.length, 4, `${group.unitId} must remain a full 4-question text block`);
}

// Cross-attempt selection prioritizes questions not used by the previous form.
const quickNext = make('quick', [{ questionIds: quick.questionIds }]);
assert.equal(quickNext.questionIds.filter(id => quick.questionIds.includes(id)).length, 0);
const lifetimeUsage = Object.fromEntries(quick.questionIds.map(id => [id, 1]));
const quickNextFromLifetimeLedger = make('quick', [], lifetimeUsage);
assert.equal(quickNextFromLifetimeLedger.questionIds.filter(id => quick.questionIds.includes(id)).length, 0, 'the persistent usage ledger must rotate away from every question in the previous Quick test');
const usedFullForm = Object.fromEntries(full.questionIds.map(id => [id, 1]));
const secondFull = make('full', [], usedFullForm);
assert.equal(new Set(secondFull.questionIds).size, 200, 'a new Full form must never contain an internal duplicate');
assert.ok(secondFull.questionIds.some(id => !usedFullForm[id]), 'the next Full form should prioritize any never-used eligible questions');
const firstReadingIds = fullR.map(q => q.id);
const secondReadingIds = getExamQuestions(secondFull.sections.reading).map(q => q.id);
const firstListeningIds = fullL.map(q => q.id);
const secondListeningIds = getExamQuestions(secondFull.sections.listening).map(q => q.id);
assert.equal(secondReadingIds.length, 100);
assert.equal(secondReadingIds.filter(id => firstReadingIds.includes(id)).length, 0, 'two consecutive Full forms must not reuse eligible Reading questions');
assert.equal(secondListeningIds.filter(id => firstListeningIds.includes(id)).length, 98, 'the 102-question eligible Listening pool allows only two new questions in the next 100-question form');
assert.equal(secondListeningIds.filter(id => !firstListeningIds.includes(id)).length, 2, 'the next Full Listening section must prioritize the two never-used eligible questions');

// Timed section boundary and completion state.
assert.equal(getMockSectionForTime(full, full.startedAt + 1), 'listening');
assert.equal(getMockSectionForTime(full, full.listeningDeadlineAt), 'reading');
assert.equal(getMockSectionForTime(full, full.totalDeadlineAt), 'expired');

// Scoring handles incorrect and unanswered items without treating blanks as correct.
const scoreExam = make('quick');
const scoreQuestions = [...getExamQuestions(scoreExam.sections.listening), ...getExamQuestions(scoreExam.sections.reading)];
scoreExam.answers[scoreQuestions[0].id] = scoreQuestions[0].answerIndex;
scoreExam.answers[scoreQuestions[1].id] = (scoreQuestions[1].answerIndex + 1) % scoreQuestions[1].choices.length;
const result = scoreMockExam(scoreExam);
assert.equal(result.total.questions, 25);
assert.equal(result.total.correct, 1);
assert.equal(result.total.answered, 2);
assert.equal(result.total.unanswered, 23);
assert.ok(result.listening.target75 >= 0);
assert.ok(result.reading.target75 >= 0);
assert.ok(result.parts['Part 1']);

console.log('Mock exam engine PASS: quick 15m (25Q), half 60m (100Q), full 120m (200Q), exact Part blueprint, indivisible blocks, 98 reserve questions excluded, unknown editorial states fail closed, no in-form duplicates, usage rotation, timer boundaries and scoring.');
