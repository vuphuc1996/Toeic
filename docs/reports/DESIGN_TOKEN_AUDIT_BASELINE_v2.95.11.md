# CSS design-token ratchet — v2.95.11

## Scope and method

The audit scans only `assets/css/app.css` and `assets/css/design-system.css`. It strips CSS comments, parses selector declarations and `@media` width conditions, and records violations by the composite identity `(rule, file, selector, property)`, together with exact violating value(s) and occurrence count. Existing identities are warnings; a new identity, a new value on an existing identity, an increase in occurrences, or a changed rules-file SHA-256 is an error. The audit never rewrites the baseline.

`tools/design-token-rules.json` is the canonical ruleset input. `tools/design-token-baseline.json` stores the ruleset SHA-256. This makes edits to allowed font weights, color tokens, radii, shadows or breakpoint boundaries raise `RULE-DRIFT` until the policy is separately reviewed. The one-time `--bootstrap-baseline` option refuses to overwrite an existing baseline.

## Reproducible scan of the v2.95.10 CSS

| Measure | Claude's independent report | Local scanner before update-banner tokenization | Local scanner after tokenization |
|---|---:|---:|---:|
| Distinct hex literals | 979 | 979 | 979 |
| Hex occurrences | 1,508 | 1,508 | 1,508 |
| Distinct `font-size` values | 128 | 128 | 128 |
| `font-size` declarations | 918 | 921 | 921 |
| Distinct `font-weight` values | Not stated | 9 | 9 |
| Nonstandard values 550/650/750/850/950 | 70 declarations | 70 declarations among the reported values | 70; there are also 19 declarations at 900, which violate the stricter five-weight rule |
| Distinct `border-radius` values | 47 | 47 | 47 |
| Distinct `box-shadow` values | 69 | 69 | 70 (the banner now references the canonical float-shadow token) |
| `!important` occurrences | 114 | 114 | 114 |
| Distinct media width values | 25 | 24 | 24 |
| `@keyframes` | 34 | 34 | 34 |

The local scanner intentionally reports its own exact declaration and media-query counts instead of adjusting them to Claude's figures. The three-item difference in `font-size` declarations and one-item difference in media width values remain a measurement-definition discrepancy; this does not affect the ratchet comparison because the baseline stores selector/property/value identities.

## Ratchet baseline and first migration

- Initial v2.95.10 baseline: **2,781 identities / 3,000 occurrences**.
- The update banner had three violations that were fixed using existing shared tokens: `.app-update-banner` radius and shadow, and `.app-update-copy strong` font size.
- Baseline was then tightened by deleting only those three fixed identities: **2,778 identities / 2,997 occurrences**.
- Current scan: 2,778 legacy warning identities, **0 new violations**, 0 baseline additions and 0 RULE-DRIFT.
- No bulk CSS conversion was performed. The rest of the legacy styles remain visible as warnings for incremental screen-by-screen migration after browser review.

## Tests and CI

`tools/tests/test_audit_design_tokens.py`: 8/8 PASS, covering compliant tokens, each disallowed CSS rule, legacy warning behavior, newly introduced violations, value changes on an existing selector/property, resolved findings, immutable baseline and RULE-DRIFT after a policy-parameter change. CI runs this suite and `python tools/audit-design-tokens.py` in a dedicated step. `test_ci_coverage.py` confirms every Python test module is registered in the workflow.

The update-banner change also passed the existing design profile, design system, responsive layout, visual composition, learning surface consistency and alphabet sound lab test modules. No browser screenshot or physical-device comparison was performed, so this is not visual acceptance.
