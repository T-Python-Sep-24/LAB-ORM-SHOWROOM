from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/')
    about = models.TextField()
    found_at = models.DateField(null=True)
    
    def __str__(self):
        return self.name

