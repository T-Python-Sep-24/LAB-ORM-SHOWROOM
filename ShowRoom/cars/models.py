from django.db import models
from brands.models import Brand
# Create your models here.


class Review(models.Model):

    class RatingChoics(models.IntegerChoices):
        OneStar = 1, 'one star'
        TwoStar = 2, 'two star'
        ThreeStar = 3, 'three star'
        FourStar = 4, 'four star'
        FiveStar = 5, 'five star'

    user = models.CharField(max_length=50)
    comment = models.TextField()
    rating = models.CharField(max_length=20, choices=RatingChoics.choices)

    def __str__(self):
        return self.user


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
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model_year} {self.name}"
