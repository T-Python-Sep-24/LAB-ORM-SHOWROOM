from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='brand_logo/',default="brand_logo/default.jpg")
    about = models.TextField()