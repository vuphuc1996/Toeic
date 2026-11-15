import assert from 'node:assert/strict';
import { ensureObjectiveProgress, recordObjectiveAttempt, summarizeObjectiveProgress } from '../../assets/js/learning-outcome-progress.js';

const day = 24 * 60 * 60 * 1000;
const t0 = Date.now() - 10 * day;
let ledger = ensureObjectiveProgress({});
ledger = recordObjectiveAttempt(ledger, ['grammar-core'], 'q1', true, t0, 4200);
let item = ledger.objectives['grammar-core'].items.q1;
assert.equal(item.recallDueAt, t0 + day, 'first response schedules first recall after one day');
assert.equal(item.attempts[0].durationMs, 4200, 'response duration is retained');

ledger = recordObjectiveAttempt(ledger, ['grammar-core'], 'q1', false, t0 + 2 * day, 5100);
item = ledger.objectives['grammar-core'].items.q1;
assert.equal(item.recallChecks.length, 1, 'overdue repeat becomes a recall check');
assert.equal(item.recallChecks[0].correct, false);
assert.equal(item.recallDueAt, t0 + 3 * day, 'failed recall schedules retry after one day');

ledger = recordObjectiveAttempt(ledger, ['grammar-core'], 'q1', true, t0 + 4 * day, 3900);
item = ledger.objectives['grammar-core'].items.q1;
assert.equal(item.recallChecks.length, 2);
assert.equal(item.recallChecks[1].correct, true);
assert.equal(item.recallDueAt, t0 + 7 * day, 'successful recall advances to three-day interval');

const summary = summarizeObjectiveProgress(ledger, 'grammar-core', { minimumUniqueItems: 1 });
assert.equal(summary.uniqueItems, 1, 'recall never inflates independent question count');
assert.equal(summary.totalAttempts, 3);
assert.equal(summary.timedAttempts, 3);
assert.equal(summary.averageResponseTimeMs, 4400);
assert.equal(summary.recallChecks, 2);
assert.equal(summary.recallAccuracyPercent, 50);
console.log('PASS: timed evidence, 1/3-day recall scheduling, failed/successful recall intervals and unique-question preservation.');
