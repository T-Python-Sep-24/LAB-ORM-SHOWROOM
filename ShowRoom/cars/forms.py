from django import forms
from .models import Car, Color 

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'engine', 'performance', 'cargoSpace', 'infotainment', 'photo']

    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), widget=forms.CheckboxSelectMultiple)
    
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'hex_code']

