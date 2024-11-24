from django import forms
from games.models import Game

# Create the form class.
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        widgets = {
            'title' : forms.TextInput({"class" : "form-control"})
        }