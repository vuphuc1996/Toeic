import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8');
const index = read('index.html');
const app = read('assets/js/app.js');
const sw = read('sw.js');
const css = read('assets/css/app.css');
const designCss = read('assets/css/design-system.css');
const runtime = [index, app, sw, css, designCss].join('\n');

for (const id of ['quickHelpLauncher', 'quickHelpPanel', 'quickHelpClose', 'robotCompanionGreeting', 'robotCompanionMessage', 'robotCompanionSnapshot', 'robotCompanionActions']) {
  assert.ok(index.includes(`id="${id}"`), `Missing Robot Buddy UI: ${id}`);
}
assert.ok(index.includes('id="icon-robot"'), 'The help launcher must use the robot icon.');
assert.ok(index.includes('<use href="#icon-robot"></use>'), 'Robot icon must render in the launcher/header.');
assert.ok(!index.includes('quickHelpGuide') && !index.includes('data-quick-help-guide'), 'The usage guide must be removed.');
assert.ok(!/Hướng dẫn sử dụng/.test(index), 'The removed usage guide must not be advertised.');
assert.ok(app.includes('data-robot-onboarding=\"start\"') && app.includes('data-robot-onboarding=\"skip\"'), 'New users must be offered Placement Diagnostic or skip.');
assert.ok(app.includes("const ROBOT_ONBOARDING_KEY='toeic:robot-companion-onboarding:v1'"), 'First-run choice must be remembered on this device.');
assert.ok(app.includes('initializeRobotCompanion();'), 'Robot onboarding must initialize after progress loads.');
assert.ok(app.includes('hasReturningLearnerFootprint()'), 'Returning users must not be mistaken for a first-time visitor.');
assert.ok(app.includes('data-robot-action') && app.includes('handleRobotAction'), 'Robot recommendations must be interactive.');
assert.ok(app.includes('publishRobotEvent('), 'Learning milestones must be able to notify the Robot.');
assert.ok(app.includes("case 'weakest-grammar'"), 'Robot must link to a grammar lesson with enough evidence to identify a review need.');
assert.ok(app.includes('snapshot.weakestGrammarLesson'), 'The Robot must only summarize grammar weak areas backed by existing progress.');
assert.ok(app.includes("page==='mock'&&state.mockExam?.status==='active'"), 'Robot must not obstruct a timed mock exam.');
assert.ok(/@media\(max-width:820px\)[\s\S]*?\.quick-help-panel/.test(css), 'Robot panel must have a compact mobile layout.');
assert.ok(css.includes('@media(prefers-reduced-motion:reduce)'), 'Animations must respect reduced-motion preferences.');
assert.ok(css.includes('@keyframes robot-launcher-float') && css.includes('@keyframes robot-panel-in'), 'Robot motion states must be defined.');
assert.ok(sw.includes('./assets/js/learning-assistant.js') && sw.includes('./assets/js/quick-help.js'), 'Both compatibility JS files must be registered in the offline cache.');
assert.ok(fs.existsSync(path.join(root, 'assets/js/quick-help.js')), 'Quick Help compatibility tombstone must exist to overwrite stale repository files.');
assert.ok(!/quickHelpWordSearch|findVocabularyPrefixMatches|maskVocabularyHeadword|quick-help-word-search/.test(runtime), 'The old character-search feature must not return.');
assert.ok(!/Google AI|google\.com|data-ai-/.test(index.slice(index.indexOf('<aside class="quick-help"'), index.indexOf('</aside>', index.indexOf('<aside class="quick-help"')))), 'Robot UI must not contain new contextual Google AI actions.');

for (const iconId of ['icon-robot', 'icon-target', 'icon-book-open', 'icon-brain', 'icon-layers', 'icon-clipboard-check', 'icon-bolt', 'icon-stopwatch', 'icon-trophy']) assert.ok(index.includes(`id="${iconId}"`), `Missing retained mock icon: ${iconId}`);
assert.ok(!/◷/.test(index), 'The obsolete mock-exam clock glyph must stay removed.');

console.log('PASS: Robot Buddy first-run, local progress and milestone UI, icon/animation/accessibility and SW cache; no usage guide, no prefix search, no v2.80 contextual AI; mock icons retained.');
