from django.db import models
from brands.models import Brand

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex_code = models.CharField(max_length=7, unique=True, blank=True, null=True)  # Store the hexadecimal code for the color (e.g., #FF5733)

    def __str__(self):
        return self.name

class Car(models.Model):
    class CarType(models.TextChoices):
        SEDAN = 'Sedan', 'Sedan'
        SUV = 'SUV', 'SUV'
        COUPE = 'Coupe', 'Coupe'
        HATCHBACK = 'Hatchback', 'Hatchback'
        CONVERTIBLE = 'Convertible', 'Convertible'
        TRUCK = 'Truck', 'Truck'
        VAN = 'Van', 'Van'
        OTHER = 'Other', 'Other'

    name = models.CharField(max_length=255)
    brand = models.ForeignKey('brands.Brand', on_delete=models.CASCADE, related_name='cars')
    colors = models.ManyToManyField('Color')
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)
    specs = models.TextField()
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.CharField(
        max_length=50,
        choices=CarType.choices,
        default=CarType.OTHER
    )

    def __str__(self):
        return self.name