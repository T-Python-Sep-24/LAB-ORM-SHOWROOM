from django import forms
from .models import Car , Color

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'photo', 'year', 'price', 'car_type']


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'hex_code']
