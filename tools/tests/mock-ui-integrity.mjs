import assert from 'node:assert/strict';
import fs from 'node:fs';

const html = fs.readFileSync(new URL('../../index.html', import.meta.url), 'utf8');
const app = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const engine = fs.readFileSync(new URL('../../assets/js/mock-engine.js', import.meta.url), 'utf8');
const css = fs.readFileSync(new URL('../../assets/css/app.css', import.meta.url), 'utf8');
const sw = fs.readFileSync(new URL('../../sw.js', import.meta.url), 'utf8');

const ids = [...html.matchAll(/\bid=["']([^"']+)["']/g)].map(match => match[1]);
assert.equal(ids.length, new Set(ids).size, 'index.html must not contain duplicate IDs');
for (const id of ['page-mock','mockLanding','mockPoolStats','mockResumePanel','mockExamStage','mockTimerValue','mockQuestionMap','mockQuestionGroups','mockResultStage','mockSubmitButton','mockHistoryList']) {
  assert.ok(ids.includes(id), `missing required Mock UI node #${id}`);
}
for (const mode of ['quick','half','full']) assert.ok(html.includes(`data-mock-start="${mode}"`), `missing ${mode} mode card`);
assert.match(app, /from ['"]\.\/mock-engine\.js['"]/);
assert.match(app, /toeic:mock-usage:v1/, 'lifetime question rotation must have its own LocalStorage key');
assert.match(app, /mockUsageCounts/);
assert.match(app, /mock-score-dial/);
assert.match(app, /equating theo từng đề/);
assert.match(engine, /new Set\(questionIds\)\.size !== questionIds\.length/);
assert.match(engine, /usageCounts = null/);
assert.match(css, /\.mock-score-dial/);
assert.match(sw, /"\.\/assets\/js\/mock-engine\.js"/);
assert.doesNotMatch(app, /dbSet\(['"]mock-/i, 'mock state must not be written into IndexedDB');

console.log(`Mock UI integrity PASS: ${ids.length} unique HTML IDs, three modes, split skill report, persistent usage ledger, no IndexedDB writes.`);
