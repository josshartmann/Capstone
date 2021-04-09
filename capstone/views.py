from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

from .models import User


def index(request):
    if request.user.is_authenticated:
        return render(request, "capstone/home.html")
    else:
        return render(request, "capstone/index.html")


@login_required(login_url='login')
def home(request):
    return render(request, "capstone/home.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/index.html", {
                "message": "Passwords must match."
            })
        
        # attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/index.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, "capstone/index.html")


def login_view(request):
    if request.method == "POST":
        # attempt to sign user id
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "capstone/index.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def shouldIEat(request):
    return render(request, "capstone/should-i-eat.html")


def results(request):
    if request.method == "POST":
        food = request.POST["food"]
        calories = request.POST["calories"]
        weight = request.POST["weight"]

        met = [13.5, 10, 8, 7, 4.8, 4,2]

        resultHours = []
        resultMinutes = []

        for i in met:
            duration = (int(calories) * 200) / (i * 3.5 * int(weight))
            duration = round(duration)

            hours = int(duration/60)
            minutes = duration % 60

            minutes = format(minutes, '02d')

            resultHours.append(hours)
            resultMinutes.append(minutes)
        
        return render(request, "capstone/results.html", {
            "food": food,
            "calories": calories,
            "hours": resultHours,
            "minutes": resultMinutes,
        })