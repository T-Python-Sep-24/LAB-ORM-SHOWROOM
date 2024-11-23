from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand 
        fields ="__all__"
        widgets = {
            'founded_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }