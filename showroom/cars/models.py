from django.db import models
from brands.models import Brand

class Color(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7)  # Hex code (e.g., #FFFFFF)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color)
    photo = models.ImageField(upload_to='cars/photos/')
    specs = models.TextField()
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name
