from django.db import models
from brands.models import Brand
from django.utils import timezone

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)  
    
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, blank=True) 
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True, default='default.jpg')
    engine = models.TextField(default='')
    performance = models.TextField(default='')
    cargoSpace = models.TextField(default='')
    infotainment = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name