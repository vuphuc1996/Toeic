import assert from 'node:assert/strict';
import fs from 'node:fs';

const root = new URL('../../', import.meta.url);
const read = path => fs.readFileSync(new URL(path, root), 'utf8');
const html = read('index.html');
const app = read('assets/js/app.js');
const css = read('assets/css/app.css');
const ids = [...html.matchAll(/\bid=["']([^"']+)["']/g)].map(m => m[1]);
assert.equal(ids.length, new Set(ids).size, 'all HTML IDs must be unique');
for (const id of ['flashTopicGrid','flashSession','flashQuiz','flashResult','practiceModeGrid','weakWordList','newQuestionButton','learningFocusBackdrop','learningFocusTitle','learningFocusSubtitle','learningFocusClose','learningFocusContent']) {
  assert.ok(ids.includes(id), `missing #${id}`);
}
assert.match(html, /<section class="panel quiz-panel" hidden>/, 'practice questions must not be visible on the dashboard before Start');
for (const mode of ['random','word-to-meaning','meaning-to-word','missing','pos','synonym','antonym','verb']) {
  assert.ok(html.includes(`data-practice-mode="${mode}"`), `missing practice mode ${mode}`);
}
assert.match(app, /function openLearningFocus\(/);
assert.match(app, /function closeLearningFocus\(/);
assert.match(app, /function startPracticeFocus\(/);
assert.match(app, /nextQuestion\(mode\)\.then\(started=>\{/,'Start always generates a question in the mode selected on the dashboard');
assert.match(app, /function advanceFlashCard\(/);
assert.match(app, /ss\.flipped=true;renderFlashCard\(\);return;/, 'first flashcard tap must reveal details');
assert.match(app, /ss\.index\+\+;ss\.flipped=false/, 'second flashcard tap must advance');
assert.match(app, /elements:\['#flashSession','#flashQuiz','#flashResult'\]/, 'learning and quick-check views share the focus layer');
assert.match(app, /elements:\[panel\]/, 'practice question panel must move into focus workspace');
assert.match(app, /if\(kind==='practice'\)[\s\S]*panel\.hidden=true/, 'closing practice must restore dashboard');
assert.match(app, /if\(kind==='flashcards'\)[\s\S]*renderFlashHome\(\)/, 'closing flashcard session must return to topic selection');
assert.match(app, /is-learning-detail/);
for (const fn of ['openGrammarLesson','openReadingDetail','openListeningDetail']) {
  const at = app.indexOf(`function ${fn}(`);
  assert.ok(at >= 0, `missing ${fn}`);
  const body = app.slice(at, app.indexOf('\n}', at) > at ? app.indexOf('\n}', at) : at + 5000);
  assert.match(body, /is-learning-detail/, `${fn} should use the shared focus detail presentation`);
}
assert.match(css, /\.learning-focus-backdrop\{position:fixed;inset:0;/);
assert.match(css, /\.learning-focus-dialog\{[^}]*max-height:min\(94dvh/);
assert.match(css, /\.learning-focus-content\{[^}]*overflow:auto/);
assert.match(css, /@media\(max-width:640px\)[\s\S]*\.learning-focus-dialog/);
assert.match(css, /@media\(prefers-reduced-motion:reduce\)/);
assert.match(css, /body\.has-learning-focus\{overflow:hidden\}/);
assert.match(app, /indexedDB\.open\(DB_NAME, 1\)/, 'personal IndexedDB schema version remains unchanged');
assert.doesNotMatch(app, /indexedDB\.open\(DB_NAME,\s*[2-9]/, 'no personal IndexedDB migration is introduced');

const batch = JSON.parse(read('data/vocabulary/batch-006.json'));
assert.equal(batch.count, 43);
assert.equal(batch.words.length, 43);
assert.match(batch.editorialStatus, /pending/i);
const canonical = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').flatMap(letter => JSON.parse(read(`data/vocabulary/${letter}.json`)).words || []);
const words = new Set(canonical.map(item => item.word.toLowerCase()));
for (const item of batch.words) assert.ok(words.has(item.word.toLowerCase()), `Batch 006 word not in A-Z vocabulary: ${item.word}`);
assert.equal(canonical.length, new Set(canonical.map(item => item.id)).size, 'canonical vocabulary IDs must remain unique');

console.log(`Learning focus workspace PASS: ${ids.length} unique IDs, flashcard/review flow, shared modal detail styling, responsive rules, unchanged IndexedDB v1, and 43 Batch 006 vocabulary additions (${canonical.length} canonical headwords).`);
