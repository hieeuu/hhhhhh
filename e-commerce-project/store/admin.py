# store/admin.py
from django.contrib import admin
from .models import Book, Address

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    search_fields = ('title', 'author')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'phone_number')
    list_filter = ('city',)
    search_fields = ('user__username', 'full_name', 'phone_number')