# PWA Release Coherence and Batch 022 CI Fix — v2.95.66 candidate

## Root cause: mixed HTML / app.js release

The supplied browser console values showed v2.95.65 HTML, modalLayer: true, and legacyModalBackdrop: false. The running app module was fetched at the stable URL assets/js/app.js.

GitHub history shows the exact stale expression:
$('#modalBackdrop').addEventListener('click', ...)
exists at app.js v2.95.64 line 2135, around column 170. v2.95.65 HTML removes that node in favor of modalLayer, and v2.95.65 app.js binds #modalLayer.

The v2.95.65 Service Worker used cache-first lookup for same-origin non-data assets. The HTML script URL did not carry a release query, so an older worker could return its cached app.js while navigation delivered the newer HTML shell. The app then attempted to bind a listener to a DOM element that no longer existed.

## v2.95.66 correction

- Add meta name="toeic-release" content="2.95.66".
- Load app CSS, design-system CSS and app.js with ?v=2.95.66.
- Precache the same versioned URLs in Service Worker REQUIRED and APP_SHELL.
- Keep the Service Worker registration URL stable at ./sw.js and retain updateViaCache: 'none', allowing the browser to update the script in the existing scope without creating URL churn. The versioned CSS/JS requests, not a changing worker URL, isolate app-shell cache keys.
- Before bindEvents(), require the HTML release marker to match APP_RELEASE_VERSION. On mismatch, log a specific release-coherence error, display the existing update banner with a reload action, and stop initialization rather than producing a misleading null-listener failure.
- Fix Batch 022's CI test to validate the actual unittest discover selector with glob semantics.
- Update PWA readiness to strip query parameters from local asset paths.
- Add release-asset-coherence.mjs and register it in GitHub Actions.

## Data / UX boundary

No learner data, IndexedDB schema, question/answer data, vocabulary/glossary content, Mock eligibility or UI layout was changed. The change affects static asset identity, startup mismatch handling, CI assertions and release documentation only.

## Test status

Hosted Actions and physical PWA/device acceptance are pending. See the v2.95.66 Test Report and Command Log Index; no skipped or pending checks are represented as passing.
