from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'brand', 'colors', 'photo', 'specs', 'model', 'price']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        # Apply the 'form-control' class to each field
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'