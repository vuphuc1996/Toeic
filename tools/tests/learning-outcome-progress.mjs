import assert from 'node:assert/strict';
import { buildObjectiveResourceIndex, ensureObjectiveProgress, recordObjectiveAttempt, summarizeObjectiveProgress, summarizeAllObjectives } from '../../assets/js/learning-outcome-progress.js';

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
assert.equal(summary.status, 'in_progress');

for (let i = 2; i <= 10; i += 1) ledger = recordObjectiveAttempt(ledger, ['grammar-core'], `q${i}`, true, 200 + i);
summary = summarizeObjectiveProgress(ledger, 'grammar-core');
assert.equal(summary.uniqueItems, 10);
assert.equal(summary.accuracyPercent, 90);
assert.equal(summary.evidenceCoveragePercent, 100);
assert.equal(summary.status, 'practice_threshold_met');

const all = summarizeAllObjectives(ledger, map);
assert.equal(all.length, 4);
assert.equal(all[1].status, 'insufficient_evidence');
assert.equal(all[2].status, 'content_review_pending', 'pending independent review must block threshold status');
assert.equal(all[3].status, 'content_review_pending', 'second editorial review must block threshold status');
console.log('PASS: objective index, unique-item denominator, retry history, latest-attempt scoring and threshold gate.');
