from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """
    A class to generate form from Contact Model
    """
    class Meta:
        model = ContactModel
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'message'
        )
