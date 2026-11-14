# TOEIC Vocabulary Batch 020 — v2.30.0

**Base:** v2.29.0  
**Status:** added to canonical data locally; independent lexical/editorial review remains pending.  
**Scope:** Accounting and finance, logistics, inventory operations, contracts and HR records.

## 1. Added headwords

| ID | Headword | POS | Primary TOEIC meaning | Topic |
|---|---|---|---|---|
| `accrual-n` | accrual | noun | khoản phát sinh/tích lũy được ghi nhận theo kỳ | Finance |
| `receivable-adj` | receivable | adjective | còn phải được nhận/thu (khoản tiền) | Finance |
| `collateral-n` | collateral | noun | tài sản bảo đảm cho khoản vay | Finance, Legal |
| `escrow-n` | escrow | noun | thỏa thuận ký quỹ do bên thứ ba giữ tiền/tài sản | Finance, Legal |
| `consignor-n` | consignor | noun | bên gửi hàng | Shipping, Business |
| `consignee-n` | consignee | noun | bên nhận hàng | Shipping, Business |
| `stockout-n` | stockout | noun | tình trạng hết hàng để bán | Purchasing, Shipping |
| `bottleneck-n` | bottleneck | noun | điểm nghẽn làm chậm quy trình | Business, Technology, Shipping |
| `throughput-n` | throughput | noun | khối lượng xử lý trong một khoảng thời gian | Business, Shipping, Technology |
| `outlay-n` | outlay | noun | khoản tiền chi ra/chi phí đầu tư ban đầu | Finance, Business |
| `covenant-n` | covenant | noun | điều khoản cam kết trong hợp đồng/khoản vay | Legal, Finance |
| `timesheet-n` | timesheet | noun | bảng ghi số giờ làm việc | HR, Office |
| `replenishment-n` | replenishment | noun | việc bổ sung hàng đã dùng/bán | Purchasing, Shipping |

**Vocabulary total:** 979 → **992 canonical headwords**. Existing 979 IDs are retained; 13 new stable IDs are additive. The 26 A–Z JSON files remain the only runtime source; `batch-008.json` is provenance only.

## 2. Record-quality rules

- Each record has sense-specific POS, Vietnamese meaning, English definition, contextual example and Vietnamese translation, topic and relevant collocations.
- US IPA is included only where the checked dictionary page explicitly provides a US pronunciation. The Cambridge pronunciation pages checked for `consignor` and `receivable` do not show a US IPA value; those two fields are deliberately omitted instead of guessed.
- No forced word family, verb forms, synonym or antonym was added to these noun/adjective records when a natural supported value was unavailable.
- CEFR labels are editorial estimates, not official ETS classifications or independently certified CEFR levels.
- Examples and Vietnamese translations are original project-authored content, not copied dictionary examples.

## 3. Editorial source references

The sources were consulted for sense boundaries, business usage and/or US pronunciation. The source notes do not imply endorsement by the publisher.

- [Accrual — Cambridge](https://dictionary.cambridge.org/dictionary/english/accrual)
- [Receivable — Cambridge Business English](https://dictionary.cambridge.org/dictionary/english/receivable)
- [Collateral — Cambridge](https://dictionary.cambridge.org/dictionary/english/collateral)
- [Escrow — Cambridge](https://dictionary.cambridge.org/dictionary/english/escrow)
- [Consignor — Cambridge Business English](https://dictionary.cambridge.org/dictionary/english/consignor)
- [Consignee — Cambridge Business English](https://dictionary.cambridge.org/dictionary/english/consignee)
- [Stockout — Cambridge Business English](https://dictionary.cambridge.org/dictionary/english/stockout)
- [Bottleneck — Cambridge US](https://dictionary.cambridge.org/us/dictionary/english/bottleneck)
- [Throughput — Cambridge](https://dictionary.cambridge.org/dictionary/english/throughput)
- [Outlay — Cambridge US pronunciation](https://dictionary.cambridge.org/us/pronunciation/english/outlay)
- [Covenant — Cambridge Business English](https://dictionary.cambridge.org/dictionary/english/covenant)
- [Timesheet — Cambridge Business English](https://dictionary.cambridge.org/dictionary/english/timesheet)
- [Replenishment — Cambridge](https://dictionary.cambridge.org/dictionary/english/replenishment)

## 4. Manual smoke test

1. Search for all 13 new headwords in the Dictionary page.
2. Open each detail and verify spelling, POS, Vietnamese meaning, English definition, topic, example and translation.
3. Confirm `consignor` and `receivable` do not display fabricated US IPA; other displayed IPA matches the source notes.
4. Open each new word in Flashcard and Review. Confirm the record is available through canonical A–Z data without duplicate cards.
5. Check that existing 979 IDs and user-owned local profiles remain unchanged.

## 5. Non-changes

- No Listening/Reading/Grammar question content or IDs changed in this batch.
- No IndexedDB database/version/store changes; user profile import/export/reset/inspection/migration remains out of scope.
- No user-owned image assets or Part 1 JPG files are included or removed.
