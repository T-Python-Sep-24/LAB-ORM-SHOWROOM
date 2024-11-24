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
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')  
    colors = models.ManyToManyField(Color, related_name='cars')  
    photo = models.ImageField(upload_to='car_photos/') 
    specs = models.TextField()  
    model_year = models.PositiveIntegerField()  

    def __str__(self):
        return f"{self.name} ({self.model_year})"
