from django.db import models
from brands.models import Brand
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7)  
    
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, blank=True) 
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True, default='default.jpg')
    engine = models.TextField(default='')
    performance = models.TextField(default='')
    cargoSpace = models.TextField(default='')
    infotainment = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return f'Review for {self.car.name} by {self.user.username}'