from django.urls import path
from capstone import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("should-i-eat", views.shouldIEat, name="shouldIEat"),
    path("results", views.results, name="results"),
    path("save-results", views.saveResults, name="saveResults"),
    path("log", views.log, name="log"),
    path("workout-generator", views.workoutGenerator, name="workoutGenerator"),
    path("edit", views.edit, name="edit"),
    path("edit2", views.edit2, name="edit2"),
]