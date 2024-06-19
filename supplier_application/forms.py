from django import forms
from .models import SupplierApplication


class SupplierApplicationForm(forms.ModelForm):
    """
    Form class for creating or updating a SupplierApplication.
    """

    class Meta:
        model = SupplierApplication
        fields = [
            'name',
            'email',
            'phone_number',
            'company_name',
            'product_description',
        ]
