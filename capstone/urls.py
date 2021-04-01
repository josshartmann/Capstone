from django.urls import path
from capstone import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
]