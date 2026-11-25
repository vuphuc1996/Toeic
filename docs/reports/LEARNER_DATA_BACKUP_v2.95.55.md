# Learner data backup and restore — v2.95.55

Date: 2026-11-24

## Scope

This release adds a complete local learner-data backup beside the existing vocabulary-only JSON/CSV export. The implementation reads the current `toeic-vocabulary-phase1` IndexedDB database, version 1, object store `workspace`, by cursor; it does not introduce a database upgrade or alter the existing store contract. It also enumerates every localStorage key in the application namespace `toeic:`, including legacy and future keys, rather than relying on a brittle hard-coded list.

## Backup envelope

- Type: `TOEIC_LEARNER_DATA_BACKUP`
- Backup schema version: `1`
- IndexedDB: database name, version, store name and every `{key,value}` entry
- localStorage: namespace and every `{key,value}` entry (raw string values preserved)
- Browser persistence: whether `navigator.storage.persist()` is supported, requested and granted (best effort; browser-controlled)
- Integrity: SHA-256 digest over a recursively key-sorted canonical representation of the complete payload, excluding only the integrity field itself

The existing `Export JSON` and CSV remain vocabulary-only. The new action is explicitly named “Sao lưu toàn bộ dữ liệu học tập”.

## Restore safeguards

1. Parse the file and validate its type, supported schema version, exact database/store contract, entry shapes, unique keys, localStorage namespace and SHA-256 digest before any write.
2. Ask for explicit confirmation and explain that matching keys will be overwritten while keys absent from the backup are preserved.
3. Create and download a fresh pre-restore full backup before applying imported data.
4. Write all IndexedDB entries in one read-write transaction using `put`; do not clear the store.
5. Apply localStorage values only after the IndexedDB transaction completes. If localStorage writing fails, restore the prior localStorage snapshot and attempt to restore the prior IndexedDB snapshot.
6. Reload after successful restore so in-memory application state is hydrated from storage.

The restore path does not delete current keys absent from the import, migrate the IndexedDB schema, or rewrite canonical vocabulary/question data. It preserves unknown keys already on the device.

## Validation

- `learner-data-backup.mjs`: backup envelope, SHA-256 round-trip, tamper rejection, unsupported schema rejection, duplicate-key rejection, namespace isolation and exact value round-trip.
- `learner-data-backup-integration.mjs`: UI wiring, dynamic IndexedDB/localStorage enumeration, persistence request, merge semantics, rollback guard, unchanged IndexedDB v1 and Service Worker precache registration.
- Full Node regression suite: 42/42 scripts PASS (Node v22.16.0).
- Full Python discovery: 711 tests executed; 710 PASS, 1 accepted SKIP requiring Git metadata (source archive has no `.git`), 0 FAIL, 0 ERROR; 143.055 seconds (Python 3.13.5).
- Data validator: 1,141 records; zero ID additions/removals; 0 ERROR / 0 WARNING.
- Version synchronization: all registered markers and `docs/CHANGELOG.md` PASS at 2.95.55.

## Limitations / unverified

- Browser permission for persistent storage is best effort and cannot be guaranteed by the application.
- Storage quota failures, browser crashes/power loss during cross-store restore, and rollback failure cannot be proven away by static tests. IndexedDB is transactional; localStorage and IndexedDB do not share a cross-API atomic transaction.
- Physical iOS Safari/iPadOS, Android browsers, actual download/import picker behavior, and hosted GitHub Actions/Pages have not been tested in this environment.
- Backups contain private learner progress and should be stored securely by the user. No data is uploaded by this feature.
