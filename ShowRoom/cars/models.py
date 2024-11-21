from django.db import models

# Create your models here.
from brands.models import Brand 



class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)  
    photo = models.ImageField(upload_to='color_photos/', blank=True, null=True)  

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')  # علاقة مع Brand
    colors = models.ManyToManyField(Color, related_name='cars')  # علاقة مع Color
    photo = models.ImageField(upload_to='car_photos/') 
    specs = models.TextField()  # المواصفات
    model_year = models.PositiveIntegerField()  

    def __str__(self):
        return f"{self.name} ({self.model_year})"
