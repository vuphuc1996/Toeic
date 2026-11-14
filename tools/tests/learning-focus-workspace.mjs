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
assert.match(app, /function openLearningDetail\(/, 'Grammar, Reading and Listening share one focus-shell entry point');
assert.match(app, /openLearningDetail\(\{title:lesson\.title/, 'Grammar uses the shared learning shell');
assert.match(app, /openLearningDetail\(\{title:reading\.title/, 'Reading uses the shared learning shell');
assert.match(app, /openLearningDetail\(\{title:item\.title/, 'Listening uses the shared learning shell');
assert.doesNotMatch(app, /classList\.add\('is-learning-detail'\)/, 'learning detail no longer opens a separate modal shell');
assert.match(app, /flashcard-details-panel/, 'Flashcard details expand below the word panel');
assert.match(app, /flashcard-front-panel/, 'Flashcard word stays in the upper panel');
for (const [fn,needle] of [['openGrammarLesson','openLearningDetail({title:lesson.title'],['openReadingDetail','openLearningDetail({title:reading.title'],['openListeningDetail','openLearningDetail({title:item.title']]) {
  const at = app.indexOf(`function ${fn}(`);
  assert.ok(at >= 0, `missing ${fn}`);
  const end = app.indexOf('\n}', at);
  const body = app.slice(at, end > at ? end : at + 5000);
  assert.ok(body.includes(needle), `${fn} should use the shared focus detail presentation`);
}
assert.match(css, /\.learning-focus-backdrop\{position:fixed;inset:0;/);
assert.match(css, /\.learning-focus-dialog\{[^}]*max-height:min\(94dvh/);
assert.match(css, /\.learning-focus-content\{[^}]*overflow:auto/);
assert.match(css, /\.learning-focus-content>\.modal-content\{[^}]*overflow:visible/, 'detail body does not create a nested scrolling viewport');
assert.match(css, /\.flashcard-details-panel/);
assert.match(css, /\.flashcard-front-panel/);
assert.doesNotMatch(css, /\.flashcard-content|\.flashcard-no-art/, 'legacy Flashcard inner-scroll face styles must not remain active');
assert.match(css, /\.learning-focus-content\.*/);
assert.match(css, /@media\(max-width:640px\)[\s\S]*\.learning-focus-dialog/);
assert.match(css, /@media\(prefers-reduced-motion:reduce\)/);
assert.match(css, /body\.has-learning-focus\{overflow:hidden\}/);
assert.match(app, /indexedDB\.open\(DB_NAME, 1\)/, 'personal IndexedDB schema version remains unchanged');
assert.doesNotMatch(app, /indexedDB\.open\(DB_NAME,\s*[2-9]/, 'no personal IndexedDB migration is introduced');

const batch = JSON.parse(read('data/vocabulary/batch-006.json'));
const batch018 = JSON.parse(read('data/vocabulary/batch-007.json'));
assert.equal(batch.count, 43);
assert.equal(batch.words.length, 43);
assert.equal(batch018.words.length, 8);
assert.match(batch.editorialStatus, /pending/i);
const canonical = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').flatMap(letter => JSON.parse(read(`data/vocabulary/${letter}.json`)).words || []);
const words = new Set(canonical.map(item => item.word.toLowerCase()));
assert.ok(batch018.words.every(w => canonical.some(c => c.id === w.id)));
assert.ok(batch018.words.every(w => words.has(w.word.toLowerCase())));
for (const item of batch.words) assert.ok(words.has(item.word.toLowerCase()), `Batch 006 word not in A-Z vocabulary: ${item.word}`);
assert.equal(canonical.length, new Set(canonical.map(item => item.id)).size, 'canonical vocabulary IDs must remain unique');

console.log(`Learning focus workspace PASS: ${ids.length} unique IDs, flashcard/review flow, shared modal detail styling, responsive rules, unchanged IndexedDB v1, and Batch 006/007 vocabulary additions (${canonical.length} canonical headwords).`);
