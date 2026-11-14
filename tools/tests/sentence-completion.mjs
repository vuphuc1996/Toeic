import assert from 'node:assert/strict';
import fs from 'node:fs';
import { chooseSentenceCompletionQuestion, validateSentenceCompletionBank } from '../../assets/js/sentence-completion.js';

const root = new URL('../../', import.meta.url);
const bank = JSON.parse(fs.readFileSync(new URL('data/practice/part5-sentence-completion.json', root), 'utf8'));
const words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').flatMap(letter => {
  const data = JSON.parse(fs.readFileSync(new URL(`data/vocabulary/${letter}.json`, root), 'utf8'));
  return data.words || [];
});

assert.deepEqual(validateSentenceCompletionBank(bank.questions, words), [], 'authored bank passes runtime integrity validation');
assert.equal(bank.questions.length, 80, 'the bank contains the core and grammar-expansion question sets');
assert.equal(bank.questions.filter(item => item.editorialBatch === '016').length, 45, 'Batch 016 contains 45 questions');
assert.ok(new Set(bank.questions.map(item => item.grammarCategory)).size >= 10, 'the bank covers multiple grammar groups');
const question = chooseSentenceCompletionQuestion(bank.questions, words, {}, [], () => 0);
assert.ok(question, 'a Part 5 question is selected');
assert.equal(question.mode, 'sentence-completion');
assert.equal(question.choices.length, 4);
assert.equal(new Set(question.choices.map(x => x.toLowerCase())).size, 4);
assert.equal(question.sentence.match(/_____/g)?.length, 1);
assert.ok(question.choices.includes(question.accepted[0]), 'the answer remains among shuffled choices');
const answerIndex = question.choices.indexOf(question.accepted[0]);
assert.match(question.optionExplanations[answerIndex], /^Đúng:/, 'option explanations remain aligned after shuffle');
assert.ok(question.grammarPoint && question.grammarCategory && question.translationVi && question.singleAnswerReason);

// Force each record through the selector once to verify every keyed option keeps its own explanation after shuffle.
for (const item of bank.questions) {
  const seenExceptItem = bank.questions.filter(candidate => candidate.id !== item.id).map(candidate => candidate.id);
  const selected = chooseSentenceCompletionQuestion(bank.questions, words, {}, seenExceptItem, () => 0.37);
  assert.equal(selected.id, item.id, `selector should isolate ${item.id}`);
  const keyedIndex = selected.choices.indexOf(selected.accepted[0]);
  assert.ok(keyedIndex >= 0, `${item.id} key should survive shuffle`);
  assert.match(selected.optionExplanations[keyedIndex], /^Đúng:/, `${item.id} correct explanation should follow its key`);
}

const seen = bank.questions.map(item => item.id);
const fallback = chooseSentenceCompletionQuestion(bank.questions, words, {}, seen, () => 0);
assert.ok(fallback, 'the selector cycles again after all unique Part 5 questions have been seen');
const unrelatedVocabularyHistory = [bank.questions[0].wordId];
const isolated = chooseSentenceCompletionQuestion(bank.questions, words, {}, unrelatedVocabularyHistory, () => 0);
assert.ok(isolated, 'Part 5 cycling state is independent from vocabulary-mode seen-word IDs');
assert.equal(isolated.id, bank.questions[0].id, 'a vocabulary word-ID must not mark its linked Part 5 question as seen');

const corrupted = structuredClone(bank.questions[0]);
corrupted.sentence = 'This sentence has no gap.';
assert.ok(validateSentenceCompletionBank([corrupted], words).some(error => error.includes('exactly one blank')));

console.log('Sentence completion PASS: curated bank validation, canonical word links, one blank, four choices, shuffle/explanation alignment, and seen-item cycling.');
