from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="images/usersAvatars/", default="images/usersAvatars/defaultAvatar.png")

    def __str__(self) -> str:
        return f'Profile {self.user.username}'