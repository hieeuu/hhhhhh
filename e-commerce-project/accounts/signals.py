# accounts/signals.py
from django.core.mail import send_mail
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.conf import settings

@receiver(user_logged_in)
def send_login_notification(sender, request, user, **kwargs):
    """
    Gửi email thông báo khi người dùng đăng nhập thành công.
    """
    subject = 'Đăng nhập thành công vào hệ thống'
    message = f'Chào {user.username},\n\nBạn vừa đăng nhập thành công vào website của chúng tôi. Nếu không phải là bạn, vui lòng liên hệ hỗ trợ ngay lập tức.\n\nTrân trọng.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        # Ghi lại lỗi nếu cần, ví dụ: print(f"Lỗi gửi mail: {e}")
        pass # Bỏ qua lỗi để không làm gián đoạn quá trình login