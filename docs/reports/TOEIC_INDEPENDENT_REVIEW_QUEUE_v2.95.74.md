# TOEIC Independent Editorial Review Queue — v2.95.74

> Mục đích: chuyển nội dung reserve cho người rà soát độc lập. Đây là phiếu làm việc, không phải chứng nhận đã duyệt. Không đổi `editorialStatus` sang `approved-for-mock` cho đến khi reviewer ghi quyết định và ngày rà soát.

## Queue summary

| Bank | Items pending | Resources | Structured Packet Fields | Required review |
|---|---:|---:|---|---|
| Listening Parts 1–4 | 193 | 89 units | `editorialStatus`, `reviewScope`, `certaintyLevel`, `rationale`, `proposedCorrection`, AI triage cross-ref | Source/key fit, response fit, distractor uniqueness; P1 photo/action match |
| Reading Part 7 | 87 | 22 resources | `editorialStatus`, `reviewScope`, `certaintyLevel`, `rationale`, `proposedCorrection`, AI triage cross-ref | Document evidence, inference, cross-document links, one-best-answer uniqueness |
| Separate Part 5 sentence completion | 80 | 1 bank | `editorialStatus`, `reviewScope`, `certaintyLevel`, `rationale`, `proposedCorrection`, AI triage cross-ref | Grammar, naturalness, distractors, translation and one-answer uniqueness |
| **Total** | **360** | **112** | **All 360 items protected** | **Independent review required** |

## Protected inventory metrics

- Listening: **102 eligible + 193 reserve = 295 total**.
- Part 7 reserve: **87 questions**; remains separate from Listening and Part 5.
- Separate Part 5 practice-only bank: **80 questions**; 80 are review-pending.

## Reviewer record

- Reviewer name / role: ____________________________________
- Review date: _____________________________________________
- Review method / reference material: ________________________
- Decision key: `APPROVE` / `REVISE` / `REJECT` (record per item; do not approve a whole batch by default).
- For approval: confirm one defensible key, all distractors are wrong in context, source evidence supports the key, and explanation/translation are accurate.
- For revision: record the exact field and `proposedCorrection`; keep the item out of Mock until the correction is retested.

## A. Listening reserve

For Part 2, assess speech act, polarity, indirect response and naturalness. For Parts 3–4, assess transcript support and distractor plausibility. For Part 1, inspect the photo itself as well as the spoken statements.

### Part 1 · `part1-office-cleaning` · Sweeping an office hallway

- Batch: `017` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 1 photograph-audio alignment, spoken A-D mapping, and unique true description
- Transcript: A maintenance worker is sweeping the floor in a hallway. A cleaner is wiping the glass doors with a cloth. A worker is pushing a cleaning cart down the corridor. Several chairs are being arranged near the entrance.
- Spoken-statement translation / A–D mapping: A. Một nhân viên bảo trì đang quét sàn hành lang. B. Một nhân viên vệ sinh đang lau cửa kính bằng khăn. C. Một công nhân đang đẩy xe vệ sinh dọc hành lang. D. Một số chiếc ghế đang được sắp xếp gần lối vào.
- Photo: `./assets/listening/part1-office-cleaning.jpg` · Alt: A maintenance worker is sweeping the tiled floor of an office hallway with a broom. A cleaning cart stands nearby.
- Internal visual note (not independent approval): Image check: the worker is visibly using a broom to sweep the tiled hallway floor; the cleaning cart is stationary beside him. The image does not show wiping the glass doors, pushing the cart, or arranging chairs. This is an internal visual check, not independent certification.

**Q1. Listen to the four statements and select the one that best describes the photograph.**

- Choices: **A. Option A**<br>B. Option B<br>C. Option C<br>D. Option D
- Current keyed answer: **A. Option A**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 1 photograph-audio alignment, spoken A-D mapping, and unique true description
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): A maintenance worker is sweeping the floor in a hallway. — Đáp án A: Người công nhân đang dùng chổi quét sàn hành lang. Xe vệ sinh chỉ đang đặt bên cạnh, không được đẩy đi. Ảnh không cho thấy người này lau cửa kính hoặc sắp xếp ghế.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: A maintenance worker is sweeping the floor in a hallway.
- Current explanation: Đáp án A: Người công nhân đang dùng chổi quét sàn hành lang. Xe vệ sinh chỉ đang đặt bên cạnh, không được đẩy đi. Ảnh không cho thấy người này lau cửa kính hoặc sắp xếp ghế.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-monitor-delivery-arrival` · Replacement monitor delivery

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Has the replacement monitor arrived yet?
- Transcript translation: Màn hình thay thế đã được giao đến chưa? — Chưa; đơn vị chuyển phát dự kiến giao sau bữa trưa.

**Q1. Choose the most appropriate response.**

- Choices: A. The monitor has a wider screen.<br>**B. Not yet; the courier expects it after lunch.**<br>C. I ordered a desk lamp last week.
- Current keyed answer: **B. Not yet; the courier expects it after lunch.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Has the replacement monitor arrived yet? — Câu hỏi Has ... arrived yet? hỏi tình trạng hàng đã đến hay chưa. “Not yet” trả lời trực tiếp và mốc sau bữa trưa cung cấp thời gian dự kiến. Hai lựa chọn còn lại nói về đặc điểm thiết bị và một đơn hàng khác.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Has the replacement monitor arrived yet?
- Current explanation: Câu hỏi Has ... arrived yet? hỏi tình trạng hàng đã đến hay chưa. “Not yet” trả lời trực tiếp và mốc sau bữa trưa cung cấp thời gian dự kiến. Hai lựa chọn còn lại nói về đặc điểm thiết bị và một đơn hàng khác.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-revised-budget-approval` · Approval for a revised budget

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Who needs to approve the revised budget?
- Transcript translation: Ai cần phê duyệt ngân sách đã điều chỉnh? — Giám đốc khu vực.

**Q1. Choose the most appropriate response.**

- Choices: **A. The regional director.**<br>B. Before the end of the quarter.<br>C. It was reduced by five percent.
- Current keyed answer: **A. The regional director.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Who needs to approve the revised budget? — Who hỏi người cần thực hiện việc phê duyệt. “The regional director” xác định đúng người; hai phương án còn lại lần lượt là thời hạn và thông tin về mức ngân sách.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Who needs to approve the revised budget?
- Current explanation: Who hỏi người cần thực hiện việc phê duyệt. “The regional director” xác định đúng người; hai phương án còn lại lần lượt là thời hạn và thông tin về mức ngân sách.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-visitor-parking` · Parking for visitors

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Where should visitors park during the renovation?
- Transcript translation: Khách nên đỗ xe ở đâu trong thời gian sửa chữa? — Trong nhà để xe đối diện lối vào chính.

**Q1. Choose the most appropriate response.**

- Choices: A. The renovation will begin on Monday.<br>B. A visitor badge is available at reception.<br>**C. In the garage across from the main entrance.**
- Current keyed answer: **C. In the garage across from the main entrance.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Where should visitors park during the renovation? — Where hỏi địa điểm. “In the garage across from the main entrance” chỉ rõ nơi khách nên đỗ xe; các lựa chọn khác nói về ngày thi công và thẻ khách.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Where should visitors park during the renovation?
- Current explanation: Where hỏi địa điểm. “In the garage across from the main entrance” chỉ rõ nơi khách nên đỗ xe; các lựa chọn khác nói về ngày thi công và thẻ khách.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-training-session-reschedule` · Rescheduling a training session

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Would you mind moving the training session to Thursday?
- Transcript translation: Bạn có phiền chuyển buổi đào tạo sang thứ Năm không? — Được thôi; giảng viên rảnh vào ngày đó.

**Q1. Choose the most appropriate response.**

- Choices: A. The training materials are in the cabinet.<br>**B. That is fine; the instructor is available then.**<br>C. It lasted about two hours.
- Current keyed answer: **B. That is fine; the instructor is available then.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Would you mind moving the training session to Thursday? — Would you mind ...? là lời đề nghị lịch sự. “That is fine” chấp nhận đề nghị và thông tin giảng viên rảnh vào thứ Năm xác nhận việc đổi lịch khả thi. Các phương án còn lại không phản hồi yêu cầu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Would you mind moving the training session to Thursday?
- Current explanation: Would you mind ...? là lời đề nghị lịch sự. “That is fine” chấp nhận đề nghị và thông tin giảng viên rảnh vào thứ Năm xác nhận việc đổi lịch khả thi. Các phương án còn lại không phản hồi yêu cầu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-customer-survey-sent` · Customer survey distribution

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Haven't you sent the customer survey yet?
- Transcript translation: Bạn vẫn chưa gửi khảo sát khách hàng à? — Tôi gửi rồi; sáng nay tôi đã gửi email đến danh sách nhận thư.

**Q1. Choose the most appropriate response.**

- Choices: **A. I have; I emailed it to the mailing list this morning.**<br>B. The survey includes six questions.<br>C. The customer service desk is downstairs.
- Current keyed answer: **A. I have; I emailed it to the mailing list this morning.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): Haven't you sent the customer survey yet? — Câu hỏi đuôi phủ định Haven’t you ... yet? hỏi việc gửi khảo sát đã hoàn thành chưa. “I have” xác nhận đã gửi và câu sau nêu cách thức, thời điểm gửi. Hai phương án khác nói về nội dung khảo sát và địa điểm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Haven't you sent the customer survey yet?
- Current explanation: Câu hỏi đuôi phủ định Haven’t you ... yet? hỏi việc gửi khảo sát đã hoàn thành chưa. “I have” xác nhận đã gửi và câu sau nêu cách thức, thời điểm gửi. Hai phương án khác nói về nội dung khảo sát và địa điểm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-training-handouts` · Delayed workshop handouts

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The printed handouts for tomorrow’s workshop still haven’t arrived. Did the supplier give you an update? Yes. The courier collected them late, so the package will not reach our office until tomorrow afternoon. That is too late. The workshop begins at nine in the morning, and the participants need the materials when they arrive. I have the final PDF. I will upload it to the training portal this afternoon and email the participants a link.
- Transcript translation: Tài liệu in cho buổi workshop ngày mai vẫn chưa đến. Người phụ nữ hỏi thông tin từ nhà cung cấp. Người đàn ông giải thích đơn vị chuyển phát nhận hàng muộn nên gói hàng chỉ đến vào chiều hôm sau. Vì buổi workshop bắt đầu lúc 9 giờ sáng, người đàn ông sẽ tải bản PDF cuối cùng lên cổng đào tạo và gửi đường dẫn cho người tham dự trong chiều nay.

**Q1. What problem are the speakers discussing?**

- Choices: **A. The printed handouts are delayed.**<br>B. The workshop has been canceled.<br>C. The supplier sent the wrong invoice.<br>D. The training room is unavailable.
- Current keyed answer: **A. The printed handouts are delayed.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): The printed handouts for tomorrow’s workshop still haven’t arrived. — Người phụ nữ nói tài liệu in vẫn chưa đến; người đàn ông xác nhận chuyển phát muộn nên gói hàng sẽ đến sau thời điểm cần dùng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The printed handouts for tomorrow’s workshop still haven’t arrived.
- Current explanation: Người phụ nữ nói tài liệu in vẫn chưa đến; người đàn ông xác nhận chuyển phát muộn nên gói hàng sẽ đến sau thời điểm cần dùng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why are the printed handouts needed earlier?**

- Choices: A. The supplier has closed its office.<br>**B. The workshop begins before the materials will arrive.**<br>C. The participants requested a different venue.<br>D. The final PDF has not been approved.
- Current keyed answer: **B. The workshop begins before the materials will arrive.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The workshop begins at nine in the morning, and the participants need the materials when they arrive. — Buổi workshop bắt đầu lúc 9 giờ sáng, trong khi tài liệu in chỉ đến vào chiều hôm sau; vì vậy tài liệu sẽ đến quá muộn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The workshop begins at nine in the morning, and the participants need the materials when they arrive.
- Current explanation: Buổi workshop bắt đầu lúc 9 giờ sáng, trong khi tài liệu in chỉ đến vào chiều hôm sau; vì vậy tài liệu sẽ đến quá muộn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will the man do this afternoon?**

- Choices: A. Ask the courier to return the package.<br>B. Print a new set at the reception desk.<br>**C. Upload the PDF and email a link.**<br>D. Postpone the workshop until Friday.
- Current keyed answer: **C. Upload the PDF and email a link.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I will upload it to the training portal this afternoon and email the participants a link. — Người đàn ông nói sẽ tải tệp PDF lên cổng đào tạo và gửi đường dẫn cho người tham dự qua email.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I will upload it to the training portal this afternoon and email the participants a link.
- Current explanation: Người đàn ông nói sẽ tải tệp PDF lên cổng đào tạo và gửi đường dẫn cho người tham dự qua email.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-east-elevator-maintenance` · Maintenance in the east elevator bank

- Batch: `legacy` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Attention, employees. The elevators in the east wing will be out of service this Friday from one until four in the afternoon while technicians replace a control panel. During that time, please use the west elevator bank near the main lobby. Employees expecting large deliveries should arrange them before noon, when the service entrance will be staffed. We apologize for the inconvenience and appreciate your cooperation.
- Transcript translation: Thông báo cho nhân viên biết các thang máy ở cánh phía đông sẽ ngừng hoạt động vào thứ Sáu, từ 1 đến 4 giờ chiều, để kỹ thuật viên thay bảng điều khiển. Trong thời gian đó, nhân viên cần sử dụng cụm thang máy phía tây gần sảnh chính. Những người có đơn giao hàng lớn nên sắp xếp trước buổi trưa. Ban quản lý xin lỗi vì sự bất tiện và cảm ơn mọi người đã hợp tác.

**Q1. Which facility will be unavailable?**

- Choices: **A. The east wing elevators.**<br>B. The main lobby doors.<br>C. The west stairwell.<br>D. The service entrance.
- Current keyed answer: **A. The east wing elevators.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The elevators in the east wing will be out of service this Friday from one until four in the afternoon — Thông báo nói các thang máy ở cánh phía đông sẽ ngừng hoạt động để kỹ thuật viên thay bảng điều khiển.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The elevators in the east wing will be out of service this Friday from one until four in the afternoon
- Current explanation: Thông báo nói các thang máy ở cánh phía đông sẽ ngừng hoạt động để kỹ thuật viên thay bảng điều khiển.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When will the maintenance take place?**

- Choices: A. On Thursday morning.<br>B. From noon until one.<br>**C. From one until four on Friday.**<br>D. Throughout the weekend.
- Current keyed answer: **C. From one until four on Friday.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): this Friday from one until four in the afternoon — Thời gian được nêu rõ là thứ Sáu, từ 1 giờ đến 4 giờ chiều.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: this Friday from one until four in the afternoon
- Current explanation: Thời gian được nêu rõ là thứ Sáu, từ 1 giờ đến 4 giờ chiều.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What are employees asked to do during the maintenance?**

- Choices: A. Use the east stairwell.<br>**B. Use the west elevator bank.**<br>C. Delay all office deliveries.<br>D. Contact the building manager.
- Current keyed answer: **B. Use the west elevator bank.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): During that time, please use the west elevator bank near the main lobby — Người thông báo hướng dẫn nhân viên sử dụng cụm thang máy phía tây gần sảnh chính.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: During that time, please use the west elevator bank near the main lobby
- Current explanation: Người thông báo hướng dẫn nhân viên sử dụng cụm thang máy phía tây gần sảnh chính.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-vendor-credit-note` · Following up on a credit note

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Has the supplier issued the credit note yet?
- Transcript translation: Nhà cung cấp đã phát hành phiếu ghi có chưa? — Chưa; bộ phận kế toán dự kiến sẽ nhận được vào ngày mai.

**Q1. Choose the most appropriate response.**

- Choices: **A. Not yet; the accounting team expects it tomorrow.**<br>B. The supplier offers a thirty-day payment term.<br>C. I attached the delivery labels to the cartons.
- Current keyed answer: **A. Not yet; the accounting team expects it tomorrow.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Has the supplier issued the credit note yet? — Câu hỏi Has ... yet? hỏi một việc đã hoàn tất hay chưa. “Not yet” trả lời trực tiếp và mệnh đề sau nêu thời điểm dự kiến. Hai lựa chọn còn lại nói về điều khoản thanh toán và thao tác với nhãn giao hàng, không trả lời tình trạng phát hành.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Has the supplier issued the credit note yet?
- Current explanation: Câu hỏi Has ... yet? hỏi một việc đã hoàn tất hay chưa. “Not yet” trả lời trực tiếp và mệnh đề sau nêu thời điểm dự kiến. Hai lựa chọn còn lại nói về điều khoản thanh toán và thao tác với nhãn giao hàng, không trả lời tình trạng phát hành.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-warehouse-shipment-hold` · Holding a shipment

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Could you ask the warehouse to hold the shipment until Monday?
- Transcript translation: Bạn có thể nhờ kho giữ lô hàng đến thứ Hai không? — Được, tôi sẽ thông báo cho bộ phận điều phối xuất hàng.

**Q1. Choose the most appropriate response.**

- Choices: **A. Certainly. I'll notify the dispatch team.**<br>B. The shipment weighs eighteen kilograms.<br>C. The warehouse closes at six on weekdays.
- Current keyed answer: **A. Certainly. I'll notify the dispatch team.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Could you ask the warehouse to hold the shipment until Monday? — Could you ...? là lời yêu cầu lịch sự. “Certainly” chấp nhận yêu cầu và việc thông báo cho bộ phận xuất hàng là hành động phù hợp để giữ lô hàng. Hai lựa chọn còn lại chỉ cung cấp thông tin về trọng lượng và giờ đóng cửa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Could you ask the warehouse to hold the shipment until Monday?
- Current explanation: Could you ...? là lời yêu cầu lịch sự. “Certainly” chấp nhận yêu cầu và việc thông báo cho bộ phận xuất hàng là hành động phù hợp để giữ lô hàng. Hai lựa chọn còn lại chỉ cung cấp thông tin về trọng lượng và giờ đóng cửa.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-purchase-order-return` · A returned purchase order

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Why was the purchase order returned?
- Transcript translation: Tại sao đơn đặt hàng mua bị trả lại? — Vì thiếu mã trung tâm chi phí.

**Q1. Choose the most appropriate response.**

- Choices: A. It will be delivered by noon.<br>**B. The cost center code was missing.**<br>C. The order was placed last Thursday.
- Current keyed answer: **B. The cost center code was missing.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Why was the purchase order returned? — Why hỏi nguyên nhân. “The cost center code was missing” nêu trực tiếp lý do đơn đặt hàng bị trả lại; hai phương án còn lại lần lượt nói về thời điểm giao hàng và thời điểm đặt hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Why was the purchase order returned?
- Current explanation: Why hỏi nguyên nhân. “The cost center code was missing” nêu trực tiếp lý do đơn đặt hàng bị trả lại; hai phương án còn lại lần lượt nói về thời điểm giao hàng và thời điểm đặt hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-orientation-leader` · New employee orientation

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Who will lead the new employee orientation?
- Transcript translation: Ai sẽ phụ trách buổi định hướng nhân viên mới? — Cô Alvarez thuộc bộ phận Nhân sự.

**Q1. Choose the most appropriate response.**

- Choices: A. In the training room on the fourth floor.<br>B. It begins at 8:30.<br>**C. Ms. Alvarez from Human Resources.**
- Current keyed answer: **C. Ms. Alvarez from Human Resources.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Who will lead the new employee orientation? — Who hỏi người phụ trách. “Ms. Alvarez from Human Resources” xác định đúng người; các lựa chọn còn lại lần lượt trả lời về địa điểm và thời gian.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Who will lead the new employee orientation?
- Current explanation: Who hỏi người phụ trách. “Ms. Alvarez from Human Resources” xác định đúng người; các lựa chọn còn lại lần lượt trả lời về địa điểm và thời gian.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-inventory-report-frequency` · Inventory report schedule

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: How often is the inventory report updated?
- Transcript translation: Báo cáo tồn kho được cập nhật bao lâu một lần? — Vào mỗi chiều thứ Sáu.

**Q1. Choose the most appropriate response.**

- Choices: A. The inventory clerk is on leave.<br>**B. Every Friday afternoon.**<br>C. It was sent to the regional office.
- Current keyed answer: **B. Every Friday afternoon.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): How often is the inventory report updated? — How often hỏi tần suất. “Every Friday afternoon” nêu chu kỳ cập nhật; hai lựa chọn còn lại là tình trạng nhân sự và nơi nhận báo cáo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: How often is the inventory report updated?
- Current explanation: How often hỏi tần suất. “Every Friday afternoon” nêu chu kỳ cập nhật; hai lựa chọn còn lại là tình trạng nhân sự và nơi nhận báo cáo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-printer-maintenance-contract` · Revising a printer maintenance contract

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: I reviewed the draft maintenance agreement from Apex Office Systems. The annual fee is unchanged, but urgent repairs are still listed with a two-business-day response time. The operations team requested next-business-day service because the new printers are used for customer orders. Did the supplier agree? They can provide next-day service, but only if we extend the agreement for another year. That seems reasonable. Please send the revised clause to Legal before we sign anything.
- Transcript translation: Người phụ nữ đã xem dự thảo hợp đồng bảo trì của Apex Office Systems. Mức phí năm không đổi nhưng thời gian phản hồi sửa chữa khẩn cấp vẫn là hai ngày làm việc. Nhóm vận hành muốn được hỗ trợ vào ngày làm việc kế tiếp vì máy in phục vụ đơn hàng khách hàng. Nhà cung cấp đồng ý nếu hợp đồng được gia hạn thêm một năm. Người đàn ông đề nghị gửi điều khoản sửa đổi cho bộ phận Pháp chế trước khi ký.

**Q1. What are the speakers discussing?**

- Choices: **A. A revised maintenance agreement for office printers**<br>B. A proposal to replace the office network<br>C. A schedule for employee training<br>D. A complaint about a delayed customer order
- Current keyed answer: **A. A revised maintenance agreement for office printers**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I reviewed the draft maintenance agreement from Apex Office Systems. — Hai người đang xem bản dự thảo thỏa thuận bảo trì máy in và trao đổi về thời gian phản hồi khi sửa chữa khẩn cấp. Vì vậy, đáp án là thỏa thuận bảo trì máy in được sửa đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I reviewed the draft maintenance agreement from Apex Office Systems.
- Current explanation: Hai người đang xem bản dự thảo thỏa thuận bảo trì máy in và trao đổi về thời gian phản hồi khi sửa chữa khẩn cấp. Vì vậy, đáp án là thỏa thuận bảo trì máy in được sửa đổi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why did the operations team request next-business-day service?**

- Choices: A. The current printers are being relocated.<br>**B. The printers are used for customer orders.**<br>C. The supplier has reduced its annual fee.<br>D. The office will be closed for two days.
- Current keyed answer: **B. The printers are used for customer orders.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): because the new printers are used for customer orders. — Người đàn ông nói rõ máy in mới được dùng để xử lý đơn hàng khách hàng, nên nhóm vận hành cần dịch vụ sửa chữa nhanh hơn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: because the new printers are used for customer orders.
- Current explanation: Người đàn ông nói rõ máy in mới được dùng để xử lý đơn hàng khách hàng, nên nhóm vận hành cần dịch vụ sửa chữa nhanh hơn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What does the man ask the woman to do next?**

- Choices: A. Schedule a printer installation.<br>B. Extend the agreement immediately.<br>**C. Send the revised clause to the Legal department.**<br>D. Prepare a new annual budget.
- Current keyed answer: **C. Send the revised clause to the Legal department.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): Please send the revised clause to Legal before we sign anything. — Ở lượt cuối, người đàn ông yêu cầu gửi điều khoản đã chỉnh sửa cho bộ phận Pháp chế trước khi ký. Anh ấy chưa yêu cầu ký hay gia hạn ngay.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Please send the revised clause to Legal before we sign anything.
- Current explanation: Ở lượt cuối, người đàn ông yêu cầu gửi điều khoản đã chỉnh sửa cho bộ phận Pháp chế trước khi ký. Anh ấy chưa yêu cầu ký hay gia hạn ngay.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-branch-inventory-transfer` · Checking a branch inventory transfer

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The inventory report lists eighteen wireless keyboards as available, but the cycle count in aisle B12 shows none. I found the cartons in the transfer area. They are marked for the Riverside branch, not this warehouse. Then they should not be included in our available stock. Has the driver signed the transfer form? Not yet. I will move the cartons to the branch-transfer section and update the count after the driver signs.
- Transcript translation: Báo cáo tồn kho ghi nhận có 18 bàn phím không dây sẵn có nhưng kiểm kê tại dãy B12 không thấy sản phẩm nào. Người phụ nữ tìm thấy các thùng hàng ở khu vực chuyển kho và xác nhận chúng được ghi nhãn dành cho chi nhánh Riverside. Người đàn ông nói chúng không được tính vào lượng hàng sẵn có của kho hiện tại. Cô ấy sẽ chuyển thùng hàng sang khu vực điều chuyển chi nhánh và cập nhật số liệu sau khi tài xế ký biểu mẫu.

**Q1. Which product is involved in the discrepancy?**

- Choices: **A. Wireless keyboards**<br>B. Desktop monitors<br>C. Printer cartridges<br>D. Office chairs
- Current keyed answer: **A. Wireless keyboards**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The inventory report lists eighteen wireless keyboards as available, but the cycle count in aisle B12 shows none. — Người đàn ông gọi tên rõ “eighteen wireless keyboards” khi mô tả chênh lệch kiểm kê. Các sản phẩm còn lại không được nhắc đến.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The inventory report lists eighteen wireless keyboards as available, but the cycle count in aisle B12 shows none.
- Current explanation: Người đàn ông gọi tên rõ “eighteen wireless keyboards” khi mô tả chênh lệch kiểm kê. Các sản phẩm còn lại không được nhắc đến.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why should the cartons be excluded from this warehouse’s available stock?**

- Choices: A. They are damaged and must be returned.<br>B. They are reserved for a customer demonstration.<br>**C. They are assigned to the Riverside branch.**<br>D. They have not yet been entered in the supplier invoice.
- Current keyed answer: **C. They are assigned to the Riverside branch.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): They are marked for the Riverside branch, not this warehouse. — Người phụ nữ đọc nhãn trên các thùng hàng và cho biết chúng được phân bổ cho chi nhánh Riverside, không thuộc kho hiện tại.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: They are marked for the Riverside branch, not this warehouse.
- Current explanation: Người phụ nữ đọc nhãn trên các thùng hàng và cho biết chúng được phân bổ cho chi nhánh Riverside, không thuộc kho hiện tại.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When will the woman update the inventory count?**

- Choices: A. As soon as the cartons arrive.<br>**B. After the driver signs the transfer form.**<br>C. At the end of the next quarter.<br>D. Before the supplier issues an invoice.
- Current keyed answer: **B. After the driver signs the transfer form.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I will move the cartons to the branch-transfer section and update the count after the driver signs. — Cô ấy nói sẽ cập nhật số lượng sau khi tài xế ký biểu mẫu chuyển hàng. Đây là điều kiện thời điểm được nêu trực tiếp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I will move the cartons to the branch-transfer section and update the count after the driver signs.
- Current explanation: Cô ấy nói sẽ cập nhật số lượng sau khi tài xế ký biểu mẫu chuyển hàng. Đây là điều kiện thời điểm được nêu trực tiếp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-expense-reimbursement-procedure` · A change to expense reimbursement procedures

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Starting December first, employees must submit travel and meal expense claims through the finance portal. Each claim must include an itemized receipt for expenses over twenty dollars. Claims for the previous month are due by the fifth business day of the following month. Paper forms will no longer be accepted, although managers will continue to approve claims online. For help, contact the accounts-payable team.
- Transcript translation: Kể từ ngày 1 tháng 12, nhân viên phải gửi yêu cầu thanh toán chi phí đi lại và ăn uống qua cổng tài chính. Mỗi yêu cầu phải có hóa đơn chi tiết đối với khoản chi trên 20 đô la. Các khoản của tháng trước phải được gửi trước ngày làm việc thứ năm của tháng kế tiếp. Biểu mẫu giấy sẽ không còn được chấp nhận; quản lý tiếp tục phê duyệt trực tuyến. Nhân viên cần trợ giúp có thể liên hệ bộ phận công nợ phải trả.

**Q1. What change is being introduced?**

- Choices: **A. Employees must submit expense claims through the finance portal.**<br>B. Managers must approve claims in person.<br>C. Travel claims will be processed every Friday.<br>D. Employees must use a new company credit card.
- Current keyed answer: **A. Employees must submit expense claims through the finance portal.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): employees must submit travel and meal expense claims through the finance portal — Thông báo nêu rõ kể từ ngày 1 tháng 12, nhân viên phải gửi yêu cầu thanh toán chi phí qua cổng tài chính; biểu mẫu giấy sẽ không còn được chấp nhận.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: employees must submit travel and meal expense claims through the finance portal
- Current explanation: Thông báo nêu rõ kể từ ngày 1 tháng 12, nhân viên phải gửi yêu cầu thanh toán chi phí qua cổng tài chính; biểu mẫu giấy sẽ không còn được chấp nhận.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When is an itemized receipt required?**

- Choices: A. For every expense, regardless of amount.<br>**B. For expenses over twenty dollars.**<br>C. Only for hotel reservations.<br>D. When a manager requests a paper copy.
- Current keyed answer: **B. For expenses over twenty dollars.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Each claim must include an itemized receipt for expenses over twenty dollars — Người thông báo quy định chứng từ chi tiết phải được đính kèm đối với khoản chi trên 20 đô la.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Each claim must include an itemized receipt for expenses over twenty dollars
- Current explanation: Người thông báo quy định chứng từ chi tiết phải được đính kèm đối với khoản chi trên 20 đô la.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. By when must claims for the previous month be submitted?**

- Choices: A. By the last calendar day of that month.<br>B. By the first Monday of the next month.<br>**C. By the fifth business day of the following month.**<br>D. Within two weeks after a manager approves them.
- Current keyed answer: **C. By the fifth business day of the following month.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Claims for the previous month are due by the fifth business day of the following month — Thời hạn được nêu là ngày làm việc thứ năm của tháng tiếp theo. Không phải ngày lịch thứ năm hay hai tuần sau khi phê duyệt.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Claims for the previous month are due by the fifth business day of the following month
- Current explanation: Thời hạn được nêu là ngày làm việc thứ năm của tháng tiếp theo. Không phải ngày lịch thứ năm hay hai tuần sau khi phê duyệt.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-new-employee-orientation-room-change` · A room change for new employee orientation

- Batch: `014` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Please note a room change for Wednesday’s new-employee orientation. Because the projector in Training Room Two is being repaired, the session will now take place in Conference Room C. The start time remains nine thirty in the morning. Participants should bring their laptops; printed copies of the employee handbook will be available at the door. Anyone who cannot attend should notify Human Resources by Tuesday afternoon.
- Transcript translation: Thông báo về việc đổi phòng cho buổi định hướng nhân viên mới vào thứ Tư. Do máy chiếu tại Training Room Two đang được sửa chữa, buổi học sẽ chuyển sang Conference Room C. Giờ bắt đầu vẫn là 9 giờ 30 sáng. Người tham gia cần mang laptop; bản in sổ tay nhân viên sẽ được phát ở cửa. Ai không thể tham dự cần báo cho bộ phận Nhân sự trước chiều thứ Ba.

**Q1. Where will the orientation session take place?**

- Choices: A. In Training Room Two<br>**B. In Conference Room C**<br>C. In the main reception area<br>D. In the employee cafeteria
- Current keyed answer: **B. In Conference Room C**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): the session will now take place in Conference Room C — Người thông báo nói buổi định hướng được chuyển sang Conference Room C. Training Room Two đang được sửa máy chiếu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: the session will now take place in Conference Room C
- Current explanation: Người thông báo nói buổi định hướng được chuyển sang Conference Room C. Training Room Two đang được sửa máy chiếu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why has the room been changed?**

- Choices: A. The original room is being repainted.<br>B. The session has attracted more participants.<br>**C. The projector in the original room is being repaired.**<br>D. The Human Resources office is closed.
- Current keyed answer: **C. The projector in the original room is being repaired.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Because the projector in Training Room Two is being repaired — Lý do được nêu trực tiếp là máy chiếu tại Training Room Two đang được sửa chữa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Because the projector in Training Room Two is being repaired
- Current explanation: Lý do được nêu trực tiếp là máy chiếu tại Training Room Two đang được sửa chữa.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should participants bring?**

- Choices: **A. Their laptops**<br>B. A printed employee handbook<br>C. A signed expense form<br>D. A visitor parking pass
- Current keyed answer: **A. Their laptops**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Participants should bring their laptops — Người tham gia được yêu cầu mang laptop. Bản in sổ tay nhân viên sẽ được chuẩn bị sẵn ở cửa nên không cần tự mang.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Participants should bring their laptops
- Current explanation: Người tham gia được yêu cầu mang laptop. Bản in sổ tay nhân viên sẽ được chuẩn bị sẵn ở cửa nên không cần tự mang.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-freight-invoice-surcharge` · Checking a freight invoice

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Could you confirm whether the revised freight invoice includes the weekend surcharge?
- Transcript translation: Could you confirm whether the revised freight invoice includes the weekend surcharge?

**Q1. Choose the most appropriate response.**

- Choices: **A. Yes, it is listed on the second page.**<br>B. The warehouse closes at six.<br>C. We ordered the smaller cartons.
- Current keyed answer: **A. Yes, it is listed on the second page.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Could you confirm whether the revised freight invoice includes the weekend surcharge? — Người nói hỏi liệu phụ phí cuối tuần đã được tính trong hóa đơn sửa đổi chưa. “Yes” xác nhận và vị trí ở trang hai cung cấp chi tiết phù hợp; hai phương án còn lại không liên quan đến nội dung hóa đơn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Could you confirm whether the revised freight invoice includes the weekend surcharge?
- Current explanation: Người nói hỏi liệu phụ phí cuối tuần đã được tính trong hóa đơn sửa đổi chưa. “Yes” xác nhận và vị trí ở trang hai cung cấp chi tiết phù hợp; hai phương án còn lại không liên quan đến nội dung hóa đơn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-safety-certificate-owner` · Obtaining a safety certificate

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Who is responsible for obtaining the updated safety certificate?
- Transcript translation: Who is responsible for obtaining the updated safety certificate?

**Q1. Choose the most appropriate response.**

- Choices: A. It expires at the end of June.<br>**B. The facilities coordinator is handling it.**<br>C. We need two additional copies.
- Current keyed answer: **B. The facilities coordinator is handling it.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Who is responsible for obtaining the updated safety certificate? — Câu hỏi Who hỏi người chịu trách nhiệm. “The facilities coordinator” nêu đúng người phụ trách; phương án về ngày hết hạn và số bản sao không trả lời câu hỏi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Who is responsible for obtaining the updated safety certificate?
- Current explanation: Câu hỏi Who hỏi người chịu trách nhiệm. “The facilities coordinator” nêu đúng người phụ trách; phương án về ngày hết hạn và số bản sao không trả lời câu hỏi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-purchase-order-release` · Releasing a purchase order

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: When will the purchasing team release the order?
- Transcript translation: When will the purchasing team release the order?

**Q1. Choose the most appropriate response.**

- Choices: **A. After the revised quote is approved.**<br>B. The order includes replacement cables.<br>C. Please put it near the entrance.
- Current keyed answer: **A. After the revised quote is approved.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): When will the purchasing team release the order? — When hỏi thời điểm. Cụm “After the revised quote is approved” chỉ rõ điều kiện và thời điểm dự kiến; hai lựa chọn khác mô tả nội dung hoặc vị trí.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: When will the purchasing team release the order?
- Current explanation: When hỏi thời điểm. Cụm “After the revised quote is approved” chỉ rõ điều kiện và thời điểm dự kiến; hai lựa chọn khác mô tả nội dung hoặc vị trí.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-returned-serial-number` · Returning a replacement unit

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Why was the replacement unit sent back?
- Transcript translation: Why was the replacement unit sent back?

**Q1. Choose the most appropriate response.**

- Choices: A. The service desk opens at eight.<br>B. It was covered by the annual plan.<br>**C. Its serial number did not match the request.**
- Current keyed answer: **C. Its serial number did not match the request.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Why was the replacement unit sent back? — Why hỏi nguyên nhân. Số sê-ri không khớp yêu cầu giải thích trực tiếp việc gửi trả; hai phương án kia nói về giờ mở cửa và phạm vi gói dịch vụ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Why was the replacement unit sent back?
- Current explanation: Why hỏi nguyên nhân. Số sê-ri không khớp yêu cầu giải thích trực tiếp việc gửi trả; hai phương án kia nói về giờ mở cửa và phạm vi gói dịch vụ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-itemized-receipt-forward` · Forwarding an itemized receipt

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Would you mind forwarding the itemized receipt?
- Transcript translation: Would you mind forwarding the itemized receipt?

**Q1. Choose the most appropriate response.**

- Choices: **A. Certainly, I will send it with my report.**<br>B. The meeting was moved to Thursday.<br>C. There are six chairs in the room.
- Current keyed answer: **A. Certainly, I will send it with my report.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Would you mind forwarding the itemized receipt? — Đây là lời đề nghị lịch sự. “Certainly” chấp nhận lời đề nghị và nói rõ sẽ gửi kèm báo cáo; các đáp án khác không liên quan.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Would you mind forwarding the itemized receipt?
- Current explanation: Đây là lời đề nghị lịch sự. “Certainly” chấp nhận lời đề nghị và nói rõ sẽ gửi kèm báo cáo; các đáp án khác không liên quan.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-warehouse-label-printing` · Printing warehouse labels

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Have the warehouse labels been printed?
- Transcript translation: Have the warehouse labels been printed?

**Q1. Choose the most appropriate response.**

- Choices: A. The printer is beside the loading door.<br>**B. Only the labels for the first shipment have been printed.**<br>C. We usually count stock on Fridays.
- Current keyed answer: **B. Only the labels for the first shipment have been printed.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Have the warehouse labels been printed? — Câu hỏi Have ... been printed? hỏi tình trạng hoàn tất. “Only the labels for the first shipment have been printed” cho biết mới hoàn tất một phần; các lựa chọn còn lại không cho biết tiến độ in.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Have the warehouse labels been printed?
- Current explanation: Câu hỏi Have ... been printed? hỏi tình trạng hoàn tất. “Only the labels for the first shipment have been printed” cho biết mới hoàn tất một phần; các lựa chọn còn lại không cho biết tiến độ in.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-revised-budget-director` · Finalizing a revised budget

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Is the revised budget ready for the director?
- Transcript translation: Is the revised budget ready for the director?

**Q1. Choose the most appropriate response.**

- Choices: **A. Not until Finance checks the figures.**<br>B. The director is traveling by train.<br>C. It was printed in color.
- Current keyed answer: **A. Not until Finance checks the figures.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Is the revised budget ready for the director? — Câu hỏi Yes/No được trả lời gián tiếp bằng “Not until...”, cho biết ngân sách chưa sẵn sàng trước khi bộ phận Tài chính kiểm tra số liệu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Is the revised budget ready for the director?
- Current explanation: Câu hỏi Yes/No được trả lời gián tiếp bằng “Not until...”, cho biết ngân sách chưa sẵn sàng trước khi bộ phận Tài chính kiểm tra số liệu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-supplier-meeting-time` · Scheduling a supplier call

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: The supplier can only meet before noon, can’t they?
- Transcript translation: The supplier can only meet before noon, can’t they?

**Q1. Choose the most appropriate response.**

- Choices: **A. I will move our call to eleven.**<br>B. The supplier sent three invoices.<br>C. No, the office has a new address.
- Current keyed answer: **A. I will move our call to eleven.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The supplier can only meet before noon, can’t they? — Câu hỏi đuôi xác nhận giới hạn thời gian. Việc dời cuộc gọi sang 11 giờ đáp ứng yêu cầu gặp trước buổi trưa; hai phương án còn lại không phù hợp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The supplier can only meet before noon, can’t they?
- Current explanation: Câu hỏi đuôi xác nhận giới hạn thời gian. Việc dời cuộc gọi sang 11 giờ đáp ứng yêu cầu gặp trước buổi trưa; hai phương án còn lại không phù hợp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-safety-workshop-room` · Finding a workshop room

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Which room is reserved for the safety workshop?
- Transcript translation: Which room is reserved for the safety workshop?

**Q1. Choose the most appropriate response.**

- Choices: A. It begins at half past two.<br>**B. The one next to the loading area.**<br>C. The instructor has arrived.
- Current keyed answer: **B. The one next to the loading area.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Which room is reserved for the safety workshop? — Which hỏi địa điểm. “The one next to the loading area” xác định phòng; các lựa chọn khác chỉ thời gian và người tham gia.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Which room is reserved for the safety workshop?
- Current explanation: Which hỏi địa điểm. “The one next to the loading area” xác định phòng; các lựa chọn khác chỉ thời gian và người tham gia.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-bulk-order-discount` · Confirming a volume discount

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Didn’t the vendor offer a discount for bulk orders?
- Transcript translation: Didn’t the vendor offer a discount for bulk orders?

**Q1. Choose the most appropriate response.**

- Choices: **A. Yes, for quantities above five hundred.**<br>B. The order was delivered yesterday.<br>C. Please use the side entrance.
- Current keyed answer: **A. Yes, for quantities above five hundred.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Didn’t the vendor offer a discount for bulk orders? — Câu hỏi phủ định xác nhận liệu nhà cung cấp có ưu đãi hay không. “Yes” xác nhận, kèm điều kiện số lượng trên 500; hai đáp án khác không liên quan.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Didn’t the vendor offer a discount for bulk orders?
- Current explanation: Câu hỏi phủ định xác nhận liệu nhà cung cấp có ưu đãi hay không. “Yes” xác nhận, kèm điều kiện số lượng trên 500; hai đáp án khác không liên quan.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-pallet-arrival-count` · Checking pallet arrival

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Do you know whether the pallets arrived?
- Transcript translation: Do you know whether the pallets arrived?

**Q1. Choose the most appropriate response.**

- Choices: **A. The receiving team is counting them now.**<br>B. They were made from recycled paper.<br>C. The driver needs a new badge.
- Current keyed answer: **A. The receiving team is counting them now.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Do you know whether the pallets arrived? — Câu hỏi Do you know whether... hỏi tình trạng đến nơi. Đội nhận hàng đang đếm pallet cho biết hàng đã tới và đang được kiểm tra.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Do you know whether the pallets arrived?
- Current explanation: Câu hỏi Do you know whether... hỏi tình trạng đến nơi. Đội nhận hàng đang đếm pallet cho biết hàng đã tới và đang được kiểm tra.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-reference-check-owner` · Assigning reference checks

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Who should review the applicants’ references?
- Transcript translation: Who should review the applicants’ references?

**Q1. Choose the most appropriate response.**

- Choices: **A. The HR manager will take care of that.**<br>B. The references are printed in blue.<br>C. We received the applications on Monday.
- Current keyed answer: **A. The HR manager will take care of that.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Who should review the applicants’ references? — Who yêu cầu người phụ trách. Quản lý Nhân sự sẽ xử lý việc kiểm tra tham chiếu; các đáp án khác không xác định người thực hiện.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Who should review the applicants’ references?
- Current explanation: Who yêu cầu người phụ trách. Quản lý Nhân sự sẽ xử lý việc kiểm tra tham chiếu; các đáp án khác không xác định người thực hiện.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-server-room-inspection` · Scheduling server-room access

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: How long will the server room be unavailable?
- Transcript translation: How long will the server room be unavailable?

**Q1. Choose the most appropriate response.**

- Choices: **A. Until the inspection is finished tomorrow.**<br>B. The replacement server arrived early.<br>C. It is located on the third floor.
- Current keyed answer: **A. Until the inspection is finished tomorrow.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): How long will the server room be unavailable? — How long hỏi khoảng thời gian. Câu trả lời nêu mốc kết thúc là khi kiểm tra hoàn tất vào ngày mai; các lựa chọn khác nói về việc giao hàng và địa điểm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: How long will the server room be unavailable?
- Current explanation: How long hỏi khoảng thời gian. Câu trả lời nêu mốc kết thúc là khi kiểm tra hoàn tất vào ngày mai; các lựa chọn khác nói về việc giao hàng và địa điểm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-sample-color-comparison` · Comparing product samples

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Would you prefer the blue samples or the gray ones?
- Transcript translation: Would you prefer the blue samples or the gray ones?

**Q1. Choose the most appropriate response.**

- Choices: **A. Let’s compare both before deciding.**<br>B. The sample room is being cleaned.<br>C. They were shipped by air.
- Current keyed answer: **A. Let’s compare both before deciding.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Would you prefer the blue samples or the gray ones? — Câu hỏi đưa ra hai lựa chọn. “Compare both” phản hồi trực tiếp rằng người nói muốn xem cả hai trước khi quyết định.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Would you prefer the blue samples or the gray ones?
- Current explanation: Câu hỏi đưa ra hai lựa chọn. “Compare both” phản hồi trực tiếp rằng người nói muốn xem cả hai trước khi quyết định.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-hotel-confirmation-delay` · Confirming hotel reservations

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Why haven’t the hotel rooms been confirmed?
- Transcript translation: Why haven’t the hotel rooms been confirmed?

**Q1. Choose the most appropriate response.**

- Choices: **A. The conference dates changed.**<br>B. The hotel has a rooftop restaurant.<br>C. Three employees submitted receipts.
- Current keyed answer: **A. The conference dates changed.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Why haven’t the hotel rooms been confirmed? — Why hỏi lý do chưa xác nhận. Ngày hội nghị thay đổi là nguyên nhân trực tiếp; các lựa chọn khác không giải thích việc xác nhận phòng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Why haven’t the hotel rooms been confirmed?
- Current explanation: Why hỏi lý do chưa xác nhận. Ngày hội nghị thay đổi là nguyên nhân trực tiếp; các lựa chọn khác không giải thích việc xác nhận phòng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `part2-survey-results-folder` · Locating survey results

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Where can I find the latest survey results?
- Transcript translation: Where can I find the latest survey results?

**Q1. Choose the most appropriate response.**

- Choices: **A. They are in the shared project folder.**<br>B. The survey was conducted last month.<br>C. Please ask the customers to wait.
- Current keyed answer: **A. They are in the shared project folder.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Where can I find the latest survey results? — Where hỏi vị trí lưu trữ. Thư mục dự án dùng chung cung cấp địa điểm cụ thể; các lựa chọn khác nói thời gian và hành động không đúng trọng tâm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Where can I find the latest survey results?
- Current explanation: Where hỏi vị trí lưu trữ. Thư mục dự án dùng chung cung cấp địa điểm cụ thể; các lựa chọn khác nói thời gian và hành động không đúng trọng tâm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-cold-storage-capacity` · Planning cold-storage capacity

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The northern warehouse is nearly at its refrigerated capacity. We received two additional food orders this morning, and both require temperature-controlled storage. Could we move the beverage shipment to the West Depot? It has unused cold space this week. Possibly, but the West Depot needs the updated temperature log before it accepts another shipment. I will ask Quality Assurance to send the log today. Then we can reserve the space for Friday.
- Transcript translation: Kho phía Bắc gần hết sức chứa lạnh. Người đàn ông đề xuất chuyển lô đồ uống sang West Depot, nhưng kho này cần nhật ký nhiệt độ cập nhật. Anh ấy sẽ nhờ bộ phận Đảm bảo chất lượng gửi nhật ký trong ngày để đặt chỗ vào thứ Sáu.

**Q1. What problem are the speakers discussing?**

- Choices: **A. A shortage of refrigerated storage space**<br>B. A delay in hiring warehouse staff<br>C. A damaged delivery vehicle<br>D. An increase in electricity rates
- Current keyed answer: **A. A shortage of refrigerated storage space**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): nearly at its refrigerated capacity — Người phụ nữ nói kho phía Bắc gần đạt giới hạn sức chứa lạnh trong khi có thêm hai đơn hàng cần bảo quản nhiệt độ kiểm soát.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: nearly at its refrigerated capacity
- Current explanation: Người phụ nữ nói kho phía Bắc gần đạt giới hạn sức chứa lạnh trong khi có thêm hai đơn hàng cần bảo quản nhiệt độ kiểm soát.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What does the man suggest doing?**

- Choices: A. Canceling one of the food orders<br>**B. Moving a beverage shipment to another depot**<br>C. Renting additional office space<br>D. Changing the delivery temperature
- Current keyed answer: **B. Moving a beverage shipment to another depot**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): move the beverage shipment to the West Depot — Người đàn ông đề xuất chuyển lô đồ uống sang kho West Depot vì nơi đó còn chỗ lạnh chưa sử dụng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: move the beverage shipment to the West Depot
- Current explanation: Người đàn ông đề xuất chuyển lô đồ uống sang kho West Depot vì nơi đó còn chỗ lạnh chưa sử dụng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What must happen before the West Depot accepts the shipment?**

- Choices: A. The customer must pay the invoice<br>B. The truck must be inspected<br>**C. An updated temperature log must be sent**<br>D. The warehouse manager must return
- Current keyed answer: **C. An updated temperature log must be sent**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): needs the updated temperature log — Người phụ nữ nêu điều kiện kho West Depot cần nhật ký nhiệt độ cập nhật trước khi nhận thêm hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: needs the updated temperature log
- Current explanation: Người phụ nữ nêu điều kiện kho West Depot cần nhật ký nhiệt độ cập nhật trước khi nhận thêm hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-recruitment-assessment-room` · Preparing a recruitment assessment

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The recruitment assessment is scheduled for Tuesday morning, but the training room is no longer available. Facilities has booked it for a fire-safety inspection. I can reserve the smaller conference room on the fourth floor. It has twelve computers, which should be enough for the shortlisted candidates. There are fourteen candidates on the final list. Could two of them complete the assessment remotely? Yes. I will contact those candidates and send the revised instructions before the end of the day.
- Transcript translation: Phòng đào tạo bị đặt cho cuộc kiểm tra an toàn nên buổi đánh giá tuyển dụng phải chuyển địa điểm. Phòng họp nhỏ có 12 máy tính nhưng có 14 ứng viên; hai người có thể làm từ xa. Người phụ nữ sẽ liên hệ họ và gửi hướng dẫn mới.

**Q1. Why must the assessment location be changed?**

- Choices: A. The candidates requested a later date<br>**B. The training room is booked for an inspection**<br>C. The computers have not been delivered<br>D. The recruiter is working remotely
- Current keyed answer: **B. The training room is booked for an inspection**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): booked it for a fire-safety inspection — Phòng đào tạo đã được bộ phận Cơ sở vật chất đặt cho cuộc kiểm tra an toàn cháy nổ vào cùng thời điểm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: booked it for a fire-safety inspection
- Current explanation: Phòng đào tạo đã được bộ phận Cơ sở vật chất đặt cho cuộc kiểm tra an toàn cháy nổ vào cùng thời điểm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. How many candidates are on the final list?**

- Choices: A. Twelve<br>B. Two<br>**C. Fourteen**<br>D. Sixteen
- Current keyed answer: **C. Fourteen**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): fourteen candidates on the final list — Người đàn ông nói rõ có fourteen candidates trong danh sách cuối cùng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: fourteen candidates on the final list
- Current explanation: Người đàn ông nói rõ có fourteen candidates trong danh sách cuối cùng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will the woman do next?**

- Choices: **A. Contact two candidates about taking the assessment remotely**<br>B. Order six more computers<br>C. Cancel Tuesday’s assessment<br>D. Ask Facilities to postpone the inspection
- Current keyed answer: **A. Contact two candidates about taking the assessment remotely**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): I will contact those candidates — Người phụ nữ nhận nhiệm vụ liên hệ hai ứng viên và gửi hướng dẫn sửa đổi trong ngày.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I will contact those candidates
- Current explanation: Người phụ nữ nhận nhiệm vụ liên hệ hai ứng viên và gửi hướng dẫn sửa đổi trong ngày.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-conference-catering-count` · Revising a conference catering order

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The catering company has confirmed lunch for 120 people, but registration has increased to 138. We also received six requests for vegetarian meals. The contract allows us to change the quantity until Thursday. We should add eighteen meals and list the dietary requests separately. I will update the attendance sheet. Do you want me to ask for the extra meals to be individually labeled? Yes, please. That will help the volunteers distribute the correct meals during the lunch break.
- Transcript translation: Số người tham dự hội nghị tăng từ 120 lên 138 và có sáu yêu cầu ăn chay. Hợp đồng cho phép thay đổi số lượng đến thứ Năm. Hai người thống nhất thêm 18 suất và dán nhãn riêng để phát đúng bữa ăn.

**Q1. What are the speakers mainly discussing?**

- Choices: **A. A change to a conference lunch order**<br>B. A new registration website<br>C. A delay in the keynote presentation<br>D. A request to cancel the event
- Current keyed answer: **A. A change to a conference lunch order**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): registration has increased to 138 — Số người đăng ký tăng từ 120 lên 138 và hai người thống nhất cập nhật số suất ăn cùng yêu cầu ăn chay.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: registration has increased to 138
- Current explanation: Số người đăng ký tăng từ 120 lên 138 và hai người thống nhất cập nhật số suất ăn cùng yêu cầu ăn chay.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. How many additional meals do they plan to order?**

- Choices: A. Six<br>B. Twelve<br>**C. Eighteen**<br>D. Thirty-eight
- Current keyed answer: **C. Eighteen**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): add eighteen meals — Người đàn ông đề xuất thêm eighteen meals để tăng từ 120 lên 138 suất.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: add eighteen meals
- Current explanation: Người đàn ông đề xuất thêm eighteen meals để tăng từ 120 lên 138 suất.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What does the man ask the woman to do?**

- Choices: A. Contact the keynote speaker<br>**B. Label the additional meals individually**<br>C. Move lunch to another room<br>D. Prepare a new catering contract
- Current keyed answer: **B. Label the additional meals individually**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): extra meals to be individually labeled — Người đàn ông đồng ý yêu cầu dán nhãn riêng từng suất ăn để tình nguyện viên phân phát đúng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: extra meals to be individually labeled
- Current explanation: Người đàn ông đồng ý yêu cầu dán nhãn riêng từng suất ăn để tình nguyện viên phân phát đúng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-software-pilot-feedback` · Discussing pilot software feedback

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The pilot group has finished testing the new inventory application. Most users like the barcode scanner, but several reported that the weekly export takes too long. The developer has already identified a problem with large files. A performance update is scheduled for Wednesday. Should we delay the company-wide launch until the update is tested? I recommend keeping the launch date, provided the pilot group confirms that the export problem is fixed by Friday.
- Transcript translation: Nhóm thử nghiệm thích máy quét mã vạch nhưng báo cáo chức năng xuất dữ liệu tuần còn chậm. Nhà phát triển lên lịch cập nhật vào thứ Tư. Người phụ nữ đề nghị giữ ngày ra mắt toàn công ty nếu nhóm thử nghiệm xác nhận lỗi được khắc phục trước thứ Sáu.

**Q1. What have the pilot users reported?**

- Choices: A. The barcode scanner is difficult to operate<br>**B. The weekly data export is slow**<br>C. The application cannot connect to the network<br>D. The user guide is missing
- Current keyed answer: **B. The weekly data export is slow**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): the weekly export takes too long — Người đàn ông cho biết nhiều người dùng phản ánh thao tác xuất dữ liệu hàng tuần mất quá nhiều thời gian.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: the weekly export takes too long
- Current explanation: Người đàn ông cho biết nhiều người dùng phản ánh thao tác xuất dữ liệu hàng tuần mất quá nhiều thời gian.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When is the performance update scheduled?**

- Choices: A. Monday<br>B. Tuesday<br>**C. Wednesday**<br>D. Friday
- Current keyed answer: **C. Wednesday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): scheduled for Wednesday — Người phụ nữ nói bản cập nhật hiệu năng đã được lên lịch vào Wednesday.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: scheduled for Wednesday
- Current explanation: Người phụ nữ nói bản cập nhật hiệu năng đã được lên lịch vào Wednesday.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What condition does the woman set for keeping the launch date?**

- Choices: **A. The pilot group must confirm the export issue is fixed by Friday**<br>B. The barcode scanner must be replaced<br>C. The company must hire another developer<br>D. The launch must be moved to Wednesday
- Current keyed answer: **A. The pilot group must confirm the export issue is fixed by Friday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): confirms that the export problem is fixed by Friday — Cô ấy đồng ý giữ ngày ra mắt nếu nhóm thử nghiệm xác nhận lỗi xuất dữ liệu được sửa trước thứ Sáu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: confirms that the export problem is fixed by Friday
- Current explanation: Cô ấy đồng ý giữ ngày ra mắt nếu nhóm thử nghiệm xác nhận lỗi xuất dữ liệu được sửa trước thứ Sáu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-business-travel-itinerary` · Updating a business travel itinerary

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: I received the revised agenda for the supplier meeting in Singapore. The first session now starts at nine on Thursday instead of ten. That means the morning flight will be too late. Can you move my reservation to the previous evening? There is a flight leaving at six forty on Wednesday evening. It arrives before midnight, and one standard seat is still available. Please book that flight and keep the return ticket unchanged. I have already arranged the hotel for Wednesday night.
- Transcript translation: Lịch họp nhà cung cấp được chuyển sớm hơn một giờ nên chuyến bay sáng thứ Năm không phù hợp. Có chuyến bay tối thứ Tư lúc 6:40. Người đàn ông yêu cầu đặt chuyến đó và giữ nguyên vé về.

**Q1. Why does the man need to change his flight?**

- Choices: **A. The supplier meeting begins earlier**<br>B. The return flight has been canceled<br>C. The hotel has no available rooms<br>D. His passport needs to be renewed
- Current keyed answer: **A. The supplier meeting begins earlier**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): starts at nine on Thursday instead of ten — Cuộc họp nhà cung cấp bắt đầu lúc 9 giờ thay vì 10 giờ, khiến chuyến bay buổi sáng không còn phù hợp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: starts at nine on Thursday instead of ten
- Current explanation: Cuộc họp nhà cung cấp bắt đầu lúc 9 giờ thay vì 10 giờ, khiến chuyến bay buổi sáng không còn phù hợp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When does the available flight depart?**

- Choices: A. Tuesday evening<br>B. Wednesday morning<br>**C. Wednesday evening**<br>D. Thursday afternoon
- Current keyed answer: **C. Wednesday evening**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): leaving at six forty on Wednesday evening — Người phụ nữ nêu chuyến bay rời đi lúc 6:40 tối thứ Tư.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: leaving at six forty on Wednesday evening
- Current explanation: Người phụ nữ nêu chuyến bay rời đi lúc 6:40 tối thứ Tư.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What does the man ask the woman to do?**

- Choices: A. Change the hotel reservation<br>**B. Book the Wednesday evening flight**<br>C. Cancel the return ticket<br>D. Reserve a premium seat
- Current keyed answer: **B. Book the Wednesday evening flight**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): Please book that flight — Người đàn ông yêu cầu đặt chuyến bay tối thứ Tư và giữ nguyên vé khứ hồi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Please book that flight
- Current explanation: Người đàn ông yêu cầu đặt chuyến bay tối thứ Tư và giữ nguyên vé khứ hồi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-customer-replacement-delivery` · Arranging a replacement delivery

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: A customer reported that one of the display monitors arrived with a cracked screen. The other three units in the same package appear to be undamaged. I checked the warranty record. We can send a replacement monitor at no charge, but the damaged unit must be collected first. The customer is available on Friday afternoon. Can the courier collect the damaged unit and deliver the replacement during the same visit? I will request a combined pickup and delivery. The courier needs the original packaging, so please remind the customer to keep the box.
- Transcript translation: Một màn hình trong gói hàng bị nứt. Công ty có thể gửi sản phẩm thay thế miễn phí sau khi thu hồi máy hỏng. Nhân viên sẽ yêu cầu đơn vị giao nhận vừa lấy máy hỏng vừa giao máy mới vào chiều thứ Sáu, đồng thời nhắc khách giữ hộp gốc.

**Q1. What problem did the customer report?**

- Choices: **A. A monitor arrived with a cracked screen**<br>B. The order contained the wrong model<br>C. The delivery was sent to another office<br>D. A monitor stopped connecting to the network
- Current keyed answer: **A. A monitor arrived with a cracked screen**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): arrived with a cracked screen — Khách hàng báo một màn hình bị nứt khi nhận hàng; ba thiết bị còn lại không hư hỏng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: arrived with a cracked screen
- Current explanation: Khách hàng báo một màn hình bị nứt khi nhận hàng; ba thiết bị còn lại không hư hỏng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What must happen before the replacement is sent?**

- Choices: A. The customer must pay a new delivery fee<br>**B. The damaged unit must be collected**<br>C. The warranty must be extended<br>D. All four monitors must be returned
- Current keyed answer: **B. The damaged unit must be collected**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): the damaged unit must be collected first — Người phụ nữ nói thiết bị hư hỏng phải được thu hồi trước khi gửi màn hình thay thế.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: the damaged unit must be collected first
- Current explanation: Người phụ nữ nói thiết bị hư hỏng phải được thu hồi trước khi gửi màn hình thay thế.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What does the woman ask the man to remind the customer to do?**

- Choices: A. Send a photograph of the office<br>**B. Keep the original packaging**<br>C. Call the manufacturer directly<br>D. Sign a new warranty agreement
- Current keyed answer: **B. Keep the original packaging**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): keep the box — Đơn vị vận chuyển cần bao bì gốc, nên khách hàng được nhắc giữ lại hộp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: keep the box
- Current explanation: Đơn vị vận chuyển cần bao bì gốc, nên khách hàng được nhắc giữ lại hộp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-procurement-quote-comparison` · Comparing equipment quotations

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: We have received two quotations for the new conference-room projectors. Northstar is less expensive, but its delivery time is three weeks. The other supplier, Brightline, can deliver in ten days. Their price is higher, although installation is included. The facilities team needs the projectors before the annual meeting next month. I think the shorter delivery time is important. Agreed. Let us ask Brightline for a demonstration unit before we approve the purchase.
- Transcript translation: Hai nhân viên so sánh hai báo giá máy chiếu. Brightline đắt hơn nhưng giao nhanh hơn và bao gồm lắp đặt. Vì cần thiết bị trước cuộc họp thường niên, họ sẽ yêu cầu Brightline cung cấp máy mẫu để trình diễn.

**Q1. What are the speakers comparing?**

- Choices: **A. Two quotations for conference-room projectors**<br>B. Two plans for employee relocation<br>C. Two maintenance schedules for elevators<br>D. Two bids for office cleaning
- Current keyed answer: **A. Two quotations for conference-room projectors**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): two quotations for the new conference-room projectors — Hai người so sánh hai báo giá cho máy chiếu phòng hội nghị.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: two quotations for the new conference-room projectors
- Current explanation: Hai người so sánh hai báo giá cho máy chiếu phòng hội nghị.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What advantage does Brightline offer?**

- Choices: A. A lower price<br>B. A longer warranty<br>**C. Faster delivery with installation included**<br>D. Free replacement lamps for a year
- Current keyed answer: **C. Faster delivery with installation included**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): can deliver in ten days. Their price is higher, although installation is included. — Brightline giao trong 10 ngày và đã bao gồm lắp đặt, trong khi nhà cung cấp kia mất ba tuần.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: can deliver in ten days. Their price is higher, although installation is included.
- Current explanation: Brightline giao trong 10 ngày và đã bao gồm lắp đặt, trong khi nhà cung cấp kia mất ba tuần.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What do the speakers plan to request next?**

- Choices: A. A discount from Northstar<br>**B. A demonstration unit from Brightline**<br>C. A larger conference room<br>D. A new annual meeting date
- Current keyed answer: **B. A demonstration unit from Brightline**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): a demonstration unit — Người đàn ông đề nghị yêu cầu Brightline cung cấp một thiết bị mẫu để trình diễn trước khi duyệt mua.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: a demonstration unit
- Current explanation: Người đàn ông đề nghị yêu cầu Brightline cung cấp một thiết bị mẫu để trình diễn trước khi duyệt mua.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-month-end-expense-reconciliation` · Reconciling month-end expenses

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The travel expense report for October is missing receipts for two taxi rides. The total amount is small, but the audit team requires supporting documents for every claim. I have the electronic receipts in my email. The employee submitted the paper report before leaving for a business trip. Could you forward the electronic copies to the accounts-payable mailbox today? We need to close the report by four. Of course. I will send them now and add a note explaining why the original receipts were not attached.
- Transcript translation: Báo cáo chi phí tháng Mười thiếu hai hóa đơn taxi, dù đội kiểm toán yêu cầu chứng từ cho mọi khoản. Người phụ nữ có hóa đơn điện tử trong email và sẽ gửi tới hộp thư công nợ phải trả, kèm ghi chú giải thích.

**Q1. What is missing from the expense report?**

- Choices: **A. Two taxi receipts**<br>B. A hotel reservation<br>C. A manager’s signature<br>D. The employee’s travel itinerary
- Current keyed answer: **A. Two taxi receipts**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): missing receipts for two taxi rides — Báo cáo thiếu hóa đơn cho hai chuyến taxi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: missing receipts for two taxi rides
- Current explanation: Báo cáo thiếu hóa đơn cho hai chuyến taxi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Where does the woman have the receipts?**

- Choices: A. In a filing cabinet<br>**B. In her email**<br>C. At the hotel reception<br>D. In the employee’s car
- Current keyed answer: **B. In her email**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): electronic receipts in my email — Người phụ nữ nói cô ấy có hóa đơn điện tử trong email.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: electronic receipts in my email
- Current explanation: Người phụ nữ nói cô ấy có hóa đơn điện tử trong email.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will the woman do?**

- Choices: A. Submit a new travel request<br>**B. Forward the receipts and add an explanatory note**<br>C. Ask the audit team to cancel the review<br>D. Wait until the employee returns
- Current keyed answer: **B. Forward the receipts and add an explanatory note**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): send them now and add a note — Cô ấy sẽ gửi các bản điện tử ngay và thêm ghi chú giải thích vì sao chưa đính kèm bản gốc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: send them now and add a note
- Current explanation: Cô ấy sẽ gửi các bản điện tử ngay và thêm ghi chú giải thích vì sao chưa đính kèm bản gốc.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-safety-training-evacuation` · Preparing an evacuation training session

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The annual evacuation exercise is scheduled for next Wednesday at ten. The safety officer wants all department coordinators to attend a short briefing beforehand. I can attend, but the production supervisors are working on the morning shift. Could the briefing be recorded for them? Yes. The safety officer will record it and upload the video to the staff portal by the end of the day. Great. I will send the meeting invitation to the coordinators and remind the supervisors to watch the recording before the exercise.
- Transcript translation: Buổi diễn tập sơ tán hằng năm diễn ra lúc 10 giờ thứ Tư tuần tới. Một số giám sát sản xuất làm ca sáng nên khó dự buổi hướng dẫn trước đó. Nhân viên an toàn sẽ ghi hình và tải video lên cổng nhân viên.

**Q1. When will the evacuation exercise take place?**

- Choices: A. Next Monday at ten<br>**B. Next Wednesday at ten**<br>C. Next Wednesday at noon<br>D. The following Friday
- Current keyed answer: **B. Next Wednesday at ten**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): next Wednesday at ten — Người phụ nữ nêu rõ buổi diễn tập được lên lịch vào 10 giờ thứ Tư tuần tới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: next Wednesday at ten
- Current explanation: Người phụ nữ nêu rõ buổi diễn tập được lên lịch vào 10 giờ thứ Tư tuần tới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why might some supervisors miss the briefing?**

- Choices: A. They are attending a conference<br>**B. They are working the morning shift**<br>C. They are on annual leave<br>D. They are visiting another office
- Current keyed answer: **B. They are working the morning shift**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): working on the morning shift — Người đàn ông nói các giám sát sản xuất làm ca sáng nên có thể không tham gia buổi hướng dẫn trực tiếp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: working on the morning shift
- Current explanation: Người đàn ông nói các giám sát sản xuất làm ca sáng nên có thể không tham gia buổi hướng dẫn trực tiếp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Where will the recording be made available?**

- Choices: **A. On the staff portal**<br>B. In the main reception area<br>C. By postal mail<br>D. On the company’s public website
- Current keyed answer: **A. On the staff portal**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): upload the video to the staff portal — Video sẽ được tải lên cổng thông tin nhân viên vào cuối ngày.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: upload the video to the staff portal
- Current explanation: Video sẽ được tải lên cổng thông tin nhân viên vào cuối ngày.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-international-shipment-customs` · Resolving a customs-document issue

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The replacement machine parts are still at the export terminal. Customs has asked for a more detailed description of the components on the commercial invoice. The invoice only says “metal parts.” I can prepare a revised document with the product codes and country of origin. Please include the quantities for each code as well. The freight forwarder said that the shipment can be released once the corrected invoice is received. I will add the product codes, country of origin, and quantities for each code, then send the revised invoice to the forwarder before lunch and copy the purchasing manager.
- Transcript translation: Lô linh kiện máy móc đang bị giữ tại cảng xuất vì hải quan cần mô tả chi tiết hơn trên hóa đơn. Nhân viên sẽ thêm mã sản phẩm, xuất xứ và số lượng từng mã rồi gửi hóa đơn chỉnh sửa cho đơn vị giao nhận trước bữa trưa.

**Q1. Why is the shipment being held?**

- Choices: A. The machine parts were damaged<br>**B. Customs needs a more detailed invoice description**<br>C. The freight forwarder has changed companies<br>D. The purchasing manager has not approved the order
- Current keyed answer: **B. Customs needs a more detailed invoice description**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Customs has asked for a more detailed description — Hải quan yêu cầu mô tả chi tiết hơn các linh kiện trên hóa đơn thương mại nên lô hàng chưa được thông quan.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Customs has asked for a more detailed description
- Current explanation: Hải quan yêu cầu mô tả chi tiết hơn các linh kiện trên hóa đơn thương mại nên lô hàng chưa được thông quan.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What information will the woman add?**

- Choices: **A. Product codes, country of origin, and quantities for each code**<br>B. The driver’s name and phone number<br>C. A new payment schedule<br>D. The warehouse opening hours
- Current keyed answer: **A. Product codes, country of origin, and quantities for each code**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): product codes, country of origin, and quantities for each code — Người phụ nữ xác nhận sẽ bổ sung mã sản phẩm, quốc gia xuất xứ và số lượng tương ứng của từng mã trước khi gửi hóa đơn sửa đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: product codes, country of origin, and quantities for each code
- Current explanation: Người phụ nữ xác nhận sẽ bổ sung mã sản phẩm, quốc gia xuất xứ và số lượng tương ứng của từng mã trước khi gửi hóa đơn sửa đổi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When can the shipment be released?**

- Choices: **A. After the corrected invoice is received**<br>B. After the next scheduled inspection<br>C. When the customer pays in cash<br>D. At the end of the following month
- Current keyed answer: **A. After the corrected invoice is received**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): released once the corrected invoice is received — Đơn vị giao nhận thông báo hàng có thể được giải phóng sau khi nhận hóa đơn đã chỉnh sửa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: released once the corrected invoice is received
- Current explanation: Đơn vị giao nhận thông báo hàng có thể được giải phóng sau khi nhận hóa đơn đã chỉnh sửa.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-office-relocation-equipment` · Coordinating an office equipment move

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The finance department will move to the renovated floor on the twenty-second. The movers can transport the desks and cabinets, but the IT team must disconnect the workstations. IT can start after five on Friday. We should label each monitor and docking station with the employee’s new desk number. I have prepared the seating plan. I will send it to the moving company and the IT coordinator this afternoon. Please also reserve two carts for the archive boxes. Those files must stay with the finance department during the move.
- Transcript translation: Bộ phận Tài chính sẽ chuyển lên tầng đã cải tạo vào ngày 22. Nhóm chuyển nhà vận chuyển bàn và tủ, còn IT ngắt kết nối máy trạm sau 5 giờ chiều thứ Sáu. Nhân viên cũng cần dán nhãn màn hình và đặt hai xe đẩy cho thùng hồ sơ.

**Q1. Which department is relocating?**

- Choices: A. Human Resources<br>**B. Finance**<br>C. Customer Service<br>D. Information Technology
- Current keyed answer: **B. Finance**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): the finance department will move — Người phụ nữ nói rõ bộ phận Tài chính sẽ chuyển lên tầng đã cải tạo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: the finance department will move
- Current explanation: Người phụ nữ nói rõ bộ phận Tài chính sẽ chuyển lên tầng đã cải tạo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When can the IT team begin disconnecting workstations?**

- Choices: **A. After five on Friday**<br>B. Before noon on Thursday<br>C. On the twenty-second in the morning<br>D. During the weekend
- Current keyed answer: **A. After five on Friday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): start after five on Friday — Người đàn ông nói bộ phận IT có thể bắt đầu sau 5 giờ chiều thứ Sáu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: start after five on Friday
- Current explanation: Người đàn ông nói bộ phận IT có thể bắt đầu sau 5 giờ chiều thứ Sáu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What does the man ask the woman to reserve?**

- Choices: A. A storage room for new desks<br>**B. Two carts for archive boxes**<br>C. Extra monitors for the IT team<br>D. A meeting room for employees
- Current keyed answer: **B. Two carts for archive boxes**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): reserve two carts for the archive boxes — Anh ấy yêu cầu đặt hai xe đẩy cho các thùng hồ sơ lưu trữ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: reserve two carts for the archive boxes
- Current explanation: Anh ấy yêu cầu đặt hai xe đẩy cho các thùng hồ sơ lưu trữ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-vendor-payment-portal` · A change to vendor payment submissions

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Beginning on the first of next month, all vendor invoices must be submitted through the supplier portal. Invoices sent directly to individual employees will be returned without processing. Each submission should include the purchase-order number and the receiving confirmation. The finance team will review complete invoices within five business days. Suppliers who have difficulty accessing the portal should contact the vendor-support desk.
- Transcript translation: Từ ngày đầu tháng tới, hóa đơn nhà cung cấp phải gửi qua cổng nhà cung cấp. Mỗi lần gửi phải có số đơn đặt hàng và xác nhận nhận hàng. Bộ phận Tài chính xử lý hồ sơ đầy đủ trong vòng năm ngày làm việc.

**Q1. What change is being announced?**

- Choices: **A. Invoices must be sent through the supplier portal**<br>B. Payments will be made every Friday<br>C. Purchase orders will be discontinued<br>D. Suppliers must visit the finance office
- Current keyed answer: **A. Invoices must be sent through the supplier portal**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): submitted through the supplier portal — Thông báo yêu cầu tất cả hóa đơn nhà cung cấp được gửi qua cổng nhà cung cấp từ đầu tháng tới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: submitted through the supplier portal
- Current explanation: Thông báo yêu cầu tất cả hóa đơn nhà cung cấp được gửi qua cổng nhà cung cấp từ đầu tháng tới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Which two details must be included?**

- Choices: A. A bank statement and a tax return<br>**B. A purchase-order number and receiving confirmation**<br>C. A delivery photograph and employee ID<br>D. A signed contract and a price list
- Current keyed answer: **B. A purchase-order number and receiving confirmation**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): purchase-order number and the receiving confirmation — Người thông báo yêu cầu số đơn đặt hàng và xác nhận đã nhận hàng đi kèm mỗi lần gửi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: purchase-order number and the receiving confirmation
- Current explanation: Người thông báo yêu cầu số đơn đặt hàng và xác nhận đã nhận hàng đi kèm mỗi lần gửi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. How long will the finance team take to review complete invoices?**

- Choices: A. Two calendar days<br>B. Three business days<br>**C. Five business days**<br>D. Ten business days
- Current keyed answer: **C. Five business days**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): within five business days — Thông báo nêu bộ phận Tài chính sẽ xem xét hóa đơn đầy đủ trong vòng năm ngày làm việc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: within five business days
- Current explanation: Thông báo nêu bộ phận Tài chính sẽ xem xét hóa đơn đầy đủ trong vòng năm ngày làm việc.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-loading-dock-temporary-closure` · A temporary loading-dock closure

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Attention, delivery drivers. The east loading dock will be closed from Tuesday through Thursday while the floor markings are replaced. During this period, all incoming deliveries should use the west entrance near Gate Three. Please check in at the security booth before unloading. The usual delivery appointment times will remain in effect, and warehouse staff will direct vehicles to the correct bay.
- Transcript translation: Cửa bốc dỡ phía Đông đóng từ thứ Ba đến thứ Năm để thay vạch sàn. Xe giao hàng phải đi qua lối phía Tây gần Cổng 3, đăng ký tại chốt an ninh rồi mới dỡ hàng. Giờ hẹn giao hàng không thay đổi.

**Q1. Why will the east loading dock be closed?**

- Choices: **A. The floor markings are being replaced**<br>B. A new security booth is being built<br>C. The warehouse is changing its opening hours<br>D. The entrance road is being widened
- Current keyed answer: **A. The floor markings are being replaced**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): floor markings are replaced — Khu bốc dỡ phía Đông đóng cửa để thay lại vạch sàn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: floor markings are replaced
- Current explanation: Khu bốc dỡ phía Đông đóng cửa để thay lại vạch sàn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Where should incoming deliveries go?**

- Choices: A. The main office entrance<br>**B. The west entrance near Gate Three**<br>C. The visitor parking lot<br>D. The south warehouse door
- Current keyed answer: **B. The west entrance near Gate Three**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): west entrance near Gate Three — Người thông báo yêu cầu mọi xe giao hàng đến lối vào phía Tây gần Cổng số Ba.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: west entrance near Gate Three
- Current explanation: Người thông báo yêu cầu mọi xe giao hàng đến lối vào phía Tây gần Cổng số Ba.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should drivers do before unloading?**

- Choices: A. Call the purchasing manager<br>B. Wait for a new appointment<br>**C. Check in at the security booth**<br>D. Park outside the property
- Current keyed answer: **C. Check in at the security booth**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): check in at the security booth — Tài xế phải đăng ký tại chốt an ninh trước khi dỡ hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: check in at the security booth
- Current explanation: Tài xế phải đăng ký tại chốt an ninh trước khi dỡ hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-new-employee-orientation-agenda` · An updated orientation agenda

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Welcome to the company orientation for new employees. The session will begin at nine in Conference Room B, not in the training hall as originally planned. After a short introduction from Human Resources, participants will meet their department supervisors. A safety demonstration will follow at eleven fifteen. Please bring your employee identification form, which must be completed before the lunch break. Printed copies are available at the registration desk.
- Transcript translation: Buổi định hướng bắt đầu lúc 9 giờ tại Phòng họp B. Sau phần giới thiệu của Nhân sự, người tham gia gặp quản lý bộ phận. Phần trình diễn an toàn diễn ra lúc 11:15; biểu mẫu nhận dạng nhân viên phải hoàn thành trước giờ ăn trưa.

**Q1. Where will the orientation take place?**

- Choices: A. In the training hall<br>**B. In Conference Room B**<br>C. At the registration desk<br>D. In the cafeteria
- Current keyed answer: **B. In Conference Room B**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Conference Room B — Địa điểm được cập nhật là Phòng họp B thay vì hội trường đào tạo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Conference Room B
- Current explanation: Địa điểm được cập nhật là Phòng họp B thay vì hội trường đào tạo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What will happen at eleven fifteen?**

- Choices: **A. A safety demonstration**<br>B. A lunch break<br>C. A department tour<br>D. A payroll presentation
- Current keyed answer: **A. A safety demonstration**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): A safety demonstration will follow at eleven fifteen — Chương trình nêu phần trình diễn an toàn sẽ diễn ra lúc 11:15.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: A safety demonstration will follow at eleven fifteen
- Current explanation: Chương trình nêu phần trình diễn an toàn sẽ diễn ra lúc 11:15.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What must participants complete before lunch?**

- Choices: A. A travel request<br>**B. An employee identification form**<br>C. A benefits survey<br>D. A computer skills test
- Current keyed answer: **B. An employee identification form**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): employee identification form — Người mới phải hoàn thành biểu mẫu nhận dạng nhân viên trước giờ nghỉ trưa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: employee identification form
- Current explanation: Người mới phải hoàn thành biểu mẫu nhận dạng nhân viên trước giờ nghỉ trưa.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-quarterly-sales-data-cutoff` · A deadline for the quarterly sales report

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: The quarterly sales report will be distributed to regional managers next Monday. To ensure that all figures are included, branch offices must enter their final sales data by five p.m. on Thursday. Any corrections submitted after that time will be included in the following report. The analytics team will send a confirmation email when each branch has completed its submission. Questions about the reporting template should be directed to the sales operations mailbox.
- Transcript translation: Báo cáo doanh số quý được gửi vào thứ Hai tuần tới. Các chi nhánh phải nhập số liệu cuối cùng trước 5 giờ chiều thứ Năm. Chỉnh sửa sau hạn sẽ chuyển sang báo cáo kế tiếp.

**Q1. When will the quarterly sales report be distributed?**

- Choices: **A. Next Monday**<br>B. This Thursday<br>C. The end of the month<br>D. The following Friday
- Current keyed answer: **A. Next Monday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): distributed to regional managers next Monday — Báo cáo sẽ được gửi tới quản lý khu vực vào thứ Hai tuần tới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: distributed to regional managers next Monday
- Current explanation: Báo cáo sẽ được gửi tới quản lý khu vực vào thứ Hai tuần tới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. By when must branch offices enter their final data?**

- Choices: A. By noon on Wednesday<br>**B. By five p.m. on Thursday**<br>C. By the end of Friday<br>D. Before the next monthly meeting
- Current keyed answer: **B. By five p.m. on Thursday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): by five p.m. on Thursday — Hạn chót được nêu rõ là 5 giờ chiều thứ Năm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: by five p.m. on Thursday
- Current explanation: Hạn chót được nêu rõ là 5 giờ chiều thứ Năm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What happens to corrections submitted after the deadline?**

- Choices: A. They are rejected permanently<br>B. They are sent to the branch supervisor<br>**C. They appear in the following report**<br>D. They delay the report by one week
- Current keyed answer: **C. They appear in the following report**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): included in the following report — Các chỉnh sửa sau giờ chốt sẽ được đưa vào báo cáo tiếp theo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: included in the following report
- Current explanation: Các chỉnh sửa sau giờ chốt sẽ được đưa vào báo cáo tiếp theo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-building-elevator-maintenance` · An elevator maintenance announcement

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: A maintenance inspection of the north elevator will take place tomorrow from eight in the morning until one in the afternoon. During this period, please use the south elevator or the stairs. Contractors will also test the emergency communication system on each floor. Building occupants may hear a short alarm during the test; no action is required unless a member of the safety team gives an instruction. We apologize for the inconvenience.
- Transcript translation: Thang máy phía Bắc được kiểm tra từ 8 giờ sáng đến 1 giờ chiều ngày mai. Trong thời gian đó, người trong tòa nhà dùng thang phía Nam hoặc cầu thang bộ. Hệ thống liên lạc khẩn cấp được thử, có thể phát ra chuông ngắn.

**Q1. When will the north elevator be inspected?**

- Choices: A. Today from one to five<br>**B. Tomorrow from eight to one**<br>C. On Friday afternoon<br>D. Next Monday morning
- Current keyed answer: **B. Tomorrow from eight to one**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): tomorrow from eight in the morning until one — Thông báo nêu khoảng thời gian kiểm tra là ngày mai từ 8 giờ sáng đến 1 giờ chiều.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: tomorrow from eight in the morning until one
- Current explanation: Thông báo nêu khoảng thời gian kiểm tra là ngày mai từ 8 giờ sáng đến 1 giờ chiều.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should building occupants use during the inspection?**

- Choices: **A. The south elevator or the stairs**<br>B. The service entrance only<br>C. The parking garage elevator<br>D. The loading dock ramp
- Current keyed answer: **A. The south elevator or the stairs**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): use the south elevator or the stairs — Người trong tòa nhà được hướng dẫn dùng thang máy phía Nam hoặc cầu thang bộ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: use the south elevator or the stairs
- Current explanation: Người trong tòa nhà được hướng dẫn dùng thang máy phía Nam hoặc cầu thang bộ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What may occupants hear during the test?**

- Choices: A. A fire alarm lasting several minutes<br>**B. A short alarm**<br>C. A public-address message about parking<br>D. A telephone ringing on every floor
- Current keyed answer: **B. A short alarm**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): may hear a short alarm — Hệ thống liên lạc khẩn cấp sẽ được thử và người trong tòa nhà có thể nghe một chuông báo ngắn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: may hear a short alarm
- Current explanation: Hệ thống liên lạc khẩn cấp sẽ được thử và người trong tòa nhà có thể nghe một chuông báo ngắn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-travel-reimbursement-deadline` · A reminder about travel reimbursements

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Employees who traveled for business in November should submit reimbursement requests by December sixth. Please upload receipts for transportation, lodging, and meals to the expense system. If a receipt is unavailable, add a short explanation and obtain approval from your department manager. Requests submitted after the deadline may be processed in the next payment cycle. The finance help desk will hold an online question session on Wednesday at two.
- Transcript translation: Nhân viên đi công tác trong tháng Mười Một phải gửi yêu cầu hoàn phí trước ngày 6 tháng 12. Cần tải hóa đơn lên hệ thống. Nếu không có hóa đơn, phải ghi giải thích và xin quản lý phê duyệt. Buổi hỏi đáp trực tuyến diễn ra thứ Tư lúc 2 giờ.

**Q1. Who is the announcement intended for?**

- Choices: **A. Employees who traveled for business in November**<br>B. Customers with outstanding invoices<br>C. Managers attending a budget meeting<br>D. New vendors registering for payment
- Current keyed answer: **A. Employees who traveled for business in November**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Employees who traveled for business in November — Thông báo hướng tới nhân viên đã đi công tác trong tháng Mười Một.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Employees who traveled for business in November
- Current explanation: Thông báo hướng tới nhân viên đã đi công tác trong tháng Mười Một.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should employees do if a receipt is unavailable?**

- Choices: A. Pay the expense again<br>**B. Add an explanation and obtain manager approval**<br>C. Contact the hotel for a refund<br>D. Wait until the next travel period
- Current keyed answer: **B. Add an explanation and obtain manager approval**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): add a short explanation and obtain approval — Nếu thiếu hóa đơn, nhân viên phải ghi giải thích ngắn và xin phê duyệt từ quản lý bộ phận.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: add a short explanation and obtain approval
- Current explanation: Nếu thiếu hóa đơn, nhân viên phải ghi giải thích ngắn và xin phê duyệt từ quản lý bộ phận.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When will the online question session take place?**

- Choices: A. Tuesday at ten<br>**B. Wednesday at two**<br>C. Thursday at six<br>D. Friday at noon
- Current keyed answer: **B. Wednesday at two**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Wednesday at two — Thông tin cuối bài nói bộ phận hỗ trợ Tài chính tổ chức buổi hỏi đáp trực tuyến vào thứ Tư lúc 2 giờ; đây là thời điểm được nêu trong thông báo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Wednesday at two
- Current explanation: Thông tin cuối bài nói bộ phận hỗ trợ Tài chính tổ chức buổi hỏi đáp trực tuyến vào thứ Tư lúc 2 giờ; đây là thời điểm được nêu trong thông báo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-conference-registration-policy` · A conference registration reminder

- Batch: `015` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Registration for the regional operations conference will close at noon on Friday. Employees who plan to attend should complete the online form and select their preferred workshop. Each department has a limited number of places, so confirmations will be sent in the order that applications are received. The conference will be held at the Riverside Center, and shuttle buses will leave from the main office at seven thirty on the event day. Please contact the events team if you need accessibility assistance.
- Transcript translation: Đăng ký hội nghị vận hành khu vực đóng lúc 12 giờ trưa thứ Sáu. Nhân viên phải điền biểu mẫu trực tuyến và chọn hội thảo. Chỗ tham dự được xác nhận theo thứ tự đăng ký. Xe đưa đón khởi hành từ văn phòng chính lúc 7:30.

**Q1. When will registration close?**

- Choices: **A. At noon on Friday**<br>B. At five on Thursday<br>C. At seven thirty on the event day<br>D. At the end of the month
- Current keyed answer: **A. At noon on Friday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): close at noon on Friday — Thông báo nêu đăng ký đóng lúc 12 giờ trưa thứ Sáu; đây là hạn cuối cho người muốn tham dự.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: close at noon on Friday
- Current explanation: Thông báo nêu đăng ký đóng lúc 12 giờ trưa thứ Sáu; đây là hạn cuối cho người muốn tham dự.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. How will attendance places be confirmed?**

- Choices: A. By department seniority<br>**B. In the order applications are received**<br>C. Through a random drawing<br>D. After the event begins
- Current keyed answer: **B. In the order applications are received**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): in the order that applications are received — Thông báo cho biết xác nhận được gửi theo thứ tự đơn đăng ký được nhận.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: in the order that applications are received
- Current explanation: Thông báo cho biết xác nhận được gửi theo thứ tự đơn đăng ký được nhận.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Where will shuttle buses depart from?**

- Choices: A. The Riverside Center<br>B. The airport terminal<br>**C. The main office**<br>D. The city bus station
- Current keyed answer: **C. The main office**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): leave from the main office at seven thirty — Xe buýt đưa đón khởi hành từ văn phòng chính lúc 7:30.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: leave from the main office at seven thirty
- Current explanation: Xe buýt đưa đón khởi hành từ văn phòng chính lúc 7:30.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-projector-maintenance-window` · A maintenance window for the conference room

- Batch: `024` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Hi, Daniel. The facilities team says the main conference room projector needs a replacement part. They can install it on Wednesday morning, but the room is booked for the quarterly planning session. I can move the planning session to Room 4, but that room only seats twelve. We have fifteen department heads attending. Could the installation be done after lunch instead? The technician has another appointment at one, so the earliest afternoon slot is three thirty. The room is free then. I will ask the team to reserve that time and send an updated notice. That works. Please also ask them to test the wireless connection before they leave. We had trouble sharing slides during last month’s review.
- Transcript translation: Chào Daniel. Bộ phận cơ sở vật chất cho biết máy chiếu ở phòng họp chính cần thay linh kiện. Họ có thể lắp vào sáng thứ Tư, nhưng phòng đã được đặt cho buổi lập kế hoạch quý. Daniel đề nghị chuyển buổi họp sang Phòng 4, nhưng phòng đó chỉ có 12 chỗ trong khi có 15 trưởng bộ phận tham dự. Maya đề nghị đặt lịch lắp đặt lúc 3 giờ 30 chiều, khi phòng trống, đồng thời kiểm tra kết nối không dây trước khi kỹ thuật viên rời đi.

**Q1. What problem does the conference room have?**

- Choices: **A. Its projector needs a replacement part**<br>B. Its air conditioning is broken<br>C. Its seating capacity has been reduced<br>D. Its wireless network has been disconnected
- Current keyed answer: **A. Its projector needs a replacement part**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): projector needs a replacement part — Nhóm cơ sở vật chất cho biết máy chiếu cần thay linh kiện.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: projector needs a replacement part
- Current explanation: Nhóm cơ sở vật chất cho biết máy chiếu cần thay linh kiện.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why does Daniel reject Room 4?**

- Choices: A. It is being renovated<br>**B. It cannot seat all the attendees**<br>C. It has no presentation screen<br>D. It is reserved for another team
- Current keyed answer: **B. It cannot seat all the attendees**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): only seats twelve — Phòng 4 chỉ có 12 chỗ, không đủ cho 15 trưởng bộ phận tham dự.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: only seats twelve
- Current explanation: Phòng 4 chỉ có 12 chỗ, không đủ cho 15 trưởng bộ phận tham dự.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will Maya ask the facilities team to do?**

- Choices: A. Move the quarterly session<br>B. Order fifteen new chairs<br>**C. Test the wireless connection**<br>D. Install a second projector
- Current keyed answer: **C. Test the wireless connection**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): test the wireless connection — Daniel yêu cầu kiểm tra kết nối không dây trước khi kỹ thuật viên rời đi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: test the wireless connection
- Current explanation: Daniel yêu cầu kiểm tra kết nối không dây trước khi kỹ thuật viên rời đi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-vendor-invoice-correction` · Correcting a vendor invoice

- Batch: `024` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Priya, I reviewed the invoice from Northstar Supplies. The total is correct, but the delivery fee appears twice. We should not approve it until the vendor sends a corrected copy. I noticed the duplicate charge too. The purchase order lists one delivery fee of eighty dollars. I will contact their billing department and attach the purchase order for reference. Please ask them to send the revision before Thursday. Accounts payable closes this month’s batch on Friday morning, and we need a full day to verify the changes. Understood. I will request the corrected invoice today and flag it in the tracking sheet. If it does not arrive tomorrow, I will call the account representative directly.
- Transcript translation: Priya, tôi đã kiểm tra hóa đơn của Northstar Supplies. Tổng tiền đúng nhưng phí giao hàng bị tính hai lần. Chúng ta không nên duyệt hóa đơn cho đến khi nhà cung cấp gửi bản điều chỉnh. Priya sẽ liên hệ bộ phận thanh toán và đính kèm đơn đặt hàng, trong đó ghi một khoản phí giao hàng 80 đô la. Cô ấy được yêu cầu xin bản sửa trước thứ Năm vì bộ phận công nợ khóa đợt thanh toán vào sáng thứ Sáu. Nếu chưa nhận được vào ngày mai, cô ấy sẽ gọi trực tiếp cho đại diện tài khoản.

**Q1. What is wrong with the invoice?**

- Choices: A. The item quantities are incorrect<br>**B. A delivery fee is listed twice**<br>C. The tax rate is missing<br>D. The purchase order number is invalid
- Current keyed answer: **B. A delivery fee is listed twice**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): delivery fee appears twice — Vấn đề là phí giao hàng xuất hiện hai lần trên hóa đơn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: delivery fee appears twice
- Current explanation: Vấn đề là phí giao hàng xuất hiện hai lần trên hóa đơn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What will Priya attach to her message?**

- Choices: A. A payment receipt<br>B. A shipping label<br>**C. The purchase order**<br>D. A monthly sales report
- Current keyed answer: **C. The purchase order**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): attach the purchase order — Priya sẽ đính kèm đơn đặt hàng để đối chiếu khoản phí giao hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: attach the purchase order
- Current explanation: Priya sẽ đính kèm đơn đặt hàng để đối chiếu khoản phí giao hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why is Thursday the requested deadline?**

- Choices: A. The vendor closes on Friday<br>B. The invoice must be paid immediately<br>**C. Accounts payable closes its batch on Friday morning**<br>D. The purchase order expires Thursday
- Current keyed answer: **C. Accounts payable closes its batch on Friday morning**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): closes this month’s batch on Friday morning — Bộ phận công nợ khóa đợt thanh toán vào sáng thứ Sáu nên cần nhận hóa đơn sửa trước đó.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: closes this month’s batch on Friday morning
- Current explanation: Bộ phận công nợ khóa đợt thanh toán vào sáng thứ Sáu nên cần nhận hóa đơn sửa trước đó.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `part3-training-room-change` · Changing a training room

- Batch: `024` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The customer service workshop has been moved from Room 2 to the learning center. The original room will be used for an equipment demonstration, and the workshop registration is higher than expected. That should be fine. Does the learning center have enough computers for the software exercise? We have twenty-four participants, and everyone needs to complete the online simulation. It has twenty computers. I have arranged four laptops from the support office, and the IT team will deliver them before nine. The workshop itself begins at nine thirty. Great. I will update the calendar invitation and tell the trainer to arrive fifteen minutes early to check the login accounts.
- Transcript translation: Buổi hội thảo dịch vụ khách hàng được chuyển từ Phòng 2 sang trung tâm đào tạo vì Phòng 2 sẽ dùng để trình diễn thiết bị và số người đăng ký vượt dự kiến. Trung tâm đào tạo có 20 máy tính, nhưng có 24 người tham gia. Nora đã mượn thêm bốn máy tính xách tay từ bộ phận hỗ trợ; nhóm IT sẽ chuyển chúng đến trước 9 giờ. Buổi học bắt đầu lúc 9 giờ 30. Ethan sẽ cập nhật lời mời lịch và nhắc giảng viên đến sớm 15 phút để kiểm tra tài khoản đăng nhập.

**Q1. Why was the workshop moved?**

- Choices: **A. The original room will host an equipment demonstration**<br>B. The trainer requested a quieter room<br>C. The learning center is closer to reception<br>D. The workshop was postponed
- Current keyed answer: **A. The original room will host an equipment demonstration**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): used for an equipment demonstration — Phòng 2 được dùng cho buổi trình diễn thiết bị nên hội thảo phải chuyển phòng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: used for an equipment demonstration
- Current explanation: Phòng 2 được dùng cho buổi trình diễn thiết bị nên hội thảo phải chuyển phòng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What has Nora arranged?**

- Choices: **A. Four additional laptops**<br>B. A second trainer<br>C. Twenty new desktop computers<br>D. A later starting time
- Current keyed answer: **A. Four additional laptops**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): four laptops from the support office — Nora đã sắp xếp thêm bốn máy tính xách tay từ bộ phận hỗ trợ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: four laptops from the support office
- Current explanation: Nora đã sắp xếp thêm bốn máy tính xách tay từ bộ phận hỗ trợ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will Ethan do next?**

- Choices: A. Contact the equipment vendor<br>B. Prepare printed certificates<br>**C. Update the calendar invitation**<br>D. Cancel the online simulation
- Current keyed answer: **C. Update the calendar invitation**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): update the calendar invitation — Ethan sẽ cập nhật lời mời lịch để thông báo cho người tham dự.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: update the calendar invitation
- Current explanation: Ethan sẽ cập nhật lời mời lịch để thông báo cho người tham dự.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-parking-policy-update` · An update to the employee parking policy

- Batch: `024` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Beginning next Monday, employees who use the south parking lot must display the new blue permit on the lower-left corner of the windshield. Permits can be collected from the security desk between eight and five. Please bring your employee identification card. Vehicles without a visible permit may be directed to the visitor area. The north lot is not affected by this change.
- Transcript translation: Bắt đầu từ thứ Hai tới, nhân viên sử dụng bãi đỗ xe phía Nam phải đặt thẻ màu xanh mới ở góc dưới bên trái kính chắn gió. Có thể nhận thẻ tại bàn an ninh từ 8 giờ đến 17 giờ. Nhân viên cần mang theo thẻ nhận dạng. Xe không có thẻ hiển thị rõ có thể bị hướng dẫn sang khu vực dành cho khách. Bãi đỗ xe phía Bắc không bị ảnh hưởng bởi thay đổi này.

**Q1. What is being changed?**

- Choices: **A. The employee parking permit procedure**<br>B. The opening hours of the security desk<br>C. The location of the visitor entrance<br>D. The size of the north parking lot
- Current keyed answer: **A. The employee parking permit procedure**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): new blue permit — Thông báo nêu thay đổi quy định thẻ đỗ xe ở bãi phía Nam.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: new blue permit
- Current explanation: Thông báo nêu thay đổi quy định thẻ đỗ xe ở bãi phía Nam.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Where can employees collect the permits?**

- Choices: A. At the visitor entrance<br>**B. From the security desk**<br>C. In the north parking lot<br>D. At the human resources office
- Current keyed answer: **B. From the security desk**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): collected from the security desk — Nhân viên có thể nhận thẻ tại bàn an ninh.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: collected from the security desk
- Current explanation: Nhân viên có thể nhận thẻ tại bàn an ninh.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Which area is unaffected?**

- Choices: A. The south parking lot<br>B. The visitor area<br>**C. The north parking lot**<br>D. The loading zone
- Current keyed answer: **C. The north parking lot**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): north lot is not affected — Thông báo nói rõ bãi phía Bắc không bị ảnh hưởng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: north lot is not affected
- Current explanation: Thông báo nói rõ bãi phía Bắc không bị ảnh hưởng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-customer-survey-results` · Results of a customer survey

- Batch: `024` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: The customer experience team has completed its quarterly service survey. Overall satisfaction increased by six percentage points, mainly because response times improved. However, customers still report difficulty finding the returns form on our website. The digital team will move the form to the support menu by the end of this week. Team leaders should review the detailed results before Monday’s staff meeting. A summary will be sent by email this afternoon.
- Transcript translation: Nhóm trải nghiệm khách hàng đã hoàn thành khảo sát dịch vụ hàng quý. Mức độ hài lòng chung tăng sáu điểm phần trăm, chủ yếu nhờ thời gian phản hồi được cải thiện. Tuy nhiên, khách hàng vẫn gặp khó khăn khi tìm biểu mẫu trả hàng trên trang web. Nhóm kỹ thuật số sẽ chuyển biểu mẫu vào menu hỗ trợ trước cuối tuần này. Trưởng nhóm nên xem kết quả chi tiết trước cuộc họp nhân viên thứ Hai. Bản tóm tắt sẽ được gửi qua email vào chiều nay.

**Q1. What contributed to higher satisfaction?**

- Choices: A. Lower product prices<br>**B. Faster response times**<br>C. A new returns policy<br>D. Longer store hours
- Current keyed answer: **B. Faster response times**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): response times improved — Thời gian phản hồi được cải thiện là nguyên nhân chính giúp mức hài lòng tăng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: response times improved
- Current explanation: Thời gian phản hồi được cải thiện là nguyên nhân chính giúp mức hài lòng tăng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What problem do customers still report?**

- Choices: A. They cannot track deliveries<br>**B. The returns form is difficult to find**<br>C. The website loads too slowly<br>D. The support menu is unavailable
- Current keyed answer: **B. The returns form is difficult to find**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): difficulty finding the returns form — Khách hàng vẫn gặp khó khăn khi tìm biểu mẫu trả hàng trên trang web.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: difficulty finding the returns form
- Current explanation: Khách hàng vẫn gặp khó khăn khi tìm biểu mẫu trả hàng trên trang web.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should team leaders do before Monday?**

- Choices: A. Move the form to the website<br>B. Send a summary to customers<br>**C. Review the detailed results**<br>D. Conduct another survey
- Current keyed answer: **C. Review the detailed results**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): review the detailed results — Trưởng nhóm cần xem kết quả chi tiết trước cuộc họp thứ Hai.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: review the detailed results
- Current explanation: Trưởng nhóm cần xem kết quả chi tiết trước cuộc họp thứ Hai.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `part4-inventory-count-schedule` · A revised inventory count schedule

- Batch: `024` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: The annual inventory count will begin on Tuesday, October seventeenth, one day later than originally planned. The delay will allow the warehouse team to finish labeling the new storage area. Staff assigned to the count should report to the east entrance at seven thirty and collect a scanner from the operations desk. The morning shift will count small equipment, while the afternoon shift will verify boxed supplies. Please complete the online safety refresher before Monday.
- Transcript translation: Đợt kiểm kê hằng năm sẽ bắt đầu vào thứ Ba, ngày 17 tháng 10, muộn hơn kế hoạch ban đầu một ngày. Việc lùi lịch giúp nhóm kho hoàn tất dán nhãn khu vực lưu trữ mới. Nhân viên tham gia kiểm kê cần có mặt tại lối vào phía Đông lúc 7 giờ 30 và nhận máy quét ở bàn vận hành. Ca sáng kiểm đếm thiết bị nhỏ; ca chiều kiểm tra vật tư đóng hộp. Mọi người cần hoàn thành khóa ôn tập an toàn trực tuyến trước thứ Hai.

**Q1. Why was the inventory count delayed?**

- Choices: A. Some scanners have not arrived<br>**B. The new storage area needs labeling**<br>C. The warehouse will be closed<br>D. The safety training was canceled
- Current keyed answer: **B. The new storage area needs labeling**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): finish labeling the new storage area — Nhóm kho cần hoàn tất việc dán nhãn khu lưu trữ mới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: finish labeling the new storage area
- Current explanation: Nhóm kho cần hoàn tất việc dán nhãn khu lưu trữ mới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Where should staff report?**

- Choices: A. The west loading dock<br>B. The main reception<br>**C. The east entrance**<br>D. The operations parking area
- Current keyed answer: **C. The east entrance**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): report to the east entrance — Nhân viên cần có mặt tại lối vào phía Đông.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: report to the east entrance
- Current explanation: Nhân viên cần có mặt tại lối vào phía Đông.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What must employees complete before Monday?**

- Choices: **A. An online safety refresher**<br>B. A stock transfer request<br>C. A scanner maintenance form<br>D. A shift preference survey
- Current keyed answer: **A. An online safety refresher**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): complete the online safety refresher — Nhân viên cần hoàn thành khóa ôn tập an toàn trực tuyến trước thứ Hai.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: complete the online safety refresher
- Current explanation: Nhân viên cần hoàn thành khóa ôn tập an toàn trực tuyến trước thứ Hai.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch025-part2-client-appointment` · A revised client appointment

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Could we move the client appointment to Thursday afternoon?
- Transcript translation: Người nói hỏi liệu có thể chuyển cuộc hẹn với khách hàng sang chiều thứ Năm hay không.

**Q1. Choose the most appropriate response.**

- Choices: A. On Wednesday morning<br>**B. On Thursday afternoon**<br>C. After the monthly review
- Current keyed answer: **B. On Thursday afternoon**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Thursday afternoon — Người nói đề nghị chuyển cuộc hẹn với khách hàng sang chiều thứ Năm. Cụm When would the revised appointment take place? hỏi thời điểm của lịch hẹn mới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Thursday afternoon
- Current explanation: Người nói đề nghị chuyển cuộc hẹn với khách hàng sang chiều thứ Năm. Cụm When would the revised appointment take place? hỏi thời điểm của lịch hẹn mới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch025-part2-equipment-status` · A question about equipment delivery

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Has the replacement printer arrived at the branch yet?
- Transcript translation: Người nói muốn biết máy in thay thế đã được giao đến chi nhánh hay chưa.

**Q1. Choose the most appropriate response.**

- Choices: **A. Whether the replacement printer has arrived**<br>B. Who approved the purchase<br>C. Why the meeting was canceled
- Current keyed answer: **A. Whether the replacement printer has arrived**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Has the replacement printer arrived — Người nói muốn xác nhận máy in thay thế đã được giao đến chi nhánh hay chưa. Câu hỏi Has ... arrived yet? yêu cầu thông tin về tình trạng giao hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Has the replacement printer arrived
- Current explanation: Người nói muốn xác nhận máy in thay thế đã được giao đến chi nhánh hay chưa. Câu hỏi Has ... arrived yet? yêu cầu thông tin về tình trạng giao hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch025-part3-training-room-change` · A change to the training room

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Did you see the message about tomorrow’s customer-service training? The room has changed. I thought it was in Conference Room B. Is that room unavailable? Yes. The projector is being repaired, so the session will be held in Room D on the fourth floor. I’ll update the calendar invitation and let the new employees know. Should they still arrive at nine? Yes, the starting time is unchanged. Please remind them to bring their access cards. All right. I’ll send a short notice before the end of the day.
- Transcript translation: Buổi đào tạo dịch vụ khách hàng được chuyển từ phòng B sang phòng D vì máy chiếu đang được sửa. Daniel sẽ cập nhật lịch và thông báo cho nhân viên mới. Thời gian bắt đầu vẫn là 9 giờ và mọi người cần mang thẻ ra vào.

**Q1. Why was the training room changed?**

- Choices: A. The room is being renovated<br>**B. The projector is being repaired**<br>C. The instructor is unavailable<br>D. More employees registered
- Current keyed answer: **B. The projector is being repaired**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The projector is being repaired — Máy chiếu đang được sửa chữa nên buổi học chuyển sang phòng D.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The projector is being repaired
- Current explanation: Máy chiếu đang được sửa chữa nên buổi học chuyển sang phòng D.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What will Daniel do?**

- Choices: A. Prepare the training materials<br>B. Contact the building manager<br>**C. Update the invitation and notify employees**<br>D. Change the starting time
- Current keyed answer: **C. Update the invitation and notify employees**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): update the calendar invitation and let the new employees know — Daniel sẽ cập nhật lời mời lịch và thông báo cho nhân viên mới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: update the calendar invitation and let the new employees know
- Current explanation: Daniel sẽ cập nhật lời mời lịch và thông báo cho nhân viên mới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should employees bring?**

- Choices: **A. Their access cards**<br>B. A printed report<br>C. A laptop charger<br>D. A parking receipt
- Current keyed answer: **A. Their access cards**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): bring their access cards — Thông tin trong đoạn nghe cho biết: Mia nhắc nhân viên mang thẻ ra vào.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: bring their access cards
- Current explanation: Thông tin trong đoạn nghe cho biết: Mia nhắc nhân viên mang thẻ ra vào.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch025-part3-invoice-clarification` · Clarifying a supplier invoice

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: I reviewed the invoice from Northstar Supplies. The total is higher than the purchase order. That may be because they included the express delivery charge. The order was supposed to use standard shipping. I checked the delivery note, and it says standard shipping. I’ll ask the supplier to issue a corrected invoice. Please copy me on the email. We should hold the payment until the revised document arrives. I can do that. Their account representative usually responds within one business day. Good. Once we receive the correction, I’ll approve the payment in the system.
- Transcript translation: Nora phát hiện hóa đơn của nhà cung cấp cao hơn đơn đặt hàng do có thể tính nhầm phí giao nhanh. Cô sẽ yêu cầu hóa đơn điều chỉnh. Ethan sẽ tạm giữ thanh toán cho đến khi nhận được chứng từ đúng.

**Q1. What problem does Nora mention?**

- Choices: **A. The invoice exceeds the purchase order**<br>B. The goods were delivered late<br>C. The supplier changed its bank<br>D. The purchase order is missing
- Current keyed answer: **A. The invoice exceeds the purchase order**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The total is higher than the purchase order — Thông tin trong đoạn nghe cho biết: Tổng hóa đơn cao hơn đơn đặt hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The total is higher than the purchase order
- Current explanation: Thông tin trong đoạn nghe cho biết: Tổng hóa đơn cao hơn đơn đặt hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What will Nora do next?**

- Choices: A. Cancel the order<br>**B. Request a corrected invoice**<br>C. Arrange express shipping<br>D. Contact the bank
- Current keyed answer: **B. Request a corrected invoice**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): ask the supplier to issue a corrected invoice — Thông tin trong đoạn nghe cho biết: Nora sẽ yêu cầu nhà cung cấp phát hành hóa đơn đã chỉnh sửa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: ask the supplier to issue a corrected invoice
- Current explanation: Thông tin trong đoạn nghe cho biết: Nora sẽ yêu cầu nhà cung cấp phát hành hóa đơn đã chỉnh sửa.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When will Ethan approve payment?**

- Choices: A. Before the goods arrive<br>B. After the supplier changes its account<br>**C. Once the corrected invoice arrives**<br>D. At the end of the quarter
- Current keyed answer: **C. Once the corrected invoice arrives**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): Once we receive the correction — Ethan chỉ phê duyệt thanh toán sau khi nhận hóa đơn đã sửa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Once we receive the correction
- Current explanation: Ethan chỉ phê duyệt thanh toán sau khi nhận hóa đơn đã sửa.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch025-part3-access-card-renewal` · Renewing office access cards

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: The security team is replacing access cards next week. Have you submitted the employee list? Not yet. I’m waiting for the department heads to confirm which temporary staff are staying. The list must be finalized by Wednesday so the cards can be printed before Friday. I’ll send a reminder this afternoon. Can employees collect the new cards at reception? Yes, but they must return their old cards when they sign for the replacements. Understood. I’ll include that instruction in the announcement.
- Transcript translation: Nhóm an ninh sẽ thay thẻ ra vào. Mark đang chờ xác nhận danh sách nhân viên thời vụ và sẽ gửi lời nhắc. Nhân viên nhận thẻ mới tại lễ tân và phải trả lại thẻ cũ.

**Q1. What is Mark waiting for?**

- Choices: A. A security inspection<br>**B. Confirmation about temporary staff**<br>C. A new printer<br>D. A budget approval
- Current keyed answer: **B. Confirmation about temporary staff**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): confirm which temporary staff are staying — Thông tin trong đoạn nghe cho biết: Mark đang chờ trưởng bộ phận xác nhận nhân sự thời vụ nào tiếp tục làm việc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: confirm which temporary staff are staying
- Current explanation: Thông tin trong đoạn nghe cho biết: Mark đang chờ trưởng bộ phận xác nhận nhân sự thời vụ nào tiếp tục làm việc.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. By when must the list be finalized?**

- Choices: A. Monday<br>B. Tuesday<br>**C. Wednesday**<br>D. Friday
- Current keyed answer: **C. Wednesday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): finalized by Wednesday — Danh sách phải hoàn tất trước thứ Tư.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: finalized by Wednesday
- Current explanation: Danh sách phải hoàn tất trước thứ Tư.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What must employees do when collecting new cards?**

- Choices: A. Pay a replacement fee<br>B. Visit the security office<br>**C. Return their old cards**<br>D. Bring a passport photo
- Current keyed answer: **C. Return their old cards**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): return their old cards — Nhân viên phải trả thẻ cũ khi ký nhận thẻ mới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: return their old cards
- Current explanation: Nhân viên phải trả thẻ cũ khi ký nhận thẻ mới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch025-part4-delivery-route-update` · An update to delivery routes

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Good morning, drivers. Due to road maintenance near the central market, all deliveries to the eastern district will use Riverside Avenue today. Please check the revised route sheet before leaving the depot. The first departure is still scheduled for eight thirty. If a customer is unavailable, record the attempt in the handheld device and contact dispatch before returning the parcel. Updated maps are available beside the vehicle keys.
- Transcript translation: Do bảo trì đường gần chợ trung tâm, tài xế giao hàng đến quận phía Đông phải đi theo đại lộ Riverside. Họ cần xem tuyến đường mới và ghi nhận lần giao không thành công trên thiết bị.

**Q1. Why are routes being changed?**

- Choices: A. A bridge has reopened<br>**B. Road maintenance is taking place**<br>C. The depot is moving<br>D. A customer requested a delay
- Current keyed answer: **B. Road maintenance is taking place**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Due to road maintenance — Tuyến đường thay đổi do công tác bảo trì đường gần chợ trung tâm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Due to road maintenance
- Current explanation: Tuyến đường thay đổi do công tác bảo trì đường gần chợ trung tâm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should drivers do before leaving?**

- Choices: A. Collect a cash receipt<br>B. Call every customer<br>**C. Check the revised route sheet**<br>D. Refuel at the eastern station
- Current keyed answer: **C. Check the revised route sheet**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): check the revised route sheet — Tài xế cần xem bảng tuyến đường đã sửa trước khi rời kho.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: check the revised route sheet
- Current explanation: Tài xế cần xem bảng tuyến đường đã sửa trước khi rời kho.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should a driver do if a customer is unavailable?**

- Choices: A. Leave the parcel outside<br>**B. Record the attempt and contact dispatch**<br>C. Return immediately without a note<br>D. Ask another driver to deliver it
- Current keyed answer: **B. Record the attempt and contact dispatch**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): record the attempt in the handheld device and contact dispatch — Tài xế cần ghi nhận lần giao và liên hệ điều phối.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: record the attempt in the handheld device and contact dispatch
- Current explanation: Tài xế cần ghi nhận lần giao và liên hệ điều phối.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch025-part4-benefits-enrollment` · Quarterly benefits enrollment reminder

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: This is a reminder that the quarterly benefits enrollment period closes on the twenty-eighth. Employees who want to change their medical or transportation options should submit the online form by five p.m. on that date. Existing selections will remain in place if no changes are submitted. A benefits specialist will be available in Meeting Room 3 on Tuesday and Thursday to answer individual questions. Please bring your employee identification number to the consultation.
- Transcript translation: Đợt đăng ký quyền lợi theo quý kết thúc ngày 28 lúc 5 giờ chiều. Nếu không thay đổi, lựa chọn hiện tại được giữ nguyên. Chuyên viên nhân sự tư vấn vào thứ Ba và thứ Năm.

**Q1. When does enrollment close?**

- Choices: A. On the twenty-first<br>**B. On the twenty-eighth**<br>C. At the end of the quarter<br>D. Next Thursday
- Current keyed answer: **B. On the twenty-eighth**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): closes on the twenty-eighth — Thông tin trong đoạn nghe cho biết: Thời hạn kết thúc vào ngày 28.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: closes on the twenty-eighth
- Current explanation: Thông tin trong đoạn nghe cho biết: Thời hạn kết thúc vào ngày 28.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What happens if an employee submits no changes?**

- Choices: A. All benefits are canceled<br>B. The employee must attend a meeting<br>**C. Current selections remain**<br>D. The form is automatically rejected
- Current keyed answer: **C. Current selections remain**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Existing selections will remain in place — Lựa chọn hiện tại được giữ nguyên nếu không gửi thay đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Existing selections will remain in place
- Current explanation: Lựa chọn hiện tại được giữ nguyên nếu không gửi thay đổi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should employees bring to a consultation?**

- Choices: A. A medical receipt<br>B. A passport<br>**C. Their employee identification number**<br>D. A completed paper survey
- Current keyed answer: **C. Their employee identification number**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): employee identification number — Nhân viên cần mang mã số nhân viên.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: employee identification number
- Current explanation: Nhân viên cần mang mã số nhân viên.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch025-part4-display-maintenance` · Maintenance notice for a product display area

- Batch: `025` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Attention, store associates. The product display area on the second floor will be closed from six to eight tomorrow morning while the lighting system is upgraded. Please move promotional materials to the storage room before closing today. The maintenance team will reopen the area after completing a safety inspection. Customers may still access the other departments through the north escalator. Thank you for helping us keep the store organized.
- Transcript translation: Khu trưng bày tầng hai đóng cửa từ 6 đến 8 giờ sáng để nâng cấp chiếu sáng. Nhân viên chuyển vật liệu quảng bá vào kho trước khi kết thúc ngày làm việc. Khu vực mở lại sau kiểm tra an toàn.

**Q1. What will happen tomorrow morning?**

- Choices: A. The store will open late<br>**B. The lighting system will be upgraded**<br>C. A new department will open<br>D. The escalator will be replaced
- Current keyed answer: **B. The lighting system will be upgraded**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): lighting system is upgraded — Khu trưng bày sẽ đóng để nâng cấp hệ thống chiếu sáng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: lighting system is upgraded
- Current explanation: Khu trưng bày sẽ đóng để nâng cấp hệ thống chiếu sáng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should associates do before closing today?**

- Choices: **A. Move promotional materials**<br>B. Clean the north escalator<br>C. Count all products<br>D. Print new price labels
- Current keyed answer: **A. Move promotional materials**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): move promotional materials to the storage room — Nhân viên cần chuyển tài liệu quảng bá vào kho.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: move promotional materials to the storage room
- Current explanation: Nhân viên cần chuyển tài liệu quảng bá vào kho.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When will the display area reopen?**

- Choices: A. At six tomorrow<br>**B. After a safety inspection**<br>C. When the store closes<br>D. Next Monday
- Current keyed answer: **B. After a safety inspection**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): after completing a safety inspection — Khu vực mở lại sau khi đội bảo trì hoàn tất kiểm tra an toàn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: after completing a safety inspection
- Current explanation: Khu vực mở lại sau khi đội bảo trì hoàn tất kiểm tra an toàn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch026-part3-vendor-call` · A call about a delayed component order

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Hi Daniel, the replacement components were supposed to arrive this morning. Do you have an update from the supplier? They called ten minutes ago. The truck was held at the distribution center, so delivery is now expected around three this afternoon. That is still before our technicians leave. Please tell receiving to inspect the boxes immediately and send me the count. I will. If anything is missing, I will contact the supplier before the warehouse closes.

**Q1. When are the components expected to arrive?**

- Choices: **A. At about three**<br>B. At noon<br>C. Tomorrow morning<br>D. After the warehouse closes
- Current keyed answer: **A. At about three**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): delivery is now expected around three this afternoon — Daniel cho biết hàng dự kiến đến khoảng 3 giờ chiều.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: delivery is now expected around three this afternoon
- Current explanation: Daniel cho biết hàng dự kiến đến khoảng 3 giờ chiều.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What does Maya ask receiving to do?**

- Choices: A. Store the boxes overnight<br>**B. Inspect the boxes immediately**<br>C. Return the order<br>D. Call the technicians
- Current keyed answer: **B. Inspect the boxes immediately**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): inspect the boxes immediately — Maya cần yêu cầu bộ phận nhận hàng kiểm tra các thùng ngay lập tức.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: inspect the boxes immediately
- Current explanation: Maya cần yêu cầu bộ phận nhận hàng kiểm tra các thùng ngay lập tức.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will Daniel do if items are missing?**

- Choices: A. Ask Maya to drive there<br>B. Cancel the order<br>**C. Contact the supplier**<br>D. Reschedule the technicians
- Current keyed answer: **C. Contact the supplier**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): contact the supplier before the warehouse closes — Daniel sẽ liên hệ nhà cung cấp trước khi kho đóng cửa nếu thiếu hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: contact the supplier before the warehouse closes
- Current explanation: Daniel sẽ liên hệ nhà cung cấp trước khi kho đóng cửa nếu thiếu hàng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch026-part3-training-room` · Changing the training room

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Did you see the email about tomorrow’s software training? The room has changed. Yes, but I thought it was still in Conference Room A. Where are we meeting now? It will be in the computer lab on the fourth floor. The instructor needs a workstation for every participant. I will update the calendar and send a message to the team. Should we arrive early? Please be there fifteen minutes before nine so we can sign in.

**Q1. What is the purpose of the conversation?**

- Choices: A. To cancel a course<br>B. To order computers<br>C. To hire an instructor<br>**D. To confirm a room change**
- Current keyed answer: **D. To confirm a room change**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The room has changed — Cuộc trao đổi nêu rằng địa điểm đào tạo ngày mai đã thay đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The room has changed
- Current explanation: Cuộc trao đổi nêu rằng địa điểm đào tạo ngày mai đã thay đổi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Where will the training take place?**

- Choices: **A. The computer lab**<br>B. The lobby<br>C. Conference Room A<br>D. The cafeteria
- Current keyed answer: **A. The computer lab**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): computer lab on the fourth floor — Thông tin cho biết buổi học diễn ra tại phòng máy tầng bốn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: computer lab on the fourth floor
- Current explanation: Thông tin cho biết buổi học diễn ra tại phòng máy tầng bốn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What time should participants arrive?**

- Choices: A. 9:00<br>**B. 8:45**<br>C. 9:15<br>D. 10:00
- Current keyed answer: **B. 8:45**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): fifteen minutes before nine — Người tham dự cần đến trước 9 giờ 15 phút.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: fifteen minutes before nine
- Current explanation: Người tham dự cần đến trước 9 giờ 15 phút.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch026-part3-invoice-correction` · Correcting an invoice

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: I noticed that the invoice from Bright Office lists twenty chairs, but we ordered twelve. You are right. The purchase order shows twelve chairs. I will ask the vendor to issue a corrected invoice. Please copy me on the email. Finance cannot schedule payment until the quantities match. I will send it this morning and request the revised document by Friday.

**Q1. What discrepancy did Noah notice?**

- Choices: A. The delivery date<br>B. The unit price<br>**C. The chair quantity**<br>D. The vendor name
- Current keyed answer: **C. The chair quantity**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): lists twenty chairs, but we ordered twelve — Hóa đơn cho biết có 20 ghế, trong khi đơn chỉ đặt 12.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: lists twenty chairs, but we ordered twelve
- Current explanation: Hóa đơn cho biết có 20 ghế, trong khi đơn chỉ đặt 12.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What will Lena request?**

- Choices: A. A refund check<br>B. A new purchase order<br>C. A delivery appointment<br>**D. A corrected invoice**
- Current keyed answer: **D. A corrected invoice**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): issue a corrected invoice — Lena cần yêu cầu nhà cung cấp phát hành hóa đơn điều chỉnh.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: issue a corrected invoice
- Current explanation: Lena cần yêu cầu nhà cung cấp phát hành hóa đơn điều chỉnh.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why can Finance not schedule payment yet?**

- Choices: **A. The quantities do not match**<br>B. The vendor is closed<br>C. The order was canceled<br>D. The email is missing
- Current keyed answer: **A. The quantities do not match**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): quantities match — Finance không thể lên lịch thanh toán do số lượng chưa khớp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: quantities match
- Current explanation: Finance không thể lên lịch thanh toán do số lượng chưa khớp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch026-part3-access-card` · Renewing an access card

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: My access card expires at the end of this week. Do I need to visit security to renew it? You can submit the renewal form online. Security will send a confirmation once your manager approves it. How long does approval usually take? I have a client meeting early Monday. Usually one business day. If you submit it before noon today, it should be ready tomorrow afternoon.

**Q1. How can Erin renew her access card?**

- Choices: A. By calling the client<br>**B. By submitting an online form**<br>C. By visiting the warehouse<br>D. By purchasing a new card
- Current keyed answer: **B. By submitting an online form**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): submit the renewal form online — Erin có thể nộp biểu mẫu gia hạn trực tuyến.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: submit the renewal form online
- Current explanation: Erin có thể nộp biểu mẫu gia hạn trực tuyến.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Who must approve the renewal?**

- Choices: A. The receptionist<br>B. The client<br>**C. Her manager**<br>D. The vendor
- Current keyed answer: **C. Her manager**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): once your manager approves it — Quản lý của Erin phải phê duyệt yêu cầu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: once your manager approves it
- Current explanation: Quản lý của Erin phải phê duyệt yêu cầu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When should the card be ready if she submits before noon?**

- Choices: A. This evening<br>B. Monday morning<br>C. Next week<br>**D. Tomorrow afternoon**
- Current keyed answer: **D. Tomorrow afternoon**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): ready tomorrow afternoon — Nộp trước buổi trưa thì thẻ dự kiến sẵn sàng chiều mai.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: ready tomorrow afternoon
- Current explanation: Nộp trước buổi trưa thì thẻ dự kiến sẵn sàng chiều mai.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch026-part4-building-notice` · Building maintenance announcement

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Good afternoon. Water service on floors six through eight will be temporarily unavailable tomorrow from 9 a.m. to 11 a.m. while plumbing work is completed. Please use the restrooms on floors three or five during this period. The maintenance team will post an update if the work finishes early. We apologize for the inconvenience and appreciate your cooperation.

**Q1. Which floors will have no water service?**

- Choices: **A. Six through eight**<br>B. Three through five<br>C. All floors<br>D. The lobby only
- Current keyed answer: **A. Six through eight**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Water service on floors six through eight — Thông báo cho biết các tầng sáu đến tám sẽ bị gián đoạn nước.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Water service on floors six through eight
- Current explanation: Thông báo cho biết các tầng sáu đến tám sẽ bị gián đoạn nước.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When will the work take place?**

- Choices: A. Today at noon<br>**B. Tomorrow from 9 to 11**<br>C. Tomorrow after 5<br>D. Next week
- Current keyed answer: **B. Tomorrow from 9 to 11**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): tomorrow from 9 a.m. to 11 a.m. — Công việc được thực hiện từ 9 đến 11 giờ sáng ngày mai.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: tomorrow from 9 a.m. to 11 a.m.
- Current explanation: Công việc được thực hiện từ 9 đến 11 giờ sáng ngày mai.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Where should people go during the interruption?**

- Choices: A. The rooftop<br>B. The parking garage<br>**C. Floors three or five**<br>D. The maintenance office
- Current keyed answer: **C. Floors three or five**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): use the restrooms on floors three or five — Người dùng được hướng dẫn đến nhà vệ sinh tầng ba hoặc năm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: use the restrooms on floors three or five
- Current explanation: Người dùng được hướng dẫn đến nhà vệ sinh tầng ba hoặc năm.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch026-part4-travel-update` · Updated travel itinerary

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Travelers attending the regional sales meeting should note a change to the return schedule. The shuttle will leave the hotel at 4:20 p.m., rather than 4:45, because the airport road is expected to be busy. Please check out before lunch and leave your luggage with the front desk. The driver will collect everyone at the main entrance.

**Q1. What schedule has changed?**

- Choices: A. The arrival flight<br>B. The hotel check-in<br>C. The meeting agenda<br>**D. The return shuttle**
- Current keyed answer: **D. The return shuttle**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): change to the return schedule — Thông báo cho biết lịch xe đưa khách về đã thay đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: change to the return schedule
- Current explanation: Thông báo cho biết lịch xe đưa khách về đã thay đổi.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What time will the shuttle depart?**

- Choices: **A. 4:20 p.m.**<br>B. 4:45 p.m.<br>C. 5:20 p.m.<br>D. 5:45 p.m.
- Current keyed answer: **A. 4:20 p.m.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): shuttle will leave the hotel at 4:20 p.m. — Xe được lên lịch rời khách sạn lúc 4 giờ 20 chiều.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: shuttle will leave the hotel at 4:20 p.m.
- Current explanation: Xe được lên lịch rời khách sạn lúc 4 giờ 20 chiều.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Where should travelers leave their luggage?**

- Choices: A. On the shuttle<br>**B. At the front desk**<br>C. In the meeting room<br>D. At the airport
- Current keyed answer: **B. At the front desk**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): leave your luggage with the front desk — Hành khách cần gửi hành lý tại quầy lễ tân.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: leave your luggage with the front desk
- Current explanation: Hành khách cần gửi hành lý tại quầy lễ tân.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch026-part4-product-launch` · Product launch briefing

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: The marketing team will launch the updated scheduling app on Tuesday. The demonstration has been moved to the second-floor auditorium to accommodate additional guests. Representatives should collect their presentation badges from reception by 8:30 a.m. Printed brochures will be available at the entrance, but the product guide is now distributed digitally. Please test your demonstration account before arriving.

**Q1. When will the app be launched?**

- Choices: A. Monday<br>B. Wednesday<br>**C. Tuesday**<br>D. Friday
- Current keyed answer: **C. Tuesday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): launch the updated scheduling app on Tuesday — Thông báo nêu ứng dụng lịch mới được ra mắt vào thứ Ba.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: launch the updated scheduling app on Tuesday
- Current explanation: Thông báo nêu ứng dụng lịch mới được ra mắt vào thứ Ba.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why was the demonstration moved?**

- Choices: A. The projector failed<br>B. The app is delayed<br>C. The auditorium is closed<br>**D. More guests are expected**
- Current keyed answer: **D. More guests are expected**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): to accommodate additional guests — Buổi giới thiệu được chuyển địa điểm để tiếp nhận thêm khách.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: to accommodate additional guests
- Current explanation: Buổi giới thiệu được chuyển địa điểm để tiếp nhận thêm khách.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should representatives collect by 8:30?**

- Choices: **A. Presentation badges**<br>B. Printed invoices<br>C. Product samples<br>D. Parking permits
- Current keyed answer: **A. Presentation badges**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): collect their presentation badges from reception by 8:30 a.m. — Đại diện cần nhận thẻ trình bày tại lễ tân trước 8 giờ 30.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: collect their presentation badges from reception by 8:30 a.m.
- Current explanation: Đại diện cần nhận thẻ trình bày tại lễ tân trước 8 giờ 30.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch026-part4-policy-reminder` · Expense policy reminder

- Batch: `026` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: A reminder to all employees who travel for business: expense claims must be submitted within ten working days after the trip. Receipts for meals and transportation should be attached to the online form. If a receipt is unavailable, include a brief explanation in the notes section. Claims submitted after the deadline may be returned for correction.

**Q1. How long do employees have to submit expense claims?**

- Choices: A. Five working days<br>**B. Ten working days**<br>C. Two weeks<br>D. One month
- Current keyed answer: **B. Ten working days**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): within ten working days after the trip — Nhân viên được yêu cầu gửi yêu cầu chi phí trong mười ngày làm việc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: within ten working days after the trip
- Current explanation: Nhân viên được yêu cầu gửi yêu cầu chi phí trong mười ngày làm việc.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should be attached to the online form?**

- Choices: A. Meeting notes<br>B. A passport copy<br>**C. Meal and transportation receipts**<br>D. A manager biography
- Current keyed answer: **C. Meal and transportation receipts**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Receipts for meals and transportation should be attached — Cần đính kèm hóa đơn ăn uống và phương tiện đi lại.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Receipts for meals and transportation should be attached
- Current explanation: Cần đính kèm hóa đơn ăn uống và phương tiện đi lại.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should employees do if a receipt is missing?**

- Choices: A. Cancel the claim<br>B. Ask the hotel for a refund<br>C. Submit the form blank<br>**D. Include an explanation in the notes**
- Current keyed answer: **D. Include an explanation in the notes**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): include a brief explanation in the notes section — Nếu thiếu hóa đơn, cần ghi lời giải thích trong phần ghi chú.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: include a brief explanation in the notes section
- Current explanation: Nếu thiếu hóa đơn, cần ghi lời giải thích trong phần ghi chú.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-room-booking` · A room booking

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Could you reserve the smaller conference room for Thursday?
- Transcript translation: Bạn có thể đặt phòng họp nhỏ cho thứ Năm không?

**Q1. Choose the most appropriate response.**

- Choices: **A. Sure, I’ll check its availability.**<br>B. The report is about last quarter.<br>C. It was delivered by courier.
- Current keyed answer: **A. Sure, I’ll check its availability.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Could you reserve the smaller conference room for Thursday? — Người nói yêu cầu đặt phòng họp. Lựa chọn A đáp lại đúng bằng việc kiểm tra tình trạng phòng; B và C không xử lý yêu cầu đặt phòng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Could you reserve the smaller conference room for Thursday?
- Current explanation: Người nói yêu cầu đặt phòng họp. Lựa chọn A đáp lại đúng bằng việc kiểm tra tình trạng phòng; B và C không xử lý yêu cầu đặt phòng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-invoice-copy` · An invoice copy

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Who should I send the revised invoice to?
- Transcript translation: Tôi nên gửi hóa đơn đã chỉnh sửa cho ai?

**Q1. Choose the most appropriate response.**

- Choices: A. It was revised yesterday.<br>**B. Please send it to Ms. Nguyen in accounting.**<br>C. The printer is out of paper.
- Current keyed answer: **B. Please send it to Ms. Nguyen in accounting.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Who should I send the revised invoice to? — Câu hỏi Who hỏi người nhận. Lựa chọn B xác định người nhận và bộ phận; A nói thời gian, C nói thiết bị.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Who should I send the revised invoice to?
- Current explanation: Câu hỏi Who hỏi người nhận. Lựa chọn B xác định người nhận và bộ phận; A nói thời gian, C nói thiết bị.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-training-start` · Training schedule

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: What time does the safety training begin?
- Transcript translation: Buổi đào tạo an toàn bắt đầu lúc mấy giờ?

**Q1. Choose the most appropriate response.**

- Choices: A. In the training room upstairs.<br>**B. It begins at nine thirty.**<br>C. She has completed the online form.
- Current keyed answer: **B. It begins at nine thirty.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): What time does the safety training begin? — What time yêu cầu giờ bắt đầu; B trả lời 9:30. A là địa điểm, C không liên quan.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: What time does the safety training begin?
- Current explanation: What time yêu cầu giờ bắt đầu; B trả lời 9:30. A là địa điểm, C không liên quan.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-parking-access` · Parking access

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Where can visitors park during the renovation?
- Transcript translation: Khách có thể đỗ xe ở đâu trong thời gian cải tạo?

**Q1. Choose the most appropriate response.**

- Choices: **A. The visitor lot behind Building C.**<br>B. It should be finished next week.<br>C. They renovated the lobby.
- Current keyed answer: **A. The visitor lot behind Building C.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Where can visitors park during the renovation? — Where yêu cầu địa điểm. A chỉ rõ bãi đỗ xe; B trả lời thời gian và C nói về công việc cải tạo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Where can visitors park during the renovation?
- Current explanation: Where yêu cầu địa điểm. A chỉ rõ bãi đỗ xe; B trả lời thời gian và C nói về công việc cải tạo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-catering-count` · Catering estimate

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Have we confirmed how many meals the caterer needs?
- Transcript translation: Chúng ta đã xác nhận số suất ăn bên cung cấp cần chưa?

**Q1. Choose the most appropriate response.**

- Choices: A. The catering company is new.<br>**B. Yes, I emailed them the updated count this morning.**<br>C. We will meet after lunch.
- Current keyed answer: **B. Yes, I emailed them the updated count this morning.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): Have we confirmed how many meals the caterer needs? — Câu hỏi Have we confirmed…? hỏi xác nhận hành động; B nêu đã gửi số lượng cập nhật.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Have we confirmed how many meals the caterer needs?
- Current explanation: Câu hỏi Have we confirmed…? hỏi xác nhận hành động; B nêu đã gửi số lượng cập nhật.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-maintenance` · Maintenance request

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Why is the elevator out of service?
- Transcript translation: Tại sao thang máy không hoạt động?

**Q1. Choose the most appropriate response.**

- Choices: **A. A technician is replacing a control panel.**<br>B. Take the elevator to the fifth floor.<br>C. The service desk closes at six.
- Current keyed answer: **A. A technician is replacing a control panel.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Why is the elevator out of service? — Why hỏi nguyên nhân; A nêu kỹ thuật viên đang thay bảng điều khiển.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Why is the elevator out of service?
- Current explanation: Why hỏi nguyên nhân; A nêu kỹ thuật viên đang thay bảng điều khiển.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-project-update` · Project update

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: Would you like me to include the cost estimates in the presentation?
- Transcript translation: Bạn có muốn tôi đưa các ước tính chi phí vào bài thuyết trình không?

**Q1. Choose the most appropriate response.**

- Choices: A. The presentation is in Room 12.<br>**B. Yes, that would make the proposal more complete.**<br>C. We estimated three hours.
- Current keyed answer: **B. Yes, that would make the proposal more complete.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Would you like me to include the cost estimates in the presentation? — Would you like me to… là lời đề nghị; B chấp nhận và nêu lợi ích. A là địa điểm, C nói thời lượng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Would you like me to include the cost estimates in the presentation?
- Current explanation: Would you like me to… là lời đề nghị; B chấp nhận và nêu lợi ích. A là địa điểm, C nói thời lượng.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 2 · `batch027-part2-delivery-window` · Delivery window

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Transcript: The replacement parts should arrive before noon, shouldn’t they?
- Transcript translation: Các linh kiện thay thế sẽ đến trước buổi trưa, đúng không?

**Q1. Choose the most appropriate response.**

- Choices: A. The parts are made of steel.<br>**B. No, the shipment was rescheduled for two o’clock.**<br>C. I replaced the window last year.
- Current keyed answer: **B. No, the shipment was rescheduled for two o’clock.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 2 speech act, polarity, indirect response naturalness, and distractor uniqueness
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The replacement parts should arrive before noon, shouldn’t they? — Câu hỏi đuôi yêu cầu xác nhận thời gian; B điều chỉnh thông tin bằng thời điểm giao mới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The replacement parts should arrive before noon, shouldn’t they?
- Current explanation: Câu hỏi đuôi yêu cầu xác nhận thời gian; B điều chỉnh thông tin bằng thời điểm giao mới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch027-part3-equipment-return` · Returning office equipment

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Hi, I’m returning the projector I borrowed for yesterday’s workshop. Thanks. Did you notice any problems with it? The image was a little blurry, even after I adjusted the focus. I’ll tag it for inspection before the next reservation.
- Transcript translation: Người phụ nữ trả máy chiếu sau workshop và báo hình ảnh hơi mờ. Nhân viên sẽ đưa thiết bị đi kiểm tra.

**Q1. Why is the woman returning the projector?**

- Choices: A. The workshop was canceled.<br>**B. She has finished using it.**<br>C. It was purchased for her department.<br>D. It needs a new cable.
- Current keyed answer: **B. She has finished using it.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Hi, I’m returning the projector I borrowed for yesterday’s workshop. — Cô ấy trả máy chiếu sau khi mượn cho buổi workshop hôm qua; buổi đó đã kết thúc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Hi, I’m returning the projector I borrowed for yesterday’s workshop.
- Current explanation: Cô ấy trả máy chiếu sau khi mượn cho buổi workshop hôm qua; buổi đó đã kết thúc.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What problem did she report?**

- Choices: **A. The image was blurry.**<br>B. The sound was too loud.<br>C. The lamp would not turn on.<br>D. The screen was missing.
- Current keyed answer: **A. The image was blurry.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The image was a little blurry, even after I adjusted the focus. — Cô ấy nói hình ảnh hơi mờ ngay cả sau khi điều chỉnh tiêu cự.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The image was a little blurry, even after I adjusted the focus.
- Current explanation: Cô ấy nói hình ảnh hơi mờ ngay cả sau khi điều chỉnh tiêu cự.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will the man do next?**

- Choices: A. Cancel the next workshop.<br>B. Order a replacement projector.<br>**C. Send the device for inspection.**<br>D. Change the reservation time.
- Current keyed answer: **C. Send the device for inspection.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I’ll tag it for inspection before the next reservation. — Anh ấy sẽ đánh dấu thiết bị để kiểm tra trước lượt đặt tiếp theo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I’ll tag it for inspection before the next reservation.
- Current explanation: Anh ấy sẽ đánh dấu thiết bị để kiểm tra trước lượt đặt tiếp theo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch027-part3-benefits-enrollment` · Benefits enrollment

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: I still haven’t submitted my benefits selection. Is the deadline this Friday? Yes, but you can complete it online. The portal closes at five p.m. Can I change my selection after submitting it? You can make changes until the enrollment period ends. After that, contact HR if you have a qualifying event.
- Transcript translation: Hai đồng nghiệp trao đổi về đăng ký quyền lợi, thời hạn trên cổng trực tuyến và quy định thay đổi lựa chọn.

**Q1. What is the man concerned about?**

- Choices: A. A payroll error<br>**B. A benefits enrollment deadline**<br>C. A vacation request<br>D. A training certificate
- Current keyed answer: **B. A benefits enrollment deadline**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I still haven’t submitted my benefits selection. Is the deadline this Friday? — Câu hỏi là về thời hạn đăng ký quyền lợi; người đàn ông hỏi khi nào phải hoàn tất lựa chọn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I still haven’t submitted my benefits selection. Is the deadline this Friday?
- Current explanation: Câu hỏi là về thời hạn đăng ký quyền lợi; người đàn ông hỏi khi nào phải hoàn tất lựa chọn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. How can employees submit their selections?**

- Choices: A. By calling the manager<br>B. At the reception desk<br>**C. Through an online portal**<br>D. By mailing a printed form
- Current keyed answer: **C. Through an online portal**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Yes, but you can complete it online. The portal closes at five p.m. — Người phụ nữ cho biết có thể hoàn tất trực tuyến trên portal.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Yes, but you can complete it online. The portal closes at five p.m.
- Current explanation: Người phụ nữ cho biết có thể hoàn tất trực tuyến trên portal.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When can the man change his selection?**

- Choices: A. Only before noon today<br>**B. Until the enrollment period ends**<br>C. After the next payroll<br>D. Once he receives a certificate
- Current keyed answer: **B. Until the enrollment period ends**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): You can make changes until the enrollment period ends. — Anh ấy có thể thay đổi cho đến khi kỳ đăng ký kết thúc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: You can make changes until the enrollment period ends.
- Current explanation: Anh ấy có thể thay đổi cho đến khi kỳ đăng ký kết thúc.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch027-part3-vendor-quotation` · Comparing vendor quotations

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: We received three quotations for the new office chairs. One is significantly lower than the others. Does it include delivery and assembly? Delivery is included, but assembly is charged separately. The other vendors include both services. Let’s compare the total cost before we make a recommendation.
- Transcript translation: Hai nhân viên xem ba báo giá ghế văn phòng, nhận ra một báo giá thấp không bao gồm phí lắp ráp và quyết định so sánh tổng chi phí.

**Q1. What are the speakers discussing?**

- Choices: **A. Office chair quotations**<br>B. A delayed meeting<br>C. A damaged shipment<br>D. An employee transfer
- Current keyed answer: **A. Office chair quotations**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): We received three quotations for the new office chairs. One is significantly lower than the others. — Họ đang so sánh báo giá cho ghế văn phòng mới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: We received three quotations for the new office chairs. One is significantly lower than the others.
- Current explanation: Họ đang so sánh báo giá cho ghế văn phòng mới.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What is excluded from the lowest quotation?**

- Choices: A. Delivery<br>B. Warranty coverage<br>**C. Assembly**<br>D. Taxes
- Current keyed answer: **C. Assembly**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Delivery is included, but assembly is charged separately. The other vendors include both services. — Báo giá thấp bao gồm giao hàng nhưng tính riêng lắp ráp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Delivery is included, but assembly is charged separately. The other vendors include both services.
- Current explanation: Báo giá thấp bao gồm giao hàng nhưng tính riêng lắp ráp.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will they do before recommending a vendor?**

- Choices: A. Place an order immediately<br>**B. Compare the total cost**<br>C. Ask employees to return chairs<br>D. Cancel the procurement request
- Current keyed answer: **B. Compare the total cost**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Let’s compare the total cost before we make a recommendation. — Người đàn ông đề nghị so sánh tổng chi phí trước khi đưa ra khuyến nghị.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Let’s compare the total cost before we make a recommendation.
- Current explanation: Người đàn ông đề nghị so sánh tổng chi phí trước khi đưa ra khuyến nghị.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 3 · `batch027-part3-client-appointment` · Rescheduling a client visit

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Transcript: Our client asked to move tomorrow’s site visit to the afternoon. I can change it to two thirty, but the technician is unavailable after four. That works. Please confirm the new time with the client and update the calendar. I’ll send the confirmation right away.
- Transcript translation: Khách hàng muốn chuyển lịch thăm hiện trường sang buổi chiều. Hai nhân viên thống nhất 2:30 và xác nhận lịch mới.

**Q1. What change did the client request?**

- Choices: A. A different technician<br>**B. A later appointment**<br>C. A new service contract<br>D. A revised invoice
- Current keyed answer: **B. A later appointment**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Our client asked to move tomorrow’s site visit to the afternoon. — Khách hàng là người yêu cầu chuyển buổi thăm hiện trường sang buổi chiều.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Our client asked to move tomorrow’s site visit to the afternoon.
- Current explanation: Khách hàng là người yêu cầu chuyển buổi thăm hiện trường sang buổi chiều.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When is the technician unavailable?**

- Choices: A. Before noon<br>**B. After four o’clock**<br>C. At two thirty<br>D. All day tomorrow
- Current keyed answer: **B. After four o’clock**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I can change it to two thirty, but the technician is unavailable after four. — Người phụ nữ nói kỹ thuật viên không thể sau 4 giờ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I can change it to two thirty, but the technician is unavailable after four.
- Current explanation: Người phụ nữ nói kỹ thuật viên không thể sau 4 giờ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will the woman do?**

- Choices: **A. Send a confirmation**<br>B. Prepare a contract<br>C. Call another technician<br>D. Print an invoice
- Current keyed answer: **A. Send a confirmation**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 3 multi-speaker dialogue evidence, inference grounding, and distractors
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): I’ll send the confirmation right away. — Cô ấy sẽ gửi xác nhận ngay sau khi cập nhật lịch.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: I’ll send the confirmation right away.
- Current explanation: Cô ấy sẽ gửi xác nhận ngay sau khi cập nhật lịch.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch027-part4-maintenance-notice` · Scheduled maintenance notice

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Good afternoon. The building's water supply will be temporarily shut off this Saturday from eight in the morning until noon while maintenance crews replace a valve. Please fill any bottles you may need before leaving on Friday. Restrooms on the first floor of the neighboring building will remain available. We apologize for the inconvenience.
- Transcript translation: Thông báo tạm ngừng cấp nước sáng thứ Bảy để thay van; nhân viên nên chuẩn bị nước từ trước.

**Q1. What is the announcement mainly about?**

- Choices: **A. A water service interruption**<br>B. A building security change<br>C. A new cafeteria opening<br>D. A parking restriction
- Current keyed answer: **A. A water service interruption**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The building's water supply will be temporarily shut off this Saturday from eight in the morning until noon while maintenance crews replace a valve. — Thông báo về việc tạm ngừng cấp nước để thay van.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The building's water supply will be temporarily shut off this Saturday from eight in the morning until noon while maintenance crews replace a valve.
- Current explanation: Thông báo về việc tạm ngừng cấp nước để thay van.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When will the work take place?**

- Choices: A. Friday afternoon<br>**B. Saturday morning**<br>C. Saturday evening<br>D. Monday morning
- Current keyed answer: **B. Saturday morning**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Please fill any bottles you may need before leaving on Friday. — Việc bảo trì diễn ra từ 8 giờ sáng đến 12 giờ trưa thứ Bảy.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Please fill any bottles you may need before leaving on Friday.
- Current explanation: Việc bảo trì diễn ra từ 8 giờ sáng đến 12 giờ trưa thứ Bảy.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What are employees advised to do?**

- Choices: A. Move their desks<br>B. Contact the maintenance crew<br>**C. Fill water bottles before Friday ends**<br>D. Use the restroom on the top floor
- Current keyed answer: **C. Fill water bottles before Friday ends**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Restrooms on the first floor of the neighboring building will remain available. — Nhân viên được nhắc lấy nước cần dùng trước khi rời đi vào thứ Sáu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Restrooms on the first floor of the neighboring building will remain available.
- Current explanation: Nhân viên được nhắc lấy nước cần dùng trước khi rời đi vào thứ Sáu.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch027-part4-travel-expense-policy` · Travel expense reminder

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: This is a reminder that travel expense reports for last month's business trips are due by the end of the day on Wednesday. Please attach receipts for hotel stays, meals, and transportation. If a receipt is missing, include a brief explanation in the comments field. Reports submitted after Wednesday may be processed in the following pay cycle. Contact Finance if you have questions.
- Transcript translation: Nhắc nhân viên nộp báo cáo công tác đúng hạn, đính kèm hóa đơn hoặc giải thích khi thiếu hóa đơn.

**Q1. Who is the announcement intended for?**

- Choices: A. New customers<br>**B. Employees who traveled for business**<br>C. Hotel managers<br>D. Finance department applicants
- Current keyed answer: **B. Employees who traveled for business**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Travel expense reports for last month's business trips are due by the end of the day on Wednesday. — Thông báo dành cho nhân viên đã đi công tác tháng trước và cần nộp báo cáo chi phí.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Travel expense reports for last month's business trips are due by the end of the day on Wednesday.
- Current explanation: Thông báo dành cho nhân viên đã đi công tác tháng trước và cần nộp báo cáo chi phí.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should employees do if a receipt is missing?**

- Choices: A. Request a new travel card<br>B. Leave the report blank<br>**C. Explain the missing receipt in comments**<br>D. Submit the report next month
- Current keyed answer: **C. Explain the missing receipt in comments**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): If a receipt is missing, include a brief explanation in the comments field. — Nếu thiếu hóa đơn, nhân viên phải giải thích ngắn trong phần comments.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: If a receipt is missing, include a brief explanation in the comments field.
- Current explanation: Nếu thiếu hóa đơn, nhân viên phải giải thích ngắn trong phần comments.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What may happen to late reports?**

- Choices: **A. They may be processed in the next pay cycle.**<br>B. They will be automatically rejected.<br>C. They will be paid in cash.<br>D. They must be approved by the hotel.
- Current keyed answer: **A. They may be processed in the next pay cycle.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Reports submitted after Wednesday may be processed in the following pay cycle. — Báo cáo nộp trễ có thể được xử lý ở kỳ lương tiếp theo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Reports submitted after Wednesday may be processed in the following pay cycle.
- Current explanation: Báo cáo nộp trễ có thể được xử lý ở kỳ lương tiếp theo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch027-part4-product-training` · Product training session

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Next week, our sales team will attend a training session on the updated inventory platform. The session will be held in the computer lab on Tuesday at ten. Please bring your laptop, although several demonstration devices will be available. The trainer will cover searching stock, creating transfer requests, and reviewing delivery status. A short practice exercise will follow each topic.
- Transcript translation: Thông báo buổi đào tạo nền tảng quản lý tồn kho vào thứ Ba tuần sau, có nội dung và bài thực hành theo từng chủ đề.

**Q1. What will the sales team learn about?**

- Choices: **A. A new inventory platform**<br>B. A revised travel policy<br>C. A marketing campaign<br>D. A customer loyalty program
- Current keyed answer: **A. A new inventory platform**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Our sales team will attend a training session on the updated inventory platform. — Buổi đào tạo tập trung vào nền tảng inventory được cập nhật.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Our sales team will attend a training session on the updated inventory platform.
- Current explanation: Buổi đào tạo tập trung vào nền tảng inventory được cập nhật.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Where will the training take place?**

- Choices: A. In the main auditorium<br>B. At the warehouse<br>**C. In the computer lab**<br>D. At the reception area
- Current keyed answer: **C. In the computer lab**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The session will be held in the computer lab on Tuesday at ten. — Buổi học diễn ra trong phòng máy tính.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The session will be held in the computer lab on Tuesday at ten.
- Current explanation: Buổi học diễn ra trong phòng máy tính.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What will participants do after each topic?**

- Choices: A. Take a long break<br>**B. Complete a short exercise**<br>C. Submit a travel report<br>D. Interview a customer
- Current keyed answer: **B. Complete a short exercise**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The trainer will cover searching stock, creating transfer requests, and reviewing delivery status. — Sau mỗi chủ đề sẽ có bài thực hành ngắn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The trainer will cover searching stock, creating transfer requests, and reviewing delivery status.
- Current explanation: Sau mỗi chủ đề sẽ có bài thực hành ngắn.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### Part 4 · `batch027-part4-store-hours` · Holiday store hours

- Batch: `027` · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Transcript: Please note that our downtown service counter will close at three p.m. on the day before the public holiday. Regular hours will resume on the following Monday. Customers who need to collect repaired items should do so before closing time. The online support team will remain available until six p.m. for urgent inquiries. Thank you for planning ahead.
- Transcript translation: Thông báo giờ đóng cửa sớm trước ngày lễ và nhắc khách nhận đồ sửa chữa trước 3 giờ; hỗ trợ trực tuyến vẫn hoạt động đến 6 giờ.

**Q1. What change is being announced?**

- Choices: A. The online service is permanently closed.<br>**B. The service counter will close early.**<br>C. Repairs are no longer available.<br>D. The store is moving downtown.
- Current keyed answer: **B. The service counter will close early.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Our downtown service counter will close at three p.m. on the day before the public holiday. — Quầy dịch vụ sẽ đóng sớm lúc 3 giờ chiều trước ngày lễ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Our downtown service counter will close at three p.m. on the day before the public holiday.
- Current explanation: Quầy dịch vụ sẽ đóng sớm lúc 3 giờ chiều trước ngày lễ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When will regular hours resume?**

- Choices: A. The next morning<br>B. On the public holiday<br>**C. The following Monday**<br>D. At six p.m.
- Current keyed answer: **C. The following Monday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Regular hours will resume on the following Monday. — Giờ hoạt động bình thường trở lại vào thứ Hai tiếp theo.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: Regular hours will resume on the following Monday.
- Current explanation: Giờ hoạt động bình thường trở lại vào thứ Hai tiếp theo.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Which service remains available until six p.m.?**

- Choices: A. Item collection<br>B. The downtown counter<br>C. The repair workshop<br>**D. Online support for urgent inquiries**
- Current keyed answer: **D. Online support for urgent inquiries**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Listening Part 4 monologue talk evidence, detail tracking, and next-step inference
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): The online support team will remain available until six p.m. for urgent inquiries. — Đội hỗ trợ trực tuyến là bộ phận vẫn tiếp nhận vấn đề khẩn cấp đến 6 giờ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Source pointer: The online support team will remain available until six p.m. for urgent inquiries.
- Current explanation: Đội hỗ trợ trực tuyến là bộ phận vẫn tiếp nhận vấn đề khẩn cấp đến 6 giờ.
- Reviewer: [ ] source supports key  [ ] response/action fits  [ ] distractors are clearly wrong  [ ] only one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

## B. Reading Part 7 reserve

Review source text and all documents together. Confirm that each selected answer is supported by the cited document(s), that the question does not require outside assumptions, and that no other option is also defensible.

### `part7-double-training-registration` · Part 7

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: EMAIL FROM TRAINING To: Department Supervisors From: Learning and Development Subject: Registration for the service workshop  The next customer service workshop will take place on April 18 in Training Room C. Each department may register up to four employees. Please submit names through the staff portal by April 10. Employees who attended the January session should not register again because the new workshop covers the same introductory material. A separate advanced session is planned for June.  REPLY FROM OPERATIONS To: Learning and Development From: Operations Supervisor Subject: Re: Registration for the service workshop  Our department would like to register three employees: Linh Tran, Marco Ruiz, and Helen Park. None of them attended the January session. Could you confirm whether laptops will be provided? They will need to access the updated customer record system during the final exercise.  Thank you, Operations
- EMAIL FROM TRAINING: To: Department Supervisors From: Learning and Development Subject: Registration for the service workshop  The next customer service workshop will take place on April 18 in Training Room C. Each department may register up to four employees. Please submit names through the staff portal by April 10. Employees who attended the January session should not register again because the new workshop covers the same introductory material. A separate advanced session is planned for June.
- REPLY FROM OPERATIONS: To: Learning and Development From: Operations Supervisor Subject: Re: Registration for the service workshop  Our department would like to register three employees: Linh Tran, Marco Ruiz, and Helen Park. None of them attended the January session. Could you confirm whether laptops will be provided? They will need to access the updated customer record system during the final exercise.  Thank you, Operations

**Q1. What is the purpose of the first email?**

- Choices: **A. To announce a new customer service workshop**<br>B. To explain a change in employee benefits<br>C. To request feedback on a training course<br>D. To cancel a previously scheduled session
- Current keyed answer: **A. To announce a new customer service workshop**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EMAIL FROM TRAINING — The next customer service workshop will take place on April 18 — Email đầu được gửi để thông báo ngày, địa điểm, điều kiện và cách đăng ký hội thảo dịch vụ khách hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EMAIL FROM TRAINING — The next customer service workshop will take place on April 18
- Current explanation: Email đầu được gửi để thông báo ngày, địa điểm, điều kiện và cách đăng ký hội thảo dịch vụ khách hàng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. By what date should supervisors submit employee names?**

- Choices: A. April 4<br>**B. April 10**<br>C. April 18<br>D. June 10
- Current keyed answer: **B. April 10**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EMAIL FROM TRAINING — Please submit names through the staff portal by April 10 — Hạn gửi danh sách nhân viên là ngày 10 tháng 4.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EMAIL FROM TRAINING — Please submit names through the staff portal by April 10
- Current explanation: Hạn gửi danh sách nhân viên là ngày 10 tháng 4.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why should some employees not register?**

- Choices: A. The room has limited computer access<br>B. They have not completed the portal profile<br>**C. They attended the same introductory session in January**<br>D. Their departments have exceeded the registration limit
- Current keyed answer: **C. They attended the same introductory session in January**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EMAIL FROM TRAINING — Employees who attended the January session should not register again — Nhân viên đã dự buổi nhập môn tháng 1 không nên đăng ký lại vì nội dung mới giống buổi trước.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EMAIL FROM TRAINING — Employees who attended the January session should not register again
- Current explanation: Nhân viên đã dự buổi nhập môn tháng 1 không nên đăng ký lại vì nội dung mới giống buổi trước.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What does the Operations Supervisor want to know?**

- Choices: A. Whether meals will be served<br>B. Whether the session can be moved to June<br>C. Whether the advanced course is full<br>**D. Whether laptops will be provided**
- Current keyed answer: **D. Whether laptops will be provided**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): REPLY FROM OPERATIONS — Could you confirm whether laptops will be provided? — Giám sát vận hành muốn xác nhận liệu máy tính xách tay có được cung cấp hay không.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: REPLY FROM OPERATIONS — Could you confirm whether laptops will be provided?
- Current explanation: Giám sát vận hành muốn xác nhận liệu máy tính xách tay có được cung cấp hay không.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. Which additional session is mentioned in the first email?**

- Choices: **A. An advanced session in June**<br>B. A leadership seminar in May<br>C. A software workshop in July<br>D. A safety briefing in August
- Current keyed answer: **A. An advanced session in June**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EMAIL FROM TRAINING — A separate advanced session is planned for June. — Email đầu nêu một buổi học nâng cao riêng dự kiến tổ chức vào tháng 6.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EMAIL FROM TRAINING — A separate advanced session is planned for June.
- Current explanation: Email đầu nêu một buổi học nâng cao riêng dự kiến tổ chức vào tháng 6.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `part7-double-delivery-reschedule` · Part 7

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: CUSTOMER MESSAGE To: Harbor Office Delivery From: Daniel Cho Subject: Delivery appointment  Our office renovation is taking longer than expected, and the receiving area will not be ready on August 7. Could you move the delivery of order HO-8842 to August 12? The building manager has confirmed that the loading bay will be available after 10 A.M. on that date. Please let me know if the change affects the delivery charge.  DELIVERY TEAM RESPONSE To: Daniel Cho From: Harbor Office Delivery Subject: Re: Delivery appointment  We have moved order HO-8842 to August 12. The delivery window is 10 A.M. to noon, as requested. There is no additional charge because the request was received more than three business days before the original appointment. Please ensure that the loading bay is clear when the driver arrives.
- CUSTOMER MESSAGE: To: Harbor Office Delivery From: Daniel Cho Subject: Delivery appointment  Our office renovation is taking longer than expected, and the receiving area will not be ready on August 7. Could you move the delivery of order HO-8842 to August 12? The building manager has confirmed that the loading bay will be available after 10 A.M. on that date. Please let me know if the change affects the delivery charge.
- DELIVERY TEAM RESPONSE: To: Daniel Cho From: Harbor Office Delivery Subject: Re: Delivery appointment  We have moved order HO-8842 to August 12. The delivery window is 10 A.M. to noon, as requested. There is no additional charge because the request was received more than three business days before the original appointment. Please ensure that the loading bay is clear when the driver arrives.

**Q1. Why does Daniel request a new delivery date?**

- Choices: A. The order has not left the warehouse<br>**B. The receiving area will not be ready**<br>C. The driver is unavailable<br>D. The loading bay is being repaired
- Current keyed answer: **B. The receiving area will not be ready**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): CUSTOMER MESSAGE — receiving area will not be ready on August 7 — Daniel yêu cầu đổi lịch vì khu vực nhận hàng chưa sẵn sàng do việc cải tạo kéo dài.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: CUSTOMER MESSAGE — receiving area will not be ready on August 7
- Current explanation: Daniel yêu cầu đổi lịch vì khu vực nhận hàng chưa sẵn sàng do việc cải tạo kéo dài.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What is the new delivery date?**

- Choices: A. August 7<br>B. August 10<br>**C. August 12**<br>D. August 14
- Current keyed answer: **C. August 12**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): DELIVERY TEAM RESPONSE — We have moved order HO-8842 to August 12 — Đội giao hàng xác nhận ngày giao mới là 12 tháng 8.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: DELIVERY TEAM RESPONSE — We have moved order HO-8842 to August 12
- Current explanation: Đội giao hàng xác nhận ngày giao mới là 12 tháng 8.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why is there no additional charge?**

- Choices: A. The order is a priority shipment<br>B. The customer has a premium account<br>C. The delivery distance has changed<br>**D. The request was made more than three business days in advance**
- Current keyed answer: **D. The request was made more than three business days in advance**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): DELIVERY TEAM RESPONSE — received more than three business days before the original appointment — Không có phụ phí vì yêu cầu được gửi trước lịch cũ hơn ba ngày làm việc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: DELIVERY TEAM RESPONSE — received more than three business days before the original appointment
- Current explanation: Không có phụ phí vì yêu cầu được gửi trước lịch cũ hơn ba ngày làm việc.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What should Daniel ensure?**

- Choices: **A. The loading bay is clear**<br>B. A payment is made in advance<br>C. The order is divided into two shipments<br>D. A staff member signs at the warehouse
- Current keyed answer: **A. The loading bay is clear**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: CROSS_QUESTION_KEY_LEAKAGE_CUE)
- Rationale (`rationale`): DELIVERY TEAM RESPONSE — Please ensure that the loading bay is clear — Daniel cần bảo đảm khu vực bốc dỡ thông thoáng khi tài xế đến.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: DELIVERY TEAM RESPONSE — Please ensure that the loading bay is clear
- Current explanation: Daniel cần bảo đảm khu vực bốc dỡ thông thoáng khi tài xế đến.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. When will the loading bay be available on the new date?**

- Choices: A. Before 8 A.M.<br>**B. After 10 A.M.**<br>C. Only after 2 P.M.<br>D. Throughout the previous day
- Current keyed answer: **B. After 10 A.M.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): CUSTOMER MESSAGE — loading bay will be available after 10 A.M. on that date — Daniel cho biết khu vực bốc dỡ sẽ sẵn sàng sau 10 giờ sáng ngày 12 tháng 8.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: CUSTOMER MESSAGE — loading bay will be available after 10 A.M. on that date
- Current explanation: Daniel cho biết khu vực bốc dỡ sẽ sẵn sàng sau 10 giờ sáng ngày 12 tháng 8.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `part7-single-office-closure` · Part 7

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: NOTICE NOTICE TO ALL STAFF  The third-floor office will be closed for electrical inspection on Friday, November 21. Employees assigned to that floor should work remotely or use available desks on the second floor. The inspection is expected to finish by 3 P.M.; however, staff should wait for an all-clear message from Facilities before returning. The small meeting room on the third floor will remain unavailable throughout the day. Questions should be directed to extension 204.
- NOTICE: NOTICE TO ALL STAFF  The third-floor office will be closed for electrical inspection on Friday, November 21. Employees assigned to that floor should work remotely or use available desks on the second floor. The inspection is expected to finish by 3 P.M.; however, staff should wait for an all-clear message from Facilities before returning. The small meeting room on the third floor will remain unavailable throughout the day. Questions should be directed to extension 204.

**Q1. Why will the third-floor office be closed?**

- Choices: A. A new team is moving in<br>B. The building will be repainted<br>**C. An electrical inspection is scheduled**<br>D. The network is being upgraded
- Current keyed answer: **C. An electrical inspection is scheduled**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): NOTICE — closed for electrical inspection — Thông báo cho biết tầng ba đóng cửa để kiểm tra hệ thống điện.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: NOTICE — closed for electrical inspection
- Current explanation: Thông báo cho biết tầng ba đóng cửa để kiểm tra hệ thống điện.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What may employees do during the closure?**

- Choices: A. Use the third-floor meeting room<br>B. Wait in the reception area<br>C. Transfer to another office building<br>**D. Work remotely or use second-floor desks**
- Current keyed answer: **D. Work remotely or use second-floor desks**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): NOTICE — work remotely or use available desks on the second floor — Nhân viên có thể làm từ xa hoặc dùng bàn trống ở tầng hai.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: NOTICE — work remotely or use available desks on the second floor
- Current explanation: Nhân viên có thể làm từ xa hoặc dùng bàn trống ở tầng hai.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When may employees return to the third floor?**

- Choices: **A. After receiving an all-clear message**<br>B. Immediately after 3 P.M.<br>C. At the beginning of the afternoon<br>D. Once the meeting room is reopened
- Current keyed answer: **A. After receiving an all-clear message**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): NOTICE — wait for an all-clear message from Facilities — Nhân viên chỉ được quay lại sau khi nhận thông báo xác nhận an toàn từ Facilities.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: NOTICE — wait for an all-clear message from Facilities
- Current explanation: Nhân viên chỉ được quay lại sau khi nhận thông báo xác nhận an toàn từ Facilities.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What is stated about the small meeting room?**

- Choices: A. It will be available after lunch<br>**B. It will remain closed all day**<br>C. It will be used by the inspection team<br>D. It has been moved to the second floor
- Current keyed answer: **B. It will remain closed all day**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): NOTICE — will remain unavailable throughout the day — Phòng họp nhỏ sẽ không sử dụng được trong suốt ngày hôm đó.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: NOTICE — will remain unavailable throughout the day
- Current explanation: Phòng họp nhỏ sẽ không sử dụng được trong suốt ngày hôm đó.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `part7-single-expense-guideline` · Part 7

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: INTERNAL GUIDELINE TRAVEL EXPENSE SUBMISSIONS  Employees must submit travel expenses within ten calendar days of returning from a business trip. Original receipts are required for individual expenses above $25. For public transportation, a digital ticket or payment confirmation is acceptable. Claims missing required documents will be returned to the employee and may be delayed until the next payment cycle. Managers should approve complete claims within three business days.
- INTERNAL GUIDELINE: TRAVEL EXPENSE SUBMISSIONS  Employees must submit travel expenses within ten calendar days of returning from a business trip. Original receipts are required for individual expenses above $25. For public transportation, a digital ticket or payment confirmation is acceptable. Claims missing required documents will be returned to the employee and may be delayed until the next payment cycle. Managers should approve complete claims within three business days.

**Q1. What is the deadline for submitting travel expenses?**

- Choices: A. Three business days after approval<br>B. Twenty-five days after departure<br>**C. Ten calendar days after returning**<br>D. Before the business trip begins
- Current keyed answer: **C. Ten calendar days after returning**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): INTERNAL GUIDELINE — within ten calendar days of returning — Hạn nộp chi phí là mười ngày theo lịch kể từ ngày nhân viên trở về.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: INTERNAL GUIDELINE — within ten calendar days of returning
- Current explanation: Hạn nộp chi phí là mười ngày theo lịch kể từ ngày nhân viên trở về.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When is an original receipt required?**

- Choices: A. For every public transportation trip<br>B. Only for hotel expenses<br>C. When a manager requests one<br>**D. For individual expenses above $25**
- Current keyed answer: **D. For individual expenses above $25**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): INTERNAL GUIDELINE — Original receipts are required for individual expenses above $25 — Hóa đơn gốc bắt buộc đối với từng khoản chi trên 25 đô la.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: INTERNAL GUIDELINE — Original receipts are required for individual expenses above $25
- Current explanation: Hóa đơn gốc bắt buộc đối với từng khoản chi trên 25 đô la.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What document may be used for public transportation?**

- Choices: **A. A digital ticket or payment confirmation**<br>B. A manager’s handwritten note<br>C. A hotel invoice<br>D. A printed travel itinerary only
- Current keyed answer: **A. A digital ticket or payment confirmation**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): INTERNAL GUIDELINE — a digital ticket or payment confirmation is acceptable — Vé điện tử hoặc xác nhận thanh toán được chấp nhận cho phương tiện công cộng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: INTERNAL GUIDELINE — a digital ticket or payment confirmation is acceptable
- Current explanation: Vé điện tử hoặc xác nhận thanh toán được chấp nhận cho phương tiện công cộng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What may happen to an incomplete claim?**

- Choices: A. It will be automatically approved<br>**B. It may be delayed until the next payment cycle**<br>C. It will be paid in cash<br>D. It will be transferred to another department
- Current keyed answer: **B. It may be delayed until the next payment cycle**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): INTERNAL GUIDELINE — may be delayed until the next payment cycle — Hồ sơ thiếu giấy tờ có thể bị chuyển sang chu kỳ thanh toán kế tiếp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: INTERNAL GUIDELINE — may be delayed until the next payment cycle
- Current explanation: Hồ sơ thiếu giấy tờ có thể bị chuyển sang chu kỳ thanh toán kế tiếp.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `part7-double-product-recall` · Part 7

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: CUSTOMER BULLETIN PRODUCT NOTICE: MODEL AX-40  Northstar Electronics is asking customers who purchased an AX-40 desk scanner between February 1 and May 30 to stop using the device. A component may overheat during extended operation. Customers can request a free replacement by entering the serial number on the support website. The company will cover return shipping. Orders placed after May 30 use an updated component and are not included in this notice.  SERVICE TEAM EMAIL To: Customer Support Team From: Quality Assurance Subject: Handling AX-40 inquiries  When customers contact us about an AX-40 scanner, first confirm the purchase date and serial number. If the device was purchased within the affected period, direct the customer to the replacement form. Do not promise a specific delivery date; replacement units are being shipped in batches. Escalate any report of smoke or unusual heat to the safety desk immediately.
- CUSTOMER BULLETIN: PRODUCT NOTICE: MODEL AX-40  Northstar Electronics is asking customers who purchased an AX-40 desk scanner between February 1 and May 30 to stop using the device. A component may overheat during extended operation. Customers can request a free replacement by entering the serial number on the support website. The company will cover return shipping. Orders placed after May 30 use an updated component and are not included in this notice.
- SERVICE TEAM EMAIL: To: Customer Support Team From: Quality Assurance Subject: Handling AX-40 inquiries  When customers contact us about an AX-40 scanner, first confirm the purchase date and serial number. If the device was purchased within the affected period, direct the customer to the replacement form. Do not promise a specific delivery date; replacement units are being shipped in batches. Escalate any report of smoke or unusual heat to the safety desk immediately.

**Q1. What issue is associated with the AX-40?**

- Choices: A. Its scanning speed is inconsistent<br>B. Its power cable is too short<br>**C. A component may overheat**<br>D. The software cannot save files
- Current keyed answer: **C. A component may overheat**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): CUSTOMER BULLETIN — A component may overheat — Vấn đề của AX-40 là một linh kiện có thể quá nóng khi thiết bị hoạt động lâu.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: CUSTOMER BULLETIN — A component may overheat
- Current explanation: Vấn đề của AX-40 là một linh kiện có thể quá nóng khi thiết bị hoạt động lâu.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Which customers are included in the notice?**

- Choices: A. Those who bought the scanner after May 30<br>B. All customers who own any Northstar scanner<br>C. Only customers with an expired warranty<br>**D. Those who bought it between February 1 and May 30**
- Current keyed answer: **D. Those who bought it between February 1 and May 30**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): CUSTOMER BULLETIN — between February 1 and May 30 — Thông báo áp dụng cho khách hàng mua máy trong khoảng từ ngày 1 tháng 2 đến 30 tháng 5.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: CUSTOMER BULLETIN — between February 1 and May 30
- Current explanation: Thông báo áp dụng cho khách hàng mua máy trong khoảng từ ngày 1 tháng 2 đến 30 tháng 5.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should support staff verify first?**

- Choices: **A. The purchase date and serial number**<br>B. The customer’s address and payment method<br>C. The device color and packaging<br>D. The software version and operating system
- Current keyed answer: **A. The purchase date and serial number**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE TEAM EMAIL — confirm the purchase date and serial number — Nhân viên hỗ trợ phải xác nhận ngày mua và số sê-ri trước tiên.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE TEAM EMAIL — confirm the purchase date and serial number
- Current explanation: Nhân viên hỗ trợ phải xác nhận ngày mua và số sê-ri trước tiên.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What should staff do if a customer reports smoke?**

- Choices: A. Offer a discount on a new model<br>**B. Escalate the report to the safety desk immediately**<br>C. Ask the customer to restart the scanner<br>D. Wait for the next replacement batch
- Current keyed answer: **B. Escalate the report to the safety desk immediately**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE TEAM EMAIL — Escalate any report of smoke or unusual heat to the safety desk immediately — Báo cáo có khói hoặc nhiệt bất thường phải được chuyển ngay đến bộ phận an toàn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE TEAM EMAIL — Escalate any report of smoke or unusual heat to the safety desk immediately
- Current explanation: Báo cáo có khói hoặc nhiệt bất thường phải được chuyển ngay đến bộ phận an toàn.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. What are support employees instructed not to do?**

- Choices: A. Ask for the serial number<br>B. Direct customers to the replacement form<br>**C. Promise a specific replacement delivery date**<br>D. Confirm the purchase date
- Current keyed answer: **C. Promise a specific replacement delivery date**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE TEAM EMAIL — Do not promise a specific delivery date — Nhân viên hỗ trợ không được hứa một ngày giao máy thay thế cụ thể.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE TEAM EMAIL — Do not promise a specific delivery date
- Current explanation: Nhân viên hỗ trợ không được hứa một ngày giao máy thay thế cụ thể.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `part7-single-recruitment-fair` · Part 7

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: EVENT ANNOUNCEMENT CAREER OPEN HOUSE  The annual career open house will be held on Saturday, September 13, from 9 A.M. to 1 P.M. at the Riverside Training Center. Visitors can speak with recruitment specialists, attend short sessions on interview preparation, and submit résumés for current openings. Registration is free, but attendees must reserve a time slot online. Parking is limited, so visitors are encouraged to use the public bus stop outside the east entrance. A confirmation email will include the room schedule.
- EVENT ANNOUNCEMENT: CAREER OPEN HOUSE  The annual career open house will be held on Saturday, September 13, from 9 A.M. to 1 P.M. at the Riverside Training Center. Visitors can speak with recruitment specialists, attend short sessions on interview preparation, and submit résumés for current openings. Registration is free, but attendees must reserve a time slot online. Parking is limited, so visitors are encouraged to use the public bus stop outside the east entrance. A confirmation email will include the room schedule.

**Q1. What is the main purpose of the announcement?**

- Choices: A. To announce a change in office hours<br>B. To introduce a new training policy<br>C. To request employee volunteers<br>**D. To advertise a recruitment event**
- Current keyed answer: **D. To advertise a recruitment event**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EVENT ANNOUNCEMENT — annual career open house — Thông báo nhằm giới thiệu ngày hội nghề nghiệp và các hoạt động tuyển dụng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EVENT ANNOUNCEMENT — annual career open house
- Current explanation: Thông báo nhằm giới thiệu ngày hội nghề nghiệp và các hoạt động tuyển dụng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What must attendees do before arriving?**

- Choices: **A. Reserve a time slot online**<br>B. Pay an entrance fee<br>C. Send a résumé by mail<br>D. Contact a recruitment specialist
- Current keyed answer: **A. Reserve a time slot online**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EVENT ANNOUNCEMENT — must reserve a time slot online — Người tham dự phải đặt khung giờ trực tuyến trước khi đến.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EVENT ANNOUNCEMENT — must reserve a time slot online
- Current explanation: Người tham dự phải đặt khung giờ trực tuyến trước khi đến.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why are visitors encouraged to use public transportation?**

- Choices: A. The event starts before buses operate<br>**B. Parking is limited**<br>C. The training center is closed to cars<br>D. The east entrance is under construction
- Current keyed answer: **B. Parking is limited**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EVENT ANNOUNCEMENT — Parking is limited — Ban tổ chức khuyến khích dùng phương tiện công cộng vì chỗ đỗ xe hạn chế.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EVENT ANNOUNCEMENT — Parking is limited
- Current explanation: Ban tổ chức khuyến khích dùng phương tiện công cộng vì chỗ đỗ xe hạn chế.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What will the confirmation email contain?**

- Choices: A. A list of current vacancies<br>B. A parking permit<br>**C. The room schedule**<br>D. An interview result
- Current keyed answer: **C. The room schedule**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EVENT ANNOUNCEMENT — confirmation email will include the room schedule — Email xác nhận sẽ cung cấp lịch sử dụng các phòng để người tham dự chuẩn bị.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EVENT ANNOUNCEMENT — confirmation email will include the room schedule
- Current explanation: Email xác nhận sẽ cung cấp lịch sử dụng các phòng để người tham dự chuẩn bị.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-single-equipment-inspection` · Equipment inspection schedule

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: MAINTENANCE NOTICE The annual inspection of office equipment will take place on May 6 and 7. Technicians will visit each department between 9 A.M. and 3 P.M. Employees should save their work and leave desktop computers powered on. Any device that cannot be inspected during the scheduled visit should be reported to Facilities by May 3. A temporary loan unit may be requested if essential equipment must be removed for repair.
- MAINTENANCE NOTICE: The annual inspection of office equipment will take place on May 6 and 7. Technicians will visit each department between 9 A.M. and 3 P.M. Employees should save their work and leave desktop computers powered on. Any device that cannot be inspected during the scheduled visit should be reported to Facilities by May 3. A temporary loan unit may be requested if essential equipment must be removed for repair.

**Q1. What is the purpose of the notice?**

- Choices: **A. To announce an equipment inspection**<br>B. To introduce a new computer system<br>C. To recruit maintenance staff<br>D. To report a power failure
- Current keyed answer: **A. To announce an equipment inspection**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): MAINTENANCE NOTICE — annual inspection of office equipment — Thông tin trong tài liệu cho biết: Thông báo về lịch kiểm tra thiết bị văn phòng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: MAINTENANCE NOTICE — annual inspection of office equipment
- Current explanation: Thông tin trong tài liệu cho biết: Thông báo về lịch kiểm tra thiết bị văn phòng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should employees do with desktop computers?**

- Choices: A. Disconnect all cables<br>**B. Leave them powered on**<br>C. Move them to reception<br>D. Return them to the supplier
- Current keyed answer: **B. Leave them powered on**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): MAINTENANCE NOTICE — leave desktop computers powered on — Nhân viên cần để máy tính để bàn bật nguồn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: MAINTENANCE NOTICE — leave desktop computers powered on
- Current explanation: Nhân viên cần để máy tính để bàn bật nguồn.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. By when should uninspectable devices be reported?**

- Choices: A. May 6<br>B. May 7<br>**C. May 3**<br>D. May 9
- Current keyed answer: **C. May 3**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): MAINTENANCE NOTICE — reported to Facilities by May 3 — Thiết bị không thể kiểm tra theo lịch cần báo trước ngày 3 tháng 5.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: MAINTENANCE NOTICE — reported to Facilities by May 3
- Current explanation: Thiết bị không thể kiểm tra theo lịch cần báo trước ngày 3 tháng 5.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What may employees request?**

- Choices: A. A permanent replacement<br>B. A later inspection fee<br>C. A new office<br>**D. A temporary loan unit**
- Current keyed answer: **D. A temporary loan unit**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): MAINTENANCE NOTICE — A temporary loan unit may be requested — Có thể yêu cầu thiết bị cho mượn tạm thời nếu thiết bị thiết yếu phải sửa chữa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: MAINTENANCE NOTICE — A temporary loan unit may be requested
- Current explanation: Có thể yêu cầu thiết bị cho mượn tạm thời nếu thiết bị thiết yếu phải sửa chữa.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-single-training-registration` · Training registration instructions

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: TRAINING PORTAL MESSAGE Registration for the project-management workshop is now open. The two-day workshop will be held June 18–19 in the West Training Center. Staff members must complete the online registration form and obtain approval from their supervisors by June 10. Because seating is limited to twenty-four participants, applications will be processed in the order received. A confirmation message will be sent within two business days.
- TRAINING PORTAL MESSAGE: Registration for the project-management workshop is now open. The two-day workshop will be held June 18–19 in the West Training Center. Staff members must complete the online registration form and obtain approval from their supervisors by June 10. Because seating is limited to twenty-four participants, applications will be processed in the order received. A confirmation message will be sent within two business days.

**Q1. How long will the workshop last?**

- Choices: **A. Two days**<br>B. One day<br>C. Three days<br>D. One week
- Current keyed answer: **A. Two days**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): TRAINING PORTAL MESSAGE — two-day workshop — Workshop diễn ra trong hai ngày 18–19 tháng 6.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: TRAINING PORTAL MESSAGE — two-day workshop
- Current explanation: Workshop diễn ra trong hai ngày 18–19 tháng 6.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What must staff obtain before registering?**

- Choices: A. A travel voucher<br>**B. A supervisor’s approval**<br>C. A printed certificate<br>D. A customer reference
- Current keyed answer: **B. A supervisor’s approval**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): TRAINING PORTAL MESSAGE — obtain approval from their supervisors — Nhân viên phải có phê duyệt của quản lý.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: TRAINING PORTAL MESSAGE — obtain approval from their supervisors
- Current explanation: Nhân viên phải có phê duyệt của quản lý.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why may some applicants not get a place?**

- Choices: A. The fee is too high<br>B. The workshop is canceled<br>**C. Seats are limited**<br>D. The form is unavailable
- Current keyed answer: **C. Seats are limited**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): TRAINING PORTAL MESSAGE — seating is limited to twenty-four participants — Số chỗ chỉ giới hạn 24 người.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: TRAINING PORTAL MESSAGE — seating is limited to twenty-four participants
- Current explanation: Số chỗ chỉ giới hạn 24 người.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. When should applicants expect confirmation?**

- Choices: A. Immediately<br>B. On June 10<br>C. After the workshop<br>**D. Within two business days**
- Current keyed answer: **D. Within two business days**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): TRAINING PORTAL MESSAGE — within two business days — Tin xác nhận được gửi trong vòng hai ngày làm việc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: TRAINING PORTAL MESSAGE — within two business days
- Current explanation: Tin xác nhận được gửi trong vòng hai ngày làm việc.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-single-customer-feedback` · Customer feedback summary

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: SERVICE QUALITY UPDATE The customer support team received 486 survey responses in April. Overall satisfaction increased from 82 percent to 87 percent, mainly because average response time fell by three hours. However, comments about the returns process remained negative. The operations manager will review the current return instructions and propose revisions at the May 14 meeting. Team leaders are asked to share the updated procedure with all agents after approval.
- SERVICE QUALITY UPDATE: The customer support team received 486 survey responses in April. Overall satisfaction increased from 82 percent to 87 percent, mainly because average response time fell by three hours. However, comments about the returns process remained negative. The operations manager will review the current return instructions and propose revisions at the May 14 meeting. Team leaders are asked to share the updated procedure with all agents after approval.

**Q1. What improved in April?**

- Choices: **A. Overall customer satisfaction**<br>B. Product availability<br>C. Delivery costs<br>D. The number of returns
- Current keyed answer: **A. Overall customer satisfaction**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE QUALITY UPDATE — Overall satisfaction increased from 82 percent to 87 percent — Mức độ hài lòng tổng thể tăng từ 82% lên 87%.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE QUALITY UPDATE — Overall satisfaction increased from 82 percent to 87 percent
- Current explanation: Mức độ hài lòng tổng thể tăng từ 82% lên 87%.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What contributed to the improvement?**

- Choices: A. A new advertising campaign<br>**B. A lower average response time**<br>C. Longer opening hours<br>D. A price reduction
- Current keyed answer: **B. A lower average response time**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE QUALITY UPDATE — average response time fell by three hours — Thông tin trong tài liệu cho biết: Thời gian phản hồi trung bình giảm ba giờ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE QUALITY UPDATE — average response time fell by three hours
- Current explanation: Thông tin trong tài liệu cho biết: Thời gian phản hồi trung bình giảm ba giờ.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What issue still requires attention?**

- Choices: A. The survey website<br>B. The office schedule<br>**C. The returns process**<br>D. The support team size
- Current keyed answer: **C. The returns process**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE QUALITY UPDATE — comments about the returns process remained negative — Thông tin trong tài liệu cho biết: Nhận xét về quy trình đổi trả vẫn tiêu cực.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE QUALITY UPDATE — comments about the returns process remained negative
- Current explanation: Thông tin trong tài liệu cho biết: Nhận xét về quy trình đổi trả vẫn tiêu cực.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What are team leaders asked to do?**

- Choices: A. Rewrite all customer surveys<br>B. Cancel the May meeting<br>C. Hire additional agents<br>**D. Share the approved procedure**
- Current keyed answer: **D. Share the approved procedure**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SERVICE QUALITY UPDATE — share the updated procedure with all agents after approval — Trưởng nhóm cần chia sẻ quy trình cập nhật sau khi được duyệt.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SERVICE QUALITY UPDATE — share the updated procedure with all agents after approval
- Current explanation: Trưởng nhóm cần chia sẻ quy trình cập nhật sau khi được duyệt.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-single-library-hours` · Changes to library opening hours

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: COMMUNITY LIBRARY ANNOUNCEMENT Beginning September 1, the Central Community Library will open at 8 A.M. on weekdays instead of 9 A.M. Weekend hours will remain unchanged. The earlier opening is intended to provide students and commuters with additional study time before work or classes. The self-service return box will continue to operate outside the building after closing. Visitors who need assistance with research databases should book a twenty-minute appointment with a librarian.
- COMMUNITY LIBRARY ANNOUNCEMENT: Beginning September 1, the Central Community Library will open at 8 A.M. on weekdays instead of 9 A.M. Weekend hours will remain unchanged. The earlier opening is intended to provide students and commuters with additional study time before work or classes. The self-service return box will continue to operate outside the building after closing. Visitors who need assistance with research databases should book a twenty-minute appointment with a librarian.

**Q1. When will the new weekday schedule begin?**

- Choices: **A. September 1**<br>B. August 1<br>C. September 9<br>D. October 1
- Current keyed answer: **A. September 1**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): COMMUNITY LIBRARY ANNOUNCEMENT — Beginning September 1 — Lịch mới bắt đầu từ ngày 1 tháng 9.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: COMMUNITY LIBRARY ANNOUNCEMENT — Beginning September 1
- Current explanation: Lịch mới bắt đầu từ ngày 1 tháng 9.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What will remain unchanged?**

- Choices: A. Weekday opening time<br>**B. Weekend hours**<br>C. The return box location<br>D. Research database access
- Current keyed answer: **B. Weekend hours**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): COMMUNITY LIBRARY ANNOUNCEMENT — Weekend hours will remain unchanged — Giờ cuối tuần không thay đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: COMMUNITY LIBRARY ANNOUNCEMENT — Weekend hours will remain unchanged
- Current explanation: Giờ cuối tuần không thay đổi.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Why is the library opening earlier?**

- Choices: A. To reduce staffing costs<br>B. To host weekend events<br>**C. To provide more study time**<br>D. To renovate the building
- Current keyed answer: **C. To provide more study time**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): COMMUNITY LIBRARY ANNOUNCEMENT — additional study time before work or classes — Mục đích là tạo thêm thời gian học trước giờ làm hoặc học.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: COMMUNITY LIBRARY ANNOUNCEMENT — additional study time before work or classes
- Current explanation: Mục đích là tạo thêm thời gian học trước giờ làm hoặc học.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. How can visitors get help with research databases?**

- Choices: A. By sending a letter<br>B. By using the return box<br>C. By visiting on weekends only<br>**D. By booking an appointment**
- Current keyed answer: **D. By booking an appointment**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): COMMUNITY LIBRARY ANNOUNCEMENT — book a twenty-minute appointment with a librarian — Khách cần đặt lịch 20 phút với thủ thư.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: COMMUNITY LIBRARY ANNOUNCEMENT — book a twenty-minute appointment with a librarian
- Current explanation: Khách cần đặt lịch 20 phút với thủ thư.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-double-conference-booking` · Conference room booking and confirmation

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: EMAIL To: Department Coordinators Subject: Conference room reservations The third-floor conference rooms will be unavailable on July 8 while new video equipment is installed. Teams that already reserved a room for that date may use the second-floor training rooms instead. Please reply to this email by July 2 with your preferred time. Reservations for all other dates are unaffected.  REPLY To: Facilities Desk Subject: Re: Conference room reservations Our product team has a reservation for July 8 at 10 A.M. We would like to use Training Room 2 at the same time. We will need the large display and a speakerphone for a remote presentation. Please confirm whether these items will be available before we notify the attendees.
- EMAIL: To: Department Coordinators Subject: Conference room reservations The third-floor conference rooms will be unavailable on July 8 while new video equipment is installed. Teams that already reserved a room for that date may use the second-floor training rooms instead. Please reply to this email by July 2 with your preferred time. Reservations for all other dates are unaffected.
- REPLY: To: Facilities Desk Subject: Re: Conference room reservations Our product team has a reservation for July 8 at 10 A.M. We would like to use Training Room 2 at the same time. We will need the large display and a speakerphone for a remote presentation. Please confirm whether these items will be available before we notify the attendees.

**Q1. Why are the third-floor rooms unavailable?**

- Choices: **A. Video equipment is being installed**<br>B. They are being painted<br>C. A conference is taking place<br>D. The floor is being expanded
- Current keyed answer: **A. Video equipment is being installed**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EMAIL — new video equipment is installed — Thiết bị video mới đang được lắp đặt.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EMAIL — new video equipment is installed
- Current explanation: Thiết bị video mới đang được lắp đặt.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What must coordinators do by July 2?**

- Choices: A. Pay a room fee<br>**B. Reply with a preferred time**<br>C. Submit a list of attendees<br>D. Collect a room key
- Current keyed answer: **B. Reply with a preferred time**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EMAIL — reply to this email by July 2 with your preferred time — Điều phối viên cần phản hồi thời gian mong muốn trước ngày 2 tháng 7.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EMAIL — reply to this email by July 2 with your preferred time
- Current explanation: Điều phối viên cần phản hồi thời gian mong muốn trước ngày 2 tháng 7.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Which room does the product team request?**

- Choices: A. Conference Room 3<br>B. Training Room 1<br>**C. Training Room 2**<br>D. The main auditorium
- Current keyed answer: **C. Training Room 2**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_DISTRACTOR_HIGH_OVERLAP)
- Rationale (`rationale`): REPLY — use Training Room 2 — Thông tin trong tài liệu cho biết: Nhóm sản phẩm yêu cầu Training Room 2.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: REPLY — use Training Room 2
- Current explanation: Thông tin trong tài liệu cho biết: Nhóm sản phẩm yêu cầu Training Room 2.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What equipment does the team need?**

- Choices: A. A printer and scanner<br>B. Two laptops<br>C. A projector and microphone<br>**D. A large display and speakerphone**
- Current keyed answer: **D. A large display and speakerphone**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): REPLY — large display and a speakerphone — Thông tin trong tài liệu cho biết: Email yêu cầu màn hình lớn và điện thoại hội nghị.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: REPLY — large display and a speakerphone
- Current explanation: Thông tin trong tài liệu cho biết: Email yêu cầu màn hình lớn và điện thoại hội nghị.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. What does the team want Facilities to do before notifying attendees?**

- Choices: **A. Confirm equipment availability**<br>B. Change the presentation topic<br>C. Move the meeting to July 9<br>D. Send a new calendar invitation
- Current keyed answer: **A. Confirm equipment availability**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): REPLY — confirm whether these items will be available — Nhóm muốn xác nhận thiết bị có sẵn trước khi thông báo người tham dự.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: REPLY — confirm whether these items will be available
- Current explanation: Nhóm muốn xác nhận thiết bị có sẵn trước khi thông báo người tham dự.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-double-shipping-delay` · Shipment delay and revised delivery plan

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: CUSTOMER EMAIL Hello, our order of replacement filters was expected to arrive on March 12, but the tracking page has not changed for two days. We need the filters before our maintenance shutdown on March 18. Could you check the shipment status and advise whether delivery can be expedited?  SUPPLIER RESPONSE Thank you for contacting us. The shipment was held at the regional sorting center because of severe weather. It has now been released and is scheduled to reach your facility on March 15. We cannot guarantee an earlier delivery, but we have upgraded the shipment to priority handling at no additional charge. The tracking page should refresh by this evening.
- CUSTOMER EMAIL: Hello, our order of replacement filters was expected to arrive on March 12, but the tracking page has not changed for two days. We need the filters before our maintenance shutdown on March 18. Could you check the shipment status and advise whether delivery can be expedited?
- SUPPLIER RESPONSE: Thank you for contacting us. The shipment was held at the regional sorting center because of severe weather. It has now been released and is scheduled to reach your facility on March 15. We cannot guarantee an earlier delivery, but we have upgraded the shipment to priority handling at no additional charge. The tracking page should refresh by this evening.

**Q1. What is the customer concerned about?**

- Choices: A. A missing invoice<br>**B. A delayed shipment**<br>C. A damaged warehouse<br>D. A price increase
- Current keyed answer: **B. A delayed shipment**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): CUSTOMER EMAIL — tracking page has not changed for two days — Khách lo lắng vì lô hàng bị chậm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: CUSTOMER EMAIL — tracking page has not changed for two days
- Current explanation: Khách lo lắng vì lô hàng bị chậm.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why does the customer need the filters before March 18?**

- Choices: A. A new branch is opening<br>B. The supplier is closing<br>**C. A maintenance shutdown is planned**<br>D. An audit will begin
- Current keyed answer: **C. A maintenance shutdown is planned**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): CUSTOMER EMAIL — maintenance shutdown on March 18 — Khách cần bộ lọc trước đợt dừng bảo trì ngày 18 tháng 3.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: CUSTOMER EMAIL — maintenance shutdown on March 18
- Current explanation: Khách cần bộ lọc trước đợt dừng bảo trì ngày 18 tháng 3.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What caused the delay?**

- Choices: A. A customs inspection<br>B. A payment issue<br>C. Incorrect packaging<br>**D. Severe weather**
- Current keyed answer: **D. Severe weather**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SUPPLIER RESPONSE — held at the regional sorting center because of severe weather — Thời tiết xấu khiến lô hàng bị giữ tại trung tâm phân loại.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SUPPLIER RESPONSE — held at the regional sorting center because of severe weather
- Current explanation: Thời tiết xấu khiến lô hàng bị giữ tại trung tâm phân loại.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. When is the shipment expected to arrive?**

- Choices: **A. March 15**<br>B. March 12<br>C. March 18<br>D. March 20
- Current keyed answer: **A. March 15**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SUPPLIER RESPONSE — scheduled to reach your facility on March 15 — Thông tin trong tài liệu cho biết: Nhà cung cấp dự kiến giao ngày 15 tháng 3.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SUPPLIER RESPONSE — scheduled to reach your facility on March 15
- Current explanation: Thông tin trong tài liệu cho biết: Nhà cung cấp dự kiến giao ngày 15 tháng 3.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. What has the supplier done?**

- Choices: A. Canceled the order<br>**B. Upgraded to priority handling**<br>C. Charged for express delivery<br>D. Sent a replacement invoice
- Current keyed answer: **B. Upgraded to priority handling**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SUPPLIER RESPONSE — upgraded the shipment to priority handling — Thông tin trong tài liệu cho biết: Nhà cung cấp nâng cấp xử lý ưu tiên miễn phí.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SUPPLIER RESPONSE — upgraded the shipment to priority handling
- Current explanation: Thông tin trong tài liệu cho biết: Nhà cung cấp nâng cấp xử lý ưu tiên miễn phí.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-double-job-fair` · Job fair registration and visitor follow-up

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: EVENT WEBPAGE The Regional Careers Fair will take place on October 4 at the Civic Exhibition Hall. Employers from finance, technology and logistics will attend. Job seekers may register online until September 27. Bring printed copies of your résumé; on-site printing will not be available. A free shuttle will run every thirty minutes from Central Station.  FOLLOW-UP EMAIL Thank you for registering for the Regional Careers Fair. Your entry pass is attached. The logistics employers will be located in Hall C, while finance and technology companies will be in Hall A. The first career advice session begins at 10:30 A.M. If you can no longer attend, please cancel your registration so another visitor can use the place.
- EVENT WEBPAGE: The Regional Careers Fair will take place on October 4 at the Civic Exhibition Hall. Employers from finance, technology and logistics will attend. Job seekers may register online until September 27. Bring printed copies of your résumé; on-site printing will not be available. A free shuttle will run every thirty minutes from Central Station.
- FOLLOW-UP EMAIL: Thank you for registering for the Regional Careers Fair. Your entry pass is attached. The logistics employers will be located in Hall C, while finance and technology companies will be in Hall A. The first career advice session begins at 10:30 A.M. If you can no longer attend, please cancel your registration so another visitor can use the place.

**Q1. Where will the fair be held?**

- Choices: A. Central Station<br>B. Regional Training Center<br>**C. Civic Exhibition Hall**<br>D. Hall C only
- Current keyed answer: **C. Civic Exhibition Hall**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EVENT WEBPAGE — at the Civic Exhibition Hall — Địa điểm là Civic Exhibition Hall.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EVENT WEBPAGE — at the Civic Exhibition Hall
- Current explanation: Địa điểm là Civic Exhibition Hall.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should visitors bring?**

- Choices: A. A laptop<br>B. A payment receipt<br>C. A company badge<br>**D. A printed résumé**
- Current keyed answer: **D. A printed résumé**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): EVENT WEBPAGE — Bring printed copies of your résumé — Khách cần mang bản in hồ sơ xin việc.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: EVENT WEBPAGE — Bring printed copies of your résumé
- Current explanation: Khách cần mang bản in hồ sơ xin việc.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Where will logistics employers be located?**

- Choices: **A. Hall C**<br>B. Hall A<br>C. Hall B<br>D. The main entrance
- Current keyed answer: **A. Hall C**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): FOLLOW-UP EMAIL — logistics employers will be located in Hall C — Thông tin trong tài liệu cho biết: Nhà tuyển dụng ngành logistics ở Hall C.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: FOLLOW-UP EMAIL — logistics employers will be located in Hall C
- Current explanation: Thông tin trong tài liệu cho biết: Nhà tuyển dụng ngành logistics ở Hall C.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. What time does the first advice session begin?**

- Choices: A. 9:30 A.M.<br>**B. 10:30 A.M.**<br>C. 10:00 A.M.<br>D. 11:30 A.M.
- Current keyed answer: **B. 10:30 A.M.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): FOLLOW-UP EMAIL — begins at 10:30 A.M. — Thông tin trong tài liệu cho biết: Buổi tư vấn đầu tiên bắt đầu lúc 10 giờ 30.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: FOLLOW-UP EMAIL — begins at 10:30 A.M.
- Current explanation: Thông tin trong tài liệu cho biết: Buổi tư vấn đầu tiên bắt đầu lúc 10 giờ 30.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. Why should people cancel if they cannot attend?**

- Choices: A. To receive a refund<br>B. To change the event date<br>**C. To help another visitor attend**<br>D. To request a printed pass
- Current keyed answer: **C. To help another visitor attend**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): FOLLOW-UP EMAIL — so another visitor can use the place — Việc hủy đăng ký giúp người khác có thể sử dụng chỗ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: FOLLOW-UP EMAIL — so another visitor can use the place
- Current explanation: Việc hủy đăng ký giúp người khác có thể sử dụng chỗ.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch025-part7-double-software-renewal` · Software renewal proposal and approval

- Document type: DOUBLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: IT PROPOSAL The design department currently uses 18 licenses of the StudioPro application. The annual subscription expires on November 30. The vendor has offered a 12 percent discount if the company renews at least 15 licenses before November 15. Usage records show that three licenses have not been used in the past six months. IT recommends renewing 15 licenses and reallocating the remaining budget to staff training.  FINANCE APPROVAL The proposal is approved, provided that the department confirms the three unused licenses can be removed without losing archived project files. Please submit the final license count and training estimate by November 8. Finance will process the renewal after receiving written confirmation from IT. The discount should be listed separately in the purchase request.
- IT PROPOSAL: The design department currently uses 18 licenses of the StudioPro application. The annual subscription expires on November 30. The vendor has offered a 12 percent discount if the company renews at least 15 licenses before November 15. Usage records show that three licenses have not been used in the past six months. IT recommends renewing 15 licenses and reallocating the remaining budget to staff training.
- FINANCE APPROVAL: The proposal is approved, provided that the department confirms the three unused licenses can be removed without losing archived project files. Please submit the final license count and training estimate by November 8. Finance will process the renewal after receiving written confirmation from IT. The discount should be listed separately in the purchase request.

**Q1. How many licenses does the department currently use?**

- Choices: A. 12<br>B. 15<br>C. 21<br>**D. 18**
- Current keyed answer: **D. 18**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): IT PROPOSAL — uses 18 licenses — Thông tin trong tài liệu cho biết: Bộ phận hiện sử dụng 18 giấy phép.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: IT PROPOSAL — uses 18 licenses
- Current explanation: Thông tin trong tài liệu cho biết: Bộ phận hiện sử dụng 18 giấy phép.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why does IT recommend renewing fewer licenses?**

- Choices: **A. Three licenses have been unused**<br>B. The vendor discontinued the product<br>C. The discount is unavailable<br>D. The department is closing
- Current keyed answer: **A. Three licenses have been unused**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): IT PROPOSAL — three licenses have not been used — Có ba giấy phép không được sử dụng trong sáu tháng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: IT PROPOSAL — three licenses have not been used
- Current explanation: Có ba giấy phép không được sử dụng trong sáu tháng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What condition must be confirmed?**

- Choices: A. Training can be canceled<br>**B. Archived files will remain accessible**<br>C. The subscription can be transferred<br>D. The vendor will change its price
- Current keyed answer: **B. Archived files will remain accessible**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): FINANCE APPROVAL — without losing archived project files — Finance yêu cầu xác nhận có thể bỏ ba license mà không mất tệp dự án lưu trữ.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: FINANCE APPROVAL — without losing archived project files
- Current explanation: Finance yêu cầu xác nhận có thể bỏ ba license mà không mất tệp dự án lưu trữ.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q4. By when should the final count be submitted?**

- Choices: A. November 15<br>B. November 30<br>**C. November 8**<br>D. December 8
- Current keyed answer: **C. November 8**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): FINANCE APPROVAL — by November 8 — Hạn nộp số lượng cuối cùng là ngày 8 tháng 11.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: FINANCE APPROVAL — by November 8
- Current explanation: Hạn nộp số lượng cuối cùng là ngày 8 tháng 11.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q5. When will Finance process the renewal?**

- Choices: A. Immediately after the proposal<br>B. At the end of December<br>C. Before the license count is known<br>**D. After written IT confirmation**
- Current keyed answer: **D. After written IT confirmation**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (DOUBLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): FINANCE APPROVAL — after receiving written confirmation from IT — Finance xử lý sau khi nhận xác nhận bằng văn bản từ IT.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: FINANCE APPROVAL — after receiving written confirmation from IT
- Current explanation: Finance xử lý sau khi nhận xác nhận bằng văn bản từ IT.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-schedule-email` · Revised customer-support schedule

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: Hello team, Beginning next Monday, the customer-support desk will open at 7:30 a.m. instead of 8:00 a.m. to cover early inquiries from overseas clients. The afternoon shift will end at 4:30 p.m., and the rotating lunch schedule remains unchanged. Employees who cannot work the revised hours should contact Jordan in Human Resources by Thursday. The updated roster will be posted on the internal portal Friday afternoon. Please review your assigned hours before the weekend.

**Q1. When will the revised schedule begin?**

- Choices: **A. Next Monday**<br>B. This Friday<br>C. Next Thursday<br>D. At the end of the month
- Current keyed answer: **A. Next Monday**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — Beginning next Monday — Lịch mới bắt đầu từ thứ Hai tuần tới.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — Beginning next Monday
- Current explanation: Lịch mới bắt đầu từ thứ Hai tuần tới.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why will the desk open earlier?**

- Choices: A. To train new staff<br>**B. To cover overseas client inquiries**<br>C. To reduce lunch breaks<br>D. To prepare the roster
- Current keyed answer: **B. To cover overseas client inquiries**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — to cover early inquiries from overseas clients — Giờ mở cửa sớm hơn để hỗ trợ khách quốc tế.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — to cover early inquiries from overseas clients
- Current explanation: Giờ mở cửa sớm hơn để hỗ trợ khách quốc tế.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should employees do by Thursday?**

- Choices: A. Review the portal<br>B. Change their lunch break<br>**C. Contact HR if unable to work the new hours**<br>D. Submit a customer report
- Current keyed answer: **C. Contact HR if unable to work the new hours**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: KEY_UNUSUALLY_LONG)
- Rationale (`rationale`): SINGLE PASSAGE — contact Jordan in Human Resources by Thursday — Nhân viên không thể làm theo giờ mới cần liên hệ HR trước thứ Năm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — contact Jordan in Human Resources by Thursday
- Current explanation: Nhân viên không thể làm theo giờ mới cần liên hệ HR trước thứ Năm.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-room-ad` · Conference room booking advertisement

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: Need a quiet space for a client presentation? The Riverside Business Center offers four meeting rooms with video conferencing, whiteboards, and complimentary Wi-Fi. Small rooms accommodate up to six guests, while the largest room seats twenty. Bookings made at least three days in advance receive a ten-percent discount. Catering is available by request, but orders must be placed before 5 p.m. on the previous business day. Call the reception desk to check availability. The center also provides a projector at no extra charge, and its staff can help arrange seating before the event.

**Q1. What service is being advertised?**

- Choices: A. Office furniture sales<br>B. Video equipment repairs<br>C. Catering delivery only<br>**D. Meeting room rentals**
- Current keyed answer: **D. Meeting room rentals**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — offers four meeting rooms — Trung tâm cho thuê phòng họp.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — offers four meeting rooms
- Current explanation: Trung tâm cho thuê phòng họp.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. How many people can the largest room accommodate?**

- Choices: **A. Twenty**<br>B. Ten<br>C. Twelve<br>D. Six
- Current keyed answer: **A. Twenty**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — largest room seats twenty — Phòng lớn nhất có sức chứa 20 người.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — largest room seats twenty
- Current explanation: Phòng lớn nhất có sức chứa 20 người.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. How can customers receive a discount?**

- Choices: A. Pay in cash<br>**B. Book three days in advance**<br>C. Order catering<br>D. Book after 5 p.m.
- Current keyed answer: **B. Book three days in advance**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — at least three days in advance receive a ten-percent discount — Đặt trước ít nhất ba ngày được giảm giá.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — at least three days in advance receive a ten-percent discount
- Current explanation: Đặt trước ít nhất ba ngày được giảm giá.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-cafeteria-notice` · Cafeteria service notice

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: The company cafeteria will close at 2 p.m. on Thursday for a scheduled deep cleaning. Lunch service will be available from 11 a.m. to 1:30 p.m., and the coffee station will remain open until noon. Employees may use the vending area on the first floor after the cafeteria closes. The regular cafeteria schedule will resume on Friday. Please remove personal items from the tables before leaving. The cleaning contractor will place signs near the elevators to direct employees to the alternative facilities.

**Q1. Why will the cafeteria close early?**

- Choices: A. A staff meeting<br>B. A menu change<br>**C. Deep cleaning**<br>D. Equipment delivery
- Current keyed answer: **C. Deep cleaning**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — scheduled deep cleaning — Căng tin đóng cửa để vệ sinh tổng thể.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — scheduled deep cleaning
- Current explanation: Căng tin đóng cửa để vệ sinh tổng thể.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Until what time is lunch served?**

- Choices: A. Noon<br>B. 1 p.m.<br>C. 2 p.m.<br>**D. 1:30 p.m.**
- Current keyed answer: **D. 1:30 p.m.**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — from 11 a.m. to 1:30 p.m. — Bữa trưa được phục vụ đến 13 giờ 30.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — from 11 a.m. to 1:30 p.m.
- Current explanation: Bữa trưa được phục vụ đến 13 giờ 30.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What can employees use after the cafeteria closes?**

- Choices: **A. The vending area**<br>B. The coffee station all day<br>C. The second-floor kitchen<br>D. The meeting room
- Current keyed answer: **A. The vending area**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — use the vending area on the first floor after the cafeteria closes — Khu máy bán hàng được dùng sau khi căng tin đóng cửa.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — use the vending area on the first floor after the cafeteria closes
- Current explanation: Khu máy bán hàng được dùng sau khi căng tin đóng cửa.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-interview-memo` · Interview arrangements for a technician position

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: The facilities department will interview three candidates for the maintenance technician position next Wednesday. Each interview will last thirty minutes and take place in Room 204. Candidates should bring a copy of their certification and a list of previous projects. The hiring panel includes the facilities supervisor and two senior technicians. HR will send parking instructions to candidates who confirm attendance by Monday afternoon. Applicants who need to change their appointment should reply to the invitation rather than call the facilities desk.

**Q1. How many candidates will be interviewed?**

- Choices: A. Two<br>**B. Three**<br>C. Four<br>D. Five
- Current keyed answer: **B. Three**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — interview three candidates — Bản ghi nêu có ba ứng viên sẽ được phỏng vấn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — interview three candidates
- Current explanation: Bản ghi nêu có ba ứng viên sẽ được phỏng vấn.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. What should candidates bring?**

- Choices: A. A laptop and invoice<br>B. A passport and photo<br>**C. Certification and project list**<br>D. A reference letter only
- Current keyed answer: **C. Certification and project list**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — bring a copy of their certification and a list of previous projects — Ứng viên cần mang chứng chỉ và danh sách dự án.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — bring a copy of their certification and a list of previous projects
- Current explanation: Ứng viên cần mang chứng chỉ và danh sách dự án.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When will parking instructions be sent?**

- Choices: A. After the interview<br>B. To all applicants immediately<br>C. On Wednesday morning<br>**D. To those confirming by Monday afternoon**
- Current keyed answer: **D. To those confirming by Monday afternoon**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — confirm attendance by Monday afternoon — HR gửi hướng dẫn đỗ xe cho người xác nhận trước chiều thứ Hai.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — confirm attendance by Monday afternoon
- Current explanation: HR gửi hướng dẫn đỗ xe cho người xác nhận trước chiều thứ Hai.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-shipment-email` · Shipment tracking update

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: Dear Ms. Tran, Your order of display stands has left our central warehouse and is scheduled to arrive at your store on Tuesday, October 14. The carrier will call approximately one hour before delivery. Please ensure that the loading area is clear and that a staff member is available to sign the receipt. If the delivery address has changed, notify our logistics desk before 4 p.m. today. Tracking details are available in your account.

**Q1. What has already happened to the order?**

- Choices: **A. It left the central warehouse**<br>B. It was returned<br>C. It was installed<br>D. It was canceled
- Current keyed answer: **A. It left the central warehouse**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — has left our central warehouse — Đơn hàng đã được gửi khỏi kho trung tâm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — has left our central warehouse
- Current explanation: Đơn hàng đã được gửi khỏi kho trung tâm.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When will the order arrive?**

- Choices: A. Monday, October 13<br>**B. Tuesday, October 14**<br>C. Wednesday, October 15<br>D. Friday, October 17
- Current keyed answer: **B. Tuesday, October 14**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — arrive at your store on Tuesday, October 14 — Đơn hàng được lên lịch giao vào thứ Ba, ngày 14 tháng 10.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — arrive at your store on Tuesday, October 14
- Current explanation: Đơn hàng được lên lịch giao vào thứ Ba, ngày 14 tháng 10.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. What should the recipient ensure?**

- Choices: A. The stands are assembled<br>B. The store is closed<br>**C. A staff member can sign**<br>D. The address is removed
- Current keyed answer: **C. A staff member can sign**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — a staff member is available to sign the receipt — Người nhận cần bố trí người ký xác nhận nhận hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — a staff member is available to sign the receipt
- Current explanation: Người nhận cần bố trí người ký xác nhận nhận hàng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-award-news` · Employee recognition announcement

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: Congratulations to the customer-service team for receiving this quarter’s service award. The team reduced average response time by 18 percent while maintaining its customer satisfaction rating. The award will be presented during the monthly staff meeting on November 6. Team members who work at the regional office may join by video conference. The department director thanked employees for sharing updated response templates and coordinating their schedules during the busy period. A short summary of the team’s improvement will appear in the internal newsletter later this month.

**Q1. Why did the team receive the award?**

- Choices: A. It hired more staff<br>B. It reduced its service hours<br>C. It opened a new office<br>**D. It improved response time while maintaining satisfaction**
- Current keyed answer: **D. It improved response time while maintaining satisfaction**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — reduced average response time by 18 percent while maintaining its customer satisfaction rating — Đội đã giảm thời gian phản hồi và giữ mức hài lòng của khách hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — reduced average response time by 18 percent while maintaining its customer satisfaction rating
- Current explanation: Đội đã giảm thời gian phản hồi và giữ mức hài lòng của khách hàng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When will the award be presented?**

- Choices: **A. November 6**<br>B. November 16<br>C. December 6<br>D. October 6
- Current keyed answer: **A. November 6**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — monthly staff meeting on November 6 — Giải được trao trong cuộc họp nhân viên ngày 6 tháng 11.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — monthly staff meeting on November 6
- Current explanation: Giải được trao trong cuộc họp nhân viên ngày 6 tháng 11.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. How can regional-office employees attend?**

- Choices: A. By phone only<br>**B. By video conference**<br>C. In person at headquarters<br>D. They cannot attend
- Current keyed answer: **B. By video conference**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — may join by video conference — Nhân viên văn phòng vùng có thể tham dự qua video.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — may join by video conference
- Current explanation: Nhân viên văn phòng vùng có thể tham dự qua video.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-payment-terms` · Updated payment terms

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: Starting with orders placed in January, business customers may choose either a thirty-day invoice or a discounted prepaid option. The discount applies only when payment is received before the order is shipped. Customers who select the invoice option will receive a reminder five days before the due date. Questions about account balances should be directed to the billing team rather than the sales representative. Account statements can be downloaded from the customer portal, and billing inquiries are answered on business days.

**Q1. When does the new policy begin?**

- Choices: A. In December<br>B. In March<br>**C. In January**<br>D. Immediately
- Current keyed answer: **C. In January**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — Starting with orders placed in January — Chính sách mới được áp dụng cho đơn đặt hàng từ tháng Một.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — Starting with orders placed in January
- Current explanation: Chính sách mới được áp dụng cho đơn đặt hàng từ tháng Một.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. When is the prepaid discount applied?**

- Choices: A. After shipment<br>B. Only after a reminder<br>C. At the end of the month<br>**D. When payment arrives before shipment**
- Current keyed answer: **D. When payment arrives before shipment**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — payment is received before the order is shipped — Chiết khấu được áp dụng khi thanh toán đến trước lúc giao hàng.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — payment is received before the order is shipped
- Current explanation: Chiết khấu được áp dụng khi thanh toán đến trước lúc giao hàng.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. Who should customers contact about account balances?**

- Choices: **A. The billing team**<br>B. The warehouse<br>C. The sales representative<br>D. The shipping driver
- Current keyed answer: **A. The billing team**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — directed to the billing team — Câu hỏi về số dư cần gửi đến nhóm billing.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — directed to the billing team
- Current explanation: Câu hỏi về số dư cần gửi đến nhóm billing.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `batch026-part7-travel-change` · Conference travel update

- Document type: SINGLE PASSAGE · Status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Passage: Due to a timetable change, the express train to Central City will depart at 7:40 a.m. instead of 8:10 a.m. on Friday. Conference registration opens at 9:30, so travelers should use the earlier service to avoid arriving late. Tickets purchased for the original departure remain valid. The travel coordinator will email the group with platform information on Thursday evening. Travelers should keep the confirmation email available and arrive at the station at least ten minutes early.

**Q1. What has changed?**

- Choices: A. The registration time<br>**B. The train departure time**<br>C. The ticket price<br>D. The conference location
- Current keyed answer: **B. The train departure time**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — will depart at 7:40 a.m. instead of 8:10 a.m. — Thông báo cho biết giờ khởi hành tàu đã thay đổi.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — will depart at 7:40 a.m. instead of 8:10 a.m.
- Current explanation: Thông báo cho biết giờ khởi hành tàu đã thay đổi.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q2. Why should travelers take the earlier train?**

- Choices: A. To meet the coordinator<br>B. To collect tickets<br>**C. To avoid arriving late**<br>D. To visit the station office
- Current keyed answer: **C. To avoid arriving late**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — use the earlier service to avoid arriving late — Chuyến tàu sớm được đề xuất để tránh đến muộn.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — use the earlier service to avoid arriving late
- Current explanation: Chuyến tàu sớm được đề xuất để tránh đến muộn.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

**Q3. When will platform information be emailed?**

- Choices: A. Wednesday morning<br>B. After registration<br>C. Friday at 7:40<br>**D. Thursday evening**
- Current keyed answer: **D. Thursday evening**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Reading Part 7 (SINGLE PASSAGE) passage grounding, cross-document inference, and distractor exclusion
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): SINGLE PASSAGE — email the group with platform information on Thursday evening — Điều phối viên sẽ gửi thông tin sân ga cho nhóm vào tối thứ Năm.
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Evidence reference: SINGLE PASSAGE — email the group with platform information on Thursday evening
- Current explanation: Điều phối viên sẽ gửi thông tin sân ga cho nhóm vào tối thứ Năm.
- Reviewer: [ ] citation supports key  [ ] cross-document reasoning valid  [ ] distractors wrong  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

## C. Separate TOEIC Part 5 sentence-completion reserve

This 80-question bank is separate from Reading Part 5 and must not be counted as Mock-eligible. Check the complete sentence, grammar focus, distractors, translation and every option explanation.

### `p5-sc-001` · Infinitives and Verb Patterns

- Sentence: The HR manager asked all new employees to __________ the orientation form by Friday.
- Choices: **A. complete**<br>B. completion<br>C. completely<br>D. completed
- Current keyed answer: **A. complete**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “to” đứng ngay trước chỗ trống nên chỉ động từ nguyên mẫu “complete” phù hợp; các lựa chọn còn lại là danh từ, trạng từ hoặc quá khứ phân từ. — Verb pattern: ask + object + to-infinitive
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Verb pattern: ask + object + to-infinitive
- Single-answer rationale: “to” đứng ngay trước chỗ trống nên chỉ động từ nguyên mẫu “complete” phù hợp; các lựa chọn còn lại là danh từ, trạng từ hoặc quá khứ phân từ.
- Vietnamese translation: Quản lý nhân sự yêu cầu tất cả nhân viên mới hoàn thành biểu mẫu định hướng trước thứ Sáu.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-002` · Passive Voice

- Sentence: The shipment will be __________ as soon as the customs documents are approved.
- Choices: **A. released**<br>B. release<br>C. releasing<br>D. releases
- Current keyed answer: **A. released**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Passive Voice): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cấu trúc bị động “will be + V3” xác định dạng phân từ; các dạng còn lại không hoàn thành cấu trúc bị động chuẩn. — Passive voice: will be + past participle
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Passive voice: will be + past participle
- Single-answer rationale: Cấu trúc bị động “will be + V3” xác định dạng phân từ; các dạng còn lại không hoàn thành cấu trúc bị động chuẩn.
- Vietnamese translation: Lô hàng sẽ được thông quan/giải phóng ngay khi chứng từ hải quan được phê duyệt.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-003` · Infinitives and Verb Patterns

- Sentence: The interview panel will __________ three finalists for the management position.
- Choices: **A. select**<br>B. selection<br>C. selected<br>D. selecting
- Current keyed answer: **A. select**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “will” là dấu hiệu trực tiếp yêu cầu động từ nguyên mẫu; “selection” là danh từ, “selected” và “selecting” không đúng dạng sau modal. — Modal verb: will + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: will + base form
- Single-answer rationale: “will” là dấu hiệu trực tiếp yêu cầu động từ nguyên mẫu; “selection” là danh từ, “selected” và “selecting” không đúng dạng sau modal.
- Vietnamese translation: Hội đồng phỏng vấn sẽ chọn ba ứng viên cuối cùng cho vị trí quản lý.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-004` · Gerunds and Infinitives

- Sentence: Ms. Patel is responsible for __________ the monthly sales report.
- Choices: A. prepare<br>B. prepares<br>C. prepared<br>**D. preparing**
- Current keyed answer: **D. preparing**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Gerunds and Infinitives): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Giới từ “for” đứng ngay trước chỗ trống buộc dùng dạng V-ing; ba lựa chọn còn lại không phù hợp vị trí này. — Gerund after a preposition: responsible for + V-ing
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Gerund after a preposition: responsible for + V-ing
- Single-answer rationale: Giới từ “for” đứng ngay trước chỗ trống buộc dùng dạng V-ing; ba lựa chọn còn lại không phù hợp vị trí này.
- Vietnamese translation: Bà Patel chịu trách nhiệm chuẩn bị báo cáo doanh số hằng tháng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-005` · Infinitives and Verb Patterns

- Sentence: Only trained technicians are authorized to __________ the equipment.
- Choices: A. operation<br>B. operating<br>C. operated<br>**D. operate**
- Current keyed answer: **D. operate**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cụm cố định “authorized to” đòi hỏi động từ nguyên mẫu; “operation” là danh từ và các dạng còn lại sai hình thái. — Adjective + to-infinitive: authorized to + V1
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective + to-infinitive: authorized to + V1
- Single-answer rationale: Cụm cố định “authorized to” đòi hỏi động từ nguyên mẫu; “operation” là danh từ và các dạng còn lại sai hình thái.
- Vietnamese translation: Chỉ kỹ thuật viên đã qua đào tạo mới được phép vận hành thiết bị.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-006` · Adjectives and Adverbs

- Sentence: Please contact the supplier if you need __________ information about the delivery schedule.
- Choices: **A. additional**<br>B. additionally<br>C. addition<br>D. add
- Current keyed answer: **A. additional**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Từ đứng trước danh từ “information” phải là tính từ; “additionally” là trạng từ, “addition” là danh từ và “add” là động từ. — Adjective before a noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective before a noun
- Single-answer rationale: Từ đứng trước danh từ “information” phải là tính từ; “additionally” là trạng từ, “addition” là danh từ và “add” là động từ.
- Vietnamese translation: Vui lòng liên hệ nhà cung cấp nếu bạn cần thêm thông tin về lịch giao hàng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-007` · Verb Tense and Aspect

- Sentence: The finance director will __________ the budget proposal before approving it.
- Choices: **A. review**<br>B. reviewed<br>C. reviewing<br>D. reviewer
- Current keyed answer: **A. review**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Modal “will” yêu cầu dạng nguyên mẫu; các lựa chọn khác là quá khứ phân từ, V-ing hoặc danh từ chỉ người. — Modal verb: will + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: will + base form
- Single-answer rationale: Modal “will” yêu cầu dạng nguyên mẫu; các lựa chọn khác là quá khứ phân từ, V-ing hoặc danh từ chỉ người.
- Vietnamese translation: Giám đốc tài chính sẽ xem xét đề xuất ngân sách trước khi phê duyệt.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-008` · Word Forms and Nouns

- Sentence: Customers must present the original __________ to request a refund.
- Choices: **A. receipt**<br>B. receive<br>C. receiver<br>D. receptive
- Current keyed answer: **A. receipt**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Ngữ cảnh yêu cầu một chứng từ mua hàng; “receipt” là biên lai. Các lựa chọn còn lại không mang nghĩa chứng từ này. — Noun selection and word meaning
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Noun selection and word meaning
- Single-answer rationale: Ngữ cảnh yêu cầu một chứng từ mua hàng; “receipt” là biên lai. Các lựa chọn còn lại không mang nghĩa chứng từ này.
- Vietnamese translation: Khách hàng phải xuất trình biên lai gốc để yêu cầu hoàn tiền.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-009` · Adjectives and Adverbs

- Sentence: The new attendance policy will become __________ on July 1.
- Choices: **A. effective**<br>B. effect<br>C. effectively<br>D. effects
- Current keyed answer: **A. effective**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Vị trí sau động từ nối “become” cần tính từ; “effective” là tính từ, còn các lựa chọn khác là danh từ hoặc trạng từ. — Linking verb become + adjective
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Linking verb become + adjective
- Single-answer rationale: Vị trí sau động từ nối “become” cần tính từ; “effective” là tính từ, còn các lựa chọn khác là danh từ hoặc trạng từ.
- Vietnamese translation: Chính sách chấm công mới sẽ bắt đầu có hiệu lực vào ngày 1 tháng 7.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-010` · Prepositions and Collocations

- Sentence: The invoice must be paid __________ 30 days of receipt.
- Choices: **A. within**<br>B. among<br>C. across<br>D. between
- Current keyed answer: **A. within**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “within” diễn đạt thời hạn không vượt quá một khoảng thời gian; “between” cần hai mốc, “among” chỉ ở giữa nhiều đối tượng và “across” không dùng theo nghĩa thời hạn này. — Preposition of time: within + time period
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Preposition of time: within + time period
- Single-answer rationale: Chỉ “within” diễn đạt thời hạn không vượt quá một khoảng thời gian; “between” cần hai mốc, “among” chỉ ở giữa nhiều đối tượng và “across” không dùng theo nghĩa thời hạn này.
- Vietnamese translation: Hóa đơn phải được thanh toán trong vòng 30 ngày kể từ ngày nhận.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-011` · Infinitives and Verb Patterns

- Sentence: The company plans to __________ a regional office in Da Nang next year.
- Choices: A. established<br>B. establishment<br>C. establishing<br>**D. establish**
- Current keyed answer: **D. establish**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cấu trúc “plans to + V1” chỉ chấp nhận động từ nguyên mẫu ở chỗ trống; các lựa chọn khác sai dạng. — Verb pattern: plan to + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Verb pattern: plan to + base form
- Single-answer rationale: Cấu trúc “plans to + V1” chỉ chấp nhận động từ nguyên mẫu ở chỗ trống; các lựa chọn khác sai dạng.
- Vietnamese translation: Công ty dự định thành lập một văn phòng khu vực tại Đà Nẵng vào năm tới.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-012` · Infinitives and Verb Patterns

- Sentence: The supplier agreed to __________ the defective printer at no additional cost.
- Choices: A. replacement<br>B. replaced<br>C. replacing<br>**D. replace**
- Current keyed answer: **D. replace**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cụm “agreed to” yêu cầu nguyên mẫu; “replacement” là danh từ, còn “replaced/replacing” không đúng dạng. — Verb pattern: agree to + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Verb pattern: agree to + base form
- Single-answer rationale: Cụm “agreed to” yêu cầu nguyên mẫu; “replacement” là danh từ, còn “replaced/replacing” không đúng dạng.
- Vietnamese translation: Nhà cung cấp đồng ý thay thế máy in bị lỗi mà không tính thêm phí.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-013` · Word Forms and Nouns

- Sentence: The purchase order requires written __________ from the manager.
- Choices: **A. approval**<br>B. approve<br>C. approved<br>D. approving
- Current keyed answer: **A. approval**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cụm “written + noun” yêu cầu danh từ; “approval” là danh từ. “Approve” là động từ, “approved” là phân từ/tính từ và “approving” là V-ing nên không phù hợp. — Noun after a possessive determiner
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Noun after a possessive determiner
- Single-answer rationale: Cụm “written + noun” yêu cầu danh từ; “approval” là danh từ. “Approve” là động từ, “approved” là phân từ/tính từ và “approving” là V-ing nên không phù hợp.
- Vietnamese translation: Đơn đặt hàng yêu cầu phải có sự phê duyệt bằng văn bản từ quản lý.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-014` · Adjectives and Adverbs

- Sentence: The report provides a __________ overview of last quarter’s operating costs.
- Choices: **A. comprehensive**<br>B. comprehensively<br>C. comprehend<br>D. comprehension
- Current keyed answer: **A. comprehensive**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cấu trúc “a + adjective + noun” cần tính từ; ba lựa chọn còn lại lần lượt là trạng từ, động từ và danh từ. — Adjective before a noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective before a noun
- Single-answer rationale: Cấu trúc “a + adjective + noun” cần tính từ; ba lựa chọn còn lại lần lượt là trạng từ, động từ và danh từ.
- Vietnamese translation: Báo cáo cung cấp cái nhìn tổng quan toàn diện về chi phí vận hành của quý trước.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-015` · Verb Tense and Aspect

- Sentence: The HR department will __________ all applications within five business days.
- Choices: **A. process**<br>B. processing<br>C. processed<br>D. processor
- Current keyed answer: **A. process**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Modal “will” xác định dạng động từ nguyên mẫu; các lựa chọn khác là V-ing, quá khứ phân từ hoặc danh từ chỉ thiết bị/người xử lý. — Modal verb: will + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: will + base form
- Single-answer rationale: Modal “will” xác định dạng động từ nguyên mẫu; các lựa chọn khác là V-ing, quá khứ phân từ hoặc danh từ chỉ thiết bị/người xử lý.
- Vietnamese translation: Phòng nhân sự sẽ xử lý tất cả hồ sơ trong vòng năm ngày làm việc.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-016` · Infinitives and Verb Patterns

- Sentence: Applicants are required to __________ two professional references.
- Choices: A. provides<br>B. provided<br>C. providing<br>**D. provide**
- Current keyed answer: **D. provide**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “to” trong cấu trúc “are required to” cần động từ nguyên mẫu; các lựa chọn còn lại không hợp lệ về hình thái. — Passive reporting phrase: be required to + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Passive reporting phrase: be required to + base form
- Single-answer rationale: “to” trong cấu trúc “are required to” cần động từ nguyên mẫu; các lựa chọn còn lại không hợp lệ về hình thái.
- Vietnamese translation: Ứng viên được yêu cầu cung cấp hai người tham chiếu chuyên môn.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-017` · Word Forms and Nouns

- Sentence: The company made a large __________ of office supplies before the relocation.
- Choices: A. purchasing<br>B. purchased<br>C. purchaser<br>**D. purchase**
- Current keyed answer: **D. purchase**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Vị trí sau “a large” cần danh từ số ít; “purchase” là danh từ phù hợp. “Purchaser” chỉ người mua, còn các dạng khác không phù hợp cấu trúc. — Article + adjective + noun / collocation make a purchase
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Article + adjective + noun / collocation make a purchase
- Single-answer rationale: Vị trí sau “a large” cần danh từ số ít; “purchase” là danh từ phù hợp. “Purchaser” chỉ người mua, còn các dạng khác không phù hợp cấu trúc.
- Vietnamese translation: Công ty đã mua một lượng lớn vật dụng văn phòng trước khi chuyển địa điểm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-018` · Infinitives and Verb Patterns

- Sentence: The purchasing department plans to __________ additional laptops before the new employees arrive.
- Choices: **A. order**<br>B. ordering<br>C. ordered<br>D. orders
- Current keyed answer: **A. order**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “to” trong “plans to” yêu cầu động từ nguyên mẫu; ba lựa chọn còn lại là V-ing, quá khứ phân từ hoặc dạng chia ngôi. — Verb pattern: plan to + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Verb pattern: plan to + base form
- Single-answer rationale: “to” trong “plans to” yêu cầu động từ nguyên mẫu; ba lựa chọn còn lại là V-ing, quá khứ phân từ hoặc dạng chia ngôi.
- Vietnamese translation: Phòng mua hàng dự định đặt thêm máy tính xách tay trước khi nhân viên mới đến.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-019` · Imperatives and Verb Forms

- Sentence: Please __________ your expense claims through the employee portal by Friday.
- Choices: A. submission<br>B. submits<br>C. submitted<br>**D. submit**
- Current keyed answer: **D. submit**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Imperatives and Verb Forms): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Câu mệnh lệnh lịch sự bắt đầu bằng “Please” dùng động từ nguyên mẫu; các lựa chọn khác là danh từ hoặc dạng chia động từ. — Imperative sentence: base verb
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Imperative sentence: base verb
- Single-answer rationale: Câu mệnh lệnh lịch sự bắt đầu bằng “Please” dùng động từ nguyên mẫu; các lựa chọn khác là danh từ hoặc dạng chia động từ.
- Vietnamese translation: Vui lòng nộp yêu cầu thanh toán chi phí qua cổng thông tin nhân viên trước thứ Sáu.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-020` · Passive Voice

- Sentence: The revised schedule will be __________ to all department heads tomorrow.
- Choices: A. distributing<br>B. distributes<br>C. distribute<br>**D. distributed**
- Current keyed answer: **D. distributed**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Passive Voice): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “will be” kết hợp với V3 để tạo bị động; “distributed” là quá khứ phân từ của “distribute”. — Passive voice: will be + past participle
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Passive voice: will be + past participle
- Single-answer rationale: “will be” kết hợp với V3 để tạo bị động; “distributed” là quá khứ phân từ của “distribute”.
- Vietnamese translation: Lịch trình đã sửa đổi sẽ được phân phát đến tất cả trưởng bộ phận vào ngày mai.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-021` · Word Forms and Nouns

- Sentence: The company will open a new __________ near the central station.
- Choices: **A. branch**<br>B. branching<br>C. branched<br>D. branches
- Current keyed answer: **A. branch**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Mạo từ “a” và tính từ “new” xác định danh từ đếm được số ít; “branches” là số nhiều, còn “branching/branched” không phù hợp. — Singular count noun after a new
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Singular count noun after a new
- Single-answer rationale: Mạo từ “a” và tính từ “new” xác định danh từ đếm được số ít; “branches” là số nhiều, còn “branching/branched” không phù hợp.
- Vietnamese translation: Công ty sẽ mở một chi nhánh mới gần nhà ga trung tâm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-022` · Word Forms and Nouns

- Sentence: All office __________ must be inspected before the building reopens.
- Choices: A. equipments<br>B. equipped<br>**C. equipment**<br>D. equipping
- Current keyed answer: **C. equipment**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Ngữ cảnh cần danh từ không đếm được “equipment”; “equipments” là dạng số nhiều không chuẩn trong nghĩa chung, còn các lựa chọn khác không phải danh từ phù hợp. — Uncountable noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Uncountable noun
- Single-answer rationale: Ngữ cảnh cần danh từ không đếm được “equipment”; “equipments” là dạng số nhiều không chuẩn trong nghĩa chung, còn các lựa chọn khác không phải danh từ phù hợp.
- Vietnamese translation: Toàn bộ thiết bị văn phòng phải được kiểm tra trước khi tòa nhà mở cửa trở lại.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-023` · Word Forms and Nouns

- Sentence: The revised __________ for next week’s product briefing is posted on the intranet.
- Choices: A. scheduled<br>B. scheduler<br>C. scheduling<br>**D. schedule**
- Current keyed answer: **D. schedule**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Sau mạo từ “the” và tính từ “revised” cần danh từ chỉ lịch; “schedule” đáp ứng cả cấu trúc và nghĩa. “scheduled” là phân từ/tính từ, “scheduling” chỉ quá trình lên lịch, “scheduler” chỉ người/công cụ lập lịch. — Noun as the head of a noun phrase
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Noun as the head of a noun phrase
- Single-answer rationale: Sau mạo từ “the” và tính từ “revised” cần danh từ chỉ lịch; “schedule” đáp ứng cả cấu trúc và nghĩa. “scheduled” là phân từ/tính từ, “scheduling” chỉ quá trình lên lịch, “scheduler” chỉ người/công cụ lập lịch.
- Vietnamese translation: Lịch trình đã chỉnh sửa cho buổi giới thiệu sản phẩm tuần tới được đăng trên mạng nội bộ.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-024` · Modal Verbs

- Sentence: The position will __________ frequent travel to regional offices.
- Choices: **A. require**<br>B. requirement<br>C. required<br>D. requiring
- Current keyed answer: **A. require**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Modal Verbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Modal “will” buộc dùng V1; “requirement” là danh từ, “required” là quá khứ/phân từ, “requiring” là V-ing. — Modal verb: will + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: will + base form
- Single-answer rationale: Modal “will” buộc dùng V1; “requirement” là danh từ, “required” là quá khứ/phân từ, “requiring” là V-ing.
- Vietnamese translation: Vị trí này sẽ yêu cầu đi công tác thường xuyên đến các văn phòng khu vực.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-025` · Adjectives and Adverbs

- Sentence: Conference Room B is not __________ until after 2 p.m.
- Choices: A. availability<br>B. avail<br>C. availably<br>**D. available**
- Current keyed answer: **D. available**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Vị trí sau “is not” yêu cầu tính từ; “available” là tính từ, “availability” là danh từ và “availably” không tự nhiên trong cấu trúc này. — Linking verb be + adjective
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Linking verb be + adjective
- Single-answer rationale: Vị trí sau “is not” yêu cầu tính từ; “available” là tính từ, “availability” là danh từ và “availably” không tự nhiên trong cấu trúc này.
- Vietnamese translation: Phòng họp B sẽ không trống cho đến sau 2 giờ chiều.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-026` · Subject–Verb Agreement

- Sentence: As part of its service policy, the customer service department __________ to all inquiries within one business day.
- Choices: A. response<br>B. responded<br>C. responsive<br>**D. responds**
- Current keyed answer: **D. responds**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cụm “As part of its service policy” xác định hành động thường lệ; “department” là chủ ngữ số ít nên hiện tại đơn cần “responds”. “Response” là danh từ, “responsive” là tính từ, “responded” là quá khứ. — Present simple subject–verb agreement
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Present simple subject–verb agreement
- Single-answer rationale: Cụm “As part of its service policy” xác định hành động thường lệ; “department” là chủ ngữ số ít nên hiện tại đơn cần “responds”. “Response” là danh từ, “responsive” là tính từ, “responded” là quá khứ.
- Vietnamese translation: Theo chính sách dịch vụ, phòng chăm sóc khách hàng phản hồi tất cả yêu cầu trong vòng một ngày làm việc.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-027` · Word Forms and Nouns

- Sentence: Please verify the __________ of each item before signing the delivery receipt.
- Choices: A. quantify<br>B. quantitatively<br>C. quantitative<br>**D. quantity**
- Current keyed answer: **D. quantity**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cấu trúc “the ___ of each item” cần danh từ “quantity”; các lựa chọn còn lại là động từ, tính từ và trạng từ. — Noun after the definite article
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Noun after the definite article
- Single-answer rationale: Cấu trúc “the ___ of each item” cần danh từ “quantity”; các lựa chọn còn lại là động từ, tính từ và trạng từ.
- Vietnamese translation: Vui lòng xác minh số lượng của từng mặt hàng trước khi ký biên nhận giao hàng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-028` · Linking Verbs

- Sentence: The reception desk will __________ open until 8 p.m. during the exhibition.
- Choices: A. remains<br>B. remaining<br>**C. remain**<br>D. remained
- Current keyed answer: **C. remain**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Linking Verbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “will” yêu cầu nguyên mẫu “remain”; ba dạng còn lại không đứng trực tiếp sau modal này. — Modal verb: will + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: will + base form
- Single-answer rationale: “will” yêu cầu nguyên mẫu “remain”; ba dạng còn lại không đứng trực tiếp sau modal này.
- Vietnamese translation: Quầy lễ tân sẽ tiếp tục mở cửa đến 8 giờ tối trong thời gian triển lãm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-029` · Modal Verbs

- Sentence: Staff members must __________ each customer’s identity before changing account details.
- Choices: A. verification<br>B. verified<br>**C. verify**<br>D. verifying
- Current keyed answer: **C. verify**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Modal Verbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Sau modal “must” chỉ dùng động từ nguyên mẫu “verify”; danh từ và các dạng phân từ không phù hợp. — Modal verb: must + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: must + base form
- Single-answer rationale: Sau modal “must” chỉ dùng động từ nguyên mẫu “verify”; danh từ và các dạng phân từ không phù hợp.
- Vietnamese translation: Nhân viên phải xác minh danh tính từng khách hàng trước khi thay đổi thông tin tài khoản.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-030` · Articles and Determiners

- Sentence: Please attach a copy of the __________ to your reimbursement request.
- Choices: A. invoicing<br>B. invoiced<br>**C. invoice**<br>D. invoicer
- Current keyed answer: **C. invoice**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Articles and Determiners): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Sau “the” trong cụm “the ___” cần danh từ chỉ chứng từ; “invoice” là hóa đơn. — Noun after the definite article
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Noun after the definite article
- Single-answer rationale: Sau “the” trong cụm “the ___” cần danh từ chỉ chứng từ; “invoice” là hóa đơn.
- Vietnamese translation: Vui lòng đính kèm một bản sao hóa đơn vào yêu cầu hoàn tiền của bạn.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-031` · Word Forms and Nouns

- Sentence: The hiring manager received more than 200 __________ for the position.
- Choices: A. applicant<br>**B. applications**<br>C. apply<br>D. applying
- Current keyed answer: **B. applications**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Số lượng lớn hơn một yêu cầu danh từ đếm được số nhiều; “applications” là danh từ chỉ hồ sơ, còn các lựa chọn khác sai từ loại hoặc số. — Plural count noun after a number
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Plural count noun after a number
- Single-answer rationale: Số lượng lớn hơn một yêu cầu danh từ đếm được số nhiều; “applications” là danh từ chỉ hồ sơ, còn các lựa chọn khác sai từ loại hoặc số.
- Vietnamese translation: Quản lý tuyển dụng đã nhận hơn 200 hồ sơ cho vị trí này.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-032` · Word Forms and Nouns

- Sentence: The successful __________ will be notified by email next week.
- Choices: A. candidacy<br>**B. candidate**<br>C. candid<br>D. candidly
- Current keyed answer: **B. candidate**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Vị trí sau tính từ “successful” cần danh từ chỉ người; các lựa chọn còn lại là danh từ trừu tượng, tính từ hoặc trạng từ. — Adjective + singular count noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective + singular count noun
- Single-answer rationale: Vị trí sau tính từ “successful” cần danh từ chỉ người; các lựa chọn còn lại là danh từ trừu tượng, tính từ hoặc trạng từ.
- Vietnamese translation: Ứng viên thành công sẽ được thông báo qua email vào tuần tới.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-033` · Word Forms and Nouns

- Sentence: The new store __________, Ms. Ortiz, will approve the staff schedule before it is posted.
- Choices: A. manage<br>B. management<br>**C. manager**<br>D. managerial
- Current keyed answer: **C. manager**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Word Forms and Nouns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Tên người “Ms. Ortiz” ở vị trí đồng vị xác định chỗ trống phải là danh từ chỉ người. “Management” là hoạt động/bộ phận quản lý, không chỉ một cá nhân; các lựa chọn còn lại không phải danh từ chỉ người. — Compound noun: noun modifier + noun head
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Compound noun: noun modifier + noun head
- Single-answer rationale: Tên người “Ms. Ortiz” ở vị trí đồng vị xác định chỗ trống phải là danh từ chỉ người. “Management” là hoạt động/bộ phận quản lý, không chỉ một cá nhân; các lựa chọn còn lại không phải danh từ chỉ người.
- Vietnamese translation: Quản lý cửa hàng mới, bà Ortiz, sẽ phê duyệt lịch làm việc của nhân viên trước khi lịch được đăng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-034` · Articles and Determiners

- Sentence: The carrier confirmed that the replacement parts would be sent in a single __________.
- Choices: A. shipper<br>**B. shipment**<br>C. shipping<br>D. ships
- Current keyed answer: **B. shipment**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Articles and Determiners): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cụm “a single + singular count noun” yêu cầu danh từ đếm được số ít chỉ lô hàng. “Shipment” đúng nghĩa; “shipping” là hoạt động vận chuyển, “shipper” là người/đơn vị gửi và “ships” là dạng số nhiều của “ship”. — Article + adjective + singular count noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Article + adjective + singular count noun
- Single-answer rationale: Cụm “a single + singular count noun” yêu cầu danh từ đếm được số ít chỉ lô hàng. “Shipment” đúng nghĩa; “shipping” là hoạt động vận chuyển, “shipper” là người/đơn vị gửi và “ships” là dạng số nhiều của “ship”.
- Vietnamese translation: Đơn vị vận chuyển xác nhận các phụ tùng thay thế sẽ được gửi trong một lô hàng duy nhất.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-035` · Verb Tense and Aspect

- Sentence: The technician will __________ the air-conditioning system before the office opens.
- Choices: A. inspection<br>B. inspected<br>C. inspecting<br>**D. inspect**
- Current keyed answer: **D. inspect**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Modal “will” yêu cầu V1; “inspection” là danh từ, “inspected” là quá khứ/phân từ và “inspecting” là V-ing. — Modal verb: will + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb: will + base form
- Single-answer rationale: Modal “will” yêu cầu V1; “inspection” là danh từ, “inspected” là quá khứ/phân từ và “inspecting” là V-ing.
- Vietnamese translation: Kỹ thuật viên sẽ kiểm tra hệ thống điều hòa trước khi văn phòng mở cửa.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-036` · Verb Tense and Aspect

- Sentence: The board __________ the revised travel budget at yesterday’s meeting.
- Choices: A. approves<br>B. approval<br>**C. approved**<br>D. approving
- Current keyed answer: **C. approved**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “approved” phù hợp với chủ ngữ “The board” và mốc thời gian “yesterday”; các lựa chọn còn lại sai loại từ hoặc sai dạng thì. — Past simple with a completed past-time marker
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Past simple with a completed past-time marker
- Single-answer rationale: Chỉ “approved” phù hợp với chủ ngữ “The board” và mốc thời gian “yesterday”; các lựa chọn còn lại sai loại từ hoặc sai dạng thì.
- Vietnamese translation: Hội đồng đã phê duyệt ngân sách đi lại sửa đổi tại cuộc họp ngày hôm qua.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-037` · Verb Tense and Aspect

- Sentence: By 8 a.m. tomorrow, the reception team __________ all transportation arrangements for the visiting delegates.
- Choices: **A. will have arranged**<br>B. had arranged<br>C. will arranging<br>D. has arranged
- Current keyed answer: **A. will have arranged**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “will have arranged” thể hiện đúng hành động hoàn tất trước mốc 8 giờ sáng ngày mai. — Future perfect with “by” + future time
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Future perfect with “by” + future time
- Single-answer rationale: Chỉ “will have arranged” thể hiện đúng hành động hoàn tất trước mốc 8 giờ sáng ngày mai.
- Vietnamese translation: Trước 8 giờ sáng ngày mai, nhóm lễ tân sẽ hoàn tất mọi sắp xếp phương tiện đi lại cho các đại biểu đến thăm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-038` · Infinitives and Verb Patterns

- Sentence: The policy requires the finance director to __________ any refund exceeding $500.
- Choices: A. authorization<br>**B. authorize**<br>C. authorizing<br>D. authorized
- Current keyed answer: **B. authorize**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Sau “the finance director to” cần động từ nguyên mẫu “authorize”; các đáp án khác không tạo được cấu trúc đúng. — Require + object + to-infinitive
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Require + object + to-infinitive
- Single-answer rationale: Sau “the finance director to” cần động từ nguyên mẫu “authorize”; các đáp án khác không tạo được cấu trúc đúng.
- Vietnamese translation: Chính sách yêu cầu giám đốc tài chính phê duyệt mọi khoản hoàn tiền vượt quá 500 đô la.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-039` · Subject–Verb Agreement

- Sentence: The accounting department __________ the monthly depreciation expense at the end of each quarter.
- Choices: A. calculate<br>B. calculating<br>**C. calculates**<br>D. calculation
- Current keyed answer: **C. calculates**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chủ ngữ trung tâm là “department” số ít; chỉ “calculates” hòa hợp về chủ-vị và đúng chức năng động từ. — Singular collective/department noun + present simple verb
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Singular collective/department noun + present simple verb
- Single-answer rationale: Chủ ngữ trung tâm là “department” số ít; chỉ “calculates” hòa hợp về chủ-vị và đúng chức năng động từ.
- Vietnamese translation: Phòng kế toán tính chi phí khấu hao hằng tháng vào cuối mỗi quý.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-040` · Verb Tense and Aspect

- Sentence: Because of the severe weather alert, the airline has __________ all evening flights.
- Choices: A. cancel<br>B. cancelling<br>C. cancels<br>**D. canceled**
- Current keyed answer: **D. canceled**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Sau “has” chỉ dạng phân từ “canceled” phù hợp; ba dạng còn lại không thể đi sau trợ động từ này. — Present perfect: has + past participle
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Present perfect: has + past participle
- Single-answer rationale: Sau “has” chỉ dạng phân từ “canceled” phù hợp; ba dạng còn lại không thể đi sau trợ động từ này.
- Vietnamese translation: Do cảnh báo thời tiết khắc nghiệt, hãng hàng không đã hủy tất cả các chuyến bay buổi tối.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-041` · Infinitives and Verb Patterns

- Sentence: The revised instructions were issued to __________ the procedure for submitting travel claims.
- Choices: A. clarification<br>B. clarifying<br>**C. clarify**<br>D. clarified
- Current keyed answer: **C. clarify**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Vị trí sau “to” chỉ mục đích cần động từ nguyên mẫu “clarify”; danh từ, V-ing và quá khứ phân từ đều không phù hợp. — To-infinitive of purpose
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: To-infinitive of purpose
- Single-answer rationale: Vị trí sau “to” chỉ mục đích cần động từ nguyên mẫu “clarify”; danh từ, V-ing và quá khứ phân từ đều không phù hợp.
- Vietnamese translation: Hướng dẫn sửa đổi được ban hành nhằm làm rõ quy trình nộp yêu cầu thanh toán công tác phí.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-042` · Infinitives and Verb Patterns

- Sentence: Please contact the supplier with the specific purpose of __________ the delivery date before arranging the installation.
- Choices: A. confirm<br>B. confirmation<br>C. confirmed<br>**D. confirming**
- Current keyed answer: **D. confirming**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cấu trúc cố định “purpose of + V-ing” chỉ chấp nhận danh động từ sau “of”; do đó “confirming” là đáp án duy nhất. — Preposition + gerund: purpose of + V-ing
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Preposition + gerund: purpose of + V-ing
- Single-answer rationale: Cấu trúc cố định “purpose of + V-ing” chỉ chấp nhận danh động từ sau “of”; do đó “confirming” là đáp án duy nhất.
- Vietnamese translation: Vui lòng liên hệ nhà cung cấp với mục đích cụ thể là xác nhận ngày giao hàng trước khi sắp xếp việc lắp đặt.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-043` · Gerunds and Infinitives

- Sentence: The committee is considering __________ the application deadline by one week.
- Choices: A. extend<br>B. extension<br>**C. extending**<br>D. extended
- Current keyed answer: **C. extending**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Gerunds and Infinitives): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “extending” tạo đúng mẫu “consider + V-ing” và phù hợp nghĩa gia hạn thời hạn nộp đơn. — Consider + gerund
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Consider + gerund
- Single-answer rationale: Chỉ “extending” tạo đúng mẫu “consider + V-ing” và phù hợp nghĩa gia hạn thời hạn nộp đơn.
- Vietnamese translation: Ủy ban đang cân nhắc gia hạn thời hạn nộp đơn thêm một tuần.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-044` · Verb Tense and Aspect

- Sentence: By 5 p.m. yesterday, the courier __________ all urgent documents to the head office.
- Choices: A. has delivered<br>**B. had delivered**<br>C. delivers<br>D. delivering
- Current keyed answer: **B. had delivered**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “had delivered” diễn tả đúng quan hệ thời gian trước-mốc-quá-khứ; hiện tại hoàn thành, hiện tại đơn và V-ing đều sai. — Past perfect with a past reference point
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Past perfect with a past reference point
- Single-answer rationale: Chỉ “had delivered” diễn tả đúng quan hệ thời gian trước-mốc-quá-khứ; hiện tại hoàn thành, hiện tại đơn và V-ing đều sai.
- Vietnamese translation: Đến 5 giờ chiều hôm qua, nhân viên chuyển phát đã giao toàn bộ tài liệu khẩn đến trụ sở chính.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-045` · Verb Tense and Aspect

- Sentence: The company __________ a new customer portal since January, and development is still ongoing.
- Choices: A. developed<br>B. has developed<br>**C. has been developing**<br>D. is develop
- Current keyed answer: **C. has been developing**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Verb Tense and Aspect): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Has been developing” là lựa chọn duy nhất diễn tả rõ quá trình liên tục còn đang diễn ra; “has developed” thiên về kết quả hoàn tất. — Present perfect continuous with “since”
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Present perfect continuous with “since”
- Single-answer rationale: “Has been developing” là lựa chọn duy nhất diễn tả rõ quá trình liên tục còn đang diễn ra; “has developed” thiên về kết quả hoàn tất.
- Vietnamese translation: Công ty đã và đang phát triển một cổng thông tin khách hàng mới kể từ tháng Một, và việc phát triển vẫn đang tiếp tục.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-046` · Subject–Verb Agreement

- Sentence: Neither the sales manager nor the assistants __________ the product demonstration schedule.
- Choices: A. coordinates<br>B. coordination<br>**C. coordinate**<br>D. coordinating
- Current keyed answer: **C. coordinate**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chủ ngữ gần động từ nhất là “assistants”, vì vậy dùng “coordinate”, không thêm -s. — Neither…nor: agreement with the nearer subject
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Neither…nor: agreement with the nearer subject
- Single-answer rationale: Chủ ngữ gần động từ nhất là “assistants”, vì vậy dùng “coordinate”, không thêm -s.
- Vietnamese translation: Cả quản lý bán hàng lẫn các trợ lý đều không điều phối lịch trình buổi giới thiệu sản phẩm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-047` · Subject–Verb Agreement

- Sentence: The number of online orders __________ by 12 percent in October.
- Choices: A. increase<br>**B. increased**<br>C. increasing<br>D. increases
- Current keyed answer: **B. increased**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Increased” vừa hòa hợp với chủ ngữ số ít ở dạng quá khứ, vừa phù hợp mốc thời gian quá khứ. — “The number of” + plural noun takes a singular verb
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: “The number of” + plural noun takes a singular verb
- Single-answer rationale: “Increased” vừa hòa hợp với chủ ngữ số ít ở dạng quá khứ, vừa phù hợp mốc thời gian quá khứ.
- Vietnamese translation: Số lượng đơn đặt hàng trực tuyến đã tăng 12% trong tháng Mười.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-048` · Subject–Verb Agreement

- Sentence: The new safety procedures __________ to a reduction in workplace accidents.
- Choices: A. contributes<br>B. contribution<br>C. contributing<br>**D. contribute**
- Current keyed answer: **D. contribute**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “contribute” hòa hợp với chủ ngữ số nhiều và tạo được kết hợp “contribute to a reduction”. — Plural subject + base-form present simple verb
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Plural subject + base-form present simple verb
- Single-answer rationale: Chỉ “contribute” hòa hợp với chủ ngữ số nhiều và tạo được kết hợp “contribute to a reduction”.
- Vietnamese translation: Các quy trình an toàn mới góp phần làm giảm tai nạn tại nơi làm việc.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-049` · Subject–Verb Agreement

- Sentence: The updated software __________ each scanned receipt into a searchable PDF.
- Choices: **A. converts**<br>B. convert<br>C. conversion<br>D. converting
- Current keyed answer: **A. converts**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Converts” là lựa chọn duy nhất vừa hòa hợp với chủ ngữ số ít vừa hoàn chỉnh cấu trúc “convert A into B”. — Singular uncountable subject + present simple -s
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Singular uncountable subject + present simple -s
- Single-answer rationale: “Converts” là lựa chọn duy nhất vừa hòa hợp với chủ ngữ số ít vừa hoàn chỉnh cấu trúc “convert A into B”.
- Vietnamese translation: Phần mềm được cập nhật chuyển mỗi biên lai đã quét thành một tệp PDF có thể tìm kiếm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-050` · Subject–Verb Agreement

- Sentence: The contract __________ which party is responsible for customs fees.
- Choices: A. specify<br>B. specification<br>**C. specifies**<br>D. specifying
- Current keyed answer: **C. specifies**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Subject–Verb Agreement): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Specifies” là dạng duy nhất phù hợp với chủ ngữ số ít và vị trí động từ chính. — Singular subject in present simple
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Singular subject in present simple
- Single-answer rationale: “Specifies” là dạng duy nhất phù hợp với chủ ngữ số ít và vị trí động từ chính.
- Vietnamese translation: Hợp đồng nêu rõ bên nào chịu trách nhiệm thanh toán phí hải quan.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-051` · Passive Voice

- Sentence: Customer complaints should be __________ promptly and documented in the service log.
- Choices: A. handling<br>**B. handled**<br>C. handle<br>D. handler
- Current keyed answer: **B. handled**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Passive Voice): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ quá khứ phân từ “handled” hoàn thành cấu trúc bị động sau “should be”. — Modal + be + past participle
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal + be + past participle
- Single-answer rationale: Chỉ quá khứ phân từ “handled” hoàn thành cấu trúc bị động sau “should be”.
- Vietnamese translation: Khiếu nại của khách hàng cần được xử lý kịp thời và ghi lại trong nhật ký dịch vụ.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-052` · Passive Voice

- Sentence: The customer database __________ automatically every night by the system.
- Choices: A. updates<br>**B. is updated**<br>C. is updating<br>D. has update
- Current keyed answer: **B. is updated**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Passive Voice): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Is updated” là lựa chọn duy nhất vừa đúng bị động vừa đúng thì hiện tại đơn của một tác vụ lặp lại. — Present simple passive for routine system actions
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Present simple passive for routine system actions
- Single-answer rationale: “Is updated” là lựa chọn duy nhất vừa đúng bị động vừa đúng thì hiện tại đơn của một tác vụ lặp lại.
- Vietnamese translation: Cơ sở dữ liệu khách hàng được hệ thống tự động cập nhật mỗi đêm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-053` · Passive Voice

- Sentence: The remaining funds were __________ to the reserve account on Friday.
- Choices: A. transferring<br>B. transfer<br>**C. transferred**<br>D. transfers
- Current keyed answer: **C. transferred**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Passive Voice): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “transferred” tạo đúng cấu trúc “were + past participle”. — Past simple passive: was/were + past participle
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Past simple passive: was/were + past participle
- Single-answer rationale: Chỉ “transferred” tạo đúng cấu trúc “were + past participle”.
- Vietnamese translation: Khoản tiền còn lại đã được chuyển vào tài khoản dự phòng vào thứ Sáu.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-054` · Adjectives and Adverbs

- Sentence: The current storage area is not __________ for the additional inventory.
- Choices: A. adequacy<br>**B. adequate**<br>C. adequately<br>D. adequateness
- Current keyed answer: **B. adequate**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ tính từ “adequate” phù hợp sau “is” và kết hợp đúng với giới từ “for”. — Linking verb + adjective; adequate for
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Linking verb + adjective; adequate for
- Single-answer rationale: Chỉ tính từ “adequate” phù hợp sau “is” và kết hợp đúng với giới từ “for”.
- Vietnamese translation: Khu vực lưu trữ hiện tại không đủ chỗ cho lượng hàng tồn kho bổ sung.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-055` · Prepositions and Collocations

- Sentence: The training room is adjacent __________ the main conference hall.
- Choices: A. with<br>B. at<br>**C. to**<br>D. from
- Current keyed answer: **C. to**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cụm “adjacent to” là kết hợp chuẩn; các giới từ còn lại không đi với “adjacent” trong cấu trúc này. — Adjective + fixed preposition: adjacent to
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective + fixed preposition: adjacent to
- Single-answer rationale: Cụm “adjacent to” là kết hợp chuẩn; các giới từ còn lại không đi với “adjacent” trong cấu trúc này.
- Vietnamese translation: Phòng đào tạo nằm liền kề hội trường hội nghị chính.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-056` · Articles and Determiners

- Sentence: The company conducts __________ annual review of each supplier’s performance.
- Choices: A. a<br>**B. an**<br>C. the<br>D. no article
- Current keyed answer: **B. an**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Articles and Determiners): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “an” vừa đáp ứng yêu cầu mạo từ trước danh từ đếm được số ít, vừa đúng âm đầu của “annual”. — Indefinite article an before a vowel sound
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Indefinite article an before a vowel sound
- Single-answer rationale: Chỉ “an” vừa đáp ứng yêu cầu mạo từ trước danh từ đếm được số ít, vừa đúng âm đầu của “annual”.
- Vietnamese translation: Công ty tiến hành một cuộc đánh giá hằng năm về hiệu suất của từng nhà cung cấp.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-057` · Prepositions and Collocations

- Sentence: Flexible working hours can be beneficial __________ employees with long commutes.
- Choices: A. on<br>B. with<br>C. at<br>**D. to**
- Current keyed answer: **D. to**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “To” là giới từ theo sau “beneficial” khi nêu đối tượng nhận lợi ích; các lựa chọn còn lại không tạo kết hợp đúng trong cấu trúc này. — Adjective + preposition: beneficial to
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective + preposition: beneficial to
- Single-answer rationale: “To” là giới từ theo sau “beneficial” khi nêu đối tượng nhận lợi ích; các lựa chọn còn lại không tạo kết hợp đúng trong cấu trúc này.
- Vietnamese translation: Giờ làm việc linh hoạt có thể có lợi cho những nhân viên phải di chuyển quãng đường dài.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-058` · Adjectives and Adverbs

- Sentence: To remain __________ in the regional market, the company has lowered its delivery fees.
- Choices: A. competition<br>B. competitively<br>**C. competitive**<br>D. compete
- Current keyed answer: **C. competitive**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Competitive” là tính từ duy nhất phù hợp về từ loại và ý nghĩa với “remain”. — Linking verb remain + adjective
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Linking verb remain + adjective
- Single-answer rationale: “Competitive” là tính từ duy nhất phù hợp về từ loại và ý nghĩa với “remain”.
- Vietnamese translation: Để duy trì khả năng cạnh tranh trên thị trường khu vực, công ty đã giảm phí giao hàng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-059` · Adjectives and Adverbs

- Sentence: All salary information must remain strictly __________.
- Choices: **A. confidential**<br>B. confidentially<br>C. confidentiality<br>D. confide
- Current keyed answer: **A. confidential**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Confidential” là tính từ duy nhất hoàn thành cấu trúc “remain + adjective”; các dạng còn lại sai từ loại. — Adverb + adjective after a linking verb
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adverb + adjective after a linking verb
- Single-answer rationale: “Confidential” là tính từ duy nhất hoàn thành cấu trúc “remain + adjective”; các dạng còn lại sai từ loại.
- Vietnamese translation: Mọi thông tin về tiền lương phải luôn được giữ bí mật nghiêm ngặt.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-060` · Adjectives and Adverbs

- Sentence: The warehouse has operated without an incident for 120 __________ days.
- Choices: A. consecutively<br>**B. consecutive**<br>C. consequence<br>D. consecutiveness
- Current keyed answer: **B. consecutive**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “consecutive” là tính từ phù hợp cả vị trí lẫn nghĩa; “consecutively” là trạng từ. — Adjective before a plural count noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective before a plural count noun
- Single-answer rationale: Chỉ “consecutive” là tính từ phù hợp cả vị trí lẫn nghĩa; “consecutively” là trạng từ.
- Vietnamese translation: Kho hàng đã hoạt động 120 ngày liên tiếp mà không xảy ra sự cố.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-061` · Adjectives and Adverbs

- Sentence: The company offers __________ working hours during the summer to accommodate parents with school-age children.
- Choices: A. flexibility<br>B. flexibly<br>**C. flexible**<br>D. flex
- Current keyed answer: **C. flexible**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Flexible” là tính từ duy nhất bổ nghĩa đúng cho “working hours”; các lựa chọn khác sai từ loại hoặc sắc thái. — Adjective + noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adjective + noun
- Single-answer rationale: “Flexible” là tính từ duy nhất bổ nghĩa đúng cho “working hours”; các lựa chọn khác sai từ loại hoặc sắc thái.
- Vietnamese translation: Công ty cung cấp giờ làm việc linh hoạt vào mùa hè để hỗ trợ phụ huynh có con trong độ tuổi đi học.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-062` · Prepositions and Collocations

- Sentence: The flight was delayed __________ heavy fog at the airport.
- Choices: A. although<br>**B. because of**<br>C. despite<br>D. unless
- Current keyed answer: **B. because of**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “because of” vừa đi với cụm danh từ vừa diễn đạt nguyên nhân; “although/unless” cần mệnh đề và “despite” mang nghĩa nhượng bộ. — Cause phrase: because of + noun phrase
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Cause phrase: because of + noun phrase
- Single-answer rationale: Chỉ “because of” vừa đi với cụm danh từ vừa diễn đạt nguyên nhân; “although/unless” cần mệnh đề và “despite” mang nghĩa nhượng bộ.
- Vietnamese translation: Chuyến bay bị trì hoãn do sương mù dày đặc tại sân bay.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-063` · Prepositions and Collocations

- Sentence: The HR department must notify all applicants __________ any change in the interview schedule.
- Choices: A. for<br>**B. of**<br>C. with<br>D. at
- Current keyed answer: **B. of**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Of” là giới từ theo sau tân ngữ người trong kết hợp “notify all applicants of any change”; các lựa chọn còn lại không tạo mẫu này. — Verb + object + fixed preposition: notify someone of something
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Verb + object + fixed preposition: notify someone of something
- Single-answer rationale: “Of” là giới từ theo sau tân ngữ người trong kết hợp “notify all applicants of any change”; các lựa chọn còn lại không tạo mẫu này.
- Vietnamese translation: Phòng nhân sự phải thông báo cho tất cả ứng viên về mọi thay đổi trong lịch phỏng vấn.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-064` · Prepositions and Collocations

- Sentence: Employees can obtain a parking permit __________ the facilities office.
- Choices: **A. from**<br>B. to<br>C. among<br>D. during
- Current keyed answer: **A. from**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “from” nêu đúng nguồn mà nhân viên nhận giấy phép; các lựa chọn khác chỉ vị trí/thời gian hoặc sai quan hệ. — Obtain something from a source
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Obtain something from a source
- Single-answer rationale: Chỉ “from” nêu đúng nguồn mà nhân viên nhận giấy phép; các lựa chọn khác chỉ vị trí/thời gian hoặc sai quan hệ.
- Vietnamese translation: Nhân viên có thể nhận giấy phép đỗ xe từ văn phòng cơ sở vật chất.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-065` · Prepositions and Collocations

- Sentence: All employees are expected to participate __________ the annual safety drill.
- Choices: A. at<br>B. on<br>C. with<br>**D. in**
- Current keyed answer: **D. in**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Participate in the annual safety drill” là kết hợp đúng; các giới từ còn lại không phù hợp với hoạt động được tham gia. — Verb + preposition: participate in
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Verb + preposition: participate in
- Single-answer rationale: “Participate in the annual safety drill” là kết hợp đúng; các giới từ còn lại không phù hợp với hoạt động được tham gia.
- Vietnamese translation: Tất cả nhân viên được kỳ vọng tham gia buổi diễn tập an toàn hằng năm.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-066` · Prepositions and Collocations

- Sentence: The new filter helps prevent dust __________ entering the ventilation system.
- Choices: A. to<br>**B. from**<br>C. for<br>D. by
- Current keyed answer: **B. from**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “from” tạo đúng mẫu “prevent dust from entering”; các giới từ còn lại sai kết hợp. — Prevent + object + from + gerund
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Prevent + object + from + gerund
- Single-answer rationale: Chỉ “from” tạo đúng mẫu “prevent dust from entering”; các giới từ còn lại sai kết hợp.
- Vietnamese translation: Bộ lọc mới giúp ngăn bụi xâm nhập vào hệ thống thông gió.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-067` · Prepositions and Collocations

- Sentence: The company plans to reduce operating costs __________ consolidating two warehouse locations.
- Choices: **A. by**<br>B. at<br>C. since<br>D. unless
- Current keyed answer: **A. by**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “By” là giới từ chỉ phương thức và được theo sau bởi V-ing; các lựa chọn khác không đúng cấu trúc. — By + gerund to express method
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: By + gerund to express method
- Single-answer rationale: “By” là giới từ chỉ phương thức và được theo sau bởi V-ing; các lựa chọn khác không đúng cấu trúc.
- Vietnamese translation: Công ty dự định giảm chi phí vận hành bằng cách hợp nhất hai địa điểm kho.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-068` · Conjunctions and Clauses

- Sentence: The committee rejected the proposal __________ it did not include a cost estimate.
- Choices: A. despite<br>**B. because**<br>C. however<br>D. during
- Current keyed answer: **B. because**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Conjunctions and Clauses): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “because” nối trực tiếp mệnh đề nguyên nhân hoàn chỉnh “it did not include a cost estimate”. — Because + subject + verb clause
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Because + subject + verb clause
- Single-answer rationale: Chỉ “because” nối trực tiếp mệnh đề nguyên nhân hoàn chỉnh “it did not include a cost estimate”.
- Vietnamese translation: Ủy ban đã từ chối đề xuất vì đề xuất không bao gồm ước tính chi phí.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-069` · Conjunctions and Clauses

- Sentence: The supplier must submit its renewal application __________ the current certification expires.
- Choices: A. after<br>**B. before**<br>C. while<br>D. since
- Current keyed answer: **B. before**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Conjunctions and Clauses): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Câu yêu cầu nộp hồ sơ gia hạn trước ngày chứng nhận hiện tại hết hiệu lực; “before” diễn đạt đúng thứ tự đó. — Time conjunction: before + present simple clause
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Time conjunction: before + present simple clause
- Single-answer rationale: Câu yêu cầu nộp hồ sơ gia hạn trước ngày chứng nhận hiện tại hết hiệu lực; “before” diễn đạt đúng thứ tự đó.
- Vietnamese translation: Nhà cung cấp phải nộp hồ sơ gia hạn trước khi chứng nhận hiện tại hết hiệu lực.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-070` · Prepositions and Collocations

- Sentence: The conference room is being kept available __________ the visiting auditors during next week’s inspection.
- Choices: A. at<br>**B. for**<br>C. with<br>D. from
- Current keyed answer: **B. for**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Cấu trúc tự nhiên trong ngữ cảnh này là “keep the room available for someone”: phòng được giữ sẵn để nhóm kiểm toán sử dụng. — Reserved for + intended recipient
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Reserved for + intended recipient
- Single-answer rationale: Cấu trúc tự nhiên trong ngữ cảnh này là “keep the room available for someone”: phòng được giữ sẵn để nhóm kiểm toán sử dụng.
- Vietnamese translation: Phòng hội nghị đang được giữ sẵn dành cho các kiểm toán viên đến thăm trong đợt kiểm tra tuần tới.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-071` · Conjunctions and Clauses

- Sentence: The company offers professional development opportunities to retain employees __________ demonstrate strong leadership potential.
- Choices: A. which<br>B. whose<br>**C. who**<br>D. where
- Current keyed answer: **C. who**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Conjunctions and Clauses): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Who” là đại từ quan hệ duy nhất phù hợp với người và làm chủ ngữ trước động từ “demonstrate”. — Relative pronoun who for people
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Relative pronoun who for people
- Single-answer rationale: “Who” là đại từ quan hệ duy nhất phù hợp với người và làm chủ ngữ trước động từ “demonstrate”.
- Vietnamese translation: Công ty cung cấp cơ hội phát triển nghề nghiệp để giữ chân những nhân viên thể hiện tiềm năng lãnh đạo mạnh mẽ.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-072` · Participles and Reduced Relative Clauses

- Sentence: The technician __________ the night shift must complete the safety log before leaving.
- Choices: A. supervise<br>B. supervises<br>**C. supervising**<br>D. supervised
- Current keyed answer: **C. supervising**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Participles and Reduced Relative Clauses): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Supervising” là phân từ hiện tại phù hợp với nghĩa chủ động và chức năng bổ nghĩa cho “technician”. — Present participle clause modifying a noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Present participle clause modifying a noun
- Single-answer rationale: “Supervising” là phân từ hiện tại phù hợp với nghĩa chủ động và chức năng bổ nghĩa cho “technician”.
- Vietnamese translation: Kỹ thuật viên đang giám sát ca đêm phải hoàn thành nhật ký an toàn trước khi rời đi.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-073` · Infinitives and Verb Patterns

- Sentence: The new recognition program is designed to __________ employees to share practical ideas.
- Choices: A. encouraging<br>B. encouragement<br>**C. encourage**<br>D. encouraged
- Current keyed answer: **C. encourage**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Sau “to” của cụm “be designed to” cần động từ nguyên mẫu “encourage”. — Be designed to + base verb
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Be designed to + base verb
- Single-answer rationale: Sau “to” của cụm “be designed to” cần động từ nguyên mẫu “encourage”.
- Vietnamese translation: Chương trình ghi nhận mới được thiết kế nhằm khuyến khích nhân viên chia sẻ các ý tưởng thiết thực.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-074` · Infinitives and Verb Patterns

- Sentence: Managers must __________ that all visitors sign in at reception.
- Choices: A. ensuring<br>B. ensures<br>C. ensured<br>**D. ensure**
- Current keyed answer: **D. ensure**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Ensure” là dạng nguyên mẫu duy nhất đi sau “must”; các lựa chọn khác sai dạng động từ. — Modal verb + base form
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Modal verb + base form
- Single-answer rationale: “Ensure” là dạng nguyên mẫu duy nhất đi sau “must”; các lựa chọn khác sai dạng động từ.
- Vietnamese translation: Các quản lý phải bảo đảm tất cả khách đến thăm đăng ký tại quầy lễ tân.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-075` · Prepositions and Collocations

- Sentence: Please forward the signed contract __________ the legal department for review.
- Choices: **A. to**<br>B. at<br>C. for<br>D. with
- Current keyed answer: **A. to**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “To the legal department” xác định đích đến của tài liệu; các giới từ còn lại không thể hiện quan hệ chuyển tiếp này. — Forward something to a recipient
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Forward something to a recipient
- Single-answer rationale: “To the legal department” xác định đích đến của tài liệu; các giới từ còn lại không thể hiện quan hệ chuyển tiếp này.
- Vietnamese translation: Vui lòng chuyển tiếp hợp đồng đã ký đến bộ phận pháp chế để xem xét.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-076` · Infinitives and Verb Patterns

- Sentence: The company plans to __________ its response time by introducing an online support desk.
- Choices: A. improvement<br>B. improved<br>C. improving<br>**D. improve**
- Current keyed answer: **D. improve**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Infinitives and Verb Patterns): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “improve” tạo đúng mẫu “plans to + base verb”. — Plan + to-infinitive
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Plan + to-infinitive
- Single-answer rationale: Chỉ “improve” tạo đúng mẫu “plans to + base verb”.
- Vietnamese translation: Công ty dự định cải thiện thời gian phản hồi bằng cách triển khai quầy hỗ trợ trực tuyến.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-077` · Gerunds and Infinitives

- Sentence: The facilities team spends two hours each morning __________ the public areas.
- Choices: A. maintain<br>**B. maintaining**<br>C. maintenance<br>D. maintained
- Current keyed answer: **B. maintaining**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Gerunds and Infinitives): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): Chỉ “maintaining” hoàn thành cấu trúc “spends two hours ...”; danh từ hoặc nguyên mẫu không phù hợp. — Spend time + gerund
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Spend time + gerund
- Single-answer rationale: Chỉ “maintaining” hoàn thành cấu trúc “spends two hours ...”; danh từ hoặc nguyên mẫu không phù hợp.
- Vietnamese translation: Nhóm cơ sở vật chất dành hai giờ mỗi sáng để bảo trì các khu vực công cộng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-078` · Prepositions and Collocations

- Sentence: The project team managed to accomplish its goals __________ the original deadline.
- Choices: A. among<br>B. beyond<br>**C. within**<br>D. beside
- Current keyed answer: **C. within**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Within” là giới từ duy nhất diễn tả hoàn thành trong giới hạn thời gian; “beyond” mang nghĩa ngược lại. — Within + time limit/deadline
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Within + time limit/deadline
- Single-answer rationale: “Within” là giới từ duy nhất diễn tả hoàn thành trong giới hạn thời gian; “beyond” mang nghĩa ngược lại.
- Vietnamese translation: Nhóm dự án đã hoàn thành các mục tiêu trong thời hạn ban đầu.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-079` · Prepositions and Collocations

- Sentence: New employees must adapt __________ the company’s safety procedures before starting work.
- Choices: A. with<br>**B. to**<br>C. for<br>D. at
- Current keyed answer: **B. to**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Prepositions and Collocations): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Adapt to the company’s safety procedures” là kết hợp chuẩn; các giới từ còn lại không mang nghĩa thích nghi với quy trình. — Adapt to + noun
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adapt to + noun
- Single-answer rationale: “Adapt to the company’s safety procedures” là kết hợp chuẩn; các giới từ còn lại không mang nghĩa thích nghi với quy trình.
- Vietnamese translation: Nhân viên mới phải thích nghi với các quy trình an toàn của công ty trước khi bắt đầu làm việc.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

### `p5-sc-080` · Adjectives and Adverbs

- Sentence: Payroll is processed __________, on the last working day of each month.
- Choices: A. month<br>**B. monthly**<br>C. monthly basis<br>D. month’s
- Current keyed answer: **B. monthly**
- Editorial status (`editorialStatus`): `reserve-pending-independent-review`
- Review scope (`reviewScope`): Separate Part 5 practice-only sentence completion (Adjectives and Adverbs): grammar point, single-answer uniqueness, and option explanations
- Certainty level (`certaintyLevel`): `unreviewed-reserve` (structural audit passed; AI triage: none)
- Rationale (`rationale`): “Monthly” là trạng từ duy nhất có thể đứng độc lập ở vị trí này; “monthly basis” cần giới từ và mạo từ “on a”. — Adverb of frequency: monthly
- Proposed correction (`proposedCorrection`): `None pending human review — record exact edit if REVISE`
- Grammar point: Adverb of frequency: monthly
- Single-answer rationale: “Monthly” là trạng từ duy nhất có thể đứng độc lập ở vị trí này; “monthly basis” cần giới từ và mạo từ “on a”.
- Vietnamese translation: Bảng lương được xử lý hằng tháng, vào ngày làm việc cuối cùng của mỗi tháng.
- Reviewer: [ ] grammar correct  [ ] sentence natural  [ ] distractors wrong  [ ] translation/explanations accurate  [ ] one defensible answer
- Decision: `________` · Correction / notes: __________________________________________

## Release rule

- The current 102 eligible Listening questions remain the only approved Listening pool; the 193 reserve questions are not promoted by this packet.
- The 87 Part 7 reserve questions remain excluded from Mock approval until item-level independent review is recorded.
- The separate Part 5 practice-only bank contains 80 questions and remains outside Mock eligibility; any review-status change requires item-level sign-off.
- A structural pass, traceable evidence quote or AI-assisted audit is not a substitute for the independent reviewer decision.
