from django.db import models
from brands.models import Brand  # Import Brand model

# Color model
class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Color name (e.g., Red, Blue)
    hex_code = models.CharField(max_length=7, unique=True)  # Hexadecimal color code (e.g., #FF5733)

    def __str__(self):
        return self.name


# Car model
class Car(models.Model):
    name = models.CharField(max_length=128)  # Car name (e.g., Camry, Model 3)
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.CASCADE, 
        related_name='cars'
    )  # Relationship to Brand
    colors = models.ManyToManyField(
        Color, 
        related_name='cars'
    )  # Many-to-Many relation with Color
    photo = models.ImageField(upload_to="cars/photos/")  # Car photo
    specs = models.TextField()  # Specifications (e.g., engine, features)
    model = models.CharField(max_length=50)  # Car model year (e.g., 2023)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the car

    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.model})"
