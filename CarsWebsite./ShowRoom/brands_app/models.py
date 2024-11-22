from django.db import models
from django.urls import reverse

class Brand(models.Model):
    class BrandType(models.TextChoices):
        BMW = 'BMW', 'BMW'
        MAZDA = 'MAZDA', 'Mazda'
        TOYOTA = 'TOYOTA', 'Toyota'
        MERCEDES = 'MERCEDES', 'Mercedes'
        JEEP = 'JEEP', 'Jeep'
        FORD = 'FORD', 'Ford'
        DODGE = 'DODGE', 'Dodge'

    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/')
    about = models.TextField(blank=True)
    founded_at = models.DateField(null=True, blank=True)
    brand_type = models.CharField(max_length=20, choices=BrandType.choices, default=BrandType.BMW)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', args=[self.id])

    @property
    def car_count(self):
        return self.cars.count()  # Count of related cars