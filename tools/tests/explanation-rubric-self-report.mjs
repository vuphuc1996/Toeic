import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { ensureObjectiveProgress, recordObjectiveAttempt, recordExplanationRubric, summarizeObjectiveProgress } from '../../assets/js/learning-outcome-progress.js';

let ledger = ensureObjectiveProgress({ objectives: { 'part5-sentence-completion': { items: { 'p5-sc-001': { latestCorrect: true, latestAnsweredAt: 100, attempts: [{ correct: true, answeredAt: 100, durationMs: 4200 }], recallDueAt: 86400100, recallChecks: [] } } } } });
ledger = recordExplanationRubric(ledger, ['part5-sentence-completion'], 'p5-sc-001', [true, true, false], 200);
let item = ledger.objectives['part5-sentence-completion'].explanationRubrics['p5-sc-001'];
assert.equal(item.latestScore, 2);
assert.deepEqual(item.latestRatings, [true, true, false]);
assert.equal(item.attempts[0].assessmentType, 'learner_self_report');
assert.equal(ledger.objectives['part5-sentence-completion'].items['p5-sc-001'].attempts.length, 1, 'rubric must not mutate answer-attempt history');

ledger = recordExplanationRubric(ledger, ['part5-sentence-completion'], 'p5-sc-001', [true, true, true], 300);
item = ledger.objectives['part5-sentence-completion'].explanationRubrics['p5-sc-001'];
assert.equal(item.attempts.length, 2, 'self-assessment history is retained');
assert.equal(item.latestScore, 3, 'latest self-assessment is the displayed result');
const summary = summarizeObjectiveProgress(ledger, 'part5-sentence-completion');
assert.equal(summary.uniqueItems, 1, 'rubric does not inflate unique question denominator');
assert.equal(summary.totalAttempts, 1, 'rubric does not inflate answer attempts');
assert.equal(summary.explanationRubricItems, 1);
assert.equal(summary.explanationRubricAverage, 3);
assert.equal(summary.explanationRubricAttempts, 2);

const before = JSON.stringify(ledger);
recordExplanationRubric(ledger, ['part5-sentence-completion'], 'bad', [true, 'yes', false], 400);
assert.equal(JSON.stringify(ledger), before, 'invalid ratings are rejected without mutation');
const appSource = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const cssSource = await readFile(new URL('../../assets/css/app.css', import.meta.url), 'utf8');
assert.match(appSource, /data-save-explanation-rubric/, 'Part 5 review UI must expose the save action');
assert.match(appSource, /\['clue','fit','distractor'\]/, 'UI must collect all three explanation criteria');
assert.match(appSource, /recordExplanationRubric\(state\.objectiveProgress/, 'UI action must persist self-report to objective ledger');
assert.match(cssSource, /@media\(max-width:520px\)\{\.explanation-rubric-item/, 'rubric controls must adapt to narrow viewports');
console.log('PASS: Part 5 explanation self-report rubric, UI wiring, responsive controls, retry history, invalid-input guard and denominator isolation.');
