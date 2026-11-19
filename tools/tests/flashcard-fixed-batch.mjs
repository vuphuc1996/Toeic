import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const html = read('index.html');
const app = read('assets/js/app.js');
const workflow = read('.github/workflows/validate-data.yml');

assert.doesNotMatch(html, /flashNextBatch|Số từ tiếp theo|<option value=\"5\">5 từ/);
assert.match(html, /Mỗi lượt học gồm tối đa 10 từ/);
assert.doesNotMatch(app, /flashNextBatch|Ôn từ sai \+ 5 từ mới/);
const start = app.match(/function startFlashSession\([\s\S]*?\nfunction advanceFlashCard/);
assert.ok(start, 'startFlashSession definition should be present');
assert.match(start[0], /includeIds\.slice\(0,10\)/);
assert.match(start[0], /flashPickBatch\(topic,10\)/);
assert.match(app, /const nextSize=10/);
assert.match(app, /allWrong\.slice\(0,10\)/);
assert.match(app, /flashPickBatch\(topic,Math\.max\(0,10-ids\.length\),ids\)/);
assert.match(workflow, /node tools\/tests\/flashcard-fixed-batch\.mjs/);

console.log('PASS: Flashcard has one 10-word session size across topic, next-batch and wrong-answer review flows; 5-word selector removed.');
