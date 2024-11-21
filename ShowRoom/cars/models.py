from django.db import models
from brands.models import Brand
from colorfield.fields import ColorField

# Create your models here.

class Color(models.Model):

    name = models.CharField(max_length = 255)
    hexadeicml_color = ColorField()
    
class Car(models.Model):

    class Segment(models.TextChoices):
        
        ECONOMY = "economy" , "Economy"
        LUXURY = "luxury" , "Luxury"
        SPORTS = "sports" , "Sports"
        ELECTRIC = "electric" , "Electric"
        SEDAN = "sedan" , "Sedan"
        WAGON = 'wagon', 'Wagon'
        PREMIUM = 'premium', 'Premium'
        SUV = 'suv', 'Sport Utility Vehicle' 
        MINIVAN = 'minivan', 'Minivan'

    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images/")
    specs = models.TextField()
    model = models.CharField(max_length=255)
    segment = models.CharField(max_length=64, choices=Segment.choices)
    color = models.ManyToManyField(Color)

    def __str__(self): return self.name

