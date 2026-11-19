import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const css = fs.readFileSync(path.join(root, 'assets/css/app.css'), 'utf8');
const app = fs.readFileSync(path.join(root, 'assets/js/app.js'), 'utf8');
const index = fs.readFileSync(path.join(root, 'index.html'), 'utf8');

function rules(selector) {
  const escaped = selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const matches = [...css.matchAll(new RegExp(`${escaped}\\s*\\{([^}]*)\\}`, 'g'))];
  assert.ok(matches.length, `Missing CSS rule: ${selector}`);
  return matches.map(match => match[1]);
}

const chatRules = rules('.robot-chat-log');
const promptRules = rules('.robot-quick-prompts');
const shellRules = rules('.robot-chat-shell');
const footerRules = rules('.robot-local-note');
assert.ok(chatRules.some(rule => /flex:1 1 220px/.test(rule)), 'Chat log must have an independent flexible basis.');
assert.ok(chatRules.some(rule => /min-height:132px/.test(rule)), 'Desktop chat needs a bounded minimum height.');
assert.ok(chatRules.some(rule => /flex-basis:190px/.test(rule)), 'Mobile chat must use its own flexible basis.');
assert.ok(chatRules.some(rule => /overflow(?:-y)?:auto/.test(rule)), 'Chat content must scroll within its own area.');
assert.ok(promptRules.some(rule => /flex:0 0 auto/.test(rule) && /flex-shrink:0/.test(rule) && /max-height:112px/.test(rule)), 'Quick prompts must not shrink with chat content.');
assert.ok(promptRules.some(rule => /max-height:104px/.test(rule)), 'Mobile quick prompts need a bounded independent area.');
assert.ok(promptRules.some(rule => /max-height:68px/.test(rule) && /min-height:34px/.test(rule)), 'Short landscape must retain a scrollable minimum prompt tray.');
assert.match(css, /@media\(orientation:landscape\) and \(max-height:520px\)\{[^}]*\.robot-chat-shell\{gap:5px;padding:6px 10px 7px\}/s, 'Short landscape must use a compact chat shell.');
assert.ok(shellRules.some(rule => /min-height:0/.test(rule) && /overflow:hidden/.test(rule)), 'Chat shell must constrain its children.');
assert.ok(footerRules.some(rule => /font-size:6\.5px/.test(rule)), 'Privacy footer must use smaller type.');
assert.match(css, /\.robot-chat-form,\.robot-typing,\.robot-local-note\{flex:0 0 auto\}/, 'Composer, typing indicator and privacy footer must not shrink.');
assert.ok(index.includes('id="robotQuickPrompts"'), 'Quick-prompt menu must remain available in the panel.');
const sendMessageBlock = app.slice(app.indexOf('function sendRobotMessage'), app.indexOf('function robotShowWelcome'));
assert.doesNotMatch(sendMessageBlock, /robotQuickPrompts[^\n]*hidden\s*=\s*true/, 'Sending a message must not hide the quick-prompt menu.');
assert.match(sendMessageBlock, /Keep the quick-prompt menu available during the whole chat session/);
console.log('PASS: Robot Buddy chat scrolls independently; quick prompts, composer and footer remain pinned; offline note uses compact type.');

// Mobile composer must avoid iOS automatic focus zoom while retaining normal pinch zoom.
assert.match(css, /@media \(hover:none\) and \(pointer:coarse\)\{[\s\S]*?#quickHelp \.robot-chat-form input\{[^}]*font-size:16px!important/);
assert.match(css, /#quickHelp \.robot-chat-form input\{[^}]*min-height:42px/);
assert.doesNotMatch(index, /user-scalable\s*=\s*no/);
// Progress dashboard is constructed from read-only snapshots and uses accessible bounded meters.
assert.match(app, /function appendRobotProgressDashboard\(insights,anchor=null,actions=\[\]\)/);
assert.match(app, /role','progressbar'/);
assert.match(app, /Phân tích tiến độ của tôi/);
assert.match(css, /\.robot-progress-total\.is-learn/);
assert.match(css, /\.robot-progress-total\.is-practice/);
assert.match(css, /\.robot-progress-total\.is-review/);
console.log('PASS: mobile focus zoom is prevented without disabling pinch zoom; Robot Buddy progress dashboard is responsive, color-coded and accessible.');

// Page-only insight action buttons must be delegated and navigable.
assert.match(app, /closest\('\[data-robot-command\],\[data-robot-page\]'\)/);
assert.match(app, /handleRobotCommand\(command\.dataset\.robotCommand\|\|'',command\.dataset\.robotPage\|\|''\)/);
const robotCommand = app.slice(app.indexOf('function handleRobotCommand('), app.indexOf('function handleRobotInput('));
assert.match(robotCommand, /if\(page\)\{setQuickHelpOpen\(false\);navigate\(page\);return;\}/);
// The progress insight response is one dashboard, not a duplicate prose summary.
const insightSend = app.slice(app.indexOf('function sendRobotMessage('), app.indexOf('function robotShowWelcome('));
assert.match(insightSend, /if\(progressInsights\)\{[\s\S]*?streamRobotMessage\(/);
assert.match(insightSend, /appendRobotProgressDashboard\(progressInsights,null,reply\.actions\|\|\[\]\)/);
assert.match(insightSend, /else streamRobotMessage\(reply\.text,reply\.actions\|\|\[\],onComplete\)/);
assert.match(app, /function appendRobotProgressDashboard\(insights,anchor=null,actions=\[\]\)/);
assert.match(app, /className='robot-progress-actions'/);
assert.match(app, /button\.dataset\.robotPage=action\.page/);
// Flashcard assessment confirmation must render above its focused learning backdrop (z-index 62).
const assessmentOverlayRules = rules('.modal-backdrop[data-modal-type="assessment-result"]');
assert.ok(assessmentOverlayRules.some(rule => Number((rule.match(/z-index\s*:\s*(\d+)/)||[])[1]) > 62), 'Flashcard result confirmation must stay above learning-focus-backdrop');
console.log('PASS: Robot Buddy page actions navigate; progress analysis renders one dashboard with routes; flashcard assessment modal stacks above focused learning.');
