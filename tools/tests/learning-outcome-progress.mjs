import assert from 'node:assert/strict';
import { buildObjectiveResourceIndex, ensureObjectiveProgress, recordObjectiveAttempt, recordExplanationRubric, listDueRecallItems, summarizeObjectiveProgress, summarizeAllObjectives, auditObjectiveProgress } from '../../assets/js/learning-outcome-progress.js';

const map = { objectives: [
  { id: 'grammar-core', title: 'Grammar', kind: 'grammar', resourceIds: ['lesson-a', 'lesson-b'] },
  { id: 'listening-part-2', title: 'Listening P2', kind: 'listening', part: 'Part 2', resourceIds: ['audio-a'] },
  { id: 'part5-sentence-completion', title: 'Part 5 reserve', kind: 'practice', resourceIds: ['p5-reserve'], reviewState: 'pending_independent_review_practice_only_not_mock_eligible' },
  { id: 'reading-part-7', title: 'Reading P7', kind: 'reading', part: 'Part 7', resourceIds: ['reading-p7'], reviewState: 'part7_expansion_requires_second_review' }
] };
const index = buildObjectiveResourceIndex(map);
assert.deepEqual(index['lesson-a'], ['grammar-core']);
assert.deepEqual(index['audio-a'], ['listening-part-2']);
assert.equal(index.unknown, undefined);

let ledger = ensureObjectiveProgress(null);
ledger = recordObjectiveAttempt(ledger, index['lesson-a'], 'q1', true, 100);
ledger = recordObjectiveAttempt(ledger, index['lesson-a'], 'q1', false, 200);
let summary = summarizeObjectiveProgress(ledger, 'grammar-core', { minimumUniqueItems: 1, defaultThreshold: 0.8 });
assert.equal(summary.uniqueItems, 1, 'retry must not inflate unique item count');
assert.equal(summary.totalAttempts, 2, 'retry history must be retained');
assert.equal(summary.accuracy, 0, 'latest attempt is the current evidence');
assert.equal(summary.firstAttemptItems, 1);
assert.equal(summary.firstAttemptCorrect, 1);
assert.equal(summary.firstAttemptAccuracyPercent, 100, 'first attempt remains correct even when a later retry is wrong');
assert.equal(summary.status, 'in_progress');

for (let i = 2; i <= 10; i += 1) ledger = recordObjectiveAttempt(ledger, ['grammar-core'], `q${i}`, true, 200 + i);
summary = summarizeObjectiveProgress(ledger, 'grammar-core');
assert.equal(summary.uniqueItems, 10);
assert.equal(summary.accuracyPercent, 90);
assert.equal(summary.firstAttemptItems, 10);
assert.equal(summary.firstAttemptAccuracyPercent, 100, 'the initial correct answer remains distinct from the later wrong retry');
assert.notEqual(summary.firstAttemptAccuracyPercent, summary.accuracyPercent);
assert.equal(summary.evidenceCoveragePercent, 100);
assert.equal(summary.status, 'practice_threshold_met');

const all = summarizeAllObjectives(ledger, map);
assert.equal(all.length, 4);
assert.equal(all[1].status, 'insufficient_evidence');
assert.equal(all[2].status, 'content_review_pending', 'pending independent review must block threshold status');
assert.equal(all[3].status, 'content_review_pending', 'second editorial review must block threshold status');
console.log('PASS: objective index, unique-item denominator, retry history, latest-attempt scoring and threshold gate.');

let mixedLedger = recordObjectiveAttempt({}, ['grammar-core'], 'mixed-q1', false, 10);
mixedLedger = recordObjectiveAttempt(mixedLedger, ['grammar-core'], 'mixed-q1', true, 20);
const mixedSummary = summarizeObjectiveProgress(mixedLedger, 'grammar-core', { minimumUniqueItems: 1 }, 20);
assert.equal(mixedSummary.accuracyPercent, 100, 'latest-attempt metric reflects the successful retry');
assert.equal(mixedSummary.firstAttemptAccuracyPercent, 0, 'first-attempt metric preserves initial performance');
assert.equal(mixedSummary.totalAttempts, 2);
console.log('PASS: first-attempt and latest-attempt accuracy remain separate and can diverge.');

// Deterministic delayed-recall reporting: callers can evaluate due evidence at
// a supplied clock instant without depending on the host wall clock.
const recallNow = 10_000;
let recallLedger = recordObjectiveAttempt({}, ['grammar-core'], 'recall-q1', true, recallNow);
const recallDueAt = recallLedger.objectives['grammar-core'].items['recall-q1'].recallDueAt;
assert.equal(recallDueAt, recallNow + 24 * 60 * 60 * 1000);
assert.equal(summarizeObjectiveProgress(recallLedger, 'grammar-core', {}, recallDueAt - 1).dueRecallItems, 0);
assert.equal(summarizeObjectiveProgress(recallLedger, 'grammar-core', {}, recallDueAt).dueRecallItems, 1);
assert.equal(summarizeAllObjectives(recallLedger, { objectives: [{ id: 'grammar-core', title: 'Grammar' }] }, {}, recallDueAt)[0].dueRecallItems, 1);
assert.equal(summarizeObjectiveProgress(recallLedger, 'grammar-core', {}, Number.NaN).dueRecallItems >= 0, true, 'invalid injected time falls back safely to the wall clock');
console.log('PASS: delayed-recall due counts use an injectable deterministic evaluation clock.');

// Read-only summaries and due-recall queries must not initialize missing ledgers,
// append defaults, or mutate nested learner history.
const frozenReadOnlyLedger = Object.freeze({
  schemaVersion: 1,
  objectives: Object.freeze({
    'grammar-core': Object.freeze({
      items: Object.freeze({
        'frozen-q1': Object.freeze({
          latestCorrect: true,
          latestAnsweredAt: 10,
          attempts: Object.freeze([Object.freeze({ correct: true, answeredAt: 10 })]),
          recallDueAt: 20,
          recallChecks: Object.freeze([])
        })
      })
    })
  })
});
const frozenSnapshot = JSON.stringify(frozenReadOnlyLedger);
assert.equal(summarizeObjectiveProgress(frozenReadOnlyLedger, 'grammar-core', {}, 20).dueRecallItems, 1);
assert.equal(summarizeAllObjectives(frozenReadOnlyLedger, map, {}, 20)[0].uniqueItems, 1);
assert.equal(listDueRecallItems(frozenReadOnlyLedger, map, 20).length, 1);
assert.equal(JSON.stringify(frozenReadOnlyLedger), frozenSnapshot, 'all read-only queries must preserve frozen learner history');
const absentLedger = {};
assert.equal(summarizeObjectiveProgress(absentLedger, 'grammar-core').uniqueItems, 0);
assert.equal(summarizeAllObjectives(absentLedger, map).length, map.objectives.length);
assert.deepEqual(listDueRecallItems(absentLedger, map), []);
assert.deepEqual(absentLedger, {}, 'read-only calls must not create schemaVersion or objectives');
assert.equal(summarizeObjectiveProgress(null, 'grammar-core').uniqueItems, 0);
assert.deepEqual(listDueRecallItems(null, map), []);
console.log('PASS: summaries and due-recall queries are strictly non-mutating, including frozen or absent ledgers.');


// Read-only ledger integrity audit: valid data passes, malformed/orphaned data
// is reported precisely, and the original learner record remains unchanged.
const cleanLedger = recordObjectiveAttempt({}, ['grammar-core'], 'audit-q1', true, 1234, 250);
const cleanSnapshot = JSON.stringify(cleanLedger);
const cleanAudit = auditObjectiveProgress(cleanLedger, map);
assert.equal(cleanAudit.valid, true);
assert.equal(cleanAudit.itemCount, 1);
assert.equal(cleanAudit.attemptCount, 1);
assert.equal(JSON.stringify(cleanLedger), cleanSnapshot, 'audit must not mutate learner progress');
const damagedLedger = JSON.parse(cleanSnapshot);
damagedLedger.objectives['grammar-core'].items['audit-q1'].attempts[0].durationMs = -1;
damagedLedger.objectives['grammar-core'].items['audit-q1'].recallDueAt = 'tomorrow';
damagedLedger.objectives['removed-objective'] = { items: {} };
const damagedAudit = auditObjectiveProgress(damagedLedger, map);
assert.equal(damagedAudit.valid, true, 'non-critical warnings must not invalidate otherwise readable history');
assert.ok(damagedAudit.issues.some(issue => issue.code === 'invalid_attempt_duration'));
assert.ok(damagedAudit.issues.some(issue => issue.code === 'invalid_recall_due_at'));
assert.ok(damagedAudit.issues.some(issue => issue.code === 'orphan_objective'));
const invalidLedger = { schemaVersion: 0, objectives: { 'grammar-core': { items: { broken: { latestCorrect: 'yes', latestAnsweredAt: -1, attempts: [{}] } } } } };
const invalidAudit = auditObjectiveProgress(invalidLedger, map);
assert.equal(invalidAudit.valid, false);
assert.ok(invalidAudit.errorCount >= 3);
assert.equal(auditObjectiveProgress(null, map).valid, false);
console.log('PASS: read-only objective evidence integrity audit, warning/error classification and non-mutation guarantee.');


// Defensive boundary handling: malformed optional branches must not crash
// dashboards, and invalid write timestamps must not create evidence records.
assert.deepEqual(buildObjectiveResourceIndex(null), {});
assert.deepEqual(buildObjectiveResourceIndex({ objectives: [null, {}, { id: 'ok', resourceIds: ['x', '', null, 'x'] }] }), { x: ['ok'] });
const malformedReadLedger = {
  objectives: {
    'grammar-core': {
      items: {
        nullItem: null,
        badAttempts: { latestCorrect: true, latestAnsweredAt: 5, attempts: 'not-an-array', recallChecks: 'bad' },
        goodItem: { latestCorrect: false, latestAnsweredAt: 6, attempts: [{ correct: false, answeredAt: 6, durationMs: 30 }], recallDueAt: 1, recallChecks: [{ correct: true, answeredAt: 2, dueAt: 1 }] }
      },
      explanationRubrics: ['malformed-array']
    },
    'orphan-objective': null
  }
};
assert.doesNotThrow(() => summarizeObjectiveProgress(malformedReadLedger, 'grammar-core', {}, 10));
assert.doesNotThrow(() => summarizeAllObjectives(malformedReadLedger, { objectives: [null, { id: 'grammar-core' }] }, {}, 10));
assert.doesNotThrow(() => listDueRecallItems(malformedReadLedger, { objectives: [null, { id: 'grammar-core' }] }, 10));
assert.doesNotThrow(() => auditObjectiveProgress(malformedReadLedger, null));
const malformedSummary = summarizeObjectiveProgress(malformedReadLedger, 'grammar-core', {}, 10);
assert.equal(malformedSummary.uniqueItems, 2, 'malformed non-object item records are excluded from safe summaries');
assert.equal(malformedSummary.totalAttempts, 1, 'malformed attempts containers are ignored by summaries');
assert.equal(listDueRecallItems(malformedReadLedger, { objectives: [{ id: 'grammar-core' }] }, 10).length, 1);
const guardedWrite = recordObjectiveAttempt({}, ['grammar-core', '', null, 'grammar-core'], 'invalid-time-q', true, Number.NaN);
assert.deepEqual(guardedWrite.objectives, {}, 'non-finite timestamps must not create evidence items');
const guardedRubric = recordExplanationRubric({}, ['grammar-core'], 'invalid-rubric-q', [true, false, true], -1);
assert.deepEqual(guardedRubric.objectives, {}, 'negative rubric timestamps must not create evidence items');
const duplicateSafeWrite = recordObjectiveAttempt({}, ['grammar-core', 'grammar-core', ''], 'dedup-q', true, 100);
assert.deepEqual(Object.keys(duplicateSafeWrite.objectives), ['grammar-core']);
assert.equal(duplicateSafeWrite.objectives['grammar-core'].items['dedup-q'].attempts.length, 1);
const validRubricLedger = recordExplanationRubric({}, ['grammar-core', 'grammar-core'], 'rubric-q', [true, false, true], 200);
assert.equal(validRubricLedger.objectives['grammar-core'].explanationRubrics['rubric-q'].latestScore, 2);
assert.equal(validRubricLedger.objectives['grammar-core'].explanationRubrics['rubric-q'].attempts.length, 1);
assert.equal(auditObjectiveProgress(validRubricLedger, map).valid, true, 'valid rubric-only evidence must satisfy the ledger shape');
assert.equal(summarizeObjectiveProgress(validRubricLedger, 'grammar-core').explanationRubricItems, 1);
const mismatchLedger = recordObjectiveAttempt({}, ['grammar-core'], 'mismatch-q', true, 100);
mismatchLedger.objectives['grammar-core'].items['mismatch-q'].latestCorrect = false;
const mismatchAudit = auditObjectiveProgress(mismatchLedger, map);
assert.ok(mismatchAudit.issues.some(issue => issue.code === 'latest_attempt_mismatch' && issue.severity === 'warning'));
console.log('PASS: malformed ledger branches are safely read, invalid write timestamps are rejected, and duplicate objective IDs are deduplicated.');
