from django.contrib import admin
from .models import User, ShouldIEat, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")


class ShouldIEatAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "food", "calories", "weight")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name")


admin.site.register(User, UserAdmin)
admin.site.register(ShouldIEat, ShouldIEatAdmin)
admin.site.register(Profile, ProfileAdmin)