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
const batch014 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-014.json', import.meta.url), 'utf8'));
const batch015 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-015.json', import.meta.url), 'utf8'));
const batch016 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-016.json', import.meta.url), 'utf8'));
const batch017 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-017.json', import.meta.url), 'utf8'));
const batch018 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-018.json', import.meta.url), 'utf8'));
const batch019 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-019.json', import.meta.url), 'utf8'));
const batch020 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-020.json', import.meta.url), 'utf8'));
const batch021 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-021.json', import.meta.url), 'utf8'));
const batch022 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-022.json', import.meta.url), 'utf8'));
const batch023 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-023.json', import.meta.url), 'utf8'));
const batch024 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-024.json', import.meta.url), 'utf8'));
const batch028 = JSON.parse(await readFile(new URL('../../data/vocabulary/batch-028.json', import.meta.url), 'utf8'));
const ipaPatch024 = JSON.parse(await readFile(new URL('../../patches/v2.95.18/batch-001-ipa.json', import.meta.url), 'utf8'));
const relatedPatch021 = JSON.parse(await readFile(new URL('../../patches-related-terms/v2.95.14/related-terms-001.json', import.meta.url), 'utf8'));
const relatedPatch022 = JSON.parse(await readFile(new URL('../../patches-related-terms/v2.95.15/related-terms-001.json', import.meta.url), 'utf8'));
const relatedPatch023 = JSON.parse(await readFile(new URL('../../patches-related-terms/v2.95.17/related-terms-001.json', import.meta.url), 'utf8'));
const relatedTerms = JSON.parse(await readFile(new URL('../../data/related-terms.json', import.meta.url), 'utf8'));
const glossaryBatch026 = JSON.parse(await readFile(new URL('../../patches-related-terms/v2.95.20/batch-026-glossary-ledger.json', import.meta.url), 'utf8'));
const glossaryBatch027 = JSON.parse(await readFile(new URL('../../patches-related-terms/v2.95.21/batch-027-glossary-ledger.json', import.meta.url), 'utf8'));
assert.equal(glossaryBatch026.count, 4);
assert.equal(glossaryBatch027.count, 23);
assert.ok(glossaryBatch026.records.every(entry => relatedTerms.terms.some(term => term.term.toLowerCase() === entry.term.toLowerCase() && term.meaning_vi === entry.meaning_vi)));
assert.ok(glossaryBatch027.records.every(entry => relatedTerms.terms.some(term => term.term.toLowerCase() === entry.term.toLowerCase() && term.meaning_vi === entry.meaning_vi)));
assert.deepEqual(glossaryBatch027.records.map(entry => entry.term).sort(), ['activity','answer','carry out','combination','common','continue','decrease','employee','funding','goal','inaction','make','minor','objective','oppose','send','study','support','work','maximum','different','determine','approach'].sort());

assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
assert.equal(manifest.version, JSON.parse(await readFile(new URL('../../data/manifest.json', import.meta.url), 'utf8')).version, 'release manifest matches current candidate');
assert.equal(manifest.totalWords, 1221);
assert.equal(manifest.previousReleaseTotalWords, 1181);
assert.equal(manifest.releaseAdditionIds.length, 40);
assert.deepEqual(manifest.releaseAdditionIds, batch028.words.map(word => word.id), 'release delta IDs match Batch 028');
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
assert.equal(ids.size, 1221);
assert.equal(batch009.words.length, 34);
assert.ok(batch009.words.every(word => ids.has(word.id)));
assert.equal(batch010.words.length, 37);
assert.ok(batch010.words.every(word => ids.has(word.id)));
assert.equal(batch011.words.length, 37);
assert.ok(batch011.words.every(word => ids.has(word.id)));
assert.equal(batch012.words.length, 37);
assert.equal(batch012.ipaSummary.populated, 35);
assert.equal(batch012.ipaSummary.leftBlank, 2);
assert.equal(batch013.words.length, 4);
assert.equal(batch013.ipaSummary.populated, 4);
assert.equal(batch013.ipaSummary.leftBlank, 0);
assert.ok(batch013.words.every(word => ids.has(word.id)));
assert.equal(batch028.words.length, 40);
assert.equal(batch028.ipaSummary.populated, 0);
assert.equal(batch028.ipaSummary.leftBlank, 40);
assert.ok(batch028.words.every(word => ids.has(word.id)));
assert.equal(batch014.release, '2.95.12');
assert.equal(batch014.count, 9);
assert.ok(batch014.records.every(word => ids.has(word.id)));
assert.equal(batch015.release, '2.95.12');
assert.equal(batch015.count, 1);
assert.ok(ids.has(batch015.records[0].id));
assert.equal(batch016.release, '2.95.12');
assert.equal(batch016.count, 22);
assert.equal(batch017.release, '2.95.13');
assert.equal(batch017.count, 10);
assert.ok(batch017.records.every(word => ids.has(word.id)));
assert.equal(batch018.release, '2.95.13');
assert.equal(batch018.count, 4);
const relatedKeys = new Set(relatedTerms.terms.map(row => row.term.toLocaleLowerCase('en-US')));
assert.ok(batch016.records.every(row => relatedKeys.has(row.term.toLocaleLowerCase('en-US')) && row.sourceUrls?.length));
assert.ok(batch018.records.every(row => relatedKeys.has(row.term.toLocaleLowerCase('en-US')) && row.sourceUrls?.length));
assert.ok(batch021.records.every(row => relatedKeys.has(row.term.toLocaleLowerCase('en-US')) && row.sourceUrls?.length));
assert.ok(batch022.records.every(row => relatedKeys.has(row.term.toLocaleLowerCase('en-US')) && row.sourceUrls?.length));
assert.ok(batch023.records.every(row => relatedKeys.has(row.term.toLocaleLowerCase('en-US')) && row.sourceUrls?.length));
assert.ok(relatedTerms.terms.length >= 519);
assert.equal(relatedKeys.size, relatedTerms.terms.length);
assert.equal(batch019.release, '2.95.13');
assert.equal(batch019.count, 1);
assert.equal(batch020.release, '2.95.13');
assert.equal(batch020.count, 1);
assert.equal(batch021.release, '2.95.14');
assert.equal(batch021.count, 10);
assert.equal(relatedPatch021.operations.length, 10);
assert.equal(batch022.release, '2.95.15');
assert.equal(batch022.count, 4);
assert.equal(relatedPatch022.operations.length, 4);
assert.ok(relatedPatch022.operations.every(op => op.expect?.absent === true));
assert.equal(batch023.release, '2.95.17');
assert.equal(batch023.count, 9);
assert.equal(batch024.release, '2.95.18');
assert.equal(batch024.count, 13);
assert.equal(ipaPatch024.operations.length, 13);
assert.ok(batch024.records.every(row => ids.has(row.id) && row.phonetic?.us && row.sourceUrl?.startsWith('https://dictionary.cambridge.org/')));
for (const operation of ipaPatch024.operations) {
  const word = baseWords.find(row => row.id === operation.id);
  assert.ok(word, `IPA batch ID ${operation.id} exists`);
  assert.equal(word.phonetic.us, operation.new, `IPA batch value matches ${operation.id}`);
}
assert.equal(relatedPatch023.operations.length, 9);
assert.ok(relatedPatch023.operations.every(op => op.expect?.absent === true));
const valuable = baseWords.find(row => row.id === 'valuable-adj');
const valuation = baseWords.find(row => row.id === 'valuation-n');
assert.deepEqual(valuable.word_family.find(row => row.word === 'value'), {word:'value',pos:'n',meaning_vi:'giá trị; số tiền mà một thứ đáng giá'});
assert.deepEqual(valuation.word_family.find(row => row.word === 'value'), {word:'value',pos:'v',meaning_vi:'định giá; xác định một thứ đáng giá bao nhiêu tiền'});
const multiSenseRecords = baseWords.filter(word => word.senses?.length > 1);
assert.equal(multiSenseRecords.length, 49);
assert.equal(multiSenseRecords.reduce((sum, word) => sum + (word.examples?.length || 0), 0), 105);
const orderEntry = batch014.records.find(row => row.id === 'order-v');
assert.deepEqual(orderEntry.senses[0].synonyms, ['purchase order']);
const claimantEntry = baseWords.find(row => row.id === 'claimant-n');
assert.equal(claimantEntry.word_family.find(row => row.word === 'claim').pos, 'n');

const repair1181 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1181);
assert.ok(repair1181);
assert.equal(repair1181.releaseAdditionIds.length, 40);

const repair1141 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1141);
assert.ok(repair1141);
assert.equal(repair1141.releaseAdditionIds.length, 80);

const repair1137 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1137);
assert.ok(repair1137);
assert.equal(repair1137.releaseAdditionIds.length, 84);

const repair979 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 979);
const repair992 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 992);
const repair1026 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1026);
assert.ok(repair979 && repair992 && repair1026, 'all known legacy workspace profiles are registered');
assert.equal(repair979.releaseAdditionIds.length, 242, '979-word snapshots restore all cumulative additions through Batch 028');
assert.equal(repair992.releaseAdditionIds.length, 229, '992-word snapshots restore Batch 009 through Batch 028 additions');
assert.equal(repair1026.releaseAdditionIds.length, 195, '1026-word snapshots restore Batch 010 through Batch 028 additions');

const repair1063 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1063);
const repair1100 = manifest.releaseRepairProfiles.find(profile => profile.previousTotalWords === 1100);
assert.ok(repair1063, 'the immediate v2.69.0 workspace profile is registered');
assert.equal(repair1063.releaseAdditionIds.length, 158, '1063-word snapshots restore Batch 011 through Batch 028');
assert.ok(repair1100, 'the immediate v2.70.0 workspace profile is registered');
assert.equal(repair1100.releaseAdditionIds.length, 121, '1100-word snapshots restore Batch 012 through Batch 028');

const additionRepair1181 = detectLegacyReleaseAdditionRepair({deletedBaseIds:repair1181.releaseAdditionIds,legacyRecords:baseWords.filter(word => !repair1181.releaseAdditionIds.includes(word.id)),baseWords,releaseAdditionIds:manifest.releaseAdditionIds,previousTotalWords:manifest.previousReleaseTotalWords,releaseRepairProfiles:manifest.releaseRepairProfiles,currentTotalWords:manifest.totalWords});
assert.equal(additionRepair1181.length,40,'the exact 1181-word snapshot restores Batch 028');

const additionRepair1141 = detectLegacyReleaseAdditionRepair({deletedBaseIds:repair1141.releaseAdditionIds,legacyRecords:baseWords.filter(word => !repair1141.releaseAdditionIds.includes(word.id)),baseWords,releaseAdditionIds:manifest.releaseAdditionIds,previousTotalWords:manifest.previousReleaseTotalWords,releaseRepairProfiles:manifest.releaseRepairProfiles,currentTotalWords:manifest.totalWords});
assert.equal(additionRepair1141.length,80,'the exact 1141-word snapshot restores Batch 026 and 028');

const additionRepair1137 = detectLegacyReleaseAdditionRepair({deletedBaseIds:repair1137.releaseAdditionIds,legacyRecords:baseWords.filter(word => !repair1137.releaseAdditionIds.includes(word.id)),baseWords,releaseAdditionIds:manifest.releaseAdditionIds,previousTotalWords:manifest.previousReleaseTotalWords,releaseRepairProfiles:manifest.releaseRepairProfiles,currentTotalWords:manifest.totalWords});
assert.equal(additionRepair1137.length,84,'the exact 1137-word snapshot restores Batch 013, 026 and 028');

const additionRepair979 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair979.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair979.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseAdditionIds: manifest.releaseAdditionIds,
  previousTotalWords: manifest.previousReleaseTotalWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair979.length, 242, 'the exact legacy 979-word snapshot restores all additions through Batch 028');

const additionRepair992 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair992.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair992.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair992.length, 229, 'the exact 992-word snapshot restores Batch 009–028 additions');

const additionRepair1026 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair1026.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair1026.releaseAdditionIds.includes(word.id)),
  baseWords, releaseRepairProfiles: manifest.releaseRepairProfiles, currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair1026.length, 195, 'the exact 1026-word snapshot restores Batch 010–028');

const additionRepair1063 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair1063.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair1063.releaseAdditionIds.includes(word.id)),
  baseWords, releaseRepairProfiles: manifest.releaseRepairProfiles, currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair1063.length, 158, 'the exact 1063-word snapshot restores Batch 011–028');

const additionRepair1100 = detectLegacyReleaseAdditionRepair({
  deletedBaseIds: repair1100.releaseAdditionIds,
  legacyRecords: baseWords.filter(word => !repair1100.releaseAdditionIds.includes(word.id)),
  baseWords,
  releaseRepairProfiles: manifest.releaseRepairProfiles,
  currentTotalWords: manifest.totalWords
});
assert.equal(additionRepair1100.length, 121, 'the exact 1100-word snapshot restores Batch 012, 013 and 028');

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
console.log('Vocabulary release integrity: PASS (26 files, 1,221 records, 979/992/1026/1063/1100/1137/1141/1181 legacy migration repair profiles, Batch 028 release additions, unique IDs/headwords, cache-bust and PWA update guards).');
