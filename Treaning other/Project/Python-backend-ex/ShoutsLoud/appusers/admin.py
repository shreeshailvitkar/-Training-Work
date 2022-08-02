from django.contrib import admin
from appusers.models import FriendRequest, Profile
# Register your models here.

@admin.register(FriendRequest)
class FriendRequest(admin.ModelAdmin):
    pass

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    pass

