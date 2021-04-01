from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError

from .models import User

def index(request):
    return HttpResponse("index")

def home(request):
    return HttpResponse("in-homepage")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })
        
        # attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })

        return render(request, "capstone/register.html", {
            "message": "ok-register"
        })
    else:
        return render(request, "capstone/register.html")

def login(request):
    return render(request, "capstone/login.html")