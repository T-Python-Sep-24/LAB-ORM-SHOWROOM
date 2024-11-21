from django.db import models

class Brand(models.Model):
    logo = models.ImageField(upload_to="images/brands/", default="images/default.jpg")
    name = models.CharField(max_length=256)
    about = models.TextField()
    headquarters = models.CharField(max_length=1024)
    founder = models.CharField(max_length=256)
    founded = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}"
