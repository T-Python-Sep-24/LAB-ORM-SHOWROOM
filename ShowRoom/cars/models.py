from django.db import models
from brands.models import Brand


class Color(models.Model):
    
    name = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    class DoorChoices(models.IntegerChoices):
        DOOR2 = 2, "Two Doors"
        DOOR3 = 3, "Three Doors"
        DOOR4 = 4, "Four Doors"
        DOOR5 = 5, "Five Doors"
        
    class Category(models.TextChoices):
        LUXURY = 'luxury', 'Luxury Car'
        FAMILY = 'family', 'Family Car'
        SPORT = 'sport', 'Super Sport Car'
        SEDAN = 'sedan', 'Sedan Car'
        SUV = 'suv', 'SUV'
        TRUCK = 'truck', 'Truck'
    
    name = models.CharField(max_length=1024)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True)
    colors = models.ManyToManyField(Color)
    engine = models.CharField(max_length=1024)
    doors = models.SmallIntegerField(choices=DoorChoices.choices)
    category = models.CharField(choices=Category.choices, max_length=48)    
    year = models.DateField()
    image = models.ImageField(upload_to="images/")
    
    def __str__(self) -> str:
        return f'{self.name} - {self.brand.name}'
    
    '''
    This is a model to represent cars, ex: Camry, Caprice, Model 3, etc.
It should at least have the following attributes: name, brand, colors,
photo, specs, model, ..... etc. You can add more.
Note: car model has a relation with Car model and Color model
(use appropriate relation types for each)
    '''