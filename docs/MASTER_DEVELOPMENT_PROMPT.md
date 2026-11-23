# MASTER DEVELOPMENT PROMPT — TOEIC Dictionary PWA

**Purpose:** the single authoritative development contract for every future TOEIC Dictionary task, batch, review, release and handoff. This document consolidates the project rules in Sections 1–15. A later user prompt supplies the task scope; it does not silently replace this contract.

**Current task baseline (candidate v2.95.46 is derived from this source):**

- Official input Full Source: `TOEIC_Dictionary_v2.95.45_FullSource.zip`
- Baseline version: `2.95.45`
- Baseline files: `698`
- Baseline SHA-256: `2d4f1f58aa355c8515b311d11fe01852f80d8c4dea57f5fff8631e955a6f112e`
- Immediately previous released source: `v2.95.44`
- The alternate uploaded `v2.95.44` was a distinct source branch and was selectively reviewed; it is not an approved replacement baseline.
- No complete, verifiable Batch 039 source/ledger was present in the accessible v2.95.45 source or current work directory at the time this guide was consolidated. Never invent or assume that candidate exists; inspect any newly attached/library source before deciding whether to reuse it.

After a release is explicitly accepted, `docs/versions/CURRENT_VERSION.md`, `PREVIOUS_VERSION.md`, the manifest and the corresponding verified package/hash become the new source-of-truth references. Do not keep using the baseline hash above after the official baseline changes.

---

## 1. SOURCE OF TRUTH — ONE CANONICAL BASELINE

1. Start each development run from the exact, latest **officially accepted Full Source**, not from a stale working directory, Patch, report, screenshot or remembered file listing.
2. Verify the input ZIP CRC, SHA-256 sidecar, root folder, packaged file count, manifest version and version ledger before editing.
3. Keep one canonical source tree, one working tree and one release candidate. Two ZIPs with the same version but different hashes are different branches, not interchangeable copies.
4. Compare alternate uploads path-by-path. Cherry-pick only individually verified improvements; never overlay an entire alternate branch without a full review.
5. A working folder or candidate manifest is not an official release. It becomes official only after the applicable Source Release gates in Section 14 pass and the owner accepts it.
6. Preserve the exact base source and its hash in every Change Manifest and Patch metadata record.
7. If source bytes are inaccessible, do not claim source changes, tests, cleanup or packaging. Perform only useful source-grounded research from available materials and state what is blocked.
8. Do not infer a source's contents from its filename, a past assistant report or a previous candidate's summary. Reopen the exact source.

## 2. PRODUCT IDENTITY AND ARCHITECTURE — DO NOT DRIFT

- Product: TOEIC Dictionary PWA, focused on TOEIC Listening and Reading.
- Deployment architecture: GitHub Pages / GitHub-only static PWA.
- No Cloudflare, application backend, GAS, iframe, server-side database or external learner-data service.
- Preserve the current local-first model and browser/device SpeechSynthesis behavior.
- TOEIC Speaking/Writing, IELTS and other future curricula remain deferred unless the owner explicitly changes scope.
- The UI is frozen. Do not redesign, add menus, restructure navigation, alter the design system or make cosmetic changes without a reproduced defect and a narrowly scoped fix.
- Existing learning areas remain compatible: vocabulary, flashcards, review, grammar, listening, reading, Part 5 practice, Mock, Foundation, Robot Buddy, local progress and PWA offline/update lifecycle.
- Robot Buddy remains an offline, bundled-content companion under its existing privacy boundary. Do not claim it is a generative AI service or allow it to read personal progress outside the existing opt-in, read-only in-memory evidence flow.

## 3. DATA PRESERVATION — HIGHEST PRIORITY

Unless a verified defect and an explicitly approved migration justify a narrowly scoped change, preserve byte-for-byte:

**Canonical vocabulary**
- The 1,141 A–Z canonical headwords and their stable vocabulary IDs.
- Canonical sense structure, POS and existing synonym/antonym relationship arrays.
- Existing word-family links and source provenance.

**Learning and assessment data**
- Listening, Reading, Grammar, Part 5, Foundation and Mock resource/question identities.
- Question IDs, choice IDs, answer indexes/keys, evidence pointers and eligibility states.
- Editorial reserve classifications and separate practice-only banks.
- Existing learner attempts/history and assessment records.

**Learner storage**
- IndexedDB database `toeic-vocabulary-phase1`, schema version `1`, store `workspace`.
- Existing localStorage keys, vocabulary progress, saved words, review history, attempts, Mock history and user settings.
- Do not reset, rename, replace, clear or migrate learner storage as a convenience for tests.

Any required schema migration must have a separate approved plan, additive/backward-compatible design, fixture-based migration tests, preservation checks and recovery/rollback evidence. A backup does not authorize destructive testing against real learner data.

## 4. PRIORITY ZERO — BASELINE GOVERNANCE AND KNOWN DEFECTS

Before broad feature or content expansion, inspect and close foundational integrity issues:

1. Version/documentation markers must agree with `data/manifest.json` and the official version ledger.
2. `docs/COMPATIBILITY.md`, README, Master Status and Manual Acceptance Checklist must describe the current source, not stale v2.95.9/v2.95.15-era markers.
3. Editorial Review Queue figures must be computed from source records through shared metrics, not copied literals. Baseline values to verify against v2.95.45 are Listening 102 eligible + 193 reserve = 295 total; Part 7 reserve 87; separate Part 5 practice-only bank 80. These are regression baselines, not permanent hardcoded report values.
4. Listening reserve, Part 7 reserve and Part 5 practice-only classifications must remain separate and fail closed. Never promote reserve items to Mock eligibility from an audit or generated report.
5. Dynamic test discovery, test execution evidence, checkpoint compatibility and source fingerprint scope must be reliable before trusting a resumed full-suite result.
6. Major Release Audit must distinguish cumulative inventory/provenance counts from changes made by the current release.
7. Documentation cleanup must retain source ledgers, test fixtures, open review handoffs, accepted runtime contracts and reproducible historical evidence.
8. Inspect all candidate worktrees before a new batch. Reuse verified work; do not create duplicate or parallel version branches.

## 5. DEVELOPMENT PRIORITIES — LARGE, COHERENT BATCHES

Choose substantial work with a clear dependency and measurable quality outcome. Combine compatible tasks; avoid one-feature-per-session and cosmetic version bumps.

Recommended order:
1. Baseline/source integrity and acceptance governance.
2. Editorial Review Queue, metrics and classification integrity.
3. Dynamic test inventory, sharded execution and checkpoint integrity.
4. Vocabulary semantic accuracy and Related Glossary completion.
5. Placeholder English definitions, POS and sense alignment.
6. IPA/pronunciation accuracy, word family, verb forms and collocations.
7. Synonym/antonym quality and relationship graph.
8. Listening and Reading evidence, editorial quality and distractors.
9. Grammar, Part 5 and answer explanations.
10. Learning Outcomes instrumentation, validation and test coverage.
11. Performance, offline, Service Worker and PWA update reliability.
12. Final Source Release and Production Deployment acceptance.

Do not inflate counts merely to show progress. A smaller set of verified, context-accurate improvements is preferable to a larger set of uncertain content.

## 6. CONTENT RESEARCH AND PROVENANCE

Use reliable, item-level sources such as Cambridge Dictionary, Oxford Learner's Dictionaries, Merriam-Webster, Longman or other suitable authoritative references.

Every new or materially corrected content record must retain:
- Exact headword/phrase and intended sense.
- Part of speech and context/sense note where needed.
- English definition, Vietnamese meaning and the relation/context it supports.
- Specific source URL and retrieval/review date.
- Provenance/batch identifier and whether independent editorial review is pending or complete.

Never invent or misattribute meanings, examples, IPA, pronunciation variants, collocations or word-family relations. Do not infer synonymy from spelling similarity, derivation or a broad topic association. Do not auto-apply ambiguous pronunciations. Distinguish a dictionary's multiple senses and do not blend unrelated meanings into one glossary record. Search-index excerpts or snippets must be labelled accurately when the full source page could not be inspected. Pending content must stay pending until reviewed.

## 7. VERSION CONTROL — ONE RELEASE SEQUENCE

- One official current release and one immediately previous official release.
- A new version is justified by a coherent, verified batch, not by every small edit, report refresh or failed test retry.
- Never create two Full Sources with the same version but different content/hashes.
- Do not silently reuse a version number from an unverified candidate branch.
- Keep `data/manifest.json`, runtime/cache markers, README, Master Status, Changelog, Current/Previous Version and release reports synchronized.
- Do not mark a candidate as accepted merely because version labels or ZIPs exist.
- A blocked candidate may be delivered for review only as `ACCEPT WITH FIXES` or `BLOCK RELEASE`, never mislabeled as a completed official release.
- Preserve previous version lineage; update Previous Version only when the new Source Release is accepted.

## 8. DEVELOPMENT EXECUTION — IMPLEMENT, DO NOT JUST PLAN

For every run:
1. Read this guide and inspect the latest accepted source.
2. Verify baseline hashes and current/previous version state.
3. Inspect the active backlog, Master Status, changelog, latest test report and open review items.
4. Inspect existing candidate work and avoid repeating completed changes.
5. Select one coherent large batch and state its scope internally before editing.
6. Implement real source changes, not only an audit or a plan, whenever source bytes are available.
7. Add/update regression tests for each behavior/data change.
8. Run the relevant tests, validators and audits; keep exact command/exit evidence.
9. Update Master, Changelog, Current/Previous Version (only when acceptance allows), test/command logs and release reports.
10. Package only when the tree is changed and verifiable; replay the Patch against the immediate previous official source.
11. Report completed, failed, incomplete, not-run and unverified work separately.

If the source is unavailable, do not simulate implementation or fabricate a release. Perform verified research and give concrete candidates with sources, or explain the exact blocker.

## 9. TEST AND RELEASE GATES

Run all relevant checks, including:
- Python test inventory and sharded suite.
- JavaScript regression suites and Node syntax checks.
- Python compile checks.
- Vocabulary/data validator and learning-content validator.
- Repository integrity and version synchronization.
- Editorial review queue metrics and classification tests.
- Listening readiness, question evidence and distractor audits.
- Related Glossary candidate/backlog/quality and vocabulary relationship graph audits.
- Learning Outcomes evidence and objective-resource audits.
- Major Release Quality Audit and Release Acceptance Runner.
- Package CRC/root/exclusion/hash and Patch replay checks.

Record exact commands, exit codes, test counts and timeouts. A timeout, incomplete discovery, import/collection error or unrun module is not PASS. A focused green subset does not prove a full-suite pass. Remote GitHub Actions, GitHub Pages, actual browser offline behavior and real-device tests remain unverified until directly performed.

## 10. FULL SOURCE, PATCH AND CHECKSUMS

When source artifacts have actually changed and the package can be verified, deliver:
- One FullSource ZIP with one root directory.
- One Patch based on the immediately previous official FullSource.
- FullSource and Patch SHA-256 sidecars.
- Change Manifest and Package Verification.

Patch requirements:
- Record added, modified and deleted paths.
- Include an explicit, safe deletion manifest when files are removed; never rely on overlay extraction alone to delete old files.
- Replay onto a fresh extraction of the exact previous official FullSource.
- Compare every resulting path and file byte-for-byte with the candidate FullSource.
- Require zero missing, extra or mismatched files.
- If replay or hash validation fails, BLOCK RELEASE.

## 11. REPORTING CONTRACT — EVIDENCE, NOT CLAIMS

Every batch report separates:

**Completed:** exact files/records changed, metrics before/after, tests actually executed and package/replay evidence.

**Failed/incomplete:** failing assertions, import/discovery errors, timeouts, interrupted commands, pending modules and unresolved source issues.

**Not run/unverified:** remote CI, GitHub Pages deployment, cache/CDN, browser/device workflows, native TTS behavior and independent editorial review unless directly verified.

Distinguish module counts from test-case counts. Distinguish cumulative inventory metrics from release deltas. Cite content sources and retain provenance. Never copy old counts into a new report without recalculating from current source.

## 12. DEFINITION OF DONE AND DEVELOPMENT OBJECTIVE

The objective is a stable, accurate, maintainable TOEIC learning PWA, not a large sequence of version labels.

A batch is complete only when:
- The intended implementation is present and reproducible.
- Protected data remains intact or an explicitly approved migration is verified.
- Relevant tests and validators have actual results.
- Documentation accurately describes current behavior and limitations.
- Source lineage and package replay are verifiable when packages are issued.
- Outstanding work remains visible in the Master/backlog.

Do not call the product production-ready unless the Production Deployment Acceptance gates pass.

## 13. DYNAMIC TEST INVENTORY AND ENVIRONMENT CONTROL

The v2.95.45 baseline contains **88 Python test modules**. This is a baseline reference, not a permanent limit.

- Dynamically discover every Python test module under all explicitly approved test roots.
- Keep approved roots, discovery patterns and exclusions explicit and version-controlled.
- Compare each candidate inventory with the accepted baseline.
- Report added, removed, confirmed-renamed and suspected-renamed modules. A rename requires evidence; do not infer it solely from a matching count.
- Never silently exclude a newly added module.
- Discovery/collection/import failure is a failure, not an empty successful inventory.
- Run each module in isolation with bounded timeout and process-group cleanup.
- Continue inventory execution after a module fails so the final report accounts for all modules.

### 13.1 Test Inventory Baseline

Maintain a versioned test inventory baseline containing normalized module paths and content hashes. Record the baseline version and compare it to each dynamic discovery. Update the accepted baseline only as part of an accepted release; never update it merely to hide removed or failing tests.

### 13.2 Execution Environment

Record Python/Node versions where relevant, OS, architecture, test runner hash, dependency/lockfile hashes, exact command and arguments. Do not store credential values or other secrets. A missing runtime or incompatible environment must be explicit.

### 13.3 Terminal States

Every discovered module receives exactly one terminal state:
- `PASS`
- `PASS WITH SKIPS`
- `FAIL`
- `TIMEOUT`
- `ERROR`
- `NOT RUN`

For strict release verification: zero `FAIL`, `TIMEOUT`, `ERROR` or `NOT RUN`. `PASS WITH SKIPS` is allowed only when every skipped test name/reason is recorded and the release policy explicitly accepts that environment-dependent skip. No module with zero collected tests may pass unless a reviewed empty-module policy exists.

### 13.4 Full Suite Completion

All discovered modules must reach a terminal state. Specifically confirm long-running and previously problematic modules such as `test_patch_data.py` and `test_validator.py`. Resume only from a compatible checkpoint. Do not convert partial runs, timeouts or import errors to PASS.

### 13.5 TEST INVENTORY AND EXECUTION EVIDENCE

- Approved test roots and exclusion rules must be explicitly defined and version-controlled.
- Every discovered test module must include test case counts.
- Record total discovered, collected, passed, failed, skipped, errored and deselected test cases.
- Record every skipped test name and reason.
- Discovery, collection, import, setup and teardown failures must be recorded explicitly.
- Discovery or collection failures must never be classified as PASS.
- A module with zero collected tests must not be PASS without an explicit verified empty-module policy.
- Test case counts must come from the actual test framework, not static estimates.
- Distinguish discovery, collection, execution and final status for each module.
- File permissions, symbolic links and normalized paths must be handled consistently by source fingerprinting.
- Symbolic links must not escape approved roots or create recursive traversal loops.
- Normalize Unicode and path separators consistently; detect normalized/case-folded path collisions.
- Environment fingerprints must never expose credentials, tokens, passwords, private keys or other secret values. Do not store ordinary hashes of low-entropy secrets.
- Record per module: normalized path, discovery/collection/execution statuses, counts, exit code, duration, command, skip names/reasons and log reference.
- Report module counts separately from test-case counts.

### 13.6 CHECKPOINT AND SOURCE SCOPE

Maintain two distinct deterministic fingerprints:

**`SOURCE_RELEASE_FINGERPRINT`** represents every file included in the actual release package.

**`TEST_INPUT_FINGERPRINT`** represents source, tests, shared helpers, data, configuration, runner, dependencies and environment inputs that affect the test result.

- Define both scopes exactly in `tools/source-fingerprint-policy.json` and `tools/test-inventory-policy.json`; review any change to either policy as a source-governance change.
- List generated outputs excluded from test-input fingerprints; never exclude a file merely because it fails.
- Preserve deterministic file ordering and normalized relative paths.
- Include file content hashes, file size, file type and relevant permission metadata.
- Record symbolic link targets without following links outside approved roots.
- Do not use unstable timestamps or owner/group metadata unless a proven build dependency requires them.
- Keep generated logs/checkpoints out of their own input fingerprint to prevent self-invalidation. The explicit `exclude_patterns` list may exclude only named generated release-evidence reports from `SOURCE_RELEASE_FINGERPRINT`; those files remain inside FullSource and are still covered by ZIP CRC and the final FullSource SHA-256. Ordinary source, policy, tests, data, provenance and active documentation must never be excluded to avoid a failure.
- Record runtime/dependency fingerprints and exact test command/arguments.
- A checkpoint PASS may only be reused when its source and execution environment are proven compatible.
- Development resume may reuse a module only when its relevant dependency fingerprint is unchanged and the reason is recorded.
- Strict Release Verification must invalidate all checkpoints whenever the full source tree fingerprint changes.
- Any uncertainty about source, environment, dependency or command compatibility results in invalidation and rerun.

## 14. SOURCE RELEASE AND PRODUCTION ACCEPTANCE

Maintain two separate acceptance levels. Never describe source-only acceptance as production acceptance.

### 14.1 SOURCE RELEASE ACCEPTED

All mandatory gates must pass:
- Official source lineage and source fingerprint.
- ZIP/tree integrity and version synchronization.
- Data and learning-content validators.
- Complete dynamic Python inventory under the strict release policy.
- JavaScript regression and syntax checks.
- Repository, content and quality audits.
- Protected-data integrity.
- Release Acceptance Runner.
- Patch replay byte-identical to the candidate FullSource.
- FullSource/Patch SHA-256 and package verification.
- Current Master, Changelog, test report, command log, Change Manifest and release notes.

Source Release Accepted means the source package passed its engineering/data gates. It does not prove a remote deployment or real-device behavior.

### 14.2 PRODUCTION DEPLOYMENT ACCEPTED

Requires Source Release Accepted plus direct evidence of:
- GitHub Actions success.
- GitHub Pages deployment success and deployed commit/artifact identity matching the accepted source.
- Application smoke tests across core navigation and learning workflows.
- Valid PWA manifest and successful Service Worker install/activation/update.
- Cache namespace/version agreement and safe old-cache cleanup.
- Offline behavior after a completed online cache warm-up, plus reconnect/recovery.
- IndexedDB continuity across application update.
- Critical desktop and mobile workflows on actual supported browsers/devices.

### 14.3 ACCEPTANCE EVIDENCE

Record release version, source fingerprint, commit/deployment identity, deployment URL, command/results, browser/OS/device/screen, logs or screenshots and all failed/unverified checks. If deployment/device access is unavailable, mark it `UNVERIFIED`; do not infer success from local ZIPs or simulated tests.

### 14.4 NON-DESTRUCTIVE PRODUCTION TESTING

- Production smoke tests must use isolated test data or dedicated test profiles.
- Never reset or overwrite real learner progress during acceptance testing.
- IndexedDB migration and recovery tests must use controlled test fixtures.
- Any destructive test must be restricted to an isolated environment.
- Test cleanup must not affect existing learner records, review history or Mock history.
- Use a dedicated browser profile, test device or isolated automation context. A different URL path on the same origin does not isolate IndexedDB.
- Use synthetic, identifiable test-owned records and record pre/post fixture state.
- Validate that cleanup only removes data created by that test profile.
- Never clear the user's site data, full IndexedDB database/store or all localStorage as part of acceptance.
- If isolation cannot be guaranteed, mark the test `BLOCKED` or `NOT RUN`, never `PASS`.

## 15. FUTURE PROMPT INTAKE AND ANTI-DRIFT RULES

Every new user prompt is a task request inside this Master contract, not a new architecture or baseline by implication.

1. Read this guide, Current/Previous Version, Master Status, active backlog and latest test report before selecting work.
2. Interpret the new prompt as the requested outcome and scope; retain all unchanged project constraints from this guide and earlier approved requirements.
3. Do not ask the owner to repeat a requirement already documented here or in the current source.
4. If a new request conflicts with a protected constraint (UI freeze, GitHub-only, learner-data protection, stable IDs/answer keys, source lineage or release gates), stop that conflicting change, explain the conflict and propose the narrowest safe alternative. Do not silently override the contract.
5. A user may explicitly approve a policy change; record it in Master Status, Compatibility and Changelog before implementation.
6. Reconcile every requested task with current source, completed work and backlog to avoid duplicate implementation.
7. Choose one substantial, coherent batch and combine compatible fixes. Do not create one version per small correction.
8. Maintain one canonical working tree and one candidate version. Never create parallel branches or same-version/different-hash packages.
9. If a request asks only for plans, provide a plan; otherwise implement real changes when the source is accessible.
10. Report unchanged/no-match results honestly. Do not invent source files, test outputs, citations, package paths or deployment outcomes.
11. After each run, leave the project in a clear state: official baseline, candidate (if any), completed work, active backlog, failed/incomplete checks and exact next step.
12. Do not schedule more work or create background runs unless the owner explicitly asks for automation.

**Reusable instruction for a future task:**

> Continue TOEIC Dictionary PWA development under `docs/MASTER_DEVELOPMENT_PROMPT.md`. Use the latest officially accepted FullSource from `docs/versions/CURRENT_VERSION.md` and verify its SHA-256 before editing. Read Master Status, Changelog, active backlog and latest test evidence. Treat my new request as the next task scope without overriding the Master contract. Select one substantial compatible batch, avoid duplicate work/version branches, preserve UI and learner data, implement and test real changes, update documentation, and deliver evidence-based status. If source is inaccessible, do not pretend to edit or release it.

---

**Ownership rule:** this file is the single master development contract. Update this file when the owner explicitly approves a policy change; do not create parallel master prompts, competing roadmaps or multiple “final” instruction files.
