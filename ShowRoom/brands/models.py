from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)
    about = models.TextField()
    founded_at = models.IntegerField()
    headquarters = models.CharField(max_length=255)

    def __str__(self):
        return self.name
