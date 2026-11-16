import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const read = (relative) => fs.readFileSync(path.join(root, relative), 'utf8');
const index = read('index.html');
const app = read('assets/js/app.js');
const css = read('assets/css/app.css');

// These are the pre-v2.80, user-initiated, one-way Google AI actions restored from v2.79.
for (const id of [
  'analyzeAnswerAIButton',
  'googleSearchBackdrop',
  'googleSearchTitle',
  'googleSearchSummary',
  'googleSearchContext',
  'runGoogleAIButton',
  'closeGoogleSearch'
]) {
  assert.ok(index.includes(`id="${id}"`), `Missing legacy Google AI UI element: ${id}`);
}

for (const functionName of [
  'buildListeningAIPrompt',
  'buildGrammarAIPrompt',
  'buildReadingAIPrompt',
  'buildWordAIPrompt',
  'buildPracticeAIPrompt',
  'showAIPromptModal',
  'closeGoogleSearchPanel',
  'buildOneWayGoogleAIUrl',
  'openGoogleSearch',
  'openGoogleAIFromPanel',
  'openLookupTerm'
]) {
  assert.ok(app.includes(`function ${functionName}(`), `Missing legacy Google AI function: ${functionName}`);
}

for (const action of [
  'data-ai-word=',
  'data-ai-lesson=',
  'data-ai-reading=',
  'data-ai-listening=',
  'data-practice-review-ai'
]) {
  assert.ok(app.includes(action), `Missing legacy Google AI action: ${action}`);
}

assert.ok(app.includes("$('#analyzeAnswerAIButton').addEventListener('click'"), 'Practice answer analysis button must have its direct listener.');
assert.ok(app.includes("$('#closeGoogleSearch').addEventListener('click',closeGoogleSearchPanel)"), 'Legacy Google AI panel must be closable.');
assert.ok(app.includes("$('#runGoogleAIButton').addEventListener('click',openGoogleSearch)"), 'Legacy Google AI action must be explicit and user-triggered.');
assert.ok(app.includes("const ai=e.target.closest('[data-ai-word]')"), 'Vocabulary AI action must be delegated from the modal.');
assert.ok(app.includes("const grammarAI=e.target.closest('[data-ai-lesson]')"), 'Grammar AI action must be delegated from the modal.');
assert.ok(app.includes("const readingAI=e.target.closest('[data-ai-reading]')"), 'Reading AI action must be delegated from the modal.');
assert.ok(app.includes("const listeningAI=e.target.closest('[data-ai-listening]')"), 'Listening AI action must be delegated from the modal.');
assert.ok(app.includes("const reviewAI=e.target.closest('[data-practice-review-ai]')"), 'Practice review AI action must be delegated from the modal.');
assert.ok(app.includes("url.searchParams.set('udm','50')") && app.includes("url.searchParams.set('hl','vi')"), 'Legacy Google AI Mode must retain the known Google Search query parameters.');
assert.ok(app.includes("new URL('https://www.google.com/search')"), 'Legacy integration must remain a user-initiated external Google Search handoff, not an embedded service.');
assert.match(app, /function openGoogleSearch\(\)[\s\S]*?window\.open\(url,'_blank'\)/, 'The external Google tab may only be opened by the explicit run action.');
assert.ok(index.includes('Google AI Mode chỉ mở khi bạn chủ động chọn'), 'Privacy settings must disclose the explicit external handoff.');
assert.ok(css.includes('.google-search-backdrop') && css.includes('.ai-oneway-panel') && css.includes('.feedback-ai-row'), 'Legacy modal and action styling must be present.');

// Keep the v2.80 floating assistant's AI follow-up flow removed. The local Quick Help itself stays offline-only.
for (const removed of [
  'assistantAskGoogleAI',
  'askAssistantWithGoogleAI',
  'buildAssistantCurrentPrompt',
  'copyGoogleAIPrompt',
  'copyGoogleAIPromptButton',
  'googleSearchTransferNote',
  'runGoogleAIButtonLabel',
  'data-quick-help-ask-google',
  'quick-help-ask-google'
]) {
  assert.ok(![index, app, css].join('\n').includes(removed), `The v2.80 assistant-specific AI feature must remain removed: ${removed}`);
}
const quickHelpStart = index.indexOf('<aside class="quick-help"');
const quickHelpEnd = index.indexOf('</aside>', quickHelpStart);
const quickHelpMarkup = index.slice(quickHelpStart, quickHelpEnd);
assert.ok(!/Google AI|google\.com|data-ai-/i.test(quickHelpMarkup), 'Quick Help must remain local-only; only the older per-feature buttons may invoke Google AI.');

console.log('PASS: v2.79 legacy Google AI actions restored (vocabulary, practice answer/review, grammar, reading, listening); v2.80 assistant-specific AI handoff remains removed; Quick Help remains local-only.');
