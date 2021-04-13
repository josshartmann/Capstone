from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ShouldIEat(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    food = models.CharField(max_length=255)
    calories = models.IntegerField()
    weight = models.IntegerField()