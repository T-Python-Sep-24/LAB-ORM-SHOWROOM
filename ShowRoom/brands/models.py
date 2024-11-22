from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/' , default="images/default.jpg")
    about = models.TextField()
    founded_at = models.DateField()

