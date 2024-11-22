from django.db import models
from brands_app.models import Brand 

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)  # For Hexadecimal color

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')  # ForeignKey to Brand
    colors = models.ManyToManyField(Color)  # ManyToManyField to Color
    photo = models.ImageField(upload_to='images/')
    specs = models.TextField()
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name
