from django.db import models
from brands.models import Brand


class Color(models.Model):
    name = models.CharField(max_length=258, unique=True)
    hexCode = models.CharField(max_length=8, unique=True)
    image = models.ImageField(upload_to="images/colors/", default="images/default.jpg")

    def __str__(self) -> str:
        return f"{self.name}"


class Car(models.Model):
    class Gear(models.TextChoices):
        AUTO = "Automatic", "Automatic"
        MANUAL = "Manual", "Manual"

    class Fuel(models.TextChoices):
        ELECTRIC = "Electric", "Electric"
        GASOLINE = "Gasoline", "Gasoline"
    
    class BodyType(models.TextChoices):
        SUV = "SUV", "Suv"
        SEDAN = "Sedan", "Sedan"
        SPORT = "Sport", "Sport"
        PICKUP = "Pick-up", "Pick-up"
        CONVERTABLE = "Convertable", "Convertable"
        COUPE = "Coupe", "Coupe"
        MINIVAN = "Minivan", "Minivan"

    model = models.CharField(max_length=1024)
    modelYear = models.SmallIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True)
    topSpeed = models.CharField(max_length=258)
    engine = models.CharField(max_length=1024)
    gear = models.CharField(max_length=128, choices=Gear.choices)
    bodyType = models.CharField(max_length=128, choices=BodyType.choices)
    capacity = models.SmallIntegerField()
    fuel = models.CharField(max_length=128, choices=Fuel.choices)
    colors = models.ManyToManyField(Color)
    price = models.IntegerField()
    addedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.model}"
    

class Attachment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/cars/", default="images/default.jpg")

    def __str__(self) -> str:
        return f"Images for: {self.car}"
