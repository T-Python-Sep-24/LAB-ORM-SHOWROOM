from django import forms
from .models import Car, Color

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = [
            "name",
            "hexadecimal",

        ]

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            "name",
            "brand",
            "colors",
            "photo",
            "specs",
            "model_year"
        ]