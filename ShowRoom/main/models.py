from django.db import models
from cars.models import Car
# Create your models here.

class TestDriveRequest(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)