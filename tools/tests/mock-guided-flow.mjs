import assert from 'node:assert/strict';
import { buildMockQuestionSchedule, getMockScheduledQuestion, getMockTransitionLeadIn, getMockQuestionTimeRemaining } from '../../assets/js/mock-flow.js';

const listening = { groups: [
  { unitId: 'p1-a', part: 'Part 1', title: 'Photograph A', segments: [{ text: 'Now listen to four statements. Passengers are boarding an aircraft by stairs. A suitcase is being weighed at a counter.' }], questions: [{ id: 'l1', question: 'Which statement is correct?', choices: ['A','B','C','D'] }] },
  { unitId: 'p3-a', part: 'Part 3', title: 'Meeting conversation', segments: [{ text: 'Good morning. The meeting begins at nine. Please bring the report.' }], questions: [{ id: 'l2', question: 'What time does the meeting begin?', choices: ['8','9','10','11'] }, { id: 'l3', question: 'What should the listener bring?', choices: ['Report','Laptop','Invoice','Map'] }] },
]};
const start = 1_000_000;
const listeningSchedule = buildMockQuestionSchedule(listening, 'listening', start, 322);
assert.equal(listeningSchedule.length, 3);
assert.equal(listeningSchedule[0].startAt, start);
assert.equal(listeningSchedule.at(-1).endAt, start + 322_000);
assert.ok(listeningSchedule.every((slot, index) => slot.allottedMs > 0 && (!index || slot.startAt === listeningSchedule[index - 1].endAt)));
assert.equal(getMockScheduledQuestion(listeningSchedule, start).questionId, 'l1');
assert.equal(getMockScheduledQuestion(listeningSchedule, listeningSchedule[1].startAt).questionId, 'l2');
assert.equal(getMockQuestionTimeRemaining(listeningSchedule[0], start), Math.ceil(listeningSchedule[0].allottedMs / 1000));
const firstLead = getMockTransitionLeadIn(null, listeningSchedule[0], 12);
assert.match(firstLead, /Listening section.*Part 1.*Question 1 of 12/s);
const nextGroupLead = getMockTransitionLeadIn(listeningSchedule[0], listeningSchedule[1], 12);
assert.match(nextGroupLead, /Next group.*Part 3.*Question 2 of 12/s);
const sameGroupLead = getMockTransitionLeadIn(listeningSchedule[1], listeningSchedule[2], 12);
assert.match(sameGroupLead, /Continue with the same audio/);

const reading = { groups: [
  { unitId: 'r5-1', part: 'Part 5', passage: '', questions: [{ id: 'r1', question: 'The new policy will _____ on Monday.', choices: ['take effect','effect','effective','affect'] }] },
  { unitId: 'r7-1', part: 'Part 7', title: 'Notice', passage: ' '.repeat(0) + 'The company announces a series of important changes to the annual training schedule. Employees are requested to review the revised timetable and contact the administrative office if additional information is required.', questions: [{ id: 'r2', question: 'What should employees do?', choices: ['Review the schedule','Cancel training','Pay a fee','Call a customer'] }, { id: 'r3', question: 'Who can provide more information?', choices: ['The admin office','A supplier','A customer','A hotel'] }] },
]};
const readingSchedule = buildMockQuestionSchedule(reading, 'reading', start + 322_000, 578, 12);
assert.equal(readingSchedule.length, 3);
assert.equal(readingSchedule.at(-1).endAt, start + 900_000);
assert.ok(readingSchedule[1].allottedMs > readingSchedule[0].allottedMs, 'the first question in a longer passage receives context-reading time');
assert.match(getMockTransitionLeadIn(null, readingSchedule[0], 3), /Reading section.*Part 5.*Question 1 of 3/s);
assert.match(getMockTransitionLeadIn(readingSchedule[0], readingSchedule[1], 3), /Next reading group.*Part 7.*Question 2 of 3/s);
assert.match(getMockTransitionLeadIn(readingSchedule[1], readingSchedule[2], 3), /Question 3 of 3. Continue with the same passage/s);
console.log('Mock guided flow PASS: time budget coverage, weighted passage/audio slots, automatic focus sequence, stable transition lead-ins and section-wide deadline alignment.');
