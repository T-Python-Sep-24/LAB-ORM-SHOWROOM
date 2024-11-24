from django.db import models

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=164)
    logo=models.FileField(upload_to="images/")
    about=models.TextField()
    found_at= models.DateField()

    def __str__(self) -> str:
        return self.name
