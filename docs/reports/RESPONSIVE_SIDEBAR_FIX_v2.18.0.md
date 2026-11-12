# Responsive Sidebar Fix — v2.18.0

Ngày: 11/11/2026  
Phạm vi: desktop/laptop, đặc biệt viewport chiều cao thấp ở mức zoom 100%.

## Vấn đề

Ở một số laptop 15,6 inch (ví dụ viewport CSS gần 1366×768 sau khi tính vùng hiển thị của trình duyệt), menu bên trái có thể chiếm hết chiều cao. Khi đó khối thông tin cuối menu — **Dữ liệu cục bộ**, **Lưu riêng trên thiết bị**, và dòng phiên bản/host — bị đẩy ra ngoài hoặc không còn nhìn thấy ở mức zoom 100%.

## Thay đổi

- Tại desktop `min-width: 851px`, sidebar dùng `100dvh` (có fallback `100vh`) và không cho nội dung tràn khỏi khung sidebar.
- `.side-nav` trở thành vùng flex có `min-height: 0` và `overflow-y: auto`; khi menu dài, chỉ danh sách điều hướng cuộn.
- `.sidebar-bottom` không co lại, được đẩy xuống đáy sidebar và giữ nền riêng để không bị menu phủ lên.
- Khi chiều cao viewport ≤820 CSS px, giảm padding, khoảng cách menu và chiều cao dòng. Ở ≤680 CSS px, áp dụng compact mode mạnh hơn.
- Nội dung trạng thái cuối menu không bị `display:none`, không bị cắt chữ và không phụ thuộc vào zoom 90%.
- Không thay đổi hành vi icon rail tablet 641–850 px hoặc mobile navigation.

## Kiểm thử tĩnh

Hai regression tests được thêm vào `tools/tests/test_design_system.py` để kiểm tra footer sidebar luôn được giữ và nav có thể cuộn độc lập; cả hai nằm trong nhóm test nhanh đã PASS. Ngoài ra, script cuối xác nhận ba chuỗi trạng thái hiện diện trong `index.html`, 74/74 APP_SHELL path tồn tại và JavaScript/CSS liên quan không bị thay đổi ngoài dự kiến.

## Giới hạn xác minh

Chưa có trình duyệt đồ họa được phép chạy trong sandbox để chụp màn hình hoặc tương tác thật. Vì vậy **chưa tuyên bố đã xác minh trực quan ở zoom 100% trên laptop 15,6 inch**. Người dùng cần push/deploy rồi kiểm tra ở zoom 100%; nếu footer vẫn bị ẩn, cần ảnh chụp toàn màn hình kèm kích thước viewport để điều chỉnh theo đúng môi trường.
