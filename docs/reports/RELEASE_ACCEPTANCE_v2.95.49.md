# Release Acceptance — TOEIC Dictionary v2.95.49

Date: 2026-11-24

## Local source acceptance

| Gate | Result | Evidence |
|---|---|---|
| Version markers / changelog | PASS | `python tools/sync-version.py --check` |
| Vocabulary structural and quality validator | PASS | 1,141 records; 0 new IDs, 0 missing IDs; 0 ERROR / 0 WARNING |
| Objective definitions and resource links | PASS | 11 objectives / 33 criteria; 379/379 resource links; 6 criteria instrumented |
| Related Glossary quality audit | PASS as read-only audit | 567 entries; 227 review flags; no automatic data repair |
| Placeholder display-safety regression | PASS | New Node runtime test checks all 73 canonical placeholder rows and valid definitions |
| Python test inventory | PASS WITH SKIPS | 89/89 modules terminal; 692 PASS, 1 accepted environment SKIP; 0 FAIL / ERROR / TIMEOUT / NOT RUN |
| GitHub Actions workflow shell replay | PASS | 110/110 `run:` steps; 0 fail / timeout / error / pending |
| FullSource archive | PASS | 539 files; CRC and exact source-byte comparison verified |
| Patch | PASS | 29 adds / 11 modifies / 0 deletes; exact predecessor SHA preconditions and replay verified |

## Accepted environment skip

`tools/tests/test_patch_data.py::PatchDataTests::test_repository_gitignore_excludes_audit_logs` is skipped because this source archive has no `.git` metadata and that assertion requires a clone. The reason matches the explicit allowlist in `tools/test-inventory-policy.json`. The skip remains reported separately and is not counted as a passed test.

## Production / deployment gates — not yet accepted

- Remote GitHub-hosted Actions run: UNVERIFIED.
- GitHub Pages publish and deployed asset verification: UNVERIFIED.
- Service-worker update on an already-installed PWA, cache propagation and offline operation: UNVERIFIED.
- Physical iOS / Android / iPad / tablet / desktop browser acceptance: UNVERIFIED.

## Decision

**Local source/package acceptance: PASS WITH SKIPS. Production acceptance: NOT YET GRANTED.** Do not describe v2.95.49 as deployed or production-accepted until the remote and device gates above have evidence.
