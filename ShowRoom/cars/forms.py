from django import forms
from .models import Car, Color, VehiclePhoto ,Review
from django.forms import inlineformset_factory


class CarForm(forms.ModelForm):


    class Meta:  
        model = Car
        fields = ['name', 'brand', 'photo', 'specs', 'model', 'segment', 'price', 'currency', 'color']
    color = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), widget=forms.CheckboxSelectMultiple)


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your review...', 'rows': 4}))
    rating = forms.ChoiceField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], widget=forms.Select)
    
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
