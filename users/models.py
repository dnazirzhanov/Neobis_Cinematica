from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class BonusCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s bonus card"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s feedback"

