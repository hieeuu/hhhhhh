# store/forms.py
from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        # Không bao gồm trường 'user' vì nó sẽ được gán tự động trong view
        fields = ['full_name', 'phone_number', 'street_address', 'city']