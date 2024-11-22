from django import forms
from .models import Brand

# Form for Brand model
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields ="__all__"