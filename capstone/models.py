from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ShouldIEat(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    food = models.CharField(max_length=255)
    calories = models.IntegerField()
    weight = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

class Quotes(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=100)