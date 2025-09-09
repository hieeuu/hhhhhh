# store/models.py
from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title

class Address(models.Model):
    # Liên kết với User, có thể là NULL cho khách vãng lai
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    # có thể thêm state, zip_code... nếu cần

    def __str__(self):
        if self.user:
            return f"Địa chỉ của {self.user.username}"
        return f"Địa chỉ khách: {self.full_name}"