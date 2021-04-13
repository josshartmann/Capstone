from django.contrib import admin
from .models import User, ShouldIEat


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")


class ShouldIEatAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "food", "calories", "weight")


admin.site.register(User, UserAdmin)
admin.site.register(ShouldIEat, ShouldIEatAdmin)