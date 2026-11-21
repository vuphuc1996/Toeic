# Change Manifest — TOEIC Dictionary v2.95.20

## Baseline and scope
- Reconstructed candidate baseline: available `TOEIC_Dictionary_v2.95.19_FullSource.zip`.
- Actual recovered baseline in this workspace is v2.95.19. Earlier chat-described v2.95.20/21 working trees were not present as files here and are not assumed.
- UI/CSS/layout: frozen; no interface changes in this release.

## Data change
- Added 4 Cambridge Dictionary lookup glosses: `method`, `consume`, `function`, `launch`.
- Related-term glossary: 396 → 400.
- Patch is absent-only and hash-guarded; provenance ledger is under `patches-related-terms/v2.95.20/`.
- Existing canonical vocabulary IDs/headwords and synonym/antonym relationships were not edited.

## Tests added/updated
- Added 5 focused tests for Batch 026.
- Registered Batch 026 tests in CI workflow and compile list.
- Updated release-integrity checks to validate manifest version dynamically and glossary size 400; it also checks Batch 026 terms.

## Release boundaries
- Local candidate only. GitHub Actions, Pages deployment, browser/device QA and owner manual acceptance were not performed.
