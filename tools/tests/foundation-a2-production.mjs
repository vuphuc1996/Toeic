import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import {
  recordFoundationProductionAttempt,
  summarizeFoundationProduction,
  summarizeFoundationOutcomeProgress
} from '../../assets/js/foundation-evidence.js';

const root = new URL('../../', import.meta.url);
const curriculum = JSON.parse(await readFile(new URL('data/learning-path/pre-a1-a1.json', root), 'utf8'));
const lessons = curriculum.lessons.filter(lesson => lesson.level === 'A2');
assert.equal(lessons.length, 13, 'all A2 lessons must have their own production prompt');
const politeRequestLesson = lessons.find(lesson => lesson.id === 'a2-polite-requests');
assert.match(politeRequestLesson.productionTask.scenario, /Bạn cần đồng nghiệp gửi biên bản cuộc họp/,
  'scenario direction must match the instruction asking the colleague to send the notes');
const ids = new Set();
for (const lesson of lessons) {
  const task = lesson.productionTask;
  assert.ok(task, `${lesson.id} must define productionTask`);
  assert.equal(task.id, `${lesson.id}::produce1`);
  assert.notEqual(task.id, lesson.applicationTask.id, 'new production evidence must not overwrite legacy application-keyed evidence');
  assert.ok(!ids.has(task.id), `duplicate production ID ${task.id}`);
  ids.add(task.id);
  assert.equal(task.minimumWords, 8);
  assert.ok(task.scenario?.length >= 30);
  assert.ok(task.instruction?.length >= 30);
  assert.equal(task.requirements?.length, 3);
  assert.equal(task.rubric?.length, 3);
  assert.ok(task.sentenceFrame?.length > 10);
  assert.ok(task.modelAnswer?.length > 20);
  assert.ok(task.requiredFeatures?.length >= 2);
  const model = task.modelAnswer.toLowerCase();
  for (const feature of task.requiredFeatures) assert.ok(model.includes(feature), `${lesson.id}: model answer missing ${feature}`);
  assert.ok(task.modelAnswer.trim().split(/\s+/).length >= task.minimumWords);
  assert.equal(task.evidenceType, 'learner-authored-contextual-production');
  assert.ok(task.minimumWords >= 8 && task.minimumWords <= 60, `${lesson.id}: word minimum must be practical and within local evidence limits`);
  assert.equal(task.requirements?.length, 3, `${lesson.id}: three explicit task requirements are required`);
  assert.equal(task.rubric?.length, 3, `${lesson.id}: three self-review criteria are required`);
  assert.equal(task.revisionChecklist?.length, 3, `${lesson.id}: three guided revision checks are required`);
  const modelAnswer = String(task.modelAnswer || '').toLowerCase();
  for (const feature of task.requiredFeatures || []) {
    assert.ok(modelAnswer.includes(String(feature).toLowerCase()), `${lesson.id}: model answer must demonstrate ${feature}`);
  }
  assert.ok(task.modelAnswer.trim().split(/\s+/).length >= task.minimumWords, `${lesson.id}: model answer must meet the word minimum`);
}

const target = lessons[0];
const applicationId = target.applicationTask.id;
const productionId = target.productionTask.id;
const response = 'Could you please send the updated meeting notes before three o clock today?';
assert.ok(response.split(/\s+/).length >= 8);
let progress = {};
progress = recordFoundationProductionAttempt(progress, target.id, applicationId,
  'Legacy sentence kept from the previous release.', [true, false, true], 1000, 3);
const legacySaved = progress[target.id].productionEvidence[applicationId];
const rejected = recordFoundationProductionAttempt(progress, target.id, productionId,
  'This is seven words only', [true, true, true], 2000, 8);
assert.equal(rejected, progress, 'responses below the A2 word floor must not be recorded');
progress = recordFoundationProductionAttempt(progress, target.id, productionId,
  response, [true, true, false], 3000, 8);
assert.deepEqual(progress[target.id].productionEvidence[applicationId], legacySaved,
  'the old production record must remain byte-for-byte equivalent in memory');
assert.equal(progress[target.id].productionEvidence[productionId].latestWordCount, response.split(/\s+/).length);
assert.equal(progress[target.id].productionEvidence[productionId].minimumWords, 8);
assert.equal(summarizeFoundationProduction(progress, [target]).uniqueItems, 1);
assert.equal(summarizeFoundationProduction(progress, [target]).scorePercent, 67);

const outcomeRegistry = { objectives: [{
  objectiveId: 'foundation-a2',
  outcomes: [{ id: 'foundation-a2-production', title: 'Production', evidenceMetric: 'self_report', minimumUniqueItems: 1, masteryThreshold: 0.8 }]
}] };
const outcome = summarizeFoundationOutcomeProgress(progress, [target], outcomeRegistry)[0];
assert.equal(outcome.uniqueItems, 1);
assert.equal(outcome.accuracyPercent, 67);
assert.equal(outcome.selfReportOnly, true);

const app = await readFile(new URL('assets/js/app.js', root), 'utf8');
const evidence = await readFile(new URL('assets/js/foundation-evidence.js', root), 'utf8');
const css = await readFile(new URL('assets/css/app.css', root), 'utf8');
assert.match(app, /function renderFoundationProductionSection\(/);
assert.match(app, /data-foundation-production-count/);
assert.match(app, /<details class="foundation-production-model"/);
assert.match(app, /lesson\.productionTask\?\.id\|\|lesson\.applicationTask\.id/);
assert.match(app, /Date\.now\(\),minimumWords/);
assert.match(evidence, /Math\.max\(3, Math\.min\(60, Number\(minimumWords\) \|\| 3\)\)/);
assert.match(evidence, /lesson\.productionTask\?\.id \|\| lesson\.applicationTask\?\.id/);
assert.match(css, /foundation-production-context/);
assert.match(css, /foundation-production-word-count/);
console.log('PASS: 13 contextual A2 production tasks, hidden model answers, tailored self-check rubrics, minimum word gate, and legacy evidence preservation.');
