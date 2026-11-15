import assert from 'node:assert/strict';
import fs from 'node:fs';

const app = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const stateLine = app.split('\n').find(line => line.startsWith('const state =')) || '';
assert.match(stateLine, /questionStartedAt: null/, 'practice state has a dedicated question start timestamp');
assert.match(app, /state\.currentQuestion=q; state\.questionStartedAt=null;[\s\S]*?await savePracticeSession\(\); state\.questionStartedAt=Date\.now\(\); renderQuestion\(\);/, 'timer starts immediately before the question is rendered, after session persistence');
assert.match(app, /const answeredAt=Date\.now\(\);\s*const responseDurationMs=Number\.isFinite\(state\.questionStartedAt\)\?Math\.max\(0,answeredAt-state\.questionStartedAt\):null;/, 'duration is measured once at answer submission and never negative');
assert.match(app, /state\.pendingSinglePractice=\{wordId:q\.wordId,questionId:q\.id,mode:q\.mode,correct,input,answeredAt,responseDurationMs\}/, 'Part 5 timing and answer are staged without revealing or persisting assessment evidence');
assert.match(app, /trackObjectivePractice\(q\.id,\{id:q\.id,choiceIds:\[`part5:\$\{q\.id\}`\]\},pending\.correct,pending\.answeredAt,pending\.responseDurationMs\)/, 'Part 5 timing is persisted with the stable question ID only after explicit confirmation');
console.log('PASS: Part 5 sentence-completion response-time capture is wired from question assignment through objective evidence persistence.');
