import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { recordFoundationAttempt, summarizeFoundationLesson } from '../../assets/js/foundation-evidence.js';

const lessons = JSON.parse(await readFile(new URL('../../data/learning-path/pre-a1-a1.json', import.meta.url), 'utf8'));
assert.equal(lessons.lessons.length, 23);
for (const lesson of lessons.lessons) {
  assert.equal(lesson.questionBank.length, 3, `${lesson.id} must have three independent checks`);
  assert.equal(new Set(lesson.questionBank.map(q => q.id)).size, 3);
  for (const q of lesson.questionBank) {
    assert.equal(q.choices.length, 4);
    assert.ok(q.answerIndex >= 0 && q.answerIndex < 4);
    assert.ok(q.rationale);
  }
}
let progress = { 'pa1-alphabet': { attempted: true, completed: true, attempts: 8, legacyField: 'preserve-me' } };
progress = recordFoundationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::q1', true, 100);
progress = recordFoundationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::q1', false, 200);
let summary = summarizeFoundationLesson(progress, 'pa1-alphabet');
assert.equal(summary.uniqueQuestions, 1, 'retries must not inflate unique evidence');
assert.equal(summary.totalAttempts, 2);
assert.equal(summary.accuracyPercent, 0, 'latest result is the current signal');
assert.equal(summary.status, 'insufficient_evidence');
progress = recordFoundationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::q2', true, 300);
progress = recordFoundationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::q3', true, 400);
summary = summarizeFoundationLesson(progress, 'pa1-alphabet');
assert.equal(summary.uniqueQuestions, 3);
assert.equal(summary.accuracyPercent, 67);
assert.equal(summary.status, 'in_progress');
progress = recordFoundationAttempt(progress, 'pa1-alphabet', 'pa1-alphabet::q1', true, 500);
summary = summarizeFoundationLesson(progress, 'pa1-alphabet');
assert.equal(summary.accuracyPercent, 100);
assert.equal(summary.status, 'practice_threshold_met');
assert.equal(progress['pa1-alphabet'].legacyField, 'preserve-me');
assert.equal(progress['pa1-alphabet'].completed, true, 'legacy fields remain untouched but are not used as new evidence');
const app = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
assert.match(app, /nextProgress=recordFoundationAttempt\(nextProgress/);
const foundationConfirm = app.slice(app.indexOf('function confirmFoundationAssessmentResult('), app.indexOf('function renderLearningObjectiveProgress('));
assert.ok(foundationConfirm.indexOf('localStorage.setItem(storageKey') < foundationConfirm.indexOf('state[progressKey]=nextProgress'), 'Foundation state must change only after durable storage succeeds');
assert.match(app, /summarizeFoundationLesson\(state\.foundationProgress/);
assert.match(app, /data-foundation-question-id/);
console.log('PASS: foundation question bank integrity, stable unique evidence, retry handling, threshold gating and legacy preservation.');
