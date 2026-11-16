import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import {
  recordFoundationAttempt,
  recordFoundationRecallAttempt,
  listDueFoundationRecallItems,
  summarizeFoundationRetention,
  recordFoundationProductionAttempt,
  summarizeFoundationProduction,
  summarizeFoundationOutcomeProgress
} from '../../assets/js/foundation-evidence.js';

const root = new URL('../../', import.meta.url);
const data = JSON.parse(await readFile(new URL('data/learning-path/pre-a1-a1.json', root), 'utf8'));
const outcomes = JSON.parse(await readFile(new URL('data/learning-path/objective-outcomes.json', root), 'utf8'));
const app = await readFile(new URL('assets/js/app.js', root), 'utf8');
const html = await readFile(new URL('index.html', root), 'utf8');
const sw = await readFile(new URL('sw.js', root), 'utf8');
const lessons = data.lessons;
const a2 = lessons.filter(lesson => lesson.level === 'A2');
const preA1A1 = lessons.filter(lesson => ['PRE-A1', 'A1'].includes(lesson.level));
assert.equal(a2.length, 13, 'A2 outcome aggregation includes all thirteen lessons');
assert.equal(preA1A1.length, 10);

const DAY = 24 * 60 * 60 * 1000;
const start = 1_800_000_000_000;
let progress = { 'legacy-lesson': { completed: true, oldField: 'keep' } };
const firstLesson = a2[0];
const firstQuestion = firstLesson.questionBank[0];
progress = recordFoundationAttempt(progress, firstLesson.id, firstQuestion.id, true, start);
assert.equal(progress[firstLesson.id].evidence[firstQuestion.id].recallDueAt, start + DAY, 'first practice schedules delayed recall in 24 hours');
assert.equal(listDueFoundationRecallItems(progress, lessons, start + DAY - 1).length, 0, 'recall cannot be due early');
let unchanged = recordFoundationRecallAttempt(progress, firstLesson.id, firstQuestion.id, true, start + DAY - 1);
assert.equal(unchanged, progress, 'early recall attempts are rejected without mutating evidence');
assert.equal(listDueFoundationRecallItems(progress, lessons, start + DAY).length, 1);
progress = recordFoundationRecallAttempt(progress, firstLesson.id, firstQuestion.id, true, start + DAY);
assert.equal(progress[firstLesson.id].evidence[firstQuestion.id].recallChecks.length, 1);
assert.equal(progress[firstLesson.id].evidence[firstQuestion.id].recallDueAt, start + DAY + 3 * DAY, 'correct recall schedules the next check in three days');
progress = recordFoundationRecallAttempt(progress, firstLesson.id, firstQuestion.id, false, start + DAY + 3 * DAY);
assert.equal(progress[firstLesson.id].evidence[firstQuestion.id].recallChecks.length, 2);
assert.equal(progress[firstLesson.id].evidence[firstQuestion.id].recallDueAt, start + DAY + 4 * DAY, 'incorrect recall reschedules in one day');
assert.equal(progress[firstLesson.id].evidence[firstQuestion.id].attempts.length, 1, 'recall must not inflate recognition attempts');
assert.equal(progress['legacy-lesson']?.oldField, 'keep');

// Complete A2 and Pre-A1/A1 outcome ledgers independently with synthetic data.
for (const lessonGroup of [preA1A1, a2]) {
  for (const lesson of lessonGroup) {
    for (const [index, question] of lesson.questionBank.entries()) {
      progress = recordFoundationAttempt(progress, lesson.id, question.id, true, start);
      progress = recordFoundationRecallAttempt(progress, lesson.id, question.id, true, start + 10 * DAY);
    }
    const taskId = lesson.productionTask?.id || lesson.applicationTask.id;
    const minimumWords = lesson.productionTask?.minimumWords || 3;
    progress = recordFoundationProductionAttempt(progress, lesson.id, taskId,
      'I would like to confirm the meeting schedule today.', [true, true, true], start + 2 * DAY, minimumWords);
  }
}
const rows = summarizeFoundationOutcomeProgress(progress, lessons, outcomes, start + 11 * DAY);
assert.equal(rows.length, 6, 'both Foundation tracks expose recognition, production and retention outcomes');
for (const objectiveId of ['foundation-pre-a1-a1', 'foundation-a2']) {
  const group = rows.filter(row => row.objectiveId === objectiveId);
  const expectedLessonCount = objectiveId === 'foundation-a2' ? 13 : 10;
  const expectedQuestionCount = expectedLessonCount * 3;
  assert.deepEqual(group.map(row => row.kind).sort(), ['production', 'recognition', 'retention']);
  assert.equal(group.find(row => row.kind === 'recognition').uniqueItems, expectedQuestionCount);
  assert.equal(group.find(row => row.kind === 'retention').uniqueItems, expectedQuestionCount);
  assert.equal(group.find(row => row.kind === 'production').uniqueItems, expectedLessonCount);
  assert.ok(group.every(row => row.accuracyPercent === 100));
}
const a2Production = rows.find(row => row.objectiveId === 'foundation-a2' && row.kind === 'production');
assert.equal(a2Production.uniqueItems, 13);
assert.equal(a2Production.selfReportOnly, true, 'production is explicitly learner self-report');
assert.equal(summarizeFoundationProduction(progress, a2).scorePercent, 100);
const retention = summarizeFoundationRetention(progress, a2, { now: start + 11 * DAY });
assert.equal(retention.uniqueItems, 39, 'A2 delayed recall includes all thirteen three-question lessons');
assert.equal(retention.accuracyPercent, 100);

// Self-production accepts only complete three-point rubrics and preserves the latest learner sentence locally.
const saved = progress[a2[0].id].productionEvidence[a2[0].productionTask.id];
assert.equal(saved.latestResponse, 'I would like to confirm the meeting schedule today.');
assert.equal(saved.latestWordCount, 9);
const rejected = recordFoundationProductionAttempt(progress, a2[0].id, a2[0].productionTask.id, 'Too short', [true, true, true], start + 3 * DAY, 8);
assert.equal(rejected, progress, 'short fragments are not counted as production evidence');

assert.match(app, /recordFoundationRecallAttempt/);
assert.match(app, /listDueFoundationRecallItems/);
assert.match(app, /recordFoundationProductionAttempt/);
assert.match(app, /data-foundation-recall-answer/);
assert.match(app, /data-foundation-production-save/);
assert.match(html, /foundationOutcomeDashboard/);
assert.match(sw, /objective-outcomes\.json/);
console.log('PASS: Foundation recognition, 1/3-day delayed recall, learner production self-report, separate Pre-A1/A1 and A2 outcome aggregation, UI and offline-shell wiring.');
