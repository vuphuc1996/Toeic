# Test Report — TOEIC Dictionary v2.95.43

**Scope:** Related Glossary Batch 036; historical glossary regression and CI registration; version synchronization; no UI or learner-data change.


## Completed local checks

| Check | Result | Detail |
|---|---|---|
| Related Glossary test modules | PASS | 104/104 across all `test_related_glossary*.py` modules |
| Batch 036 focused | PASS | 6/6 (includes provenance, relation target, patch-base and protected-bank SHA guards) |
| Batch 035 focused | PASS | 5/5; historical base reconstructed while removing later additive ledgers |
| Related-term patch updater | PASS | 11/11 |
| CI coverage | PASS | 3/3; every Python test module and all JS suites are registered |
| Major release quality audit | PASS | 8/8 |
| Related-term explanation context | PASS | 3/3 |
| Version sync tests | PASS | 12/12 |
| Source package tests | PASS | 3/3 |
| Python compileall | PASS | `python -m compileall -q tools` |
| Canonical data validator | PASS | 1,141 records; 0 IDs added / 0 lost; 0 errors / 0 warnings |
| Learning content validator | PASS | 0 errors / 0 warnings |
| Repository integrity | PASS | 413 references/data files inspected; 0 errors / 0 optional warnings |
| Release version sync | PASS | manifest, app, service worker, index markers, README, current version, Master and changelog agree on 2.95.43 |
| Related glossary candidate audit | PASS | 546 entries; 535/804 covered; 269 unique missing; 270 occurrences missing |
| Related glossary quality audit | PASS | 546 entries; 227 flagged (223 High, 2 Medium, 2 Low); 0 duplicate groups |
| Relationship graph audit | PASS | 1,141 headwords; 1,037 references; 0 malformed / 0 self-reference; 248 non-reciprocal review flags |
| TOEIC content coverage audit | PASS | Generated current version report; inventory unchanged |
| Project progress snapshot | PASS | Generated for 2.95.43 |
| JavaScript regression suites | PASS | 39/39 suites; no failed suite |


## Focused Python execution count

The separate focused commands executed **144 test cases** (104 related-glossary tests + 11 patch-updater + 3 CI-coverage + 8 major-release + 3 related-term-explanation + 12 version-sync + 3 package-source tests). This is not a count of the entire repository test suite.


## Incomplete checks / resolved issues

- **Full Python discovery:** attempted with `python -m unittest discover -s tools/tests -p 'test_*.py' -v`, but execution was terminated by the runtime limit before the aggregate summary. No full-discovery PASS is claimed. The partial log reached `test_patch_data.py` and does not provide a complete result.
- **Initial focused glossary run:** surfaced stale historical expectations in Batch 027 coverage and Batch 034 patch-base reconstruction after Batch 035/036 additions. The expected coverage was updated to the current 535/767 covered targets/occurrences; Batch 034 now removes all later additive glossary batches when reconstructing its historical base. The related-glossary aggregate was rerun and passed 104/104.
- **CI registration:** first check detected missing explicit Batch 036 execution step; step added, then CI coverage test rerun and passed 3/3.
- **Cambridge direct access:** all 11 direct page fetches returned HTTP 403. Search-index excerpts were reviewed; independent editorial review remains pending.


## Not verified externally

- Remote GitHub Actions run.
- GitHub Pages deployment, CDN/cache propagation or installed PWA update.
- Browser acceptance, offline/reconnect, screen reader, or physical Android/iOS/tablet/desktop tests.
- Independent lexical and Vietnamese editorial review.
- Full Python suite.


## Preservation assertions

- Canonical A–Z vocabulary files byte hashes unchanged (guarded in Batch 036 test).
- Grammar, Listening, Reading and separate Part 5 banks byte hashes unchanged.
- No canonical IDs/headwords, synonym/antonym arrays, learning questions/answer keys, Mock eligibility, learner IndexedDB, UI, Robot Buddy boundary, backend or deployment settings changed.


## Packaging and replay

- Full Source: **641 files**; one root `Toeic_Dictionary_v2.95.43/`; ZIP CRC, root and exclusions PASS.
- Patch overlay: **39 files (18 modified + 21 added; 0 deletions)**.
- Patch replay against v2.95.42: **641/641 files byte-identical** to the Full Source; no missing, extra or mismatched files.
- SHA-256 sidecars generated outside the source package.
