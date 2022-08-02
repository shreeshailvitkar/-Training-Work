from django.contrib import admin
from usersProfile.models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass
