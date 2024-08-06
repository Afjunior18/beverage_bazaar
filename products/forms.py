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
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Price cannot be negative')
        return price

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and rating < 0:
            raise forms.ValidationError('Rating cannot be negative')
        return rating
