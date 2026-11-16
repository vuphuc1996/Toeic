import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import {
  recordFoundationProductionAttempt,
  recordFoundationProductionRevision,
  summarizeFoundationProduction,
  summarizeFoundationProductionPortfolio
} from '../../assets/js/foundation-evidence.js';

const root = new URL('../../', import.meta.url);
const curriculum = JSON.parse(await readFile(new URL('data/learning-path/pre-a1-a1.json', root), 'utf8'));
const lessons = curriculum.lessons.filter(lesson => lesson.level === 'A2');
assert.equal(lessons.length, 13);
for (const lesson of lessons) {
  const task = lesson.productionTask;
  assert.equal(task.revisionChecklist?.length, 3, `${lesson.id}: exactly three task-specific revision checks`);
  assert.ok(task.revisionChecklist.every(item => item.trim().length >= 12), `${lesson.id}: revision checks must be useful prompts`);
  assert.ok(task.revisionHint?.length >= 50, `${lesson.id}: add a topic-specific revision hint`);
}

const lesson = lessons[0];
const taskId = lesson.productionTask.id;
const first = 'Could you please send the meeting notes before three p.m.? Thank you for your help.';
const revised = 'Could you please send me the updated meeting notes before 3 p.m.? Thank you for your help.';
const revisedAgain = 'Could you please send me the updated meeting notes before 3 p.m. today? Thank you for your help.';
const legacyTaskId = lesson.applicationTask.id;
let progress = {};
progress = recordFoundationProductionAttempt(progress, lesson.id, legacyTaskId,
  'Legacy response from earlier production task.', [true, false, true], 1000, 3);
const legacySnapshot = structuredClone(progress[lesson.id].productionEvidence[legacyTaskId]);
progress = recordFoundationProductionAttempt(progress, lesson.id, taskId, first,
  [true, true, false], 2000, 8);
let saved = progress[lesson.id].productionEvidence[taskId];
assert.equal(saved.initialResponse, first);
assert.equal(saved.attempts[0].response, first, 'new first attempts retain the exact response');
assert.equal(saved.revisionCount || 0, 0);
assert.deepEqual(progress[lesson.id].productionEvidence[legacyTaskId], legacySnapshot,
  'legacy ::apply1 progress is preserved');

const noChange = recordFoundationProductionRevision(progress, lesson.id, taskId, first,
  [true, true, true], [true, true, true], 3000, 8);
assert.equal(noChange, progress, 'identical revision must be rejected');
const noReview = recordFoundationProductionRevision(progress, lesson.id, taskId, revised,
  [true, true, true], [true, false, true], 3000, 8);
assert.equal(noReview, progress, 'revision without all review confirmations must be rejected');
const tooShort = recordFoundationProductionRevision(progress, lesson.id, taskId, 'Too short to pass',
  [true, true, true], [true, true, true], 3000, 8);
assert.equal(tooShort, progress, 'revision below the task word minimum must be rejected');

progress = recordFoundationProductionRevision(progress, lesson.id, taskId, revised,
  [true, true, true], [true, true, true], 4000, 8);
saved = progress[lesson.id].productionEvidence[taskId];
assert.equal(saved.initialResponse, first);
assert.equal(saved.lastRevisionSource, first);
assert.equal(saved.latestResponse, revised);
assert.equal(saved.revisionCount, 1);
assert.equal(saved.latestAssessmentType, 'guided_revision');
assert.equal(saved.attempts.length, 2);
assert.equal(saved.attempts[1].response, revised);
assert.equal(saved.attempts[1].basedOnResponse, first);
assert.deepEqual(saved.attempts[1].reviewChecks, [true, true, true]);

progress = recordFoundationProductionRevision(progress, lesson.id, taskId, revisedAgain,
  [true, false, true], [true, true, true], 5000, 8);
saved = progress[lesson.id].productionEvidence[taskId];
assert.equal(saved.revisionCount, 2);
assert.equal(saved.lastRevisionSource, revised);
assert.equal(saved.attempts.length, 3);
assert.equal(saved.attempts[2].basedOnResponse, revised);
assert.deepEqual(progress[lesson.id].productionEvidence[legacyTaskId], legacySnapshot);
assert.equal(summarizeFoundationProduction(progress, [lesson]).uniqueItems, 1);
assert.equal(summarizeFoundationProduction(progress, [lesson]).totalAttempts, 3, 'legacy application attempts must not be mixed into the new production task');


// A2 Final Review portfolio: compare learner self-ratings across revisions only.
let portfolioProgress = {};
const task1 = lessons[0], task2 = lessons[1], task3 = lessons[2];
portfolioProgress = recordFoundationProductionAttempt(portfolioProgress, task1.id, task1.productionTask.id,
  'Please confirm the meeting room before the client arrives tomorrow.', [true, false, false], 6000, 8);
portfolioProgress = recordFoundationProductionRevision(portfolioProgress, task1.id, task1.productionTask.id,
  'Please confirm the meeting room before the client arrives tomorrow morning.', [true, true, true], [true, true, true], 7000, 8);
portfolioProgress = recordFoundationProductionAttempt(portfolioProgress, task2.id, task2.productionTask.id,
  'The report has been prepared for the department manager today.', [true, true, true], 8000, 8);
portfolioProgress = recordFoundationProductionRevision(portfolioProgress, task2.id, task2.productionTask.id,
  'The report was prepared for the department manager earlier today.', [true, false, false], [true, true, true], 9000, 8);
portfolioProgress = recordFoundationProductionAttempt(portfolioProgress, task3.id, task3.productionTask.id,
  'The technician will inspect the new equipment after lunch.', [true, true, false], 10000, 8);
// An unrelated legacy application ID must not be included in the A2 writing portfolio.
portfolioProgress = recordFoundationProductionAttempt(portfolioProgress, task1.id, task1.applicationTask.id,
  'Legacy practice remains separate from the portfolio record.', [true, true, true], 11000, 3);
const emptyPortfolio = summarizeFoundationProductionPortfolio({}, lessons, { level: 'A2' });
assert.equal(emptyPortfolio.totalTasks, 13);
assert.equal(emptyPortfolio.startedTasks, 0);
const portfolio = summarizeFoundationProductionPortfolio(portfolioProgress, lessons, { level: 'A2' });
assert.equal(portfolio.totalTasks, 13);
assert.equal(portfolio.startedTasks, 3);
assert.equal(portfolio.revisedTasks, 2);
assert.equal(portfolio.totalAttempts, 5);
assert.equal(portfolio.selfReportedImproved, 1);
assert.equal(portfolio.selfReportedUnchanged, 0);
assert.equal(portfolio.selfReportedReduced, 1);
const task1Portfolio = portfolio.records.find(item => item.lessonId === task1.id);
assert.equal(task1Portfolio.initialScore, 1);
assert.equal(task1Portfolio.latestScore, 3);
assert.deepEqual(task1Portfolio.latestRatings, [true, true, true]);
assert.equal(task1Portfolio.rubric.length, 3, 'Portfolio detail must preserve each lesson’s own rubric wording.');
assert.equal(portfolio.selfReportOnly, true);
assert.equal(portfolio.objectiveGrading, false);
assert.ok(portfolio.records.every(item => !Object.hasOwn(item, 'latestResponse')), 'Portfolio rows must not expose or duplicate saved response text.');

const app = await readFile(new URL('assets/js/app.js', root), 'utf8');
const evidence = await readFile(new URL('assets/js/foundation-evidence.js', root), 'utf8');
const css = await readFile(new URL('assets/css/app.css', root), 'utf8');
assert.match(app, /data-foundation-production-revision-save/);
assert.match(app, /data-foundation-revision-text/);
assert.match(app, /data-foundation-revision-check/);
assert.match(app, /recordFoundationProductionRevision\(/);
assert.match(app, /summarizeFoundationProductionPortfolio/);
assert.match(app, /Nhật ký viết A2/);
assert.match(app, /Bản trước để đối chiếu/);
assert.match(app, /Gợi ý sửa theo chủ điểm/);
assert.match(evidence, /assessmentType: 'guided_revision'/);
assert.match(evidence, /basedOnResponse: previousResponse/);
assert.match(css, /foundation-revision-workspace/);
assert.match(css, /foundation-revision-check/);
console.log('PASS: 13 task-specific revision guides, first/revised response history, review gates, distinct revisions, additive legacy preservation, and no automated grading.');
