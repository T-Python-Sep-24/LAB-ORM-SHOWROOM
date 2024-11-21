from django import forms
from .models import Contact

# Form for Contact model
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ="__all__"
