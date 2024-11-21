from django import forms
from .models import Car


# Create the form class.
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'name': forms.TextInput({"class": "form-control"}),
            'specs': forms.Textarea({"class": "form-control", "rows": 3}),
            'model_year': forms.NumberInput({"class": "form-control"}),
        }

