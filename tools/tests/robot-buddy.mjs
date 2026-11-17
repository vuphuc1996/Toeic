import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRobotBuddy, normalizeRobotText } from '../../assets/js/robot-buddy.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const library = JSON.parse(read('data/robot/robot-library.json'));
const app = read('assets/js/app.js');
const index = read('index.html');
const css = read('assets/css/app.css');
const sw = read('sw.js');
const manifest = JSON.parse(read('data/manifest.json'));

// Static library size, diversity and metadata contract.
const expected = { greeting: 60, encouragement: 100, caring: 60, learning: 80, help: 100, reaction: 60, rest: 40 };
const allMessages = Object.values(library.categories).flatMap(group => group.messages.map(item => item.text));
assert.deepEqual(Object.fromEntries(Object.entries(library.categories).map(([key, value]) => [key, value.messages.length])), expected);
assert.equal(allMessages.length, 500, 'The primary dialogue library must contain exactly 500 authored message variants.');
assert.equal(new Set(allMessages).size, 500, 'Primary message variants must be unique.');
assert.ok(Object.keys(library.features).length >= 12, 'Feature help must cover at least 10 real application destinations.');
assert.ok(library.faq.length >= 6, 'The local FAQ set must cover common support topics.');
assert.ok(library.quickPrompts.length >= 10, 'Provide enough quick prompts for conversational discovery.');
assert.equal(library.privacy.readsLearnerProgress, true);
assert.equal(library.privacy.learnerProgressAccess, 'read-only-local-snapshot');
assert.equal(library.privacy.usesExternalApi, false);
assert.equal(library.privacy.usesGenerativeModel, false);
assert.equal(library.privacy.transmitsLearnerData, false);

// Engine responses are deterministic with a fixed random source and never need a learner profile.
const engine = createRobotBuddy(library, () => 0);
assert.equal(normalizeRobotText('Đánh giá ĐẦU VÀO!'), 'danh gia dau vao');
assert.equal(engine.reply('Bạn là ai?').intent, 'identity');
assert.match(engine.reply('Bạn là ai?').text, /Vũ Nguyễn Hoàng Phúc/);
assert.match(engine.reply('Bạn là ai?').text, /đọc tiến độ học/);
assert.equal(engine.classify('Phân tích tiến độ học của tôi').intent, 'insights');
const dictionary = engine.reply('Tôi muốn tìm từ vựng');
assert.equal(dictionary.intent, 'feature');
assert.equal(dictionary.actions[0].page, 'dictionary');
assert.match(dictionary.text, /Từ vựng/);
assert.equal(engine.reply('Tôi muốn luyện Listening').actions[0].page, 'listening');
assert.equal(engine.reply('Mở đánh giá đầu vào').actions[0].command, 'placement');
const routeCases = [
  ['Giới thiệu Trang chủ','dashboard'], ['Mở Flashcard','flashcards'], ['Mở Ôn tập','practice'], ['Học ngữ pháp','grammar'],
  ['Luyện đọc Reading','reading'], ['Luyện nghe Listening','listening'], ['Thi thử TOEIC','mock'],
  ['Học Foundation','foundation'], ['Mở Cấu hình','settings'], ['Quản lý dữ liệu','data']
];
for (const [utterance, destination] of routeCases) {
  const routed = engine.reply(utterance);
  assert.equal(routed.intent, 'feature', `Expected feature intent for: ${utterance}`);
  assert.equal(routed.actions[0].page, destination, `Incorrect destination for: ${utterance}`);
  assert.ok(routed.text.length > 10, `Missing feature-help content for: ${utterance}`);
}
assert.equal(Object.keys(library.features).length, 12);
assert.equal(Object.values(library.features).reduce((sum,item)=>sum+item.messages.length,0), 59);
for (const faq of library.faq) {
  const result = engine.reply(faq.keywords[0]);
  assert.equal(result.intent, 'faq', `FAQ keyword did not resolve: ${faq.id}`);
  assert.ok(result.text.length > 10, `FAQ answer missing: ${faq.id}`);
}
assert.equal(engine.reply('Ứng dụng có dùng offline không?').intent, 'faq');
assert.match(engine.reply('Bạn có thể kể về tàu vũ trụ Sao Hỏa không?').text, /chưa hiểu mọi câu hỏi tự do/);
assert.ok(['motivation','caring','sleepy','listening','thinking'].includes(engine.reply('Hãy động viên tôi nhé').emotion));

// Robot receives already-loaded local progress snapshots; it must not open storage itself.
const robotBlock = app.slice(app.indexOf('function robotHeadMarkup'), app.indexOf('function detectDeviceProfile'));
assert.ok(robotBlock.length > 5000, 'Robot runtime should be present in the application.');
for (const forbidden of ['dbGet(', 'DB_NAME', 'indexedDB.open', 'fetch(https://', 'publishRobotEvent(']) {
  assert.ok(!robotBlock.includes(forbidden), `Robot UI must not open storage or call remote services: ${forbidden}`);
}
assert.ok(app.includes('buildRobotLearningInsights(getRobotLearningSnapshot())'), 'Robot must use the local progress insight aggregator.');
assert.ok(app.includes('insights.totals.review>0') && app.includes('insights.totals.practice>0'), 'Idle nudges may use grounded local progress signals.');
assert.ok(app.includes('learningInsightsEnabled!==false'), 'Progress analysis must be independently switchable.');
assert.ok(app.includes("import { createRobotBuddy } from './robot-buddy.js'"));
assert.ok(app.includes("import { buildRobotLearningInsights, formatRobotLearningInsights } from './robot-learning-insights.js'"));
assert.ok(app.includes("fetch(releaseDataUrl('./data/robot/robot-library.json')"), 'Robot loads only its bundled static content library.');
assert.ok(app.includes("const ROBOT_BUDDY_SETTINGS_KEY = 'toeic:robot-buddy-settings:v1'"));
assert.ok(app.includes("toeic:robot-companion-onboarding:v1"), 'Migrate only the old Robot onboarding preference; do not re-prompt v2.83 users.');
assert.ok(app.includes("accepted:'start',skipped:'skip',returning:'returning'"));
assert.ok(app.includes('startPlacementDiagnostic()'), 'Placement is only opened through an explicit user action.');
assert.ok(app.includes('scheduleRobotIdle(90000)'));
assert.ok(app.includes('now-time<3600000') && app.includes('robotIdleNoticeTimes.length<3'));
assert.ok(app.includes('setTimeout(()=>{hideRobotIdleNudge();scheduleRobotIdle(robotIdleStage===1?300000:600000);},14000)'));
assert.ok(index.includes('id="robotIdleNudge"') && index.includes('id="robotChatForm"') && index.includes('id="robotMuteToggle"'));
assert.ok(index.includes('id="robotChatLog"') && index.includes('id="robotQuickPrompts"'));
assert.ok(index.includes('id="robotInsightsToggle"'));
assert.match(index, /chỉ đọc tiến độ cục bộ khi bật phân tích/);
assert.ok(index.includes('class="robot-header-main"') && index.includes('class="robot-header-controls"'), 'Robot header must keep the title/close row separate from the two preference controls.');
assert.match(index, /Lời nhắc: Bật/);
assert.match(css, /\.robot-quick-prompts\{[^}]*max-height:118px/);
assert.match(css, /\.robot-prompt-chip\{[^}]*font:700 10px/);
assert.match(css, /\.robot-mute-toggle\[aria-pressed=\"true\"\]\{background:#eef7ff/);
assert.ok(app.includes('function updateRobotMuteToggle()'), 'Reminder state must be presented as an explicit on/off toggle.');
assert.ok(app.includes('function getRobotInsightActions(insights)'), 'Learning insights must expose grounded navigation shortcuts.');
const insightActionSource = app.slice(app.indexOf('function getRobotInsightActions'), app.indexOf('function sendRobotMessage'));
const getInsightActions = new Function(`${insightActionSource}; return getRobotInsightActions;`)();
assert.deepEqual(getInsightActions({ hasEvidence: false, items: { learn: [{ area: 'Từ vựng' }] } }), []);
assert.deepEqual(getInsightActions({ hasEvidence: true, items: {
  review: [{ area: 'Từ vựng' }, { area: 'Nghe hiểu' }],
  practice: [{ area: 'Thi thử' }],
  learn: [{ area: 'Foundation' }, { area: 'Flashcard' }]
} }), [
  { label: 'Mở Từ vựng', page: 'dictionary' },
  { label: 'Mở Nghe hiểu', page: 'listening' },
  { label: 'Mở Thi thử', page: 'mock' },
  { label: 'Mở Foundation', page: 'foundation' }
], 'Only evidence-mapped, unique module actions are returned, capped at four.');
assert.ok(app.includes('/(Robot Buddy|TOEIC Dictionary|Vũ Nguyễn Hoàng Phúc)/giu'), 'Robot replies must safely emphasize the product and developer names.');
assert.ok((index.match(/class="robot-head-svg"/g) || []).length >= 3, 'The same head-only SVG is reused for launcher, panel and idle bubble.');
assert.ok(!/robot-body|robot-torso|robot-arms|robot-legs/i.test(index), 'The mascot must be head-only.');
assert.ok(css.includes('.robot-head-svg[data-emotion="thinking"]') && css.includes('.robot-head-svg[data-emotion="analyzing"]') && css.includes('.robot-head-svg[data-emotion="celebrate"]') && css.includes('.robot-head-svg[data-emotion="sleepy"]'));
assert.ok(css.includes('@media(prefers-reduced-motion:reduce)'));
assert.match(css, /@media\(max-width:430px\)\{\.quick-help-panel\{max-height:72dvh/);

// Static assets must be available offline and version markers must match.
assert.equal(manifest.version, '2.85.0');
for (const file of ['./assets/js/robot-buddy.js', './assets/js/robot-learning-insights.js', './data/robot/robot-library.json', './assets/js/learning-assistant.js', './assets/js/quick-help.js']) {
  assert.ok(sw.includes(file), `Service Worker missing required offline resource: ${file}`);
  assert.ok(fs.existsSync(path.join(root, file.slice(2))), `Static resource does not exist: ${file}`);
}
assert.match(read('assets/js/learning-assistant.js'), /Intentionally executes nothing/i);
assert.match(read('assets/js/quick-help.js'), /intentionally executes nothing/i);

console.log('PASS: offline dialogue library, feature/FAQ routing, read-only local progress integration, privacy toggle, head-only emotions and idle safeguards.');
