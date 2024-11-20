from django.db import models

# Create your models here.


class Brand(models.Model):

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
    logo = models.ImageField(upload_to="images/")
    about = models.TextField()
    founded_at = models.DateField()
    origin = models.CharField(max_length=255)
    segment = models.CharField(max_length=64, choices=Segment.choices)
    
    def __str__(self): return self.name
    