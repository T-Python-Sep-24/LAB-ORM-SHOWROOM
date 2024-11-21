from django.db import models
from brands.models import Brand


# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    colors = models.ManyToManyField('Color', related_name='cars')

    def __str__(self):
        return f"{self.model} ({self.brand.name})"
