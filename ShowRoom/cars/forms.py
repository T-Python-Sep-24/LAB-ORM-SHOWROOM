from django import forms
from .models import Car, Color 

# Forms for Car and Color models
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields ="__all__"

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields ="__all__"
