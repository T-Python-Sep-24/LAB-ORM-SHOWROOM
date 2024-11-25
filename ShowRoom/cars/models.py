from django.db import models
from django.contrib.auth.models import User
from brands.models import Brand
# Create your models here.





class Color(models.Model):
    name=models.CharField(max_length=164)
    hex_code= models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.name


class Car (models.Model):
    name=models.CharField(max_length=164)
    model = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    doors = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specs = models.TextField()
    colors=models.ManyToManyField(Color, blank=True,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name="cars")
    class FuelChoices(models.TextChoices):
        PETROL='PET',"Petrol"
        DIESEL='DIE',"Diesel"
        ELECTRIC='ELE',"Electric"
        HYBRID='HYB',"Hybrid"
        GAS='GAS',"Gas"
        LPG='LPG', "LPG"
        CNG='CNG',"CNG"
    
    fuel=models.CharField(max_length=64,choices=FuelChoices.choices,default=FuelChoices.PETROL)

    def __str__(self) -> str:
        return self.name

class Photo (models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE,related_name='photos')
    image= models.ImageField(upload_to="images/",default='images/default.jpg')

    def __str__(self) -> str:
        return self.car.name
    

class Review(models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating= models.SmallIntegerField()
    comment= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} on {self.car.name}"