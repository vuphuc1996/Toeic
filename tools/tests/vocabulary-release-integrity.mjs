import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { detectLegacyReleaseAdditionRepair } from '../../assets/js/vocabulary-release-integrity.js';

const manifest = JSON.parse(await readFile(new URL('../../data/manifest.json', import.meta.url), 'utf8'));
const app = await readFile(new URL('../../assets/js/app.js', import.meta.url), 'utf8');
const sw = await readFile(new URL('../../sw.js', import.meta.url), 'utf8');
const html = await readFile(new URL('../../index.html', import.meta.url), 'utf8');
const batch008 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-008.json', import.meta.url), 'utf8'));
const batch009 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-009.json', import.meta.url), 'utf8'));
const batch010 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-010.json', import.meta.url), 'utf8'));
const batch011 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-011.json', import.meta.url), 'utf8'));
const batch012 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-012.json', import.meta.url), 'utf8'));
const batch013 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-013.json', import.meta.url), 'utf8'));

assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
assert.equal(manifest.totalWords, 1141);
assert.equal(manifest.previousReleaseTotalWords, 1137);
assert.equal(manifest.releaseAdditionIds.length, 4);
assert.deepEqual(manifest.releaseAdditionIds, batch013.words.map(word => word.id), 'release delta IDs match Batch 013');
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
assert.equal(ids.size, 1141);
assert.equal(batch009.words.length, 34);
assert.ok(batch009.words.every(word => ids.has(word.id)));
assert.equal(batch010.words.length, 37);
assert.ok(batch010.words.every(word => ids.has(word.id)));
assert.equal(batch011.words.length, 37);
assert.ok(batch011.words.every(word => ids.has(word.id)));
assert.equal(batch012.words.length, 37);
assert.ok(batch012.words.every(word => ids.has(word.id)));
assert.equal(batch012.ipaSummary.populated, 35);
assert.equal(batch012.ipaSummary.leftBlank, 2);
assert.equal(batch013.words.length, 4);
assert.equal(batch013.ipaSummary.populated, 4);
assert.equal(batch013.ipaSummary.leftBlank, 0);
assert.ok(batch013.words.every(word => ids.has(word.id)));
const repair1137 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1137);
assert.ok(repair1137);
assert.equal(repair1137.releaseAdditionIds.length, 4);
const repair979 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 979);
const repair992 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 992);
const repair1026 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1026);
assert.ok(repair979 && repair992 && repair1026, 'all known legacy workspace profiles are registered');
assert.equal(repair979.releaseAdditionIds.length, 162, '979-word snapshots restore all cumulative additions through Batch 012');
assert.equal(repair992.releaseAdditionIds.length, 149, '992-word snapshots restore Batch 009, 010, 011 and 012 additions');
assert.equal(repair1026.releaseAdditionIds.length, 115, '1026-word snapshots restore Batch 010, 011 and 012 additions');
const repair1063 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1063);
const repair1100 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1100);
assert.ok(repair1063, 'the immediate v2.69.0 workspace profile is registered');
assert.equal(repair1063.releaseAdditionIds.length, 78, '1063-word snapshots restore Batch 011 and 012');
assert.ok(repair1100, 'the immediate v2.70.0 workspace profile is registered');
assert.equal(repair1100.releaseAdditionIds.length, 41, '1100-word snapshots restore only Batch 012');
const additionRepair1137 = detectLegacyReleaseAdditionRepair({deletedBaseIds:repair1137.releaseAdditionIds,legacyRecords:baseWords.filter(word => !repair1137.releaseAdditionIds.includes(word.id)),baseWords,releaseAdditionIds:manifest.releaseAdditionIds,previousTotalWords:manifest.previousReleaseTotalWords,releaseRepairProfiles:manifest.releaseRepairProfiles,currentTotalWords:manifest.totalWords});
assert.equal(additionRepair1137.length,4,'the exact 1137-word snapshot restores Batch 013');
const additionRepair979 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair979.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair979.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseAdditionIds: manifest.releaseAdditionIds,
  previousTotalWords: manifest.previousReleaseTotalWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair979.length, 162, 'the exact legacy 979-word snapshot restores all additions through Batch 012');
const additionRepair992 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair992.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair992.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair992.length, 149, 'the exact 992-word snapshot restores Batch 009, 010, 011 and 012 additions');
const additionRepair1026 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair1026.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair1026.releaseAdditionIds.includes(word.id)),
  baseWords, releaseRepairProfiles: manifest.releaseRepairProfiles, currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair1026.length, 115, 'the exact 1026-word snapshot restores Batch 010, 011 and 012');
const additionRepair1063 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair1063.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair1063.releaseAdditionIds.includes(word.id)),
  baseWords, releaseRepairProfiles: manifest.releaseRepairProfiles, currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair1063.length, 78, 'the exact 1063-word snapshot restores Batch 011 and 012');
const additionRepair1100 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair1100.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair1100.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair1100.length, 41, 'the exact 1100-word snapshot restores only Batch 012');
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
console.log('Vocabulary release integrity: PASS (26 files, 1,141 records, 979/992/1026/1063/1100/1137 legacy migration repair profiles, Batches 008/009/010/011/012/013, unique IDs/headwords, cache-bust and PWA update guards).');
