from django import forms
from cars.models import Car,Color



class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = "__all__"
