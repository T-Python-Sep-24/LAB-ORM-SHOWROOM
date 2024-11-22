from django import forms

from cars.models import Color,Photo,Car

# Create the form class
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = "__all__"