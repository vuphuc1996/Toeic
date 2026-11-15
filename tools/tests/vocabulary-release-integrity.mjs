import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { detectLegacyReleaseAdditionRepair } from '../../assets/js/vocabulary-release-integrity.js';

const manifest = JSON.parse(await readFile(new URL('../../data/manifest.json', import.meta.url), 'utf8'));
const app = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const sw = await readFile(new URL('../../sw.js', import.meta.url), 'utf8');
const html = await readFile(new URL('../../index.html', import.meta.url), 'utf8');
const batch008 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-008.json', import.meta.url), 'utf8'));

assert.equal(manifest.version, '2.60.0');
assert.equal(manifest.totalWords, 992);
assert.equal(manifest.previousReleaseTotalWords, 979);
assert.equal(manifest.releaseAdditionIds.length, 13);
assert.deepEqual(manifest.releaseAdditionIds, batch008.words.map(word => word.id), 'release delta IDs match the 13-word 979→992 addition batch');
assert.equal(manifest.letters.length, 26);
let total = 0;
const ids = new Set();
const headwords = new Set();
const baseWords = [];
for (const entry of manifest.letters) {
  const file = JSON.parse(await readFile(new URL(`../../${entry.file.replace(/^\.\//, '')}`, import.meta.url), 'utf8'));
  assert.equal(file.letter, entry.letter);
  assert.equal(file.words.length, entry.count, `${entry.letter} count matches manifest`);
  total += file.words.length;
  for (const word of file.words) {
    baseWords.push(word);
    assert.ok(!ids.has(word.id), `duplicate vocabulary ID ${word.id}`);
    assert.ok(!headwords.has(String(word.word).trim().toLocaleLowerCase('en-US')), `duplicate headword ${word.word}`);
    ids.add(word.id);
    headwords.add(String(word.word).trim().toLocaleLowerCase('en-US'));
  }
}
assert.equal(total, manifest.totalWords);
assert.equal(ids.size, 992);
const additionRepair = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: manifest.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !manifest.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseAdditionIds: manifest.releaseAdditionIds,
  previousTotalWords: manifest.previousReleaseTotalWords,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair.length, 13, 'the exact legacy 979-word snapshot restores only the 13 known release additions');
assert.deepEqual(detectLegacyReleaseAdditionRepair({
  deletedBaseIds: manifest.releaseAdditionIds,
  legacyRecords: [], baseWords,
  releaseAdditionIds: manifest.releaseAdditionIds,
  previousTotalWords: 979, currentTotalWords: 992
}), [], 'missing or incomplete legacy snapshot must not trigger automatic repair');
assert.match(app, /const APP_RELEASE_VERSION = '2\.60\.0'/);
assert.match(app, /detectLegacyReleaseAdditionRepair/);
assert.match(app, /personal\.deletedBaseIds=\[\]/);
assert.match(app, /searchParams\.set\('__release', version\)/);
assert.match(app, /payload\.words\.length!==entry\.count/);
assert.match(app, /loaded\.length!==manifest\.totalWords/);
assert.match(app, /navigator\.serviceWorker\.addEventListener\('controllerchange'/);
assert.match(app, /registration\.update\(\)/);
assert.match(sw, /const VERSION = '2\.60\.0'/);
assert.match(sw, /cacheUrl\.searchParams\.delete\('__release'\)/);
assert.match(html, /id="metricWordsStatus"/);
console.log('Vocabulary release integrity: PASS (26 files, 992 records, 979→992 legacy migration repair, unique IDs/headwords, cache-bust and PWA update guards).');
