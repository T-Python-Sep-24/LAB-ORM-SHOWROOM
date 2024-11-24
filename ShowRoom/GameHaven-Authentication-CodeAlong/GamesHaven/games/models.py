from django.db import models
from publishers.models import Publisher
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name

class Game(models.Model):

    class RatingChoices(models.IntegerChoices):
        STAR1 = 1, "One Star"
        STAR2 = 2, "Two Stars"
        STAR3 = 3, "Three Stars"
        STAR4 = 4, "Four Stars"
        STAR5 = 5, "Five Stars"

    
    class ESRBRating(models.TextChoices):
        E = "E", "Everyone"
        E10 = "E10",  "Everyone +10"
        T = "T", "Teen"
        M = "M", "Mature 17+"
        AO = "AO", "Adult Only 18+"
        RP = "RP", "Rating Pending"

    title = models.CharField(max_length=1024)
    description = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True)
    rating = models.SmallIntegerField(choices=RatingChoices.choices)
    release_date = models.DateField()
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    categories = models.ManyToManyField(Category)
    esrb = models.CharField(max_length=64, choices=ESRBRating.choices, default=ESRBRating.RP)


    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} on {self.game.title}"








