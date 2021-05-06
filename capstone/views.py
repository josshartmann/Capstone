import requests
import random
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .models import User, ShouldIEat, Quotes, Profile


def index(request):
    if request.user.is_authenticated:
        user = request.user
        

        quotes = Quotes.objects.all()
        random_quote = random.choice(quotes)

        profile = Profile.objects.get(user=user)

        return render(request, "capstone/home.html", {
            "random_quote": random_quote,
            "profile": profile,
        })
    else:
        return render(request, "capstone/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        profession = request.POST["profession"]
        phone = request.POST["phone"]
        birth_date = request.POST["birth-date"]

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

            ins = Profile(user=user, first_name=first_name, last_name=last_name, phone=phone, profession=profession, birth_date=birth_date)
            ins.save()
        except IntegrityError:
            return render(request, "capstone/index.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse('index'))
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
            return HttpResponseRedirect(reverse("index"))
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

        met = [13.5, 10, 8, 7, 4.8, 4, 2]

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
            "weight": weight,
        })


def saveResults(request):
    if request.method == "POST":
        food = request.POST["food"]
        calories = request.POST["calories"]
        weight = request.POST["weight"]
        user = request.user

        ins = ShouldIEat(user=user, food=food, calories=calories, weight=weight)
        ins.save()
        
        return HttpResponseRedirect(reverse("log"))


def log(request):
    if request.method == "POST":
        user = request.user
        cheats = ShouldIEat.objects.filter(user=user)

        cheat = request.POST["row_delete"]
        
        ShouldIEat.objects.get(id=cheat).delete()

        return render(request,"capstone/log.html", {
            "cheats":cheats
            })
    else:
        user = request.user
        cheats = ShouldIEat.objects.filter(user=user)
        
        return render(request,"capstone/log.html", {
            "cheats":cheats
        })


def workoutGenerator(request):
    if request.method == "POST":

        workout = request.POST.getlist('workout')

        chest = ["Flat Barbell or Dumbbell Bench Press", "Dips (on parallel bars with slight forward lean)", "Push-Ups", "Incline Dumbbell Flyes", "Staggered press-up"]
        back = ["Pull-Ups", "Lat Pull-Downs", "Bent Over Barbell or Dumbbell Rows", "T-Bar Rows", "Barbell, Dumbbell or Machine Shrugs"]
        shoulders = ["Barbell Overhead Shoulder Press", "Seated Dumbbell Shoulder Press", "Front Raise", "Reverse Pec Deck Fly", "Bent-Over Dumbbell Lateral Raise"]
        legs = ["Barbell or Dumbbell Squats", "Barbell or Dumbbell Lunges", "Leg Press", "Machine Squat/Hack Squat", "Step-ups"]
        biceps = ["Standing Barbell or Dumbbell Curls", "Barbell or Dumbbell Preacher Curls", "Hammer Curls", "Concentration Curl", "Reverse-Grip Bent-Over Row"]
        triceps = ["Flat Close Grip Bench Press", "Close Grip Push-Ups", "Skull Crushers", "Overhead Barbell or Dumbbell Triceps Extensions", "Bench Dips"]
        abdominal = ["Plank", "Hand slide crunch", "Mountain climber", "Reverse crunch", "Dead bug", "Bird-dog", "Flutter kicks"]
        
        n = 0
        workout_list = []

        if len(workout) == 1:
            n = 5
        elif len(workout) == 2:
            n = 4
        elif len(workout) == 3:
            n = 3
        elif len(workout) == 4:
            n = 2
        else:
            n = 1


        if 'chest' in workout:
            for i in range(n):
                workout_list.append(chest[i])
        if 'back' in workout:
            for i in range(n):
                workout_list.append(back[i])
        if 'shoulders' in workout:
            for i in range(n):
                workout_list.append(shoulders[i])
        if 'legs' in workout:
            for i in range(n):
                workout_list.append(legs[i])
        if 'biceps' in workout:
            for i in range(n):
                workout_list.append(biceps[i])
        if 'triceps' in workout:
            for i in range(n):
                workout_list.append(triceps[i])
        if 'abdominals' in workout:
            for i in range(n):
                workout_list.append(abdominal[i])

        n = 0

        return render(request, 'capstone/workout.html', {
            "workout_list": workout_list,
        })
    else:
        return render(request, 'capstone/workout-generator.html')



def edit(request):
    if request.method == "POST":
        user = request.user
        email = request.POST["editEmail"]
        phone = request.POST["editPhone"]
        profession = request.POST["editProfession"]

        profile = Profile.objects.get(user=user)

        profile.phone = phone
        profile.profession = profession
        profile.save()

        user = User.objects.get(username=user)
        user.email = email
        user.save()

        return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)