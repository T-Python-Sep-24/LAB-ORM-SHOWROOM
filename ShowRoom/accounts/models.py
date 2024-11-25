from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="images/usersAvatars/", default="images/usersAvatars/defaultAvatar.png")

    def __str__(self) -> str:
        return f'Profile {self.user.username}'
    
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    addedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Bookmark for {self.user.username}'
