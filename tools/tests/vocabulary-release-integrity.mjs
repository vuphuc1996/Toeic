import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { detectLegacyReleaseAdditionRepair } from '../../assets/js/vocabulary-release-integrity.js';

const manifest = JSON.parse(await readFile(new URL('../../data/manifest.json', import.meta.url), 'utf8'));
const app = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const sw = await readFile(new URL('../../sw.js', import.meta.url), 'utf8');
const html = await readFile(new URL('../../index.html', import.meta.url), 'utf8');
const batch008 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-008.json', import.meta.url), 'utf8'));
const batch009 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-009.json', import.meta.url), 'utf8'));

assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
assert.equal(manifest.totalWords, 1026);
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
assert.equal(ids.size, 1026);
assert.equal(batch009.words.length, 34);
assert.ok(batch009.words.every(word => ids.has(word.id)));
const repair979 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 979);
const repair992 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 992);
assert.ok(repair979 && repair992, 'both legacy workspace profiles are registered');
assert.equal(repair979.releaseAdditionIds.length, 47, '979-word snapshots restore all cumulative additions through the current release');
assert.equal(repair992.releaseAdditionIds.length, 34, '992-word snapshots restore only the current batch');
const additionRepair979 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair979.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair979.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseAdditionIds: manifest.releaseAdditionIds,
  previousTotalWords: manifest.previousReleaseTotalWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair979.length, 47, 'the exact legacy 979-word snapshot restores only the cumulative additions');
const additionRepair992 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair992.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair992.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair992.length, 34, 'the exact 992-word snapshot restores only Batch 009');
assert.deepEqual(detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair992.releaseAdditionIds.slice(1),
  legacyRecords: baseWords.filter(word => !repair992.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
}), [], 'partial deletion fingerprint must not trigger automatic repair');
assert.deepEqual(detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair992.releaseAdditionIds,
  legacyRecords: [], baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
}), [], 'missing or incomplete legacy snapshot must not trigger automatic repair');
assert.ok(app.includes(`const APP_RELEASE_VERSION = '${manifest.version}'`));
assert.match(app, /detectLegacyReleaseAdditionRepair/);
assert.match(app, /personal\.deletedBaseIds=\[\]/);
assert.match(app, /searchParams\.set\('__release', version\)/);
assert.match(app, /payload\.words\.length!==entry\.count/);
assert.match(app, /loaded\.length!==manifest\.totalWords/);
assert.match(app, /navigator\.serviceWorker\.addEventListener\('controllerchange'/);
assert.match(app, /registration\.update\(\)/);
assert.ok(sw.includes(`const VERSION = '${manifest.version}'`));
assert.match(sw, /cacheUrl\.searchParams\.delete\('__release'\)/);
assert.match(html, /id="metricWordsStatus"/);
console.log('Vocabulary release integrity: PASS (26 files, 1,026 records, 979/992 legacy migration repair profiles, Batch 009, unique IDs/headwords, cache-bust and PWA update guards).');
