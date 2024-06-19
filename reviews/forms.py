from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Rating form"""

    class Meta:
        model = Review
        fields = ['rating']
        widgets = {
            'rating': forms.RadioSelect,
        }
