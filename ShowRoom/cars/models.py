from django.db import models
from brands .models import Brand
# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=100)  
    hex_value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)  
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')  # Many-to-One with Brand
    colors = models.ManyToManyField(Color, related_name='cars')  # Many-to-Many with Color
    photo = models.ImageField(upload_to='images/' , default="images/default.jpg") 
    specs = models.TextField()  # Specifications for the car
    model_year = models.DateField()

    def __str__(self) -> str:
        return self.name