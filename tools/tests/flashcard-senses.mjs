import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { renderAdditionalFlashSenses } from '../../assets/js/flashcard-senses.js';

const manifest = JSON.parse(await readFile(new URL('../../data/manifest.json', import.meta.url), 'utf8'));
async function findWord(headword) {
  for (const letter of manifest.letters) {
    const file = JSON.parse(await readFile(new URL(`../../${letter.file.replace(/^\.\//, '')}`, import.meta.url), 'utf8'));
    const word = file.words.find(item => item.word === headword && item.senses?.length > 1);
    if (word) return word;
  }
  return null;
}
const word = await findWord('address');
assert.ok(word, 'multi-sense fixture exists in canonical vocabulary');
const markup = renderAdditionalFlashSenses(word, pos => ({ n: 'Danh từ', v: 'Động từ' }[pos] || 'Từ loại'));
assert.match(markup, /OTHER MEANINGS · 1/);
assert.match(markup, /Nghĩa 2 · Động từ/);
assert.match(markup, /giải quyết|xử lý/i);
const linkedExample = word.examples.find(example => example.sense_index === 1);
assert.ok(linkedExample, 'extra sense has a linked example');
assert.ok(markup.includes(linkedExample.en));
assert.ok(markup.includes(linkedExample.vi));

const charge = await findWord('charge');
assert.ok(charge, 'charge has multiple dictionary senses');
const chargeMarkup = renderAdditionalFlashSenses(charge, pos => ({ n: 'Danh từ', v: 'Động từ' }[pos] || 'Từ loại'));
assert.match(chargeMarkup, /OTHER MEANINGS · 2/);
for (const example of charge.examples.filter(row => row.sense_index > 0)) {
  assert.ok(chargeMarkup.includes(example.en), `charge sense ${example.sense_index} example is rendered`);
  assert.ok(chargeMarkup.includes(example.vi), `charge sense ${example.sense_index} translation is rendered`);
}

const offer = await findWord('offer');
assert.ok(offer, 'offer has noun and two verb senses');
const offerMarkup = renderAdditionalFlashSenses(offer, pos => ({ n: 'Danh từ', v: 'Động từ' }[pos] || 'Từ loại'));
assert.match(offerMarkup, /OTHER MEANINGS · 2/);
assert.ok(offerMarkup.includes('cung cấp'));
assert.equal(renderAdditionalFlashSenses({ word: 'single', senses: [{ meaning_vi: 'một nghĩa' }] }), '');

const hostile = renderAdditionalFlashSenses({
  word: '<img src=x onerror=alert(1)>',
  senses: [{ meaning_vi: 'primary' }, { meaning_vi: '<script>alert(1)</script>', pos: 'n' }],
  examples: [{ sense_index: 1, en: '<svg onload=alert(1)>', vi: '<b>unsafe</b>' }],
}, () => '<b>POS</b>');
assert.ok(!hostile.includes('<script>'));
assert.ok(!hostile.includes('<svg'));
assert.ok(!hostile.includes('<b>'));
assert.match(hostile, /&lt;script&gt;/);
assert.match(hostile, /&lt;svg/);
assert.match(hostile, /&lt;b&gt;POS&lt;\/b&gt;/);
console.log('PASS: multi-sense Flashcard helper renders only sense-linked examples, escapes HTML, and returns empty markup for single-sense words.');
