from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form for creating or updating a product.
    """
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'region',
                  'price', 'rating', 'sku', 'image']
