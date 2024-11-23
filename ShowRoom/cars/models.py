from django.db import models
from brands.models import Brand

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_value = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    

    
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    colors = models.ManyToManyField(Color, related_name="cars")
    specs = models.TextField()
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.brand.name})"



class Photo(models.Model):
    car = models.ForeignKey(Car, related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="car_photos/")