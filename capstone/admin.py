from django.contrib import admin
from .models import User, ShouldIEat, Quotes


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")


class ShouldIEatAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "food", "calories", "weight")


class QuotesAdmin(admin.ModelAdmin):
    list_display = ("id", "quote", "author")


admin.site.register(User, UserAdmin)
admin.site.register(ShouldIEat, ShouldIEatAdmin)
admin.site.register(Quotes, QuotesAdmin)