# Vocabulary Batch 006 — v2.9.9 Batch 001

**Trạng thái:** Đã áp dụng trong working tree v2.9.9; chưa phải ZIP phát hành cuối cùng.  
**Nền dữ liệu:** v2.9.8, 928 headwords.  
**Phạm vi:** 40 headwords A–C; sửa `definition_en` và ví dụ tiếng Anh/bản dịch.  
**Cơ chế:** `patches/v2.9.9/batch-001.json`, kiểm tra ID + SHA-256 + `expect.old` + POS; có `--dry-run`, `--apply`, `--rollback`.

## Tiêu chí biên tập

- Definition là câu/nhóm từ định nghĩa tiếng Anh tự nhiên, không lặp lại headword ở đầu theo dạng nhãn.
- Ví dụ đặt trong ngữ cảnh TOEIC (văn phòng, tài chính, cuộc họp, vận hành, kho vận, dịch vụ); không dùng câu khuôn chung.
- Bản dịch diễn đạt tự nhiên, giữ đúng nghĩa của câu tiếng Anh.
- Không thay đổi ID, POS, IPA, CEFR, word family, verb forms, collocations, synonyms hoặc antonyms.
- Đây là nội dung biên tập mới, không sao chép nguyên văn ví dụ của từ điển tham khảo.

## Danh sách 40 mục đã xử lý

| ID | Headword | Definition tiếng Anh mới | Ví dụ tiếng Anh mới | Bản dịch |
|---|---|---|---|---|
| absence-n | absence | the fact of not being present in a place or at an event | The employee's absence was recorded in the attendance system. | Sự vắng mặt của nhân viên đã được ghi nhận trong hệ thống chấm công. |
| accommodate-v | accommodate | to provide enough space for someone or something, or to adjust to someone's needs | The conference room can accommodate up to forty participants. | Phòng hội nghị có thể đáp ứng chỗ ngồi cho tối đa bốn mươi người tham dự. |
| accomplish-v | accomplish | to succeed in doing or completing something, especially a task or goal | The project team accomplished all of its targets ahead of schedule. | Nhóm dự án đã hoàn thành tất cả mục tiêu trước thời hạn. |
| accordance-n | accordance | the condition of following a rule, instruction, or standard; commonly used in “in accordance with” | All expense claims must be submitted in accordance with company policy. | Mọi đề nghị thanh toán chi phí phải được gửi theo đúng chính sách công ty. |
| accountable-adj | accountable | responsible for actions or decisions and required to explain them | Each department manager is accountable for the accuracy of the monthly report. | Mỗi trưởng phòng chịu trách nhiệm về độ chính xác của báo cáo hằng tháng. |
| accrue-v | accrue | to increase or accumulate gradually over time, especially money, interest, or benefits | Interest will accrue on the outstanding balance until it is paid in full. | Tiền lãi sẽ tích lũy trên số dư còn nợ cho đến khi được thanh toán đầy đủ. |
| accurate-adj | accurate | correct and exact, with no significant mistakes | Please make sure that the figures in the sales report are accurate. | Vui lòng đảm bảo các số liệu trong báo cáo bán hàng là chính xác. |
| activate-v | activate | to make a system, device, account, or process start working | New employees must activate their accounts before accessing the portal. | Nhân viên mới phải kích hoạt tài khoản trước khi truy cập cổng thông tin. |
| additional-adj | additional | extra; added to what is already available or required | The supplier agreed to deliver the additional office chairs by Friday. | Nhà cung cấp đồng ý giao thêm số ghế văn phòng trước thứ Sáu. |
| adjacent-adj | adjacent | next to or sharing a boundary with something | The training room is adjacent to the main conference hall. | Phòng đào tạo nằm liền kề hội trường chính. |
| adjustment-n | adjustment | a small change made to improve something or make it suitable | The finance department made an adjustment to the travel budget. | Phòng tài chính đã điều chỉnh ngân sách công tác. |
| administrative-adj | administrative | related to organizing, managing, or running the work of an organization | Administrative staff will send the revised schedule to all employees. | Nhân viên hành chính sẽ gửi lịch trình đã sửa đổi cho toàn thể nhân viên. |
| administrator-n | administrator | a person responsible for managing an organization, system, or process | Contact the system administrator if your account is locked. | Hãy liên hệ quản trị viên hệ thống nếu tài khoản của bạn bị khóa. |
| admission-n | admission | permission to enter a place or event; the fee charged for entry | Admission to the annual trade exhibition is free for registered customers. | Khách hàng đã đăng ký được vào triển lãm thương mại thường niên miễn phí. |
| adopt-v | adopt | to formally accept or begin using a plan, policy, or method | The board voted to adopt the new customer service guidelines. | Hội đồng đã bỏ phiếu thông qua bộ hướng dẫn dịch vụ khách hàng mới. |
| allocation-n | allocation | the process of assigning money, time, or resources for a particular purpose | The allocation of funds for staff training was approved last week. | Việc phân bổ kinh phí đào tạo nhân viên đã được phê duyệt tuần trước. |
| amend-v | amend | to make a formal change to a document, contract, or law | Both parties agreed to amend the contract before signing it. | Hai bên đồng ý sửa đổi hợp đồng trước khi ký. |
| annually-adv | annually | once every year | The company reviews employee performance annually. | Công ty đánh giá hiệu quả làm việc của nhân viên hằng năm. |
| apologize-v | apologize | to tell someone that you are sorry for a mistake or for causing trouble | The airline apologized to passengers for the unexpected delay. | Hãng hàng không đã xin lỗi hành khách vì sự chậm trễ ngoài dự kiến. |
| applicable-adj | applicable | relevant to a particular person, situation, or set of conditions | The discount is applicable to orders placed before the end of the month. | Mức giảm giá được áp dụng cho các đơn hàng đặt trước cuối tháng. |
| approval-n | approval | official agreement or permission for a plan, request, or action | The marketing proposal is awaiting approval from the regional director. | Đề xuất tiếp thị đang chờ giám đốc khu vực phê duyệt. |
| approximately-adv | approximately | used to indicate an amount, time, or number that is close to but not exactly correct | The replacement parts are expected to arrive in approximately five days. | Các linh kiện thay thế dự kiến sẽ đến trong khoảng năm ngày. |
| arrangement-n | arrangement | a plan or agreement made in advance about how something will happen | The travel arrangements for the visiting delegates have been finalized. | Các sắp xếp đi lại cho đoàn đại biểu đến thăm đã được hoàn tất. |
| assess-v | assess | to examine something and judge its quality, value, importance, or condition | The consultant will assess the building before preparing a renovation estimate. | Chuyên gia tư vấn sẽ đánh giá tòa nhà trước khi lập dự toán cải tạo. |
| assistance-n | assistance | help or support given to someone who needs it | Customers can request technical assistance through the support center. | Khách hàng có thể yêu cầu hỗ trợ kỹ thuật thông qua trung tâm hỗ trợ. |
| attendance-n | attendance | the act of being present at a meeting, event, or place | Attendance at the safety training session is required for all warehouse staff. | Toàn bộ nhân viên kho bắt buộc tham dự buổi đào tạo an toàn. |
| attendee-n | attendee | a person who is present at a meeting, conference, or other event | Each attendee will receive a copy of the conference program at registration. | Mỗi người tham dự sẽ nhận một bản chương trình hội nghị khi đăng ký. |
| authorization-n | authorization | official permission to do something or to access something | Written authorization is required before confidential files can be released. | Cần có văn bản ủy quyền trước khi hồ sơ mật được cung cấp. |
| authorize-v | authorize | to give someone official permission to do something | Only the finance director can authorize payments above the stated limit. | Chỉ giám đốc tài chính mới có quyền phê duyệt các khoản thanh toán vượt hạn mức đã quy định. |
| backlog-n | backlog | a quantity of work, orders, or requests that have not yet been completed | The support team is hiring temporary staff to reduce its backlog of requests. | Nhóm hỗ trợ đang tuyển nhân viên thời vụ để giảm lượng yêu cầu tồn đọng. |
| backup-n | backup | a copy of data kept in case the original is lost, or a person or resource ready to provide support | The IT team creates a backup of the customer database every night. | Đội CNTT tạo bản sao lưu cơ sở dữ liệu khách hàng mỗi đêm. |
| bargain-n | bargain | an agreement reached after discussion, or something bought at a price lower than usual | The purchasing manager negotiated a bargain with the equipment supplier. | Trưởng bộ phận mua hàng đã thương lượng được một thỏa thuận có lợi với nhà cung cấp thiết bị. |
| beneficial-adj | beneficial | helpful or producing a positive effect | Flexible working hours can be beneficial to employees with long commutes. | Giờ làm việc linh hoạt có thể mang lại lợi ích cho nhân viên phải đi làm xa. |
| billable-adj | billable | able to be charged to a customer or included on an invoice | The consultant records all billable hours in the project management system. | Chuyên gia tư vấn ghi lại toàn bộ số giờ có thể tính phí trong hệ thống quản lý dự án. |
| billing-n | billing | the process of preparing invoices and collecting payment for goods or services | The billing department will issue the revised invoice tomorrow. | Bộ phận lập hóa đơn sẽ phát hành hóa đơn đã điều chỉnh vào ngày mai. |
| briefing-n | briefing | a short meeting or summary that provides essential information or instructions | All drivers must attend a safety briefing before starting their shifts. | Tất cả tài xế phải tham dự buổi phổ biến an toàn trước khi bắt đầu ca làm. |
| capacity-n | capacity | the maximum amount something can hold or the ability to perform a task | The new warehouse has the capacity to store 8,000 packages. | Nhà kho mới có sức chứa 8.000 kiện hàng. |
| cargo-n | cargo | goods carried by a ship, aircraft, train, or truck | The cargo was inspected before it was loaded onto the aircraft. | Hàng hóa đã được kiểm tra trước khi được xếp lên máy bay. |
| certificate-n | certificate | an official document that confirms a fact, qualification, or completed course | Applicants must submit a safety training certificate with their forms. | Ứng viên phải nộp chứng chỉ đào tạo an toàn kèm theo hồ sơ. |
| circulate-v | circulate | to distribute a document or information to a group, or to move continuously through a system | Please circulate the updated meeting agenda to all department heads. | Vui lòng gửi chương trình họp đã cập nhật đến tất cả trưởng bộ phận. |
