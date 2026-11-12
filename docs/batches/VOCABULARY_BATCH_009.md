# Vocabulary Quality Correction Batch 004 — v2.9.9

**Trạng thái:** Đã dry-run và áp dụng bằng `tools/patch-data.py`; đã chạy validator. Đây là working tree, chưa phải ZIP phát hành cuối.
**Nền dữ liệu:** v2.9.8, 928 ID; `baseDataVersion=2.9.8`; `idSetSha256` giữ nguyên.
**Phạm vi:** 40 headwords; sửa definition tiếng Anh và rà soát ví dụ/bản dịch theo ngữ cảnh TOEIC.
**Patch:** `patches/v2.9.9/batch-004.json` (120 thao tác).

Mỗi thao tác khóa theo ID, JSON Pointer và `expect.old`; trường definition còn kiểm tra POS. Patch hủy toàn batch nếu dữ liệu nền không khớp. Không thay đổi ID/POS/IPA/CEFR/schema hoặc dữ liệu cá nhân.

## Danh sách mục đã xử lý

| ID | Headword | Definition tiếng Anh mới | Ví dụ tiếng Anh | Bản dịch tiếng Việt |
|---|---|---|---|---|
| performance-n | performance | how well a person, team, or organization carries out a task or achieves its goals | The quarterly report shows a significant improvement in employee performance. | Báo cáo quý cho thấy hiệu suất làm việc của nhân viên được cải thiện đáng kể. |
| perishable-adj | perishable | likely to decay or become unsafe to eat after a relatively short time | The warehouse stores perishable products in temperature-controlled rooms. | Kho hàng bảo quản các sản phẩm dễ hư hỏng trong những phòng có kiểm soát nhiệt độ. |
| portfolio-n | portfolio | a collection of investments, projects, or examples of work held or presented by a person or organization | The investment firm reviewed each client’s portfolio before recommending changes. | Công ty đầu tư đã xem xét danh mục đầu tư của từng khách hàng trước khi đề xuất điều chỉnh. |
| postage-n | postage | the fee charged for sending a letter or package through the postal service | The online order confirmation states that postage will be added to the final cost. | Xác nhận đơn hàng trực tuyến cho biết phí gửi bưu chính sẽ được cộng vào tổng chi phí. |
| postponement-n | postponement | the act of arranging for an event or activity to take place at a later time | Due to severe weather, the postponement of the outdoor event was announced this morning. | Do thời tiết khắc nghiệt, việc hoãn sự kiện ngoài trời đã được thông báo sáng nay. |
| precaution-n | precaution | an action taken in advance to reduce the risk of harm, damage, or an unwanted problem | As a precaution, all visitors must sign in at the reception desk. | Để phòng ngừa rủi ro, tất cả khách đến thăm phải đăng ký tại quầy lễ tân. |
| premium-n | premium | an amount paid regularly for an insurance policy, or an additional charge for a higher level of service | The company will pay the annual insurance premium for all full-time employees. | Công ty sẽ thanh toán phí bảo hiểm hằng năm cho tất cả nhân viên toàn thời gian. |
| prescribe-v | prescribe | to state officially what must be done or what treatment or procedure should be followed | The safety regulations prescribe a monthly inspection of all lifting equipment. | Quy định an toàn yêu cầu kiểm tra hằng tháng toàn bộ thiết bị nâng. |
| priority-n | priority | something that is considered more important than other matters and should be dealt with first | Resolving the customer’s billing issue is our top priority today. | Giải quyết vấn đề thanh toán của khách hàng là ưu tiên hàng đầu của chúng ta hôm nay. |
| productivity-n | productivity | the rate at which work is completed or goods and services are produced | The new scheduling system has increased productivity across the service department. | Hệ thống lập lịch mới đã nâng cao năng suất trên toàn bộ bộ phận dịch vụ. |
| proficiency-n | proficiency | a high level of skill or ability in a particular subject or activity | The position requires proficiency in business English and spreadsheet software. | Vị trí này yêu cầu trình độ thành thạo tiếng Anh thương mại và phần mềm bảng tính. |
| proficient-adj | proficient | having the skill and ability needed to do something well | Applicants must be proficient in using common office applications. | Ứng viên phải thành thạo việc sử dụng các ứng dụng văn phòng phổ biến. |
| prolong-v | prolong | to make an activity, situation, or period of time continue for longer than expected | A shortage of replacement parts could prolong the equipment repair. | Tình trạng thiếu linh kiện thay thế có thể kéo dài việc sửa chữa thiết bị. |
| prolonged-adj | prolonged | continuing for a longer period than is usual or expected | The airport issued an apology after prolonged delays disrupted several flights. | Sân bay đã đưa ra lời xin lỗi sau khi tình trạng chậm trễ kéo dài làm gián đoạn một số chuyến bay. |
| promptly-adv | promptly | quickly and without unnecessary delay | Please forward the signed contract to our legal department promptly. | Vui lòng nhanh chóng chuyển hợp đồng đã ký đến bộ phận pháp lý của chúng tôi. |
| provisional-adj | provisional | temporary and intended to be confirmed, changed, or replaced later | The provisional schedule will be finalized after all department managers respond. | Lịch trình tạm thời sẽ được chốt sau khi tất cả trưởng bộ phận phản hồi. |
| qualification-n | qualification | a skill, experience, or certificate that makes someone suitable for a particular job or activity | Applicants should list each relevant qualification on the application form. | Ứng viên nên liệt kê từng bằng cấp và năng lực phù hợp trong mẫu đơn ứng tuyển. |
| reconciliation-n | reconciliation | the process of comparing two sets of financial records to make sure that they agree | The accounting team performs a bank reconciliation at the end of every month. | Nhóm kế toán thực hiện đối chiếu ngân hàng vào cuối mỗi tháng. |
| recurring-adj | recurring | happening repeatedly, often at regular intervals | The finance department monitors recurring payments for all company subscriptions. | Bộ phận tài chính theo dõi các khoản thanh toán định kỳ cho tất cả thuê bao của công ty. |
| reimburse-v | reimburse | to repay someone for money they have spent on an approved expense | Employees can submit receipts to be reimbursed for business travel costs. | Nhân viên có thể nộp hóa đơn để được hoàn trả chi phí đi công tác. |
| reliable-adj | reliable | able to be trusted to work correctly or to provide consistent and accurate results | We need a reliable supplier that can deliver office materials on schedule. | Chúng tôi cần một nhà cung cấp đáng tin cậy có thể giao vật tư văn phòng đúng lịch. |
| renew-v | renew | to extend the period for which an agreement, license, or document remains valid | The tenant must renew the office lease before the end of December. | Người thuê phải gia hạn hợp đồng thuê văn phòng trước cuối tháng Mười Hai. |
| renewal-n | renewal | the process of extending the period for which an agreement, license, or document remains valid | The renewal of the maintenance contract was approved by the director. | Việc gia hạn hợp đồng bảo trì đã được giám đốc phê duyệt. |
| replacement-n | replacement | a person or thing that takes the place of another that is missing, damaged, or no longer suitable | A replacement printer will be delivered to the branch by Friday. | Một máy in thay thế sẽ được giao đến chi nhánh trước thứ Sáu. |
| requirement-n | requirement | something that is necessary or must be done to meet a rule, standard, or need | A valid identification card is a requirement for entering the secure area. | Thẻ căn cước hợp lệ là yêu cầu bắt buộc để vào khu vực an ninh. |
| reschedule-v | reschedule | to arrange for an event or appointment to take place at a different time or date | The coordinator had to reschedule the interview because the manager was unavailable. | Điều phối viên phải sắp xếp lại lịch phỏng vấn vì quản lý không thể tham dự. |
| revision-n | revision | a change made to something after it has been reviewed, or a version containing such changes | The latest revision of the employee handbook includes the updated leave policy. | Bản chỉnh sửa mới nhất của sổ tay nhân viên bao gồm chính sách nghỉ phép đã cập nhật. |
| specify-v | specify | to state or describe something clearly and exactly | Please specify the quantity and delivery address when placing your order. | Vui lòng ghi rõ số lượng và địa chỉ giao hàng khi đặt đơn. |
| subscribe-v | subscribe | to arrange to receive a publication or service, usually by paying regularly | Customers can subscribe to the monthly industry newsletter on our website. | Khách hàng có thể đăng ký nhận bản tin ngành hằng tháng trên trang web của chúng tôi. |
| subscription-n | subscription | an arrangement in which someone pays regularly to receive a service or publication | The annual software subscription includes technical support and security updates. | Gói thuê bao phần mềm hằng năm bao gồm hỗ trợ kỹ thuật và các bản cập nhật bảo mật. |
| sufficient-adj | sufficient | as much as is needed for a particular purpose; enough | Please allow sufficient time for the shipment to clear customs. | Vui lòng dành đủ thời gian để lô hàng hoàn tất thủ tục thông quan. |
| sufficiently-adv | sufficiently | to the degree that is needed or adequate for a particular purpose | The conference room is sufficiently large to accommodate all registered guests. | Phòng hội nghị đủ rộng để bố trí chỗ cho tất cả khách đã đăng ký. |
| surcharge-n | surcharge | an extra amount of money added to the usual price or basic charge | A fuel surcharge may apply to deliveries outside the metropolitan area. | Phụ phí nhiên liệu có thể được áp dụng cho các chuyến giao hàng ngoài khu vực đô thị. |
| suspend-v | suspend | to stop an activity, service, or privilege temporarily, often until a problem is resolved | The airline will suspend the route while runway repairs are underway. | Hãng hàng không sẽ tạm ngừng tuyến bay trong thời gian sửa chữa đường băng. |
| suspension-n | suspension | the temporary stopping of an activity, service, or privilege | The temporary suspension of deliveries was announced after the warehouse fire. | Việc tạm ngừng giao hàng đã được thông báo sau vụ cháy nhà kho. |
| transact-v | transact | to carry out business or financial activities, especially by exchanging money or information | Customers can transact securely through the bank’s mobile application. | Khách hàng có thể thực hiện giao dịch an toàn thông qua ứng dụng di động của ngân hàng. |
| transit-n | transit | the process of being moved from one place to another, especially during transportation | The shipment is currently in transit and is expected to reach the regional depot tomorrow. | Lô hàng hiện đang trong quá trình vận chuyển và dự kiến đến kho khu vực vào ngày mai. |
| turnover-n | turnover | the total value of sales made by a business during a period, or the rate at which employees leave and are replaced | The retailer reported a 12 percent increase in annual turnover. | Nhà bán lẻ báo cáo doanh thu hằng năm tăng 12 phần trăm. |
| undergo-v | undergo | to experience or be subjected to a process, examination, or change | All new employees must undergo safety training before starting work. | Tất cả nhân viên mới phải trải qua khóa đào tạo an toàn trước khi bắt đầu công việc. |
| validity-n | validity | the state of being legally or officially acceptable, or the period during which something remains valid | Please check the validity of your access permit before entering the facility. | Vui lòng kiểm tra hiệu lực của giấy phép ra vào trước khi vào cơ sở. |

## Kiểm soát chất lượng

- Kiểm tra nội dung theo nghĩa, từ loại và bối cảnh TOEIC; ví dụ phải tự nhiên, có bản dịch tương ứng.
- Không tự sinh IPA, CEFR hoặc quan hệ từ; giữ nguyên các trường này.
- Validator sau khi áp dụng phải có 0 ERROR. Chỉ siết baseline sau khi các nội dung đã được rà soát; không thêm lỗi mới.
