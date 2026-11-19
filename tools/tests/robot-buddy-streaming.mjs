import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRobotBuddy } from '../../assets/js/robot-buddy.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const library = JSON.parse(read('data/robot/robot-library.json'));
const app = read('assets/js/app.js');
const css = read('assets/css/app.css');
const index = read('index.html');
const robotSource = read('assets/js/robot-buddy.js');

// Repeated questions should not be rendered as one rigid, identical sentence.
const engine = createRobotBuddy(library, () => 0);
const firstFeatureReply = engine.reply('Mở Từ vựng');
const secondFeatureReply = engine.reply('Mở Từ vựng');
assert.equal(firstFeatureReply.intent, 'feature');
assert.equal(firstFeatureReply.actions[0].page, 'dictionary');
assert.notEqual(firstFeatureReply.text, secondFeatureReply.text, 'Feature replies should vary their introduction, guidance or next-step wording.');
assert.equal(firstFeatureReply.source, 'local-context-composition');

const context = { page: 'dictionary', pageLabel: 'Từ vựng', currentItem: { kind: 'word', title: 'schedule', snippet: 'lên lịch' } };
const contextFirst = engine.reply('Giải thích từ này giúp tôi', context);
const contextSecond = engine.reply('Giải thích từ này giúp tôi', context);
assert.match(contextFirst.text, /schedule/);
assert.match(contextFirst.text, /lên lịch/);
assert.notEqual(contextFirst.text, contextSecond.text, 'Contextual answers should be composed with varied transitions and follow-up wording.');
assert.equal(contextFirst.source, 'current-app-interaction-context');

const unknown = engine.reply('Giúp tôi hiểu về tàu vũ trụ Sao Hỏa', context);
assert.match(unknown.text, /không muốn đoán sai|thêm một chút ngữ cảnh/);
assert.match(unknown.text, /schedule/);
assert.doesNotMatch(unknown.text, /mình có thể trả lời mọi câu hỏi/i);

// A real progressive renderer must reveal grapheme-sized text safely and finish outstanding streams.
assert.match(app, /function streamRobotMessage\(text,actions=\[\],onComplete=null\)/);
assert.match(app, /function finishRobotStream\(\)/);
assert.match(app, /active\.item\.removeAttribute\('aria-busy'\)/);
assert.match(app, /active\.content\.textContent=active\.characters\.slice\(0,active\.index\)\.join\(''\)/);
assert.match(app, /finishRobotStream\(\);[\s\S]*appendRobotMessage\('user',text\)/, 'A new user turn must finish the previous partial answer before appending the next turn.');
assert.match(app, /prefers-reduced-motion: reduce/);
assert.match(app, /streamRobotMessage\(reply\.text,reply\.actions\|\|\[\],onComplete\)/);
assert.doesNotMatch(app.slice(app.indexOf('function streamRobotMessage'), app.indexOf('\nfunction appendRobotChoiceButtons')), /innerHTML\s*=/, 'Streamed content must be rendered with textContent, never injected HTML.');
assert.match(css, /\.robot-chat-bubble p\.is-streaming::after/);
assert.match(css, /@keyframes robot-stream-caret/);
assert.match(index, /Phản hồi được kết hợp theo ngữ cảnh và hiển thị từng phần/);

// The Buddy stays offline and does not turn a visual typing effect into a false AI/API claim.
assert.equal(library.privacy.usesExternalApi, false);
assert.equal(library.privacy.usesGenerativeModel, false);
assert.equal(library.privacy.transmitsLearnerData, false);
assert.doesNotMatch(robotSource, /fetch\s*\(|XMLHttpRequest|WebSocket|window\.ai/i);

console.log('PASS: Robot Buddy streamed response renderer, dynamic local composition, contextual variation, safe text rendering and offline boundary.');
