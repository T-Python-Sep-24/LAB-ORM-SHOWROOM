from django import forms
from .models import Car, Photo, Color

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'specs', 'model', 'price']
        widgets = {
            'colors': forms.CheckboxSelectMultiple(),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'hex_value']
        widgets = {
            'hex_value': forms.TextInput(attrs={'type': 'color'}),
        }