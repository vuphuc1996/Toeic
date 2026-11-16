import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  findVocabularyPrefixMatches,
  maskVocabularyHeadword,
  normalizeVocabularyPrefix,
  validateVocabularyCompletion
} from '../../assets/js/quick-help.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const words = letters.flatMap(letter => {
  const file = path.join(root, 'data', 'vocabulary', `${letter}.json`);
  const parsed = JSON.parse(fs.readFileSync(file, 'utf8'));
  return Array.isArray(parsed) ? parsed : (parsed.words || []);
});

assert.equal(words.length, 1137, 'Quick Help must use the canonical current vocabulary data.');
assert.equal(normalizeVocabularyPrefix(' HÓ! '), 'ho', 'Prefix normalization should be case/diacritic/punctuation safe.');
assert.deepEqual(findVocabularyPrefixMatches(words, 'h', 6), [], 'A single letter should not flood the panel.');
const matches = findVocabularyPrefixMatches(words, 'ho', 6);
assert.deepEqual(matches.map(item => item.word.toLowerCase()), ['hospitality','host','hotline','hour','housekeeping']);
for (const absent of ['house','horse','home','hold']) assert.equal(words.some(item => item.word.toLowerCase() === absent), false, `${absent} must not be fabricated when absent from the dataset.`);
assert.ok(matches.every(item => item.word.toLowerCase().startsWith('ho')));
assert.deepEqual(matches.map(item => item.word.toLowerCase()), [...matches.map(item => item.word.toLowerCase())].sort((a,b)=>a.localeCompare(b)));
assert.equal(maskVocabularyHeadword('housekeeping', 'ho'), 'ho••••••••••');
assert.equal(maskVocabularyHeadword('housekeeping', 'xx'), '');
assert.equal(validateVocabularyCompletion('housekeeping', 'ho', 'usekeeping'), true);
assert.equal(validateVocabularyCompletion('housekeeping', 'ho', 'usekeepin'), false);
assert.equal(validateVocabularyCompletion('housekeeping', 'xx', 'usekeeping'), false);
assert.equal(validateVocabularyCompletion('housekeeping', 'ho', 'usekeepin!'), false);
assert.ok(findVocabularyPrefixMatches(words, 'ho', 99).length <= 12);

const index = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const app = fs.readFileSync(path.join(root, 'assets', 'js', 'app.js'), 'utf8');
const sw = fs.readFileSync(path.join(root, 'sw.js'), 'utf8');
const css = fs.readFileSync(path.join(root, 'assets', 'css', 'app.css'), 'utf8');
const runtimeSources = [index, app, sw, css, fs.readFileSync(path.join(root, 'assets', 'js', 'quick-help.js'), 'utf8')].join('\n');
for (const id of ['quickHelpLauncher','quickHelpPanel','quickHelpGuide','quickHelpWordSearch','quickHelpWordSuggestions','quickHelpWordChallenge']) assert.ok(index.includes(`id="${id}"`), `Missing local Quick Help UI ${id}`);
for (const handler of ['toggleQuickHelp','renderQuickHelpSuggestions','renderQuickHelpChallenge','verifyQuickHelpChallenge','startPlacementDiagnostic']) assert.ok(app.includes(handler), `Missing local Quick Help behavior ${handler}`);
assert.ok(sw.includes('./assets/js/quick-help.js'), 'The local helper must be precached for offline use.');
assert.ok(/@media\(max-width:820px\)[\s\S]*?\.quick-help-panel/.test(css), 'Quick Help must have a compact mobile layout.');
assert.ok(app.includes("page==='mock'&&state.mockExam?.status==='active'"), 'The helper launcher must not obstruct a timed mock exam.');
assert.ok(app.includes('word.word.toLowerCase()===normalizeVocabularyPrefix(clean)'), 'An exact headword query must open the dictionary detail directly.');
assert.ok(app.includes('setQuickHelpOpen(false);}') , 'Navigating away must close the panel.');
assert.ok(app.includes("if($('#quickHelpPanel')&&!$('#quickHelpPanel').hidden)setQuickHelpOpen(false)"), 'Escape must close Quick Help.');
assert.ok(app.includes('if(page!==state.activePage){state.quickHelpSelectedWordId=null;state.quickHelpCompletedWordId=null;setQuickHelpOpen(false);}'), 'Navigation must clear the word challenge and close the panel.');
for (const id of ['icon-bolt','icon-stopwatch','icon-trophy']) assert.ok(index.includes(`id=\"${id}\"`), `Missing mock mode icon ${id}`);
assert.ok(index.includes('<symbol id=\"icon-layers\"'), 'The flashcard guide must reference a defined SVG symbol.');
for (const page of ['dashboard','dictionary','flashcards','foundation','practice','grammar','mock','reading','listening','data','settings']) assert.ok(index.includes(`data-quick-help-navigate="${page}"`), `The guide is missing ${page}`);
assert.ok(!/◷/.test(index), 'The obsolete clock glyph must be removed from the product UI.');
const quickHelpStart = index.indexOf('<aside class="quick-help"');
const quickHelpEnd = index.indexOf('</aside>', quickHelpStart);
assert.ok(quickHelpStart >= 0 && quickHelpEnd > quickHelpStart, 'The local Quick Help region must exist.');
const quickHelpMarkup = index.slice(quickHelpStart, quickHelpEnd);
assert.ok(!/Google AI|google\.com|data-ai-|AIPrompt/i.test(quickHelpMarkup), 'The v2.80 floating assistant Google AI/contextual handoff must stay removed from Quick Help.');
assert.ok(!/assistantAskGoogleAI|buildAssistantCurrentPrompt|copyGoogleAIPromptButton|data-quick-help-ask-google|quick-help-ask-google/i.test(runtimeSources), 'The v2.80 assistant-specific AI handoff must not be restored.');
assert.ok(app.includes('findVocabularyPrefixMatches') && app.includes('validateVocabularyCompletion'), 'Quick Help must continue to use the local vocabulary matching/completion engine.');
console.log('PASS: local Quick Help, real vocabulary matches, masked completion, answer validation, navigation, responsive/offline shell; legacy Google AI is tested separately and is not embedded in Quick Help.');
