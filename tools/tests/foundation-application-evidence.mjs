import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { recordFoundationAttempt, summarizeFoundationLesson, recordFoundationApplicationAttempt, summarizeFoundationApplication } from '../../assets/js/foundation-evidence.js';

const data = JSON.parse(await readFile(new URL('../../data/learning-path/pre-a1-a1.json', import.meta.url), 'utf8'));
assert.equal(data.lessons.length, 10);
const ids = [];
for (const lesson of data.lessons) {
  const task = lesson.applicationTask;
  assert.ok(task, `${lesson.id} needs a contextual task`);
  assert.equal(task.id, `${lesson.id}::apply1`);
  assert.equal(task.choices.length, 4);
  assert.ok(task.answerIndex >= 0 && task.answerIndex < 4);
  assert.ok(task.prompt && task.rationale && task.focus);
  ids.push(task.id);
}
assert.equal(new Set(ids).size, 10);
let progress = {};
progress = recordFoundationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::q1', true, 10);
progress = recordFoundationApplicationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::apply1', false, 20);
progress = recordFoundationApplicationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::apply1', true, 30);
assert.equal(summarizeFoundationLesson(progress, 'pa1-alphabet').uniqueQuestions, 1, 'application evidence must not inflate recognition denominator');
const summary = summarizeFoundationApplication(progress, 'pa1-alphabet');
assert.equal(summary.uniqueTasks, 1);
assert.equal(summary.totalAttempts, 2);
assert.equal(summary.accuracyPercent, 100, 'latest application result is the current signal');
assert.equal(summary.status, 'application_check_passed');
const app = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
assert.match(app, /recordFoundationApplicationAttempt/);
assert.match(app, /data-foundation-application-answer/);
assert.match(app, /function answerFoundationApplication\(/);
console.log('PASS: 10 stable contextual application tasks, isolated evidence ledger, retry handling and UI wiring.');
