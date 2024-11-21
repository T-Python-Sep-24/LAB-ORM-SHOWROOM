from django import forms
from .models import TestDriveRequest


class TestDriveRequestForm(forms.ModelForm):
    class Meta:
        model = TestDriveRequest
        fields = [
            'name',
            'email',
            'car'
            'created_at'
        ]