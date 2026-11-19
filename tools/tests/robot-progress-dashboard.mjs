import assert from 'node:assert/strict';
import fs from 'node:fs';

const app = fs.readFileSync(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const dashboardStart = app.indexOf('function appendRobotProgressDashboard(insights,anchor=null,actions=[])');
const dashboardEnd = app.indexOf('\nfunction runRobotProgressAnalysis()', dashboardStart);
const analysisStart = dashboardEnd + 1;
const analysisEnd = app.indexOf('\nfunction sendRobotMessage(', analysisStart);
const sendStart = analysisEnd + 1;
const sendEnd = app.indexOf('\nfunction robotShowWelcome()', sendStart);
assert.ok(dashboardStart >= 0 && dashboardEnd > dashboardStart, 'visual dashboard renderer must exist');
assert.ok(analysisEnd > analysisStart && sendEnd > sendStart, 'both progress-analysis entry points must exist');

class Element {
  constructor(tag) { this.tag = tag; this.children = []; this.attributes = {}; this.style = {}; this.dataset = {}; this.parentNode = null; this._text = ''; this.className = ''; }
  append(...nodes) { for (const node of nodes) { this.children.push(node); if (node && typeof node === 'object') node.parentNode = this; } }
  after(node) { if (!this.parentNode) return; const list = this.parentNode.children; const index = list.indexOf(this); list.splice(index + 1, 0, node); node.parentNode = this.parentNode; }
  setAttribute(key, value) { this.attributes[key] = String(value); }
  get childNodes() { return this.children; }
  get textContent() { return [this._text, ...this.children.map(child => child?.textContent || '')].filter(Boolean).join(' '); }
  set textContent(value) { this._text = String(value ?? ''); this.children = []; }
  get scrollHeight() { return this.children.length; }
}

const log = new Element('div');
const messages = [];
const input = { value: 'Phân tích tiến độ học tập của tôi.' };
const insights = {
  hasEvidence: true,
  totals: { learn: 12, practice: 3, review: 4 },
  sections: [
    { name: 'Từ vựng', learn: 4, practice: 1, review: 2, evidence: 8, accuracy: 75, attempted: 8, studiedUnits: 8, totalUnits: 10, coveragePercent: 80 },
    { name: 'Nghe hiểu', learn: 8, practice: 2, review: 2, evidence: 5, accuracy: 60, attempted: 5, studiedUnits: 2, totalUnits: 10, coveragePercent: 20 },
  ],
  items: { learn: [], practice: [], review: [] },
};
const actions = [{ label: 'Mở Từ vựng', page: 'dictionary' }];
let settings = { learningInsightsEnabled: true };
let typingTimer = null;
let speakingTimer = null;
const fakeDocument = { createElement: tag => new Element(tag) };
const fakeDollar = selector => selector === '#robotChatLog' ? log : selector === '#robotChatInput' ? input : null;
const classifyEngine = { classify: () => ({ intent: 'insights' }), reply: () => ({ text: 'legacy prose should not be rendered', actions: [], emotion: 'happy' }) };

const functions = new Function('document', '$', 'robotReadSettings', 'getRobotLearningInsightsNow', 'appendRobotMessage', 'getRobotInsightActions', 'setRobotEmotion', 'setRobotTyping', 'robotBuddyEngine', 'state', 'displayWord', 'getPrimarySense', 'setTimeout', 'clearTimeout',
  `${app.slice(dashboardStart, dashboardEnd)}\n${app.slice(analysisStart, analysisEnd)}\nlet robotTypingTimer=null; let robotSpeakingTimer=null;\n${app.slice(sendStart, sendEnd)}\nreturn { appendRobotProgressDashboard, runRobotProgressAnalysis, sendRobotMessage };`)(
  fakeDocument, fakeDollar, () => settings, () => insights,
  (role, text) => messages.push({ role, text }), () => actions,
  () => {}, () => {}, classifyEngine,
  { activePage: 'dashboard' }, value => value, () => null,
  callback => { callback(); return 1; }, () => {}
);

// Explicit analysis must append one dashboard, with no duplicate bot prose summary.
functions.runRobotProgressAnalysis();
assert.equal(messages.length, 1);
assert.deepEqual(messages[0], { role: 'user', text: 'Phân tích tiến độ học tập của tôi.' });
assert.equal(log.children.filter(node => node.className === 'robot-progress-dashboard').length, 1);
let dashboard = log.children.find(node => node.className === 'robot-progress-dashboard');
assert.equal(dashboard.children.filter(node => node.className === 'robot-progress-totals').length, 1);
assert.equal(dashboard.children.find(node => node.className === 'robot-progress-totals').children.length, 3);
assert.ok(!dashboard.textContent.includes('legacy prose should not be rendered'));

// Natural-language insight intent must use the same single-dashboard output path.
log.children = [];
messages.length = 0;
functions.sendRobotMessage('Phân tích tiến độ học tập của tôi.');
assert.equal(messages.length, 1, 'insight response must not append a second prose bot message');
assert.equal(messages[0].role, 'user');
assert.equal(log.children.filter(node => node.className === 'robot-progress-dashboard').length, 1);
dashboard = log.children.find(node => node.className === 'robot-progress-dashboard');
assert.equal(dashboard.children.filter(node => node.className === 'robot-progress-totals').length, 1);
assert.equal(dashboard.children.find(node => node.className === 'robot-progress-totals').children.length, 3);
assert.ok(!dashboard.textContent.includes('legacy prose should not be rendered'));

// The output is one visual summary, not repeated prose copies of the same totals.
for (const label of ['Cần học', 'Cần luyện', 'Cần ôn']) {
  const totalCards = dashboard.children.find(node => node.className === 'robot-progress-totals');
  assert.equal(totalCards.children.filter(card => card.textContent.includes(label)).length, 1, `${label} total appears once`);
}
console.log('PASS: Robot Buddy explicit and natural-language progress analysis each render one dashboard and suppress duplicate prose/totals.');
