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

// The floating assistant and contextual Google AI handoff introduced in v2.80 must stay absent.
for (const obsolete of [
  'id="learningAssistant"', 'id="assistantLauncher"', 'id="assistantPanel"',
  'id="assistantAskGoogle"', 'id="copyGoogleAIPromptButton"',
  'toggleLearningAssistant', 'buildAssistantCurrentPrompt', 'askAssistantWithGoogleAI',
  'assets/js/learning-assistant.js', 'assistant-followup', 'assistant-context-prompt',
  'data-quick-help-ask-google', 'quick-help-ask-google'
]) assert.ok(!runtime.includes(obsolete), `v2.80 floating AI artifact must remain removed: ${obsolete}`);

// Word-prefix suggestions and masked-letter completion were explicitly rejected as well.
for (const obsolete of [
  'quickHelpWordSearch', 'quickHelpWordSuggestions', 'quickHelpWordChallenge',
  'findVocabularyPrefixMatches', 'maskVocabularyHeadword', 'validateVocabularyCompletion',
  'renderQuickHelpSuggestions', 'renderQuickHelpChallenge', 'verifyQuickHelpChallenge',
  'quick-help-word-search', 'quick-help-letter-slot', 'assets/js/quick-help.js'
]) assert.ok(!runtime.includes(obsolete), `v2.80 word-search artifact must remain removed: ${obsolete}`);

// Non-AI guide and Placement remain available.
for (const id of ['quickHelpLauncher', 'quickHelpPanel', 'quickHelpGuide']) assert.ok(index.includes(`id="${id}"`), `Local guide UI must remain: ${id}`);
assert.ok(app.includes('startPlacementDiagnostic'), 'Placement Diagnostic remains available.');

// Keep the v2.80 mock-exam icon refresh.
for (const iconId of ['icon-clipboard-check', 'icon-bolt', 'icon-stopwatch', 'icon-trophy']) assert.ok(index.includes(`id="${iconId}"`), `Mock icon refresh must remain: ${iconId}`);
assert.ok(!/◷/.test(index), 'The obsolete clock glyph must not return.');

console.log('PASS: v2.80 floating AI and Quick Help word-search removed; local guide/Placement and mock-exam icons retained.');
