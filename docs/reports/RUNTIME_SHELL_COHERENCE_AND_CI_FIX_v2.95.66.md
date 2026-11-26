# Runtime Shell Coherence and CI Fix — v2.95.66

## Reported symptoms

- Browser reported `Cannot read properties of null (reading 'addEventListener')` at `bindEvents()` around the modal-layer listener.
- The user inspected the current page and found v2.95.65 title, `modalLayer: true`, `legacyModalBackdrop: false`, but the runtime error remained.
- GitHub Actions stopped at Batch 022 because its test expected a literal source path string even though workflow execution uses `unittest discover`.

## Root cause addressed

The PWA used cache-first handling for static scripts/styles while the root HTML navigation could return a fresh network document from the active older Service Worker. This permitted a mixed shell: newly deployed HTML alongside old cache-first application JavaScript (or the reverse after a partial update). Presence of `#modalLayer` in the inspected DOM did not prove the app module came from the same release.

## Fixes

1. Add a release marker to HTML and assert it matches `APP_RELEASE_VERSION` before `bindEvents()` executes.
2. Release-key the HTML entry module/styles/manifest and all local ES-module dependency URLs.
3. Add a second `__shell` key to data requests. An older worker that strips only `__release` still sees a new, non-colliding cache key; the current worker strips both keys inside its own versioned cache so canonical data remains reusable offline.
4. Make the root navigation use the active worker's cached `index.html` while an updated worker is waiting for user approval. It no longer returns freshly deployed HTML under an older worker's cache-first static assets.
5. Guard the `#modalLayer` click listener, and add a static `bindEvents` DOM inventory test.
6. Correct Batch 022 and Batch 023 test contracts to verify the exact `unittest discover` command used by the workflow.
7. Update `validate-data.py` to remove query/fragment components only for filesystem existence checks, retaining the versioned URL identity for service-worker checks.

## Verification

- 100/100 Python modules excluding the heavy validator module: 727/727 test cases PASS.
- Validator's two new release-query tests: 2/2 PASS.
- Full `test_validator.py` (44 test methods) did not complete within the available execution window; the first 21 cases passed before the next case exceeded the limit. This module remains INCOMPLETE and is not represented as PASS.
- All Node regression scripts: 43/43 PASS.
- Data validator: 1,141 records, 0 errors/warnings, no ID changes.
- Learning content: 0 errors/warnings; Part 1 photos: 9/9; repository integrity: 405 references with 0 errors/warnings.
- Version synchronization: 18/18; JavaScript syntax and Python compileall pass.

## Acceptance still required

The branch must run on GitHub Actions, Pages must deploy v2.95.66, and an existing installed PWA with an old active Service Worker must accept the waiting update. A follow-up browser console check should show:

- `document.title` includes `v2.95.66`.
- `document.getElementById('modalLayer')` is present.
- `document.getElementById('modalBackdrop')` is absent.
- The app module resource URL contains `?__release=2.95.66`.
- The rendered app starts without a `bindEvents()` null-listener error.

Do not clear IndexedDB or site data to perform the update test; learner records remain local and must be preserved.
