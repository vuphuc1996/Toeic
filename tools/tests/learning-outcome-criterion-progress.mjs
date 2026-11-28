import assert from 'node:assert/strict';
import {
  buildObjectiveCriterionIndex,
  recordObjectiveAttempt,
  recordExplanationRubric,
  listDueRecallItems,
  summarizeOutcomeCriteria,
  auditObjectiveProgress
} from '../../assets/js/learning-outcome-progress.js';

const resourceMap = { objectives: [
  { id: 'grammar-core', title: 'Grammar', kind: 'grammar', part: 'Grammar', resourceIds: ['grammar-lesson-a'] },
  { id: 'reading-part-7', title: 'Reading Part 7', kind: 'reading', part: 'Part 7', resourceIds: ['reading-p7'], reviewState: 'part7_expansion_requires_second_review' },
  { id: 'part5-sentence-completion', title: 'Separate Part 5', kind: 'practice', part: 'Part 5', resourceIds: ['p5-001'], reviewState: 'pending_independent_review_practice_only_not_mock_eligible' },
  { id: 'listening-part-4', title: 'Listening Part 4', kind: 'listening', part: 'Part 4', resourceIds: ['audio-4'] }
] };
const registry = { objectives: [
  { objectiveId: 'foundation-pre-a1-a1', outcomes: [{ id: 'foundation-pre-a1-a1-recognition', status: 'instrumented_practice_evidence' }] },
  { objectiveId: 'grammar-core', outcomes: [
    { id: 'grammar-core-contextual-choice', title: 'Grammar contextual choice', evidenceMetric: 'correct_rate', minimumUniqueItems: 2, masteryThreshold: 0.8, status: 'instrumented_practice_evidence' },
    { id: 'grammar-core-error-explanation', title: 'Grammar explanation', evidenceMetric: 'explanation_rubric', minimumUniqueItems: 2, masteryThreshold: 0.8, status: 'instrumented_learner_self_report' }
  ] },
  { objectiveId: 'reading-part-7', outcomes: [
    { id: 'reading-part-7-information-location', title: 'Find information', evidenceMetric: 'correct_rate', minimumUniqueItems: 2, masteryThreshold: 0.8, status: 'instrumented_practice_evidence' }
  ] },
  { objectiveId: 'part5-sentence-completion', outcomes: [
    { id: 'part5-sentence-completion-time-management', title: 'Timed accuracy', evidenceMetric: 'timed_accuracy', minimumUniqueItems: 2, masteryThreshold: 0.8, timeTargetMs: 30000, status: 'instrumented_practice_evidence' }
  ] },
  { objectiveId: 'listening-part-4', outcomes: [
    { id: 'listening-part-4-inference-action', title: 'Inference', evidenceMetric: 'correct_rate', minimumUniqueItems: 2, masteryThreshold: 0.8, status: 'criteria_defined_not_yet_instrumented' }
  ] }
] };
const criterionMap = { mappings: [
  { objectiveId: 'grammar-core', criterionId: 'grammar-core-contextual-choice', resourceId: 'grammar-lesson-a', questionKey: 'grammar:lesson-a:1' },
  { objectiveId: 'grammar-core', criterionId: 'grammar-core-contextual-choice', resourceId: 'grammar-lesson-a', questionKey: 'grammar:lesson-a:2' },
  { objectiveId: 'grammar-core', criterionId: 'grammar-core-error-explanation', resourceId: 'grammar-lesson-a', questionKey: 'grammar:lesson-a:1' },
  { objectiveId: 'grammar-core', criterionId: 'grammar-core-error-explanation', resourceId: 'grammar-lesson-a', questionKey: 'grammar:lesson-a:2' },
  { objectiveId: 'reading-part-7', criterionId: 'reading-part-7-information-location', resourceId: 'reading-p7', questionKey: 'reading:reading-p7:1' },
  { objectiveId: 'reading-part-7', criterionId: 'reading-part-7-information-location', resourceId: 'reading-p7', questionKey: 'reading:reading-p7:2' },
  { objectiveId: 'part5-sentence-completion', criterionId: 'part5-sentence-completion-time-management', resourceId: 'p5-001', questionId: 'p5-001', questionKey: 'part5:p5-001' },
  { objectiveId: 'part5-sentence-completion', criterionId: 'part5-sentence-completion-time-management', resourceId: 'p5-002', questionId: 'p5-002', questionKey: 'part5:p5-002' }
], mappingCountsByCriterion: {
  'grammar-core-contextual-choice': 2,
  'grammar-core-error-explanation': 2,
  'reading-part-7-information-location': 2,
  'part5-sentence-completion-time-management': 2
} };
const criterionIndex = buildObjectiveCriterionIndex(criterionMap);
assert.deepEqual(criterionIndex['grammar:lesson-a:1'], ['grammar-core-contextual-choice', 'grammar-core-error-explanation']);
assert.deepEqual(criterionIndex['part5:p5-001'], ['part5-sentence-completion-time-management']);
assert.deepEqual(criterionIndex['p5-001'], ['part5-sentence-completion-time-management']);
assert.equal(criterionIndex.unknown, undefined);
console.log('PASS: stable choiceId prefix and explicit questionId both index criterion evidence.');

let ledger = {};
ledger = recordObjectiveAttempt(ledger, ['grammar-core-contextual-choice'], 'grammar:lesson-a:1', true, 1000, 12000);
ledger = recordObjectiveAttempt(ledger, ['grammar-core-contextual-choice'], 'grammar:lesson-a:2', true, 2000, 14000);
ledger = recordObjectiveAttempt(ledger, ['grammar-core-error-explanation'], 'grammar:lesson-a:1', true, 1000, 12000);
ledger = recordObjectiveAttempt(ledger, ['grammar-core-error-explanation'], 'grammar:lesson-a:2', true, 2000, 14000);
ledger = recordExplanationRubric(ledger, ['grammar-core-error-explanation'], 'grammar:lesson-a:1', [true, true, true], 2100);
ledger = recordExplanationRubric(ledger, ['grammar-core-error-explanation'], 'grammar:lesson-a:2', [true, true, false], 2200);

ledger = recordObjectiveAttempt(ledger, ['reading-part-7-information-location'], 'reading:reading-p7:1', true, 1000, 10000);
ledger = recordObjectiveAttempt(ledger, ['reading-part-7-information-location'], 'reading:reading-p7:2', true, 2000, 11000);

ledger = recordObjectiveAttempt(ledger, ['part5-sentence-completion-time-management'], 'part5:p5-001', true, 1000, 25000);
ledger = recordObjectiveAttempt(ledger, ['part5-sentence-completion-time-management'], 'part5:p5-002', true, 2000, 35000);

const resultRows = summarizeOutcomeCriteria(ledger, registry, resourceMap, criterionMap, 5000);
assert.equal(resultRows.length, 5, 'Foundation criteria use their separate evidence store and are omitted from this TOEIC ledger summary');
const byId = new Map(resultRows.map(row => [row.outcomeId, row]));
assert.equal(byId.get('grammar-core-contextual-choice').mappingCount, 2);
assert.equal(byId.get('grammar-core-contextual-choice').observedItemCount, 2);
assert.equal(byId.get('grammar-core-contextual-choice').observedPercent, 100);
assert.equal(byId.get('grammar-core-contextual-choice').status, 'practice_threshold_met');
assert.equal(byId.get('grammar-core-error-explanation').observedPercent, 83);
assert.equal(byId.get('grammar-core-error-explanation').status, 'practice_threshold_met');
assert.equal(byId.get('reading-part-7-information-location').status, 'content_review_pending', 'second review gate blocks a practice threshold');
assert.equal(byId.get('part5-sentence-completion-time-management').observedItemCount, 2);
assert.equal(byId.get('part5-sentence-completion-time-management').observedCorrectCount, 1, 'timed accuracy rejects a correct response outside the 30-second internal target');
assert.equal(byId.get('part5-sentence-completion-time-management').observedPercent, 50);
assert.equal(byId.get('part5-sentence-completion-time-management').timeTargetMs, 30000);
assert.equal(byId.get('listening-part-4-inference-action').status, 'not_instrumented');
assert.equal(byId.get('listening-part-4-inference-action').mappingCount, 0);
console.log('PASS: criterion-specific accuracy, learner-self-report rubric, internal timed target and editorial gate.');

const dueAt = ledger.objectives['grammar-core-contextual-choice'].items['grammar:lesson-a:1'].recallDueAt;
const due = listDueRecallItems(ledger, resourceMap, dueAt, 50, registry, criterionMap);
const criterionDue = due.find(item => item.objectiveId === 'grammar-core-contextual-choice' && item.itemId === 'grammar:lesson-a:1');
assert.ok(criterionDue);
assert.equal(criterionDue.isOutcomeCriterion, true);
assert.equal(criterionDue.mappedResourceId, 'grammar-lesson-a');
assert.equal(criterionDue.questionKey, 'grammar:lesson-a:1');
console.log('PASS: criterion-level delayed recall is present in the existing queue and retains its source resource.');

const cleanAudit = auditObjectiveProgress(ledger, resourceMap, registry);
assert.equal(cleanAudit.valid, true, 'criterion IDs are recognized when the outcome registry is supplied to the read-only audit');
const frozen = Object.freeze({ schemaVersion: 1, objectives: Object.freeze({ 'grammar-core-contextual-choice': Object.freeze({ items: Object.freeze({ q: Object.freeze({ latestCorrect: true, latestAnsweredAt: 1, attempts: Object.freeze([Object.freeze({ correct: true, answeredAt: 1 })]), recallDueAt: 0, recallChecks: Object.freeze([]) }) }) }) }) });
const snapshot = JSON.stringify(frozen);
assert.equal(summarizeOutcomeCriteria(frozen, registry, resourceMap, criterionMap).length, 5);
assert.equal(JSON.stringify(frozen), snapshot, 'criterion summaries are read-only');
console.log('PASS: criterion ledger integrity and read-only dashboard summary.');
