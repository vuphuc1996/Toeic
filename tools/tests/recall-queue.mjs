import assert from 'node:assert/strict';
import { listDueRecallItems, recordObjectiveAttempt } from '../../assets/js/learning-outcome-progress.js';

const resourceMap = { objectives: [
  { id: 'grammar-core', title: 'Ngữ pháp TOEIC', kind: 'grammar', resourceIds: ['lesson-a'] },
  { id: 'reading-part-7', title: 'Đọc TOEIC Part 7', kind: 'reading', part: 'Part 7', resourceIds: ['reading-a'] },
  { id: 'listening-part-1', title: 'Nghe TOEIC Part 1', kind: 'listening', part: 'Part 1', resourceIds: ['listen-a'] }
] };
let ledger = {};
ledger = recordObjectiveAttempt(ledger, ['grammar-core'], 'lesson-a::index:2::A|B', true, 1000);
ledger = recordObjectiveAttempt(ledger, ['reading-part-7'], 'read-q-1', false, 2000);
ledger = recordObjectiveAttempt(ledger, ['listening-part-1'], 'listen-q-1', true, 3000);
ledger = recordObjectiveAttempt(ledger, ['unknown-objective'], 'orphan-q', true, 4000);
const queue = listDueRecallItems(ledger, resourceMap, 86403000);
assert.equal(queue.length, 3, 'only due items belonging to known objectives appear');
assert.equal(queue[0].itemId, 'lesson-a::index:2::A|B', 'earliest due item is first');
assert.equal(queue[0].objectiveTitle, 'Ngữ pháp TOEIC');
assert.equal(queue[1].latestCorrect, false);
assert.equal(queue[2].kind, 'listening');
assert.equal(listDueRecallItems(ledger, resourceMap, 86403000, 2).length, 2, 'limit is applied after sorting');
assert.equal(listDueRecallItems(ledger, resourceMap, 86400999).length, 0, 'future items are not shown early');
assert.equal(listDueRecallItems(ledger, resourceMap, 86403000, 0).length, 0, 'zero limit returns an empty queue');

const app = await (await import('node:fs/promises')).readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const html = await (await import('node:fs/promises')).readFile(new URL('../../index.html', import.meta.url), 'utf8');
const css = await (await import('node:fs/promises')).readFile(new URL('../../assets/css/app.css', import.meta.url), 'utf8');
assert.match(app, /listDueRecallItems\(state\.objectiveProgress/);
assert.match(app, /data-recall-open/);
assert.match(app, /function openRecallItem\(/);
assert.match(app, /startPracticeFocus\(exactQuestion\?itemId:null\)/, 'Part 5 queue action passes only a valid exact due ID and safely falls back when the bank has changed');
assert.match(app, /chooseSentenceCompletionQuestion\(state\.sentenceCompletionItems,getSentenceCompletionWordPool\(\),state\.progress,state\.sentenceCompletionSeenIds,Math\.random,forcedWordId\)/);
assert.match(app, /visibilitychange.*renderRecallQueue/s, 'due list refreshes when the app becomes visible again');
assert.match(html, /id="learningRecallQueue"/);
assert.match(css, /\.recall-queue-item/);
assert.match(css, /@media\(max-width:560px\)\{\.recall-queue-header/);
console.log('PASS: due recall queue sorting, known-objective filtering, due boundary, cap, dashboard wiring and responsive layout.');
