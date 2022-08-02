
from django.contrib import admin
from cricket.models import (
    Team,
    Batsman,
    Bowler
)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
   pass

@admin.register(Batsman)
class BatsmanAdmin(admin.ModelAdmin):
   pass

@admin.register(Bowler)
class BowlerAdmin(admin.ModelAdmin):
   pass