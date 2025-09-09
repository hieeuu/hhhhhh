# store/urls.py
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),

    # CRUD cho Địa chỉ
    path('addresses/', views.address_list_view, name='address_list'),
    path('addresses/add/', views.address_create_view, name='address_create'),
    path('addresses/<int:pk>/edit/', views.address_update_view, name='address_update'),
    path('addresses/<int:pk>/delete/', views.address_delete_view, name='address_delete'),

    # URL Mua hàng
    path('checkout/', views.checkout_view, name='checkout'),
]