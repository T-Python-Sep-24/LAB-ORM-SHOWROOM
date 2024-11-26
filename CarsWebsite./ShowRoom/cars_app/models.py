from django.db import models
from brands_app.models import Brand
from django.urls import reverse

class Color(models.Model):
    name = models.CharField(max_length=50)
    rgb = models.CharField(max_length=7, help_text="RGB format (e.g., #FF5733)")
  

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    color = models.ManyToManyField(Color, related_name='cars')  # Many-to-many relation with Color
    photo = models.ImageField(upload_to='images/' , default="images/default.jpg")
    specs = models.TextField(blank=True)
    model_year = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_detail', args=[self.id])