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

// Keep the non-AI help guide and existing placement diagnostic.
for (const id of ['quickHelpLauncher', 'quickHelpPanel', 'quickHelpGuide', 'quickHelpClose']) {
  assert.ok(index.includes(`id="${id}"`), `Missing local help UI: ${id}`);
}
for (const handler of ['toggleQuickHelp', 'renderQuickHelpGuide', 'startPlacementDiagnostic']) {
  assert.ok(app.includes(handler), `Missing local help behavior: ${handler}`);
}
for (const page of ['dashboard','dictionary','flashcards','foundation','practice','grammar','mock','reading','listening','data','settings']) {
  assert.ok(index.includes(`data-quick-help-navigate="${page}"`), `The guide is missing ${page}`);
}
assert.ok(sw.includes('./assets/js/app.js'), 'The app shell must remain available offline.');
assert.ok(!sw.includes('./assets/js/quick-help.js'), 'The removed word-search module must not remain in the Service Worker cache lists.');
assert.ok(/@media\(max-width:820px\)[\s\S]*?\.quick-help-panel/.test(css), 'Quick Help must retain a compact mobile layout.');
assert.ok(app.includes("page==='mock'&&state.mockExam?.status==='active'"), 'Quick Help must not obstruct a timed mock exam.');
assert.ok(app.includes("$('#quickHelp')?.addEventListener('click'"), 'Guide and placement actions must remain delegated.');

// Explicitly remove the entire v2.80 word-prefix / masked-letter feature.
for (const id of ['quickHelpWordSearch','quickHelpWordSuggestions','quickHelpWordChallenge']) {
  assert.ok(!index.includes(`id="${id}"`), `Removed word-search UI must not return: ${id}`);
}
for (const symbol of [
  'findVocabularyPrefixMatches', 'maskVocabularyHeadword', 'validateVocabularyCompletion',
  'renderQuickHelpSuggestions', 'renderQuickHelpChallenge', 'verifyQuickHelpChallenge',
  'data-quick-help-letter', 'data-quick-help-select-word', 'data-quick-help-check-word',
  'quick-help-word-search', 'quick-help-letter-slot', 'quick-help-word-challenge'
]) {
  assert.ok(!runtime.includes(symbol), `Removed character-search implementation must not return: ${symbol}`);
}
assert.ok(!fs.existsSync(path.join(root, 'assets/js/quick-help.js')), 'The dedicated word-search module must be deleted.');
assert.ok(!/nhập vài chữ cái đầu|điền chữ để tìm từ|chữ cái còn thiếu/i.test(index), 'Help copy must not advertise the removed word completion feature.');

// The exam icon refresh from v2.80 remains part of the product.
for (const iconId of ['icon-clipboard-check', 'icon-bolt', 'icon-stopwatch', 'icon-trophy']) assert.ok(index.includes(`id="${iconId}"`), `Missing retained mock icon: ${iconId}`);
assert.ok(!/◷/.test(index), 'The obsolete mock-exam clock glyph must remain removed.');

console.log('PASS: local Quick Help guide and Placement remain; all v2.80 prefix search/masked-letter completion code, UI, CSS, module and cache references are removed; mock icons remain.');
