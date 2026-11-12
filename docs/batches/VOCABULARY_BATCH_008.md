# Vocabulary Quality Correction Batch 003 — v2.9.9

**Trạng thái:** Đã dry-run và áp dụng bằng `tools/patch-data.py`; đã chạy validator. Đây là working tree, chưa phải ZIP phát hành cuối.
**Nền dữ liệu:** v2.9.8, 928 ID; `baseDataVersion=2.9.8`; `idSetSha256` giữ nguyên.
**Phạm vi:** 40 headwords; sửa definition tiếng Anh và rà soát ví dụ/bản dịch theo ngữ cảnh TOEIC.
**Patch:** `patches/v2.9.9/batch-003.json` (120 thao tác).

Mỗi thao tác khóa theo ID, JSON Pointer và `expect.old`; trường definition còn kiểm tra POS. Patch hủy toàn batch nếu dữ liệu nền không khớp. Không thay đổi ID/POS/IPA/CEFR/schema hoặc dữ liệu cá nhân.

## Danh sách mục đã xử lý

| ID | Headword | Definition tiếng Anh mới | Ví dụ tiếng Anh | Bản dịch tiếng Việt |
|---|---|---|---|---|
| equivalent-adj | equivalent | equal in value, function, meaning, or importance to something else | The replacement battery is equivalent to the original model. | Pin thay thế có thông số tương đương với mẫu ban đầu. |
| exempt-adj | exempt | not required to do something or pay a particular charge because of a rule or special condition | Small businesses may be exempt from the annual registration fee. | Các doanh nghiệp nhỏ có thể được miễn lệ phí đăng ký hằng năm. |
| expiration-n | expiration | the end of the period during which a document, agreement, or product remains valid or usable | Please check the expiration date before renewing your access card. | Vui lòng kiểm tra ngày hết hạn trước khi gia hạn thẻ truy cập. |
| extension-n | extension | an arrangement that gives extra time, or an additional part connected to something; also a telephone line number | The client requested an extension of the payment deadline. | Khách hàng đề nghị gia hạn thời hạn thanh toán. |
| facilitate-v | facilitate | to make an action or process easier to do | The online form is designed to facilitate the registration process. | Biểu mẫu trực tuyến được thiết kế để tạo thuận lợi cho quy trình đăng ký. |
| feasibility-n | feasibility | the possibility that a plan or project can be carried out successfully | The engineering team will study the feasibility of building a second warehouse. | Đội ngũ kỹ thuật sẽ nghiên cứu tính khả thi của việc xây dựng nhà kho thứ hai. |
| feasible-adj | feasible | possible and practical to do under the available conditions | The manager believes that the proposed delivery schedule is feasible. | Quản lý tin rằng lịch giao hàng được đề xuất là khả thi. |
| flexibility-n | flexibility | the ability to change or adapt to different needs, conditions, or arrangements | The company introduced flexible shifts to give employees more flexibility. | Công ty áp dụng ca làm linh hoạt để nhân viên có thêm sự linh hoạt. |
| fulfill-v | fulfill | to do what is required, promised, or expected; to satisfy a need or condition | The supplier must fulfill every requirement listed in the purchase agreement. | Nhà cung cấp phải đáp ứng mọi yêu cầu được nêu trong thỏa thuận mua hàng. |
| generate-v | generate | to produce or create something, such as income, information, or electricity | The new advertising campaign is expected to generate more online sales. | Chiến dịch quảng cáo mới được kỳ vọng tạo ra thêm doanh thu trực tuyến. |
| guideline-n | guideline | a general rule or piece of advice that helps people make decisions or perform a task | The handbook provides guidelines for handling customer complaints. | Sổ tay cung cấp hướng dẫn về cách xử lý khiếu nại của khách hàng. |
| handling-n | handling | the way something is dealt with, managed, or physically treated | Careful handling is required when loading fragile equipment. | Cần thao tác cẩn thận khi xếp dỡ thiết bị dễ vỡ. |
| implement-v | implement | to put a plan, decision, or system into practical use | The company will implement the revised attendance policy next month. | Công ty sẽ triển khai chính sách chấm công đã sửa đổi vào tháng tới. |
| incentive-n | incentive | something offered to encourage a person to take an action or achieve a goal | Employees who exceed their sales targets may receive a financial incentive. | Nhân viên vượt chỉ tiêu bán hàng có thể nhận được khoản khuyến khích tài chính. |
| incentivize-v | incentivize | to encourage a particular action by offering a reward or benefit | The new commission plan is intended to incentivize higher sales. | Chính sách hoa hồng mới nhằm khuyến khích tăng doanh số. |
| inquire-v | inquire | to ask for information about something | Please inquire at the reception desk if you need a visitor pass. | Vui lòng hỏi tại quầy lễ tân nếu bạn cần thẻ khách. |
| inquiry-n | inquiry | a request for information, or an official examination of a matter | The customer submitted an inquiry about the status of the refund. | Khách hàng đã gửi yêu cầu thông tin về tình trạng hoàn tiền. |
| inspection-n | inspection | an official or careful examination to check quality, safety, or condition | The building passed its annual fire safety inspection. | Tòa nhà đã vượt qua đợt kiểm tra an toàn phòng cháy hằng năm. |
| inspector-n | inspector | a person whose job is to examine something to make sure that it meets required standards | A safety inspector will visit the factory on Thursday. | Một thanh tra an toàn sẽ đến nhà máy vào thứ Năm. |
| invoicing-n | invoicing | the process of preparing and sending invoices for goods or services | Automated invoicing has reduced paperwork in the accounting department. | Việc lập hóa đơn tự động đã giảm giấy tờ trong phòng kế toán. |
| justify-v | justify | to provide a good reason or evidence to show that an action or decision is reasonable | The project manager must justify the additional expense in the budget report. | Quản lý dự án phải giải trình khoản chi phí bổ sung trong báo cáo ngân sách. |
| laboratory-n | laboratory | a place equipped for scientific tests, research, or technical examination | The product samples were sent to an independent laboratory for testing. | Các mẫu sản phẩm đã được gửi đến phòng thí nghiệm độc lập để kiểm tra. |
| lessee-n | lessee | a person or organization that rents property or equipment under a lease | The lessee must maintain the office space throughout the rental period. | Bên thuê phải bảo trì mặt bằng văn phòng trong suốt thời hạn thuê. |
| lessor-n | lessor | a person or organization that allows another party to use property or equipment in return for rent | The lessor agreed to repair the air-conditioning system before the office opens. | Bên cho thuê đồng ý sửa hệ thống điều hòa trước khi văn phòng khai trương. |
| liability-n | liability | a legal responsibility or a debt that an individual or organization must pay | The company recorded the unpaid tax as a current liability. | Công ty ghi nhận khoản thuế chưa nộp là một khoản nợ ngắn hạn. |
| maintenance-n | maintenance | work done regularly to keep a building, machine, or system in good condition | Routine maintenance will be carried out after business hours. | Công tác bảo trì định kỳ sẽ được thực hiện sau giờ làm việc. |
| mandatory-adj | mandatory | required by a law, rule, or official instruction; not optional | Wearing a safety helmet is mandatory inside the construction area. | Việc đội mũ bảo hộ là bắt buộc trong khu vực xây dựng. |
| manufacturer-n | manufacturer | a company or person that makes goods in large quantities for sale | The manufacturer will replace any unit that fails during the warranty period. | Nhà sản xuất sẽ thay thế mọi thiết bị bị hỏng trong thời hạn bảo hành. |
| nevertheless-adj | nevertheless | despite what has just been said or the situation described; however | The shipment was delayed; nevertheless, the customer agreed to keep the order. | Lô hàng bị chậm trễ; tuy nhiên, khách hàng vẫn đồng ý giữ đơn hàng. |
| occupancy-n | occupancy | the state or number of people using or living in a building, room, or other space | The hotel expects an occupancy rate of more than eighty percent this weekend. | Khách sạn dự kiến tỷ lệ lấp đầy phòng sẽ vượt tám mươi phần trăm vào cuối tuần này. |
| officeholder-n | officeholder | a person who currently holds an official position or public office | The officeholder must submit an annual statement of interests. | Người giữ chức vụ phải nộp bản kê khai lợi ích hằng năm. |
| outsource-v | outsource | to arrange for an outside company or person to perform work instead of doing it internally | The retailer decided to outsource its delivery operations to a logistics provider. | Nhà bán lẻ quyết định thuê một đơn vị logistics bên ngoài thực hiện hoạt động giao hàng. |
| outsourcing-n | outsourcing | the practice of paying an outside organization to perform work or provide services | Outsourcing customer support helped the company reduce operating costs. | Việc thuê ngoài dịch vụ chăm sóc khách hàng đã giúp công ty giảm chi phí vận hành. |
| outstanding-adj | outstanding | not yet paid, completed, or resolved; also exceptionally good | Please settle all outstanding invoices before the end of the quarter. | Vui lòng thanh toán tất cả hóa đơn còn tồn đọng trước khi kết thúc quý. |
| overdue-adj | overdue | not paid, returned, or completed by the expected or required date | The library sent reminders to members with overdue books. | Thư viện gửi thông báo nhắc nhở các thành viên chưa trả sách đúng hạn. |
| overhaul-n | overhaul | a thorough examination and repair or major improvement of a system or organization | The airline scheduled a complete overhaul of its booking platform. | Hãng hàng không lên lịch đại tu toàn bộ nền tảng đặt chỗ. |
| parcel-n | parcel | a package or wrapped item sent or delivered to someone | The courier left the parcel at the reception desk. | Nhân viên chuyển phát đã để bưu kiện tại quầy lễ tân. |
| participant-n | participant | a person who takes part in an activity, event, or program | Each participant must complete the online safety course before the workshop. | Mỗi người tham gia phải hoàn thành khóa an toàn trực tuyến trước buổi hội thảo. |
| payable-adj | payable | required to be paid, especially by a stated date | The remaining balance is payable within thirty days of the invoice date. | Số dư còn lại phải được thanh toán trong vòng ba mươi ngày kể từ ngày xuất hóa đơn. |
| penalty-n | penalty | a punishment or additional amount of money imposed for breaking a rule or failing to meet an obligation | A penalty will be charged if the equipment is returned after the due date. | Một khoản phạt sẽ được áp dụng nếu thiết bị được trả sau ngày đến hạn. |

## Kiểm soát chất lượng

- Kiểm tra nội dung theo nghĩa, từ loại và bối cảnh TOEIC; ví dụ phải tự nhiên, có bản dịch tương ứng.
- Không tự sinh IPA, CEFR hoặc quan hệ từ; giữ nguyên các trường này.
- Validator sau khi áp dụng phải có 0 ERROR. Chỉ siết baseline sau khi các nội dung đã được rà soát; không thêm lỗi mới.
