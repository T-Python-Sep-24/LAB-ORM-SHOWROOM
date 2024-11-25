from django.db import models
from django.contrib.auth.models import User
from brands.models import Brand

class Color(models.Model):
    BLACK = 'Black'
    WHITE = 'White'
    RED = 'Red'
    BLUE = 'Blue'

    COLOR_CHOICES = [
        (BLACK, 'Black'),
        (WHITE, 'White'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
    ]

    name = models.CharField(max_length=20, choices=COLOR_CHOICES, default=BLACK)
    hex_code = models.CharField(max_length=7, blank=True)
    rgb_value = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    colors = models.ManyToManyField(Color, related_name='cars')
    photo = models.ImageField(upload_to='cars/photos/')
    specs = models.TextField()
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.car.name} by {self.user.username}"
