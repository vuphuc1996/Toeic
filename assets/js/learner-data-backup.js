const BACKUP_TYPE = 'TOEIC_LEARNER_DATA_BACKUP';
const BACKUP_SCHEMA_VERSION = 1;

function stableValue(value) {
  if (Array.isArray(value)) return value.map(stableValue);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.keys(value).sort().map(key => [key, stableValue(value[key])]));
  }
  return value;
}

export function stableBackupStringify(value) {
  return JSON.stringify(stableValue(value));
}

async function sha256Hex(value) {
  if (!globalThis.crypto?.subtle) throw new Error('Trình duyệt không hỗ trợ kiểm tra SHA-256. Hãy mở ứng dụng bằng HTTPS trên trình duyệt hiện đại.');
  const bytes = new TextEncoder().encode(value);
  const digest = await globalThis.crypto.subtle.digest('SHA-256', bytes);
  return [...new Uint8Array(digest)].map(byte => byte.toString(16).padStart(2, '0')).join('');
}

export async function createLearnerBackup({ indexedDBEntries, localStorageEntries, exportedAt = new Date().toISOString(), storagePersistence = null }) {
  if (!Array.isArray(indexedDBEntries) || !Array.isArray(localStorageEntries)) throw new Error('Snapshot lưu trữ không hợp lệ.');
  const payload = {
    type: BACKUP_TYPE,
    schemaVersion: BACKUP_SCHEMA_VERSION,
    exportedAt,
    application: 'TOEIC Dictionary',
    storage: {
      indexedDB: { database: 'toeic-vocabulary-phase1', version: 1, objectStore: 'workspace', entries: indexedDBEntries },
      localStorage: { namespace: 'toeic:', entries: localStorageEntries },
      persistence: storagePersistence
    }
  };
  return { ...payload, integrity: { algorithm: 'SHA-256', digest: await sha256Hex(stableBackupStringify(payload)) } };
}

export async function validateLearnerBackup(backup) {
  if (!backup || typeof backup !== 'object' || Array.isArray(backup)) throw new Error('Tệp sao lưu không phải JSON object.');
  if (backup.type !== BACKUP_TYPE) throw new Error('Sai loại tệp. Hãy chọn bản sao lưu toàn bộ dữ liệu học tập.');
  if (backup.schemaVersion !== BACKUP_SCHEMA_VERSION) throw new Error(`Phiên bản cấu trúc sao lưu không được hỗ trợ: ${backup.schemaVersion ?? 'không có'}.`);
  const idb = backup.storage?.indexedDB;
  const local = backup.storage?.localStorage;
  if (idb?.database !== 'toeic-vocabulary-phase1' || idb?.version !== 1 || idb?.objectStore !== 'workspace' || !Array.isArray(idb.entries)) throw new Error('Thiếu hoặc sai cấu trúc IndexedDB trong bản sao lưu.');
  if (local?.namespace !== 'toeic:' || !Array.isArray(local.entries)) throw new Error('Thiếu hoặc sai cấu trúc localStorage trong bản sao lưu.');
  const idbKeys = new Set();
  for (const entry of idb.entries) {
    if (!entry || typeof entry !== 'object' || typeof entry.key !== 'string' || !Object.hasOwn(entry, 'value')) throw new Error('Có bản ghi IndexedDB không hợp lệ.');
    if (idbKeys.has(entry.key)) throw new Error(`Khóa IndexedDB bị trùng: ${entry.key}`);
    idbKeys.add(entry.key);
    JSON.stringify(entry.value);
  }
  const localKeys = new Set();
  for (const entry of local.entries) {
    if (!entry || typeof entry !== 'object' || typeof entry.key !== 'string' || !entry.key.startsWith('toeic:') || typeof entry.value !== 'string') throw new Error('Có bản ghi localStorage không hợp lệ hoặc nằm ngoài namespace toeic:.');
    if (localKeys.has(entry.key)) throw new Error(`Khóa localStorage bị trùng: ${entry.key}`);
    localKeys.add(entry.key);
  }
  if (backup.integrity?.algorithm !== 'SHA-256' || !/^[a-f0-9]{64}$/.test(backup.integrity.digest || '')) throw new Error('Thiếu mã kiểm tra toàn vẹn SHA-256.');
  const { integrity, ...payload } = backup;
  const actual = await sha256Hex(stableBackupStringify(payload));
  if (actual !== integrity.digest) throw new Error('Kiểm tra toàn vẹn thất bại: nội dung tệp đã bị thay đổi hoặc hỏng.');
  return { indexedDBEntries: idb.entries, localStorageEntries: local.entries };
}
