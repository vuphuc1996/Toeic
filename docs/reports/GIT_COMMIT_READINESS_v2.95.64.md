# GitHub Commit Readiness — TOEIC Dictionary v2.95.64

**Date:** 2026-11-25
**Exact source predecessor:** `TOEIC_Dictionary_v2.95.63_FullSource.zip`
**Predecessor SHA-256:** `6d43a7f44e1cc84d6ad7f3ee9dae660cceb83c792668d0966ce1060f4aa9ea80`

## Scope delivered

This batch hardens the commit/CI path rather than changing learning content or the interface.

1. `tools/audit-git-commit-readiness.py` is a dependency-free, read-only Git preflight. `--staged` checks a proposed local commit before commit; `--require-clean` checks a clean checkout/committed state in CI. It validates indexed paths, case-insensitive path collisions, Windows-reserved names/characters, symlinks, tracked release archives/checksum sidecars, file sizes, generated-path ignore rules, LF/binary attributes and whitespace/conflict markers in only the staged/current commit diff. It never stages, commits, resets or edits files.
2. `.gitignore` now excludes Python bytecode and test caches, virtual environments, local logs/coverage/editor files, OS metadata and generated release ZIP/checksum/tar artifacts.
3. `.gitattributes` normalizes text files to LF and marks common media/archive formats as binary. This avoids relying on a developer's `core.autocrlf` setting.
4. GitHub Actions external dependencies are pinned to full commit SHAs:
   - `actions/checkout` v7.0.1 — `3d3c42e5aac5ba805825da76410c181273ba90b1`
   - `actions/setup-python` v7.1.0 — `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`
   - `actions/setup-node` v7.1.0 — `949feb2413d6458794dcd2491c4babbbce0c15c1`
5. Checkout fetch depth is 2 so the CI preflight can inspect the new commit against its parent without scanning historical whitespace issues. `.gitignore` and `.gitattributes` are included in both push and pull-request workflow path filters.
6. Repository integrity now understands the default Python `unittest discover` pattern (`test*.py`) as well as explicit `-p` selectors. CI coverage tests detect omitted Python/Node modules, duplicate unittest selectors and duplicate step labels. The Batch 035 wildcard remains covered.
7. The explicit Python syntax file list is replaced with `python -m compileall -q tools`, so newly introduced helpers and test modules are included automatically.
8. Duplicate executions of `test_related_glossary_batch_021.py` and `test_missing_ipa_safe_backfill.py` were removed; each module remains covered by a single CI test invocation (the full-suite discovery step remains present).

## Local verification

- New Git integration suite: **10/10 PASS**. Temporary repositories covered clean commit, staged changes, unstaged changes, untracked files, whitespace, case-collision, Windows-reserved name and release-artifact blocking.
- CI coverage suite: **8/8 PASS**.
- Repository-integrity suite: **2/2 PASS**; its live preflight: 363 references/data files, 0 errors, 0 optional warnings.
- Package-source suite: **3/3 PASS**.
- Python shard-runner suite: **19/19 PASS**.
- Release-acceptance-runner suite: **10/10 PASS**.
- Version-sync suite: **12/12 PASS**.
- YAML parsed locally; 124 steps, every step contains `run` or `uses`, no duplicate step names, no unpinned actions.
- All 43 Node regression scripts: **43/43 PASS**; `sw.js` and all `assets/js/*.js` syntax checks PASS.
- `python -m compileall -q tools`: PASS.
- Data validation: 1,141 records; 0 errors, 0 new-debt errors and 0 legacy warnings.
- Learning-content validation: 0 errors, 0 warnings. Part 1 photos: 9/9 PASS.
- Version synchronization: all 13 markers PASS.
- Current data inventory differs from v2.95.63 only at `data/manifest.json` (version marker). No canonical vocabulary, Related Glossary, question, choice, answer-key or learner-data file changed.

## Incomplete / unverified

- The complete 97-module Python shard run was started. The environment's outer command window expired after **19 modules / 144 test cases passed**, with 78 modules still pending in the saved checkpoint. The overall suite is **INCOMPLETE**, not PASS. Two subsequent isolated Foundation A2 modules passed 8/8 each, but this does not convert the full suite to PASS.
- GitHub-hosted Actions has not been run from this conversation; the workflow configuration and its local contract tests pass.
- Actual Windows/macOS GUI-client commits, deployed GitHub Pages and PWA cache/offline propagation remain unverified.

## Local pre-commit sequence

```bash
git add -A
python tools/audit-git-commit-readiness.py --staged
python tools/audit-repository-integrity.py
python tools/sync-version.py --check
git diff --cached --check
git commit -m "Release TOEIC Dictionary v2.95.64"
python tools/audit-git-commit-readiness.py --require-clean
```

The project FullSource/Patch package process must still be run from a clean committed tree. Do not commit release ZIPs or `.sha256` sidecars; they are generated outside the repository and are ignored if copied into it.

## Official action release references

- https://github.com/actions/checkout/releases/tag/v7.0.1
- https://github.com/actions/setup-python/releases/tag/v7.1.0
- https://github.com/actions/setup-node/releases/tag/v7.1.0
