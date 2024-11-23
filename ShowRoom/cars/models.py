from django.db import models
from brands.models import Brand

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='colors/photos/', blank=True, null=True)  # Path to upload color swatches
    hex_code = models.CharField(max_length=7, unique=True, blank=True, null=True)  # Store the hexadecimal code for the color (e.g., #FF5733)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE, related_name='cars')
    colors = models.ManyToManyField('Color', related_name='cars')
    photo = models.ImageField(upload_to='cars/photos/', blank=True, null=True)
    specs = models.TextField(default="No specifications provided")  # Add default value
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
