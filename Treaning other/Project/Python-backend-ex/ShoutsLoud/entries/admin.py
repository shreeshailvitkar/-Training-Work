from django.contrib import admin
from entries.models import UserData



# Register your models here.

@admin.register(UserData)
class EntryAdmin(admin.ModelAdmin):
    pass
