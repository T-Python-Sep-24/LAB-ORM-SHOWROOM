from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, blank=True, null=True)
    photo = models.ImageField(upload_to="colors/", blank=True, null=True)

    PREDEFINED_COLORS = [
        {"name": "Red", "hex_code": "#FF0000"},
        {"name": "Blue", "hex_code": "#0000FF"},
        {"name": "Green", "hex_code": "#00FF00"},
        {"name": "Black", "hex_code": "#000000"},
        {"name": "White", "hex_code": "#FFFFFF"},
    ]
    
    @classmethod
    def initialize_colors(cls):
        for color_data in cls.PREDEFINED_COLORS:
            cls.objects.get_or_create(name=color_data["name"], hex_code=color_data["hex_code"])

    def __str__(self):
        return self.name

class Car(models.Model):
    class AvailabilityChoices(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        UNAVAILABLE = 'Unavailable', 'Unavailable'
        PRE_ORDER = 'Pre-order', 'Pre-order'


    car_name = models.CharField(max_length=1024)
    available_colors = models.ManyToManyField(Color, related_name="cars")
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1886), MaxValueValidator(2100)]
    )
    engine = models.CharField(max_length=255)  
    power = models.PositiveIntegerField(help_text="Power in horsepower (HP)")
    price = models.CharField(max_length=255)
    availability = models.CharField(
        max_length=50, 
        choices=AvailabilityChoices.choices
    )
    speed = models.PositiveIntegerField(help_text="Top speed in km/h or mph")
    image = models.ImageField(upload_to="images/", default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_name
