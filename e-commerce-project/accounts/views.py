# accounts/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login') # Sau khi đăng ký thành công, chuyển đến trang đăng nhập
    template_name = 'registration/signup.html' # Sẽ tạo file này ở phần frontend