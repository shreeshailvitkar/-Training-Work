from operator import mod
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.team_name

class Batsman(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    run = models.IntegerField(blank=True,null=True)
    bowls = models.IntegerField(blank=True,null=True)
    date_of_joining = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Bowler(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )
    wicket = models.IntegerField(blank=True,null=True)
    bowls = models.IntegerField(blank=True,null=True)
    date_of_joining = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


