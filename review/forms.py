from .models import Review, Contact, Subscriber
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        widgets = {
            'review': forms.Textarea(attrs={'placeholder': 'Write your Review '})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            'f_name': forms.TextInput(attrs={'placeholder': 'Your First name ', 'class': 'col-md-6 form-group', 'value': 'name'}),
            'l_name': forms.TextInput(attrs={'placeholder': 'Your Last name ', 'class': 'col-md-6 form-group' }),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email Address ', 'class': 'form-group'}),
            'tel_no': forms.TextInput(attrs={'placeholder': 'Your Digits ', 'class': 'form-group'}),
            'message': forms.Textarea(attrs={'placeholder': 'What\'s on your mind ?  ', 'class': 'form-group'})
        }


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ("email", )

