from django.db import models
from brands.models import Brand
# Create your models here.


class Color(models.Model):
    name=models.CharField(max_length=50)
    hex_value=models.CharField(max_length=7)

class Car(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images/') 
    specs=models.TextField()
    model=models.CharField(max_length=50)
    colors=models.ManyToManyField(Color)
    brand=models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='cars')

    


