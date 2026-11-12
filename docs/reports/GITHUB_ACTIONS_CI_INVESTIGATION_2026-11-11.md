# GitHub Actions CI Investigation — 11/11/2026

## Incident supplied by the user

- Repository: `vuphuc1996/Toeic`
- Workflow/check shown: `Validate TOEIC dictionary / validate (push)`
- Run: `42981524564`
- Job: `130392820806`
- Annotation: `Process completed with exit code 1`
- Reported elapsed time: 13 seconds
- Link supplied: `https://github.com/vuphuc1996/Toeic/actions/runs/42981524564/job/130392820806#step:14:37`

## What is confirmed locally on the v2.20.0 release candidate

1. `python tools/validate-data.py` completes with **PASS**: 928 records, 0 errors and 8 known legacy `FD001` warnings. These warnings are recorded in `tools/quality-baseline.json`; they are not new regressions and do not make the local validator exit non-zero.
2. `python -m unittest discover -s tools/tests -p 'test_choice_history.py' -v` completes with **5/5 PASS**.
3. The checked-in local workflow `.github/workflows/validate-data.yml` defines a job named `validate` and runs separately named Python/unit-test/validator/audit steps. Its 14th declared step is `Unit tests — choice_history` (counting from `Checkout` as step 1).
4. The local workflow invokes `python tools/validate-data.py` under `Validate vocabulary data (structure, ID integrity, APP_SHELL, ratchet baseline)`; it does not invoke `npm run validate`.

## What is not yet confirmed

- The remote run's exact failing step and terminal output are not available from the one-line annotation.
- The commit SHA, workflow file revision and branch state used by run `42981524564` have not been independently read from GitHub.
- Therefore it is not yet possible to determine whether the remote failure came from a unit test, a validator, a stale/different workflow, a missing file, or a commit that did not contain the complete release package.
- The local pass does not prove that the remote commit has identical files.

## Impact assessment

- A failed Actions check does **not** revert a push. The commit normally remains on the branch.
- It does not itself mutate vocabulary JSON or IndexedDB data, and it does not by itself make the deployed website fail at runtime.
- It may block a protected-branch merge or a deployment pipeline only where branch protection or deployment dependencies require this check to pass.
- Whether GitHub Pages deployed this commit is unverified; do not infer deployment success or failure from this check alone.

## Required diagnostic sequence

1. Read the run's commit SHA and confirm that it is the intended v2.20.0 commit.
2. Expand the failed step and capture the complete command plus the first traceback/assertion/error lines, not only the generic job annotation.
3. Compare the workflow revision in that commit with `docs`/source package `.github/workflows/validate-data.yml`.
4. Reproduce the exact failing command against that exact commit; fix the actual defect without disabling the validation gate.
5. Commit the correction and rerun Actions. Record remote PASS only after a green run is visible.

GitHub's documented workflow-log procedure is to open the run, select the job, inspect the automatically expanded failed step, and copy/download the relevant log lines. The GitHub connector was suggested but is not yet installed/connected in this session, so direct remote log inspection remains blocked.

## Status

**IN PROGRESS — root cause unconfirmed.** Local vocabulary validation and local choice-history tests pass. No application code, vocabulary records, IndexedDB schema, or release version was changed as part of this investigation.

## Follow-up mapping after the V2.21.0 work

- The V2.20.0 local workflow was enumerated: declared step 14 is `Unit tests — choice_history`; step 21 is `Validate vocabulary data (structure, ID integrity, APP_SHELL, ratchet baseline)`. Thus, if the supplied `#step:14:37` link refers to this exact workflow revision, it points to the choice-history unit-test step rather than the vocabulary validator. This mapping is conditional on the remote run using the same workflow file revision.
- Local choice-history suite: **5/5 PASS**. Local vocabulary validator after V2.21.0 Batch 011: **0 ERROR / 0 WARNING**. These results do not prove what happened in the remote checkout.
- V2.21.0 has added `Unit tests — legacy_collocation_cleanup` as declared step 20; it does not change the meaning of step 14.

## V2.23.0 follow-up hardening (same date)

The remote incident above remains unconfirmed because the exact run log and commit SHA were not accessible. Subsequent local work found and corrected two independent test-maintenance issues in the V2.22/V2.23 source line:

1. The v2.19 second-pass registry used a whole-file SHA-256 for `data/listening/listening-library.json`. Intentional Part 1 transcript alignments and additive reserve content caused that guard to fail even when historical reviewed questions were unchanged. V2.23 replaces that brittle guard with per-question fingerprints and per-unit fingerprints (unit payload excludes the question array), explicitly records the five approved P1 alignment edits, and requires all out-of-registry questions to carry `reserve-pending-independent-review`.
2. The V2.23 reserve additions initially caused the historic answer-position balance test to include new P3/P4 items in the old 132-question certificate. The test now filters pending reserve items from the historic distribution while separately validating their choice count, unique options, and answer index.

The general Service Worker validator was also corrected so missing `OPTIONAL` paths do not raise structural errors; `APP_SHELL`/required resources remain strict. A separate `validate-part1-photo-assets.py` step remains strict and will fail CI unless all eight actual JPG files exist, match the attribution manifest and meet the minimum dimensions.

Local V2.23 status: 177/177 unit-test methods PASS; `validate-data.py` 0 errors/0 warnings; learning-content validator 0 errors / 8 warnings solely because the 8 JPG bytes are absent from the local snapshot; strict photo asset gate remains pending (0/8 local JPGs). This is a verified local repair of the newer source line, **not proof that it explains remote run 42981524564**. The remote commit/workflow/log still require direct confirmation.
