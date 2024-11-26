from django import forms
from .models import Car
from .models import Color

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'photo','color' ,'specs', 'model_year']

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'rgb']  