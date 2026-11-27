import assert from 'node:assert/strict';
import { buildRobotLearningInsights, formatRobotLearningInsights } from '../../assets/js/robot-learning-insights.js';

const now = 2_000_000_000_000;
const words = [{id:'a',word:'alpha'},{id:'b',word:'bravo'},{id:'c',word:'charlie'},{id:'d',word:'delta'}];
const result = buildRobotLearningInsights({
  words,
  vocabularyProgress: {
    a: {reviewCount:0},
    b: {reviewCount:4,correctCount:1,wrongCount:3,dueAt:now+86400000},
    c: {reviewCount:3,correctCount:3,wrongCount:0,dueAt:now-1000}
  },
  flashProgress: {a:{reps:0},b:{reps:2,lapses:2,correct:0,interval:0,dueAt:now+10000},c:{reps:2,interval:2,dueAt:now-10}},
  grammarItems:[{id:'g1',title:'Grammar 1',exercises:Array.from({length:6},(_,i)=>({id:i}))}],
  grammarProgress:{g1:{answers:{0:{answered:true,correct:false},1:{answered:true,correct:false},2:{answered:true,correct:false},3:{answered:true,correct:true},4:{answered:true,correct:false}}}},
  readingItems:[{id:'r1',title:'Reading 1',questions:[{},{},{}]}], readingProgress:{},
  listeningItems:[{id:'l1',title:'Listening 1',questions:[{},{},{}]}], listeningProgress:{},
  foundationItems:[{id:'f1',questionBank:[{},{},{}]}], foundationProgressMap:{f1:{evidence:{q1:{latestCorrect:false,recallDueAt:now-10},q2:{latestCorrect:false},q3:{latestCorrect:true}}}}, objectiveProgress:{objectives:{obj1:{items:{q1:{recallDueAt:now-100}}}}}, objectiveResourceMap:{objectives:[{id:'obj1'}]}, mockHistory:[{status:'completed',accuracy:62}]
}, now);
assert.equal(result.totals.learn > 0, true);
assert.equal(result.totals.practice > 0, true);
assert.equal(result.totals.review, 4);
assert.equal(result.sections.find(x=>x.name==='Ngữ pháp').accuracy, 20);
assert.equal(result.sections.find(x=>x.name==='Ngữ pháp').studiedUnits, 1);
assert.equal(result.sections.find(x=>x.name==='Ngữ pháp').totalUnits, 1);
assert.equal(result.sections.find(x=>x.name==='Ngữ pháp').coveragePercent, 100);
assert.equal(result.sections.find(x=>x.name==='Đọc hiểu').coveragePercent, 0);
assert.equal(result.sections.find(x=>x.name==='Từ vựng').studiedUnits, 2);
assert.equal(result.sections.find(x=>x.name==='Flashcard').studiedUnits, 2);
assert.equal(result.sections.find(x=>x.name==='Foundation').practice, 1);
assert.equal(result.sections.find(x=>x.name==='Foundation').review, 1);
assert.match(formatRobotLearningInsights(result), /Cần học/);
assert.match(formatRobotLearningInsights(result), /Cần luyện/);
assert.match(formatRobotLearningInsights(result), /Cần ôn/);
assert.ok(result.items.practice.some(item=>item.title==='bravo'));
assert.ok(result.items.review.some(item=>item.title==='charlie'));
assert.match(formatRobotLearningInsights(result), /chưa đủ dữ liệu để kết luận/);
const empty = buildRobotLearningInsights({words:[{id:'new'}]}, now);
assert.equal(empty.hasEvidence, false);
assert.equal(empty.sections.find(x=>x.name==='Từ vựng').coveragePercent, 0);
assert.equal(empty.sections.find(x=>x.name==='Thi thử').coveragePercent, null);
assert.match(formatRobotLearningInsights(empty), /chưa có lịch sử học tập đủ/);
assert.match(formatRobotLearningInsights(empty), /Cần học/);
// Snapshot aggregation is pure: caller-owned stores are not mutated.
const snapshot={words:[{id:'x'}],vocabularyProgress:{x:{reviewCount:0}},foundationItems:[{id:'f',questionBank:[{}]}],foundationProgressMap:{f:{evidence:{q:{latestCorrect:true,recallDueAt:now-1}}}}};
const before=JSON.stringify(snapshot); buildRobotLearningInsights(snapshot,now); assert.equal(JSON.stringify(snapshot),before);
// Mock-only completed history must establish hasEvidence === true (regression for array > 0 bug).
const mockOnly = buildRobotLearningInsights({ mockHistory: [{ status: 'completed', accuracy: 82, questions: 200 }] }, now);
assert.equal(mockOnly.hasEvidence, true);
assert.equal(mockOnly.sections.find(x => x.name === 'Thi thử').evidence, 1);
// Corrupted, null, or abandoned inputs must never crash or coerce null/empty accuracy into 0.
const corrupted = buildRobotLearningInsights({
  words: [null, {}, { id: 'ok' }],
  vocabularyProgress: null,
  grammarItems: [null, { id: 'g0' }],
  grammarProgress: null,
  foundationItems: null,
  mockHistory: [null, { status: 'abandoned', accuracy: 0 }, { status: 'completed', accuracy: null }, { status: 'completed', accuracy: '' }, { status: 'completed', accuracy: 120 }]
}, null);
assert.equal(corrupted.hasEvidence, false);
assert.equal(corrupted.sections.find(x => x.name === 'Thi thử').evidence, 0);
console.log('PASS: Robot learning insights classify learn/practice/review, calculate per-module studied-unit coverage, enforce evidence thresholds, handle mock-only/corrupted snapshots and do not mutate snapshots.');
