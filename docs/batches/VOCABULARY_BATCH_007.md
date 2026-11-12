# Vocabulary Quality Correction Batch 002 — v2.9.9

**Trạng thái:** Đã dry-run và áp dụng bằng `tools/patch-data.py`; đã chạy validator. Đây là working tree, chưa phải ZIP phát hành cuối.
**Nền dữ liệu:** v2.9.8, 928 ID; `baseDataVersion=2.9.8`; `idSetSha256` giữ nguyên.
**Phạm vi:** 40 headwords; sửa definition tiếng Anh và rà soát ví dụ/bản dịch theo ngữ cảnh TOEIC.
**Patch:** `patches/v2.9.9/batch-002.json` (119 thao tác).

Mỗi thao tác khóa theo ID, JSON Pointer và `expect.old`; trường definition còn kiểm tra POS. Patch hủy toàn batch nếu dữ liệu nền không khớp. Không thay đổi ID/POS/IPA/CEFR/schema hoặc dữ liệu cá nhân.

## Danh sách mục đã xử lý

| ID | Headword | Definition tiếng Anh mới | Ví dụ tiếng Anh | Bản dịch tiếng Việt |
|---|---|---|---|---|
| clarify-v | clarify | to make information, instructions, or a situation easier to understand | The purchasing manager asked the supplier to clarify the delivery terms. | Trưởng bộ phận mua hàng yêu cầu nhà cung cấp làm rõ các điều khoản giao hàng. |
| clientele-n | clientele | the people who regularly buy goods or use services from a business | The new branch is designed to serve a younger clientele. | Chi nhánh mới được thiết kế để phục vụ nhóm khách hàng trẻ hơn. |
| compensation-n | compensation | money or benefits given in return for work, or to make up for loss or injury | The compensation package includes a transport allowance and health insurance. | Gói đãi ngộ bao gồm phụ cấp đi lại và bảo hiểm y tế. |
| competitive-adj | competitive | able to compete successfully, especially because of price, quality, or performance | The company offers competitive salaries to attract experienced engineers. | Công ty đưa ra mức lương cạnh tranh để thu hút các kỹ sư giàu kinh nghiệm. |
| competitor-n | competitor | a person or organization that offers similar products or services and competes for the same customers | A major competitor has opened a new store across the street. | Một đối thủ cạnh tranh lớn đã mở cửa hàng mới bên kia đường. |
| completion-n | completion | the act or result of finishing a task, project, or process | Final payment will be made upon completion of the installation. | Khoản thanh toán cuối cùng sẽ được thực hiện sau khi hoàn tất việc lắp đặt. |
| comply-v | comply | to act according to a rule, law, request, or official requirement | All contractors must comply with the company’s safety regulations. | Tất cả nhà thầu phải tuân thủ các quy định an toàn của công ty. |
| confidential-adj | confidential | intended to be kept private and not shared with people who are not authorized | Employees must not disclose confidential customer information. | Nhân viên không được tiết lộ thông tin khách hàng bảo mật. |
| confirmation-n | confirmation | a statement or message showing that an arrangement, booking, or fact is definite | You will receive an email confirmation after your reservation is processed. | Bạn sẽ nhận được email xác nhận sau khi đặt chỗ được xử lý. |
| consecutive-adj | consecutive | following one after another without a break or interruption | The warehouse recorded three consecutive days without a shipping delay. | Nhà kho ghi nhận ba ngày liên tiếp không xảy ra chậm trễ giao hàng. |
| consent-n | consent | permission or agreement given for something to happen | The survey will be conducted only after participants give their consent. | Khảo sát chỉ được tiến hành sau khi người tham gia đưa ra sự đồng ý. |
| consumable-n | consumable | a product or material that is used up during normal operations and must be replaced | The office orders printer ink and other consumables every month. | Văn phòng đặt mực in và các vật tư tiêu hao khác mỗi tháng. |
| consumption-n | consumption | the amount of a resource, product, or service that is used | The new lighting system has reduced electricity consumption. | Hệ thống chiếu sáng mới đã giảm mức tiêu thụ điện. |
| contractual-adj | contractual | relating to a contract or to duties and rights established by a contract | The supplier failed to meet its contractual obligations. | Nhà cung cấp đã không thực hiện đúng các nghĩa vụ theo hợp đồng. |
| coordinate-v | coordinate | to organize people, activities, or resources so that they work together effectively | The event coordinator will coordinate transportation for all speakers. | Điều phối viên sự kiện sẽ phối hợp việc đưa đón tất cả diễn giả. |
| courtesy-n | courtesy | polite behavior or a considerate action intended to show respect | As a courtesy, the hotel will provide a shuttle to the airport. | Để thể hiện sự chu đáo, khách sạn sẽ cung cấp xe đưa đón đến sân bay. |
| coverage-n | coverage | the protection or services included in an insurance or warranty plan; the area or amount included | The extended warranty provides coverage for parts and labor. | Gói bảo hành mở rộng bao gồm chi phí linh kiện và nhân công. |
| creditor-n | creditor | a person or organization to whom money is owed | The company negotiated a longer repayment period with its creditors. | Công ty đã đàm phán thời hạn trả nợ dài hơn với các chủ nợ. |
| deduct-v | deduct | to take an amount away from a total, salary, or payment | The employer will deduct income tax from each monthly salary. | Người sử dụng lao động sẽ khấu trừ thuế thu nhập từ mỗi tháng lương. |
| deduction-n | deduction | an amount that is subtracted from a total, especially for tax or another payment | The payslip shows a deduction for the employee’s health insurance. | Phiếu lương thể hiện khoản khấu trừ cho bảo hiểm y tế của nhân viên. |
| defective-adj | defective | not working correctly or not made properly because of a fault | Customers may return defective products within thirty days. | Khách hàng có thể trả lại sản phẩm bị lỗi trong vòng ba mươi ngày. |
| deficit-n | deficit | an amount by which expenses or demand are greater than income, supply, or available resources | The department must reduce its budget deficit before the next quarter. | Bộ phận phải giảm mức thâm hụt ngân sách trước quý tới. |
| delegate-v | delegate | to give a task or responsibility to another person, usually with the authority to complete it | The director decided to delegate routine approvals to the regional managers. | Giám đốc quyết định ủy quyền phê duyệt công việc thường lệ cho các quản lý khu vực. |
| deliverable-n | deliverable | a product, document, or result that must be provided as part of a project or agreement | The final report is the last deliverable under the consulting contract. | Báo cáo cuối cùng là sản phẩm bàn giao cuối cùng theo hợp đồng tư vấn. |
| departure-n | departure | the act or scheduled time of leaving a place | Passengers should arrive at the gate thirty minutes before departure. | Hành khách nên có mặt tại cửa khởi hành trước ba mươi phút. |
| disclose-v | disclose | to make information known, especially information that was previously private or secret | The applicant must disclose any conflicts of interest on the form. | Ứng viên phải công khai mọi xung đột lợi ích trên biểu mẫu. |
| discrepancy-n | discrepancy | a difference between two pieces of information or amounts that should match | The accountant found a discrepancy between the invoice and the purchase order. | Kế toán phát hiện sự sai lệch giữa hóa đơn và đơn đặt hàng. |
| distribute-v | distribute | to deliver or share goods, documents, or information among several people or places | Reception will distribute the updated visitor badges this afternoon. | Bộ phận lễ tân sẽ phát thẻ khách đã cập nhật vào chiều nay. |
| documentation-n | documentation | documents that provide information, evidence, or instructions about something | Please keep the shipping documentation for customs inspection. | Vui lòng lưu giữ hồ sơ chứng từ vận chuyển để phục vụ kiểm tra hải quan. |
| duplicate-adj | duplicate | exactly the same as another item, or repeated when only one copy is needed | The database detected duplicate customer records and flagged them for review. | Cơ sở dữ liệu phát hiện các hồ sơ khách hàng trùng lặp và đánh dấu để rà soát. |
| durable-adj | durable | able to last a long time without becoming damaged or worn out | The manufacturer uses durable materials for its outdoor equipment. | Nhà sản xuất sử dụng vật liệu bền cho thiết bị ngoài trời. |
| duration-n | duration | the length of time that an event, activity, or condition continues | The training course has a duration of two weeks. | Khóa đào tạo có thời lượng hai tuần. |
| efficiently-adv | efficiently | in a way that uses time, energy, or resources without unnecessary waste | The new software allows staff to process invoices more efficiently. | Phần mềm mới giúp nhân viên xử lý hóa đơn hiệu quả hơn. |
| electronic-adj | electronic | using a computer, digital system, or electronic equipment rather than paper or mechanical methods | Electronic receipts are sent automatically after each online purchase. | Biên lai điện tử được gửi tự động sau mỗi lần mua hàng trực tuyến. |
| eligibility-n | eligibility | the state of meeting the conditions required to receive or do something | Eligibility for the housing allowance depends on length of service. | Điều kiện được hưởng trợ cấp nhà ở phụ thuộc vào thâm niên công tác. |
| eligible-adj | eligible | meeting the conditions required to receive or do something | Employees who have completed six months of service are eligible for the benefit. | Nhân viên đã làm việc đủ sáu tháng sẽ đủ điều kiện nhận phúc lợi. |
| emission-n | emission | the release of gas, heat, light, or another substance into the environment | The factory must report its annual carbon emissions to the authorities. | Nhà máy phải báo cáo lượng khí thải carbon hằng năm cho cơ quan chức năng. |
| enclose-v | enclose | to put something inside an envelope or package with another item, or to surround something | Please enclose a copy of your receipt with the warranty claim. | Vui lòng gửi kèm một bản sao biên lai cùng yêu cầu bảo hành. |
| endorse-v | endorse | to publicly express support for something, or to sign a document to make it valid | The board voted to endorse the revised investment proposal. | Hội đồng đã bỏ phiếu tán thành đề xuất đầu tư đã sửa đổi. |
| enquiry-n | enquiry | a question or request for information about a product, service, or situation | Our sales team received an enquiry about bulk delivery rates. | Đội ngũ bán hàng nhận được yêu cầu thông tin về mức phí giao hàng số lượng lớn. |

## Kiểm soát chất lượng

- Kiểm tra nội dung theo nghĩa, từ loại và bối cảnh TOEIC; ví dụ phải tự nhiên, có bản dịch tương ứng.
- Không tự sinh IPA, CEFR hoặc quan hệ từ; giữ nguyên các trường này.
- Validator sau khi áp dụng phải có 0 ERROR. Chỉ siết baseline sau khi các nội dung đã được rà soát; không thêm lỗi mới.
