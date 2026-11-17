import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import {
  buildFoundationProductionPortfolioMarkdown,
  recordFoundationProductionAttempt,
  recordFoundationProductionRevision
} from '../../assets/js/foundation-evidence.js';

const root = new URL('../../', import.meta.url);
const curriculum = JSON.parse(await readFile(new URL('data/learning-path/pre-a1-a1.json', root), 'utf8'));
const lessons = curriculum.lessons;
const a2Lessons = lessons.filter(lesson => lesson.level === 'A2');
assert.equal(a2Lessons.length, 13);
const lesson = a2Lessons[0];
const task = lesson.productionTask;
const taskId = task.id;
const firstResponse = 'Could you please send me the meeting notes before 3 p.m.? Thank you for your help. ```draft```';
const revisedResponse = 'Could you please send me the updated meeting notes before 3 p.m. today? Thank you for your help.';
let progress = {};
progress = recordFoundationProductionAttempt(progress, lesson.id, taskId,
  firstResponse, [true, false, true], 1_800_000_000_000, task.minimumWords);
progress = recordFoundationProductionRevision(progress, lesson.id, taskId,
  revisedResponse, [true, true, true], [true, true, true], 1_800_000_060_000, task.minimumWords);
// The historical application key must not leak into the new production portfolio export.
progress = recordFoundationProductionAttempt(progress, lesson.id, lesson.applicationTask.id,
  'This is a legacy application record and must not be exported.', [true, true, true], 1_800_000_120_000, 3);
const before = structuredClone(progress);
const exportText = buildFoundationProductionPortfolioMarkdown(progress, lessons, 1_800_000_180_000);

assert.match(exportText, /^# Foundation A2 — Nhật ký bài viết/m);
assert.match(exportText, /1\/13/);
assert.match(exportText, /Tình huống:/);
assert.match(exportText, /Bạn cần đồng nghiệp gửi biên bản cuộc họp/);
assert.match(exportText, /Bản đầu tiên/);
assert.match(exportText, /Bản viết lại 1/);
assert.ok(exportText.includes(firstResponse));
assert.ok(exportText.includes(revisedResponse));
assert.match(exportText, /Chi tiết tự đánh giá:[\s\S]*- \[x\]/);
assert.match(exportText, /Rà soát trước khi viết lại/);
assert.ok(exportText.includes('Could you please send me the meeting notes before 3 p.m.? Thank you for your help.'));
assert.ok(!exportText.includes('legacy application record'));
assert.match(exportText, /````text[\s\S]*```draft```[\s\S]*````/,
  'embedded triple backticks must not break the exported learner-response block');
assert.deepEqual(progress, before, 'export generation must not mutate local learning progress');

const empty = buildFoundationProductionPortfolioMarkdown({}, lessons, 1_800_000_180_000);
assert.match(empty, /0\/13/);
assert.match(empty, /Chưa có câu trả lời A2 nào được lưu/);

const app = await readFile(new URL('assets/js/app.js', root), 'utf8');
const css = await readFile(new URL('assets/css/app.css', root), 'utf8');
assert.match(app, /buildFoundationProductionPortfolioMarkdown/);
assert.match(app, /data-foundation-production-export/);
assert.match(app, /function exportFoundationProductionPortfolio\(/);
assert.match(css, /\.foundation-portfolio-export/);
console.log('PASS: local A2 writing portfolio Markdown export preserves all learner attempts, task rubric/revision context, and progress ledger immutability.');
