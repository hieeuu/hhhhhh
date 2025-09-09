# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Đưa các URL của app accounts vào project với tiền tố 'accounts/'
    path('accounts/', include('accounts.urls')),
    # Đưa các URL của app store vào project, đặt làm trang chủ
    path('', include('store.urls')),
]