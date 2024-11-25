from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User
# Create your models here.


class Color(models.Model):

    name = models.CharField(max_length=50)
    hexadecimal = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Car(models.Model):

    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color)
    photo = models.ImageField(upload_to='images/', default="images/default.jpg")
    specs = models.TextField()
    model_year = models.SmallIntegerField()


    def __str__(self):
        return f"{self.model_year} {self.name}"

class CarReview(models.Model):

    class Rates(models.IntegerChoices):

        STAR1 = 1, 'One Star'
        STAR2 = 2, 'Two Stars'
        STAR3 = 3, 'Three Stars'
        STAR4 = 4, 'Four Stars'
        STAR5 = 5, 'Five Stars'

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=Rates.choices)
    comment = models.TextField()
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.car.name}"