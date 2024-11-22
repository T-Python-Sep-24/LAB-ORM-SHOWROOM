from django.db import models
from brands.models import Brand

# Create your models here.

class Color(models.Model):

    name = models.CharField(max_length = 255)
    hexadecimal_color = models.CharField(max_length=7)

    def __str__(self):
        return self.name 
    
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
        CROSSOVER = 'crossover', 'Crossover'

    name = models.CharField(max_length=254)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images/")
    specs = models.TextField()
    model = models.CharField(max_length=254)
    segment = models.CharField(max_length=64, choices=Segment.choices)
    color = models.ManyToManyField(Color)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    currency = models.CharField(max_length=5, default='SAR')

    def __str__(self): return self.name


class VehiclePhoto(models.Model):
    car = models.ForeignKey(Car ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to= "images/")