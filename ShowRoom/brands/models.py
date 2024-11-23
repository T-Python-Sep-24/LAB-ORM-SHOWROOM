from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/logos/', blank=True, null=True)
    about = models.TextField()
    founded_at = models.DateField()
    headquarters = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
