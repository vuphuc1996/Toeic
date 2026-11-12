# TOEIC Vocabulary Batch 011 — Legacy Collocation Cleanup (v2.21.0)

- Date: 11/11/2026
- Base data version: v2.20.0
- Target version: v2.21.0
- Scope: 7 stable vocabulary IDs; 7 guarded `collocations` replacements; 8 legacy FD001 violations removed.
- Data integrity: 928/928 IDs preserved; ID-set SHA-256 remains `dd1705e64c8df4ad7ebca188a6ad856fff1d180d99730d2d77d2ba6fbdc12656`.
- No senses, definitions, examples, IPA, word-family fields, topics, Listening/Reading/Grammar content or question identities changed.

## Reviewed changes

| Stable ID | Previous collocations | Revised collocations | Rationale |
|---|---|---|---|
| `apprentice-n` | apprentice electrician; apprenticeship program | apprentice electrician; apprentice mechanic | Keep both examples as noun compounds with the headword, avoiding a derived noun that the direct-headword rule cannot trace. Collins documents “apprentice electrician” as a role. |
| `event-coordinator-n` | event coordinator; coordinate an event | event coordinator; assistant event coordinator | Keep role-name phrases for the noun; the old verb phrase was semantically related but not a direct collocation of the noun headword. |
| `fare-n` | airfare; bus fare | bus fare; one-way fare | Use two transparent fare phrases. Cambridge Business English documents “one-way fare”; airfare is valid English but the closed compound was a false negative for the boundary-based rule. |
| `replace-v` | replace a device; replacement part | replace a device; replace a battery | Keep verb + object patterns; Collins explicitly lists “replace a battery” among replace collocations. |
| `reserve-v` | reserve a room; make a reservation | reserve a room; reserve a seat | Keep verb + object patterns; Collins and Cambridge list “reserve a seat”. |
| `warehouseman-n` | warehouse staff; warehouse supervisor | assistant warehouseman; bonded warehouseman | Replace broad warehouse-role associations with compound job-title forms that contain the headword. A historical occupational dictionary defines assistant warehouseman and warehouseman, bonded. |
| `zero-based-budgeting-n` | zero-based budgeting process; zero-based budget | zero-based budgeting process; zero-based budgeting method | Keep phrases built from the exact headword; the second phrase no longer shifts to the related noun “budget”. |

## Guarded patch and baseline handling

- Patch file: `patches/v2.21.0/batch-011-collocations.json`.
- Guard: base data version, complete 928-ID set SHA-256, stable record IDs and exact old `collocations` values.
- Dry-run: PASS before apply.
- Apply: PASS, 7 operations across 6 A–Z JSON files.
- `python tools/validate-data.py` after apply: 0 ERROR; all 8 FD001 records reported as resolved.
- `python tools/validate-data.py --tighten-baseline`: removed exactly 8 resolved FD001 entries, added none.
- Final validator: 0 ERROR / 0 WARNING (legacy).

## Source notes

1. Collins Dictionary, “apprentice electrician”: https://www.collinsdictionary.com/dictionary/english/apprentice-electrician
2. Collins Dictionary, “event coordinator”: https://www.collinsdictionary.com/dictionary/english/event-coordinator
3. Cambridge Dictionary, “one-way” (Business English entry gives “one-way fare”): https://dictionary.cambridge.org/dictionary/english/one-way
4. Collins Collocations, “replace”: https://www.collinsdictionary.com/dictionary/english-collocations/replace
5. Collins Collocations, “reserve”: https://www.collinsdictionary.com/dictionary/english-collocations/reserve
6. Dictionary of Occupational Terms, “940.—Warehousemen” (assistant warehouseman; warehouseman, bonded): https://doot.spub.co.uk/code.php?value=940
7. Howard County Public School System, Zero-Based Budgeting Overview: https://www.hcpss.org/f/aboutus/zbb_manual.pdf

These sources support phrase formation and role/term usage; they do not constitute a complete TOEIC frequency ranking. No official ETS vocabulary list is implied.
