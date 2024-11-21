from django import forms
from .models import Brand

# Form for Brand and model
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields ="__all__"