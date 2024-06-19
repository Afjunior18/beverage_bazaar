from django import forms
from .models import Wishlist


class WishlistForm(forms.ModelForm):
    """
    Form for creating or updating a Wishlist.
    """
    class Meta:
        model = Wishlist
        fields = []
