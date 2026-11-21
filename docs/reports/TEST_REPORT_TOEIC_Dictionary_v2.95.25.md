# Test Report — TOEIC Dictionary v2.95.25 follow-up (Batch 028)

## Scope

- Release remains **v2.95.25**; no interim or v2.95.26 created.
- Added seven related glossary terms from exact canonical bilingual headword senses.
- Relationship arrays, canonical vocabulary headwords and learner records were not changed.

## Results

- **34 focused Python tests PASS** across seven modules (project progress, CI coverage, repository integrity, glossary batches 027/028, backlog, major-release audit, backfill).
- **39/39 JavaScript regression suites PASS.**
- Vocabulary validator: **1,141 records, 0 errors, 0 warnings** (legacy baseline informational warnings are not counted as release errors).
- Learning-content validator: **0 errors / 0 warnings**.
- Repository integrity: **397 references/files, 0 errors / 0 optional warnings**.
- Version synchronization: **PASS** for all release markers.
- Learning outcome audit: **11/11 objectives, 33 criteria, 6/33 instrumented**.
- Related-term glossary: **430 entries; 419/804 referenced terms covered (52.1%); 385 unique terms / 386 occurrences still unglossed**.

## Limitations

- Full Python discovery was not completed.
- Remote GitHub Actions and Pages deployment are not verified.
- Browser, iOS/Android/desktop acceptance, offline/reconnect and actual device TTS are not verified.
- Batch 028 uses the project’s exact canonical vocabulary senses; independent external dictionary review was not performed.

## Package checks

- FullSource ZIP integrity checked.
- Patch file set generated from v2.95.24 FullSource comparison; deletion manifest included.
- Patch replay comparison, package file counts and SHA-256 checksum verified.

## v2.95.25 continuation — read-only candidate audit

- Added `tools/audit-related-glossary-candidates.py`: read-only audit ranks missing referenced terms by relationship frequency, identifies canonical headword availability, and flags basic placeholder definitions. It does not modify data or add definitions.
- Added `tools/tests/test_related_glossary_candidate_audit.py` (3 tests) and CI registration.
- Candidate audit reconciliation: 1,141 vocabulary headwords; 430 glossary entries; 804 distinct referenced terms; 419 covered; 385 missing terms / 386 occurrences.
- Tests: candidate audit 3/3; Batch 028 4/4; Backfill 025 6/6; Major Release Quality Audit 025 8/8; all 39 JavaScript suites PASS.
- Data/content/repository validators and version sync PASS. Full Python discovery and remote CI/deploy/device acceptance are not claimed.
- No runtime vocabulary/glossary/relation data, question content, learner data or UI changed in this continuation.

## Continuation audit refinement (same release)
- Enhanced read-only candidate audit to show canonical sense count/preview and review tiers (`single-sense-review`, `multi-sense-review`, `no-canonical-headword`), without copying or editing definitions.
- Definition inventory reconciled to 229 missing English definitions + 73 placeholders + 128 non-placeholder definitions = 430 glossary entries.
- Candidate audit tests now 4/4 PASS; Batch 028 4/4; Backfill 025 6/6; Major Release Quality Audit 025 8/8; all 39 MJS suites PASS.
- Data validator, learning content validator, repository integrity preflight, and version sync PASS.
- Full `unittest discover` was attempted but exceeded the execution timeout. The interrupted log surfaced `test_repository_gitignore_excludes_audit_logs` failure because this workspace lacks `.git` metadata (`fatal: not a git repository`); this environment-dependent test was confirmed failing in isolation. This is not reported as a product test pass. Focused tests above and 39 MJS suites remain verified.

## Continuation — related glossary quality flag audit
- New read-only quality flag tool `tools/audit-related-glossary-quality.py`; generated `RELATED_GLOSSARY_QUALITY_FLAGS_v2.95.25.md`.
- Scanned 430 rows; 305 flagged for review. Overlapping issue counts: missing English definition 229, placeholder 73, missing POS 302, missing provenance 75, short definition 1. Flags are not semantic judgments.
- New focused test module: 4/4 PASS. CI step registered.
- No runtime data, glossary entries, vocabulary, relation arrays, learner data or UI altered.

## Packaging refresh after glossary-quality audit
- FullSource: 461 files; ZIP CRC/root verification PASS.
- Update Patch: 56 changed/additional files and 6 removed-path entries; ZIP CRC/root verification PASS.
- Patch overlay replayed against v2.95.24 baseline and matched all 461 FullSource files byte-for-byte.
- SHA-256 manifests refreshed.
- Verification on this continuation: candidate audit 4/4, quality flag audit 4/4, canonical glossary backfill 6/6, major release audit 8/8, JavaScript `.mjs` suites 39/39 PASS; validators (data, learning content, repository integrity) PASS; version synchronization PASS.
