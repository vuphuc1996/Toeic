import assert from 'node:assert/strict';
import { recordAlphabetSoundPractice, summarizeAlphabetSoundProgress } from '../../assets/js/alphabet-sound-progress.js';

let progress = { schemaVersion: 1, letters: {} };
progress = recordAlphabetSoundPractice(progress, 'a', 'letterName', 100);
progress = recordAlphabetSoundPractice(progress, 'A', 'exampleWord', 200);
progress = recordAlphabetSoundPractice(progress, 'B', 'exampleWord', 300);
let summary = summarizeAlphabetSoundProgress(progress, 26);
assert.deepEqual(summary, { expectedLetters: 26, practicedLetters: 2, completedPairs: 1, totalPlays: 3 });
progress = recordAlphabetSoundPractice(progress, 'A', 'letterName', 400);
summary = summarizeAlphabetSoundProgress(progress, 26);
assert.equal(summary.completedPairs, 1);
assert.equal(progress.letters.A.letterName.count, 2);
assert.equal(progress.letters.A.letterName.firstAt, 100);
assert.equal(progress.letters.A.letterName.lastAt, 400);
const unchanged = recordAlphabetSoundPractice(progress, 'AA', 'letterName', 500);
assert.deepEqual(unchanged, progress);
assert.deepEqual(recordAlphabetSoundPractice(progress, 'C', 'invalid', 600), progress);
console.log('Alphabet sound progress PASS');
