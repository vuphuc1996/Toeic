# Release Acceptance — TOEIC Dictionary v2.95.54

## Decision

**Local source acceptance: PASS.**

**Production acceptance: NOT GRANTED / NOT VERIFIED.**

## Accepted locally

- Full Python unittest discovery in reconstructed clone: 711 PASS, 0 FAIL / 0 ERROR / 0 SKIP; 135.824 seconds. From the final clean FullSource archive: 710 PASS + 1 accepted SKIP, 0 FAIL / 0 ERROR; 135.701 seconds. The skip is the `.gitignore` test, which requires `.git` metadata intentionally absent from source ZIPs.
- Data validator: 1,141 vocabulary records, zero ID additions/removals, zero ERROR and zero WARNING, verified again from extracted FullSource.
- Version synchronization: 13 markers and changelog aligned to 2.95.54.
- New validator rules VF003 and CE004 covered by focused regression tests and full discovery.
- Exact guarded data patch dry-run/apply and patch-data tests passed.
- Historical glossary snapshots remain protected by in-memory reverse reconstruction of the new exact patch; original historical hashes remain asserted.
- FullSource archive CRC/content and Patch exact replay/byte comparison passed.

## Scope restrictions confirmed

- No vocabulary IDs, headwords, topics, Vietnamese meanings, synonym/antonym arrays, question IDs, choices, answer keys or Mock eligibility changed.
- No reserve-pending Listening question was promoted.
- No learner progress, IndexedDB schema, UI feature or Robot Buddy feature changed.
- The only canonical vocabulary field changes are `appliance-n.verb_forms` and eight headword-level `cefr_level` values, all through the exact guarded patch.

## Still unverified

- Claude independent rerun on Python 3.12.3 / Node 22.
- Remote GitHub Actions execution and GitHub Pages deployment.
- Real Safari/iPad/PWA interactions, persistent storage, offline/cache propagation and physical-device TTS.
- Pedagogical validity of CEFR estimates; CE004 checks internal consistency, not independent CEFR correctness.

## Release gate

Do not describe this release as production accepted until the independent audit rerun and remote/physical-device checks above are completed.
