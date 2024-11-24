from django import forms
from .models import Brand , Review
from django.core.validators import MinValueValidator, MaxValueValidator


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'logo', 'about']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review...'}),
        }

    rating = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        widget=forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
        required=True
    )

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError('The rating must be between 1 and 5')
        return rating
