from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        widgets = {
            'review': forms.Textarea(attrs={'placeholder': 'Write your Review '})
        }
