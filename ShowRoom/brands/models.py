from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=1024)
    logo = models.ImageField(upload_to="images/")
    about = models.TextField()
    founded_at = models.DateField()