from django.db import models
from brands.models import Brand  # Import Brand model
from django.contrib.auth.models import User


# Color model
class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Color name (e.g., Red, Blue)
    hex_code = models.CharField(max_length=7, unique=True, null=True, blank=True)  # Hexadecimal color code (e.g., #FF5733)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)  # Photo representing the color

    def __str__(self):
        return f"{self.name} ({self.hex_code})"  # Showing both name and hex code in the string representation



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
    photo = models.ImageField(upload_to="photos/")  # Car photo
    specs = models.TextField()  # Specifications (e.g., engine, features)
    model = models.CharField(max_length=50)  # Car model year (e.g., 2023)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the car

    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.model})"
    
class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # You can set a range for ratings, like 1-5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.car.name}'