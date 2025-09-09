e-commerce-project/
│
├── .env                  # (Giai đoạn 1) Chứa các thông tin bí mật: database, email, secret key...
├── manage.py             # (Giai đoạn 1) Công cụ dòng lệnh của Django (dùng để runserver, migrate...).
├── requirements.txt      # (Giai đoạn 1) Liệt kê các thư viện Python cần cài (django, psycopg2...).
│
├── myproject/            # (Giai đoạn 1) Thư mục cấu hình chính của toàn bộ dự án.
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # (Giai đoạn 1) "Bộ não" của dự án: cấu hình database, apps, email, templates...
│   ├── urls.py           # (Giai đoạn 1) "Bảng chỉ đường" tổng, kết nối URL tới các app con.
│   └── wsgi.py
│
├── accounts/             # (Giai đoạn 1) App xử lý mọi thứ liên quan đến tài khoản người dùng.
│   ├── __init__.py
│   ├── admin.py          # (Giai đoạn 1) Khai báo model để hiển thị trên trang /admin.
│   ├── apps.py           # (Giai đoạn 1) Cấu hình app, nơi chúng ta import file signals.
│   ├── forms.py          # (Giai đoạn 1) Định nghĩa các form HTML, ví dụ form đăng ký.
│   ├── migrations/       # (Giai đoạn 1) Thư mục tự động tạo, chứa lịch sử thay đổi database.
│   │   └── __init__.py
│   ├── models.py         # (Giai đoạn 1) (Trống) vì ta dùng User model có sẵn của Django.
│   ├── signals.py        # (Giai đoạn 1) Logic chạy ngầm, ví dụ gửi email khi đăng nhập thành công.
│   ├── tests.py
│   ├── urls.py           # (Giai đoạn 1) "Bảng chỉ đường" cho các chức năng của app accounts.
│   └── views.py          # (Giai đoạn 1) Nơi chứa logic xử lý yêu cầu (request) của người dùng.
│
├── store/                # (Giai đoạn 1) App xử lý sách, địa chỉ, và các nghiệp vụ của cửa hàng.
│   ├── __init__.py
│   ├── admin.py          # (Giai đoạn 1) Đăng ký model Sách, Địa chỉ vào trang /admin.
│   ├── apps.py           # (Giai đoạn 1) Cấu hình app store.
│   ├── forms.py          # (Giai đoạn 1) Định nghĩa form Thêm/Sửa Địa chỉ.
│   ├── migrations/       # (Giai đoạn 1) Lịch sử thay đổi database cho model Sách, Địa chỉ.
│   │   └── __init__.py
│   ├── models.py         # (Giai đoạn 1) Định nghĩa cấu trúc dữ liệu cho Sách (Book) và Địa chỉ (Address).
│   ├── tests.py
│   ├── urls.py           # (Giai đoạn 1) "Bảng chỉ đường" cho các chức năng của app store.
│   ├── views.py          # (Giai đoạn 1) Logic xem sách, CRUD địa chỉ, xử lý mua hàng...
│   │
│   └── templates/        # (Giai đoạn 2) Thư mục chứa các file HTML dành riêng cho app store.
│       └── store/        # (Giai đoạn 2) Namespace - Thư mục con trùng tên app để tránh xung đột.
│           ├── address_confirm_delete.html
│           ├── address_form.html
│           ├── address_list.html
│           ├── book_list.html
│           ├── guest_checkout_form.html
│           └── payment.html
│
└── templates/            # (Giai đoạn 2) Thư mục chứa các file HTML dùng chung cho toàn bộ project.
    │
    ├── base.html         # (Giai đoạn 2) File "khung sườn" chung (menu, footer) cho tất cả các trang.
    │
    └── registration/     # (Giai đoạn 2) Thư mục đặc biệt chứa giao diện cho các tính năng auth có sẵn của Django.
        ├── login.html
        ├── password_reset_complete.html
        ├── password_reset_confirm.html
        ├── password_reset_done.html
        ├── password_reset_email.html
        ├── password_reset_form.html
        ├── password_reset_subject.txt  # File .txt này là tiêu đề email
        └── signup.html