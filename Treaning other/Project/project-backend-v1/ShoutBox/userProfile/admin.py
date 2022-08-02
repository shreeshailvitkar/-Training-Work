from django.contrib import admin
from userProfile.models import UserManager, User

# Register your models here.


@admin.register(UserManager)
class UserManager(admin.ModelAdmin):
    pass

@admin.register(User)
class User(admin.ModelAdmin):
    pass
