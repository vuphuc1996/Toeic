# TOEIC Dictionary — Master Status

**Phiên bản mã nguồn đang kiểm kê:** v2.95.46

## Canonical source and candidate

- Official baseline: **v2.95.45 FullSource**, 698 files, SHA-256 `2d4f1f58aa355c8515b311d11fe01852f80d8c4dea57f5fff8631e955a6f112e`.
- Current working tree: **v2.95.46 candidate**, derived from the verified baseline; not yet Source Release Accepted.
- Previous official source: v2.95.45 only. No alternative v2.95.44 branch is a release baseline.
- No complete/verified Batch 039 candidate tree was present in the accessible source/workspace; none was invented or merged.
- Official release identity is determined by manifest + FullSource SHA-256, never folder name or report version alone.

## Master development contract

- `docs/MASTER_DEVELOPMENT_PROMPT.md` is the single development policy (Sections 1–15) for all subsequent prompts.
- It governs source lineage, GitHub-only/static PWA architecture, frozen UI, learner data preservation, batch prioritization, dictionary provenance, dynamic test inventory, fingerprinting/checkpoints, separate source/production acceptance and non-destructive testing.
- `docs/README.md`, `docs/COMPATIBILITY.md`, `docs/versions/CURRENT_VERSION.md` and `docs/versions/PREVIOUS_VERSION.md` point to this contract. Do not create parallel Master prompts or roadmaps.

## Completed in the v2.95.46 candidate batch

- Consolidated Master Development Prompt Sections 1–15 and added a reusable future-task prompt with anti-drift rules.
- Updated README, Compatibility, Changelog, Current/Previous Version, Master Status and Manual Acceptance Checklist.
- Editorial Review Queue now derives counts from source JSON through `tools/editorial_inventory.py`; baseline verified values are Listening 102 eligible / 193 reserve / 295 total, Part 7 reserve 87, separate Part 5 practice-only 80. No reserve items were promoted.
- Added dynamic test inventory policy and v2.95.45 baseline inventory (88 modules). Current candidate dynamically discovers 89 modules: one added fingerprint test module, zero removed, five test modules modified. The count 88 is historical baseline only, not a cap.
- Implemented deterministic source/test-input/environment fingerprints, dependency lockfile hashes, exact command arguments, symlink escape rejection, normalized path collision detection, per-module terminal states/case counts, skip reason policy, checkpoint invalidation and persisted inventory errors.
- Updated Release Acceptance to run complete test modules rather than repeatedly splitting large modules into case batches.
- Retired 233 obsolete versioned Markdown reports and 5 old root release notes after reference analysis; full original text, path, size and SHA-256 markers are preserved in `docs/archive/PROJECT_HISTORY.md`. Exact byte-identical Markdown duplicate groups found: 0.
- Added tests for runner/fingerprint/rotation policies; no UI redesign, learner IndexedDB changes, canonical vocabulary identity changes, question/choice/answer-key changes, backend or Cloudflare additions.

## Verified focused tests and checks

- Python test sharder runner: 17/17 PASS.
- Fingerprint/path/environment policy tests: 9/9 PASS.
- Release Acceptance Runner tests: 10/10 PASS.
- Release rotation tests: 9/9 PASS.
- `test_patch_data.py`: 20 test cases; 19 passed, 1 environment-only Git metadata skip, accepted by explicit policy.
- `test_validator.py`: direct full module 38/38 PASS.
- Editorial Review Queue tests: 8/8 PASS (verified before the final sharder refinements; rerun in release acceptance).
- Data validator, learning-content validator, repository integrity, version synchronization: PASS in the targeted candidate run; final values to be refreshed by release acceptance.

## Incomplete / not yet accepted

- Final strict dynamic Python suite: 89 modules, executed by the release-acceptance runner using the current deterministic source/environment/command fingerprint. The authoritative per-module and per-case outcome is recorded in the generated v2.95.46 Test Report; do not infer aggregate PASS from focused tests.
- JavaScript regression and validators are re-executed as part of the candidate release-acceptance evidence.
- Source Release Acceptance: **candidate only until the final strict report, FullSource/Patch replay and checksums are inspected together**.
- Production Deployment Acceptance: **UNVERIFIED**; remote GitHub Actions, GitHub Pages deployed artifact identity, real browser/PWA/offline/cache behavior, Android/iOS/desktop acceptance and learner-data continuity have not been verified on a deployed build.
- Independent editorial review of pending TOEIC content remains pending.

## Protected invariants

- Canonical A–Z vocabulary IDs/headwords/relations unchanged.
- Listening/Reading/Grammar/Part 5 question IDs, choices, answer keys and Mock eligibility unchanged.
- IndexedDB `toeic-vocabulary-phase1`, schema v1, store `workspace`, learner progress/review/Mock history unchanged.
- UI remains frozen; only source-version/cache markers may change where necessary.
- GitHub Pages/GitHub-only; no Cloudflare, backend, GAS or iframe.

## Next exact step

Run the 89-module Python suite using the strict source/environment/command fingerprinted sharder, resume only from a matching checkpoint, run all final validators and JavaScript suites, then generate the final FullSource/Patch and prove byte-identical Patch replay. Keep the candidate blocked if any module is FAIL, TIMEOUT, ERROR or NOT RUN, or any protected invariant/package gate fails.
