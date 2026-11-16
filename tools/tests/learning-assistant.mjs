import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  findAssistantVocabularyMatches,
  maskAssistantHeadword,
  normalizeAssistantPrefix,
  validateAssistantWordCompletion
} from '../../assets/js/learning-assistant.js';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const words = letters.flatMap(letter => {
  const file = path.join(root, 'data', 'vocabulary', `${letter}.json`);
  const parsed = JSON.parse(fs.readFileSync(file, 'utf8'));
  return Array.isArray(parsed) ? parsed : (parsed.words || []);
});

assert.equal(words.length, 1137, 'The assistant must use the canonical current vocabulary data.');
assert.equal(normalizeAssistantPrefix(' HÓ! '), 'ho', 'Prefix normalization should be case/diacritic/punctuation safe.');
assert.deepEqual(findAssistantVocabularyMatches(words, 'h', 6), [], 'A single letter should not flood the panel.');
const matches = findAssistantVocabularyMatches(words, 'ho', 6);
assert.ok(matches.length > 0, 'The current dictionary should provide suggestions for the example prefix ho.');
assert.deepEqual(matches.map(item => item.word.toLowerCase()), ['hospitality','host','hotline','hour','housekeeping'], 'The ho example must only return the actual canonical headwords.');
for (const absent of ['house','horse','home','hold']) assert.equal(words.some(item => item.word.toLowerCase() === absent), false, `${absent} must not be fabricated when absent from the current dataset.`);
assert.ok(matches.every(item => item.word.toLowerCase().startsWith('ho')), 'Suggestions must match the typed prefix.');
assert.deepEqual(matches.map(item => item.word.toLowerCase()), [...matches.map(item => item.word.toLowerCase())].sort((a,b)=>a.localeCompare(b)), 'Suggestions should be predictably ordered.');
assert.equal(maskAssistantHeadword('housekeeping', 'ho'), 'ho••••••••••');
assert.equal(maskAssistantHeadword('housekeeping', 'xx'), '', 'A non-matching prefix must not mask unrelated words.');
assert.equal(validateAssistantWordCompletion('housekeeping', 'ho', 'usekeeping'), true);
assert.equal(validateAssistantWordCompletion('housekeeping', 'ho', 'usekeepin'), false);
assert.equal(validateAssistantWordCompletion('housekeeping', 'xx', 'usekeeping'), false);
assert.equal(validateAssistantWordCompletion('housekeeping', 'ho', 'usekeepin!'), false);
assert.ok(findAssistantVocabularyMatches(words, 'ho', 99).length <= 12, 'Suggestion count must remain bounded.');

const index = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const app = fs.readFileSync(path.join(root, 'assets', 'js', 'app.js'), 'utf8');
const sw = fs.readFileSync(path.join(root, 'sw.js'), 'utf8');
const css = fs.readFileSync(path.join(root, 'assets', 'css', 'app.css'), 'utf8');
for (const id of ['assistantLauncher','assistantPanel','assistantGuide','assistantWordSearch','assistantWordSuggestions','assistantWordChallenge','assistantAskGoogle','copyGoogleAIPromptButton']) assert.ok(index.includes(`id="${id}"`), `Missing assistant UI ${id}`);
for (const handler of ['toggleLearningAssistant','renderAssistantSuggestions','renderAssistantChallenge','verifyAssistantChallenge','startPlacementDiagnostic','buildAssistantCurrentPrompt','askAssistantWithGoogleAI']) assert.ok(app.includes(handler), `Missing integrated assistant behavior ${handler}`);
assert.ok(sw.includes('./assets/js/learning-assistant.js'), 'Assistant helper must be precached for offline use.');
assert.ok(/@media\(max-width:480px\)[\s\S]*?\.assistant-panel/.test(css), 'Assistant must have a compact mobile layout.');
assert.ok(app.includes("page==='mock'&&state.mockExam?.status==='active'"), 'Assistant launcher must not obstruct a timed mock exam.');
assert.ok(app.includes('word.word.toLowerCase()===normalizeAssistantPrefix(clean)'), 'An exact headword query must open its dictionary detail instead of showing a zero-slot challenge.');
assert.ok(app.includes('Sao chép toàn bộ prompt & mở Google AI'), 'Oversized prompts must retain all content through clipboard transfer instead of being truncated.');
assert.ok(app.includes('TOÀN BỘ NỘI DUNG NGỮ CẢNH ĐANG MỞ'), 'Context prompt must preserve the complete active content.');
assert.ok(app.includes('setLearningAssistantOpen(false);}') , 'Navigating away must close the floating panel to avoid obstructing the next page.');
assert.ok(app.includes("else if($('#assistantPanel')&&!$('#assistantPanel').hidden)setLearningAssistantOpen(false)"), 'Escape must close the assistant panel.');
assert.ok(app.includes('if(page!==state.activePage){state.assistantSelectedWordId=null;state.assistantCompletedWordId=null;setLearningAssistantOpen(false);}'), 'A completed vocabulary challenge must not leak into another page prompt and the panel closes on navigation.');
assert.ok(index.includes('icon-bolt') && index.includes('icon-stopwatch') && index.includes('icon-trophy'), 'Mock modes must use matching visual icons instead of clock glyphs.');
assert.ok(index.includes('<symbol id=\"icon-layers\"'), 'Flashcard guide must reference a defined SVG symbol.');
for (const page of ['dashboard','dictionary','flashcards','practice','grammar','mock','reading','listening','data','settings']) assert.ok(index.includes(`data-assistant-navigate=\"${page}\"`), `Assistant guide is missing ${page}`);
assert.ok(!/◷/.test(index), 'The obsolete clock glyph must be removed from the product UI.');
console.log('PASS: learning assistant vocabulary matching, masked completion, answer validation, UI wiring, offline cache and responsive layout.');
