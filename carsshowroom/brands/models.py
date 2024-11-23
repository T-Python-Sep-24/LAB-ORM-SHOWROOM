from django.db import models

# Create your models here.


class Brand(models.Model):


    name=models.CharField(max_length=1024)
    logo=models.ImageField(upload_to='images/')
    about=models.TextField()
    founded_at=models.DateField()
    