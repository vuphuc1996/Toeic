# Package Verification — TOEIC Dictionary v2.95.48

## Canonical base

- Base: `TOEIC_Dictionary_v2.95.47_FullSource.zip`
- Base SHA-256: `a3baba7192fb2fc1e6458455ee270bd459e085d5dafc018b5203269edef766de`
- Base entries: 504

## Target package

- FullSource: `TOEIC_Dictionary_v2.95.48_FullSource.zip`
- Patch: `TOEIC_Dictionary_v2.95.48_Patch_From_v2.95.47.zip`
- Patch is explicitly based on the exact base archive above, not on an earlier v2.95.46 archive.
- FullSource contains one versioned root, excludes `.git`, logs, `__pycache__`, `.pyc`, `.zip`, `.log` and temporary artifacts.

## Patch operations

- Add: 6 files
- Modify: 12 files
- Delete: 0 files

Patch manifest includes SHA-256 preconditions for every modified/deleted base file and target SHA-256 for every added/modified file. The exact base archive SHA-256 is also checked.

## Verification

- FullSource ZIP CRC test: PASS.
- FullSource path/root and file-content comparison against the working source tree: PASS.
- Patch base SHA and per-file preconditions: PASS.
- Patch replay in an isolated extracted copy of the exact base: PASS.
- Replayed target file set and every file byte matched the FullSource working tree: PASS.
- SHA-256 sidecars generated for both archives.

Package integrity does not imply full test-suite completion or production deployment acceptance. See the test report for those separate statuses.


Final byte sizes and SHA-256 values are provided by the adjacent `.sha256` sidecar files and are verified against the final artifacts.
