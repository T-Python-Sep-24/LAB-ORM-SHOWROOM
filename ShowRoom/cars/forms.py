from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'photo', 'specs', 'model', 'price']