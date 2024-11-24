from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/logos/')
    about = models.TextField()
    founded_at = models.DateField()
    
    def __str__(self):
        return self.name
