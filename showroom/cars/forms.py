from django import forms
from .models import Car, Color

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'photo', 'specs', 'model']


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'color_code']
