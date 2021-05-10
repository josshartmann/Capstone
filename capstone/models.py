from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    profession = models.CharField(max_length=55, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.URLField(max_length=300, default='https://icons-for-free.com/iconfiles/png/512/free+outline+people+profile+ui+icon-1320196081912311498.png')


class ShouldIEat(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    food = models.CharField(max_length=255)
    calories = models.IntegerField()
    weight = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

class Quotes(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=100)