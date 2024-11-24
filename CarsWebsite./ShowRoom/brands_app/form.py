from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'logo', 'about', 'founded_at', 'brand_type']
        widgets = {
            'founded_at': forms.DateInput(attrs={'type': 'date'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }