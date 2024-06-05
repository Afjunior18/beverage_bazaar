from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 5)]),
            'review_comment': forms.Textarea(attrs={'rows': 3}),
        }