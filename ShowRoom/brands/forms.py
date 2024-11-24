from django import forms
from .models import Brand

# Create the form class.
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {
            'name': forms.TextInput({"class": "form-control"}),
            'about': forms.Textarea({"class": "form-control", "rows": 4}),
            'founded_at': forms.DateInput({"class": "form-control", "type": "date"}),
        }


