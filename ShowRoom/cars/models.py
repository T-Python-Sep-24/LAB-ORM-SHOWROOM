from django.db import models
from brands.models import Brand

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True) 
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self) -> str:
      return self.name

class Car(models.Model):
    name = models.CharField(max_length=100) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars') 
    colors = models.ManyToManyField(Color, related_name='cars')  
    photo = models.ImageField(upload_to='images/')  
    model_year = models.IntegerField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    fuel_type = models.BooleanField()  
    def __str__(self) -> str:
      return self.name
 
