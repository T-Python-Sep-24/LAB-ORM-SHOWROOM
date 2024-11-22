from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=128, unique=True)
    logo = models.ImageField(upload_to="images/", default="images/default.png")
    about= models.TextField()
    founded_at = models.DateField()


    def __str__(self) -> str:
        return self.name
    
    def car_count(self):
        return self.car_set.count()  # Count cars related to the brand