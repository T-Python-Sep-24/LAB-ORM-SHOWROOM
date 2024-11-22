from django import forms
from .models import Car, Color, VehiclePhoto
from django.forms import inlineformset_factory


class CarForm(forms.ModelForm):
    colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),  
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-control'
        }), 
        required=False 
    )

    class Meta:  
        model = Car
        fields = ['name', 'brand', 'photo', 'specs', 'model', 'segment', 'price', 'currency', 'colors']



class VehiclePhotoForm(forms.ModelForm):
    class Meta:
        model = VehiclePhoto
        fields = ['image']

VehiclePhotoInlineFormSet = inlineformset_factory(
    Car,
    VehiclePhoto,
    form=VehiclePhotoForm,
    extra=1,  
    can_delete=True, 
)


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'hexadecimal_color']
        widgets = {
            'hexadecimal_color': forms.TextInput(attrs={
                'type': 'color',  
                'class': 'form-control'  
            }),
        }

