import assert from 'node:assert/strict';
import { createLearnerBackup, validateLearnerBackup, stableBackupStringify } from '../../assets/js/learner-data-backup.js';

const source = {
  indexedDBEntries: [
    { key: 'personalVocabulary', value: { schemaVersion: 3, additions: [{ id: 'custom-1', word: 'workflow' }], overrides: {}, overrideBaseSigs: {}, deletedBaseIds: [] } },
    { key: 'objectiveProgress', value: { objectives: { O1: { attempts: 3 } } } },
    { key: 'practiceSession', value: { sessionSeenIds: ['q-1', 'q-2'] } }
  ],
  localStorageEntries: [
    { key: 'toeic:mock-history:v1', value: '[{"id":"mock-1"}]' },
    { key: 'toeic:foundation-progress:v1', value: '{"lesson-1":{"attempts":2}}' }
  ],
  exportedAt: '2026-11-24T10:00:00.000Z',
  storagePersistence: { supported: true, requested: true, granted: false }
};

const backup = await createLearnerBackup(source);
assert.equal(backup.type, 'TOEIC_LEARNER_DATA_BACKUP');
assert.equal(backup.schemaVersion, 1);
assert.equal(backup.integrity.algorithm, 'SHA-256');
assert.equal(backup.integrity.digest.length, 64);
const restored = await validateLearnerBackup(backup);
assert.deepEqual(restored.indexedDBEntries, source.indexedDBEntries);
assert.deepEqual(restored.localStorageEntries, source.localStorageEntries);

const tamperedValue = structuredClone(backup);
tamperedValue.storage.indexedDB.entries[0].value.additions[0].word = 'tampered';
await assert.rejects(() => validateLearnerBackup(tamperedValue), /toàn vẹn/);

const unsupported = structuredClone(backup);
unsupported.schemaVersion = 99;
await assert.rejects(() => validateLearnerBackup(unsupported), /không được hỗ trợ/);

const duplicate = structuredClone(backup);
duplicate.storage.indexedDB.entries.push(structuredClone(duplicate.storage.indexedDB.entries[0]));
const { integrity, ...payload } = duplicate;
duplicate.integrity.digest = backup.integrity.digest;
await assert.rejects(() => validateLearnerBackup(duplicate), /bị trùng/);

const outsideNamespace = await createLearnerBackup({ indexedDBEntries: [], localStorageEntries: [{ key: 'other-app:data', value: 'x' }] });
await assert.rejects(() => validateLearnerBackup(outsideNamespace), /namespace toeic/);
assert.equal(stableBackupStringify({ b: 1, a: { z: 2, y: 3 } }), stableBackupStringify({ a: { y: 3, z: 2 }, b: 1 }));
console.log('PASS: full learner backup envelope, SHA-256 integrity, schema validation, duplicate-key rejection, namespace isolation and exact data round-trip.');
