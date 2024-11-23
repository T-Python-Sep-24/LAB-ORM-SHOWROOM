from django.db import models

# Create your models here.


class Brand(models.Model):

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="images/")
    about = models.TextField()
    founded_at = models.DateField()
    origin = models.CharField(max_length=255)
    
    def get_car_count(self):
        return self.cars.count()
    def __str__(self): return self.name
    