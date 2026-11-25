# Test report — TOEIC Dictionary v2.95.54

## Environment

- Runtime: Python 3.13.5 in the current local container. The independent Claude audit cited Python 3.12.3 and Node 22; this run is a separate environment and does not replace Claude's independent rerun.
- Source: exact v2.95.53 FullSource tree; no upstream `.git` metadata was supplied. A local Git baseline was initialized solely to satisfy per-task commit separation.

## Results

| Check | Result | Exit |
|---|---:|---:|
| Full discovery in reconstructed Git clone | 711 tests, 711 PASS, 0 FAIL, 0 ERROR, 0 SKIP | 0 |
| Full discovery from final clean FullSource archive | 711 tests, 710 PASS, 1 accepted SKIP, 0 FAIL, 0 ERROR | 0 |
| Full suite runtime | 135.824 s (clone); 135.701 s (clean archive) | 0 |
| Editorial review queue module | 8/8 PASS | 0 |
| Patch-data module | 20/20 PASS | 0 |
| Historical glossary 036 | 6/6 PASS | 0 |
| Historical glossary 037 | 7/7 PASS | 0 |
| Historical glossary 038 | 8/8 PASS | 0 |
| New verb-form validator cases | 4/4 PASS | 0 |
| New CEFR validator cases | 2/2 PASS | 0 |
| CI coverage | 3/3 PASS | 0 |
| Node syntax + runtime regressions | 40/40 `.mjs` scripts PASS; all `assets/js/*.js` and `sw.js` syntax PASS | 0 |
| Python syntax (`py_compile`) | PASS | 0 |
| `python tools/validate-data.py` | 1,141 records; 0 ID additions/removals; 0 ERROR / 0 WARNING | 0 |
| `python tools/sync-version.py --check` | all 13 version markers + changelog PASS | 0 |

The full discovery run was executed after the three historical vocabulary hash assertions and one patch-allowlist ordering assertion were updated to reverse the exact guarded v2.95.54 data patch in memory before comparing historical snapshots. No assertion was removed or weakened.

## Data deltas

- `appliance-n.verb_forms`: five empty strings → `null`.
- CEFR aggregate policy: word-level CEFR equals the highest valid sense-level CEFR in the order A1 < A2 < B1 < B2 < C1. Eight headword values corrected: `host-v` A2→B2; `supply-v` A2→B2; `bill-v` A1→A2; `document-v` A2→B1; `experience-v` A2→B1; `minute-n` A1→B2; `offer-v` A1→B1; `value-v` A2→B2. `package-nv` already met the rule and was unchanged.
- Manifest CEFR counts synchronized: A1 61, A2 234, B1 322, B2 402, C1 122.
- Vocabulary ID-set SHA-256 remains `adccbdb4c98872207d2bede7bdc530e1c079bbd8b3679e7e4f6288054c7e404b`.
- Listening reserve queue remains data-derived: eligible 102, reserve 193, total 295; all reserve units remain `reserve-pending-independent-review`.

## Unverified

- Remote GitHub Actions hosted execution and GitHub Pages deployment.
- Safari/iPad physical-device interaction, iOS PWA persistence, offline cache propagation and real TTS voices.
- Independent pedagogical review of CEFR estimates. The rule enforces internal consistency; it does not prove CEFR levels are pedagogically correct.
