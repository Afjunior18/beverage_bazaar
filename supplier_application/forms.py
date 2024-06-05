from django import forms
from .models import SupplierApplication

class SupplierApplicationForm(forms.ModelForm):
    class Meta:
        model = SupplierApplication
        fields = ['name', 'email', 'phone_number', 'company_name', 'product_description']