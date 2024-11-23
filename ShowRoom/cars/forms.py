from django import forms
from .models import Car,Color

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'photo', 'specs', 'model', 'price']
    widgets = {
            'colors': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['colors'].queryset = Color.objects.all()
        self.fields['colors'].widget.attrs.update({'class': 'form-check-input'})