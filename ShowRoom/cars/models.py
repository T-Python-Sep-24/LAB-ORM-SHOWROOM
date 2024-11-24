from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User


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
    brand = models.ForeignKey(Brand,related_name='cars', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images/")
    specs = models.TextField()
    model = models.CharField(max_length=254)
    segment = models.CharField(max_length=64, choices=Segment.choices)
    color = models.ManyToManyField(Color)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    currency = models.CharField(max_length=5, default='SAR')

    def __str__(self): return self.name

class Review(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    car = models.ForeignKey(Car ,related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i,i )for i in range(1,6)])
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.car.name}"
    
    class Meta:
        ordering = ['created_at']

class VehiclePhoto(models.Model):
    car = models.ForeignKey(Car ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to= "images/")