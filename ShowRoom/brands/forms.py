from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'logo', 'about', 'founded_at', 'headquarters']
