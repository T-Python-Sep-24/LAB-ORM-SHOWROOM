from django.db import models
from django.urls import reverse

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/')
    about = models.TextField(blank=True)
    founded_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', args=[self.id])

    @property
    def car_count(self):
        return self.cars.count()  # Count of related cars

