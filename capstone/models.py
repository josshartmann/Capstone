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


class Profile(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()
    occupation = models.CharField(max_length=255)
    interests = models.CharField(max_length=255)
    about_me = models.CharField(max_length=255)
    profile_photo = models.URLField(max_length=200, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png')


class Quotes(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=100)