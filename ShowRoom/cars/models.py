from django.db import models
from brands .models import Brand
# Create your models here.
from django.contrib.auth.models import User 

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
    specs = models.TextField()  
    model_year = models.DateField()

    def __str__(self) -> str:
        return self.name
    
class Rview(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)