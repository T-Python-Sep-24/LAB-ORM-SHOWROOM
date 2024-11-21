from django.db import models
from brands.models import Brand
# Create your models here.


class Color(models.Model):

    name = models.CharField(max_length=50)
    hexadecimal = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Car(models.Model):

    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color)
    photo = models.ImageField(upload_to='images/', default="images/default.jpg")
    specs = models.TextField()
    model_year = models.SmallIntegerField()

    def __str__(self):
        return f"{self.model_year} {self.name}"
