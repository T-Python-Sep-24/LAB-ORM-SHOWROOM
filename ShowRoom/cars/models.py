from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

#Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)

class Car(models.Model):
    name=models.CharField(max_length=1024)
    brand=models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='cars')
    colors = models.ManyToManyField(Color, related_name="cars")
    photo=models.ImageField(upload_to="images/", default="images/default.jpg")
    space=models.TextField()
    model_year=models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50, choices=[  
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid')
    ], default='Petrol')


class Review(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)