import assert from 'node:assert/strict';
import { buildMockScoreReadiness } from '../../assets/js/mock-score-readiness.js';
const ids = (prefix, count = 100) => Array.from({length:count},(_,i)=>`listening:${prefix}-${i+1}:1`);
const row=(completedAt, listeningAccuracy, readingAccuracy, questionIds = ids('form-a'), extra={})=>({status:'completed',modeId:'full',questions:200,completedAt,listeningAccuracy,readingAccuracy,questionIds:[...questionIds,...Array.from({length:100},(_,i)=>`reading:r-${i+1}:1`)],...extra});
assert.equal(buildMockScoreReadiness([]).enough,false);
assert.equal(buildMockScoreReadiness([row(1,80,70)]).count,1);
assert.equal(buildMockScoreReadiness([row(1,80,70),row(2,82,72)]).enough,false);
const repeated = buildMockScoreReadiness([row(1,70,60),row(2,75,65),row(3,80,75)]);
assert.equal(repeated.enough,true);
assert.equal(repeated.count,3);
assert.equal(repeated.readingAverage,67);
assert.equal(repeated.readingChange,15);
assert.equal(repeated.listeningTrendEnough,false,'three attempts on the same listening form must not unlock its trend');
assert.equal(repeated.listeningChange,null);
assert.match(repeated.listeningWarning,/hai bộ câu hỏi Listening khác nhau/);
const first = ids('form-a');
const second = [...first.slice(0,98), ...ids('form-b',2)];
const diverse = buildMockScoreReadiness([row(1,70,60,first),row(2,75,65,second),row(3,80,75,second)]);
assert.equal(diverse.listeningTrendEnough,true);
assert.equal(diverse.listeningDistinctForms,2);
assert.equal(diverse.listeningDistinctQuestionCount,102);
assert.equal(diverse.listeningOverlapPercent,98);
assert.equal(diverse.listeningChange,10);
assert.equal(diverse.listeningAverage,75,'Listening average uses one latest attempt per distinct form, not repeated attempts');
assert.match(diverse.listeningWarning,/trùng 98%/);
const legacy = buildMockScoreReadiness([row(1,70,60,[]),row(2,75,65,[]),row(3,80,75,[])]);
assert.equal(legacy.listeningTrendEnough,false,'legacy history without question IDs must fail closed');
const legacyThenDistinct = buildMockScoreReadiness([row(1,99,60,[]),row(2,70,65,first),row(3,80,75,second)]);
assert.equal(legacyThenDistinct.listeningTrendEnough,true);
assert.equal(legacyThenDistinct.listeningAverage,75,'legacy attempts without IDs must not contribute to Listening trend metrics');
assert.equal(legacyThenDistinct.listeningChange,10);
const distinctReadingOnly = buildMockScoreReadiness([row(1,70,60,first),row(2,75,65,first),row(3,80,75,first)]);
assert.equal(distinctReadingOnly.listeningTrendEnough,false);
const filtered = buildMockScoreReadiness([row(1,70,60,first),row(2,75,65,second),row(3,80,75,second),{...row(4,99,99,ids('x')) ,modeId:'quick'}, {...row(5,99,99,ids('y')),questions:100}]);
assert.equal(filtered.count,3);
assert.equal(filtered.listeningTrendEnough,true);
// Malformed, abandoned, null/empty accuracy, and duplicate attemptId rows must not corrupt readiness.
const edge = buildMockScoreReadiness([
  null,
  { status: 'abandoned', modeId: 'full', questions: 200, completedAt: 1, listeningAccuracy: 100, readingAccuracy: 100 },
  { status: 'completed', modeId: 'full', questions: 200, completedAt: 2, listeningAccuracy: null, readingAccuracy: 80 },
  { status: 'completed', modeId: 'full', questions: 200, completedAt: 3, listeningAccuracy: '', readingAccuracy: 80 },
  { status: 'completed', modeId: 'full', questions: 200, completedAt: 4, listeningAccuracy: 105, readingAccuracy: 80 },
  row(10, 60, 70, first, { attemptId: 'att-1' }),
  row(11, 80, 90, first, { attemptId: 'att-1' }),
  row(12, 70, 80, second, { attemptId: 'att-2' })
]);
assert.equal(edge.count, 2, 'duplicate attemptId must deduplicate and malformed rows must be ignored');
assert.equal(edge.readingAverage, 85, 'deduplicated att-1 keeps latest score 90 paired with att-2 score 80');
assert.equal(edge.listeningTrendEnough, true);
console.log('mock-score-readiness: PASS (same-form gating, distinct-form detection, overlap disclosure, legacy fail-closed, malformed/duplicate-attempt hardening, Reading independence, full-mock filtering)');
