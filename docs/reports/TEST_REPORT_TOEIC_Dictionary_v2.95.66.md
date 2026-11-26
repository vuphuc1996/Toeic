# Test Report — TOEIC Dictionary v2.95.66

## Baseline

- Sole predecessor: `TOEIC_Dictionary_v2.95.65_FullSource.zip`.
- SHA-256: `a1b95e807e08052bfa599a08ff88bc3237ae086688557ce3ae77b78e814814fb`.
- Source was reconstructed from this exact one-root archive; no earlier archive, Patch or alternate branch was used as the baseline.

## Verified results

| Validation | Result |
|---|---:|
| Python sharded suite, excluding `test_validator.py` | **100/100 modules PASS; 727/727 tests PASS** |
| Python failed / skipped / errored cases in those 100 modules | 0 / 0 / 0 |
| Batch 022 | 9/9 PASS |
| Batch 023 | 9/9 PASS |
| Batch 035 wildcard (both modules) | 10/10 PASS |
| Release shell coherence | 6/6 PASS |
| `bindEvents` DOM contract | 4/4 PASS |
| CI coverage contract | 8/8 PASS |
| PWA readiness | 3/3 PASS |
| Design system | 19/19 PASS |
| `test_validator.py` release-query cases | 2/2 PASS |
| Node regression scripts | 43/43 PASS |
| JavaScript syntax (`sw.js` and every `assets/js/*.js`) | PASS |
| Python compilation (`python -m compileall -q tools`) | PASS |
| Version synchronization | 18/18 markers PASS |
| Repository integrity preflight | 405 references/data files; 0 errors, 0 optional warnings |
| Data validator | 1,141 canonical records; 0 errors, 0 warnings; 0 IDs added/removed |
| Learning-content validator | 0 errors, 0 warnings |
| Part 1 photo validation | 9/9 PASS |
| Design-token audit | 0 new violations; 2,773 legacy findings retained as warnings |

The 100-module Python result is recorded with source/test/environment fingerprints and per-module results in `PYTHON_TEST_SHARDS_v2.95.66.md`.

## Explicitly incomplete Python module

`tools/tests/test_validator.py` contains 44 test methods and did not complete as one module within the available execution window. In a full-module attempt, its first 21 tests completed successfully; the next case exceeded the execution window before the module could emit a final unittest summary. The two newly added release-query cases were run separately and both passed (2/2). The production `python tools/validate-data.py` command also passed with zero errors and zero warnings.

Consequently, this release does **not** claim full 101/101 Python module discovery PASS. The correct status is 100 modules PASS and one module INCOMPLETE; no failed test cases were observed in the completed Python shards.

## Scope and data preservation

- HTML, app module, local ES-module imports, stylesheets, manifest and Service Worker core cache URLs are release-keyed to v2.95.66.
- Data requests carry both `__release` and `__shell`; the current worker normalizes both keys to its own canonical precache, while older workers retain `__shell` so the request does not alias an older cached data response.
- Root navigation served by an active worker stays on that worker's cached index until the waiting worker is approved. This prevents fresh HTML being combined with old cache-first JavaScript/CSS.
- A startup release-marker check prevents `bindEvents()` from running when HTML and JavaScript releases differ. The `#modalLayer` event listener is guarded, and the DOM contract inventories all required listeners.
- Batch 022 and 023 test contracts now assert the exact `unittest discover` invocation used by CI, instead of requiring an obsolete path literal.
- Only the version value changes under `data/manifest.json`. Canonical vocabulary and Related Glossary content, IDs, relations, questions, choices, answer keys, Mock eligibility, learner IndexedDB records/schema and Robot Buddy privacy boundary remain unchanged.

## External acceptance

GitHub-hosted Actions for the v2.95.66 branch, Pages deployment, update acceptance in a browser with an already-active old Service Worker, installed-PWA offline behavior and physical iOS/iPadOS/Android testing remain unverified until the branch is pushed, Actions completes and a real device is tested.
