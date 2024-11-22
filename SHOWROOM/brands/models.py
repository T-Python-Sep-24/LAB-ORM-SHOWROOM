from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=225)
    logo = models.ImageField(upload_to="images/", default="default.jpg")
    about = models.TextField()
    founded_at = models.PositiveIntegerField()
    country_of_origin = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.brand_name

