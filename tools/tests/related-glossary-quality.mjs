import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { getLearnerFacingRelatedGlossaryDefinition, isPlaceholderRelatedGlossaryDefinition } from '../../assets/js/related-glossary-quality.js';

const placeholders = [
  'Reference gloss for practice distractors.',
  ' reference gloss for a draft ',
  'TBD', 'TODO.', 'placeholder', 'definition pending',
  'unknown', 'N/A', 'not available', 'no definition',
  'generic definition for review', 'temporary definition', 'sample definition'
];
for (const value of placeholders) {
  assert.equal(isPlaceholderRelatedGlossaryDefinition(value), true, `must flag placeholder: ${value}`);
  assert.equal(getLearnerFacingRelatedGlossaryDefinition(value), '', `must not show placeholder: ${value}`);
}
const valid = [
  'A person who helps another person with work.',
  'A document requesting payment for goods or services.',
  'A person or organization that competes against another.'
];
for (const value of valid) {
  assert.equal(isPlaceholderRelatedGlossaryDefinition(value), false);
  assert.equal(getLearnerFacingRelatedGlossaryDefinition(value), value);
}
assert.equal(getLearnerFacingRelatedGlossaryDefinition(null), '');
assert.equal(getLearnerFacingRelatedGlossaryDefinition('   '), '');

const glossary = JSON.parse(await readFile(new URL('../../data/related-terms.json', import.meta.url), 'utf8'));
const placeholderRows = (glossary.terms || []).filter(row => isPlaceholderRelatedGlossaryDefinition(row.definition_en));
assert.equal(placeholderRows.length, 1, 'the v2.95.72 canonical glossary leaves only the unsupported compound placeholder (once-a-year) flagged for editorial review');
assert.ok(placeholderRows.every(row => getLearnerFacingRelatedGlossaryDefinition(row.definition_en) === ''), 'no canonical placeholder row may leak into learner-facing English text');

const app = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
assert.match(app, /import \{ getLearnerFacingRelatedGlossaryDefinition \} from '\.\/related-glossary-quality\.js\?__release=\d+\.\d+\.\d+';/);
assert.match(app, /const learnerDefinition=getLearnerFacingRelatedGlossaryDefinition\(alias\.definition_en\);/);
console.log('PASS: related glossary placeholders are suppressed from learner-facing English definitions; valid definitions remain visible.');
