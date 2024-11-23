from django.db import models
from brands.models import Brand

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=256)
    hexadecimal = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    name = models.CharField(max_length=256)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True)
    colors = models.ManyToManyField(Color)
    photo = models.ImageField(upload_to="images/", default="images/default.jpg")
    specs = models.TextField()
    model = models.IntegerField()

    def __str__(self):
        return self.name